import Link from "next/link";
import { Activity, Target, BrainCircuit, BarChart as BarChartIcon } from "lucide-react";

export default function Home() {
  return (
    <div style={{ padding: "48px 40px", maxWidth: "900px", margin: "0 auto", height: "100%", display: "flex", flexDirection: "column", justifyContent: "center" }} className="bg-grid">
      {/* Hero */}
      <div style={{ textAlign: "center", marginBottom: "72px" }} className="animate-in">
        <div style={{ display: "inline-flex", alignItems: "center", gap: "8px", padding: "6px 14px", borderRadius: "100px", background: "rgba(255,255,255,0.03)", border: "1px solid var(--border)", marginBottom: "24px" }}>
          <div style={{ width: "6px", height: "6px", borderRadius: "50%", background: "var(--text-primary)", animation: "pulse-glow 2s infinite" }} />
          <span style={{ fontSize: "12px", fontWeight: 600, color: "var(--text-secondary)", letterSpacing: "0.02em" }}>AdNova Intelligence Module</span>
        </div>
        <h1 style={{ fontSize: "56px", fontWeight: 900, letterSpacing: "-0.04em", lineHeight: 1.1, marginBottom: "20px" }}>
          Unit Economics <br /><span className="gradient-text">& Contextual Targeting</span>
        </h1>
        <p style={{ fontSize: "17px", color: "var(--text-secondary)", maxWidth: "560px", margin: "0 auto", lineHeight: 1.6 }}>
          Stop guessing what works. Know exactly why your ads succeed, fix what's broken, and optimize every rupee spent with deep AI creative analysis.
        </p>
      </div>
    </div>
  );
}
