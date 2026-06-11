# DINO (Self-Distillation with No Labels)

DINO is a self-supervised learning method that treats pre-training as a teacher-student distillation process without requiring labels or negative samples.

## Key Components
- **Student & Teacher Networks:** Both share the same architecture (e.g., ViT or ResNet).
- **Multi-crop Strategy:** Passes global and local views of an image to the networks.
- **EMA Update:** The teacher's weights are an Exponential Moving Average (EMA) of the student's weights.
- **Centering & Sharpening:** Applied to the teacher's output to avoid representation collapse.

DINO is known for learning features that capture the layout of an image, such as object boundaries, and performs exceptionally well on k-NN classification.

![DINO Architecture](./images/dino.png)
