# TCM Constitution Data Sources — Research Notes

Documentation of publicly available resources, key contacts, and data-access paths for Traditional Chinese Medicine (TCM) body constitution datasets. Compiled June 2026.

---

## Summary

| Source | Key person | Cohort size | Raw data public? | Primary contact |
|--------|------------|-------------|------------------|-----------------|
| Beijing University of Chinese Medicine (BUCM) | Prof. Wang Qi | 21,948 – 129,963+ (multiple studies) | No — request only | `wangqi710@126.com` |
| Chengdu University of TCM | Prof. Mei Zhang (corresponding author) | 54,990 longitudinal records | No — request only | `zhangmei@cdutcm.edu.cn` |

**Bottom line:** Questionnaires, scoring rules, and published aggregates are public. Individual-level clinical records require collaboration, ethics approval, and a data-use agreement.

---

## 1. Beijing University of Chinese Medicine (BUCM)

### Why contact them

- Prof. Wang Qi developed the **9-constitution CCMQ standard** (Constitution in Chinese Medicine Questionnaire).
- BUCM holds **30+ years** of constitution research data across multiple national surveys.
- The 2009 industry standard **ZYYXH/T157-2009** and newer national standard **GB/T 46939—2025** originate from this group.

### How to find them

| Resource | URL |
|----------|-----|
| National Institute of TCM Constitution and Preventive Medicine | https://tizhi.bucm.edu.cn/ |
| Wang Qi faculty page (BUCM) | https://jichu.bucm.edu.cn/yjsjy/dsjs/zytzx/29971840767e477d90fcd0fe94dbbe6e.htm |
| TCM Constitution Identification Key Lab (BUCM research office) | https://kjc.bucm.edu.cn/kypt/jd/98d514fd025f472a96fe39dc1c52b57b.htm |

### Contact

- **Email:** `wangqi710@126.com` (listed on official BUCM pages)
- **Address:** Beijing University of Chinese Medicine, Chaoyang District, Beijing
- **Secondary contacts:** Co-authors on Wang Qi papers — Minghua Bai, Ji Wang, Ling-Ru Li, Dongran Han

### Documented datasets

