<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>📊 Probability & Statistics — Master Notes</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=JetBrains+Mono:wght@400;600&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  :root {
    --ink: #0d0d14;
    --paper: #faf8f3;
    --accent: #c0392b;
    --gold: #d4a017;
    --steel: #2c3e50;
    --mist: #e8e4da;
    --teal: #1a6b72;
    --formula-bg: #0d0d14;
    --formula-text: #7ec8e3;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--paper);
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
    font-weight: 300;
    line-height: 1.8;
    overflow-x: hidden;
  }

  /* ── HERO ── */
  .hero {
    background: var(--ink);
    color: var(--paper);
    padding: 80px 60px 70px;
    position: relative;
    overflow: hidden;
  }

  .hero::before {
    content: '';
    position: absolute;
    top: -80px; right: -80px;
    width: 400px; height: 400px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(192,57,43,0.25) 0%, transparent 70%);
  }

  .hero::after {
    content: '∑ P(x) = 1';
    position: absolute;
    bottom: 24px; right: 60px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: rgba(250,248,243,0.18);
    letter-spacing: 2px;
  }

  .hero-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 4px;
    color: var(--accent);
    text-transform: uppercase;
    margin-bottom: 20px;
  }

  .hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.8rem, 6vw, 5.5rem);
    font-weight: 900;
    line-height: 1.05;
    max-width: 700px;
  }

  .hero h1 em {
    font-style: italic;
    color: var(--gold);
  }

  .hero-sub {
    margin-top: 24px;
    font-size: 1rem;
    color: rgba(250,248,243,0.6);
    max-width: 520px;
    font-weight: 300;
    letter-spacing: 0.3px;
  }

  .hero-pills {
    display: flex; flex-wrap: wrap; gap: 10px;
    margin-top: 36px;
  }

  .pill {
    border: 1px solid rgba(250,248,243,0.2);
    border-radius: 2px;
    padding: 6px 16px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 1.5px;
    color: rgba(250,248,243,0.7);
    text-transform: uppercase;
  }

  /* ── LAYOUT ── */
  .container {
    max-width: 960px;
    margin: 0 auto;
    padding: 0 40px;
  }

  /* ── CHAPTER HEADER ── */
  .chapter {
    padding: 72px 0 16px;
  }

  .chapter-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 4px;
    color: var(--accent);
    text-transform: uppercase;
  }

  .chapter h2 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.8rem, 3.5vw, 2.8rem);
    font-weight: 700;
    margin-top: 8px;
    color: var(--ink);
  }

  .rule-line {
    height: 2px;
    background: linear-gradient(90deg, var(--accent) 0%, transparent 100%);
    margin: 16px 0 32px;
    max-width: 120px;
  }

  /* ── CALLOUT ── */
  .callout {
    border-left: 3px solid var(--gold);
    background: rgba(212,160,23,0.06);
    padding: 20px 24px;
    margin: 24px 0;
    border-radius: 0 4px 4px 0;
  }

  .callout strong {
    font-family: 'Playfair Display', serif;
    font-size: 1.05rem;
    display: block;
    margin-bottom: 6px;
    color: var(--ink);
  }

  .callout p { color: #444; font-size: 0.95rem; }

  /* ── FORMULA BLOCK ── */
  .formula-block {
    background: var(--formula-bg);
    border-radius: 4px;
    padding: 28px 32px;
    margin: 20px 0;
    position: relative;
    overflow: hidden;
  }

  .formula-block::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 3px; height: 100%;
    background: var(--accent);
  }

  .formula-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 3px;
    color: rgba(126,200,227,0.4);
    text-transform: uppercase;
    margin-bottom: 12px;
  }

  .formula-block code {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.05rem;
    color: var(--formula-text);
    line-height: 1.7;
    display: block;
  }

  .formula-block .formula-note {
    font-size: 0.82rem;
    color: rgba(250,248,243,0.35);
    margin-top: 10px;
    font-family: 'JetBrains Mono', monospace;
  }

  /* ── TWO-COL GRID ── */
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin: 24px 0;
  }

  .card {
    border: 1px solid var(--mist);
    padding: 24px;
    border-radius: 4px;
    position: relative;
  }

  .card-accent {
    border-top: 3px solid var(--accent);
  }

  .card-teal {
    border-top: 3px solid var(--teal);
  }

  .card h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem;
    margin-bottom: 10px;
    color: var(--ink);
  }

  .card p, .card li {
    font-size: 0.9rem;
    color: #555;
    line-height: 1.7;
  }

  .card ul { padding-left: 16px; }

  /* ── DEFINITION LIST ── */
  .def-list { margin: 20px 0; }

  .def-item {
    display: grid;
    grid-template-columns: 180px 1fr;
    gap: 16px;
    padding: 14px 0;
    border-bottom: 1px solid var(--mist);
    align-items: start;
  }

  .def-term {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    color: var(--accent);
    font-weight: 600;
  }

  .def-desc {
    font-size: 0.92rem;
    color: #444;
  }

  /* ── PROBABILITY SCALE SVG ── */
  .prob-scale {
    margin: 28px 0;
  }

  /* ── SECTION DIVIDER ── */
  .divider {
    height: 1px;
    background: var(--mist);
    margin: 60px 0 0;
  }

  /* ── IMAGE BLOCK ── */
  .image-feature {
    background: var(--ink);
    margin: 48px -40px;
    padding: 48px 40px;
    display: grid;
    grid-template-columns: 1.1fr 1fr;
    gap: 48px;
    align-items: center;
  }

  .image-feature.flip { grid-template-columns: 1fr 1.1fr; }

  .image-feature img {
    width: 100%;
    border-radius: 4px;
    opacity: 0.88;
    filter: contrast(1.05) saturate(0.9);
  }

  .image-feature-text h3 {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    color: var(--paper);
    margin-bottom: 14px;
  }

  .image-feature-text p {
    color: rgba(250,248,243,0.6);
    font-size: 0.92rem;
    line-height: 1.8;
  }

  .image-feature-text .tag {
    display: inline-block;
    background: var(--accent);
    color: white;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 2px;
    padding: 4px 12px;
    text-transform: uppercase;
    margin-bottom: 16px;
  }

  /* ── EVENT TYPES TABLE ── */
  .event-table {
    width: 100%;
    border-collapse: collapse;
    margin: 24px 0;
    font-size: 0.9rem;
  }

  .event-table th {
    background: var(--ink);
    color: var(--paper);
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 12px 16px;
    text-align: left;
  }

  .event-table td {
    padding: 12px 16px;
    border-bottom: 1px solid var(--mist);
    color: #444;
    vertical-align: top;
  }

  .event-table tr:nth-child(even) td { background: rgba(232,228,218,0.3); }

  .event-table .formula-inline {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.82rem;
    color: var(--accent);
  }

  /* ── RULES TRIO ── */
  .rules-trio {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin: 24px 0;
  }

  .rule-card {
    background: var(--ink);
    border-radius: 4px;
    padding: 24px 20px;
    text-align: center;
  }

  .rule-card .rule-icon {
    font-size: 2rem;
    margin-bottom: 10px;
  }

  .rule-card h4 {
    font-family: 'Playfair Display', serif;
    color: var(--paper);
    margin-bottom: 12px;
    font-size: 1rem;
  }

  .rule-card code {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    color: var(--formula-text);
    line-height: 1.8;
    display: block;
  }

  /* ── EMPIRICAL RULE ── */
  .empirical {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin: 24px 0;
  }

  .emp-card {
    border-radius: 4px;
    padding: 24px;
    text-align: center;
  }

  .emp-68 { background: #c0392b; }
  .emp-95 { background: #8e2222; }
  .emp-99 { background: #5a1414; }

  .emp-card .pct {
    font-family: 'Playfair Display', serif;
    font-size: 2.4rem;
    font-weight: 900;
    color: white;
  }

  .emp-card .sigma {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    color: rgba(255,255,255,0.7);
    margin-top: 4px;
  }

  /* ── FOOTER ── */
  .footer {
    background: var(--ink);
    color: rgba(250,248,243,0.4);
    padding: 40px 60px;
    margin-top: 80px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 1.5px;
  }

  .footer .footer-brand {
    color: var(--gold);
    font-size: 1rem;
    font-family: 'Playfair Display', serif;
    letter-spacing: 0;
    font-weight: 700;
  }

  /* ── TIP BOX ── */
  .tip-box {
    border: 1.5px solid var(--teal);
    border-radius: 4px;
    padding: 24px 28px;
    margin: 32px 0;
    background: rgba(26,107,114,0.05);
    display: flex;
    gap: 18px;
    align-items: flex-start;
  }

  .tip-box .tip-icon { font-size: 1.6rem; flex-shrink: 0; margin-top: 2px; }

  .tip-box p {
    font-size: 0.95rem;
    color: #333;
    line-height: 1.75;
  }

  .tip-box strong {
    color: var(--teal);
    font-weight: 500;
  }

  /* ── TOC ── */
  .toc {
    background: var(--mist);
    padding: 32px 36px;
    margin: 40px 0;
    border-radius: 4px;
  }

  .toc h3 {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 16px;
  }

  .toc-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4px 40px;
  }

  .toc-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 6px 0;
    border-bottom: 1px dotted rgba(0,0,0,0.12);
    font-size: 0.88rem;
    color: #444;
  }

  .toc-item .toc-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: var(--accent);
    width: 22px;
    flex-shrink: 0;
  }

  /* ── ANIMATIONS ── */
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(24px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .hero h1   { animation: fadeUp 0.7s ease both; }
  .hero-sub  { animation: fadeUp 0.7s 0.15s ease both; }
  .hero-pills{ animation: fadeUp 0.7s 0.3s ease both; }

  /* ── RESPONSIVE ── */
  @media (max-width: 680px) {
    .hero { padding: 48px 24px; }
    .container { padding: 0 20px; }
    .grid-2 { grid-template-columns: 1fr; }
    .rules-trio { grid-template-columns: 1fr; }
    .empirical { grid-template-columns: 1fr; }
    .image-feature { grid-template-columns: 1fr; margin: 32px -20px; padding: 32px 20px; }
    .image-feature.flip { direction: ltr; }
    .def-item { grid-template-columns: 1fr; gap: 4px; }
    .toc-grid { grid-template-columns: 1fr; }
    .footer { flex-direction: column; gap: 12px; text-align: center; }
  }
</style>
</head>
<body>

<!-- ══ HERO ══════════════════════════════════════════ -->
<header class="hero">
  <p class="hero-label">📊 Master Reference · Mathematics</p>
  <h1>Probability &amp;<br><em>Statistics</em></h1>
  <p class="hero-sub">A complete study companion — from sample spaces and classical rules through Bayes' theorem and probability distributions, with worked examples throughout.</p>
  <div class="hero-pills">
    <span class="pill">Probability</span>
    <span class="pill">Random Variables</span>
    <span class="pill">Bayes' Theorem</span>
    <span class="pill">Distributions</span>
    <span class="pill">Normal Curve</span>
  </div>
</header>

<div class="container">

  <!-- ── TOC ── -->
  <div class="toc">
    <h3>Contents</h3>
    <div class="toc-grid">
      <div class="toc-item"><span class="toc-num">01</span> Foundations of Probability</div>
      <div class="toc-item"><span class="toc-num">05</span> Conditional Probability</div>
      <div class="toc-item"><span class="toc-num">02</span> Types &amp; Terminology</div>
      <div class="toc-item"><span class="toc-num">06</span> Bayes' Theorem</div>
      <div class="toc-item"><span class="toc-num">03</span> Key Rules</div>
      <div class="toc-item"><span class="toc-num">07</span> Random Variables &amp; Stats</div>
      <div class="toc-item"><span class="toc-num">04</span> Practice Examples</div>
      <div class="toc-item"><span class="toc-num">08</span> Probability Distributions</div>
    </div>
  </div>

  <!-- ══ 01. FOUNDATIONS ══ -->
  <section class="chapter">
    <p class="chapter-num">Chapter 01</p>
    <h2>Foundations of Probability</h2>
    <div class="rule-line"></div>

    <p>Probability quantifies uncertainty — it measures how likely an event is to occur on a scale from <strong>0</strong> (impossible) to <strong>1</strong> (certain).</p>

    <!-- SVG probability scale -->
    <div class="prob-scale">
      <svg viewBox="0 0 820 100" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:820px;">
        <defs>
          <linearGradient id="scaleGrad" x1="0" x2="1" y1="0" y2="0">
            <stop offset="0%"   stop-color="#c0392b"/>
            <stop offset="50%"  stop-color="#d4a017"/>
            <stop offset="100%" stop-color="#1a6b72"/>
          </linearGradient>
        </defs>
        <!-- Track -->
        <rect x="60" y="42" width="700" height="6" rx="3" fill="url(#scaleGrad)" opacity="0.9"/>
        <!-- Ticks & labels -->
        <line x1="60"  y1="38" x2="60"  y2="56" stroke="#0d0d14" stroke-width="2"/>
        <line x1="410" y1="38" x2="410" y2="56" stroke="#0d0d14" stroke-width="2"/>
        <line x1="760" y1="38" x2="760" y2="56" stroke="#0d0d14" stroke-width="2"/>

        <text x="60"  y="74" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="13" fill="#c0392b" font-weight="600">0</text>
        <text x="410" y="74" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="13" fill="#d4a017" font-weight="600">0.5</text>
        <text x="760" y="74" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="13" fill="#1a6b72" font-weight="600">1</text>

        <text x="60"  y="30" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="11" fill="#888">Impossible</text>
        <text x="410" y="30" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="11" fill="#888">Even Chance</text>
        <text x="760" y="30" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="11" fill="#888">Certain</text>

        <!-- Example markers -->
        <circle cx="130" cy="45" r="5" fill="#c0392b" opacity="0.7"/>
        <text x="130" y="94" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="10" fill="#aaa">Snow in July</text>

        <circle cx="550" cy="45" r="5" fill="#888" opacity="0.7"/>
        <text x="550" y="94" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="10" fill="#aaa">Coin flip</text>

        <circle cx="720" cy="45" r="5" fill="#1a6b72" opacity="0.7"/>
        <text x="720" y="94" text-anchor="middle" font-family="DM Sans,sans-serif" font-size="10" fill="#aaa">Sun rises</text>
      </svg>
    </div>

    <div class="grid-2">
      <div class="card card-accent">
        <h3>Theoretical Probability</h3>
        <p>Derived from logical reasoning about equally likely outcomes — no experimentation required.</p>
        <div style="margin-top:14px;">
          <code style="font-family:'JetBrains Mono',monospace; font-size:0.85rem; color:var(--accent);">P(E) = n(E) / n(S)</code>
        </div>
      </div>
      <div class="card card-teal">
        <h3>Empirical Probability</h3>
        <p>Computed from observed data. As trials increase, empirical probability converges toward theoretical probability.</p>
        <div style="margin-top:14px;">
          <code style="font-family:'JetBrains Mono',monospace; font-size:0.85rem; color:var(--teal);">P(E) = freq(E) / total trials</code>
        </div>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ══ 02. TERMINOLOGY ══ -->
  <section class="chapter">
    <p class="chapter-num">Chapter 02</p>
    <h2>Key Terminology</h2>
    <div class="rule-line"></div>

    <div class="def-list">
      <div class="def-item">
        <span class="def-term">Sample Space (S)</span>
        <span class="def-desc">The complete set of all possible outcomes of an experiment. For a die: S = {1, 2, 3, 4, 5, 6}</span>
      </div>
      <div class="def-item">
        <span class="def-term">Event (E)</span>
        <span class="def-desc">Any subset of the sample space. Rolling an even number: E = {2, 4, 6}</span>
      </div>
      <div class="def-item">
        <span class="def-term">Certain Event</span>
        <span class="def-desc">An event guaranteed to occur. P = 1. Example: rolling a number ≤ 6 on a standard die.</span>
      </div>
      <div class="def-item">
        <span class="def-term">Impossible Event</span>
        <span class="def-desc">An event that cannot occur. P = 0. Example: rolling a 7 on a standard die.</span>
      </div>
      <div class="def-item">
        <span class="def-term">Complementary</span>
        <span class="def-desc">Aᶜ is everything in S that is not in A. P(A) + P(Aᶜ) = 1 always.</span>
      </div>
      <div class="def-item">
        <span class="def-term">Mutually Exclusive</span>
        <span class="def-desc">Events A and B cannot both occur simultaneously. A ∩ B = ∅</span>
      </div>
      <div class="def-item">
        <span class="def-term">Independent Events</span>
        <span class="def-desc">Occurrence of A does not affect probability of B. P(A∩B) = P(A)·P(B)</span>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ══ 03. KEY RULES ══ -->
  <section class="chapter">
    <p class="chapter-num">Chapter 03</p>
    <h2>Rules of Probability</h2>
    <div class="rule-line"></div>

    <div class="rules-trio">
      <div class="rule-card">
        <div class="rule-icon">🔄</div>
        <h4>Complementary Rule</h4>
        <code>P(Aᶜ) = 1 − P(A)</code>
        <code style="color:rgba(250,248,243,0.35);font-size:0.72rem;margin-top:8px;">P(S) = 1 · P(∅) = 0</code>
      </div>
      <div class="rule-card">
        <div class="rule-icon">➕</div>
        <h4>Addition Rule</h4>
        <code>P(A∪B) = P(A) + P(B)</code>
        <code style="color:rgba(126,200,227,0.5);font-size:0.72rem;margin-top:4px;">if mutually exclusive</code>
        <code style="margin-top:10px;">P(A∪B) = P(A) + P(B)</code>
        <code>         − P(A∩B)</code>
        <code style="color:rgba(126,200,227,0.5);font-size:0.72rem;margin-top:4px;">if non-exclusive</code>
      </div>
      <div class="rule-card">
        <div class="rule-icon">✖️</div>
        <h4>Multiplication Rule</h4>
        <code>P(A∩B) = P(A)·P(B)</code>
        <code style="color:rgba(126,200,227,0.5);font-size:0.72rem;margin-top:4px;">if independent</code>
        <code style="margin-top:10px;">P(A∩B) = P(A)·P(B|A)</code>
        <code style="color:rgba(126,200,227,0.5);font-size:0.72rem;margin-top:4px;">if dependent</code>
      </div>
    </div>
  </section>

</div>

<!-- ══ IMAGE FEATURE 1: Probability Visualization ══ -->
<div class="image-feature" style="margin-left:0;margin-right:0;padding-left:max(40px, calc(50% - 480px + 40px));padding-right:max(40px, calc(50% - 480px + 40px));">
  <div class="image-feature-text">
    <span class="tag">Visual Guide</span>
    <h3>Seeing Probability in Action</h3>
    <p>Data visualizations bridge the gap between abstract formulas and intuitive understanding. Probability distributions, sample spaces, and event intersections all become clear when represented graphically — whether through Venn diagrams, histograms, or scatter plots.</p>
  </div>
  <img src="https://miro.medium.com/v2/resize:fit:1400/1*HBq9ESzH42J_kANOjvWUUg.png"
       alt="Probability and statistics visualization"
       onerror="this.style.display='none'">
</div>

<div class="container">

  <!-- ══ 04. PRACTICE EXAMPLES ══ -->
  <section class="chapter">
    <p class="chapter-num">Chapter 04</p>
    <h2>Practice Examples</h2>
    <div class="rule-line"></div>

    <table class="event-table">
      <thead>
        <tr>
          <th>Experiment</th>
          <th>Sample Space</th>
          <th>Example Event</th>
          <th>Probability</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>🎲 Roll a die</td>
          <td>{1, 2, 3, 4, 5, 6}</td>
          <td>Roll a 4</td>
          <td class="formula-inline">P(4) = 1/6 ≈ 0.167</td>
        </tr>
        <tr>
          <td>🃏 Draw a card</td>
          <td>52 cards, 4 suits</td>
          <td>Draw a heart</td>
          <td class="formula-inline">P(♥) = 13/52 = 1/4</td>
        </tr>
        <tr>
          <td>🪙 Flip 2 coins</td>
          <td>{HH, HT, TH, TT}</td>
          <td>Both tails (TT)</td>
          <td class="formula-inline">P(TT) = 1/4 = 0.25</td>
        </tr>
        <tr>
          <td>🏭 Factory defect</td>
          <td>Machine A + B</td>
          <td>Defective item</td>
          <td class="formula-inline">P(D) = 0.032</td>
        </tr>
      </tbody>
    </table>
  </section>

  <div class="divider"></div>

  <!-- ══ 05. CONDITIONAL PROBABILITY ══ -->
  <section class="chapter">
    <p class="chapter-num">Chapter 05</p>
    <h2>Conditional Probability</h2>
    <div class="rule-line"></div>

    <p>The probability of B <em>given that</em> A has already occurred:</p>

    <div class="formula-block">
      <div class="formula-label">Core Formula</div>
      <code>P(B | A) = P(A ∩ B) / P(A)</code>
      <div class="formula-note">// Read as "probability of B given A"</div>
    </div>

    <div class="callout">
      <strong>📌 Worked Example</strong>
      <p>In a class of 40 students, 25 passed both math and physics. The probability that a student passed physics given they passed math = 25/40 = <strong>0.625</strong></p>
    </div>

    <h3 style="font-family:'Playfair Display',serif; font-size:1.3rem; margin: 28px 0 12px;">Law of Total Probability</h3>
    <p>When event B can occur through several mutually exclusive pathways A₁, A₂, …, Aₙ:</p>

    <div class="formula-block">
      <div class="formula-label">Total Probability</div>
      <code>P(B) = Σ P(B | Aᵢ) · P(Aᵢ)</code>
    </div>

    <div class="callout">
      <strong>🏭 Factory Example</strong>
      <p>Machine A produces 60% of parts (2% defective). Machine B produces 40% (5% defective).<br>
      P(Defective) = (0.02 × 0.6) + (0.05 × 0.4) = 0.012 + 0.020 = <strong>0.032</strong></p>
    </div>
  </section>

</div>

<!-- ══ IMAGE FEATURE 2: Bayes Theorem ══ -->
<div class="image-feature flip" style="margin-left:0;margin-right:0;padding-left:max(40px, calc(50% - 480px + 40px));padding-right:max(40px, calc(50% - 480px + 40px));">
  <img src="https://i0.wp.com/calcworkshop.com/wp-content/uploads/bayes-theorem-tree-diagram.png"
       alt="Bayes theorem tree diagram"
       onerror="this.style.display='none'">
  <div class="image-feature-text">
    <span class="tag">Bayes' Theorem</span>
    <h3>Updating Beliefs with Evidence</h3>
    <p>Bayes' theorem is the engine of rational inference. A tree diagram reveals how prior probabilities combine with new evidence to produce updated (posterior) probabilities — the foundation of machine learning, medical diagnostics, and spam filters.</p>
  </div>
</div>

<div class="container">

  <!-- ══ 06. BAYES ══ -->
  <section class="chapter">
    <p class="chapter-num">Chapter 06</p>
    <h2>Bayes' Theorem</h2>
    <div class="rule-line"></div>

    <p>Reverses conditional probability — lets you update the probability of a cause given that you've observed an effect.</p>

    <div class="formula-block">
      <div class="formula-label">Bayes' Formula</div>
      <code>P(A | B) = [ P(B | A) · P(A) ] / P(B)</code>
      <div class="formula-note">// P(A) = prior · P(B|A) = likelihood · P(A|B) = posterior</div>
    </div>

    <div class="callout">
      <strong>📧 Spam Filter Example</strong>
      <p>20% of emails are spam. 90% of spam contains "free". 10% of legitimate email also contains "free".<br>
      → P(spam | "free") = (0.9 × 0.2) / 0.22 ≈ <strong>0.818</strong></p>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ══ 07. RANDOM VARIABLES & STATS ══ -->
  <section class="chapter">
    <p class="chapter-num">Chapter 07</p>
    <h2>Random Variables &amp; Descriptive Statistics</h2>
    <div class="rule-line"></div>

    <div class="grid-2">
      <div class="card card-accent">
        <h3>Discrete Random Variable</h3>
        <p>Takes a countable number of values. Each value has a specific probability.</p>
        <ul style="margin-top:10px;">
          <li>Number of heads in 10 coin flips</li>
          <li>Number of defects in a batch</li>
        </ul>
      </div>
      <div class="card card-teal">
        <h3>Continuous Random Variable</h3>
        <p>Takes any value in a range. Probabilities are defined over intervals (areas under a curve).</p>
        <ul style="margin-top:10px;">
          <li>Human height or weight</li>
          <li>Temperature readings</li>
        </ul>
      </div>
    </div>

    <h3 style="font-family:'Playfair Display',serif; font-size:1.3rem; margin: 28px 0 16px;">Measures of Central Tendency &amp; Spread</h3>

    <table class="event-table">
      <thead><tr><th>Measure</th><th>Description</th><th>Formula</th></tr></thead>
      <tbody>
        <tr><td>Mean (μ)</td><td>Arithmetic average</td><td class="formula-inline">μ = Σxᵢ / n</td></tr>
        <tr><td>Weighted Mean</td><td>Average with weights</td><td class="formula-inline">μ = Σwᵢxᵢ / Σwᵢ</td></tr>
        <tr><td>Median</td><td>Middle value when sorted</td><td class="formula-inline">middle of sorted list</td></tr>
        <tr><td>Mode</td><td>Most frequent value</td><td class="formula-inline">max frequency</td></tr>
        <tr><td>Variance (σ²)</td><td>Average squared deviation</td><td class="formula-inline">σ² = Σ(xᵢ−μ)² / n</td></tr>
        <tr><td>Std. Dev. (σ)</td><td>Square root of variance</td><td class="formula-inline">σ = √σ²</td></tr>
      </tbody>
    </table>
  </section>

  <div class="divider"></div>

  <!-- ══ 08. DISTRIBUTIONS ══ -->
  <section class="chapter">
    <p class="chapter-num">Chapter 08</p>
    <h2>Probability Distributions</h2>
    <div class="rule-line"></div>

    <p>A probability distribution describes how probability is spread across all possible values of a random variable.</p>

    <div class="grid-2" style="margin-top:28px;">
      <div class="card card-accent">
        <h3>🎯 Binomial Distribution</h3>
        <p>Counts successes in <em>n</em> independent trials, each with probability <em>p</em>.</p>
        <div style="margin-top:14px;">
          <code style="font-family:'JetBrains Mono',monospace; font-size:0.8rem; color:var(--accent); line-height:1.8; display:block;">
            P(X=k) = C(n,k) · pᵏ · (1−p)ⁿ⁻ᵏ
          </code>
        </div>
        <ul style="margin-top:14px;">
          <li>Fixed number of trials</li>
          <li>Two outcomes only (success / failure)</li>
          <li>Constant probability per trial</li>
          <li>Independent trials</li>
        </ul>
      </div>
      <div class="card card-teal">
        <h3>🎲 Uniform Distribution</h3>
        <p>All outcomes are equally likely — maximum entropy distribution.</p>
        <div style="margin-top:14px;">
          <code style="font-family:'JetBrains Mono',monospace; font-size:0.8rem; color:var(--teal); line-height:1.8; display:block;">
            P(X = xᵢ) = 1/n (discrete)<br>
            f(x) = 1/(b−a) (continuous)
          </code>
        </div>
        <ul style="margin-top:14px;">
          <li>Standard die roll</li>
          <li>Random number generator</li>
        </ul>
      </div>
    </div>
  </section>

</div>

<!-- ══ IMAGE FEATURE 3: Normal Distribution ══ -->
<div class="image-feature" style="margin-left:0;margin-right:0;padding-left:max(40px, calc(50% - 480px + 40px));padding-right:max(40px, calc(50% - 480px + 40px));">
  <div class="image-feature-text">
    <span class="tag">Normal Distribution</span>
    <h3>The Bell Curve</h3>
    <p>The most important distribution in all of statistics. Symmetric around the mean, with probabilities concentrated near the center and tailing off symmetrically. The empirical rule lets you quickly estimate how much data falls within 1, 2, or 3 standard deviations.</p>
  </div>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Standard_deviation_diagram.svg/1200px-Standard_deviation_diagram.svg.png"
       alt="Normal distribution bell curve with standard deviations"
       onerror="this.style.display='none'">
</div>

<div class="container">

  <!-- ── NORMAL DIST DETAIL ── -->
  <section style="padding: 40px 0 20px;">
    <h3 style="font-family:'Playfair Display',serif; font-size:1.5rem; margin-bottom:16px;">🔔 Normal Distribution Properties</h3>
    <div class="grid-2">
      <div>
        <ul style="line-height:2; color:#444; font-size:0.93rem; padding-left:16px;">
          <li>Mean = Median = Mode (perfect symmetry)</li>
          <li>Total area under the curve = 1</li>
          <li>Defined by two parameters: μ (mean) and σ (std dev)</li>
          <li>Asymptotically approaches zero at extremes</li>
        </ul>
      </div>
      <div class="formula-block" style="margin:0;">
        <div class="formula-label">PDF Formula</div>
        <code>f(x) = (1 / σ√2π) · e^(−(x−μ)²/2σ²)</code>
      </div>
    </div>

    <h3 style="font-family:'Playfair Display',serif; font-size:1.3rem; margin: 36px 0 16px;">⚡ The Empirical Rule (68–95–99.7)</h3>
    <div class="empirical">
      <div class="emp-card emp-68">
        <div class="pct">68%</div>
        <div class="sigma">within ±1σ</div>
      </div>
      <div class="emp-card emp-95">
        <div class="pct">95%</div>
        <div class="sigma">within ±2σ</div>
      </div>
      <div class="emp-card emp-99">
        <div class="pct">99.7%</div>
        <div class="sigma">within ±3σ</div>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ── CONCLUSION ── -->
  <section class="chapter" style="padding-bottom:48px;">
    <p class="chapter-num">Conclusion</p>
    <h2>Key Takeaways</h2>
    <div class="rule-line"></div>

    <div class="grid-2">
      <div class="card" style="border-top:3px solid var(--gold);">
        <h3>Core Concepts</h3>
        <ul>
          <li>Probability lives on [0, 1] — always</li>
          <li>Addition rule handles union of events</li>
          <li>Multiplication rule handles intersection</li>
          <li>Conditional probability updates with evidence</li>
        </ul>
      </div>
      <div class="card" style="border-top:3px solid var(--ink);">
        <h3>Advanced Topics</h3>
        <ul>
          <li>Bayes' theorem inverts conditional probability</li>
          <li>Binomial distribution models success counts</li>
          <li>Normal distribution is universal in nature</li>
          <li>σ and μ fully describe the normal curve</li>
        </ul>
      </div>
    </div>

    <div class="tip-box">
      <span class="tip-icon">⭐</span>
      <p><strong>Pro Tip:</strong> The best way to internalize probability is through daily problem-solving. Start with classical problems (dice, cards, coins), then move to real-world applications like quality control, medical testing, and machine learning classification — where Bayes' theorem and distributions dominate.</p>
    </div>
  </section>

</div>

<footer class="footer">
  <span class="footer-brand">Probability &amp; Statistics Notes</span>
  <span>Chapters 01–08 · Complete Reference</span>
  <span>0 ≤ P(E) ≤ 1</span>
  <span style="color:var(--gold); font-family:'Playfair Display',serif; font-size:1rem; font-weight:700; letter-spacing:0;">✍️ Created by Sayan</span>
</footer>

</body>
</html>
