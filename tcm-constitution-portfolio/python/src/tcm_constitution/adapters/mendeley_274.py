"""Load Su et al. 2019 Mendeley cohort (N=274, multimodal indices + constitution scores)."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from tcm_constitution.ccmq.scoring import CONSTITUTION_LABELS

PORTFOLIO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_DATA_DIR = PORTFOLIO_ROOT / "data" / "raw" / "mendeley_274"

DEMOGRAPHIC_COLUMNS = [
    "gender",
    "age",
    "education",
    "occupation",
    "chronic dz",
    "surgery hx",
    "BH",
    "BW",
    "BMI",
]

# Mendeley column -> internal CCMQ subscale code (8 biased types; no GTC in file)
CONSTITUTION_COLUMN_MAP: dict[str, str] = {
    "YaD": "YaDC",
    "YiD": "YiDC",
    "QiDf": "QDC",
    "PW": "PDC",
    "WH": "DHC",
    "BS": "BSC",
    "SDa": "SDC",
    "QDp": "QSC",
}

CONSTITUTION_COLUMNS = list(CONSTITUTION_COLUMN_MAP.keys())

TONGUE_COLUMNS = [
    "h2LBL",
    "h2LBM",
    "h2LBD",
    "h2RBL",
    "h2RBM",
    "h2RBD",
    "h3LBL",
    "h3LBM",
    "h3LBD",
    "h3RBL",
    "h3RBM",
    "h3RBD",
    "RET L",
    "RET_R",
    "tongue max width",
    "red dots",
    "stasis dots",
    "Proportion of scalloped tongue margin",
    "length of sublingal vein",
    "width of sublingal vein",
    "R",
    "G",
    "B",
    "H",
    "S",
    "b",
]

VOICE_COLUMNS = [
    "Intensity",
    "MaxP",
    "AvgP",
    "MinP",
    "ANZC",
    "VPV",
    "VFF",
    "LSER",
    "HSER",
    "MWTCI",
]

PULSE_COLUMNS = [
    "HR (/min)",
    "sSA_LBL",
    "sSA_LBM",
    "sSA_LBD",
    "sSA_RBL",
    "sSA_RBM",
    "sSA_RBD",
    "tSA_LBL",
    "tSA_LBM",
    "tSA_LBD",
    "tSA_RBL",
    "tSA_RBM",
    "tSA_RBD",
    "SYS",
    "DIA",
    "弦脈",
    "澀脈",
    "澀脈.1",
]

BIOSIGNAL_COLUMNS = TONGUE_COLUMNS + VOICE_COLUMNS + PULSE_COLUMNS


@dataclass(frozen=True)
class MendeleyCohort:
    """Normalized view of the Mendeley 274-subject spreadsheet."""

    raw: pd.DataFrame
    demographics: pd.DataFrame
    biosignals: pd.DataFrame
    constitution_scores: pd.DataFrame
    source_path: Path

    @property
    def n_subjects(self) -> int:
        return len(self.raw)

    def with_primary_type(self) -> pd.DataFrame:
        """Return raw rows plus derived primary constitution code and label."""
        out = self.raw.copy()
        primary = assign_primary_from_biased_scores(self.constitution_scores)
        out["primary_code"] = primary["primary_code"]
        out["primary_label"] = primary["primary_label"]
        out["primary_status"] = primary["primary_status"]
        out["max_biased_score"] = primary["max_biased_score"]
        return out


def find_share_data_xls(data_dir: Path | None = None) -> Path:
    root = data_dir or DEFAULT_DATA_DIR
    matches = sorted(root.rglob("Share data.xls"))
    if not matches:
        raise FileNotFoundError(
            f"Share data.xls not found under {root}. "
            "Run: bash python/scripts/download_data.sh"
        )
    return matches[0]


def load_mendeley_274(data_dir: Path | None = None) -> MendeleyCohort:
    """Load the Mendeley Excel file and split into demographic / biosignal / score blocks."""
    path = find_share_data_xls(data_dir)
    raw = pd.read_excel(path)
    raw.columns = [str(col).strip() for col in raw.columns]

    missing = set(CONSTITUTION_COLUMNS + DEMOGRAPHIC_COLUMNS) - set(raw.columns)
    if missing:
        raise ValueError(f"Mendeley file missing expected columns: {sorted(missing)}")

    biosignal_cols = [col for col in BIOSIGNAL_COLUMNS if col in raw.columns]
    constitution = raw[CONSTITUTION_COLUMNS].rename(columns=CONSTITUTION_COLUMN_MAP)

    return MendeleyCohort(
        raw=raw,
        demographics=raw[DEMOGRAPHIC_COLUMNS].copy(),
        biosignals=raw[biosignal_cols].copy(),
        constitution_scores=constitution,
        source_path=path,
    )


def assign_primary_from_biased_scores(scores: pd.DataFrame) -> pd.DataFrame:
    """
    Derive primary constitution from eight biased converted scores (no GTC in Mendeley file).

    Uses the highest biased score per subject. Status is 'yes' if score >= 40, else 'tendency'
    if >= 30, else 'no'. Subjects whose max biased score < 30 are labeled GTC (likely balanced).
    """
    biased_cols = [c for c in CONSTITUTION_COLUMN_MAP.values() if c in scores.columns]
    matrix = scores[biased_cols]
    max_scores = matrix.max(axis=1)
    primary_code = matrix.idxmax(axis=1)

    balanced_mask = max_scores < 30
    primary_code = primary_code.where(~balanced_mask, "GTC")

    primary_status = pd.Series("no", index=scores.index, dtype="object")
    primary_status[max_scores >= 30] = "tendency"
    primary_status[max_scores >= 40] = "yes"
    primary_status.loc[balanced_mask] = "yes"

    primary_label = primary_code.map(CONSTITUTION_LABELS)

    return pd.DataFrame(
        {
            "primary_code": primary_code,
            "primary_label": primary_label,
            "primary_status": primary_status,
            "max_biased_score": max_scores,
        }
    )
