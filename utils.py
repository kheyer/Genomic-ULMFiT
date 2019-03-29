from fastai import *
from fastai.text import *
from Bio import Seq
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import FeatureLocation, CompoundLocation
import networkx as nx

def process_fasta(fname, c1, c2, filter_txt=None):
    genome = SeqIO.parse(fname, 'fasta')
    if filter_txt:
        chroms = [GB for GB in genome if 'NC_' in GB.id]
    else:
        chroms = [GB for GB in genome]
    genome = ''.join([i.seq.__str__() for i in chroms]).upper()
    genome_chunks = [genome[i:i+c1] for i in range(0, len(genome), c1) if not 'N' in genome[i:i+c1] and set(genome[i:i+c1])==set('ATGC')]
    clean_genome = ''.join(genome_chunks)
    data = [clean_genome[i:i+c2] for i in range(0, len(clean_genome), c2)]
    
    return data

def split_data(df, pct):
    cut = int(len(df)*pct) + 1
    df_t = df[:cut]
    df_v = df[cut:]
    
    return (df_t, df_v)

class GenomicTokenizer(BaseTokenizer):
    def __init__(self, lang='en', ngram=5, stride=2):
        self.lang = lang
        self.ngram = ngram
        self.stride = stride
        
    def tokenizer(self, t):
        t = t.upper()
        if self.ngram == 1:
            toks = list(t)
        else:
            toks = [t[i:i+self.ngram] for i in range(0, len(t), self.stride) if len(t[i:i+self.ngram]) == self.ngram]
        if len(toks[-1]) < self.ngram:
            toks = toks[:-1]
        
        return toks
    
    def add_special_cases(self, toks):
        pass

class GenomicVocab(Vocab):
    def __init__(self, itos):
        self.itos = itos
        self.stoi = collections.defaultdict(int,{v:k for k,v in enumerate(self.itos)})
        
    @classmethod
    def create(cls, tokens, max_vocab, min_freq):
        freq = Counter(p for o in tokens for p in o)
        itos = [o for o,c in freq.most_common(max_vocab) if c >= min_freq]
        itos.insert(0, 'pad')
        return cls(itos)

class GenomicNumericalizeProcessor(PreProcessor):
    "`PreProcessor` that numericalizes the tokens in `ds`."
    def __init__(self, ds:ItemList=None, vocab:Vocab=None, max_vocab:int=60000, min_freq:int=3):
        vocab = ifnone(vocab, ds.vocab if ds is not None else None)
        self.vocab,self.max_vocab,self.min_freq = vocab,max_vocab,min_freq

    def process_one(self,item): return np.array(self.vocab.numericalize(item), dtype=np.int64)
    def process(self, ds):
        if self.vocab is None: self.vocab = GenomicVocab.create(ds.items, self.max_vocab, self.min_freq)
        ds.vocab = self.vocab
        super().process(ds)

def _genomic_join_texts(texts:Collection[str], mark_fields:bool=False):
    if not isinstance(texts, np.ndarray): texts = np.array(texts)
    if is1d(texts): texts = texts[:,None]
    df = pd.DataFrame({i:texts[:,i] for i in range(texts.shape[1])})
    text_col = f'{BOS} {FLD} {1} ' + df[0].astype(str) if mark_fields else  '' + df[0].astype(str)
    for i in range(1,len(df.columns)):
        text_col += (f' {FLD} {i+1} ' if mark_fields else ' ') + df[i].astype(str)   
    return text_col.values

class GenomicTokenizeProcessor(PreProcessor):
    "`PreProcessor` that tokenizes the texts in `ds`."
    def __init__(self, ds:ItemList=None, tokenizer:Tokenizer=None, chunksize:int=10000, mark_fields:bool=False):
        self.tokenizer,self.chunksize,self.mark_fields = ifnone(tokenizer, Tokenizer()),chunksize,mark_fields

    def process_one(self, item):  
        return self.tokenizer._process_all_1(_genomic_join_texts([item], self.mark_fields))[0]
    
    def process(self, ds):
        ds.items = _genomic_join_texts(ds.items, self.mark_fields)
        tokens = []
        for i in range(0,len(ds),self.chunksize):
            tokens += self.tokenizer.process_all(ds.items[i:i+self.chunksize])
        ds.items = tokens

def _get_genomic_processor(tokenizer:Tokenizer=None, vocab:Vocab=None, chunksize:int=10000, max_vocab:int=60000,
                   min_freq:int=2, mark_fields:bool=False):
    return [GenomicTokenizeProcessor(tokenizer=tokenizer, chunksize=chunksize, mark_fields=mark_fields),
            GenomicNumericalizeProcessor(vocab=vocab, max_vocab=max_vocab, min_freq=min_freq)]

