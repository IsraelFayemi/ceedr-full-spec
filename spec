<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ceedr v1 — Full Spec</title>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,500;12..96,600;12..96,700;12..96,800&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root {
  --bg: #f9f8f5;
  --ink: #18170f;
  --muted: #888070;
  --border: #e4e0d8;
  --surface: #f0ede6;
  --white: #ffffff;
  --green: #1e5c36;
  --green-light: #eaf3ee;
  --green-mid: #2d7a4a;
  --amber: #b45309;
  --amber-light: #fef3c7;
  --blue: #1d4ed8;
  --blue-light: #eff6ff;
  --red: #b91c1c;
  --red-light: #fef2f2;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body { background: var(--bg); color: var(--ink); font-family: 'Bricolage Grotesque', sans-serif; font-size: 14px; line-height: 1.6; }

.page { max-width: 960px; margin: 0 auto; padding: 48px 32px 80px; }

/* NAV TABS */
.tabs { display: flex; gap: 4px; margin-bottom: 48px; border-bottom: 1px solid var(--border); padding-bottom: 0; overflow-x: auto; }
.tab { padding: 10px 16px; font-size: 12px; font-weight: 500; color: var(--muted); cursor: pointer; border-bottom: 2px solid transparent; margin-bottom: -1px; white-space: nowrap; transition: all 0.15s; letter-spacing: 0.2px; }
.tab:hover { color: var(--ink); }
.tab.active { color: var(--green); border-bottom-color: var(--green); }

.panel { display: none; }
.panel.active { display: block; }

/* SECTION */
.sec { margin-bottom: 48px; }
.sec-label { font-size: 10px; font-weight: 600; letter-spacing: 2.5px; text-transform: uppercase; color: var(--muted); margin-bottom: 20px; display: flex; align-items: center; gap: 10px; }
.sec-label::after { content: ''; flex: 1; height: 1px; background: var(--border); }

/* PRICING GRID */
.pricing { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin-bottom: 16px; }
.p-card { border: 1px solid var(--border); border-radius: 10px; padding: 22px 18px; background: var(--white); }
.p-card.featured { border-color: var(--green); background: var(--green-light); }
.p-tier { font-size: 10px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; color: var(--muted); margin-bottom: 10px; }
.p-price { font-size: 36px; font-weight: 800; color: var(--ink); line-height: 1; letter-spacing: -2px; margin-bottom: 2px; }
.p-price sup { font-size: 16px; font-weight: 500; vertical-align: super; letter-spacing: 0; }
.p-cadence { font-size: 11px; color: var(--muted); margin-bottom: 18px; }
.p-lines { border-top: 1px solid var(--border); }
.p-line { font-size: 12px; color: var(--muted); padding: 7px 0; border-bottom: 1px solid var(--border); display: flex; align-items: flex-start; gap: 8px; line-height: 1.5; }
.p-line:last-child { border-bottom: none; }
.p-line::before { content: '✓'; color: var(--green); font-size: 11px; font-weight: 700; flex-shrink: 0; margin-top: 1px; }
.p-line.no::before { content: '—'; color: var(--border); }
.p-line.no { color: var(--border); }

/* CALLOUT */
.callout { border: 1px solid var(--green); border-radius: 10px; padding: 18px 20px; background: var(--green-light); margin-bottom: 16px; }
.callout-title { font-size: 13px; font-weight: 700; color: var(--green); margin-bottom: 6px; }
.callout-body { font-size: 13px; color: var(--ink); line-height: 1.75; }
.callout-body strong { color: var(--green-mid); }

.note { border: 1px solid var(--amber); border-radius: 10px; padding: 16px 18px; background: var(--amber-light); margin-top: 12px; font-size: 12px; color: var(--amber); line-height: 1.75; }
.note strong { font-weight: 600; }

/* FEATURE TABLE */
.ftable { width: 100%; border-collapse: collapse; background: var(--white); border: 1px solid var(--border); border-radius: 10px; overflow: hidden; }
.ftable th { text-align: left; font-size: 10px; font-weight: 600; letter-spacing: 1.5px; text-transform: uppercase; color: var(--muted); padding: 10px 14px; background: var(--surface); border-bottom: 1px solid var(--border); }
.ftable td { padding: 11px 14px; border-bottom: 1px solid var(--border); font-size: 12px; color: var(--muted); vertical-align: middle; }
.ftable tr:last-child td { border-bottom: none; }
.ftable td:first-child { font-weight: 600; color: var(--ink); font-size: 13px; width: 200px; }
.ftable td.hi { color: var(--green); font-weight: 500; }
.ftable td.dim { color: var(--border); }

/* BADGE */
.badge { display: inline-block; font-size: 10px; font-weight: 500; padding: 2px 8px; border-radius: 20px; white-space: nowrap; }
.badge-free { background: var(--surface); color: var(--muted); }
.badge-soft { background: var(--amber-light); color: var(--amber); border: 1px solid #fcd34d; }
.badge-paid { background: var(--green-light); color: var(--green); border: 1px solid #86efac; }
.badge-pub { background: var(--surface); color: var(--muted); }
.badge-auth { background: var(--blue-light); color: var(--blue); }
.badge-gate { background: var(--green-light); color: var(--green); }

/* PAGES */
.pages { display: flex; flex-direction: column; gap: 2px; }
.page-group-label { font-size: 10px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; color: var(--muted); padding: 16px 10px 8px; }
.page-row { display: grid; grid-template-columns: 180px 80px 1fr 80px; gap: 8px 16px; align-items: start; padding: 10px; border-radius: 8px; transition: background 0.12s; }
.page-row:hover { background: var(--surface); }
.page-name { font-size: 13px; font-weight: 600; color: var(--ink); }
.page-route { font-size: 10px; font-family: 'IBM Plex Mono', monospace; color: var(--muted); margin-top: 3px; }
.page-desc { font-size: 12px; color: var(--muted); line-height: 1.65; }
.page-badge { justify-self: end; margin-top: 2px; }

/* ROADMAP */
.road-item { display: grid; grid-template-columns: 180px 1fr; gap: 16px; padding: 14px 0; border-bottom: 1px solid var(--border); align-items: start; }
.road-item:last-child { border-bottom: none; }
.road-name { font-size: 13px; font-weight: 600; color: var(--ink); }
.road-desc { font-size: 12px; color: var(--muted); line-height: 1.65; }

@media (max-width: 700px) {
  .pricing { grid-template-columns: 1fr; }
  .page-row { grid-template-columns: 1fr auto; }
  .page-route, .page-desc { grid-column: 1 / -1; }
  .road-item { grid-template-columns: 1fr; gap: 4px; }
}
</style>
</head>
<body>
<div class="page">

  <div style="margin-bottom: 36px;">
    <div style="font-size: 11px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; color: var(--muted); margin-bottom: 8px;">Ceedr v1</div>
    <div style="font-size: 28px; font-weight: 800; letter-spacing: -1px; color: var(--ink); margin-bottom: 6px;">Full Product Spec</div>
    <div style="font-size: 14px; color: var(--muted);">About · Pricing · Feature access · Pages · Roadmap</div>
  </div>

  <div class="tabs">
    <div class="tab active" onclick="show('about')">About</div>
    <div class="tab" onclick="show('pricing')">Pricing</div>
    <div class="tab" onclick="show('features')">Feature Access</div>
    <div class="tab" onclick="show('pages')">All Pages</div>
    <div class="tab" onclick="show('roadmap')">Roadmap</div>
  </div>

  <!-- ABOUT -->
  <div id="about" class="panel active">

    <div class="sec">
      <div class="sec-label">What Ceedr Is</div>
      <div style="max-width: 640px;">
        <p style="font-size: 17px; font-weight: 600; color: var(--ink); line-height: 1.65; margin-bottom: 16px;">Ceedr is an AI-native career platform that helps professionals compete for the opportunities they deserve.</p>
        <p style="font-size: 14px; color: var(--muted); line-height: 1.85; margin-bottom: 12px;">Most qualified candidates lose jobs they should have gotten — not because they lack the skill, but because their resume never made it past an automated filter. Hiring today runs through ATS systems that scan for keywords, penalise poor formatting, and reject anything that doesn't match a template. Most people don't know this is happening to them.</p>
        <p style="font-size: 14px; color: var(--muted); line-height: 1.85;">Ceedr fixes that. Paste your CV, paste a job description, and in seconds you know your score, what's failing, and exactly what to change. For users who want more — Ceedr rewrites the resume, generates a matched cover letter, and tracks every application in one place. The gap between qualified and hired is almost always a communication problem. Ceedr closes it.</p>
      </div>
    </div>

    <div class="sec">
      <div class="sec-label">The Four Things It Does</div>
      <table class="ftable">
        <thead><tr><th>#</th><th>Feature</th><th>What it does</th><th>Access</th></tr></thead>
        <tbody>
          <tr>
            <td style="width:32px; color: var(--muted); font-weight:400;">01</td>
            <td>ATS Scoring</td>
            <td style="color: var(--muted);">Scores your CV against a specific job description out of 100. Shows the exact keywords missing, structural issues, and bullet point failures — before you apply. Score is always free. Full breakdown unlocks via referral or paid plan.</td>
            <td><span class="badge badge-free">Free + Soft gate</span></td>
          </tr>
          <tr>
            <td style="width:32px; color: var(--muted); font-weight:400;">02</td>
            <td>Resume Write / Rewrite</td>
            <td style="color: var(--muted);">Rewrites your existing CV or builds one from scratch. Result-driven bullet points, clean structure, ATS-safe formatting. Optionally tailored to a specific role if you provide a JD. Exports as PDF or DOCX.</td>
            <td><span class="badge badge-paid">Paid</span></td>
          </tr>
          <tr>
            <td style="width:32px; color: var(--muted); font-weight:400;">03</td>
            <td>Cover Letter</td>
            <td style="color: var(--muted);">Generates a cover letter matched to a specific job description and company — not a generic template. Written from the same profile as your CV so the voice and experience are consistent.</td>
            <td><span class="badge badge-paid">Paid</span></td>
          </tr>
          <tr>
            <td style="width:32px; color: var(--muted); font-weight:400;">04</td>
            <td>Application Log</td>
            <td style="color: var(--muted);">A simple tracker for every job you've applied to — company, role, date, current stage (Applied → Interview → Offer → Rejected), and which version of your CV was sent. Replaces the spreadsheet. Pattern analysis ships in v2.</td>
            <td><span class="badge badge-free">Free (capped)</span></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="sec">
      <div class="sec-label">Who It's For</div>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
        <div style="border: 1px solid var(--border); border-radius: 10px; padding: 20px; background: var(--white);">
          <div style="font-size: 13px; font-weight: 700; color: var(--ink); margin-bottom: 6px;">Working professionals switching roles</div>
          <div style="font-size: 12px; color: var(--muted); line-height: 1.75;">The primary target. They have money, urgency, and an existing CV that needs sharpening for a new direction. They're already on LinkedIn and understand the job market well enough to know what ATS scoring means.</div>
        </div>
        <div style="border: 1px solid var(--border); border-radius: 10px; padding: 20px; background: var(--white);">
          <div style="font-size: 13px; font-weight: 700; color: var(--ink); margin-bottom: 6px;">Students and fresh graduates</div>
          <div style="font-size: 12px; color: var(--muted); line-height: 1.75;">Entering a competitive market with little experience. Ceedr helps them structure what they have — academic projects, internships, skills — into a CV that passes filters and sounds professional.</div>
        </div>
        <div style="border: 1px solid var(--border); border-radius: 10px; padding: 20px; background: var(--white);">
          <div style="font-size: 13px; font-weight: 700; color: var(--ink); margin-bottom: 6px;">Diaspora targeting international roles</div>
          <div style="font-size: 12px; color: var(--muted); line-height: 1.75;">Nigerian and African professionals applying to UK, Canada, or US roles. They face format mismatches, language assumptions, and credential gaps. Ceedr adapts their experience to what those markets expect. (Post-launch module.)</div>
        </div>
        <div style="border: 1px solid var(--border); border-radius: 10px; padding: 20px; background: var(--white);">
          <div style="font-size: 13px; font-weight: 700; color: var(--ink); margin-bottom: 6px;">Freelancers pitching clients</div>
          <div style="font-size: 12px; color: var(--muted); line-height: 1.75;">Not applying for a job — but still needing to present their experience formally. Ceedr restructures their background into a professional profile and proposal template. (Post-launch module.)</div>
        </div>
      </div>
    </div>

    <div class="sec">
      <div class="sec-label">The Pricing Logic</div>
      <div style="max-width: 640px;">
        <p style="font-size: 14px; color: var(--muted); line-height: 1.85; margin-bottom: 12px;">Job hunting is a sprint, not a subscription. Ceedr's pricing reflects that — weekly and monthly access rather than a rolling monthly commitment. Users pay when they're actively searching and stop when they've landed. No guilt, no forgotten subscriptions.</p>
        <p style="font-size: 14px; color: var(--muted); line-height: 1.85; margin-bottom: 12px;">The free tier is deliberately generous on the ATS scoring side — because the score is the hook. A user who sees 38/100 is already sold. The paywall sits exactly where urgency peaks: at the moment they want to know why, and what to fix.</p>
        <p style="font-size: 14px; color: var(--muted); line-height: 1.85;">The referral-to-unlock mechanic on the first full report is the primary growth engine. The user most motivated to share Ceedr is a free user who just saw a bad score and urgently wants the breakdown. That's the moment the referral ask lands hardest.</p>
      </div>
    </div>

    <div class="sec">
      <div class="sec-label">Tech Stack</div>
      <table class="ftable">
        <thead><tr><th>Layer</th><th>Technology</th><th>Why</th></tr></thead>
        <tbody>
          <tr><td>Frontend</td><td>Framer</td><td style="color:var(--muted)">Marketing site and user-facing pages. Handles design and responsiveness without deep frontend engineering. Ceedr's green palette and brand applied throughout.</td></tr>
          <tr><td>Backend / API</td><td>Python · FastAPI</td><td style="color:var(--muted)">All intelligence lives here — ATS scoring engine, LLM orchestration, document generation, payment webhooks. Matches existing skill set.</td></tr>
          <tr><td>Primary AI</td><td>Claude Haiku (reports) · Claude Sonnet (rewrites)</td><td style="color:var(--muted)">Haiku for structured ATS analysis — fast and cheap. Sonnet for resume rewrites where output quality is directly user-facing.</td></tr>
          <tr><td>AI Fallback</td><td>OpenAI GPT-4o mini</td><td style="color:var(--muted)">Fallback if Claude API is down or rate-limited. Same prompt structure, same output schema. Switchable at the service layer with no user-facing change.</td></tr>
          <tr><td>ATS Scoring</td><td>spaCy · local compute</td><td style="color:var(--muted)">Score number generated locally — zero API cost. LLM only fires on full report unlock.</td></tr>
          <tr><td>Database</td><td>PostgreSQL · Prisma</td><td style="color:var(--muted)">Identity graph, document versions, application log, report cache.</td></tr>
          <tr><td>Caching</td><td>Redis</td><td style="color:var(--muted)">Same CV + same JD hash = return cached report. Eliminates repeat LLM calls for identical inputs.</td></tr>
          <tr><td>Payments</td><td>Paystack (NG) · Stripe (international)</td><td style="color:var(--muted)">Paystack for Nigerian users. Stripe for diaspora and international.</td></tr>
          <tr><td>Infra</td><td>Railway (backend)</td><td style="color:var(--muted)">Python/FastAPI services hosted on Railway. Straightforward deployment, scales with traffic.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="sec">
      <div class="sec-label">Where It Goes</div>
      <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px;">
        <div style="border: 1px solid var(--border); border-radius: 10px; padding: 20px; background: var(--white);">
          <div style="font-size: 10px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; color: var(--muted); margin-bottom: 8px;">Now</div>
          <div style="font-size: 15px; font-weight: 700; color: var(--ink); margin-bottom: 8px;">The Tool</div>
          <div style="font-size: 12px; color: var(--muted); line-height: 1.7;">Score, fix, download. Prove the unit economics. Get to 1,000 paying users. Validate that the ATS score converts free users into paying ones.</div>
        </div>
        <div style="border: 1px solid var(--border); border-radius: 10px; padding: 20px; background: var(--white);">
          <div style="font-size: 10px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; color: var(--muted); margin-bottom: 8px;">6–18 Months</div>
          <div style="font-size: 15px; font-weight: 700; color: var(--ink); margin-bottom: 8px;">The Workflow</div>
          <div style="font-size: 12px; color: var(--muted); line-height: 1.7;">Add LinkedIn script, pattern analysis, jobs on Ceedr. Users manage their whole job hunt in one place. Diaspora and Scholar modules launch.</div>
        </div>
        <div style="border: 1px solid var(--border); border-radius: 10px; padding: 20px; background: var(--white);">
          <div style="font-size: 10px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; color: var(--muted); margin-bottom: 8px;">18 Months+</div>
          <div style="font-size: 15px; font-weight: 700; color: var(--ink); margin-bottom: 8px;">The Marketplace</div>
          <div style="font-size: 12px; color: var(--muted); line-height: 1.7;">Recruiters pay to search Ceedr-standardised profiles. The talent database becomes the product. B2B revenue flips the model from consumer SaaS to platform.</div>
        </div>
      </div>
    </div>

  </div>

  <!-- PRICING -->
  <div id="pricing" class="panel">
    <div class="sec">
      <div class="sec-label">Plans</div>
      <div class="pricing">
        <div class="p-card">
          <div class="p-tier">Free</div>
          <div class="p-price">$0</div>
          <div class="p-cadence">Always</div>
          <div class="p-lines">
            <div class="p-line">Unlimited ATS score runs</div>
            <div class="p-line">Generic quality check (no JD)</div>
            <div class="p-line">First full report via referral unlock</div>
            <div class="p-line">Shareable score card</div>
            <div class="p-line no">No application log</div>
            <div class="p-line no">No resume generation</div>
            <div class="p-line no">No cover letters</div>
          </div>
        </div>
        <div class="p-card featured">
          <div class="p-tier">Weekly</div>
          <div class="p-price"><sup>$</sup>4</div>
          <div class="p-cadence">7 days · renews or expires</div>
          <div class="p-lines">
            <div class="p-line">ATS score runs — unlimited</div>
            <div class="p-line">Full ATS reports — 7 per week</div>
            <div class="p-line">Resume writes / rewrites — 3</div>
            <div class="p-line">Cover letters — 5</div>
            <div class="p-line">Application log — unlimited</div>
            <div class="p-line">PDF + DOCX download</div>
          </div>
        </div>
        <div class="p-card">
          <div class="p-tier">Monthly</div>
          <div class="p-price"><sup>$</sup>15</div>
          <div class="p-cadence">30 days · renews or expires</div>
          <div class="p-lines">
            <div class="p-line">ATS score runs — unlimited</div>
            <div class="p-line">Full ATS reports — 7 per week</div>
            <div class="p-line">Resume writes / rewrites — 10</div>
            <div class="p-line">Cover letters — 20</div>
            <div class="p-line">Application log — unlimited</div>
            <div class="p-line">PDF + DOCX download</div>
            <div class="p-line">Priority AI processing</div>
          </div>
        </div>
      </div>

      <div class="callout">
        <div class="callout-title">⚡ First Full ATS Report — Refer to Unlock</div>
        <div class="callout-body">Every user runs their ATS score free and sees the number. To unlock the full breakdown — keyword gaps, structural issues, prioritised fix list — they have two options: <strong>upgrade to weekly or monthly</strong>, or <strong>refer 2 job seekers to Ceedr</strong> and unlock it once for free. The referral link generates instantly on the result page. This is the core viral mechanic — triggered at peak urgency, right after they see a low score and need to know why.</div>
      </div>

      <div class="note">
        <strong>Why this works as a viral loop:</strong> The person most likely to share Ceedr is someone who just scored 38/100 and urgently needs the full breakdown. They share to WhatsApp groups, LinkedIn DMs, career communities. Every referred user arrives already primed — "my colleague just found out their CV was being filtered before anyone read it." Referred users convert at a higher rate than cold traffic because they arrive with context and social proof already attached.
      </div>
    </div>
  </div>

  <!-- FEATURES -->
  <div id="features" class="panel">
    <div class="sec">
      <div class="sec-label">Access by Tier</div>
      <table class="ftable">
        <thead>
          <tr>
            <th>Feature</th>
            <th>Gate</th>
            <th>Free</th>
            <th>Weekly · $4</th>
            <th>Monthly · $15</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>ATS score run</td>
            <td><span class="badge badge-free">Free</span></td>
            <td class="hi">Unlimited</td>
            <td class="hi">Unlimited</td>
            <td class="hi">Unlimited</td>
          </tr>
          <tr>
            <td>Generic quality check</td>
            <td><span class="badge badge-free">Free</span></td>
            <td class="hi">✓</td>
            <td class="hi">✓</td>
            <td class="hi">✓</td>
          </tr>
          <tr>
            <td>Full ATS report</td>
            <td><span class="badge badge-soft">Soft gate</span></td>
            <td>Refer 2 → unlock once</td>
            <td>7 per week</td>
            <td>7 per week</td>
          </tr>
          <tr>
            <td>Shareable score card</td>
            <td><span class="badge badge-free">Free</span></td>
            <td class="hi">✓ (viral mechanic)</td>
            <td class="hi">✓</td>
            <td class="hi">✓</td>
          </tr>
          <tr>
            <td>Resume write / rewrite</td>
            <td><span class="badge badge-paid">Paid</span></td>
            <td class="dim">—</td>
            <td>3 per week</td>
            <td>10 per month</td>
          </tr>
          <tr>
            <td>Cover letter</td>
            <td><span class="badge badge-paid">Paid</span></td>
            <td class="dim">—</td>
            <td>5 per week</td>
            <td>20 per month</td>
          </tr>
          <tr>
            <td>PDF / DOCX download</td>
            <td><span class="badge badge-paid">Paid</span></td>
            <td class="dim">—</td>
            <td class="hi">✓</td>
            <td class="hi">✓</td>
          </tr>
          <tr>
            <td>Application log</td>
            <td><span class="badge badge-paid">Paid</span></td>
            <td class="dim">—</td>
            <td class="hi">Unlimited</td>
            <td class="hi">Unlimited</td>
          </tr>
          <tr>
            <td>Saved document versions</td>
            <td><span class="badge badge-paid">Paid</span></td>
            <td class="dim">—</td>
            <td class="hi">✓</td>
            <td class="hi">✓</td>
          </tr>
          <tr>
            <td>Priority AI processing</td>
            <td><span class="badge badge-paid">Paid</span></td>
            <td class="dim">—</td>
            <td class="dim">—</td>
            <td class="hi">✓</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- PAGES -->
  <div id="pages" class="panel">
    <div class="pages">

      <div class="page-group-label">Public — no login required</div>
      <div class="page-row">
        <div><div class="page-name">Landing</div><div class="page-route">/</div></div>
        <div class="page-badge"><span class="badge badge-pub">Public</span></div>
        <div class="page-desc">Hero, 4-step how it works, features overview, pricing (weekly / monthly), CTA to sign up or try ATS score free.</div>
      </div>
      <div class="page-row">
        <div><div class="page-name">Sign up</div><div class="page-route">/signup</div></div>
        <div class="page-badge"><span class="badge badge-pub">Public</span></div>
        <div class="page-desc">Email + password. Google OAuth. On success → onboarding.</div>
      </div>
      <div class="page-row">
        <div><div class="page-name">Log in</div><div class="page-route">/login</div></div>
        <div class="page-badge"><span class="badge badge-pub">Public</span></div>
        <div class="page-desc">Email + password. Google OAuth. Forgot password link.</div>
      </div>
      <div class="page-row">
        <div><div class="page-name">Reset password</div><div class="page-route">/reset-password</div></div>
        <div class="page-badge"><span class="badge badge-pub">Public</span></div>
        <div class="page-desc">Email entry → confirmation email → set new password screen.</div>
      </div>
      <div class="page-row">
        <div><div class="page-name">Pricing</div><div class="page-route">/pricing</div></div>
        <div class="page-badge"><span class="badge badge-pub">Public</span></div>
        <div class="page-desc">Free vs Weekly ($9) vs Monthly ($28). Referral unlock mechanic explained. Entry to Paystack / Stripe.</div>
      </div>

      <div class="page-group-label">Onboarding — first time only</div>
      <div class="page-row">
        <div><div class="page-name">Onboarding</div><div class="page-route">/onboarding</div></div>
        <div class="page-badge"><span class="badge badge-auth">Auth</span></div>
        <div class="page-desc">Upload existing CV or paste text. Ceedr parses into identity graph. User confirms extracted data. One-time, skippable.</div>
      </div>

      <div class="page-group-label">Core App</div>
      <div class="page-row">
        <div><div class="page-name">Dashboard</div><div class="page-route">/dashboard</div></div>
        <div class="page-badge"><span class="badge badge-auth">Auth</span></div>
        <div class="page-desc">Home after login. Profile completeness, recent scores, recent documents, quick-action buttons. Plan status + usage counters shown (e.g. "2 of 3 resumes used this week").</div>
      </div>
      <div class="page-row">
        <div><div class="page-name">My profile</div><div class="page-route">/profile</div></div>
        <div class="page-badge"><span class="badge badge-auth">Auth</span></div>
        <div class="page-desc">View and edit identity graph — work history, skills, education, achievements. Persistent data every feature reads from.</div>
      </div>
      <div class="page-row">
        <div><div class="page-name">ATS scorer</div><div class="page-route">/ats</div></div>
        <div class="page-badge"><span class="badge badge-auth">Auth</span></div>
        <div class="page-desc">Upload CV (or use saved profile). Optionally paste JD or job URL. Run score. Free always. Generic check if no JD — full analysis with JD. Score visible to all.</div>
      </div>
      <div class="page-row">
        <div><div class="page-name">ATS result</div><div class="page-route">/ats/[id]</div></div>
        <div class="page-badge"><span class="badge badge-soft">Soft gate</span></div>
        <div class="page-desc">Score number shown to everyone. Full breakdown (keyword gaps, structural issues, fix priority list) shown to paid users or referral-unlocked users. Free users see: pay to unlock or refer 2 people. Shareable score card available to all.</div>
      </div>
      <div class="page-row">
        <div><div class="page-name">Referral unlock</div><div class="page-route">/refer</div></div>
        <div class="page-badge"><span class="badge badge-auth">Auth</span></div>
        <div class="page-desc">Generated when a free user hits the soft gate. Shows unique referral link. Tracks signups in real time (0/2 → 1/2 → 2/2 → unlocked). Single-use — unlocks one full report.</div>
      </div>
      <div class="page-row">
        <div><div class="page-name">Resume builder</div><div class="page-route">/resume/new</div></div>
        <div class="page-badge"><span class="badge badge-gate">Paid</span></div>
        <div class="page-desc">Create new CV. Optionally paste JD to tailor output. Pulls from profile. Counts against weekly (3) or monthly (10) limit. Gate shows upgrade prompt if limit reached.</div>
      </div>
      <div class="page-row">
        <div><div class="page-name">Resume editor</div><div class="page-route">/resume/[id]</div></div>
        <div class="page-badge"><span class="badge badge-gate">Paid</span></div>
        <div class="page-desc">View and manually edit a generated CV. Regenerate sections, download PDF or DOCX.</div>
      </div>
      <div class="page-row">
        <div><div class="page-name">My resumes</div><div class="page-route">/resumes</div></div>
        <div class="page-badge"><span class="badge badge-auth">Auth</span></div>
        <div class="page-desc">All saved CV versions — name, target role, date created, download. Linked to application log entries.</div>
      </div>
      <div class="page-row">
        <div><div class="page-name">Cover letter builder</div><div class="page-route">/cover-letter/new</div></div>
        <div class="page-badge"><span class="badge badge-gate">Paid</span></div>
        <div class="page-desc">Paste JD or URL. Pick which CV version to base it on. Generate matched cover letter. Counts against weekly (5) or monthly (20) limit. Upgrade prompt if limit reached.</div>
      </div>
      <div class="page-row">
        <div><div class="page-name">Cover letter editor</div><div class="page-route">/cover-letter/[id]</div></div>
        <div class="page-badge"><span class="badge badge-gate">Paid</span></div>
        <div class="page-desc">View, edit, regenerate, copy to clipboard, or download a specific cover letter.</div>
      </div>
      <div class="page-row">
        <div><div class="page-name">Application log</div><div class="page-route">/applications</div></div>
        <div class="page-badge"><span class="badge badge-gate">Paid</span></div>
        <div class="page-desc">Table of all logged applications — company, role, date applied, stage (Applied / Interview / Offer / Rejected), linked CV version. Paid users only. Unlimited entries. Upgrade prompt for free users.</div>
      </div>
      <div class="page-row">
        <div><div class="page-name">Application detail</div><div class="page-route">/applications/[id]</div></div>
        <div class="page-badge"><span class="badge badge-gate">Paid</span></div>
        <div class="page-desc">Single application — edit stage, add notes, view linked CV and cover letter, log follow-up activity.</div>
      </div>

      <div class="page-group-label">Account</div>
      <div class="page-row">
        <div><div class="page-name">Account settings</div><div class="page-route">/settings</div></div>
        <div class="page-badge"><span class="badge badge-auth">Auth</span></div>
        <div class="page-desc">Name, email, password change, notification preferences, delete account.</div>
      </div>
      <div class="page-row">
        <div><div class="page-name">Billing</div><div class="page-route">/settings/billing</div></div>
        <div class="page-badge"><span class="badge badge-auth">Auth</span></div>
        <div class="page-desc">Active plan, renewal/expiry date, usage this period (resumes used, cover letters used), purchase history, upgrade / cancel.</div>
      </div>

      <div class="page-group-label">System</div>
      <div class="page-row">
        <div><div class="page-name">Checkout</div><div class="page-route">/checkout</div></div>
        <div class="page-badge"><span class="badge badge-auth">Auth</span></div>
        <div class="page-desc">Weekly or monthly plan selection. Paystack for Nigeria, Stripe for international. Returns to success or failure screen.</div>
      </div>
      <div class="page-row">
        <div><div class="page-name">Payment success</div><div class="page-route">/checkout/success</div></div>
        <div class="page-badge"><span class="badge badge-auth">Auth</span></div>
        <div class="page-desc">Plan confirmed. New usage limits shown. CTA back to the feature the user was trying to unlock.</div>
      </div>
      <div class="page-row">
        <div><div class="page-name">Payment failure</div><div class="page-route">/checkout/failure</div></div>
        <div class="page-badge"><span class="badge badge-auth">Auth</span></div>
        <div class="page-desc">Payment failed. Try again CTA. Option to switch payment method.</div>
      </div>
      <div class="page-row">
        <div><div class="page-name">404</div><div class="page-route">/404</div></div>
        <div class="page-badge"><span class="badge badge-pub">Public</span></div>
        <div class="page-desc">Not found. CTA to dashboard or landing.</div>
      </div>

    </div>
  </div>

  <!-- ROADMAP -->
  <div id="roadmap" class="panel">
    <div class="sec">
      <div class="sec-label">Post-Launch Features</div>
      <div class="road-item">
        <div class="road-name">LinkedIn script</div>
        <div class="road-desc">Headline + About section rewrite generated from the same identity graph. Natural upsell once resume is done. Add to monthly plan first.</div>
      </div>
      <div class="road-item">
        <div class="road-name">Pattern analysis</div>
        <div class="road-desc">Application log v2 — surfaces which resume versions convert, which stages users drop off at, and what's working. Requires enough application data to be meaningful (50+ entries per user).</div>
      </div>
      <div class="road-item">
        <div class="road-name">Jobs on Ceedr</div>
        <div class="road-desc">Curated job listings inside the platform. Keeps users inside Ceedr rather than jumping back to Jobberman or LinkedIn. One-click apply with your Ceedr CV.</div>
      </div>
      <div class="road-item">
        <div class="road-name">Auto-apply agent</div>
        <div class="road-desc">Agentic feature — fills and submits applications automatically. High complexity. Ship only after the core document flow is stable and well-reviewed.</div>
      </div>
      <div class="road-item">
        <div class="road-name">Ceedr for Recruiters</div>
        <div class="road-desc">Separate homepage and dashboard for recruiters. Search and filter standardised Ceedr talent profiles. B2B revenue layer. Phase 3 — requires significant user base first.</div>
      </div>
    </div>
  </div>

</div>

<script>
  function show(id) {
    document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.getElementById(id).classList.add('active');
    event.target.classList.add('active');
  }
</script>
</body>
</html>
