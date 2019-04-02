# Model Interpretation

One way to interpret how the model makes classification decisions is by perturbing an input sequence and seeing how the perturbation affects the 
output prediction. These notebooks look at randomizing a sliding sequence window of varying k-mer length along an input sequence to see how 
predictions are effected. This allows us to see what sequence motifs are important for classification decisions and how robust the model is 
to noise in the input sequence.

__E. coli Interp__ runs this process on E. coli promoters. This notebook also explains the relevant code.

__Human Short Interp__ runs the process on short human promoters

__Human Long Interp__ runs the process on long human promoters

We can generate plots showing how different sequence regions are affected by purturbations of different k-mer length.

A sample E. coli promoter (the red line marks the true transcription start site):
![](https://github.com/kheyer/Genomic-ULMFiT/blob/master/Model%20Interpretations/media/coli_interp.png)

A sample long human promoter:
![](https://github.com/kheyer/Genomic-ULMFiT/blob/master/Model%20Interpretations/media/human_interp.png)

(Note the difference in Y axis scales in the two images)

# Long Sequence Prediction

We can also look at how the model performs when predicting over a long contiguous sequence instead of curated sequence segments. This process is demonstrated in the __Long Sequence Prediction E. coli__ notebook.
