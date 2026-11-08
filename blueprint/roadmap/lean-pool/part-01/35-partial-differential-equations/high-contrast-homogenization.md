---
declaration: theorem
origin: cited
lean: HCPoly.polynomial_homogenization
statement: formalized
proof: formalized
---

# Homogenization at a polynomial scale in high contrast

> Formalizes polynomial entry into the small-contrast regime, algebraic convergence of coarse blocks, and quantitative stochastic homogenization with correctors, Liouville classification and large-scale regularity. Uses locally uniformly elliptic measurable coefficient fields modulo almost-everywhere equality. The Dirichlet estimate has the documented negative-Sobolev formulation on adapted cells; the random radius is at least one and the effective matrix is existentially produced. Includes the complete production library and its pinned CoarseGraining dependency closure in an isolated support namespace.

*Quoted from the card [LeanPool/projects/high-contrast-homogenization.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/high-contrast-homogenization.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`HCPoly.polynomial_entry`](https://leanpool.github.io/lean-pool/LeanPool/HighContrastHomogenization/MainResults.html#HCPoly.polynomial_entry) (theorem), declared in [LeanPool/HighContrastHomogenization/MainResults.lean, line 77](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HighContrastHomogenization/MainResults.lean#L77): “Under stationary unit-range assumptions and the source-tail bound, every generation beyond a scale of polynomial length has annealed contrast at most one plus the prescribed tolerance.”
- [`HCPoly.algebraic_convergence`](https://leanpool.github.io/lean-pool/LeanPool/HighContrastHomogenization/MainResults.html#HCPoly.algebraic_convergence) (theorem), declared in [LeanPool/HighContrastHomogenization/MainResults.lean, line 121](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HighContrastHomogenization/MainResults.lean#L121): “The annealed coarse blocks converge algebraically to a limiting positive-definite block, with two-sided order estimates.”
- [`HCPoly.uniform_homogenization`](https://leanpool.github.io/lean-pool/LeanPool/HighContrastHomogenization/MainResults.html#HCPoly.uniform_homogenization) (theorem), declared in [LeanPool/HighContrastHomogenization/MainResults.lean, line 183](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HighContrastHomogenization/MainResults.lean#L183): “Uniformly elliptic stationary unit-range laws satisfy the negative-Sobolev Dirichlet estimate, corrector estimates, Liouville classification and first-order approximation obtained by specializing the polynomial homogenization theorem.”
- [`HCPoly.polynomial_homogenization`](https://leanpool.github.io/lean-pool/LeanPool/HighContrastHomogenization/MainResults.html#HCPoly.polynomial_homogenization) (theorem; a main declaration), declared in [LeanPool/HighContrastHomogenization/MainResults.lean, line 359](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HighContrastHomogenization/MainResults.lean#L359): “High-contrast stationary unit-range laws admit an effective matrix and a random homogenization radius with polynomial length and quantitative tails, negative-Sobolev Dirichlet estimates on adapted cells, correctors, Liouville classification and large-scale regularity.”
- [`HCPoly.quenched_convergence`](https://leanpool.github.io/lean-pool/LeanPool/HighContrastHomogenization/MainResults.html#HCPoly.quenched_convergence) (theorem), declared in [LeanPool/HighContrastHomogenization/MainResults.lean, line 513](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HighContrastHomogenization/MainResults.lean#L513): “Coarse coefficients converge almost surely beyond a quantitative random scale, with the documented source-tail and stretched-exponential tail estimates.”

## Project

- Authors: Scott Armstrong, Tuomo Kuusi, Amélie Loher.
- Source: [arXiv:2609.27647](https://arxiv.org/abs/2609.27647), [https://github.com/scottnarmstrong/HighContrastHomogenization/tree/7a13dbcd8d6609264a713373f5c69ceeac870472](https://github.com/scottnarmstrong/HighContrastHomogenization/tree/7a13dbcd8d6609264a713373f5c69ceeac870472).
- Project repository: [scottnarmstrong/HighContrastHomogenization](https://github.com/scottnarmstrong/HighContrastHomogenization), at commit [7a13dbcd](https://github.com/scottnarmstrong/HighContrastHomogenization/tree/7a13dbcd8d6609264a713373f5c69ceeac870472).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 35B27, 35J15, 60K37.
- In Lean Pool: [LeanPool/HighContrastHomogenization](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HighContrastHomogenization), from the card [LeanPool/projects/high-contrast-homogenization.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/high-contrast-homogenization.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/high-contrast-homogenization.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/high-contrast-homogenization.yaml)
- [Lean Pool at 2b205bf9: LeanPool/HighContrastHomogenization](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HighContrastHomogenization)
