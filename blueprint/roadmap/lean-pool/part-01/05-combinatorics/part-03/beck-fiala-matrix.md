---
declaration: theorem
origin: cited
lean: BeckFialaMatrix.exists_rounding
statement: formalized
proof: formalized
---

# Strict Beck–Fiala rounding for incidence matrices

> Proves the rational integer-making form of Beck–Fiala rounding for finite zero-one incidence matrices with column degree bounded by a positive t. Every row has discrepancy strictly less than t, and initially integral coordinates are preserved. Includes the necessity of the positive-bound hypothesis. This is distinct from the Komlós discrepancy bound and from the non-strict hyperedge-selection rounding used in triangle packing.

*Quoted from the card [LeanPool/projects/beck-fiala-matrix.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/beck-fiala-matrix.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`BeckFialaMatrix.exists_rounding`](https://leanpool.github.io/lean-pool/LeanPool/BeckFialaMatrix/Basic.html#BeckFialaMatrix.exists_rounding) (theorem; a main declaration), declared in [LeanPool/BeckFialaMatrix/Basic.lean, line 380](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BeckFialaMatrix/Basic.lean#L380): “Given a finite zero-one integer matrix with at most t ones per column, t at least one, and a rational vector in the unit cube, there is a zero-one integer vector whose discrepancy in every row is strictly less than t.” Its source, as the card gives it: “Rational unit-cube integer-making form with the stated strict discrepancy bound.”
- [`BeckFialaMatrix.exists_rounding_preserving_integral`](https://leanpool.github.io/lean-pool/LeanPool/BeckFialaMatrix/Basic.html#BeckFialaMatrix.exists_rounding_preserving_integral) (theorem), declared in [LeanPool/BeckFialaMatrix/Basic.lean, line 364](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BeckFialaMatrix/Basic.lean#L364): “The strict rounding can additionally be chosen to leave every initially integral coordinate unchanged.” Its source, as the card gives it: “Strengthened conclusion of the floating-coordinate proof in the pinned source.”
- [`BeckFialaMatrix.zero_bound_counterexample`](https://leanpool.github.io/lean-pool/LeanPool/BeckFialaMatrix/Basic.html#BeckFialaMatrix.zero_bound_counterexample) (theorem), declared in [LeanPool/BeckFialaMatrix/Basic.lean, line 392](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BeckFialaMatrix/Basic.lean#L392): “The same universally quantified strict rounding claim without the assumption t at least one is false, already for a one-by-one zero matrix with t equal to zero.” Its source, as the card gives it: “Boundary-condition witness in the pinned formalization.”

## Project

- Authors: Juan Pablo Traverso Gianini.
- Source: *"Integer-making" theorems* by József Beck, Tibor Fiala, [doi:10.1016/0166-218X(81)90022-6](https://doi.org/10.1016/0166-218X%2881%2990022-6), [https://github.com/jtraverso/lean-pool/blob/523a4ae71168258f9142d70bccf650a140355650/LeanPool/BeckFialaMatrix/Basic.lean](https://github.com/jtraverso/lean-pool/blob/523a4ae71168258f9142d70bccf650a140355650/LeanPool/BeckFialaMatrix/Basic.lean).
- Project repository: [jtraverso/lean-pool](https://github.com/jtraverso/lean-pool), at commit [523a4ae7](https://github.com/jtraverso/lean-pool/tree/523a4ae71168258f9142d70bccf650a140355650).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05D40.
- In Lean Pool: [LeanPool/BeckFialaMatrix](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BeckFialaMatrix), from the card [LeanPool/projects/beck-fiala-matrix.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/beck-fiala-matrix.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/beck-fiala-matrix.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/beck-fiala-matrix.yaml)
- [Lean Pool at 2b205bf9: LeanPool/BeckFialaMatrix](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BeckFialaMatrix)
