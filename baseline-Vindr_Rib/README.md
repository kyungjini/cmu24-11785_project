## Baseline Evaluation and Implementation

Our study focuses on **explainable AI (XAI)** rather than solely improving model performance. To align with this objective, we established a baseline model inspired by existing methodologies and tailored to the characteristics of our problem. The baseline was implemented experimentally, and its reproducibility was confirmed through careful validation, ensuring that it aligns with previously reported results.

### Dataset
We utilized the **VinDr-RibCXR** dataset, which consists of:
- **245 chest X-rays (CXRs)** with expert-provided ground truth annotations.
- Tasks include segmentation and labeling of **20 individual ribs**.

The dataset was divided as follows:
- **Training Set:** 196 images  
- **Test Set:** 49 images  

### Baseline Performance

| Model                           | Metric        | Previous Study       | Our Implementation       |
|---------------------------------|---------------|----------------------|--------------------------|

| **U-Net w/ EfficientNet-B0**    | Dice Score    | 0.829 (95% CI, 0.808–0.847)                | 0.825 |
|                                 

### Workflow
The baseline model was implemented with the following steps:
1. **Data Preprocessing:**
   - Standardized input dimensions.
   - Ensured data quality for training.
2. **Model Training:**
   - Documented hyperparameters and configurations for clarity.
   - Used a state-of-the-art segmentation model for training.
3. **Performance Evaluation:**
   - Conducted rigorous testing on the independent test set.
   - Verified alignment with previously reported results to ensure reproducibility.

### Key Insights
- The baseline implementation successfully reproduced the reported performance from prior studies, emphasizing the reliability and correctness of the setup.
- This work serves as a foundational benchmark for integrating XAI techniques, focusing on enhancing interpretability while maintaining consistent performance.

By confirming the reproducibility of prior work, this study establishes a solid baseline for future research in rib segmentation and labeling using chest X-rays, highlighting the value of XAI in advancing this domain.
