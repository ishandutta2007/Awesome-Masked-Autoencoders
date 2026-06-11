# Jigsaw Puzzles (Context Free Network)

Solving Jigsaw puzzles is a classic spatial pretext task where the model learns to reassemble shuffled image patches.

## Architectural Features
- **Siamese-Ennead Structure:** The model uses 9 parallel branches (with shared weights) to process 9 patches from a 3x3 grid.
- **Independent Processing:** Each branch extracts features from a patch independently.
- **Permutation Prediction:** The features are concatenated and fed into a classifier that predicts the permutation index used to shuffle the patches.

By learning the spatial arrangement of object parts, the model develops a strong understanding of object geometry and parts.

![Jigsaw Architecture](./images/jigsaw.png)
