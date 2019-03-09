# Human Promoter Classification Notebooks

These notebooks detail training classification models for human promoter sequences using the ULMFiT approach. These notebooks assume you 
are already familiar with the technique as applied to genomic data. If you are not, see the [E. coli Notebook Series](https://github.com/kheyer/Genomic-ULMFiT/tree/master/Bacteria/E.%20Coli) 
for more detail about the specifics behind data processing, model architecture and training.

__Human 0__ details processing three datasets - the human genome language model dataset, the human promoters (short) dataset, and the 
human promoters (long) dataset. The short promoter dataset allows us to directly compare model performance to the paper 
[Recognition of prokaryotic and eukaryotic promoters using convolutional deep learning neural networks](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0171410). 
The authors of the paper host their data in this [repo](https://github.com/solovictor/CNNPromoterData). The long promoters dataset allows 
us to compare the model to [PromID: human promoter prediction by deep learning](https://arxiv.org/pdf/1810.01414.pdf).

#### Some notes on the datasets used
In the short promoter paper, the authors use two separate datasets for promoters. One for promoters containing the `TATA` motif and one 
for promoters that don't. Only the non-tata dataset was hosted online, so only that data will be used for comparison.

The long promoters paper did not host their dataset online, but it is easily reproducible. Transcription Start Sites (TSS) are taken from 
the [EPDnew Database](ftp://ccg.vital-it.ch/epdnew/human/006/). Promoter sequences are taken from the region -500/500 from the TSS. Negative 
examples are taken randomly from genomic regions between TSS sites.

__Human 1__ details baseline models for the short and long promoter datasets - no pretraining.

__Human 2__ details training a genomic language model on the human genome.

__Human 3__ details using the genomic language model to initialize a classification model trained on the short promoter dataset.

__Human 4__ details adding fine tuning to the model from __Human 3__, completing the full ULMFiT process.

__Human 5__ details using the genomic language model to initialize a classification model trained on the long promoter dataset.

## Results and Comparisons

For the short promoter dataset:

| Model                            	| DNA Size 	| Accuracy 	| Precision 	| Recall 	| Correlation Coefficient 	| Specificity 	|
|----------------------------------	|----------	|----------	|-----------	|--------	|-------------------------	|-------------	|
| Kh et al.                        	| -200/50  	|     -    	|     -     	|   0.9  	|           0.89          	|     __0.98__    	|
| Naive Model                      	| -200/50  	|   0.80   	|    0.74   	|  0.80  	|           0.59          	|     0.80    	|
| With Pretraining                 	| -200/50  	|   0.922  	|   __0.963__   	|  0.849 	|          0.844          	|    0.976    	|
| With Pretraining and Fine Tuning 	| -200/50  	|   __.977__   	|    .959   	|  __.989__  	|           __.955__          	|     .969    	|


For the long promoter dataset:

| Model            	| DNA Size  	| Models           	| Accuracy 	| Precision 	| Recall 	| Correlation Coefficient 	|
|------------------	|-----------	|------------------	|:--------:	|:---------:	|:------:	|:-----------------------:	|
| Umarov et al.    	| -1000/500 	| 2 Model Ensemble 	|     -    	|   0.636   	|  0.802 	|          0.714          	|
| Umarov et al.    	|  -200/400 	| 2 Model Ensemble 	|     -    	|   0.769   	|  0.755 	|          0.762          	|
| Naive Model      	|  -500/500 	| Single Model     	|   0.858  	|   0.877   	|  0.772 	|          0.708          	|
| With Pretraining 	|  -500/500 	| Single Model     	|   __0.888__  	|    __0.90__   	|  __0.824__ 	|          __0.770__          	|




