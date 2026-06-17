"""CCMQ scoring per ZYYXH/T157-2009 (converted score + primary type assignment)."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

CATALOG_PATH = Path(__file__).with_name("items.json")

CONSTITUTION_ORDER = [
    "GTC",
    "QDC",
    "YaDC",
    "YiDC",
    "PDC",
    "DHC",
    "BSC",
    "QSC",
    "SDC",
]

CONSTITUTION_LABELS = {
    "GTC": "Balanced (Pinghe)",
    "QDC": "Qi-deficiency",
    "YaDC": "Yang-deficiency",
    "YiDC": "Yin-deficiency",
    "PDC": "Phlegm-dampness",
    "DHC": "Damp-heat",
    "BSC": "Blood-stasis",
    "QSC": "Qi-stagnation",
    "SDC": "Inherited-special",
}


@lru_cache(maxsize=1)
def load_ccmq_catalog() -> dict[str, Any]:
    with CATALOG_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def _normalize_responses(responses: dict[str | int, int]) -> dict[int, int]:
    normalized: dict[int, int] = {}
    for key, value in responses.items():
        item_id = int(str(key).upper().replace("Q", ""))
        if not 1 <= item_id <= 60:
            raise ValueError(f"Invalid item id: {key}")
        if value not in (1, 2, 3, 4, 5):
            raise ValueError(f"Item Q{item_id} must be 1-5, got {value}")
        normalized[item_id] = value
    return normalized


def _item_score(raw: int, *, reverse: bool) -> int:
    return 6 - raw if reverse else raw


def compute_converted_scores(responses: dict[str | int, int]) -> dict[str, float]:
    """Return 0-100 converted scores for each of the nine constitution subscales."""
    catalog = load_ccmq_catalog()
    subscale_items: dict[str, list[int]] = catalog["subscale_items"]
    constitution_meta: dict[str, dict[str, Any]] = catalog["constitutions"]
    answers = _normalize_responses(responses)

    missing = [item_id for item_id in range(1, 61) if item_id not in answers]
    if missing:
        preview = ", ".join(f"Q{i}" for i in missing[:5])
        suffix = "..." if len(missing) > 5 else ""
        raise ValueError(f"Missing responses for {len(missing)} items: {preview}{suffix}")

    scores: dict[str, float] = {}
    for code in CONSTITUTION_ORDER:
        items = subscale_items[code]
        reverse = constitution_meta[code]["reverse_in_scale"]
        raw_sum = sum(_item_score(answers[item_id], reverse=reverse) for item_id in items)
        n_items = len(items)
        scores[code] = round(((raw_sum - n_items) / (n_items * 4)) * 100, 2)
    return scores


def assign_primary_constitution(converted: dict[str, float]) -> dict[str, Any]:
    """
    Apply national standard thresholds:
    - GTC yes: GTC >= 60 and all biased types < 30
    - Biased yes: score >= 40
    - Biased tendency: 30 <= score < 40
    """
    biased = {k: v for k, v in converted.items() if k != "GTC"}
    max_biased = max(biased.values()) if biased else 0.0

    is_balanced = converted["GTC"] >= 60 and all(score < 30 for score in biased.values())

    if is_balanced:
        primary = "GTC"
        status = "yes"
    else:
        candidates = [
            (code, score)
            for code, score in biased.items()
            if score >= 40 or (score >= 30 and score == max_biased and score >= 30)
        ]
        if not candidates:
            primary = max(biased, key=biased.get)
            status = "tendency" if biased[primary] >= 30 else "no"
        else:
            primary = max(candidates, key=lambda pair: pair[1])[0]
            status = "yes" if converted[primary] >= 40 else "tendency"

    return {
        "primary_code": primary,
        "primary_label": CONSTITUTION_LABELS[primary],
        "status": status,
        "is_balanced": is_balanced,
    }


def score_responses(responses: dict[str | int, int]) -> dict[str, Any]:
    converted = compute_converted_scores(responses)
    primary = assign_primary_constitution(converted)
    return {
        "converted_scores": converted,
        "primary": primary,
    }
