# SwAV (Swapping Assignments between Views)

SwAV (Swapping Assignments between Views) is a self-supervised method that contrasts cluster assignments instead of individual image features.

## Key Features
- **Multi-Crop Augmentation:** Uses multiple high-resolution and low-resolution views of an image to increase the amount of data the model sees.
- **Online Clustering:** Assigns image features to a set of trainable prototypes using the Sinkhorn-Knopp algorithm.
- **Swapped Prediction:** The model is trained to predict the cluster assignment of one view from the feature representation of another view.

SwAV effectively combines clustering and contrastive learning, leading to strong performance on visual representation tasks.

![SwAV Architecture](./images/swav.png)
