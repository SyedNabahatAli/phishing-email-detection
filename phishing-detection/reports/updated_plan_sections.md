# Suggested edits to the project plan document (Week 1)

Copy these into the matching sections of your plan.

## 1.3 Objective 1 (replace)
Identify and finalize a suitable publicly available phishing email dataset. **Selected: the Kaggle "Phishing Email Dataset" (aggregated public corpora), documented in a dataset card including source, size, fields, labels and limitations.**

## 2. Research Questions (replace)
1. Which classical ML models (Logistic Regression, Naive Bayes, Random Forest, SVM) perform best on TF-IDF features for phishing detection?
2. Do engineered features (URL, structural, urgency and credential-request features) improve on a TF-IDF-only baseline?
3. Which features contribute most, measured by feature importance and ablation?
4. How well do models generalize across data sources (train on some sources, test on a held-out source)?
5. How accurately can an LLM classify real and synthetic phishing emails, compared with the trained models?
6. What is the false-positive / false-negative trade-off of the final model, and how can it be exposed in a prototype?

## 3.1 Dataset Acquisition and Preparation (replace first paragraph)
The project uses the publicly available Kaggle "Phishing Email Dataset", selected for its accessibility and its labeled phishing and legitimate emails. Because it aggregates older public corpora, its limitations (source bias, spam/phishing overlap, age of samples) are documented and addressed through deduplication, per-source analysis and cross-source evaluation.

## 3.5 / Architecture (add)
Python, pandas, scikit-learn, JupyterLab for experiments; reusable code in `src/`; Streamlit prototype in `app/`; fixed seed and saved splits for reproducibility.

## 6. Week 1 progress report
Use the entry in `research_journal.md`.

## Timeline assumptions (add)
Dataset is prepared ahead of the client meeting; the dataset card and Week 1 notebooks are shared for review.
