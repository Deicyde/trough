# Sequence growth

> Natural-division recurrence bounds and eventual exponential domination for sequences of natural numbers.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/sequence-growth/blob/ccf81c7190cb1da914c71efaa20689c0e1d7ab62/formalization.yaml) of [FormalFrontier/sequence-growth](https://github.com/FormalFrontier/sequence-growth) at commit [ccf81c71](https://github.com/FormalFrontier/sequence-growth/tree/ccf81c7190cb1da914c71efaa20689c0e1d7ab62), Apache-2.0.*

2 articles, for headline results in its README whose declaration link names a declaration the linked file declares.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/sequence-growth](https://github.com/FormalFrontier/sequence-growth), read at commit [ccf81c71](https://github.com/FormalFrontier/sequence-growth/tree/ccf81c7190cb1da914c71efaa20689c0e1d7ab62) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “agent-reviewed”
- Review notes: “The two listed recurrence theorems and their documented hypotheses have been independently agent-reviewed; no complete coverage of an external source is asserted.”
- Automation: agent; framework “Codex CLI and Lean”; tool setup “Agent-assisted Lean formalization using Mathlib.”
- Automation notes: “Formal Frontier Agents developed the Lean proofs with AI assistance and reused Mathlib's arithmetic foundations.”

## Scope

Two public natural-division growth theorems, plus ordinary-import client examples and boundary tests.

*Quoted from the status in [formalization.yaml](https://github.com/FormalFrontier/sequence-growth/blob/ccf81c7190cb1da914c71efaa20689c0e1d7ab62/formalization.yaml) of [FormalFrontier/sequence-growth](https://github.com/FormalFrontier/sequence-growth) at commit [ccf81c71](https://github.com/FormalFrontier/sequence-growth/tree/ccf81c7190cb1da914c71efaa20689c0e1d7ab62), Apache-2.0.*

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Natural-division lower-recurrence growth bounds (original formalization)*, Formal Frontier Agents (original-proof; independently-proves).

## Builds on

No other Formal Frontier library.

## Used by

- [Norm forms](../../number-theory/norm-forms/README.md)

## Headline results

- [`Nat.DivisionGrowth.affine_lower_bound`](nat-divisiongrowth-affine-lower-bound.md)
- [`Nat.DivisionGrowth.eventually_dominates`](nat-divisiongrowth-eventually-dominates.md)

The seed is sufficient, not necessary. See [the mathematical guide](https://github.com/FormalFrontier/sequence-growth/blob/ccf81c7190cb1da914c71efaa20689c0e1d7ab62/docs/DivisionGrowth.md)
for the precise Lean signatures, the rational shift, examples and boundary cases.

## Main results

The 2 main results its formalization.yaml lists (`status.main_results`). They are listed here, not made articles: in several Formal Frontier libraries this list is close to the whole API.

| Declaration | Kind | Where | Note |
| --- | --- | --- | --- |
| `Nat.DivisionGrowth.affine_lower_bound` | theorem | [SequenceGrowth/Data/Nat/DivisionGrowth.lean, line 71](https://github.com/FormalFrontier/sequence-growth/blob/ccf81c7190cb1da914c71efaa20689c0e1d7ab62/SequenceGrowth/Data/Nat/DivisionGrowth.lean#L71) | Sorry count 0. |
| `Nat.DivisionGrowth.eventually_dominates` | theorem | [SequenceGrowth/Data/Nat/DivisionGrowth.lean, line 99](https://github.com/FormalFrontier/sequence-growth/blob/ccf81c7190cb1da914c71efaa20689c0e1d7ab62/SequenceGrowth/Data/Nat/DivisionGrowth.lean#L99) | Sorry count 0. |
