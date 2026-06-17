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

## Template C — Portfolio-backed PhD inquiry (Shan Liu · 2027 intake)

**GitHub:** https://github.com/Shanni/tcm-constitution-portfolio  
**Email:** shan.liu.s3@gmail.com  
**One-page PDF:** 中国学校用 [ONE_PAGE_PITCH_ZH.md](./ONE_PAGE_PITCH_ZH.md) · 海外用 [ONE_PAGE_PITCH_EN.md](./ONE_PAGE_PITCH_EN.md)

Send **separate** emails to Wang Qi and Mei Zhang (do not CC both).

---

### Variant C1 — BUCM / 王琦（中文 · 推荐）

**To:** `wangqi710@126.com`

**主题：** 2027年博士咨询——CCMQ可复现计分流程与9.1万例调查数据合作意向

```
王琦教授，您好！

我是刘闪（Shan Liu），不列颠哥伦比亚大学（UBC）硕士毕业，计划申请2027年入学博士研究生，
研究方向为中医体质辨识与健康信息学。

近期我系统学习了您团队关于《中医体质量表（CCMQ）》的工作，特别是2024年Chinese Medicine
论文中9.1万例网络调查数据（doi:10.1186/s13020-024-00992-0）。为严谨准备，我已搭建
可复现的开源研究流程，实现 ZYYXH/T157-2009 转化分计分规则：

  • FastAPI 计分服务 + 60题 Next.js 问卷演示
  • 对照 Zenodo 官方测试数据与 SAS 参考代码（doi:10.5281/zenodo.4431679）
  • 在 Mendeley 274例公开多模态队列上完成探索性分析与基线模型（doi:10.17632/cxtph3tjsg.1）

代码与笔记本：https://github.com/Shanni/tcm-constitution-portfolio
  — notebooks/01_eda_mendeley.ipynb（队列EDA）
  — notebooks/02_reproduce_su2019.ipynb（多模态基线，macro-F1≈0.14）

公开数据上的结果表明，仅靠舌声脉指标难以准确预测主导体质，更凸显贵组大规模
CCMQ 问卷队列的价值。我非常希望有机会在您的指导下开展博士研究，或在签署数据
使用协议的前提下，使用去标识化的CCMQ调查数据开展合作研究。

附件为一页研究摘要（中文版）。如需英文版或线上演示，我可随时补充。恳请教授指正，
期待您的回复！

此致
敬礼

刘闪（Shan Liu）
UBC 硕士
shan.liu.s3@gmail.com
https://github.com/Shanni/tcm-constitution-portfolio
```

---

### Variant C2 — CDUTCM / 张美（中文 · 推荐）

**To:** `zhangmei@cdutcm.edu.cn`

**主题：** 2027年博士咨询——体质转化预测与德阳5.5万例TCMECQ队列合作

```
张美教授，您好！

我是刘闪（Shan Liu），不列颠哥伦比亚大学（UBC）硕士毕业，计划申请2027年博士研究生。
拜读了您团队在 Frontiers in Medicine 发表的体质转化趋势预测研究
（doi:10.3389/fmed.2026.1698576），与我在公开数据上的复现工作高度契合。

基于 Su 等公开的 Mendeley 274例多模态队列（doi:10.17632/cxtph3tjsg.1），我已完成：

  • 统一数据适配器与71维变量说明文档
  • 探索性分析：生物信号与8种偏颇体质分的相关结构（notebook 01）
  • 基线模型：Random Forest 回归（MAE约12–15）与主导体质分类（macro-F1≈0.14，notebook 02）

上述结果与贵文关于缺乏纵向、多模态数据时预测困难的结论一致。我希望在德阳
54,990例 TCMECQ  longitudinal 队列上延续这一工作，探讨数据共享或联合分析的可能。

开源仓库：https://github.com/Shanni/tcm-constitution-portfolio
附件：一页研究摘要（中文版）。

我可以提供可复现的机器学习流程、软件工程实现及英文写作支持，并配合贵组伦理
与数据管理要求。如蒙允准，非常希望能与您简短交流。

此致
敬礼

刘闪（Shan Liu）
UBC 硕士
shan.liu.s3@gmail.com
https://github.com/Shanni/tcm-constitution-portfolio
```

