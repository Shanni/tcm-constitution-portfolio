# Downloadable Data — Verified Links

Findings from MCP browser inspection + live URL verification (June 2026).

**Legend**

| Tag | Meaning |
|-----|---------|
| ✅ **Direct download** | File URL returns HTTP 200; no login required |
| 📄 **Paper PDF** | Full article PDF |
| 📋 **Supplementary** | Methods, tables, scoring rules — not raw cohort data |
| 🧪 **Sample/test data** | Small demo dataset for instrument validation |
| 🔒 **Request only** | Raw cohort not publicly hosted |

---

## Summary

| Category | Available? | Notes |
|----------|------------|-------|
| Raw 54,990 / 91,145 cohort records | 🔒 No | Contact authors (see [README.md](./README.md)) |
| CCMQ questionnaire instrument | ✅ Yes | PDF + supplementary tables |
| Scoring code (SAS/SPSS) + tiny test set | ✅ Yes | Zenodo — 14 rows |
| Cross-sectional study dataset (2026) | ✅ Yes | Zenodo SPSS — ~58 KB |
| Paper supplementary tables | ✅ Yes | Frontiers + Springer |
| Zenodo search "TCMECQ" | ❌ None | No public TCMECQ dump found |
| Figshare search | ❌ None | No relevant constitution datasets |
| Mendeley tongue+pulse+voice + constitution | ✅ Yes | 274 subjects — see §7 below |
| Dryad TMC-Tongue (舌象) | ✅ Yes | 6,719 images — 舌诊标签，非九体体质 |
| HuggingFace TCM 语料 | ✅ Yes | 无体质标签，可用于预训练/知识 |

---

## 7. Additional sources (expanded search, June 2026)

Beyond the BUCM/Chengdu cohorts documented earlier, these are the **best additional finds** from Mendeley, Dryad, Zenodo, paper trails, and clinical trial registries.

### 7.1 Mendeley — multimodal constitution (274 subjects) ⭐ NEW

**Best open dataset with actual constitution labels + biosignals.**

