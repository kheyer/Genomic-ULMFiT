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

The Genomic-ULMFiT process performed poorly on the enhancer dataset. Work on improving performance is ongoing.

| Model                	| Human 	| Mouse 	|  Dog  	| Opossum 	|
|----------------------	|:-----:	|:-----:	|:-----:	|:-------:	|
| Cohn et al.          	| __0.975__ 	| __0.965__ 	| __0.963__ 	|  __0.946__  	|
| 4-mer Genomic-ULMFiT 	| 0.809 	| 0.863 	| 0.790 	|  0.799  	|
| 5-mer Genomic-ULMFiT 	| 0.801 	| 0.861 	| 0.784 	|  0.796  	|
