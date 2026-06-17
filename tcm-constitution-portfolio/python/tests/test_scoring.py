import pytest

from tcm_constitution.ccmq.scoring import (
    compute_converted_scores,
    load_ccmq_catalog,
    score_responses,
)


def test_catalog_has_sixty_questions():
    catalog = load_ccmq_catalog()
    assert len(catalog["questions"]) == 60
    assert len(catalog["subscale_items"]) == 9


def test_all_likert_values_accepted():
    responses = {f"Q{i}": 3 for i in range(1, 61)}
    result = score_responses(responses)
    assert len(result["converted_scores"]) == 9
    assert "primary" in result


def test_invalid_likert_raises():
    with pytest.raises(ValueError, match="must be 1-5"):
        score_responses({"Q1": 6})


def test_balanced_profile_when_all_mild():
    """All 3s on reverse-scored GTC items should yield moderate GTC, low biased scores."""
    responses = {f"Q{i}": 3 for i in range(1, 61)}
    scores = compute_converted_scores(responses)
    assert scores["GTC"] == 50.0
    assert all(scores[code] == 50.0 for code in scores if code != "GTC")


def test_partial_responses_rejected():
    responses = {"Q1": 5, "Q2": 1}
    with pytest.raises(ValueError, match="Missing responses"):
        compute_converted_scores(responses)
