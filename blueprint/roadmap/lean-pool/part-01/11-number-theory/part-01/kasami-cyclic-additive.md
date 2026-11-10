---
declaration: theorem
origin: cited
lean: KasamiCyclicAdditive.carlet_kasami_cyclic_additive_literature
statement: formalized
proof: formalized
---

# Carlet's Kasami cyclic-additive conjecture

> Proves Carlet's cyclic-additive conjecture for the Kasami power function: over every finite field of characteristic two with cardinality 2^n and every k coprime to n, the normalized derivative image has the exact coefficient triple count 2^(2n-3) for all distinct nonzero slopes. The development combines the Müller--Cohen--Matthews permutation theorem, multiplicative character sums, Fourier inversion, and a Fermat-cubic Frobenius-kernel argument.

*Quoted from the card [LeanPool/projects/kasami-cyclic-additive.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/kasami-cyclic-additive.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`KasamiCyclicAdditive.carlet_kasami_cyclic_additive_literature`](https://leanpool.github.io/lean-pool/LeanPool/KasamiCyclicAdditive/Main.html#KasamiCyclicAdditive.carlet_kasami_cyclic_additive_literature) (theorem; a main declaration), declared in [LeanPool/KasamiCyclicAdditive/Main.lean, line 53](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/KasamiCyclicAdditive/Main.lean#L53): “For every finite field K of characteristic two with |K| = 2^n, every k coprime to n, and all distinct nonzero v₁ and v₂ in K, the coefficient triple count of the normalized Kasami derivative image is exactly 2^(2n-3).”
- [`KasamiCyclicAdditive.carlet_kasami_cyclic_additive_core`](https://leanpool.github.io/lean-pool/LeanPool/KasamiCyclicAdditive/Main.html#KasamiCyclicAdditive.carlet_kasami_cyclic_additive_core) (theorem), declared in [LeanPool/KasamiCyclicAdditive/Main.lean, line 39](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/KasamiCyclicAdditive/Main.lean#L39): “In the normalized range 1 ≤ k < n, the same coefficient triple count is 2^(2n-3), assuming characteristic two, |K| = 2^n, coprimality, and distinct nonzero coefficients.”
- [`KasamiCyclicAdditive.kasami_half_size`](https://leanpool.github.io/lean-pool/LeanPool/KasamiCyclicAdditive/MCM/HalfSize.html#KasamiCyclicAdditive.kasami_half_size) (theorem), declared in [LeanPool/KasamiCyclicAdditive/MCM/HalfSize.lean, line 71](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/KasamiCyclicAdditive/MCM/HalfSize.lean#L71): “Under the normalized admissibility hypotheses, the image of the Kasami derivative has exactly half as many elements as the field.”

## Project

- Authors: D.S. McNeil, Gábor P. Nagy, Attila Vajda.
- Source: *On a conjecture on the Kasami APN function* by Gábor P. Nagy, Attila Vajda, [arXiv:2608.18584](https://arxiv.org/abs/2608.18584).
- Project repository: [dsm054/kasami_cyclic_additive](https://github.com/dsm054/kasami_cyclic_additive), at commit [c8ab49eb](https://github.com/dsm054/kasami_cyclic_additive/tree/c8ab49ebd8e9e53f5aa7585f1d43acf1ff68d10f).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11T06, 11T71, 94A60.
- In Lean Pool: [LeanPool/KasamiCyclicAdditive](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/KasamiCyclicAdditive), from the card [LeanPool/projects/kasami-cyclic-additive.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/kasami-cyclic-additive.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/kasami-cyclic-additive.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/kasami-cyclic-additive.yaml)
- [Lean Pool at 2b205bf9: LeanPool/KasamiCyclicAdditive](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/KasamiCyclicAdditive)
