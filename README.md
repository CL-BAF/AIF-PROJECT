# AIF-PROJECT

SACE Stage 2 **Activating Identities and Futures** (AIF) coursework repository
for **CL-BAF** — Assessment Type 2: Progress Checks (35%) and the Portfolio
evidence they draw on.

## The project behind this work: Kobald

Kobald (formerly Project JARVIS) is a governed autonomous AI control plane for
research and authorised security work, built around one principle:

> *Autonomous in thought, cautious in action.*

- **Core:** Python-standard-library-only agent runtime (~50k lines, ~100 modules,
  ~2,100 tests) with WARDEN default-deny approval gating, HMAC-sealed task
  state, redacting audit logging, a Knowledge Vault with a human review gate,
  and a multi-agent spine (supervisor, departments, specialists, monitoring).
- **Deployment:** two-host split — an always-on HTTP control plane over
  Tailscale, plus an isolated worker VM behind a kill-switch VPN for anything
  state-changing.
- **Clients:** a PySide6 desktop client and a separate Tauri/React
  "Kobald Command Centre" for Windows.
- **Source:** [github.com/CL-BAF/Kobald](https://github.com/CL-BAF/Kobald)

## Repository layout

```
progress-checks/   AT2 Progress Check One and Two (the assessed writing)
portfolio/         The evidence the checks cite (the process is the assessment)
make_docx.py       Regenerates every .docx from the markdown (python3 make_docx.py, stdlib only)
```

## Progress checks

| File | Covers | Sections (word budgets met) |
|------|--------|------------------------------|
| `progress-checks/progress-check-one.md` (+ `.docx`) | Part One — mid-project check | PA2 (146) · PA3 (344, three sources/strategies judged on currency/reliability, relevance, purpose) · A2 (131) — 621 words |
| `progress-checks/progress-check-two.md` (+ `.docx`) | Part Two — end-of-period check | PA2 (399) · PA3 (88) · A2 (211) — 698 words |

Combined: **1,319 words** of the 1,500-word cap for AT2. Every claim is
anchored to dated, verifiable evidence in the portfolio and the Kobald
commit log.

## Portfolio

| File | What it evidences |
|------|-------------------|
| `learning-goal-and-plan.md` | E1/E2 — the learning goal, output definition, milestone calendar with real dated commits, deadlines, risks |
| `strategy-tracking.md` | E2/PA2 — eight strategies tracked (seven rated 1–5) with evidence of effectiveness and "where to next" |
| `feedback-and-perspectives.md` | E3/PA1 — feedback record (who, takeaways, action, what changed) and perspectives table |
| `reflection-sheet.md` | The teacher's AT1 + AT2 reflection template, filled with specific evidence |
| `sources.md` | PA3 — sources list (links, not formal citations) with what each yielded and how it shaped the next step |
| `expert-outreach.md` | E3/PA1 — who is being contacted and why, draft email, one-week follow-up rule (drafted, not yet sent) |
| `evidence-extracts.md` | Raw verbatim evidence: commit log, security review table, runtime audit trail, deployment record, test suite |

## Regenerating the Word documents

```bash
python3 make_docx.py
```

Renders every `portfolio/*.md` and `progress-checks/*.md` to a same-named `.docx`,
plus one consolidated `AIF-AT2-Progress-Checks-and-Portfolio.docx` (the lesson advice:
"put it all together"). Hand-written OOXML — the host has no pandoc/python-docx;
stdlib only. Word-count markers and working notes stay in the markdown and are
stripped from the Word documents.