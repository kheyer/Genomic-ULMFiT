# Mammalian Genome Language Models

These notebooks detail data preparation and training for language models based on several mammalian genomes. These models form the foundations 
for the classification models trained in the other directories. The language model architecture is based on the [AWD-LSTM](https://github.com/salesforce/awd-lstm-lm). 

Genomic data is broken into tokens using a k-mer approach with a set stride between k-mers. For tokenization with k-mer length k and stride s, 
the input genomic sequences are broken into chunks of length k base pairs with a shift of s base pairs between k-mers.

__LM 0__ details processing genomes from [H. sapiens](https://www.ncbi.nlm.nih.gov/genome/51), [P. troglodytes](https://www.ncbi.nlm.nih.gov/genome/202?genome_assembly_id=276759), 
[P. paniscus](https://www.ncbi.nlm.nih.gov/genome/10729?genome_assembly_id=249283) and 
[G. gorilla](https://www.ncbi.nlm.nih.gov/genome/2156?genome_assembly_id=291477).

__LM 1__ trains a model with k-mer length 5 and stride 2.

__LM 2__ trains a model with k-mer length 4 and stride 2.
