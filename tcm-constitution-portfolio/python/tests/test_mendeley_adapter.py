import pytest

from tcm_constitution.adapters.mendeley_274 import (
    CONSTITUTION_COLUMN_MAP,
    assign_primary_from_biased_scores,
    find_share_data_xls,
    load_mendeley_274,
)


@pytest.fixture(scope="module")
def cohort():
    try:
        return load_mendeley_274()
    except FileNotFoundError:
        pytest.skip("Mendeley data not downloaded")


def test_find_xls():
    path = find_share_data_xls()
    assert path.name == "Share data.xls"
    assert path.exists()


def test_load_shape(cohort):
    assert cohort.n_subjects == 274
    assert cohort.constitution_scores.shape == (274, 8)
    assert len(cohort.biosignals.columns) == 54


def test_constitution_score_range(cohort):
    scores = cohort.constitution_scores
    assert scores.min().min() >= 0
    assert scores.max().max() <= 100


def test_primary_assignment(cohort):
    primary = assign_primary_from_biased_scores(cohort.constitution_scores)
    assert len(primary) == 274
    assert primary["primary_code"].notna().all()
    assert set(primary["primary_code"]).issubset(set(CONSTITUTION_COLUMN_MAP.values()) | {"GTC"})
