#!/usr/bin/env python3
"""Run Mendeley EDA and save figures to notebooks/output/."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from tcm_constitution.adapters.mendeley_274 import load_mendeley_274
from tcm_constitution.viz.eda import (
    correlation_with_scores,
    plot_constitution_distributions,
    plot_correlation_heatmap,
    plot_primary_type_counts,
    summarize_cohort,
)

OUTPUT_DIR = Path(__file__).resolve().parents[1] / "notebooks" / "output"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    cohort = load_mendeley_274()

    summary = summarize_cohort(cohort)
    summary.to_csv(OUTPUT_DIR / "mendeley_inventory.csv", index=False)

    top_corr = correlation_with_scores(cohort, top_n=30)
    top_corr.to_csv(OUTPUT_DIR / "top_correlations.csv", index=False)

    plot_constitution_distributions(cohort)
    plt.savefig(OUTPUT_DIR / "constitution_distributions.png", dpi=150)
    plt.close()

    plot_primary_type_counts(cohort)
    plt.savefig(OUTPUT_DIR / "primary_type_counts.png", dpi=150)
    plt.close()

    plot_correlation_heatmap(cohort)
    plt.savefig(OUTPUT_DIR / "feature_score_heatmap.png", dpi=150)
    plt.close()

    enriched = cohort.with_primary_type()
    enriched[["primary_code", "primary_label", "primary_status"]].value_counts().to_csv(
        OUTPUT_DIR / "primary_type_counts.csv"
    )

    print(f"Wrote EDA outputs to {OUTPUT_DIR}")
    print(summary.to_string(index=False))
    print("\nTop 5 feature-score correlations:")
    print(top_corr.head().to_string(index=False))


if __name__ == "__main__":
    main()
