# Bacterial Metagenomics Classification

These notebooks detail training taxonomic classification models based on simulated sequencing data. The data used comes from the paper 
[Deep learning models for bacteria taxonomic classification of metagenomic data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6069770/) by 
Fiannaca et al. The dataset is available at [this repo](https://github.com/IcarPA-TBlab/MetagenomicDC).

The dataset is composed of simulated sequencing data from the 16S hypervariable region of 100 bacterial species. There are two simulated 
datasets - one for amplicon sequencing and one for shotgun short-read sequencing. For more information on construction of the dataset, see 
the linked repo.

Notebook __0__ shows preparation of the amplicon and shotgun sequence datasets

Notebook __1__ shows training a classification model on the amplicon dataset using a 5-mer stride 2 model

Notebook __2__ shows training a classification model on the amplicon dataset using a 5-mer stride 1 model

Notebook __3__ shows training a classification model on the shotgun dataset using a 5-mer stride 2 model

Notebook __4__ shows training a classification model on the shotgun dataset using a 5-mer stride 1 model

### Effect of stride

Stride was an especially important hyperparameter for the shotgun dataset

| Dataset  	| kmer/stride 	| Accuracy 	| Precision 	| Recall 	| F1    	|
|----------	|-------------	|----------	|-----------	|--------	|-------	|
| Amplicon 	| 5/2         	| .9144    	| __.9369__     	| .9250  	| .9214 	|
| Amplicon 	| 5/1         	| __.9150__    	| .9309     	| __.9263__  	| __.9230__ 	|
| Shotgun  	| 5/2         	| .8075    	| .8102     	| .8054  	| .8044 	|
| Shotgun  	| 5/1         	| __.8528__    	| __.8631__     	| __.8566__  	| __.8569__ 	|

### Results Summary

| Method          	| Data Source 	| Accuracy 	| Precision 	| Recall 	| F1    	|
|-----------------	|-------------	|----------	|-----------	|--------	|-------	|
| Fiannaca et al. 	| Amplicon    	| .9137    	| .9162     	| .9137  	| .9126 	|
| Genomic-ULMFiT  	| Amplicon    	| __.9150__    	| __.9309__     	| __.9263__  	| __.9230__ 	|
| Fiannaca et al. 	| Shotgun     	| .8550    	| .8570     	| .8520  	| .8511 	|
| Genomic-ULMFiT  	| Shotgun     	| __.8582__    	| __.8631__     	| __.8566__  	| __.8569__ 	|

Genomic-ULMFiT performed better on both datasets in all metrics, but only by a small margin.
