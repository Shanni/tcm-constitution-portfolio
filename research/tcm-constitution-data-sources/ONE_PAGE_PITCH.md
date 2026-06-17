# One-Page Pitch — TCM Constitution Research Portfolio

**For:** PhD supervisor outreach (2027 intake) · BUCM / CDUTCM / related institutes  
**Repo:** `tcm-constitution-portfolio/` (see GitHub link below)  
**Disclaimer:** Research prototype only — not clinical validation or a medical device.

---

## 1. Problem

Traditional Chinese Medicine (TCM) **body constitution** (体质) assessment relies on standardized questionnaires (CCMQ) and, in modern research, **multimodal biosignals** (tongue, voice, pulse). Large cohorts exist in China but are mostly **request-only**; only small open datasets are available for reproducible methods work.

---

## 2. Open data used (with DOI)

| Dataset | N | Role |
|---------|---|------|
| [Mendeley cxtph3tjsg](https://doi.org/10.17632/cxtph3tjsg.1) | 274 | Multimodal indices + 8 constitution scores |
| [Zenodo 4431679](https://doi.org/10.5281/zenodo.4431679) | 14 | CCMQ scoring validation (SAS reference) |
| [Zenodo 18779514](https://doi.org/10.5281/zenodo.18779514) | 511 | Cross-sectional constitution + distress (aggregated scores) |

**Target cohorts (collaboration request):**

- Wang Qi (BUCM): ~91K CCMQ web survey — doi:10.1186/s13020-024-00992-0  
- Mei Zhang (CDUTCM): 54,990 longitudinal TCMECQ — doi:10.3389/fmed.2026.1698576  

---

## 3. What I built

```text
Next.js CCMQ UI  →  FastAPI  →  Python scoring (ZYYXH/T157-2009)
                                      │
                    Mendeley adapter ─┴─ EDA + sklearn baselines
```

| Component | Path |
|-----------|------|
| 60-item questionnaire + radar chart | `tcm-constitution-portfolio/apps/web/` |
| CCMQ scoring API | `tcm-constitution-portfolio/python/src/tcm_constitution/ccmq/` |
| Mendeley data adapter + dictionary | `adapters/mendeley_274.py`, `docs/MENDELEY_DATA_DICTIONARY.md` |
| EDA notebook | `python/notebooks/01_eda_mendeley.ipynb` |
| Baseline ML notebook | `python/notebooks/02_reproduce_su2019.ipynb` |
| Tests | `python/tests/` (scoring + adapter) |

---

## 4. Results (Mendeley N=274, open data)

**EDA (notebook 01):**

- 274 subjects · 54 biosignal features · 8 constitution converted scores (0–100)
- Strongest feature–score correlations: voice pitch (`AvgP`, `MaxP`) ↔ Blood-stasis / Yin-deficiency (|r| ≈ 0.21–0.27)
- Primary-type distribution is imbalanced (Qi-deficiency / Yin-deficiency common)

**Baselines (notebook 02, 80/20 split, biosignals → constitution):**

| Metric | Value |
|--------|-------|
| Train / test | 219 / 55 |
| Macro-F1 (primary type) | **0.14** |
| Accuracy | 0.24 |
| Score MAE (typical) | **12–15** on 0–100 scale |

*Interpretation:* Open biosignal indices alone weakly predict primary type — consistent with Zhang et al. 2026 emphasis on **longitudinal + multimodal** data for transformation prediction.

---

## 5. Figures to attach

1. `python/notebooks/output/feature_score_heatmap.png` — biosignal ↔ constitution correlations  
2. `python/notebooks/output/constitution_distributions.png` — score distributions  
3. Screenshot of CCMQ web demo (localhost:3000 or deployed URL)

---

## 6. Proposed next steps (with your lab)

1. **Validate CCMQ scorer** against Zenodo SAS test rows (Phase A completion)  
2. **Scale pipeline** to BUCM 91K or CDUTCM 54K longitudinal cohort under DUA  
3. **Multimodal fusion:** questionnaire + tongue imaging / cognitive / imaging modalities (your lab’s strength)  
4. **Longitudinal labeling:** apply transition rules (e.g. Frontiers Table 3) on repeated TCMECQ measures  

---

## 7. What I offer

- Reproducible Python/TypeScript codebase with tests and open-DOI citations  
- Experience reproducing Su et al. 2019 open multimodal cohort  
- [Your skills: ML, neuroimaging, English writing, software engineering — customize]  

---

## 8. Contact

**[Your name]** · [email] · [GitHub URL]  
**Ethics:** [IRB approved / submission planned — customize]

*Export this page to PDF for email attachment (Notion / Google Docs / pandoc).*
