# Mammalian Enhancer Classification

This series of notebooks details training an enhancer classification model following the ULMFiT approach. The dataset used comes from the 
paper [Enhancer Identification using Transfer and Adversarial Deep Learning of DNA Sequences](https://www.biorxiv.org/content/biorxiv/early/2018/02/14/264200.full.pdf) 
by Cohn et al. The dataset can be downloaded from the [Enhancer CNN](https://github.com/cohnDikla/enhancer_CNN) repo. Positive examples are 
500 bp sequences defined as genomic regions showing in vivo binding by a single transcription factor, or distal genomic regions enriched for 
H3K27ac. Negative examples are genomic regions showing no H3K27ac marks.

The notebooks currently replicate one section of the paper. A classification model is trained on positive and negative sequences from Human, 
Mouse, Dog and Opossum genomes. The model is then used to predict on the test set on a per organism basis, with performance measured by 
ROC AUC score.

Notebook __0__ details preparation of the dataset

Notebook __1__ trains a classification model initialized with the 4-mer stride 2 mammalian genomic [language model](https://github.com/kheyer/Genomic-ULMFiT/blob/master/Mammals/Mammal%20Ensemble/Genomic%20Language%20Models/Mammals%20LM%202%204mer.ipynb)

Notebook __2__ trains a classification model initialized with the 5-mer stride 2 mammalian genomic [language model](https://github.com/kheyer/Genomic-ULMFiT/blob/master/Mammals/Mammal%20Ensemble/Genomic%20Language%20Models/Mammals%20LM%201%205mer.ipynb) 

The Genomic-ULMFiT approach performed poorly at this task, producing worse results than Cohn et al. 

| Model                	| Human 	| Mouse 	|  Dog  	| Opossum 	|
|----------------------	|:-----:	|:-----:	|:-----:	|:-------:	|
| Cohn et al.          	| __0.975__ 	| __0.965__ 	| __0.963__ 	|  __0.946__  	|
| 4-mer Genomic-ULMFiT 	| 0.809 	| 0.863 	| 0.790 	|  0.799  	|
| 5-mer Genomic-ULMFiT 	| 0.801 	| 0.861 	| 0.784 	|  0.796  	|

When time permits, I plan on investigating this further. For now, this appears to be an area in which the approach is ill suited.
