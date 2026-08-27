# Strategy Tracking

*(Portfolio item — the teacher's Strategy Tracking table, filled from the real project log.
Supports E2; evidence base for PA2/A2 in both Progress Checks.)*

| Strategy used + brief description | Why I chose this strategy | Rating of effectiveness (1-5) | Evidence of effectiveness | Where does this lead me? Where to next? |
|---|---|---|---|---|
| **AIF timetable** — placed my to-do list on a calendar with due dates (see `learning-goal-and-plan.md`) | Allowed me to visualise what I need to do and when | 4 | Milestones landed in date order (07-08 foundation → 07-31 policy layer → 08-03 multi-agent spine); the two busiest days were batching of pre-planned small steps, not cramming | Keep the deadline table updated weekly; add the PC2 date once the teacher confirms it |
| **Numbered-phase plan with small dated commits** — every change lands as its own commit ("Phase 3 Step 5: …"), so progress is measurable | A bad week cannot erase a good one; each commit is a rollback point | 5 | 106+ dated commits since 2026-07-08; each phase closed with a fix commit; I can point my teacher at any exact date | Continue for the OSINT subsystem; commit the current untracked work in slices |
| **Adversarial audit loop** — at the end of each phase, reviewer sessions with a single mandate: *break it* | I am the worst reviewer of my own code; a hostile reviewer finds what I rationalise | 5 | Every phase since late July closed with a "confirmed findings" fix commit; my last full audit produced 1 critical, 6 high, 16 medium, 21 low findings | Commission the same treatment from a *human* expert — AI reviewers may share my blind spots |
| **Test-pinning invariants** — every security guarantee is written as a test (~2,100 tests, 122 files) | Documentation can drift; a test that fails loudly cannot | 5 | Guarantees like "the supervisor can never approve" are pinned by tests AND a server-side refusal — three independent layers | Extend to the untracked OSINT tests; keep the "specs never silently fail" suite growing |
| **Live smoke testing on the real deployed machine** — after every change, exercise the running system, not just the tests | A test suite is a model of reality; reality has the final vote | 5 | Caught a bug every green test missed: a fake test connection accepted a keyword the real Python API rejects — it surfaced only on the first live feed refresh | Re-run the full live smoke pass after the next deploy; record results in the portfolio |
| **Secondary research: authoritative security feeds** (CISA KEV, MITRE ATT&CK, NVD, GHSA) ingested into the project's Knowledge Vault | Real data beats invented examples; also *tests* my system with real-world input | 4 | Vault grew 12 → 323 records on 15 Aug; ingestion caught two real design bugs (claim-length caps, dotted ATT&CK identifiers) | Add source-ageing so records refresh automatically; list every feed in `sources.md` |
| **Secondary research: official documentation** (Python stdlib docs, Starlette, systemd, Tailscale) before every design decision | Primary sources for how the platform actually behaves | 4 | The stdlib-only design decision came from reading what the library already provides; systemd hardening flags came straight from the manual | Compare a doc-only understanding against a YouTube walkthrough of the same topic (metacognition exercise from class) |
| **Speed-dating perspectives with classmates** (class exercise, upcoming) | A non-technical reader will catch where my explanations assume too much | — not yet trialled | — | Trial it; record what questions classmates ask — those are my explanation gaps |

## What the ratings tell me (metacognition)

My two 5-rated strategies (adversarial audit, test-pinning) share one property: **they assume
I am wrong and set out to prove it.** My 4-rated strategies (planning, secondary research) are
necessary but passive — they inform, they don't falsify. The gap in my strategy set is
*human* perspective: everything so far is AI reviewers, official documents, and my own tests,
which all inherit my blind spots. That is exactly where the expert-contact strategy fits.