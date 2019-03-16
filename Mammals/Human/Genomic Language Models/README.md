# Human Genome Language Models

These notebooks detail data preparation and training for language models based on the human genome. These models form the foundations 
for the classification models trained in the other directories. The language model architecture is based on the [AWD-LSTM](https://github.com/salesforce/awd-lstm-lm). 

Genomic data is broken into tokens using a k-mer approach with a set stride between k-mers. For tokenization with k-mer length k and stride s, 
the input genomic sequences are broken into chunks of length k base pairs with a shift of s base pairs between k-mers.

__LM 0__ details processing the [human genome](https://www.ncbi.nlm.nih.gov/genome/51) into a form we can feed into a model.

__LM 1__ trains a model with k-mer length 4 and stride 2.

__LM 2__ trains a model with k-mer length 5 and stride 2.

__LM 3__ trains a model with k-mer length 8 and stride 3.
