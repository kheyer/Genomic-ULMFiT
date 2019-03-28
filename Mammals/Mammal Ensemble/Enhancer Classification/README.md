# Mammalian Enhancer Classification

This series of notebooks details training an enhancer classification model following the ULMFiT approach. The dataset used comes from the 
paper [Enhancer Identification using Transfer and Adversarial Deep Learning of DNA Sequences](https://www.biorxiv.org/content/biorxiv/early/2018/02/14/264200.full.pdf) 
by Cohn et al. The dataset can be downloaded from the [Enhancer CNN](https://github.com/cohnDikla/enhancer_CNN) repo. Positive examples are 
500 bp sequences defined as having active enhancer marks (H3K27ac) in the liver. Negative examples are genomic regions showing no H3K27ac marks.

The data from Cohn et al. on this dataset is actually not presented in the paper itself, but put in the supplementary section, available [here](https://www.biorxiv.org/content/biorxiv/suppl/2018/02/14/264200.DC2/264200-1.pdf). The results below are compared to the author's results in supplementary Figure 3. (You have no idea how much time I sunk trying to replicate results from the paper itself before realizing the results I was trying to replicate came from a different dataset).

Classification models are trained on positive and negative sequences from Human, Mouse, Dog and Opossum genomes. Each species is modeled separately. To compare to Cohn et al., performance is measured via AUC-ROC score.

Notebook __0__ details preparation of the dataset

Notebook __1__ trains a classification model initialized with the 4-mer stride 2 mammalian genomic [language model](https://github.com/kheyer/Genomic-ULMFiT/blob/master/Mammals/Mammal%20Ensemble/Genomic%20Language%20Models/Mammals%20LM%202%204mer.ipynb)

Notebook __2__ trains a classification model initialized with the 5-mer stride 2 mammalian genomic [language model](https://github.com/kheyer/Genomic-ULMFiT/blob/master/Mammals/Mammal%20Ensemble/Genomic%20Language%20Models/Mammals%20LM%201%205mer.ipynb) 

Notebook __3__ trains a classification model initialized with the 3-mer stride 1 mammalian genomic [language model](https://github.com/kheyer/Genomic-ULMFiT/blob/master/Mammals/Mammal%20Ensemble/Genomic%20Language%20Models/Mammals%20LM%203%203m1s.ipynb)

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

