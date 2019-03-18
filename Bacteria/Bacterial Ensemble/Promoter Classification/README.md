# Bacterial Promoter Classification

These notebooks detail training promoter classification models based off the bacterial ensemble genomic language models.

__Bacterial Promoters 0__ details comparisons of promoter classification results between the Genomic-ULMFiT method and the method 
used in [Recognition of prokaryotic and eukaryotic promoters using convolutional deep learning neural networks](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0171410) 
by Kh. et al. Two models are trained - one for E. coli promoters and another for B. subtilis promoters. See the notebook for a more detailed 
comparison between methods and ananlysis of results.

#### Results Summary

| Method         	| Organism    	| Training Examples 	| Accuracy 	| Precision 	| Recall 	| Correlation Coefficient 	| Specificity 	|
|----------------	|-------------	|-------------------	|----------	|-----------	|--------	|-------------------------	|-------------	|
| Kh. et al.     	| E. coli     	|        2936       	|     -    	|     -     	|  __0.90__  	|           0.84          	|     0.96    	|
| Genomic-ULMFiT 	| E. coli     	|        2936       	|   0.956  	|   0.917   	|  0.880 	|          __0.871__          	|    __0.977__    	|
| Kh. et al.     	| B. subtilis 	|        1050       	|     -    	|     -     	|  __0.91__  	|           __0.86__          	|     0.95    	|
| Genomic-ULMFiT 	| B. subtilis 	|        1050       	|   0.905  	|   0.857   	|  0.789 	|          0.759          	|     0.95    	|

We see that when data is limited, CNN based methods perform better. However, with as few as 3000 labeled examples, LSTM based methods can reach comprable or superior performance to CNNs. I think this shows the advantage of using transfer learning and training on large, general genomic corpuses. I expect training a LSTM from scratch on such a small dataset would have produced much worse results. Additionally the source data was made up of small 81 bp sequences. I would expect LSTMs to perform better over long sequences with more complex dependencies.
