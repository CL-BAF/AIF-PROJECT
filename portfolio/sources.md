# Sources and How I Used Them

This is a source-use record, not just a bibliography. The assessment advice asks for evidence of what a source contributed and how it shaped the next step.

| Source / perspective | Why it was relevant | What I took from it | What I did next | Evidence status |
|---|---|---|---|---|
| Kobald commit history and public showcase | Primary development record | Dated changes, stated limitations and early test milestones | Used the history to reconstruct decisions rather than relying on memory | **Verified capture** |
| Official Python/platform documentation | Needed to know actual interface behaviour and deployment constraints | Documentation is authoritative for intended APIs but does not test my implementation | Compared it against live/mocked behaviour; added the need for real-interface checks | **Verified capture** as a source-use record |
| CISA KEV and MITRE ATT&CK-style security sources | Relevant examples of structured, current security information | Source data needs provenance and review before it is trusted in my project | Designed for allowlisted ingestion and human review; parser-fix capture still needed | Mixed: source choice is **verified**; current project result is **reported working-copy evidence** |
| School assessment advice, rubric and progress-check slides | Defines what counts as AIF evidence | Process, decisions, perspectives and feedback are assessed; output alone is not | Reorganised this repository around evidence status and reflection | **Verified capture** — supplied documents |
| Council, business, regional-development and community correspondence | Real constraints on funding, hardware and eligibility | A strong idea still needs a realistic budget, clear project brief and suitable funding path | Made a staged resource plan and continued targeted outreach | **Verified capture** — email history |
| Zoe Dalton’s presentation feedback | Audience needs and communication quality | Technical detail needed a clearer story, better readability and a contingency | Revised presentation language and demo plan | **Verified capture** — email history |

## Source evaluation

I judged sources by authority, currency, relevance and purpose, but I also considered their limits. Official documentation is reliable for what an interface is designed to do, not proof that my code uses it safely. A live security feed can be current and authoritative, but it can still expose parser errors in my own system. Community correspondence is not technical evidence, but it is strong evidence about local resources, eligibility and the clarity of my communication. Using the sources together gave me more useful decisions than treating any one source as final proof.
