# Sequence growth

> Natural-division recurrence bounds and eventual exponential domination for sequences of natural numbers.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/sequence-growth/blob/ccf81c7190cb1da914c71efaa20689c0e1d7ab62/formalization.yaml) of [FormalFrontier/sequence-growth](https://github.com/FormalFrontier/sequence-growth) at commit [ccf81c71](https://github.com/FormalFrontier/sequence-growth/tree/ccf81c7190cb1da914c71efaa20689c0e1d7ab62), Apache-2.0.*

2 articles: 2 for headline results in its README whose declaration link names a declaration the scan finds in the linked file.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/sequence-growth](https://github.com/FormalFrontier/sequence-growth), read at commit [ccf81c71](https://github.com/FormalFrontier/sequence-growth/tree/ccf81c7190cb1da914c71efaa20689c0e1d7ab62) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “agent-reviewed”.
- Review notes: “The two listed recurrence theorems and their documented hypotheses have been independently agent-reviewed; no complete coverage of an external source is asserted.”
- Reviewers: “Formal Frontier Agents”.
- Automation: agent; framework “Codex CLI and Lean”; tool setup “Agent-assisted Lean formalization using Mathlib.”
- Automation notes: “Formal Frontier Agents developed the Lean proofs with AI assistance and reused Mathlib's arithmetic foundations.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Natural-division lower-recurrence growth bounds (original formalization)*, Formal Frontier Agents (original-proof; independently-proves).

## Builds on

No other Formal Frontier library.

## Used by

- [Norm forms](../../number-theory/norm-forms/README.md)

## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/sequence-growth/blob/ccf81c7190cb1da914c71efaa20689c0e1d7ab62/README.md#headline-results) of [FormalFrontier/sequence-growth](https://github.com/FormalFrontier/sequence-growth) at commit [ccf81c71](https://github.com/FormalFrontier/sequence-growth/tree/ccf81c7190cb1da914c71efaa20689c0e1d7ab62), Apache-2.0.*

- [`Nat.DivisionGrowth.affine_lower_bound`](nat-divisiongrowth-affine-lower-bound.md)
- [`Nat.DivisionGrowth.eventually_dominates`](nat-divisiongrowth-eventually-dominates.md)

The seed is sufficient, not necessary. See [the mathematical guide](https://github.com/FormalFrontier/sequence-growth/blob/ccf81c7190cb1da914c71efaa20689c0e1d7ab62/docs/DivisionGrowth.md)
for the precise Lean signatures, the rational shift, examples and boundary cases.

## Main results

Its formalization.yaml lists 2 main results, and the scan finds 2 of them declared in the file the yaml gives; they are on their own page, not made articles.

- [Main results](main-results/README.md)
