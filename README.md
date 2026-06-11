# Awesome-Masked-Autoencoders
## Alternatives to Masked Autoencoders (MAEs)

When moving beyond Masked Autoencoders (MAEs) and Masked Image Modeling (MIM) for self-supervised representation learning, several powerful alternatives exist. These methods bypass pixel-level reconstruction, focusing instead on contrasting views, spatial context, or distributional properties.

## Detailed Alternatives and Architectures

Below are detailed explanations and architecture diagrams for Masked Autoencoders and their various alternatives:

1.  **[Masked Autoencoders (MAE)](./MAE.md)** - Scalable vision learners using asymmetric encoder-decoders.
2.  **[Masked Image Modeling (MIM)](./MIM.md)** - The general paradigm of reconstructing missing image patches.
3.  **[SimCLR](./SimCLR.md)** - A simple framework for contrastive learning of visual representations.
4.  **[I-JEPA](./I-JEPA.md)** - Joint-Embedding Predictive Architecture predicting in latent space.
5.  **[BEiT](./BEiT.md)** - BERT-style pre-training using discrete visual tokens.
6.  **[DINO](./DINO.md)** - Self-distillation with no labels, learning object-centric features.
7.  **[SimMIM](./SimMIM.md)** - A simplified framework for masked image modeling with pixel reconstruction.
8.  **[Data2Vec](./Data2Vec.md)** - A unified framework for self-supervised learning across vision, speech, and text.
9.  **[MaskFeat](./MaskFeat.md)** - Masked feature prediction using HOG as the target.
10. **[CAE](./CAE.md)** - Context Autoencoder using a latent regressor for masked patch prediction.
11. **[Variational Autoencoder (VAE)](./VAE.md)** - Generative models using probabilistic latent spaces and reparameterization.
12. **[Sparse Autoencoder (SAE)](./SparseAutoencoder.md)** - Autoencoders with sparsity constraints to learn efficient and salient features.

## 1. Contrastive Learning
Contrastive Learning methods learn by pulling "positive" pairs (different augmented views of the same image) closer in the embedding space, while pushing apart "negative" pairs (different images). 
* **[SimCLR](./SimCLR.md):** Uses a simple framework that avoids memory banks, relying instead on large batch sizes and data augmentation.
* **[MoCo](./MoCo.md) (Momentum Contrast):** Builds dynamic dictionaries with a queue and a momentum encoder, decoupling batch size from the number of negative samples.

## 2. Joint-Embedding Predictive Architectures (JEPAs)
Instead of matching pixel-by-pixel, JEPAs predict the representation of a masked patch in an abstract latent space rather than the input space itself. 
* **[I-JEPA](./I-JEPA.md) (Image-Joint Embedding Predictive Architecture):** Predicts the semantic embedding of a hidden/masked patch from a visible context block, resulting in strong object-level understanding without pixel-level detail reconstruction.
* **[VICReg](./VICReg.md) (Variance-Invariance-Covariance Regularization):** A non-contrastive method that prevents representation collapse by maximizing variance, ensuring feature invariance, and minimizing covariance between embedding dimensions.

## 3. Self-Distillation / Clustering Methods
These techniques align the feature representations of different views of the same image without requiring negative samples.
* **[DINO](./DINO.md) (Self-Distillation with No Labels):** Treats self-supervised learning as a teacher-student distillation process. The student network predicts the output of the teacher network, employing a centered and sharpened softmax to prevent collapse.
* **[SwAV](./SwAV.md) (Swapping Assignments between multiple Views):** Computes cluster assignments for multiple views of an image and swaps them, forcing the model to learn view-invariant features.

## 4. Canonical / Spatial Context Prediction
These spatial approaches learn by understanding geometry or absolute positioning rather than reconstructing missing parts.
* **[RotNet](./RotNet.md):** Trains models by predicting the rotational orientation of an image (0°, 90°, 180°, or 270°).
* **[Jigsaw Puzzles](./Jigsaw.md):** Divides images into a grid, shuffles the patches, and tasks the model with rearranging them into the correct spatial order. 

## 5. Deep Generative Alternatives
While not technically "masked" autoencoders, they utilize the broader Autoencoder framework for representation learning.
* **[Variational Autoencoders (VAEs)](./VAE.md):** Probabilistic models that map inputs to a latent space governed by probability distributions, allowing for both representation learning and generative decoding.
* **[Sparse Autoencoders (SAEs)](./SparseAutoencoder.md):** Enforce a sparsity penalty on the hidden layers, forcing the model to learn highly specific, localized, and meaningful features.

***

## Further Exploration
To evaluate how these alternative frameworks perform relative to masked modeling approaches, consider reviewing:
* **Benchmark Comparisons:** Explore how contrastive methods compare against MIM on ImageNet classification via the [CVPR Open Access Repository](https://thecvf.com).
* **Hybrid Approaches:** Read about frameworks that attempt to distill masked autoencoders into contrastive models in research on [MOMA](https://springer.com).
* **Theoretical Foundations:** Understand the mathematical properties of invariant feature learning via the [CVPR 2023 Paper Archive](https://thecvf.com/content/CVPR2023/papers/Kong_Understanding_Masked_Image_Modeling_via_Learning_Occlusion_Invariant_Feature_CVPR_2023_paper.pdf).


## 📈 Star History

<div align="center">
   <a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Masked-Autoencoders&type=date&legend=bottom-right">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Masked-Autoencoders&type=date&theme=dark&legend=bottom-right" />
      <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Masked-Autoencoders&type=date&legend=bottom-right" />
      <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Masked-Autoencoders&type=date&legend=bottom-right" />
    </picture>
   </a>
</div>

