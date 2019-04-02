# Human lncRNA Classification

These notebooks look at training a classification model to distinguish between human coding mRNA sequences and long noncoding RNA (lncRNA) 
sequences following the Genomic ULMFiT approach. This dataset comes from the paper 
[A deep recurrent neural network discovers complex biological rules to decipher RNA protein-coding potential](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6144860/) 
by Hill et al. and is available for download [here](https://osf.io/4htpy/). 

The dataset contains two test sets - a standard test set of 1000 sequences and a challenge test set 1000 sequences. The regular test set contains standard mRNA and lncRNA sequences. The challenge test set contains mRNA sequences with short CDSs and lncRNAs with long untranslated ORFs.

__lncRNA 0__ shows the data processing steps

__lncRNA 1__ shows training the classification model using Genomic ULMFiT and inference on the two test sets.

Results compared to Hill et al.:

| Model                          	| Test Set           	| Accuracy 	| Specificity 	| Sensitivity 	| Precision 	| MCC   	|
|--------------------------------	|--------------------	|----------	|-------------	|-------------	|-----------	|-------	|
| GRU Ensemble (Hill et al.)*    	| Standard Test Set  	|   0.96   	|     __0.97__    	|     0.95    	|    __0.97__   	|  0.92 	|
| Genomic ULMFiT (3mer stride 1) 	| Standard Test Set  	|   __0.963__  	|    0.952    	|    __0.974__    	|   0.953   	| __0.926__ 	|
| GRU Ensemble (Hill et al.)*    	| Challenge Test Set 	|   0.875  	|     __0.95__    	|     0.80    	|    __0.95__   	|  0.75 	|
| Genomic ULMFiT (3mer stride 1) 	| Challenge Test Set 	|   __0.90__   	|    0.944    	|    __0.871__    	|   0.939   	| __0.817__ 	|

(*) Hill et al. presented their results as a plot rather than as a data table. Values in the above table are estimated by reading off the plot

The GRU by Hill et al. shows slightly higher specificity and precision, but Genomic ULMFiT produces a model with much better sensitivity. 
