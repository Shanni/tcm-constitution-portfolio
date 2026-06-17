"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import {
  Radar,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  ResponsiveContainer,
} from "recharts";
import {
  API_BASE,
  CONSTITUTION_LABELS,
  fetchQuestions,
  submitScore,
  type Question,
  type QuestionsResponse,
  type ScoreResult,
} from "@/lib/api";

const PAGE_SIZE = 5;

export default function HomePage() {
  const [catalog, setCatalog] = useState<QuestionsResponse | null>(null);
  const [responses, setResponses] = useState<Record<number, number>>({});
  const [page, setPage] = useState(0);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<ScoreResult | null>(null);

  useEffect(() => {
    fetchQuestions()
      .then(setCatalog)
      .catch((err: Error) => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  const questions = catalog?.questions ?? [];
  const totalPages = Math.ceil(questions.length / PAGE_SIZE);
  const pageQuestions = questions.slice(page * PAGE_SIZE, page * PAGE_SIZE + PAGE_SIZE);
  const answeredCount = Object.keys(responses).length;
  const progress = questions.length ? (answeredCount / questions.length) * 100 : 0;

  const allAnswered = questions.length > 0 && answeredCount === questions.length;

  const onSelect = (id: number, value: number) => {
    setResponses((prev) => ({ ...prev, [id]: value }));
  };

  const buildPayload = useCallback(() => {
    const payload: Record<string, number> = {};
    for (const [id, value] of Object.entries(responses)) {
      payload[`Q${id}`] = value;
    }
    return payload;
  }, [responses]);

  const handleSubmit = async () => {
    setSubmitting(true);
    setError(null);
    try {
      const score = await submitScore(buildPayload());
      setResult(score);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Scoring failed");
    } finally {
      setSubmitting(false);
    }
  };

  const chartData = useMemo(() => {
    if (!result) return [];
    return Object.entries(result.converted_scores).map(([code, value]) => ({
      code,
      label: CONSTITUTION_LABELS[code] ?? code,
      score: value,
    }));
  }, [result]);

  if (loading) {
    return (
      <main className="app-shell">
        <p>Loading questionnaire…</p>
      </main>
    );
  }

  if (!catalog) {
    return (
      <main className="app-shell">
        <div className="error-banner">
          Could not reach API at {API_BASE}. Start the Python service first.
        </div>
      </main>
    );
  }

  if (result) {
    return (
      <main className="app-shell">
        <header className="hero">
          <h1>Your constitution profile</h1>
          <p>Converted CCMQ subscale scores (0–100). Research demo only — not clinical advice.</p>
        </header>

        <section className="card">
          <div className="result-header">
            <div className="result-badge">{result.primary.status.toUpperCase()}</div>
            <h2 style={{ margin: "0 0 0.35rem" }}>{result.primary.primary_label}</h2>
            <p style={{ margin: 0, color: "var(--muted)" }}>
              {result.primary.is_balanced
                ? "Profile meets balanced (Pinghe) criteria."
                : "Primary biased constitution by standard thresholds."}
            </p>
          </div>

          <div className="chart-wrap">
            <ResponsiveContainer width="100%" height="100%">
              <RadarChart data={chartData}>
                <PolarGrid />
                <PolarAngleAxis dataKey="label" tick={{ fontSize: 11 }} />
                <PolarRadiusAxis angle={30} domain={[0, 100]} tick={{ fontSize: 10 }} />
                <Radar dataKey="score" stroke="#0f766e" fill="#14b8a6" fillOpacity={0.35} />
              </RadarChart>
            </ResponsiveContainer>
          </div>

          <div className="score-grid">
            {chartData.map((row) => (
              <div className="score-pill" key={row.code}>
                <strong>{row.score.toFixed(1)}</strong>
                <span>{row.label}</span>
              </div>
            ))}
          </div>

          <div className="actions">
            <button
              type="button"
              className="btn btn-secondary"
              onClick={() => {
                setResult(null);
                setPage(0);
              }}
            >
              Retake
            </button>
          </div>
        </section>

        <p className="disclaimer">
          Scoring follows ZYYXH/T157-2009 converted-score rules implemented in the Python core.
        </p>
      </main>
    );
  }

  return (
    <main className="app-shell">
      <header className="hero">
        <h1>CCMQ Constitution Questionnaire</h1>
        <p>
          60-item Chinese Medicine Constitution Questionnaire (CCMQ). Answer based on how you have
          felt over the past year.
        </p>
      </header>

      {error && <div className="error-banner">{error}</div>}

      <section className="card">
        <div className="progress-bar" aria-hidden>
          <span style={{ width: `${progress}%` }} />
        </div>
        <div className="question-meta">
          <span>
            Page {page + 1} of {totalPages}
          </span>
          <span>
            {answeredCount} / {questions.length} answered
          </span>
        </div>

        {pageQuestions.map((q: Question) => (
          <QuestionBlock
            key={q.id}
            question={q}
            likert={catalog.likert}
            value={responses[q.id]}
            onSelect={onSelect}
          />
        ))}

        <div className="actions">
          <button
            type="button"
            className="btn btn-secondary"
            disabled={page === 0}
            onClick={() => setPage((p) => p - 1)}
          >
            Back
          </button>
          {page < totalPages - 1 ? (
            <button type="button" className="btn btn-primary" onClick={() => setPage((p) => p + 1)}>
              Next
            </button>
          ) : (
            <button
              type="button"
              className="btn btn-primary"
              disabled={!allAnswered || submitting}
              onClick={handleSubmit}
            >
              {submitting ? "Scoring…" : "See results"}
            </button>
          )}
        </div>
      </section>

      <p className="disclaimer">
        API: {API_BASE} · Standard: {catalog.standard}
      </p>
    </main>
  );
}

function QuestionBlock({
  question,
  likert,
  value,
  onSelect,
}: {
  question: Question;
  likert: Record<string, string>;
  value?: number;
  onSelect: (id: number, value: number) => void;
}) {
  return (
    <fieldset style={{ border: "none", padding: 0, margin: "0 0 1.75rem" }}>
      <legend className="question-text">
        Q{question.id}. {question.text_en}
      </legend>
      <p className="question-text-zh">{question.text_zh}</p>
      <div className="likert">
        {Object.entries(likert).map(([score, label]) => (
          <label key={score}>
            <input
              type="radio"
              name={`q-${question.id}`}
              value={score}
              checked={value === Number(score)}
              onChange={() => onSelect(question.id, Number(score))}
            />
            <span>
              {score} — {label}
            </span>
          </label>
        ))}
      </div>
    </fieldset>
  );
}
