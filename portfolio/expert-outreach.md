# Expert Outreach Plan

*(Portfolio item — E3/PA1. Status: **drafted, not yet sent** — this page records the plan, the
reasons, and the drafts, per the teacher's advice: contact early, follow up after one week.)*

## Why I am contacting experts

Every perspective in my portfolio so far is either my own, machine-generated, or impersonal
documentation. For a security-sensitive system, that is a structural weakness: AI reviewers
can share my blind spots, documents describe happy paths, and my tests can only check the
assumptions I already made. An independent human expert is the one perspective that can
genuinely falsify my claim that Kobald is safe to operate.

## Who I am contacting, and why them

| Person / role | Why chosen | What I hope to get |
|---|---|---|
| **My AIF teacher** | Knows the assessment; can check my read of "perspectives vs feedback" and whether my evidence is strong enough | Calibration of my portfolio before Progress Check Two |
| **A maintainer of an open-source project I depend on** (Starlette or Ollama, via their GitHub discussions) | They reason about safety and API contracts for thousands of users; public Q&A also leaves a citable record | A critique of my API-goes-wrong assumptions (auth, redirects, consent gates) |
| **A security professional in my extended network** (family friend in IT / local tech meetup contact) | Practices exactly the discipline I am simulating: adversarial thinking about systems that take real actions | A review of my threat model — especially the one critical audit finding I should not close alone |
| **Classmates** (speed-dating exercise, class time) | Non-experts find unexplained assumptions | A test of whether I can explain Kobald without jargon |

## Draft email (to send this week — by Friday 28 August)

> **Subject:** Year 12 student building a safety-gated AI system — 20 minutes of your advice?
>
> Hi [name],
>
> I'm a Year 12 student in South Australia working on my Activating Identities and Futures
> project. I'm building a small open-source system called Kobald: an AI agent that can
> research autonomously but is architecturally prevented from taking any state-changing
> action without explicit human approval — a default-deny policy engine, signed state, and a
> full audit trail.
>
> I'm contacting you because [you maintain Starlette / you work in security], and my biggest
> gap is that every review of my safety claims so far has come from me or from AI tools. I'm
> not asking you to audit the code — I'd value 20 minutes of your time (email is fine) on two
> questions:
>
> 1. If you were reviewing an approval-gating design like mine, what would you attack first?
> 2. What is the most common way systems like this fool their own authors into feeling safe?
>
> My learning goal for this project is to learn how trustworthiness is engineered into a
> system that can take real actions — your perspective would directly shape what I do next,
> and I'll record how I used it in my portfolio.
>
> Thank you,
> CL

## Follow-up rule (from the teacher's advice)

If no response within **one week** (by 4 September), send one polite follow-up; if still
silent, move to the next person on the list and record the attempt in
`feedback-and-perspectives.md` — a non-response is itself evidence of managing this risk.