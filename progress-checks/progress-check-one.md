# Progress Check One

*(AT2 Progress Checks, Part One. Word budgets per the assessment sheet: PA2 100–150, PA3 300–350, A2 100–150. Every claim is anchored to portfolio evidence: the dated commit log, the Strategy Tracking table, and the Feedback and Perspectives record.)*

## PA2 — Managing time and resources

My learning goal is to design, build and safely operate Kobald, a governed AI system that researches autonomously but takes no state-changing action without my approval. I am on track, and I know because the evidence is measurable rather than felt: the core is roughly 50,000 lines of Python across about 100 modules, covered by around 2,100 tests, versioned in over one hundred dated commits since 8 July, and it runs live on a second machine over an encrypted private network. The core claim — *autonomous in thought, cautious in action* — has been demonstrated end to end: agents research real questions while every state-changing action pauses for my approval. Time is managed in numbered phases of small, dated commits, so a bad week cannot erase a good one. My scarcest resource, write access to the live machine, became a two-person deploy rule with backups before every copy.

*(146 words)*

## PA3 — Making judgements and decisions

The three most useful sources and strategies in my portfolio so far are my adversarial audit sessions, the authoritative security feeds I ingest, and the official documentation of the platform I build on.

The most valuable strategy has been the **adversarial audit loop**: at the end of each phase, reviewer sessions run with a single mandate — *break it*. Judged against the three criteria. Currency: repeated every phase, so findings never age. Relevance: it targets the risk that matters — a mistake is not a lost mark but a double-fired command or a leaked token. Purpose: it finds defects before they become real-world harm. Critically: my last full audit returned 1 critical, 6 high, 16 medium and 21 low findings, and I deliberately did not fix all 44. Fixing everything at once would bury the critical finding (a window where an approved action could fire twice), so I ranked by exploitability and documented the rest — that critique made the strategy *useful*, not merely thorough.

Second, the **CISA KEV and MITRE ATT&CK catalogues**, ingested live by my system. Currency: KEV updates continuously, and both feeds were pulled from the source on 15 August by a fetcher that pins the server's IP to defeat DNS rebinding. Relevance: they give my agent a real, current threat vocabulary instead of invented examples. Purpose: they test my own system with messy real-world data — and passed it by failing: ingestion surfaced two design bugs (claim-length caps, dotted ATT&CK identifiers), which I fixed in the parsers rather than loosening the validation limits. I judged their trustworthiness structurally: records enter as *unreviewed*, and only a human can promote them to trusted.

Third, the **official Python, Starlette and systemd documentation**. Currency: version-matched to the interpreter and platform I run. Relevance: my design decision — a standard-library-only core — rests on knowing what the library provides. Purpose: it let me delete dependencies I would otherwise have to trust and audit. Its limitation, verified against the source: documentation describes happy paths — the signature my test's fake connection got wrong was documented correctly all along; my mock was the lie.

*(344 words)*

## A2 — Appraising the impact of strategies, perspectives and/or feedback to progress the learning

My research is headed toward independent scrutiny. The strategies I have used — adversarial audits, test-pinned invariants, live smoke testing — are effective at finding defects, but they share one flaw: every perspective in my portfolio so far is either mine, machine-generated, or impersonal documentation. All three inherit my blind spots, so no amount of the same will tell me whether Kobald is actually safe to operate. What needs development next is human perspective: the expert-contact emails drafted in my portfolio go out this week (with a one-week follow-up rule), classmates will test whether I can explain the system without jargon, and my teacher's response to this check becomes the next entry in my feedback record. The reason: the one critical finding outstanding should not be closed by the person who created it.

*(131 words)*

**Total: 621 words** — within the suggested 500–750 for the first check.
