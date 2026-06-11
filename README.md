# Awesome-Masked-Autoencoders
## Alternatives to Masked Autoencoders (MAEs)

When moving beyond Masked Autoencoders (MAEs) and Masked Image Modeling (MIM) for self-supervised representation learning, several powerful alternatives exist. These methods bypass pixel-level reconstruction, focusing instead on contrasting views, spatial context, or distributional properties.

## 1. Contrastive Learning
Contrastive Learning methods learn by pulling "positive" pairs (different augmented views of the same image) closer in the embedding space, while pushing apart "negative" pairs (different images). 
* **SimCLR:** Uses a simple framework that avoids memory banks, relying instead on large batch sizes and data augmentation.
* **MoCo (Momentum Contrast):** Builds dynamic dictionaries with a queue and a momentum encoder, decoupling batch size from the number of negative samples.

## 2. Joint-Embedding Predictive Architectures (JEPAs)
Instead of matching pixel-by-pixel, JEPAs predict the representation of a masked patch in an abstract latent space rather than the input space itself. 
* **I-JEPA (Image-Joint Embedding Predictive Architecture):** Predicts the semantic embedding of a hidden/masked patch from a visible context block, resulting in strong object-level understanding without pixel-level detail reconstruction.
* **VICReg (Variance-Invariance-Covariance Regularization):** A non-contrastive method that prevents representation collapse by maximizing variance, ensuring feature invariance, and minimizing covariance between embedding dimensions.

## 3. Self-Distillation / Clustering Methods
These techniques align the feature representations of different views of the same image without requiring negative samples.
* **DINO (Self-Distillation with No Labels):** Treats self-supervised learning as a teacher-student distillation process. The student network predicts the output of the teacher network, employing a centered and sharpened softmax to prevent collapse.
* **SwAV (Swapping Assignments between multiple Views):** Computes cluster assignments for multiple views of an image and swaps them, forcing the model to learn view-invariant features.

## 4. Canonical / Spatial Context Prediction
These spatial approaches learn by understanding geometry or absolute positioning rather than reconstructing missing parts.
* **RotNet:** Trains models by predicting the rotational orientation of an image (0°, 90°, 180°, or 270°).
* **Jigsaw Puzzles:** Divides images into a grid, shuffles the patches, and tasks the model with rearranging them into the correct spatial order. 

## 5. Deep Generative Alternatives
While not technically "masked" autoencoders, they utilize the broader Autoencoder framework for representation learning.
* **Variational Autoencoders (VAEs):** Probabilistic models that map inputs to a latent space governed by probability distributions, allowing for both representation learning and generative decoding.
* **Sparse Autoencoders:** Enforce a sparsity penalty on the hidden layers, forcing the model to learn highly specific, localized, and meaningful features.

***

## Further Exploration
To evaluate how these alternative frameworks perform relative to masked modeling approaches, consider reviewing:
* **Benchmark Comparisons:** Explore how contrastive methods compare against MIM on ImageNet classification via the [CVPR Open Access Repository](https://thecvf.com).
* **Hybrid Approaches:** Read about frameworks that attempt to distill masked autoencoders into contrastive models in research on [MOMA](https://springer.com).
* **Theoretical Foundations:** Understand the mathematical properties of invariant feature learning via the [CVPR 2023 Paper Archive](https://thecvf.com/content/CVPR2023/papers/Kong_Understanding_Masked_Image_Modeling_via_Learning_Occlusion_Invariant_Feature_CVPR_2023_paper.pdf).
