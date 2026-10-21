# Day 30: Classification Evaluation Reference

| Metric | Formula | When to Optimize |
|---|---|---|
| **Accuracy** | $(TP + TN) / Total$ | Balanced classes only |
| **Precision** | $TP / (TP + FP)$ | Minimizing False Positives (e.g. spam detection) |
| **Recall** | $TP / (TP + FN)$ | Minimizing False Negatives (e.g. cancer/fraud detection) |
| **F1-Score** | $2 \cdot \frac{P \cdot R}{P + R}$ | Balance between precision and recall |
| **ROC-AUC** | Area under FPR vs TPR | Threshold-independent discriminator capability |
