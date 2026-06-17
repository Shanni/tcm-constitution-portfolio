import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "TCM Constitution Questionnaire",
  description: "CCMQ 60-item constitution assessment demo",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
