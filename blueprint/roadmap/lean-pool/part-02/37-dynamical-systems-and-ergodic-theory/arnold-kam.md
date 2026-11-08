---
declaration: theorem
origin: cited
lean: KamProject.Arnold1963.theorem1
statement: formalized
proof: formalized
---

# Analytic Hamiltonian KAM on compact action domains

> Proves a nondegenerate analytic Hamiltonian KAM theorem on compact complex action domains whose real slice is the closure of a nonempty open set with null boundary. A positive perturbation threshold, chosen independently of the perturbation, yields a pairwise disjoint family of analytic invariant tori covering all but a prescribed relative measure error. Includes Fourier estimates, generating transformations, resonance measure bounds, infinite iteration, global Hamiltonian trajectories, and examples with a noninjective frequency map. The final torus interface asserts nonresonance but does not additionally assert a quantitative Diophantine bound or the Lagrangian property.

*Quoted from the card [LeanPool/projects/arnold-kam.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/arnold-kam.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`KamProject.Arnold1963.theorem1`](https://leanpool.github.io/lean-pool/LeanPool/ArnoldKAM/Arnold1963/Main/Theorem1.html#KamProject.Arnold1963.theorem1) (theorem; a main declaration), declared in [LeanPool/ArnoldKAM/Arnold1963/Main/Theorem1.lean, line 117](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ArnoldKAM/Arnold1963/Main/Theorem1.lean#L117): “For a positive-dimensional analytic, real-compatible unperturbed Hamiltonian with nonzero Hessian determinant on the real interior of the specified compact domain, and any positive angle width and tolerance, a positive uniform perturbation threshold gives a compact positive-measure good set partitioned into pairwise disjoint analytic nonresonant invariant tori. The complementary bad set has measure less than the tolerance times the initial phase volume. Each torus has a closed embedding, an injective derivative, small displacement, and trajectories solving the original perturbed Hamiltonian equation for all real time. The analytic width is a positive output bounded by the input width.”
- [`KamProject.Arnold1963.theorem1_of_pointwise`](https://leanpool.github.io/lean-pool/LeanPool/ArnoldKAM/Arnold1963/Main/Theorem1.html#KamProject.Arnold1963.theorem1_of_pointwise) (theorem), declared in [LeanPool/ArnoldKAM/Arnold1963/Main/Theorem1.lean, line 125](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ArnoldKAM/Arnold1963/Main/Theorem1.lean#L125): “The same KAM conclusion holds when the perturbation is pointwise strictly below the chosen threshold throughout its prescribed phase domain.”
- [`KamProject.Arnold1963.AnalyticPhaseFunction.canonical_pullback`](https://leanpool.github.io/lean-pool/LeanPool/ArnoldKAM/Arnold1963/Basic/Hamiltonian.html#KamProject.Arnold1963.AnalyticPhaseFunction.canonical_pullback) (theorem), declared in [LeanPool/ArnoldKAM/Arnold1963/Basic/Hamiltonian.lean, line 176](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ArnoldKAM/Arnold1963/Basic/Hamiltonian.lean#L176): “A differentiable symplectic transformation mapping into the analytic Hamiltonian's phase domain carries the vector field of the pulled-back Hamiltonian to the original Hamiltonian vector field.”

## Project

- Authors: Bingqi Yu.
- Source: [doi:10.5281/zenodo.23232025](https://doi.org/10.5281/zenodo.23232025).
- Project repository: [ybq1415926-droid/arnold1963-kam](https://github.com/ybq1415926-droid/arnold1963-kam), at commit [69c10c07](https://github.com/ybq1415926-droid/arnold1963-kam/tree/69c10c07bcd0a65f8965bc58c37eea2700bafafb).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 37J40, 37J35, 42A16.
- In Lean Pool: [LeanPool/ArnoldKAM](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ArnoldKAM), from the card [LeanPool/projects/arnold-kam.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/arnold-kam.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/arnold-kam.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/arnold-kam.yaml)
- [Lean Pool at 2b205bf9: LeanPool/ArnoldKAM](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ArnoldKAM)
