# BEiT (BERT Pre-Training of Image Transformers)

BEiT pioneers the use of discrete visual tokens for Masked Image Modeling (MIM), drawing a direct analogy to BERT's Masked Language Modeling (MLM) in NLP.

## Key Features
1. **Image Tokenizer (dVAE):** Maps image patches into discrete visual tokens from a fixed vocabulary.
2. **Masked Image Modeling (MIM):**
   - **Input:** A subset of image patches is randomly masked and replaced with a learnable [MASK] embedding.
   - **Objective:** The model is trained to predict the original discrete visual tokens for the masked positions.
3. **Backbone:** Uses a standard Vision Transformer (ViT).

BEiT showed that token-based reconstruction is a powerful alternative to pixel-level reconstruction.

![BEiT Architecture](./images/beit.png)
