# Bacterial Ensemble Notebooks

These notebooks detail training classification models for bacterial genomic data using the ULMFiT approach. These notebooks assume you 
are already familiar with the technique as applied to genomic data. If you are not, see the [E. coli Notebook Series](https://github.com/kheyer/Genomic-ULMFiT/tree/master/Bacteria/E.%20Coli) 
for more detail about the specifics behind data processing, model architecture and training.

__Genomic Language Models__ contains notebooks detailing training the bacterial genomic language model using an ensemble of bacterial genomes as input data. Information on the different bacterial species used can be found in the data processing notebook. This directory also details training the language model used as the basis for an E. coli promoter classification model, detailed in the [E. coli 3 Bacterial Ensemble Pretraining](https://github.com/kheyer/Genomic-ULMFiT/blob/master/Bacteria/E.%20Coli/E.%20coli%203%20Bacterial%20Ensemble%20Pretraining.ipynb) notebook. 

__Promoter Classification__ contains notebooks training classification models for bacterial promoters. This directory includes a notebook comparing performance of Genomic-ULMFiT to a CNN-based method used by Kh et al in [Recognition of prokaryotic and eukaryotic promoters using convolutional deep learning neural networks](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0171410).

__Metagenomics Classification__ contains notebooks training metagenomic classification models in a comparison to [Deep learning models for bacteria taxonomic classification of metagenomic data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6069770/) by Fiannaca et al.

## Results Summary

#### Promoter Classification

| Method         	| Organism    	| Training Examples 	| Accuracy 	| Precision 	| Recall 	| Correlation Coefficient 	| Specificity 	|
|----------------	|-------------	|-------------------	|----------	|-----------	|--------	|-------------------------	|-------------	|
| Kh. et al.     	| E. coli     	|        2936       	|     -    	|     -     	|  __0.90__  	|           0.84          	|     0.96    	|
| Genomic-ULMFiT 	| E. coli     	|        2936       	|   0.956  	|   0.917   	|  0.880 	|          __0.871__          	|    __0.977__    	|
| Kh. et al.     	| B. subtilis 	|        1050       	|     -    	|     -     	|  __0.91__  	|           __0.86__          	|     0.95    	|
| Genomic-ULMFiT 	| B. subtilis 	|        1050       	|   0.905  	|   0.857   	|  0.789 	|          0.759          	|     0.95    	|


#### Metagenomics Classification

Work ongoing
