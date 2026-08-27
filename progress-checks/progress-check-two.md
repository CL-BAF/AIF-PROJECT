# Progress Check Two

*(AT2 Progress Checks, Part Two. Word budgets per the assessment sheet: PA2 400, PA3 100, A2 250. Covers the period since Progress Check One; every claim is anchored to portfolio evidence — the Strategy Tracking table, the Feedback and Perspectives record, and the dated commit log.)*

## PA2 — Managing time and resources

I have been reflecting on strategy effectiveness the way my project itself works: by assuming each strategy is wrong and demanding evidence that it isn't. My Strategy Tracking table rates every strategy out of five with recorded evidence, and reading it honestly revealed a pattern I would have missed by feel: my two 5-rated strategies — the adversarial audit loop and test-pinning invariants — are built to *falsify* my belief that the system is correct, while my 4-rated strategies — calendar planning and secondary research — are passive: they inform decisions without ever testing them. The audit loop has closed every phase since late July with a fix commit, and my last full audit produced 1 critical, 6 high, 16 medium and 21 low findings. That distinction now governs my time: falsifying strategies get scheduled first, because passive ones can absorb unlimited hours without proving anything.

An unexpected opportunity came from the security feeds themselves. I had planned live ingestion of the CISA KEV and MITRE ATT&CK catalogues to give my agent real data; it proved equally valuable for testing my own code with messy reality. The vault grew from 12 to 323 records across the static seed and the live feeds, and the live run surfaced two design defects no unit test had imagined. I responded with compounding decisions: fix the parsers rather than loosen the validation limits, keep every feed on an allowlisted, IP-pinned fetcher, and let records enter only as *unreviewed*. A second opportunity was reframing my constraint — no write access to the live machine — into the two-person deploy rule, with timestamped backups before every copy, which now also protects me from my own deploy mistakes.

The sharpest challenge came on that first live run: all of my roughly 2,100 tests passed, yet the run failed immediately, because a fake connection in one test accepted a keyword the real Python API rejects. My tests had been agreeing with my mistake. I addressed it with a regression test asserting that mocks mirror the real API signature, and a portfolio rule: a mock that accepts what the real interface wouldn't is a bug in the test. A second risk was two weeks of finished work — including a whole OSINT subsystem — uncommitted on one machine; I scheduled slice-by-slice commits with passing tests. A third was data leaving my machines: cloud models stayed optional behind two independent consent gates, with local models the default.

*(399 words)*

## PA3 — Making judgements and decisions

My key decisions were judgements about restraint, each evidence-led. When the audit found a window where an approved action could fire twice, I ranked it critical above every feature, because exploitability matters more than embarrassment. When ingestion broke on real data, I judged the validation limits worth keeping and fixed the parsers instead — loosening a guard to pass a test is how a system becomes unsafe. And finding my supervisor daemon unable to approve actions, I kept it that way deliberately, enforcing the restriction in three independent layers.

*(88 words)*

## A2 — Appraising the impact of strategies perspectives and/or feedback to the learning

The most valuable feedback of this period came from the collision between my sources, because no single source sufficed alone. The authoritative feeds told me what is true in the world; the adversarial audits told me where my code diverged from what I believed; the live run told me where even my audits and tests were wrong together. Each caught what the others could not: documents describe happy paths, audits reason from my code's assumptions, and my tests encode them verbatim. Only running all three exposed the FakeConn defect — exactly where official documentation contradicted my test's fake.

What made these sources valuable was how they connected. The feeds filled the vault; the vault's ingestion failures became audit findings; the findings became fixes; the fixes were pinned as tests so they cannot silently regress. That chain — research producing failures, failures producing feedback, feedback pinned as tests — turned one bad afternoon into three permanent improvements.

What I still lack is a perspective outside that loop: a human who did not build the system judging whether it is safe. My expert outreach begins this week, and the critical audit finding stays open until someone independent has examined it — the most valuable feedback I can still receive cannot be generated from inside my own project.

*(211 words)*

**Total: 698 words** — within the Part Two budgets (PA2 400 / PA3 100 / A2 250) and inside the 1500-word combined cap when added to Progress Check One (621).
