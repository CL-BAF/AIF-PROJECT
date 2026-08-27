# AIF Reflection Sheet (filled)

*(Portfolio item — the teacher's AT1 & AT2 Reflection Sheet, completed 27 August 2026.
Being specific on purpose: each answer names actual evidence, not general statements.)*

| | |
|---|---|
| **Name** | CL |
| **Date** | 27 August 2026 |
| **My Learning Goal** | To design, build and safely operate Kobald — a governed autonomous AI system for research and authorised security work — and learn how trustworthiness is engineered into a system that can take real actions ("autonomous in thought, cautious in action") |

## AT1: Portfolio

### 1. What I have done so far *(E1, E2, E3, PA1)*

Built and deployed the system end to end: ~50,000 lines of Python across ~100 modules with
~2,100 tests (122 test files), running live on a second machine over an encrypted private
network since late July. Evidence by criterion — **E1:** the idea evolved from "a helpful AI
assistant" to a governed agent with a default-deny approval engine, after exploring what could
go wrong; **E2:** eight strategies tracked in `strategy-tracking.md` (seven rated; class speed-dating not yet trialled);
**E3:** five perspective types mapped (`feedback-and-perspectives.md`); **PA1:** feedback from
audits, live failures and the assessment handouts — each with an action and a "what changed".

### 2. What I might be missing *(E3, PA1)*

**Human perspectives.** Every reviewer, document and test in my portfolio so far is either
mine, machine-generated, or impersonal documentation. No independent human has examined the
security claims. The critical audit finding (a window where an approved action could fire
twice) is exactly the kind of thing I should not close alone.

### 3. What I'm unsure about *(E1)*

How much portfolio evidence is "enough" per criterion, and where the line sits between a
*perspective* (someone's view I synthesise) and *feedback* (a response to my work) — my
adversarial audits are arguably both. I have asked my teacher to check my read of this in
Progress Check One.

### 4. What I need to STOP doing *(E2)*

Treating the code as the output and the portfolio as an afterthought. The handout is explicit:
the process is the assessment. I have also been leaving finished work uncommitted (112 paths
as of this week) — that stops now, in slices, starting this week.

### 5. How I am progressing my learning *(E1, E2)*

Steadily toward the goal, with evidence: the system's core claim has been demonstrated live —
an agent researched real questions while every state-changing action paused for my approval,
and a plain-language chat returns a governed answer in under a minute. Progress is measurable
in dated commits and passing tests, not vibes.

## AT2: Progress Checks

### 1. What I have done so far *(PA2, PA3, A2)*

Progress Check One drafted to the section word budgets (PA2 146 / PA3 344 / A2 131),
naming three sources/strategies and judging each on currency/reliability, relevance and
purpose per the PA3 advice.

### 2. What I might be missing *(PA3, A2)*

Genuinely new evidence for Check Two: the strongest recent material (the live feed ingestion,
the conversational-chat fix, Work Mode) is still uncommitted, so it is not yet properly
documented as portfolio evidence.

### 3. What I'm unsure about *(A2)*

Whether "appraising" needs a measured counterfactual ("this strategy moved my learning by X")
or a argued judgement with criteria. I have drafted for the latter, using the rubric's A-band
verbs, and will confirm with the teacher's response to Check One.

### 4. What I need to STOP doing *(PA2)*

Recounting actions ("I built X") without linking them to what I learned or decided — the
Reflection Sheet warns this directly, and my earlier drafts drifted that way.

### 5. How I am progressing my learning *(PA2, PA3, A2)*

My definition of "done" has visibly changed between drafts: from "the feature works" to
"it fails loudly, its guarantees are pinned by tests, and its residual gaps are documented
honestly" — the codebase now publicly documents its one known rollback blind spot rather than
hiding it. That shift is the clearest single piece of metacognitive progress I can point to.

## Turning this into action

1. **This week:** send the expert-contact emails drafted in `expert-outreach.md`; follow up
   after one week if silent.
2. **This week:** commit the uncommitted work in slices, each with a passing test run, so
   Check Two's evidence is properly dated.
3. **Before Check Two:** incorporate the teacher's Check One feedback as a new entry in
   `feedback-and-perspectives.md` — with the action and the "what changed" already planned.