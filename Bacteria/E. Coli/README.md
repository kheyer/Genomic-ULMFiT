# E. coli Promoter Classification Notebooks

These notebooks detail using the ULMFiT method to train a promoter classifier based on genetic sequences extracted from the E. coli genome.

The ULMFiT process consists of several stages. First a language model is trained in an unsupervised fashion, using a string of tokens 
as input to predict the next token. Then a classification model is initialized with the pretrained weights from the language model.

These notebooks build up to this final procedure in several steps. In __E. coli 1__ we train a model using only the classification 
dataset - no pretraining. In __E. coli 2__ we train a language model on the E. coli genome. We then transfer the weights from the 
language model to the classification model. In __E. coli 3__ we use a much larger genomic corpus from several species of bacteria to 
train a better language model as the basis for the classification model. Progressing through this sequence of 
models shows the impact of both unsupervised pretraining in general and the quality of the initial language model. These are the results 
of the three models on the same test dataset:

  | Model                        	| Accuracy 	| Precision 	| Recall 	| Correlation Coefficient 	|
  |------------------------------	|:--------:	|:---------:	|:------:	|:-----------------------:	|
  | Naive                        	|   0.834  	|   0.847   	|  0.816 	|          0.670          	|
  | E. coli genome pretraining   	|   0.919  	|   0.941   	|  0.893 	|          0.839          	|
  | Genomic ensemble pretraining 	|   0.973  	|   0.980   	|  0.966 	|          0.947          	|

In __E. coli 4__ we reduce the amount of classification data used to see the impact on model performance. This method is robust to small 
datasets. A classification model initialized with the weights of the multi-genome language model and trained on just 20 examples performs 
the same as the naive model (no pretraining) trained on over 6000 training examples.

![data](https://github.com/kheyer/Genomic-ULMFiT/blob/master/Bacteria/E.%20Coli/Media/data_reduction.png)
