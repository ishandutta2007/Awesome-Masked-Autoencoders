# MaskFeat (Masked Feature Prediction)

MaskFeat is a masked image modeling approach that predicts hand-crafted features instead of raw pixels or discrete tokens.

## Key Details
1. **Target Feature:** Specifically predicts Histograms of Oriented Gradients (HOG) for the masked regions.
2. **Motivation:** HOG features capture local shapes and edges while being invariant to lighting changes, providing a more semantically meaningful target than raw pixels.
3. **Architecture:** Uses a standard Vision Transformer (ViT) as the backbone.
4. **Efficiency:** Does not require a pre-trained tokenizer (unlike BEiT) and uses a simple linear prediction head.

MaskFeat demonstrated that choosing the right reconstruction target can significantly impact self-supervised performance.

![MaskFeat Architecture](./images/maskfeat.png)
