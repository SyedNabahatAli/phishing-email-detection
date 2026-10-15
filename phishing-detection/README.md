# AI-Assisted Phishing Email Detection Using Machine Learning

## Setup
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m ipykernel install --user --name phishing --display-name "Python (phishing)"
jupyter lab
```

## Dataset
Download the Kaggle "Phishing Email Dataset" (search for it on kaggle.com/datasets),
unzip, and place the CSV files in `data/raw/`. Record the dataset URL, author,
version/date accessed and license in `reports/dataset_card.md`.

## Notebooks (run in order)
1. `01_dataset_review.ipynb` - load, inspect, schema, label balance, duplicates, quality checks
2. `02_dataset_finalization.ipynb` - clean, deduplicate, save the final dataset and splits

## Layout
- `data/raw` original files (never edited) | `data/interim` | `data/processed` final dataset and splits
- `src/` reusable code | `notebooks/` analysis | `app/` prototype (Week 5) | `reports/` journal, dataset card, figures
