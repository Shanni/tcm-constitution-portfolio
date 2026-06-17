export type Question = {
  id: number;
  text_en: string;
  text_zh: string;
};

export type ConstitutionMeta = {
  name_en: string;
  name_zh: string;
  reverse_in_scale: boolean;
};

export type QuestionsResponse = {
  standard: string;
  likert: Record<string, string>;
  constitutions: Record<string, ConstitutionMeta>;
  questions: Question[];
};

export type ScoreResult = {
  converted_scores: Record<string, number>;
  primary: {
    primary_code: string;
    primary_label: string;
    status: "yes" | "tendency" | "no";
    is_balanced: boolean;
  };
};

export const CONSTITUTION_LABELS: Record<string, string> = {
  GTC: "Balanced",
  QDC: "Qi-deficiency",
  YaDC: "Yang-deficiency",
  YiDC: "Yin-deficiency",
  PDC: "Phlegm-dampness",
  DHC: "Damp-heat",
  BSC: "Blood-stasis",
  QSC: "Qi-stagnation",
  SDC: "Inherited-special",
};

export const API_BASE =
  process.env.NEXT_PUBLIC_API_URL?.replace(/\/$/, "") ?? "http://127.0.0.1:8000";

export async function fetchQuestions(): Promise<QuestionsResponse> {
  const res = await fetch(`${API_BASE}/api/v1/ccmq/questions`, { cache: "no-store" });
  if (!res.ok) throw new Error("Failed to load CCMQ questions");
  return res.json();
}

export async function submitScore(responses: Record<string, number>): Promise<ScoreResult> {
  const res = await fetch(`${API_BASE}/api/v1/ccmq/score`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ responses }),
  });
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(body.detail ?? "Scoring failed");
  }
  return res.json();
}
