"""Exploratory plots for the Mendeley multimodal cohort."""

from __future__ import annotations

from typing import Any

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from tcm_constitution.adapters.mendeley_274 import MendeleyCohort
from tcm_constitution.ccmq.scoring import CONSTITUTION_LABELS


def summarize_cohort(cohort: MendeleyCohort) -> pd.DataFrame:
    """Return a one-row inventory table describing column groups and missingness."""
    rows: list[dict[str, Any]] = [
        {
            "group": "demographics",
            "n_columns": cohort.demographics.shape[1],
            "missing_cells": int(cohort.demographics.isna().sum().sum()),
        },
        {
            "group": "biosignals",
            "n_columns": cohort.biosignals.shape[1],
            "missing_cells": int(cohort.biosignals.isna().sum().sum()),
        },
        {
            "group": "constitution_scores",
            "n_columns": cohort.constitution_scores.shape[1],
            "missing_cells": int(cohort.constitution_scores.isna().sum().sum()),
        },
    ]
    summary = pd.DataFrame(rows)
    summary["n_subjects"] = cohort.n_subjects
    summary["source"] = str(cohort.source_path.name)
    return summary


def plot_constitution_distributions(
    cohort: MendeleyCohort,
    *,
    ax: plt.Axes | None = None,
) -> plt.Axes:
    scores = cohort.constitution_scores
    labels = [CONSTITUTION_LABELS.get(col, col) for col in scores.columns]

    if ax is None:
        _, ax = plt.subplots(figsize=(10, 4))

    ax.boxplot(
        [scores[col].dropna() for col in scores.columns],
        tick_labels=labels,
        vert=True,
    )
    ax.set_ylabel("Converted score (0–100)")
    ax.set_title("Constitution score distributions (Mendeley N=274)")
    ax.tick_params(axis="x", rotation=35)
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    return ax


def plot_primary_type_counts(cohort: MendeleyCohort, *, ax: plt.Axes | None = None) -> plt.Axes:
    enriched = cohort.with_primary_type()
    counts = enriched["primary_label"].value_counts()

    if ax is None:
        _, ax = plt.subplots(figsize=(8, 4))

    counts.plot(kind="bar", ax=ax, color="#0f766e")
    ax.set_ylabel("Subjects")
    ax.set_title("Derived primary constitution (max biased score rule)")
    ax.tick_params(axis="x", rotation=35)
    plt.tight_layout()
    return ax


def correlation_with_scores(cohort: MendeleyCohort, *, top_n: int = 20) -> pd.DataFrame:
    """Pearson correlation of each biosignal feature with each constitution score."""
    combined = pd.concat([cohort.biosignals, cohort.constitution_scores], axis=1)
    corr = combined.corr(numeric_only=True)
    score_cols = list(cohort.constitution_scores.columns)
    feature_cols = list(cohort.biosignals.columns)
    block = corr.loc[feature_cols, score_cols]
    flat = block.stack().reset_index()
    flat.columns = ["feature", "constitution", "pearson_r"]
    flat["abs_r"] = flat["pearson_r"].abs()
    return flat.sort_values("abs_r", ascending=False).head(top_n)


def plot_correlation_heatmap(
    cohort: MendeleyCohort,
    *,
    ax: plt.Axes | None = None,
    max_features: int = 25,
) -> plt.Axes:
    """Heatmap of biosignal features vs constitution scores (top |r| features)."""
    top_pairs = correlation_with_scores(cohort, top_n=max_features)
    top_features = top_pairs["feature"].drop_duplicates().tolist()

    combined = pd.concat(
        [cohort.biosignals[top_features], cohort.constitution_scores],
        axis=1,
    )
    corr = combined.corr(numeric_only=True)
    block = corr.loc[top_features, cohort.constitution_scores.columns]
    labels = [CONSTITUTION_LABELS.get(col, col) for col in block.columns]
    block.columns = labels

    if ax is None:
        _, ax = plt.subplots(figsize=(10, 8))

    sns.heatmap(
        block,
        cmap="RdBu_r",
        center=0,
        vmin=-0.5,
        vmax=0.5,
        ax=ax,
        cbar_kws={"label": "Pearson r"},
    )
    ax.set_title("Top biosignal features vs constitution scores")
    plt.tight_layout()
    return ax
