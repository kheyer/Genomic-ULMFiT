# Human Genome Notebooks

These notebooks detail training classification models for human promoter sequences using the ULMFiT approach. These notebooks assume you 
are already familiar with the technique as applied to genomic data. If you are not, see the [E. coli Notebook Series](https://github.com/kheyer/Genomic-ULMFiT/tree/master/Bacteria/E.%20Coli) 
for more detail about the specifics behind data processing, model architecture and training.

__Genomic Language Models__ contains notebooks detailing training different variants of the human genomic language model.

__Promoter Classification Long Sequences__ details training classification models on short (-200/50) sequences of human promoters. The 
short promoter dataset allows us to directly compare model performance to the paper [Recognition of prokaryotic and eukaryotic promoters using convolutional deep learning neural networks](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0171410). 
The authors of the paper host their data in this [repo](https://github.com/solovictor/CNNPromoterData).

__Promoter Classification Short Sequences__ details training classification models on long (-500/500) sequences of human promoters. The 
long promoters dataset allows us to compare the model to [PromID: human promoter prediction by deep learning](https://arxiv.org/pdf/1810.01414.pdf).

__lncRNA Classification__ details training a classification model on human coding mRNA and long noncoding RNA (lncRNA). The dataset used comes from the paper [A deep recurrent neural network discovers complex biological rules to decipher RNA protein-coding potential](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6144860/) by Hill et al. and is available for download [here](https://osf.io/4htpy/).

#### Some notes on the datasets used
In the short promoter paper, the authors use two separate datasets for promoters. One for promoters containing the `TATA` motif and one 
for promoters that don't. Only the non-tata dataset was hosted online, so only that data will be used for comparison.

The long promoters paper did not host their dataset online, but it is easily reproducible. Transcription Start Sites (TSS) are taken from 
the [EPDnew Database](ftp://ccg.vital-it.ch/epdnew/human/006/). Promoter sequences are taken from the region -500/500 from the TSS. Negative 
examples are taken randomly from genomic regions between TSS sites.

## Results and Comparisons

For the short promoter dataset:

| Model                            	| DNA Size 	| kmer/stride 	| Accuracy 	| Precision 	| Recall 	| Correlation Coefficient 	| Specificity 	|
|----------------------------------	|----------	|-------------	|----------	|-----------	|--------	|-------------------------	|-------------	|
| Kh et al.                        	| -200/50  	|      -      	|     -    	|     -     	|   0.9  	|           0.89          	|     0.98    	|
| Naive Model                      	| -200/50  	|     5/2     	|   0.80   	|    0.74   	|  0.80  	|           0.59          	|     0.80    	|
| With Pretraining                 	| -200/50  	|     5/2     	|   0.922  	|   0.963   	|  0.849 	|          0.844          	|    0.976    	|
| With Pretraining and Fine Tuning 	| -200/50  	|     5/2     	|   .977   	|    .959   	|  .989  	|           .955          	|     .969    	|
| With Pretraining and Fine Tuning 	| -200/50  	|     5/1     	|   .990   	|    .983   	|  .995  	|           .981          	|     .987    	|
| With Pretraining and Fine Tuning 	| -200/50  	|     3/1     	|   __.995__   	|    __.992__   	|  __.996__  	|           __.991__          	|     __.994__    	|


For the long promoter dataset:

| Model                            	| DNA Size  	| Models           	| Accuracy 	| Precision 	| Recall 	| Correlation Coefficient 	|
|----------------------------------	|-----------	|------------------	|----------	|-----------	|--------	|-------------------------	|
| Umarov et al.                    	| -1000/500 	| 2 Model Ensemble 	|     -    	|   0.636   	|  0.802 	|          0.714          	|
| Umarov et al.                    	|  -200/400 	| 2 Model Ensemble 	|     -    	|   0.769   	|  0.755 	|          0.762          	|
| Naive Model                      	|  -500/500 	|   Single Model   	|   0.858  	|   0.877   	|  0.772 	|          0.708          	|
| With Pretraining                 	|  -500/500 	|   Single Model   	|   0.888  	|    __0.90__   	|  0.824 	|          0.770          	|
| With Pretraining and Fine Tuning 	|  -500/500 	|   Single Model   	|   __0.892__  	|   0.877   	|  __0.865__ 	|          __0.778__          	|

For the lncRNA dataset:

| Model                          	| Test Set           	| Accuracy 	| Specificity 	| Sensitivity 	| MCC   	|
|--------------------------------	|--------------------	|----------	|-------------	|-------------	|-------	|
| GRU Ensemble (Hill et al.)*     | Standard Test Set  	|   0.96   	|     __0.97__    	|     0.95     	|  0.92 	|
| Genomic ULMFiT (3mer stride 1) 	| Standard Test Set  	|   __0.963__  	|    0.952    	|    __0.974__    	| __0.926__ 	|
| GRU Ensemble (Hill et al.)*     | Challenge Test Set 	|   0.875   	|     __0.95__    	|     0.80    	|  0.75 	|
| Genomic ULMFiT (3mer stride 1) 	| Challenge Test Set 	|   __0.90__   	|    0.944    	|    __0.871__    	| __0.817__ 	|

* Hill et al. presented their results as a plot rather than as a data table. Values in the above table are estimated by reading off the plot


