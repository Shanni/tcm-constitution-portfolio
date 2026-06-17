# Portfolio & System Design — TCM Constitution Data

How the open datasets are structured, how to unify them, and a **3-phase portfolio** you can build without a supervisor or large cohort access.

---

## 1. Data structures (what each file actually contains)

### 1.1 Zenodo TEST_DATA.xlsx (CCMQ demo, N≈14)

**Role:** Learn official **scoring pipeline**, not train production models.

| Layer | Fields (typical) | Type |
|-------|------------------|------|
| Raw responses | `Q1` … `Q60` | int 1–5 (Likert) |
| Demographics | `sex`, `age`, `BMI` (if present) | mixed |
| Converted scores | `GTC`, `QDC`, `YaDC`, `YiDC`, `PDC`, `DHC`, `BSC`, `QSC`, `SDC` | float 0–100 |
| Label | `primary_type` or `Pinghe` flag | categorical (9 types) |

**Scoring rule (national standard):**

```
converted_score = (sum(raw_items) - n_items) / (n_items * 4) * 100
```

- **平和质 GTC:** converted ≥ 60 AND all biased types < 30  
- **偏颇质:** converted ≥ 40 → yes; 30–40 → tendency  

**Companion files:** `CCMQ SAS code.sas` / `CCMQ SPSS syntax.sps` — reference implementation for the same logic.

---

### 1.2 Mendeley cxtph3tjsg (multimodal, N=274) ⭐ core portfolio data

**Role:** Only open set with **biosignal features + constitution scores** on the same subjects.

