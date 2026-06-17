# Outreach Email Templates

Copy and adapt for your institution and project.

---

## Template A — BUCM / Wang Qi (CCMQ data)

**To:** `wangqi710@126.com`

**Subject:** Data access inquiry — CCMQ survey data (Chinese Medicine 2024, 91,145 cases)

```
Dear Prof. Wang,

I am [your role] at [institution], working on [brief project description — e.g. 
multi-modal analysis linking TCM constitution with brain imaging / cognitive outcomes].

Your team's work on the Constitution in Chinese Medicine Questionnaire (CCMQ) and 
large-scale surveys is directly relevant to our research. In particular, the 
91,145-case web-based survey described in your 2024 Chinese Medicine paper 
(doi:10.1186/s13020-024-00992-0) notes that data are available upon request.

We would like to inquire whether de-identified data sharing or a formal research 
collaboration might be possible under a data-use agreement. We have [IRB approval / 
planned ethics submission] and can provide our institution's collaboration framework 
if helpful.

Our team can contribute [describe what you offer — e.g. neuroimaging pipeline, 
cognitive assessment battery, multi-modal fusion methods].

Thank you for your consideration. I would welcome the opportunity to discuss further.

Best regards,
[Full name]
[Title, Institution]
[Email, Phone]
```

---

## Template B — CDUTCM / Mei Zhang (54,990 longitudinal dataset)

**To:** `zhangmei@cdutcm.edu.cn`

**Subject:** Collaboration inquiry — TCMECQ longitudinal cohort (Frontiers 2026, DOI 10.3389/fmed.2026.1698576)

```
Dear Prof. Zhang,

I am [your role] at [institution], working on [brief project — e.g. proactive 
health management using multi-modal TCM constitution data].

Your recent Frontiers in Medicine paper on machine learning prediction of body 
constitution transformation trends (doi:10.3389/fmed.2026.1698576) is highly 
relevant to our work. The 54,990-record longitudinal TCMECQ cohort from Deyang 
Public Health Center (2017–2024) addresses a gap we have been unable to fill with 
public datasets alone.

Your conclusion that models struggle to predict constitutional deterioration without 
multi-modal data aligns closely with our capabilities. We can contribute 
[brain imaging / cognitive testing / biochemical panels / other modalities].

Would you consider:
  1) De-identified data sharing under a collaboration agreement, or
  2) A joint analysis where our team provides complementary multi-modal data?

We are prepared to coordinate ethics approval with your committee (2021KL-055A) 
and execute a formal data-use agreement with the relevant custodians.

Thank you for your time. I look forward to hearing from you.

Best regards,
[Full name]
[Title, Institution]
[Email, Phone]
```

---

## Template C — Portfolio-backed PhD inquiry (Wang Qi **or** Mei Zhang)

Use after you have the GitHub repo + notebooks running. **Customize** `[brackets]`; send **separate** emails (do not CC both professors in one message).

**GitHub:** `[https://github.com/YOUR_USER/tcm-constitution-portfolio]`  
**One-page PDF:** export from `ONE_PAGE_PITCH.md` in this folder.

### Variant C1 — BUCM / Wang Qi (CCMQ focus)

**To:** `wangqi710@126.com`

**Subject:** PhD inquiry (2027 intake) — reproducible CCMQ pipeline + interest in 91K survey data

```
Dear Prof. Wang,

I am [name], [current role/institution], preparing PhD applications for 2027 intake in 
TCM constitution / health informatics.

I have been studying your team's CCMQ work and the 91,145-case web survey 
(doi:10.1186/s13020-024-00992-0). To prepare rigorously, I built an open, reproducible 
pipeline that implements CCMQ converted scoring (ZYYXH/T157-2009):

  • FastAPI scoring service + 60-item Next.js questionnaire demo
  • Validation path against Zenodo test data + official SAS reference (doi:10.5281/zenodo.4431679)
  • Mendeley N=274 multimodal baseline for context (doi:10.17632/cxtph3tjsg.1)

Code and notebooks: [GitHub URL]
  — python/notebooks/01_eda_mendeley.ipynb (cohort EDA)
  — python/notebooks/02_reproduce_su2019.ipynb (multimodal baselines)

On the open Mendeley cohort, biosignal-only models yield macro-F1 ≈ 0.14 for primary 
constitution type — underscoring the value of larger, questionnaire-grounded cohorts such 
as yours.

I would be grateful for the opportunity to discuss PhD supervision or research 
collaboration, including possible access to de-identified CCMQ survey data under a 
formal data-use agreement. I can share a one-page summary and am happy to align with 
your team's ethics requirements.

Thank you for your time.

Best regards,
[Full name]
[Email] · [Phone optional]
[GitHub URL]
```

### Variant C2 — CDUTCM / Mei Zhang (longitudinal + multimodal focus)

**To:** `zhangmei@cdutcm.edu.cn`

**Subject:** PhD inquiry (2027 intake) — multimodal constitution modeling + Deyang cohort

```
Dear Prof. Zhang,

I am [name], [current role/institution], preparing PhD applications for 2027 intake. 
Your Frontiers in Medicine paper on constitution transformation trends 
(doi:10.3389/fmed.2026.1698576) directly addresses a problem I reproduced on open data.

Using the Su et al. Mendeley cohort (N=274; doi:10.17632/cxtph3tjsg.1), I built an 
end-to-end research pipeline:

  • Unified data adapter + documented column dictionary (71 features)
  • EDA: biosignal ↔ constitution correlation structure (notebook 01)
  • Baselines: RF regression on 8 scores (MAE ≈ 12–15); primary-type macro-F1 ≈ 0.14 (notebook 02)

These results align with your finding that prediction without rich longitudinal and 
multi-modal inputs remains difficult. I would like to extend this work on the 
54,990-record Deyang TCMECQ cohort under a collaboration or data-use agreement.

Repository: [GitHub URL] · One-page summary attached.

I can contribute [reproducible ML pipelines / software engineering / English writing / 
your modality — customize]. Ethics coordination: [IRB status].

Thank you for considering my inquiry. I would welcome a brief conversation.

Best regards,
[Full name]
[Email]
[GitHub URL]
```

---

## Tips for outreach

- Cite the **specific paper and DOI** — shows you've read the work
- Mention **ethics status** upfront (approved or in progress)
- Offer **something in return** — Chinese health data access rarely works as a one-way request
- Do **not** mention startup or commercial product in the first academic email
- Link **specific repo paths** (notebooks, tests) — shows the work is real
- Attach or link **ONE_PAGE_PITCH.md** exported as PDF
- Be patient — responses may take weeks; follow up **once** after 2–3 weeks
- CC your **PI or department head** if pursuing formal MOU-level collaboration
