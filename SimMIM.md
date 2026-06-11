# SimMIM (Simple Masked Image Modeling)

SimMIM is a simplified framework for masked image modeling that uses a standard encoder and an extremely lightweight prediction head to reconstruct raw pixels.

## Main Components
1. **Masking Strategy:** Random patch masking with a relatively large patch size (e.g., 32x32).
2. **Encoder:** A standard ViT or Swin Transformer that processes the masked image.
3. **Prediction Head:** A very light head (often just a single linear layer).
4. **Target:** Direct regression of raw RGB pixel values in the masked areas using L1 loss.

SimMIM emphasizes that a simple architecture can achieve competitive performance in masked modeling.

![SimMIM Framework](./images/simmim.png)
