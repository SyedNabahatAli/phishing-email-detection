# Research Journal

## Week 1: Project Planning & Dataset Finalization

**Objectives:** review the prof's feedback, refine scope and research questions, identify and finalize the dataset, set up project architecture.

**Work Completed:**
- Reviewed the project plan and refined the research questions (see updated plan).
- Compared candidate datasets; selected the Kaggle "Phishing Email Dataset" for accessibility and availability of labeled phishing and legitimate emails.
- Set up the project repository (Python, JupyterLab, scikit-learn) with reproducible data loading, cleaning and splitting code.
- Ran the dataset review notebook: schema, class balance per source, duplicates, length and URL statistics. (add findings)
- Cleaned, deduplicated and split the dataset (70/15/15 stratified, seed 42). Rows removed per step: (add from cleaning log)
- Drafted the dataset card documenting source, size, labels, limitations.

**Research Decisions:**
- Dataset: Kaggle Phishing Email Dataset (variants combined), chosen for easy access; limitations documented rather than ignored.
- Added a source-held-out evaluation to test whether models generalize beyond dataset-specific style.
- Fixed random seed and saved splits to disk so all experiments use identical data.

**Challenges or Issues:**
- Provenance and licensing of a community-aggregated dataset need to be confirmed. (update)
- Possible source/label confounding and spam-vs-phishing labeling. (update with observed numbers)

**Next Steps:**
- Present dataset and limitations to the Prof; incorporate feedback.
- Week 2: exploratory analysis, class distribution, candidate engineered features.

**Work Completed:**
- Loaded and standardized 7 source files (82,675 emails total); excluded one file (spamResults.csv) found to be sentiment-analysis output rather than raw email data.
- Cleaned the dataset: 595 duplicate rows removed after whitespace normalization; no missing labels, empty text, or conflicting-label duplicates found. Final dataset: 82,080 emails (52.2% phishing, 47.8% legitimate).
- Identified 3 sources (Nazario, Nigerian_Fraud, PhishingEmailData) that contain only phishing examples — flagged as a source-bias risk, to be tested via a held-out-source evaluation in Week 4.
- Split into stratified train/validation/test sets (70/15/15, seed 42): 57,456 / 12,312 / 12,312 rows, each preserving the 52.2/47.8 class balance.
- Drafted the dataset card documenting sources, cleaning steps, and known limitations.

**Challenges or Issues:**
- Dataset combines files with different schemas and one non-UTF-8 encoded file; resolved with a standardization/fallback-encoding step in the loading code.
- Three sources are phishing-only, creating a possible source/label confound; will be tested for directly rather than ignored.

