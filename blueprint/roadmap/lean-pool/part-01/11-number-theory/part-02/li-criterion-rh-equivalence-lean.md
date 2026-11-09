---
declaration: theorem
origin: cited
lean: li_criterion, li_coefficients_eq_zero_sum
statement: formalized
proof: formalized
---

# Li's criterion for the Riemann Hypothesis

> Li's criterion for the Riemann zeta function, formalized in Lean 4 over Mathlib: Mathlib's `RiemannHypothesis` holds if and only if every Li-Keiper coefficient of the completed xi function has nonnegative real part. The zero-indexed analytic coefficient at n is Li's classical lambda\_(n+1), the n-th Taylor coefficient at 0 of the logarithmic derivative of s |-> xi(1/(1-s)). A second compared theorem identifies this analytic coefficient with Li's arithmetic coefficient, the symmetrized sum over the nontrivial zeros counted with multiplicity, and proves that symmetrized family summable so the sum is the genuine one. Both results are unconditional: the biconditional, the coefficient identification, the genus-1 Hadamard factorization of xi (with multiplicity), genus-1 summability of 1/|rho|^2, and the growth bound order(xi) <= 1 are all proved. This is a formalization of a classically known equivalence (X.-J. Li, 1997); it is not a proof of the Riemann Hypothesis, nor of the positivity of the coefficients.

*Quoted from the card [LeanPool/projects/li-criterion-rh-equivalence-lean.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/li-criterion-rh-equivalence-lean.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`li_criterion`](https://leanpool.github.io/lean-pool/LeanPool/LiCriterion/Comparator/Solution.html#li_criterion) (theorem; a main declaration), declared in [LeanPool/LiCriterion/Comparator/Solution.lean, line 52](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LiCriterion/Comparator/Solution.lean#L52): “The Riemann hypothesis is equivalent to nonnegativity of every Li–Keiper coefficient.”
- [`li_coefficients_eq_zero_sum`](https://leanpool.github.io/lean-pool/LeanPool/LiCriterion/Comparator/Solution.html#li_coefficients_eq_zero_sum) (theorem; a main declaration), declared in [LeanPool/LiCriterion/Comparator/Solution.lean, line 58](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LiCriterion/Comparator/Solution.lean#L58): “The analytic Li–Keiper coefficients equal the symmetrically summed arithmetic coefficients over the nontrivial zeros.”

## Project

- Authors: Nicholas Bulka.
- Project repository: [nicholasbulka/li-criterion-rh-equivalence-lean](https://github.com/nicholasbulka/li-criterion-rh-equivalence-lean), at commit [35df682f](https://github.com/nicholasbulka/li-criterion-rh-equivalence-lean/tree/35df682f3b709ffe5fbcfdd452dfa964bd622b87).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11M26.
- In Lean Pool: [LeanPool/LiCriterion](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LiCriterion), from the card [LeanPool/projects/li-criterion-rh-equivalence-lean.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/li-criterion-rh-equivalence-lean.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/li-criterion-rh-equivalence-lean.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/li-criterion-rh-equivalence-lean.yaml)
- [Lean Pool at 2b205bf9: LeanPool/LiCriterion](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LiCriterion)