| Field | Value |
|-------|-------|
| Title | Diagnosis of TCM constitution by integrating tongue, acoustic sound, and pulse |
| DOI | [10.17632/cxtph3tjsg.1](https://doi.org/10.17632/cxtph3tjsg.1) |
| Page | https://data.mendeley.com/datasets/cxtph3tjsg/1 |
| Paper | [Computers in Biology and Medicine, 2019](https://doi.org/10.1016/j.compbiomed.2019.04.001) |
| N | **274 volunteers** (China Medical University Hospital, Taiwan) |
| Modalities | Tongue image indices + acoustic sound + pulse waveform + **Nine-Constitution Scale scores** |
| License | **CC BY 4.0** |

**Download:** Click "Download All" on Mendeley page (free account may be required).

**Use case:** Multimodal constitution prediction prototype; much richer than Zenodo 14-row test set, but far smaller than BUCM/Chengdu cohorts.

---

### 7.2 Dryad — TMC-Tongue tongue image dataset (2026)

| Field | Value |
|-------|-------|
| Title | TMC-Tongue: standardized tongue image dataset with pathological annotations |
| DOI | [10.5061/dryad.1c59zw48r](https://doi.org/10.5061/dryad.1c59zw48r) |
| Size | **2.34 GB** |
| N | 6,719 images (train 5594 / val 572 / test 553) |
| Labels | 21 tongue pathology categories (红舌、胖大舌、黄苔等) — **NOT** 9-type constitution |
| License | Open on Dryad |

**Use case:** Tongue imaging pipeline; pair with CCMQ questionnaire separately. Related papers (1374-case, 1149-case) use similar data but keep labels **request-only**.

---

### 7.3 Japanese CCMQ cross-sectional (851 subjects)

| Field | Value |
|-------|-------|
| Paper | [Eur Rev Med Pharmacol Sci 2026](https://doi.org/10.26355/eurrev_202601_37644) — Japanese 5-constitution / 18-item CCMQ |
| N | 851 healthy Japanese participants (60-item CCMQ) |
| PDF | https://www.europeanreview.org/wp/wp-content/uploads/4-14.pdf |
| Raw data | 🔒 Not clearly open — paper + Supplementary Table I (18 items) downloadable |

**Use case:** Cross-cultural CCMQ validation; instrument design reference.

---

### 7.4 Zenodo — already documented (quick ref)

| Record | N | Link |
|--------|---|------|
| 4431679 | 14 rows test + SAS/SPSS | https://zenodo.org/records/4431679 |
| 18779514 | Cross-sectional SPSS (.sav) | https://zenodo.org/records/18779514 |

---

### 7.5 Related TCM datasets (NOT constitution-labeled)

Useful for adjacent work (tongue AI, TCM LLM) but **do not replace** constitution cohorts:

| Source | What | Link |
|--------|------|------|
| ShizhenGPT pretrain | 5B+ tokens TCM text + 1M+ image-text pairs | [HuggingFace](https://huggingface.co/datasets/FreedomIntelligence/TCM-Pretrain-Data-ShizhenGPT) |
| ShenNong-TCM | TCM QA / instruction data | [HuggingFace](https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset) |
| TCMChat | TCM chatbot SFT data | [GitHub / HF](https://github.com/ZJUFanLab/TCMChat) |
| TCMID | Herb–target database | [Zenodo 8066910](https://zenodo.org/records/8066910) |

---

### 7.6 Papers with large cohorts — request only

| Study | N | Modality | Access |
|-------|---|----------|--------|
| Liu et al. 2025 tongue ML | 1,374 | Tongue image + 9 constitution | 🔒 Corresponding author upon request |
| Mei Zhao et al. 2024 (THC) | 1,149 | Tongue features + constitution | 🔒 Request |
| Wang Qi web survey 2024 | 91,145 | CCMQ questionnaire | 🔒 `wangqi710@126.com` |
| Zhang et al. 2026 longitudinal | 54,990 | TCMECQ longitudinal | 🔒 `zhangmei@cdutcm.edu.cn` |
| Bai et al. 2020 distribution | 108,015 | CCMQ epidemiology | 🔒 Paper aggregates only |
| TongueVLM (JMIR 2026) | Custom multimodal | Tongue + constitution reasoning | 🔒 Not publicly released |

---

### 7.7 Upcoming / trial registries (future data)

| Trial | N (planned) | Content | Status |
|-------|-------------|---------|--------|
| [NCT06525025](https://clinicaltrials.gov/study/NCT06525025) | 80,000 total; **20,000 constitution** | Tongue + face + CCMQ + dialogue | Sun Yat-sen U Fifth Hospital; est. complete ~Aug 2026 |
| [NCT03653182](https://clinicaltrials.gov/study/NCT03653182) | 200 | Tongue + pulse + voice + questionnaire | Taiwan CMU Hospital; completed, data not public |

Worth monitoring NCT06525025 — may become a major open or collaboration source after trial completion.

---

### 7.8 Recommended stack for your situation (no advisor yet)

| Priority | Dataset | Why |
|----------|---------|-----|
| 1 | Mendeley **cxtph3tjsg** (274) | Real constitution labels + multimodal — best open cohort |
| 2 | Zenodo **4431679** + CCMQ PDF | Learn official scoring pipeline |
| 3 | Dryad **TMC-Tongue** | Scale up tongue imaging skills |
| 4 | Zenodo **18779514** | Practice SPSS/constitution + mental health analysis |
| 5 | Frontiers **1698576** supplementary tables | Understand longitudinal transition labeling |
| 6 | Email Zhang / Wang | Large cohorts + potential PhD |

---

## Tier 1 — Actual datasets (individual-level records)

### 1. CCMQ test dataset + scoring scripts (Zenodo)

**Best public starting point for working with CCMQ response data.**

| Field | Value |
|-------|-------|
| Title | SAS code and SPSS syntax files for the assessment of body constitution based on the CCMQ |
| DOI | [10.5281/zenodo.4431679](https://doi.org/10.5281/zenodo.4431679) |
| Record | https://zenodo.org/records/4431679 |
| Authors | Hsu Chia-Wen, Lu Ming-Chi, Koo Malcolm |
| Uploaded | January 2021 |

| File | Size | Direct download URL | Contents |
|------|------|---------------------|----------|
| `TEST_DATA.xlsx` | 14 KB | https://zenodo.org/api/records/4431679/files/TEST_DATA.xlsx/content | **14 rows** × 63 cols (demo/test set, not epidemiological cohort) |
| `CCMQ SAS code.sas` | 31 KB | https://zenodo.org/api/records/4431679/files/CCMQ%20SAS%20code.sas/content | SAS scoring pipeline |
| `CCMQ SPSS syntax.sps` | 24 KB | https://zenodo.org/api/records/4431679/files/CCMQ%20SPSS%20syntax.sps/content | SPSS scoring pipeline |

```bash
# Download all three files
curl -LO "https://zenodo.org/api/records/4431679/files/TEST_DATA.xlsx/content"
curl -LO "https://zenodo.org/api/records/4431679/files/CCMQ%20SAS%20code.sas/content"
curl -LO "https://zenodo.org/api/records/4431679/files/CCMQ%20SPSS%20syntax.sps/content"
```

---

### 2. Cross-sectional TCM constitution + mental health dataset (Zenodo, 2026)

| Field | Value |
|-------|-------|
| Title | Association of physical activity with anxiety and depression: Mediation by balanced TCM body constitution in a cross-sectional study |
| DOI | [10.5281/zenodo.18779514](https://doi.org/10.5281/zenodo.18779514) |
| Record | https://zenodo.org/records/18779514 |
| Author | Koo Malcolm |
| Uploaded | February 2026 |

| File | Size | Direct download URL | Format |
|------|------|---------------------|--------|
| `dataset_phyact_Psychodistress_TCMBC.sav` | 58 KB | https://zenodo.org/api/records/18779514/files/dataset_phyact_Psychodistress_TCMBC.sav/content | SPSS (.sav) |

Contains physical activity, psychological distress, and TCM body constitution variables for one cross-sectional study (not the BUCM/Chengdu mega-cohorts).

```bash
curl -LO "https://zenodo.org/api/records/18779514/files/dataset_phyact_Psychodistress_TCMBC.sav/content"
```

---

## Tier 2 — Questionnaires & instruments (direct download)

### 3. Full CCMQ questionnaire PDF (Wang Qi)

| Field | Value |
|-------|-------|
| Description | 60-item Body Constitution in TCM Questionnaire + consent form |
| Source paper | Frontiers supplementary (article 723118) |
| Size | 518 KB |

**Direct download:**  
https://public-pages-files-2025.frontiersin.org/articles/723118/file/data_sheet_2.pdf/723118_supplementary-materials_datasheets_2_pdf/1

---

### 4. CCMQ item reference table (Springer supplementary)

From the 91,145-case ML paper (Wang Qi team). Contains all 60 items with abbreviations and constitution scale mappings — **not patient data**.

| Field | Value |
|-------|-------|
| Paper | Machine learning-assisted rapid determination for TCM Constitution |
| DOI | [10.1186/s13020-024-00992-0](https://doi.org/10.1186/s13020-024-00992-0) |
| File | `13020_2024_992_MOESM1_ESM.docx` |
| Size | 1.3 MB |

**Direct download:**  
https://static-content.springer.com/esm/art%3A10.1186%2Fs13020-024-00992-0/MediaObjects/13020_2024_992_MOESM1_ESM.docx

---

## Tier 3 — Paper supplementary tables (not raw cohorts)

### 5. Chengdu 54,990-record ML study (Frontiers 2026)

Verified via MCP browser on the live article page. These are **expert consensus tables and methods** — not the 54,990 patient records.

| File | Size | Direct download URL | Contents (verified) |
|------|------|---------------------|---------------------|
| `Table_1.docx` | 23 KB | https://public-pages-files-2025.frontiersin.org/articles/1698576/file/table_1.docx/1698576_table_1/1 | Supplementary Table 1 |
| `Table_2.docx` | 25 KB | https://public-pages-files-2025.frontiersin.org/articles/1698576/file/table_2.docx/1698576_table_2/1 | Supplementary Table 2 |
| `Table_3.xlsx` | 22 KB | https://public-pages-files-2025.frontiersin.org/articles/1698576/file/table_3.xlsx/1698576_table_3/1 | Expert Delphi consensus matrices (81 constitution transitions, ~46 rows) |
| `Table_4.docx` | 22 KB | https://public-pages-files-2025.frontiersin.org/articles/1698576/file/table_4.docx/1698576_table_4/1 | Supplementary Table 4 |

**Paper PDF:**  
https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1698576/pdf

**Data availability (from paper):** Raw cohort → contact `zhangmei@cdutcm.edu.cn`

```bash
# Download all supplementary files
BASE="https://public-pages-files-2025.frontiersin.org/articles/1698576/file"
curl -LO "$BASE/table_1.docx/1698576_table_1/1" -o Table_1.docx
curl -LO "$BASE/table_2.docx/1698576_table_2/1" -o Table_2.docx
curl -LO "$BASE/table_3.xlsx/1698576_table_3/1" -o Table_3.xlsx
curl -LO "$BASE/table_4.docx/1698576_table_4/1" -o Table_4.docx
```

---

### 6. 21,948-case short-form CCMQ paper (PMC)

| Field | Value |
|-------|-------|
| PMCID | [PMC10164641](https://pmc.ncbi.nlm.nih.gov/articles/PMC10164641/) |
| PDF | https://pmc.ncbi.nlm.nih.gov/articles/PMC10164641/pdf/JTCM-42-1-122.pdf (2.9 MB) |

Tables are embedded in the HTML article (no separate supplementary file bundle). Aggregate statistics only — raw 21,948 records not downloadable.

---

## Tier 4 — Not downloadable (confirmed)

| Dataset | Size | Why not public | How to get |
|---------|------|----------------|------------|
| Chengdu Deyang longitudinal cohort | 54,990 | Held by Deyang Public Health Center + CDUTCM hospital | Email `zhangmei@cdutcm.edu.cn` |
| Wang Qi web survey | 91,145 | "Available from Prof Qi Wang upon request" | Email `wangqi710@126.com` |
| BUCM national surveys | 108,015 – 129,963 | Published aggregates only | Collaboration with BUCM |
| TCMECQ elderly screening records | Millions (national program) | Government public health system | Institutional MOU required |

---

## Repository searches (MCP + API)

| Repository | Query | Result |
|------------|-------|--------|
| Zenodo | `CCMQ constitution` | 1 hit: record 4431679 (test data + code) |
| Zenodo | `TCMECQ` | 0 hits |
| Zenodo | `traditional chinese medicine body constitution` | 2 relevant: 4431679 + 18779514 |
| Figshare | `constitution chinese medicine questionnaire` | No TCM constitution datasets found |
| PMC | `PMC3655622` (HK CCMQ validation) | reCAPTCHA blocked automated access |

---

## Recommended download order for a new project

1. **Zenodo 4431679** — `TEST_DATA.xlsx` + SAS/SPSS code (learn scoring pipeline)
2. **Frontiers PDF 723118** — full CCMQ questionnaire text
3. **Springer MOESM1.docx** — item abbreviation reference for all 60 questions
4. **Frontiers 1698576 Table_3.xlsx** — expert consensus on constitution transition labels
5. **Zenodo 18779514** — real (small) cross-sectional `.sav` dataset for pipeline testing
6. **Contact authors** — for 54K longitudinal or 91K cross-sectional cohorts

---

## MCP tools used

- **cursor-ide-browser** — navigated Frontiers, Springer, Zenodo, PMC article pages; extracted download links via CDP
- **Shell (curl)** — verified HTTP 200, file sizes, and probed xlsx row counts
- **Zenodo REST API** — `https://zenodo.org/api/records/{id}` for file metadata

*Verified: June 16, 2026*
