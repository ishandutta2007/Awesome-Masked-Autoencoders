# SimCLR

SimCLR (Simple Framework for Contrastive Learning of Visual Representations) is a contrastive learning approach that learns representations by maximizing agreement between differently augmented views of the same data example.

## Core Components
1. **Data Augmentation:** Transforms any given data example into two correlated views, which are considered a positive pair.
2. **Base Encoder:** A neural network (typically ResNet-50) that extracts representation vectors from the augmented data examples.
3. **Projection Head:** A small MLP that maps the representations to a space where contrastive loss (NT-Xent) is applied.
4. **Contrastive Loss:** Maximizes agreement between positive pairs while minimizing it against all other images in the batch.

SimCLR demonstrated that large batch sizes and strong data augmentation are crucial for contrastive learning performance.

![SimCLR Architecture](./images/simclr.png)
