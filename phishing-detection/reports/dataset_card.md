# Dataset Card - Kaggle "Phishing Email Dataset"

| Field | Value (fill in) |
|---|---|
| Name / author | |
| URL | |
| Date accessed / version | |
| License and permitted use | |
| Files used | e.g. CEAS_08, Enron, Ling, Nazario, Nigerian_Fraud, SpamAssassin, combined file |
| Raw rows | (from notebook 01) |
| Rows after cleaning | (from notebook 02 cleaning log) |
| Class balance (phishing / legitimate) | |
| Fields available | subject, body, sender, receiver, date, urls, label (confirm per file) |
| Label convention | 1 = phishing/spam, 0 = legitimate (confirm against dataset description) |

| Raw rows (excluding excluded files) | 82,675 |
| Rows after cleaning | 82,080 (595 removed — all exact duplicates once whitespace was normalized; zero missing labels, zero empty text, zero conflicting-label duplicates) |
| Class balance (final) | Phishing: 52.2% | Legitimate: 47.8% |
| Files excluded | spamResults.csv — sentiment-analysis output (columns: message, compound, neg, neu, pos), not raw labeled email data |
| Single-class sources | Nazario, Nigerian_Fraud, PhishingEmailData — phishing only, ~12% of all phishing rows; addressed via a planned cross-source held-out evaluation (Week 4) |

## Composition per source
(Paste the crosstab from notebook 01.)

## Cleaning steps
Missing labels removed, whitespace normalized, empty text removed, conflicting-label duplicates removed, exact duplicates removed. Splits: stratified 70/15/15, seed 42.

## Known limitations (review and edit)
- **Aggregated, not original:** the Kaggle set is a community compilation of older public corpora, so provenance and labeling are only as reliable as the underlying sources.
- **Source/label confounding:** some sources contain a single class, so a model may learn source style instead of phishing cues. Mitigation: source-held-out evaluation (Week 4).
- **Spam vs phishing:** some sources (e.g. CEAS_08, SpamAssassin) are spam-oriented rather than strictly phishing; state how "phishing" is defined in the report.
- **Age:** several corpora are from the 2000s and do not reflect modern, LLM-written phishing.
- **Metadata:** header fields (sender, date) may be missing or inconsistent across files; text-only features are the safest common denominator.
- **Language/domain:** predominantly English.
