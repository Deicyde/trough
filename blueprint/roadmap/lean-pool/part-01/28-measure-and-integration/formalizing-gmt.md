---
declaration: theorem
origin: cited
lean: mattila_14_10, mattila_14_11
statement: formalized
proof: formalized
---

# Formalizing geometric measure theory

> A development of foundations and central results in geometric measure theory, including Hausdorff content and density bounds, weak convergence and compactness for Radon measures, tangent-measure machinery, Mattila's Lemmas 14.5--14.7, and Marstrand's integrality theorem for positive finite densities.

*Quoted from the card [LeanPool/projects/formalizing-gmt.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/formalizing-gmt.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`mattila_14_10`](https://leanpool.github.io/lean-pool/LeanPool/FormalizingGMT/MarstrandTheorem.html#mattila_14_10) (theorem; a main declaration), declared in [LeanPool/FormalizingGMT/MarstrandTheorem.lean, line 854](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FormalizingGMT/MarstrandTheorem.lean#L854): “If a Radon measure on Euclidean n-space has positive finite s-dimensional density on a set of positive measure, then s is a natural number.” Its source, as the card gives it: “Mattila, Theorem 14.10 (Marstrand's theorem).”
- [`mattila_14_11`](https://leanpool.github.io/lean-pool/LeanPool/FormalizingGMT/MarstrandTheorem.html#mattila_14_11) (theorem; a main declaration), declared in [LeanPool/FormalizingGMT/MarstrandTheorem.lean, line 879](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FormalizingGMT/MarstrandTheorem.lean#L879): “Every n-uniform measure on Euclidean n-space is a constant multiple of Lebesgue measure.” Its source, as the card gives it: “Mattila, Theorem 14.11.”
- [`MeasureTheory.Measure.weaklyConverges_iff_compactOpenBounds`](https://leanpool.github.io/lean-pool/LeanPool/FormalizingGMT/WeakConvergence/Basic.html#MeasureTheory.Measure.weaklyConverges_iff_compactOpenBounds) (theorem), declared in [LeanPool/FormalizingGMT/WeakConvergence/Basic.lean, line 306](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FormalizingGMT/WeakConvergence/Basic.lean#L306): “Vague convergence of Radon measures on Euclidean space is equivalent to the Portmanteau compact-set upper and open-set lower bounds.” Its source, as the card gives it: “Evans--Gariepy, revised edition, Theorem 1.40.”
- [`MeasureTheory.exists_vaguelyConvergent_subseq_of_compact_bounded`](https://leanpool.github.io/lean-pool/LeanPool/FormalizingGMT/WeakConvergence/CompactnessCriterion.html#MeasureTheory.exists_vaguelyConvergent_subseq_of_compact_bounded) (theorem), declared in [LeanPool/FormalizingGMT/WeakConvergence/CompactnessCriterion.lean, line 496](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FormalizingGMT/WeakConvergence/CompactnessCriterion.lean#L496): “A sequence of Radon measures on Euclidean space that is uniformly bounded on every compact set has a vaguely convergent subsequence.” Its source, as the card gives it: “Evans--Gariepy, revised edition, Theorem 1.41.”

## Project

- Authors: Theodore Meek, Ignacio Tejeda, Annie Cao, Nathan Pao.
- Project repository: [uw-math-ai/FormalizingGMT](https://github.com/uw-math-ai/FormalizingGMT), at commit [0acca38a](https://github.com/uw-math-ai/FormalizingGMT/tree/0acca38a91c4121b813f8e0b6ff719a4590bf126).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 28A75, 28A78, 49Q15.
- In Lean Pool: [LeanPool/FormalizingGMT](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FormalizingGMT), from the card [LeanPool/projects/formalizing-gmt.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/formalizing-gmt.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/formalizing-gmt.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/formalizing-gmt.yaml)
- [Lean Pool at 2b205bf9: LeanPool/FormalizingGMT](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FormalizingGMT)
