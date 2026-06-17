"""FastAPI service for CCMQ scoring."""

from __future__ import annotations

from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from tcm_constitution.ccmq.scoring import load_ccmq_catalog, score_responses

app = FastAPI(
    title="TCM Constitution API",
    description="CCMQ scoring service (ZYYXH/T157-2009)",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ScoreRequest(BaseModel):
    responses: dict[str, int] = Field(
        ...,
        description="Map of Q1..Q60 to Likert values 1-5",
        examples=[{"Q1": 3, "Q2": 2, "Q3": 1}],
    )


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/v1/ccmq/questions")
def list_questions() -> dict[str, Any]:
    catalog = load_ccmq_catalog()
    return {
        "standard": catalog["standard"],
        "likert": catalog["likert"],
        "constitutions": catalog["constitutions"],
        "questions": catalog["questions"],
    }


@app.post("/api/v1/ccmq/score")
def score_ccmq(body: ScoreRequest) -> dict[str, Any]:
    try:
        return score_responses(body.responses)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


def main() -> None:
    import uvicorn

    uvicorn.run("tcm_constitution.api.main:app", host="0.0.0.0", port=8000)