| Dataset | Size | Source paper | Raw data access |
|---------|------|--------------|-----------------|
| 9-province epidemiological survey | 21,948 | [PMC10164641](https://pmc.ncbi.nlm.nih.gov/articles/PMC10164641/) | Not downloadable |
| Web-based CCMQ survey | 91,145 valid (94,718 collected) | [Chinese Medicine 2024](https://cmjournal.biomedcentral.com/articles/10.1186/s13020-024-00992-0) | **"Available from Prof Qi Wang upon request"** |
| National survey (broader) | 129,963 | [Science of Traditional Chinese Medicine review](https://journals.lww.com/stcm/fulltext/2024/03000/remarkable_research_achievements_in_traditional.2.aspx) | Not downloadable |

### What you can download without permission

- Full 60-item CCMQ questionnaire: [Frontiers supplementary PDF](https://www.frontiersin.org/api/v4/articles/723118/file/Data_Sheet_2.PDF/723118_supplementary-materials_datasheets_2_pdf/1)
- Short-form CCMQ versions: [PMC10617149](https://pmc.ncbi.nlm.nih.gov/articles/PMC10617149/)
- Validation and psychometrics: [PMC3655622](https://pmc.ncbi.nlm.nih.gov/articles/PMC3655622/)

---

## 2. Chengdu University of Traditional Chinese Medicine (CDUTCM)

### Why contact them

- Holds the **largest published ML + longitudinal constitution dataset** (54,990 records).
- Paper explicitly calls for **multi-modal data** (labs, imaging, cognition) to improve prediction of constitutional deterioration.
- Data spans **2017–2024** from China's National Basic Public Health Service program for elderly TCM screening.

### Key paper

**Title:** Application of machine learning methods in prediction of the body constitution types and transformation trends of traditional Chinese medicine: from the datasets of questionnaire survey on elderly people in Southwest China

| Field | Value |
|-------|-------|
| Journal | Frontiers in Medicine, January 2026 |
| DOI | [10.3389/fmed.2026.1698576](https://doi.org/10.3389/fmed.2026.1698576) |
| Full text | https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1698576/full |
| PubMed | https://pubmed.ncbi.nlm.nih.gov/41626222/ |
| Ethics approval | Affiliated Hospital of CDUTCM, No. **2021KL-055A** |

### Authors and roles

| Author | Affiliation | Role |
|--------|-------------|------|
| **Mei Zhang** ★ | School of Management / Clinical Medicine, CDUTCM | **Corresponding author** — contact for data |
| Fei Wang | School of Clinical Medicine, CDUTCM | Co-author (not corresponding author) |
| Yuzhi Huo, Jia Wang | CDUTCM / collaborating institutions | Equal first authors |
| Yang Zhao | CDUTCM | Co-author |

> **Note:** Fei Wang (paper) is likely a different person from 王飞 (Wang Fei), the well-known respiratory/geriatric professor at the same hospital. Use the paper affiliation to disambiguate.

### Contact

- **Primary (data requests):** Mei Zhang — `zhangmei@cdutcm.edu.cn`
- **Institution:** https://www.cdutcm.edu.cn/
- **Hospital (ethics holder):** Affiliated Hospital of Chengdu University of TCM

### Where the data actually lives

The raw records are **not in a public repository**. Custodians include:

1. **Deyang Public Health Center** — internal cohort, 2017–2024 (54,990 records)
2. **Affiliated Hospital of CDUTCM** — ethics and research oversight
3. **External validation sites** — Shanghai (1,467 records) and Santai (714 records), July 2023 – October 2024

### Data availability statement (from paper)

> *"The original contributions presented in the study are included in the article/Supplementary material, further inquiries can be directed to the corresponding author."*

Available publicly: methods, supplementary tables, constitution transformation definitions. **Not available:** de-identified individual records.

### Instrument used

**TCMECQ** (Traditional Chinese Medicine Elderly Constitution Questionnaire) — based on Wang Qi's 9-type national standard (ZYYXH/T157-2009). Nine types: Balanced, Qi-deficiency, Yang-deficiency, Yin-deficiency, Phlegm-dampness, Damp-heat, Blood-stasis, Qi-stagnation, Inherited-special.

---

## 3. Downloadable data

**See [DOWNLOADABLE-DATA.md](./DOWNLOADABLE-DATA.md) for verified direct-download links** (MCP browser + live URL checks, June 2026).

Quick highlights:

| What | Direct download? |
|------|------------------|
| CCMQ test dataset (14 rows) + SAS/SPSS code | ✅ [Zenodo 4431679](https://zenodo.org/records/4431679) |
| Cross-sectional TCM constitution SPSS dataset | ✅ [Zenodo 18779514](https://zenodo.org/records/18779514) |
| Full CCMQ questionnaire PDF | ✅ [Frontiers supplementary PDF](https://public-pages-files-2025.frontiersin.org/articles/723118/file/data_sheet_2.pdf/723118_supplementary-materials_datasheets_2_pdf/1) |
| 54,990-record paper supplementary tables | ✅ Tables 1–4 (methods/consensus, not raw records) |
| Raw 54K / 91K cohort records | 🔒 Request from authors |

### Other public resources (papers & instruments)

| Resource | Description | Link |
|----------|-------------|------|
| CCMQ short-form development | 21,948-case methods | [PMC10164641](https://pmc.ncbi.nlm.nih.gov/articles/PMC10164641/) |
| CCMQ short-form evaluation | Psychometric validation | [PMC10617149](https://pmc.ncbi.nlm.nih.gov/articles/PMC10617149/) |
| CCMQ Hong Kong validation | Cross-cultural validation | [PMC3655622](https://pmc.ncbi.nlm.nih.gov/articles/PMC3655622/) |
| ML-assisted CCMQ (91K survey) | Methods; data on request | [BioMed Central 2024](https://cmjournal.biomedcentral.com/articles/10.1186/s13020-024-00992-0) |
| Longitudinal ML study (54K elderly) | Methods; contact Zhang | [Frontiers 2026](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1698576/full) |
| TCM constitution theory review | BUCM research overview | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2095754817301679) |

---

## 4. How to request data access

Chinese health record data typically requires:

1. **Formal collaboration** — university-to-university MOU strengthens applications
2. **Ethics approval** — in China and/or your home institution
3. **Data Use Agreement (DUA)** — with the data custodian (often hospital or public health center, not just the professor)
4. **Mutual value** — offering multi-modal data (brain imaging, cognitive tests, lab panels) aligns with what the Chengdu team says they need

### Recommended first contacts

| Goal | Contact | Reference to cite |
|------|---------|-------------------|
| CCMQ instrument + large cross-sectional surveys | `wangqi710@126.com` | Chinese Medicine 2024 (91,145 cases) |
| Longitudinal elderly constitution + ML | `zhangmei@cdutcm.edu.cn` | Frontiers 2026, DOI 10.3389/fmed.2026.1698576 |

See [outreach-templates.md](./outreach-templates.md) for draft emails.

---

## 5. Search strategy (for finding more sources)

Useful queries:

```
"Constitution in Chinese Medicine Questionnaire" data availability
"TCMECQ" OR "CCMQ" dataset
"Wang Qi" "upon request"
site:pmc.ncbi.nlm.nih.gov constitution Chinese medicine questionnaire
site:frontiersin.org body constitution machine learning
```

Workflow:

1. Find paper → read **Data Availability** section
2. If no public repo → email **corresponding author**
3. Verify email on **university faculty page**
4. Identify **institutional data owner** (hospital, public health center)
5. Propose collaboration + ethics + DUA

---

## 6. Related standards

| Standard | Description |
|----------|-------------|
| ZYYXH/T157-2009 | Industry standard: Classification and Determination of Constitution in TCM (9 types) |
| GB/T 46939—2025 | New national standard; BUCM-led rollout from April 2026 |

---

*Last updated: June 2026*
