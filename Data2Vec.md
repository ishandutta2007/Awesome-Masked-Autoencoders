# Data2Vec

Data2Vec is a unified self-supervised learning framework that works across multiple modalities: vision, speech, and text.

## Architecture Highlights
1. **Teacher-Student Setup:** The teacher processes the full input, while the student processes a masked version.
2. **EMA Update:** The teacher's weights are updated via an Exponential Moving Average of the student's weights.
3. **Latent Representation Prediction:** The student is trained to predict the teacher's latent representations (specifically, the average of the top layers) for the masked regions.
4. **Modality Agnostic:** Uses the same learning objective for different types of input data.

Data2Vec 2.0 further improved the efficiency and speed of this framework.

![Data2Vec Architecture](./images/data2vec.png)
