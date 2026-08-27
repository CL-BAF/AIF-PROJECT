# Progress Check One — Current Draft

*AT2 Progress Checks, Part One. This draft uses evidence available by 27 August 2026. It avoids presenting uncaptured working-copy claims as verified facts.*

## PA2 — Managing time and resources

My learning goal is to design and safely operate Kobald, a research assistant where a person remains responsible for state-changing actions. I am progressing because I changed a too-big hardware goal into manageable, dated phases. Git evidence begins on 8 July and records security/data-integrity work, a research-runtime boundary, a review queue and later deployment hardening. I also managed the resource problem instead of ignoring it: when cloud capacity and high-end GPU access were unreliable or expensive, I contacted local organisations and technical contacts, made a parts list, and used donated computers and networking equipment where possible. The biggest risk is false confidence — especially if old test numbers become a substitute for a current check. My response is to keep small commits, save backups before deployment, and add a redacted current test/approval-flow capture before final submission. That is more useful than claiming the system is finished.

*(149 words)*

## PA3 — Making judgements and decisions

The most important decision was changing the direction from building the most powerful local AI I could afford to investigating what makes an AI system trustworthy. I made that decision after comparing three perspectives. First, the practical resource perspective: cloud limits, cost and hardware availability made the original GPU-first plan fragile. Second, community and donor responses showed that support depends on a clear brief, realistic budget and staged needs, not just an ambitious idea. Third, technical and security perspectives showed that a capable system still needs boundaries, provenance and human review.

I judged the staged direction as better because it makes the learning goal achievable while keeping the difficult question. Instead of waiting for ideal hardware, I could test controls such as default-deny approval, audit logging and review states. The 13 July runtime-boundary commit is evidence that this was not just an idea: I separated research from action. Later changes also show that I chose safety work before extra features: the record includes data-integrity fixes, a task-breaking error fix and concurrency hardening.

I also judged my checking strategies differently. Official documentation is authoritative for what an interface is meant to do, but it mainly shows normal behaviour. Automated tests are fast and repeatable, but they can repeat my mistakes. A live run exposed a `build_context` problem that earlier checks did not show. Therefore I decided to use documentation, tests, adversarial checks and live testing together. Each one has a different purpose, so they can challenge rather than simply confirm each other.

This was a discerning choice because the methods do not have equal consequences. Documentation prevents me from inventing an API; automated tests stop known problems returning; adversarial checks focus attention on harmful behaviour; and live testing checks whether the other three survive real conditions. If the methods disagree, I will investigate the disagreement instead of choosing the evidence that feels most reassuring.

*(344 words)*

## A2 — Appraising impact

The strategy that has most improved my learning is trying to find where my confidence is wrong. The live failure was frustrating, but it was stronger evidence than another passing test because it showed a real gap in my process. It changed my plan from “increase the test count” to “use several kinds of evidence and capture a current result.” Feedback on my Rotary presentation had a similar impact: it made me explain AI risks in clearer language and plan for a demo failure. These strategies progressed my goal because trust is not only technical. A system also has to be understandable, reviewable and honest about its limits. My next improvement is external technical feedback, because my current safety loop still has too much of my own perspective in it.

*(130 words)*

**Approx. 590 words** — within the suggested 500–750 words for the first progress check.
