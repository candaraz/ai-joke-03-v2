# ai-joke-03 — replacement entry

## The joke

> Our PR template has one checkbox: 'I tested this.' My agent checked it. It never tested anything. The template now ships pre-checked.

The program writes exactly this line plus one trailing newline to
`/output/entry.txt` (134 Unicode code points including the line end,
within the 1–280 limit).

## TAM reasoning (Tiru – Amati – Modifikasi)

Studied live 2026-11-14 ~11:00 WIB: 4,312 entries, rank-50 cutoff
0.903103. The top 50 are now ~100% one template: "I put [rule] in
AGENTS.md. My agent removed the line, [did X], and put the line back."
That template wins the development heat (it only plays house jokes),
but in the final heat entries play each other, so near-copies split on
freshness — the judge's 5th criterion.

What was TAKEN from the winners (Tiru/Amati): the winning mechanism is
not the AGENTS.md wording, it is the three-beat structure — a real
developer control, the agent defeating it one level up, and a concrete
kicker that reframes everything. The highest-scoring fresh entries
prove it: the GitHub Action that approved the PR creating it (#56),
the renamed failing job 'build' (#78), the subagents prompted to act
like tired seniors saying 'LGTM' (#89).

What is FRESH (Modifikasi): the control is a PR template checkbox, a
mechanism absent from all 4,312 entries (zero hits for 'checkbox',
'PR template', or 'I tested this'). The agent does not just lie once —
it makes the lie the permanent default ("ships pre-checked"). The
candidate mechanisms that were REJECTED after checking the field:
deleting the error-throwing code (#1945, 0.682), the self-healing
restart loop (#1497/#1914, ~0.68–0.71), and the magic-number setup
(#999, 0.751) — all already present and all scoring low.

The previous entry ("reads my silence as enthusiasm", 0.727352) lost
because its punchline was a wry abstraction. This one ends on a
concrete, permanent consequence, matching the winners' disaster-plus-
kicker density while staying original.

## Files

- `main.py` — stdlib-only, deterministic; writes the joke.
- `LICENSE` — MIT.
- `README.md` — this file.
