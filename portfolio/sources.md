# Sources List

*(Portfolio item — per the teacher's advice these are recorded as links, not formal citations.
Each entry notes what I gained and how it influenced the next step.)*

## Primary project / output evidence

| # | Source | What I gained → how it influenced my next step |
|---|--------|------------------------------------------------|
| 1 | `https://github.com/CL-BAF/Kobald` — my project repository (106+ dated commits, 2026-07-08 → 2026-08-03, plus current work) | The commit log *is* my process evidence → every Progress Check claim is anchored to a dated commit |
| 2 | `https://github.com/CL-BAF/AIF-PROJECT` — this portfolio repository | Portfolio reorganised around the criteria codes (E1–E3, PA1–PA3, A2) |

## Authoritative security data (ingested live into the Knowledge Vault, 2026-08-15; with the static seed and after dedup and claim caps the vault grew 12 → 323 records)

| # | Source | What I gained → how it influenced my next step |
|---|--------|------------------------------------------------|
| 3 | CISA Known Exploited Vulnerabilities (KEV) catalogue — `https://www.cisa.gov/known-exploited-vulnerabilities-catalogue` | 50 real, current exploitation records → proved the ingestion pipeline works on messy real-world data (claim-length caps had to be fixed in the parser) |
| 4 | MITRE ATT&CK Enterprise knowledge base — `https://attack.mitre.org/` (STIX bundle) | 81 tactic/technique records including sub-techniques → exposed the dotted-identifier bug (T1564.008) and taught me to read a data schema before ingesting it |
| 5 | NVD CVE feed — `https://services.nvd.nist.gov/` | 50 vulnerability records → confirmed currency/reliability judgment: records enter as *unreviewed*, never auto-trusted |
| 6 | GitHub Security Advisories (GHSA) — `https://api.github.com/` | 50 advisories → completed the four-feed test of the fetcher's SSRF/DNS-rebinding protections |

## Technical documentation (primary sources for design decisions)

| # | Source | What I gained → how it influenced my next step |
|---|--------|------------------------------------------------|
| 7 | Python standard library documentation (3.13) — `https://docs.python.org/3/` | What the stdlib already provides (sockets, HMAC, urllib, unittest) → justified the stdlib-only core design; where docs describe happy paths I cross-checked the source |
| 8 | Starlette documentation — `https://www.starlette.io/` | Route/middleware model for the HTTP control plane → 97 explicitly declared routes instead of decorator magic, so the surface is auditable |
| 9 | systemd manual pages — `https://www.freedesktop.org/software/systemd/man/` | Service hardening flags (NoNewPrivileges, ProtectSystem=strict, RestrictAddressFamilies) → both live services hardened directly from the manual |
| 10 | Tailscale documentation — `https://tailscale.com/kb` | Private encrypted networking between my machines → replaced any public exposure of the control plane; the only unauthenticated route is a health check |
| 11 | Mullvad VPN — `https://mullvad.net/help` | Kill-switch networking for the isolated worker VM → state-changing actions execute only inside a disposable VM with no direct internet identity |
| 12 | Ollama documentation — `https://ollama.com` / `https://github.com/ollama/ollama` | Local model hosting → cloud models are now consent-gated (two independent gates) after reading how cloud calls transmit data |

## Assessment and course documents (teacher-provided)

| # | Source | What I gained → how it influenced my next step |
|---|--------|------------------------------------------------|
| 13 | Simplified Performance Standards Rubric | The A-band verbs (*discerning*, *synthesises*, *related impact*) → I now judge sources on criteria instead of naming them |
| 14 | AT2 Progress Check Combined sheet (task outline, success criteria, word budgets) | The exact section structure and the "success criteria checklist" → drafted both checks to per-section word budgets |
| 15 | "AIF STUFF FOR LKOBALD" lesson notes | "The output is not an assessment; it informs the assessment. EVERYTHING goes in the portfolio" → rebuilt the portfolio around the teacher's tables |
| 16 | Strategy Tracking + Reflection Sheet templates | The structure for my own filled versions in this repo |
| 17 | Selecting and Using Perspectives handout | The distinction between perspectives (before decisions) and feedback (after) → restructured `feedback-and-perspectives.md` around it |

## Community / social

| # | Source | What I gained → how it influenced my next step |
|---|--------|------------------------------------------------|
| 18 | GitHub project pages and issue trackers for the open-source tools I depend on (Starlette, uvicorn, Ollama) | Real-world failure modes and upgrade notes → informed my decision to pin versions and keep the core importable without any of them |