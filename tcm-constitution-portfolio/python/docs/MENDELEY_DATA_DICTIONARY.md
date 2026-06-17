# Mendeley 274 — Data dictionary & sources

Dataset: [Mendeley cxtph3tjsg v1](https://data.mendeley.com/datasets/cxtph3tjsg/1) (DOI [10.17632/cxtph3tjsg.1](https://doi.org/10.17632/cxtph3tjsg.1))

**File on disk:** `data/raw/mendeley_274/.../Share data.xls` — **274 rows × 71 columns**, all `float64`.

---

## Where official descriptions live

| Source | What it documents | URL |
|--------|-------------------|-----|
| **Mendeley record** | One-line description; no column glossary | https://data.mendeley.com/datasets/cxtph3tjsg/1 |
| **Associated paper (primary)** | Methods + **Tables** for tongue / voice / pulse indices and constitution scoring | [10.1016/j.eujim.2019.04.001](https://doi.org/10.1016/j.eujim.2019.04.001) — *European Journal of Integrative Medicine* |
| **Nine-Constitution / CCMQ standard** | Meaning of constitution types (阳虚, 阴虚, …) and 0–100 converted scores | Wang Qi CCMQ, ZYYXH/T157-2009 |
| **This repo — adapter** | Column grouping + Mendeley→CCMQ code map | `python/src/tcm_constitution/adapters/mendeley_274.py` |
| **This repo — research notes** | Portfolio context | `research/tcm-constitution-data-sources/PORTFOLIO-DESIGN.md` §1.2 |

**Important:** Mendeley’s page only says *“original data measured from subjects; names and birth dates deleted.”* **Per-column definitions are in the paper’s methods and tables**, not in the Excel file or Mendeley metadata.

---

## Constitution scores (8 columns)

Mendeley stores **eight biased-type converted scores** (0–100). There is **no 平和质 / GTC / Pinghe** column — balanced subjects must be inferred (all biased scores &lt; 30).

| Mendeley col | CCMQ code | Chinese | English |
|--------------|-----------|---------|---------|
| `YaD` | YaDC | 阳虚质 | Yang-deficiency |
| `YiD` | YiDC | 阴虚质 | Yin-deficiency |
| `QiDf` | QDC | 气虚质 | Qi-deficiency |
| `PW` | PDC | 痰湿质 | Phlegm-dampness |
| `WH` | DHC | 湿热质 | Damp-heat |
| `BS` | BSC | 血瘀质 | Blood-stasis |
| `SDa` | SDC | 特禀质 | Inherited-special |
| `QDp` | QSC | 气郁质 | Qi-stagnation |

Scoring instrument: **Nine-Constitution Scale** (paper); same family as CCMQ converted scores used nationally.

---

## Demographics (9)

| Column | Notes (from paper context) |
|--------|----------------------------|
| `gender` | Coded numeric in spreadsheet |
| `age` | Years |
| `education` | Ordinal / coded |
| `occupation` | Coded category |
| `chronic dz` | Chronic disease history (coded) |
| `surgery hx` | Surgery history (coded) |
| `BH` | Body height |
| `BW` | Body weight |
| `BMI` | Body mass index |

---

## Tongue (26)

### Color regions h2 / h3 (HSB/Lab-style indices)

Left / right tongue regions at two vertical bands (`h2` = upper?, `h3` = lower? — see paper Table for exact anatomical ROIs):

`h2LBL`, `h2LBM`, `h2LBD`, `h2RBL`, `h2RBM`, `h2RBD`,  
`h3LBL`, `h3LBM`, `h3LBD`, `h3RBL`, `h3RBM`, `h3RBD`

Suffix pattern: **L/R** = left/right, **BL/BM/BD** = color channels in the imaging pipeline (paper defines).

### Other tongue morphology

| Column | Likely meaning (verify in paper) |
|--------|----------------------------------|
| `RET L`, `RET_R` | Retina / tongue region metric (paper notation) |
| `tongue max width` | Maximum tongue width (pixels or mm) |
| `red dots` | Red spot count or area |
| `stasis dots` | Petechiae / stasis spot measure |
| `Proportion of scalloped tongue margin` | Scalloped (齿痕) margin % |
| `length of sublingal vein` | Sublingual vein length |
| `width of sublingal vein` | Sublingual vein width |
| `R`, `G`, `B`, `H`, `S`, `b` | Global tongue color (RGB + HSB) |

---

## Voice / acoustic (10)

| Column | Typical acoustic meaning (see paper) |
|--------|-------------------------------------|
| `Intensity` | Signal intensity |
| `MaxP`, `AvgP`, `MinP` | Pitch statistics |
| `ANZC` | Average zero-crossing rate |
| `VPV` | Vocal pulse volume / period variance |
| `VFF` | Vocal formant feature |
| `LSER`, `HSER` | Low / high spectral energy ratio |
| `MWTCI` | Mel-frequency weighted tonal centroid index (paper-specific) |

---

## Pulse (18)

| Column | Notes |
|--------|-------|
| `HR (/min)` | Heart rate |
| `sSA_*`, `tSA_*` | Systolic / temporal spectral area indices by tongue/pulse ROI (LBL/LBM/LBD × L/R) — paper Table |
| `SYS`, `DIA` | Systolic / diastolic blood pressure |
| `弦脈`, `澀脈`, `澀脈.1` | Wiry / rough pulse pattern indices (Chinese pulse types) |

---

## Code references

Column lists are enforced in:

```text
python/src/tcm_constitution/adapters/mendeley_274.py
  DEMOGRAPHIC_COLUMNS
  TONGUE_COLUMNS
  VOICE_COLUMNS
  PULSE_COLUMNS
  CONSTITUTION_COLUMN_MAP
```

Run EDA:

```bash
cd python
pip install -e ".[dev,notebooks]"
python scripts/run_eda_mendeley.py
jupyter notebook notebooks/01_eda_mendeley.ipynb
```

Outputs: `python/notebooks/output/*.png` and `top_correlations.csv`.
