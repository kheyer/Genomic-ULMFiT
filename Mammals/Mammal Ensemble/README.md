# Mammalian Genome Notebooks

These notebooks detail training classification models based on mammalian genomes using the ULMFiT approach. These notebooks assume you 
are already familiar with the technique as applied to genomic data. If you are not, see the [E. coli Notebook Series](https://github.com/kheyer/Genomic-ULMFiT/tree/master/Bacteria/E.%20Coli) 
for more detail about the specifics behind data processing, model architecture and training.

__Genomic Language Models__ contains notebooks detailing training different variants of the mammalian genomic language model.

__Enhancer Classification__ details training classification models on enhancer sequences from various mammalian species

#### Some notes on the datasets used

The enhancer dataset used comes from the paper [Enhancer Identification using Transfer and Adversarial Deep Learning of DNA Sequences](https://www.biorxiv.org/content/biorxiv/early/2018/02/14/264200.full.pdf) 
by Cohn et al. The dataset can be downloaded from the [Enhancer CNN](https://github.com/cohnDikla/enhancer_CNN) repo. Positive examples are 
500 bp sequences defined as genomic regions showing in vivo binding by a single transcription factor, or distal genomic regions enriched for 
H3K27ac. Negative examples are genomic regions showing no H3K27ac marks.

## Results and Comparisons

Genomic-ULMFiT shows improved results over Cohn. et al.

| Model/ROC-AUC                 	| Human 	| Mouse 	|  Dog  	| Opossum 	|
|-------------------------------	|:-----:	|:-----:	|:-----:	|:-------:	|
| Cohn et al.                   	|  0.80 	|  0.78 	|  0.77 	|   0.72  	|
| Genomic-ULMFiT 5-mer Stride 2 	| 0.812 	| 0.871 	| 0.773 	|  0.787  	|
| Genomic-ULMFiT 4-mer Stride 2 	| 0.804 	| __0.876__ 	| 0.771 	|  0.786  	|
| Genomic-ULMFiT 3-mer Stride 1 	| __0.819__ 	| 0.875 	| __0.788__ 	|  __0.798__  	|

Here are more detailed metrics for the Genomic-ULMFiT models:

| Organism/Model 	|           	| 4-mer stride 2 	| 5-mer stride 2 	| 3-mer stride 1 	|
|----------------	|-----------	|----------------	|----------------	|----------------	|
| Human          	| Accuracy  	|      .733      	|      .726      	|      .736      	|
|                	| Precision 	|      .716      	|      .717      	|      .719      	|
|                	| Recall    	|      .771      	|      .745      	|      .775      	|
| Mouse          	| Accuracy  	|      .795      	|      .792      	|      .800      	|
|                	| Precision 	|      .786      	|      .802      	|      .789      	|
|                	| Recall    	|      .810      	|      .774      	|      .819      	|
| Dog            	| Accuracy  	|      .706      	|      .704      	|      .716      	|
|                	| Precision 	|      .688      	|      .703      	|      .722      	|
|                	| Recall    	|      .753      	|      .706      	|      .705      	|
| Opossum        	| Accuracy  	|      .711      	|      .708      	|      .724      	|
|                	| Precision 	|      .712      	|      .715      	|      .733      	|
|                	| Recall    	|      .707      	|      .691      	|      .705      	|