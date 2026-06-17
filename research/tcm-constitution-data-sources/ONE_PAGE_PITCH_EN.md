# One-Page Pitch — TCM Constitution Research Portfolio (English)

**Candidate:** Shan Liu · UBC M.Sc. graduate  
**Email:** shan.liu.s3@gmail.com  
**GitHub:** https://github.com/Shanni/tcm-constitution-portfolio  
**Target:** PhD intake 2027 · BUCM / CDUTCM and related institutes  

*Research prototype only — not clinical validation or a medical device.*

---

## 1. Problem

TCM **body constitution** (体质) assessment uses standardized questionnaires (CCMQ) and, in modern studies, **multimodal biosignals** (tongue, voice, pulse). Large Chinese cohorts exist but are mostly **available upon request**; only small open datasets support reproducible methods work.

---

## 2. Open data used (DOI)

| Dataset | N | Role |
|---------|---|------|
| [Mendeley cxtph3tjsg](https://doi.org/10.17632/cxtph3tjsg.1) | 274 | Multimodal indices + 8 constitution scores |
| [Zenodo 4431679](https://doi.org/10.5281/zenodo.4431679) | 14 | CCMQ scoring validation (SAS reference) |
| [Zenodo 18779514](https://doi.org/10.5281/zenodo.18779514) | 511 | Cross-sectional constitution + distress |

**Collaboration targets:** Wang Qi (BUCM, ~91K CCMQ) · Mei Zhang (CDUTCM, 54,990 longitudinal TCMECQ)

---

## 3. What I built

```text
Next.js CCMQ UI  →  FastAPI  →  Python scoring (ZYYXH/T157-2009)
                                      │
                    Mendeley adapter ─┴─ EDA + sklearn baselines
```

| Component | Repo path |
|-----------|-----------|
| 60-item questionnaire + radar chart | `apps/web/` |
| CCMQ scoring API | `python/src/tcm_constitution/ccmq/` |
| Mendeley adapter + data dictionary | `adapters/mendeley_274.py`, `docs/MENDELEY_DATA_DICTIONARY.md` |
| EDA / baselines | `notebooks/01_eda_mendeley.ipynb`, `02_reproduce_su2019.ipynb` |

---

## 4. Results (Mendeley N=274)

**EDA:** 274 subjects · 54 biosignal features · 8 constitution scores (0–100). Strongest correlations: voice pitch ↔ Blood-stasis / Yin-deficiency (|r| ≈ 0.21–0.27).

**Baselines (80/20 split, biosignals → constitution):**

| Metric | Value |
|--------|-------|
| Train / test | 219 / 55 |
| Macro-F1 (primary type) | **0.14** |
| Score MAE | **12–15** (0–100 scale) |

*Biosignal-only models are weak alone — consistent with the need for larger longitudinal, questionnaire-grounded cohorts.*

---

## 5. Proposed next steps (with your lab)

1. Validate CCMQ scorer against Zenodo SAS test rows  
2. Scale pipeline to BUCM 91K or CDUTCM 54K cohort under DUA  
3. Multimodal fusion: questionnaire + imaging / cognitive / other modalities  
4. Longitudinal constitution transition modeling  

---

## 6. What I offer

- Reproducible Python/TypeScript codebase with tests and open-DOI citations  
- UBC master's training; fluent English writing and international collaboration experience  
- Machine learning pipelines, software engineering, and open-science workflow  

---

## 7. Contact

**Shan Liu** · shan.liu.s3@gmail.com · https://github.com/Shanni/tcm-constitution-portfolio  

*Export to PDF (Google Docs / Notion / pandoc) for non-Chinese institutions.*