Paper: [Computers in Biology and Medicine, 2019](https://doi.org/10.1016/j.compbiomed.2019.04.001)

| Block | Example indices | Notes |
|-------|-----------------|-------|
| **Demographics** | sex, age, BMI | Table 1 in paper |
| **Tongue** | G, B, S, b (color), max width, red spots, scalloped margin % | From tongue camera |
| **Voice** | intensity, zero-crossing rate, high spectral energy ratio, pitch | From acoustic recording |
| **Pulse** | main wave height, unsmooth wave, systolic area, rapid ejection time | From pulse sensor |
| **Constitution** | 8 abnormal type **scores** (Nine-Constitution Scale) | Continuous targets; not just 9-class label |

**Important:** Mendeley bundle is usually **Excel/CSV of extracted indices**, not raw tongue images or waveforms. Each row = one subject; columns = features + score columns.

**Typical row shape:**

```
subject_id | sex | age | bmi | tongue_G | tongue_B | ... | voice_intensity | ... | pulse_main_height | ... | score_QiDef | score_YangDef | ... | score_BloodStasis
```

---

### 1.3 Zenodo dataset_phyact_Psychodistress_TCMBC.sav (cross-sectional)

**Role:** Second real cohort for **questionnaire + behavioral health** analysis.

| Block | Expected variables | Type |
|-------|-------------------|------|
| Physical activity | IPAQ or similar summary scores | numeric |
| Psychological distress | anxiety / depression scales | numeric |
| TCM constitution | balanced vs biased types, or 9-type | categorical + scores |

Exact column names: inspect with `pyreadstat.read_sav()` after download. Size ~58 KB → likely **hundreds of rows**, not thousands.

---

### 1.4 Instruments only (no subject rows)

| Asset | Structure | Use |
|-------|-----------|-----|
| CCMQ PDF (723118) | 60 questions + 5-point scale text | Build web form / validation |
| Springer MOESM1.docx | Item ID → abbreviation → subscale mapping | Feature naming |
| Frontiers Table_3.xlsx | 81 transition rules (9×9 constitution pairs) | Longitudinal label logic (reference) |

---

### 1.5 Dryad TMC-Tongue (images, not constitution)

```
images/
  train/ 5594
  val/    572
  test/   553
labels: 21 tongue pathology classes (coco/txt/xml)
```

**No 9-type constitution label** — use only if you add a separate questionnaire module later.

---

## 2. Unified data model (design once, plug datasets in)

Define an internal schema so portfolio code stays clean:

```yaml
Subject:
  id: string
  demographics:
    sex: enum
    age: int
    bmi: float

  questionnaire:          # optional per dataset
    items: dict[Q1..Q60, int 1-5]
    converted_scores: dict[GTC|QDC|..., float]
    primary_constitution: enum[9 types]

  biosignals:             # Mendeley only
    tongue: dict[str, float]
    voice: dict[str, float]
    pulse: dict[str, float]

  behavioral:             # Zenodo SPSS only
    physical_activity: float
    psych_distress: float

  metadata:
    source: enum[zenodo_test|mendeley_274|zenodo_sav|synthetic]
    split: enum[train|val|test]
```

**Design principle:**  
- **Questionnaire path** and **multimodal path** share the same `Subject.primary_constitution` output.  
- Adapters per dataset map raw columns → `Subject`.

---

## 3. Portfolio strategy (3 phases)

Build in order — each phase is a **GitHub repo milestone** you can show in PhD / 套磁 emails.

### Phase A — CCMQ Engine (1–2 weeks)

**Goal:** “I implemented the national standard scoring pipeline.”

| Deliverable | Detail |
|-------------|--------|
| `ccmq/scoring.py` | 60-item → 9 converted scores → primary type |
| Unit tests | Match Zenodo TEST_DATA rows against SAS/SPSS output |
| CLI | `python -m ccmq score --input responses.csv` |
| Demo | Streamlit: 60-question form → constitution result + radar chart |

**Portfolio line:** *Reproducible implementation of Wang Qi CCMQ standard (ZYYXH/T157-2009).*

---

### Phase B — Multimodal baseline (2–3 weeks)

**Goal:** “I reproduced the 2019 multimodal constitution paper on open data.”

| Step | Action |
|------|--------|
| 1 | Download Mendeley 274; EDA + correlation heatmap (reproduce paper Table 2 idea) |
| 2 | Train **per-constitution score regression** (linear / Ridge) — paper used Pearson + linear regression |
| 3 | Train **9-type classifier** (RF / XGBoost) from stacked tongue+voice+pulse features |
| 4 | Report MAE on scores + macro-F1 on derived primary type |
| 5 | SHAP / feature importance → “which modality matters for which constitution” |

**Portfolio line:** *Multimodal TCM constitution prediction on N=274 open cohort; aligns with Su et al. 2019.*

---

### Phase C — Mini “research platform” (2–4 weeks)

**Goal:** System design story for interviews / 套磁 / startup tech demo (non-clinical).

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│  Ingestion  │────▶│  CCMQ Core   │────▶│  Constitution   │
│  CSV / Form │     │  Scoring     │     │  Profile (9)    │
└─────────────┘     └──────────────┘     └────────┬────────┘
       │                    │                      │
       ▼                    ▼                      ▼
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│  Biosignal  │────▶│  Feature     │────▶│  Fusion Model   │
│  Adapter    │     │  Store       │     │  (optional ML)  │
└─────────────┘     └──────────────┘     └─────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │  Report / API    │
                    │  JSON + PDF      │
                    └──────────────────┘
```

| Module | Responsibility |
|--------|----------------|
| `adapters/` | zenodo_test, mendeley, sav → unified `Subject` |
| `ccmq/` | scoring + short-form (26-item) optional |
| `models/` | sklearn pipelines; save with joblib |
| `api/` | FastAPI: `POST /score`, `POST /predict-multimodal` |
| `ui/` | Streamlit dashboard |
| `reports/` | Jinja2 HTML or markdown clinical-style summary |

**Portfolio line:** *End-to-end constitution assessment prototype with pluggable data sources.*

---

## 4. Recommended repo layout

```
tcm-constitution-portfolio/
├── README.md                 # screenshots + links to data DOIs
├── data/
│   ├── raw/                  # gitignored; download scripts
│   └── processed/            # parquet with unified schema
├── src/
│   ├── schema.py             # Subject dataclass / pydantic
│   ├── adapters/
│   │   ├── zenodo_test.py
│   │   ├── mendeley_274.py
│   │   └── zenodo_sav.py
│   ├── ccmq/
│   │   ├── items.py          # 60 item → subscale map
│   │   ├── scoring.py
│   │   └── classify.py
│   ├── models/
│   │   ├── train_regression.py
│   │   ├── train_classifier.py
│   │   └── evaluate.py
│   └── viz/
│       ├── radar.py
│       └── correlation.py
├── notebooks/
│   ├── 01_eda_mendeley.ipynb
│   ├── 02_reproduce_su2019.ipynb
│   └── 03_ccmq_validation.ipynb
├── apps/
│   ├── api/main.py           # FastAPI
│   └── streamlit_app.py
├── tests/
│   └── test_scoring.py
└── scripts/
    └── download_data.sh
```

---

## 5. Tech stack (keep it simple)

| Layer | Choice | Why |
|-------|--------|-----|
| Language | Python 3.11+ | pandas, sklearn, ecosystem |
| Data | pandas + pyarrow (parquet) | SPSS via `pyreadstat` |
| ML | scikit-learn, XGBoost | Enough for portfolio; matches papers |
| API | FastAPI | Clean REST for “system design” narrative |
| UI | Streamlit | Fast demo without frontend team |
| Config | pydantic-settings | Reproducible paths |
| CI | pytest on scoring tests | Shows engineering discipline |

**Do not need yet:** PyTorch, K8s, database — add PostgreSQL only if you fake longitudinal visits.

---

## 6. Implementation order (concrete tasks)

### Week 1 — Scoring core

```bash
# dependencies
pip install pandas pyreadstat scikit-learn matplotlib streamlit fastapi pydantic pytest

# download
curl -LO https://zenodo.org/api/records/4431679/files/TEST_DATA.xlsx/content
# Mendeley: manual "Download All" from browser
```

1. Hard-code 60-item → 9 subscale item lists (from MOESM1.docx or paper).  
2. Implement `compute_converted_scores(items: dict) -> dict`.  
3. Implement `assign_primary_type(scores: dict) -> str`.  
4. Assert against TEST_DATA.xlsx rows.  

### Week 2 — Mendeley EDA + baseline models

1. `adapters/mendeley_274.py`: load Excel, normalize column names.  
2. Train/test split 80/20 (stratify on binned primary type if you derive it).  
3. Baseline: Ridge regression per constitution score; RF for 9-class.  
4. Notebook comparing your metrics to paper’s correlation narrative.  

### Week 3 — API + UI

1. `POST /api/v1/ccmq/score` — body: `{ "responses": {"Q1": 3, ...} }`.  
2. Streamlit: wizard questionnaire → radar + text advice (from public TCM wellness text, not medical claims).  
3. README with architecture diagram + data citations.  

### Week 4 — Polish for 套磁

1. One-page PDF: problem → data → method → results → next steps (longitudinal / tongue images).  
2. GitHub pinned repo + optional Hugging Face Space for Streamlit demo.  
3. Email template referencing **specific reproduced table** from Su 2019 or Zhang 2026 methods.

---

## 7. What to show vs. what to avoid

| Show | Avoid |
|------|-------|
| Open DOI citations | Claiming clinical validation |
| Reproduced scoring + baselines | “AI doctor” marketing language |
| Modular adapters + tests | Training on 14 rows as “SOTA” |
| Roadmap: longitudinal + imaging | Mentioning startup product in academic email |

---

## 8. Stretch goals (if time)

| Extension | Data | Skill signal |
|-----------|------|--------------|
| Short-form CCMQ (26 items) | Paper PMC10164641 logic | Feature selection |
| Transition rules demo | Frontiers Table_3.xlsx | Understand Zhang 2026 labeling |
| Tongue CNN (transfer learning) | Dryad TMC-Tongue | CV + multimodal story |
| Merge SPSS cohort | Zenodo 18779514 | Mediation analysis (constitution ↔ distress) |

---

## 9. Success metrics (portfolio-ready)

| Phase | Metric target |
|-------|---------------|
| A | 100% match Zenodo test rows on converted scores |
| B | Report MAE / R² per constitution score; macro-F1 for type |
| C | API p95 < 200ms; demo video 2 min; README architecture |

---

*Cross-reference: [DOWNLOADABLE-DATA.md](./DOWNLOADABLE-DATA.md) for URLs · [outreach-templates.md](./outreach-templates.md) for 套磁*
