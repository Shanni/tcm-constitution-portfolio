# TCM Constitution Portfolio

Python ML core + TypeScript frontend for CCMQ (Chinese Medicine Constitution Questionnaire) research demo.

## Architecture

```text
apps/web (Next.js)  ──HTTP──▶  python/ (FastAPI + scoring + ML)
                                      │
                                      ▼
                               data/raw (Zenodo, Mendeley)
```

## Quick start

### 1. Python API

```bash
cd python
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
uvicorn tcm_constitution.api.main:app --reload --port 8000
```

### 2. Web UI

```bash
cd apps/web
cp .env.example .env.local
npm install
npm run dev
```

Open http://localhost:3000

### 3. Tests

```bash
cd python && pytest
```

### 4. Download open datasets

```bash
bash python/scripts/download_data.sh
```

### 5. Mendeley EDA + baselines

```bash
cd python
pip install -e ".[dev,notebooks]"
python scripts/run_eda_mendeley.py          # saves figures to notebooks/output/
jupyter notebook notebooks/01_eda_mendeley.ipynb
jupyter notebook notebooks/02_reproduce_su2019.ipynb
```

## Open data sources

| Dataset | DOI / URL | Use |
|---------|-----------|-----|
| CCMQ test + SAS code | [Zenodo 4431679](https://zenodo.org/records/4431679) | Scoring validation |
| Cross-sectional SPSS | [Zenodo 18779514](https://zenodo.org/records/18779514) | Population stats |
| 274-subject multimodal | [Mendeley cxtph3tjsg](https://data.mendeley.com/datasets/cxtph3tjsg/1) | ML baseline |

See [`../research/tcm-constitution-data-sources/`](../research/tcm-constitution-data-sources/) for contacts, [outreach templates](../research/tcm-constitution-data-sources/outreach-templates.md) (incl. Template C), and [one-page pitch](../research/tcm-constitution-data-sources/ONE_PAGE_PITCH.md).

## Repo layout

```text
tcm-constitution-portfolio/
├── apps/web/          # Next.js questionnaire UI
├── python/
│   ├── src/tcm_constitution/
│   │   ├── ccmq/      # items.json + scoring
│   │   └── api/       # FastAPI
│   ├── tests/
│   └── scripts/
└── data/raw/          # downloaded cohorts (gitignored)
```

## Disclaimer

Research and education demo only. Not a medical device or diagnostic tool.
