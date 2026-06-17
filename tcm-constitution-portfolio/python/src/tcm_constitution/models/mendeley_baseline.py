"""Sklearn baselines on Mendeley 274 (score regression + primary-type classification)."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    mean_absolute_error,
    r2_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from tcm_constitution.adapters.mendeley_274 import MendeleyCohort, assign_primary_from_biased_scores


@dataclass
class BaselineResults:
    regression_mae: dict[str, float]
    regression_r2: dict[str, float]
    classification_accuracy: float
    classification_macro_f1: float
    n_train: int
    n_test: int


def _features_and_targets(cohort: MendeleyCohort) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series]:
    x = cohort.biosignals.copy()
    y_scores = cohort.constitution_scores.copy()
    primary = assign_primary_from_biased_scores(y_scores)["primary_code"]
    return x, y_scores, primary


def train_mendeley_baselines(
    cohort: MendeleyCohort,
    *,
    test_size: float = 0.2,
    random_state: int = 42,
) -> BaselineResults:
    x, y_scores, primary = _features_and_targets(cohort)

    x_train, x_test, y_train, y_test, p_train, p_test = train_test_split(
        x,
        y_scores,
        primary,
        test_size=test_size,
        random_state=random_state,
        stratify=primary,
    )

    mae: dict[str, float] = {}
    r2: dict[str, float] = {}
    for col in y_scores.columns:
        pipe = Pipeline(
            [
                ("scale", StandardScaler()),
                ("model", RandomForestRegressor(n_estimators=200, random_state=random_state)),
            ]
        )
        pipe.fit(x_train, y_train[col])
        preds = pipe.predict(x_test)
        mae[col] = float(mean_absolute_error(y_test[col], preds))
        r2[col] = float(r2_score(y_test[col], preds))

    clf = Pipeline(
        [
            ("scale", StandardScaler()),
            ("model", RandomForestClassifier(n_estimators=300, random_state=random_state)),
        ]
    )
    clf.fit(x_train, p_train)
    p_pred = clf.predict(x_test)

    return BaselineResults(
        regression_mae=mae,
        regression_r2=r2,
        classification_accuracy=float(accuracy_score(p_test, p_pred)),
        classification_macro_f1=float(f1_score(p_test, p_pred, average="macro")),
        n_train=len(x_train),
        n_test=len(x_test),
    )


def results_to_frame(results: BaselineResults) -> pd.DataFrame:
    rows = [
        {"metric": f"MAE_{code}", "value": score}
        for code, score in results.regression_mae.items()
    ]
    rows += [
        {"metric": f"R2_{code}", "value": score}
        for code, score in results.regression_r2.items()
    ]
    rows += [
        {"metric": "classification_accuracy", "value": results.classification_accuracy},
        {"metric": "classification_macro_f1", "value": results.classification_macro_f1},
        {"metric": "n_train", "value": results.n_train},
        {"metric": "n_test", "value": results.n_test},
    ]
    return pd.DataFrame(rows)
