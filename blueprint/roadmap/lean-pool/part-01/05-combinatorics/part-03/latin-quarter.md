---
declaration: theorem
origin: cited
lean: LatinQuarter.Textbook.completions_even, LatinQuarter.Textbook.scs_eq_quarter
statement: formalized
proof: formalized
---

# The smallest critical set in a Latin square

> Proves that every partial Latin square of order n with fewer than floor(n²/4) filled cells has an even number of completions. Consequently every defining set has at least floor(n²/4) entries, and the two corner triangles in the cyclic square attain this bound as a critical set. Includes general results on matrix minors, square-zero ideals, and square-free polynomial coefficients.

*Quoted from the card [LeanPool/projects/latin-quarter.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/latin-quarter.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LatinQuarter.Textbook.completions_even`](https://leanpool.github.io/lean-pool/LeanPool/LatinQuarter/Textbook.html#LatinQuarter.Textbook.completions_even) (theorem; a main declaration), declared in [LeanPool/LatinQuarter/Textbook.lean, line 127](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LatinQuarter/Textbook.lean#L127): “Every set of fewer than floor(n²/4) filled triples of an order-n partial Latin square has an even number of labelled Latin-square completions.”
- [`LatinQuarter.Textbook.scs_eq_quarter`](https://leanpool.github.io/lean-pool/LeanPool/LatinQuarter/Textbook.html#LatinQuarter.Textbook.scs_eq_quarter) (theorem; a main declaration), declared in [LeanPool/LatinQuarter/Textbook.lean, line 245](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LatinQuarter/Textbook.lean#L245): “For every positive n, the smallest critical-set size among all Latin squares of order n, and the smallest critical-set size in the cyclic Latin square, both equal floor(n²/4).”
- [`LatinQuarter.defining_set_lower_bound`](https://leanpool.github.io/lean-pool/LeanPool/LatinQuarter/LowerBound.html#LatinQuarter.defining_set_lower_bound) (theorem), declared in [LeanPool/LatinQuarter/LowerBound.lean, line 51](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LatinQuarter/LowerBound.lean#L51): “Every defining set in every labelled Latin square of order n has at least floor(n²/4) cells.”
- [`LatinQuarter.cornerSet_isCritical`](https://leanpool.github.io/lean-pool/LeanPool/LatinQuarter/Main.html#LatinQuarter.cornerSet_isCritical) (theorem), declared in [LeanPool/LatinQuarter/Main.lean, line 37](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LatinQuarter/Main.lean#L37): “For every positive n, the two opposite corner triangles form a critical set in the cyclic Latin square.”

## Project

- Authors: Richard Bean.
- Source: [arXiv:2610.18199](https://arxiv.org/abs/2610.18199).
- Project repository: [RichardBean/latin-quarter-lean](https://github.com/RichardBean/latin-quarter-lean), at commit [9997439d](https://github.com/RichardBean/latin-quarter-lean/tree/9997439dee62e1ede0aa995ddb7160dbceeff7b7).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05B15.
- In Lean Pool: [LeanPool/LatinQuarter](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LatinQuarter), from the card [LeanPool/projects/latin-quarter.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/latin-quarter.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/latin-quarter.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/latin-quarter.yaml)
- [Lean Pool at 2b205bf9: LeanPool/LatinQuarter](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LatinQuarter)