class GenomicTextLMDataBunch(TextLMDataBunch):
    @classmethod
    def from_df(cls, path:PathOrStr, train_df:DataFrame, valid_df:DataFrame, test_df:Optional[DataFrame]=None,
                tokenizer:Tokenizer=None, vocab:Vocab=None, classes:Collection[str]=None, text_cols:IntsOrStrs=1,
                label_cols:IntsOrStrs=0, label_delim:str=None, chunksize:int=10000, max_vocab:int=60000,
                min_freq:int=2, mark_fields:bool=False, bptt=70, collate_fn:Callable=data_collate, bs=64, **kwargs):
        "Create a `TextDataBunch` from DataFrames. `kwargs` are passed to the dataloader creation."
        processor = _get_genomic_processor(tokenizer=tokenizer, vocab=vocab, chunksize=chunksize, max_vocab=max_vocab,
                                   min_freq=min_freq, mark_fields=mark_fields)
        if classes is None and is_listy(label_cols) and len(label_cols) > 1: classes = label_cols
        src = ItemLists(path, TextList.from_df(train_df, path, cols=text_cols, processor=processor),
                        TextList.from_df(valid_df, path, cols=text_cols, processor=processor))
        src = src.label_for_lm() 
        if test_df is not None: src.add_test(TextList.from_df(test_df, path, cols=text_cols))
        d1 = src.databunch(**kwargs)
        
        datasets = cls._init_ds(d1.train_ds, d1.valid_ds, d1.test_ds)            
        val_bs = bs
        datasets = [LanguageModelPreLoader(ds, shuffle=(i==0), bs=(bs if i==0 else val_bs), bptt=bptt, backwards=False) 
                    for i,ds in enumerate(datasets)]            
        dls = [DataLoader(d, b, shuffle=False) for d,b in zip(datasets, (bs,val_bs,val_bs,val_bs)) if d is not None]
        
        return cls(*dls, path=path, collate_fn=collate_fn, no_check=False)

