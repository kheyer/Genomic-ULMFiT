# Genomic ULMFiT

This is an implementation of [ULMFiT](https://arxiv.org/abs/1801.06146) for genomics classification using Pytorch and Fastai.

The ULMFiT approach uses three training phases to produce a classification model:
  1. Train a language model on a large, unlabeled corpus
  2. Fine tune the language model on the classification corpus
  3. Use the fine tuned language model to initialize a classification model
  
This method is particularly advantageous for genomic data, where large amounts of unlabeled data is abundant and labeled data is scarce. The ULMFiT approach allows us to train a model on a large, unlabeled genomic corpus in an unsupervised fashion. The pre-trained language model serves as a feature extractor for parsing genomic data.

Typical deep learning approaches to genomics classification are highly restricted to whatever labeled data is available. Models are usually trained from scratch on small datasets, leading to problems with overfitting. When unsupervised pre-training is used, it is typically done only on the classification dataset or on synthetically generated data. The Genomic-ULMFiT approach uses genome scale corpuses for pretraining to produce better feature extractors than we would get by training only on the classification corpus.

This method is still in development, but here are some preliminary results, both positive and negative:

#### Promoter Classification

The Genomic-ULMFiT method performs well at the task of classifying promoter sequences from random sections of the genome. The process of unsupervised pretraining and fine-tuning has a clear impact on the performance of the classification model

  | Model                        	| Accuracy 	| Precision 	| Recall 	| Correlation Coefficient 	|
  |------------------------------	|:--------:	|:---------:	|:------:	|:-----------------------:	|
  | Naive                        	|   0.834  	|   0.847   	|  0.816 	|          0.670          	|
  | E. coli genome pretraining   	|   0.919  	|   0.941   	|  0.893 	|          0.839          	|
  | Genomic ensemble pretraining 	|   0.973  	|   0.980   	|  0.966 	|          0.947          	|
  
  Classification performance on human promoters is competitive with published results
  
  For the short promoter sequences:

| Model                            	| DNA Size 	| Accuracy 	| Precision 	| Recall 	| Correlation Coefficient 	| Specificity 	|
|----------------------------------	|----------	|----------	|-----------	|--------	|-------------------------	|-------------	|
| Kh et al.                        	| -200/50  	|     -    	|     -     	|   0.9  	|           0.89          	|     __0.98__    	|
| Naive Model                      	| -200/50  	|   0.80   	|    0.74   	|  0.80  	|           0.59          	|     0.80    	|
| With Pretraining                 	| -200/50  	|   0.922  	|   __0.963__   	|  0.849 	|          0.844          	|    0.976    	|
| With Pretraining and Fine Tuning 	| -200/50  	|   __.977__   	|    .959   	|  __.989__  	|           __.955__          	|     .969    	|

For the long promoter sequences:

| Model                            	| DNA Size  	| Models           	| Accuracy 	| Precision 	| Recall 	| Correlation Coefficient 	|
|----------------------------------	|-----------	|------------------	|----------	|-----------	|--------	|-------------------------	|
| Umarov et al.                    	| -1000/500 	| 2 Model Ensemble 	|     -    	|   0.636   	|  0.802 	|          0.714          	|
| Umarov et al.                    	|  -200/400 	| 2 Model Ensemble 	|     -    	|   0.769   	|  0.755 	|          0.762          	|
| Naive Model                      	|  -500/500 	|   Single Model   	|   0.858  	|   0.877   	|  0.772 	|          0.708          	|
| With Pretraining                 	|  -500/500 	|   Single Model   	|   0.888  	|    __0.90__   	|  0.824 	|          0.770          	|
| With Pretraining and Fine Tuning 	|  -500/500 	|   Single Model   	|   __0.892__  	|   0.877   	|  __0.865__ 	|          __0.778__          	|

When training on really small datasets, CNN based methods can sometimes perform better.

| Method         	| Organism    	| Training Examples 	| Accuracy 	| Precision 	| Recall 	| Correlation Coefficient 	| Specificity 	|
|----------------	|-------------	|-------------------	|----------	|-----------	|--------	|-------------------------	|-------------	|
| Kh. et al.     	| E. coli     	|        2936       	|     -    	|     -     	|  __0.90__  	|           0.84          	|     0.96    	|
| Genomic-ULMFiT 	| E. coli     	|        2936       	|   0.956  	|   0.917   	|  0.880 	|          __0.871__          	|    __0.977__    	|
| Kh. et al.     	| B. subtilis 	|        1050       	|     -    	|     -     	|  __0.91__  	|           __0.86__          	|     0.95    	|
| Genomic-ULMFiT 	| B. subtilis 	|        1050       	|   0.905  	|   0.857   	|  0.789 	|          0.759          	|     0.95    	|

#### Enhancer Classification

Enhancer classification with Genomic-ULMFiT has proven difficult. Work on this domain is ongoing.

| Model                	| Human 	| Mouse 	|  Dog  	| Opossum 	|
|----------------------	|:-----:	|:-----:	|:-----:	|:-------:	|
| Cohn et al.          	| __0.975__ 	| __0.965__ 	| __0.963__ 	|  __0.946__  	|
| 4-mer Genomic-ULMFiT 	| 0.809 	| 0.863 	| 0.790 	|  0.799  	|
| 5-mer Genomic-ULMFiT 	| 0.801 	| 0.861 	| 0.784 	|  0.796  	|


### Upcoming Experiments

There are a number of other genomic classification domains I intend to explore when time permits.
  * Metagenomic Classification
  * CRISPR guide scoring
  * Classification from raw NGS data
  
### Relevant Literature

I'm planning on doing a more structured literature review of deep learning for genomic classification and how they compare to Genomic_ULMFiT. For now, here are links to relevant papers.

[DeepCRISPR: optimized CRISPR guide RNA design by deep learning](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6020378/)

[Recognition of prokaryotic and eukaryotic promoters using convolutional deep learning neural networks](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0171410)

[PromID: human promoter prediction by deep learning](https://arxiv.org/pdf/1810.01414.pdf)

[Deep Learning for Genomics: A Concise Overview](https://arxiv.org/pdf/1802.00810.pdf)

[Prediction of deleterious mutations in coding regions of mammals with transfer learning](https://onlinelibrary.wiley.com/doi/full/10.1111/eva.12607)

[Enhancer Identification using Transfer and Adversarial Deep Learning of DNA Sequences](https://www.biorxiv.org/content/biorxiv/early/2018/02/14/264200.full.pdf)

[PEDLA: predicting enhancers with a deep learning-based algorithmic framework](https://www.nature.com/articles/srep28517)

[Predicting enhancers with deep convolutional neural networks](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5773911/)

[BiRen: predicting enhancers with a deep-learning-based model using the DNA sequence alone](https://academic.oup.com/bioinformatics/article/33/13/1930/3002766)

[Deep learning models for bacteria taxonomic classification of metagenomic data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6069770/)

[Prediction of enhancer-promoter interactions via natural language processing](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5954283/)

[A deep recurrent neural network discovers complex biological rules to decipher RNA protein-coding potential](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6144860/)

[Recurrent Neural Network for Predicting Transcription Factor Binding Sites](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6189047/)

[Learning the Language of the Genome using RNNs](https://cs224d.stanford.edu/reports/jessesz.pdf)
