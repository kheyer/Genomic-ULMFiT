# Bactieral Genomic Language Models

These notebooks detail data preparation and training for language models based on genomic data from multiple bacterial organisms. These models form the foundations 
for the classification models trained in the other directories. The language model architecture is based on the [AWD-LSTM](https://github.com/salesforce/awd-lstm-lm). 

Genomic data is broken into tokens using a k-mer approach with a set stride between k-mers. For tokenization with k-mer length k and stride s, 
the input genomic sequences are broken into chunks of length k base pairs with a shift of s base pairs between k-mers.

__LM 0__ details processing the bacterial genomes into a form we can feed into a model. See the notebook for a list of bacterial species used

__LM 1__ trains a model with k-mer length 5 and stride 2.