class GenomicTextClasDataBunch(TextClasDataBunch):
    @classmethod
    def from_df(cls, path:PathOrStr, train_df:DataFrame, valid_df:DataFrame, test_df:Optional[DataFrame]=None,
                tokenizer:Tokenizer=None, vocab:Vocab=None, classes:Collection[str]=None, text_cols:IntsOrStrs=1,
                label_cols:IntsOrStrs=0, label_delim:str=None, chunksize:int=10000, max_vocab:int=60000,
                min_freq:int=2, mark_fields:bool=False, pad_idx=0, pad_first=True, bs=64, **kwargs) -> DataBunch:
        "Create a `TextDataBunch` from DataFrames. `kwargs` are passed to the dataloader creation."
        processor = _get_genomic_processor(tokenizer=tokenizer, vocab=vocab, chunksize=chunksize, max_vocab=max_vocab,
                                   min_freq=min_freq, mark_fields=mark_fields)
        if classes is None and is_listy(label_cols) and len(label_cols) > 1: classes = label_cols
        src = ItemLists(path, TextList.from_df(train_df, path, cols=text_cols, processor=processor),
                        TextList.from_df(valid_df, path, cols=text_cols, processor=processor))
        src = src.label_from_df(cols=label_cols, classes=classes, label_delim=label_delim)
        if test_df is not None: src.add_test(TextList.from_df(test_df, path, cols=text_cols))
        d1 = src.databunch(**kwargs)
        
        datasets = cls._init_ds(d1.train_ds, d1.valid_ds, d1.test_ds)
        collate_fn = partial(pad_collate, pad_idx=pad_idx, pad_first=pad_first, backwards=False)
        train_sampler = SortishSampler(datasets[0].x, key=lambda t: len(datasets[0][t][0].data), bs=bs//2)
        train_dl = DataLoader(datasets[0], batch_size=bs, sampler=train_sampler, drop_last=True, **kwargs)
        dataloaders = [train_dl]
        for ds in datasets[1:]:
            lengths = [len(t) for t in ds.x.items]
            sampler = SortSampler(ds.x, key=lengths.__getitem__)
            dataloaders.append(DataLoader(ds, batch_size=bs, sampler=sampler, **kwargs))
            
        return cls(*dataloaders, path=path, collate_fn=collate_fn)


def get_scores(learn, ret=False):
    preds = learn.get_preds(ordered=True)
    p = torch.argmax(preds[0], dim=1)
    y = preds[1]
    tp = ((p + y) == 2).sum().item()
    tn = ((p + y) == 0).sum().item()
    fp = (p > y).sum().item()
    fn = (p < y).sum().item()
    cc = (float(tp)*tn - fp*fn) / np.sqrt((tp + fp)*(tp + fn)*(tn + fp)*(tn + fn))
    
    print(f'Accuracy: {(tp+tn)/len(y)}')
    print(f'False Positives: {fp/len(y)}')
    print(f'False Negatives: {fn/len(y)}')
    print(f'Recall: {tp / (tp + fn)}')
    print(f'Precision: {tp / (tp + fp)}')
    print(f'Specificity: {tn / (tn + fp)}')
    print(f'MCC: {cc}')

    if ret:
        return preds

def get_model_LM(data, drop_mult, config, wd=1e-2):
    vocab_size = len(data.vocab.stoi)
    for k in config.keys(): 
        if k.endswith('_p'): config[k] *= drop_mult
            
    tie_weights,output_p,out_bias = map(config.pop, ['tie_weights', 'output_p', 'out_bias'])
    encoder = AWD_LSTM(vocab_size, **config)
    enc = encoder.encoder
    emb_sz = config['emb_sz']
    decoder = LinearDecoder(vocab_size, emb_sz, output_p, tie_encoder=enc, bias=True)
    model = SequentialRNN(encoder, decoder)
    learn = LanguageLearner(data, model, split_func=awd_lstm_lm_split, wd=wd)
    
    return learn

def get_model_clas(data, drop_mult, config, lin_ftrs=None, ps=None, bptt=70, max_len=20*70, wd=1e-2):
    n_class = data.c
    vocab_size = len(data.vocab.stoi)
    for k in config.keys(): 
        if k.endswith('_p'): config[k] *= drop_mult
    
    if lin_ftrs is None: lin_ftrs = [50]
    if ps is None:  ps = [0.1]
    emb_sz = config['emb_sz']
    layers = [emb_sz * 3] + lin_ftrs + [n_class]
    ps = [config.pop('output_p')] + ps
    encoder = MultiBatchEncoder(bptt, max_len, AWD_LSTM(vocab_size, **config))
    model = SequentialRNN(encoder, PoolingLinearClassifier(layers, ps))
    
    learn = RNNLearner(data, model, split_func=awd_lstm_clas_split, wd=wd)
    
    return learn


class SequenceShuffler():
    def __init__(self, sequence, lengths, sequence_class, tss_loc=None, inserts=None, gen_rand=False):
        
        if inserts is not None:
            assert len(lengths) == len(inserts), "Number of inserts should match number of kmer lengths"
            assert all(len(inserts[i]) == lengths[i] for i in range(len(lengths))), "Each insert kmer must match kmer length list"
        
        self.inserts = inserts
        self.sequence = sequence
        self.lengths = lengths
        self.sequence_class = sequence_class
        self.gen_rand = gen_rand
        self.tss_loc = tss_loc
        self.get_dfs()

    def rand_sequence(self, length):
        return ''.join(random.choice('CGTA') for _ in range(length))
    
    def shuffle_section(self, length, idx):
        if self.const_insert:
            insert = self.const_insert
        else:
            insert = self.rand_sequence(length)
            
        return (''.join([self.sequence[:idx], insert, self.sequence[idx+length:]]), insert)
    
    def get_shuffles(self, length):
        seqs = []
        idxs = []
        inserts = []

        for i in range(len(self.sequence)-length+1):
            seq, insert = self.shuffle_section(length, i)
            seqs.append(seq)
            inserts.append(insert)
            idxs.append(i)

        return (seqs, idxs, inserts)
    
    def get_shuffle_df(self, length):
        
        if self.inserts is not None:
            self.const_insert = self.inserts[self.lengths.index(length)]
        
        elif not self.gen_rand:
            self.const_insert = self.rand_sequence(length)
            
        else:
            self.const_insert = False
        
        seqs, idxs, inserts = self.get_shuffles(length)

        seq_df = pd.DataFrame(seqs, columns=['Sequence'])
        seq_df['length'] = length
        seq_df['position'] = idxs
        seq_df['insert'] = inserts

        return seq_df
    
    def get_dfs(self):
        self.df = pd.concat([self.get_shuffle_df(i) for i in self.lengths])
        self.df['Promoter'] = self.sequence_class
        
    def get_predictions(self, learner, path, train_df, tok, model_vocab):
        data = GenomicTextClasDataBunch.from_df(path, train_df, self.df, tokenizer=tok, vocab=model_vocab,
                                                    text_cols='Sequence', label_cols='Promoter', bs=300)
        learn.data = data
        preds = learn.get_preds(ordered=True)
        self.df['Prob'] = preds[0][:,1]
        
    def plot_results(self):
        plt.figure(figsize=(15,8))
        palette = sns.color_palette("mako_r", len(self.lengths))
        ax = sns.lineplot(x="position", y="Prob", data=self.df, hue='length', palette=palette)
        if self.tss_loc is not None:
            plt.axvline(self.tss_loc, color='r')

def plot_shuffle(idx, lengths, tss=None, inserts=None, gen_rand=False, ret=False):
    SeqShuffle = SequenceShuffler(classification_df.Sequence[idx], lengths, classification_df.Promoter[idx],
                                  tss_loc=tss, inserts=inserts, gen_rand=gen_rand)
    SeqShuffle.get_predictions(learn, path, train_df, tok, model_vocab)
    SeqShuffle.plot_results()
    
    if ret:
        return SeqShuffle