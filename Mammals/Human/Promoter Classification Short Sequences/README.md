# Human Promoter Classification with Short Sequences

This series of notebooks looks at training human promoter classification models for short sequences following the ULMFiT approach. Short here 
is defined as -200/50 relative to known TSS sites. The dataset used comes from the paper [Recognition of Prokaryotic and Eukaryotic Promoters using Convolutional Deep Learning Neural Networks](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0171410)
by Kh. et al., downloaded from [this repo](https://github.com/solovictor/CNNPromoterData). 
Notebook __0__ details preparation of the dataset.

The notebooks in this folder look at training a classification model using the different stages of the ULMFiT process. 

Notebook __1__ trains a naive baseline model. This model trains from scratch using only the promoter sequences dataset.

Notebook __2__ trains the classification model initialized with a pretrained [human genome language model](https://github.com/kheyer/Genomic-ULMFiT/tree/master/Mammals/Human/Genomic%20Language%20Models).

Notebook __3__ first fine tunes the human genome language model on the promoter corpus, then trains a classification model intitialized with 
the fine tuned language model.

The results of these notebooks are compared to the results from Kh. et al.:

| Model                            	| DNA Size 	| Accuracy 	| Precision 	| Recall 	| Correlation Coefficient 	| Specificity 	|
|----------------------------------	|----------	|----------	|-----------	|--------	|-------------------------	|-------------	|
| Kh et al.                        	| -200/50  	|     -    	|     -     	|   0.9  	|           0.89          	|     __0.98__    	|
| Naive Model                      	| -200/50  	|   0.80   	|    0.74   	|  0.80  	|           0.59          	|     0.80    	|
| With Pretraining                 	| -200/50  	|   0.922  	|   __0.963__   	|  0.849 	|          0.844          	|    0.976    	|
| With Pretraining and Fine Tuning 	| -200/50  	|   __.977__   	|    .959   	|  __.989__  	|           __.955__          	|     .969    	|
