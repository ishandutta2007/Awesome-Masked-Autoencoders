# CAE (Context Autoencoder)

CAE is a masked image modeling (MIM) approach that separates the encoding of visible patches from the prediction of masked patches using a latent context regressor.

## Components
1. **Encoder:** Processes only the visible patches to extract latent representations.
2. **Latent Context Regressor:** A module that predicts the representations of masked patches based on visible patch representations and their positions.
3. **Decoder:** Reconstructs the original pixels or tokens from the predicted masked representations.
4. **Alignment Module:** Ensures that predicted representations match the actual representations generated from unmasked patches.

CAE performs the "thinking" or reasoning in the latent space before decoding, which helps in learning more robust features.

![CAE Architecture](./images/cae.png)