---

### Variant C1-EN — BUCM / Wang Qi (English backup)

**To:** `wangqi710@126.com`

**Subject:** PhD inquiry (2027 intake) — reproducible CCMQ pipeline + interest in 91K survey data

```
Dear Prof. Wang,

I am Shan Liu, an M.Sc. graduate from the University of British Columbia (UBC), preparing 
PhD applications for 2027 intake in TCM constitution / health informatics.

I have been studying your team's CCMQ work and the 91,145-case web survey 
(doi:10.1186/s13020-024-00992-0). To prepare rigorously, I built an open, reproducible 
pipeline implementing CCMQ converted scoring (ZYYXH/T157-2009):

  • FastAPI scoring service + 60-item Next.js questionnaire demo
  • Validation path against Zenodo test data + official SAS reference (doi:10.5281/zenodo.4431679)
  • Mendeley N=274 multimodal baseline (doi:10.17632/cxtph3tjsg.1)

Code and notebooks: https://github.com/Shanni/tcm-constitution-portfolio

On the open Mendeley cohort, biosignal-only models yield macro-F1 ≈ 0.14 for primary 
constitution type — underscoring the value of larger, questionnaire-grounded cohorts such 
as yours.

I would be grateful for the opportunity to discuss PhD supervision or research 
collaboration, including possible access to de-identified CCMQ survey data under a 
formal data-use agreement. A one-page summary (Chinese and English) is attached.

Thank you for your time.

Best regards,
Shan Liu
M.Sc., University of British Columbia
shan.liu.s3@gmail.com
https://github.com/Shanni/tcm-constitution-portfolio
```

---

### Variant C2-EN — CDUTCM / Mei Zhang (English backup)

**To:** `zhangmei@cdutcm.edu.cn`

**Subject:** PhD inquiry (2027 intake) — multimodal constitution modeling + Deyang cohort

```
Dear Prof. Zhang,

I am Shan Liu, an M.Sc. graduate from the University of British Columbia (UBC), preparing 
PhD applications for 2027 intake. Your Frontiers in Medicine paper on constitution 
transformation trends (doi:10.3389/fmed.2026.1698576) directly addresses a problem I 
reproduced on open data.

Using the Su et al. Mendeley cohort (N=274; doi:10.17632/cxtph3tjsg.1), I built an 
end-to-end research pipeline:

  • Unified data adapter + documented column dictionary (71 features)
  • EDA: biosignal ↔ constitution correlation structure (notebook 01)
  • Baselines: RF regression (MAE ≈ 12–15); primary-type macro-F1 ≈ 0.14 (notebook 02)

These results align with your finding that prediction without rich longitudinal and 
multi-modal inputs remains difficult. I would like to extend this work on the 
54,990-record Deyang TCMECQ cohort under a collaboration or data-use agreement.

Repository: https://github.com/Shanni/tcm-constitution-portfolio

I can contribute reproducible ML pipelines, software engineering, and English writing. 
A one-page summary is attached.

Thank you for considering my inquiry.

Best regards,
Shan Liu
M.Sc., University of British Columbia
shan.liu.s3@gmail.com
https://github.com/Shanni/tcm-constitution-portfolio
```

---

## Tips for outreach

- Cite the **specific paper and DOI** — shows you've read the work
- Mention **ethics status** upfront (approved or in progress)
- Offer **something in return** — Chinese health data access rarely works as a one-way request
- Do **not** mention startup or commercial product in the first academic email
- Link **specific repo paths** (notebooks, tests) — shows the work is real
- Attach **ONE_PAGE_PITCH_ZH.pdf** for 中国高校; optionally attach EN version too
- Be patient — responses may take weeks; follow up **once** after 2–3 weeks
- CC your **PI or department head** if pursuing formal MOU-level collaboration
