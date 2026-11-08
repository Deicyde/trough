---
declaration: theorem
origin: cited
lean: LeanPool.PoincareThreeBody.nonintegrability_of_collisionBand
statement: formalized
proof: formalized
---

# Poincaré's Nonintegrability Theorem for the Restricted Three-Body Problem

> Formalizes Poincaré's classical parameter-analytic nonintegrability theorem for the planar circular restricted three-body problem. The development defines the rotating-frame Hamiltonian on its collision-free domain, proves logarithmic blow-up of the resonant disturbing average at an apoapsis collision boundary, and analytically propagates the resulting dense resonant obstruction to exclude an additional analytic first integral. The final statement is the fixed-coordinate, global uniform-domain special case of the planar part of Yagasaki's Theorem 1.1; his local meromorphic resonant-orbit obstruction is Theorem 3.1.

*Quoted from the card [LeanPool/projects/poincare-three-body-nonintegrability.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/poincare-three-body-nonintegrability.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`LeanPool.PoincareThreeBody.nonintegrability_of_collisionBand`](https://leanpool.github.io/lean-pool/LeanPool/PoincareThreeBody/LocalEnergyLeaf.html#LeanPool.PoincareThreeBody.nonintegrability_of_collisionBand) (theorem; a main declaration), declared in [LeanPool/PoincareThreeBody/LocalEnergyLeaf.lean, line 414](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PoincareThreeBody/LocalEnergyLeaf.lean#L414): “No jointly real-analytic family near zero mass can be an additional first integral of the planar circular restricted three-body Hamiltonian with phase differential independent from the Hamiltonian differential anywhere on the uniform collision-free domain.” Its source, as the card gives it: “Kazuyuki Yagasaki, "A new proof of Poincaré's result on the restricted three-body problem," Theorem 1.1 (p. 2), planar case; compare the precise local meromorphic obstruction near resonant unperturbed elliptic orbits in Theorem 3.1 (p. 8). The Lean result is the fixed-coordinate global uniform-domain special case: a global real-analytic family restricts and complexifies on the local neighborhoods used in the source theorem.”
- [`LeanPool.PoincareThreeBody.delaunayHomological_obstruction`](https://leanpool.github.io/lean-pool/LeanPool/PoincareThreeBody/Delaunay.html#LeanPool.PoincareThreeBody.delaunayHomological_obstruction) (theorem), declared in [LeanPool/PoincareThreeBody/Delaunay.lean, line 249](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PoincareThreeBody/Delaunay.lean#L249): “If the first homological equation holds and its perturbing Fourier coefficient is nonzero at every positive rational Kepler resonance, then the leading differential of a putative analytic first integral is nowhere independent of the unperturbed Hamiltonian frequency.”
- [`LeanPool.PoincareThreeBody.delaunayDenseResonance_obstruction`](https://leanpool.github.io/lean-pool/LeanPool/PoincareThreeBody/Delaunay.html#LeanPool.PoincareThreeBody.delaunayDenseResonance_obstruction) (theorem), declared in [LeanPool/PoincareThreeBody/Delaunay.lean, line 230](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PoincareThreeBody/Delaunay.lean#L230): “For the rotating Kepler frequency in Delaunay actions, orthogonality of a continuous candidate differential to every positive rational resonance vector forces dependence with the Hamiltonian frequency at every positive action.”
- [`LeanPool.PoincareThreeBody.homologicalEquation_obstruction`](https://leanpool.github.io/lean-pool/LeanPool/PoincareThreeBody/Resonance.html#LeanPool.PoincareThreeBody.homologicalEquation_obstruction) (theorem), declared in [LeanPool/PoincareThreeBody/Resonance.lean, line 85](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PoincareThreeBody/Resonance.lean#L85): “At a resonant action in two degrees of freedom, a nonzero perturbing Fourier mode and the first homological equation force the unperturbed frequency and the differential of a putative leading first-integral coefficient to be linearly dependent.”
- [`LeanPool.PoincareThreeBody.denseResonance_obstruction`](https://leanpool.github.io/lean-pool/LeanPool/PoincareThreeBody/Resonance.html#LeanPool.PoincareThreeBody.denseResonance_obstruction) (theorem), declared in [LeanPool/PoincareThreeBody/Resonance.lean, line 110](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PoincareThreeBody/Resonance.lean#L110): “If the resonant obstruction holds on a dense set of actions and the frequency and differential vary continuously, then they are linearly dependent at every action.”

## Project

- Authors: Gershon Bialer.
- Source: *A new proof of Poincaré's result on the restricted three-body problem* by Kazuyuki Yagasaki, [doi:10.1063/5.0266087](https://doi.org/10.1063/5.0266087), [arXiv:2111.11031](https://arxiv.org/abs/2111.11031), [https://arxiv.org/abs/2111.11031](https://arxiv.org/abs/2111.11031).
- Project repository: [gersh/lean-pool](https://github.com/gersh/lean-pool).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 70F07, 37J30, 37J40.
- In Lean Pool: [LeanPool/PoincareThreeBody](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PoincareThreeBody), from the card [LeanPool/projects/poincare-three-body-nonintegrability.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/poincare-three-body-nonintegrability.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/poincare-three-body-nonintegrability.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/poincare-three-body-nonintegrability.yaml)
- [Lean Pool at 2b205bf9: LeanPool/PoincareThreeBody](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PoincareThreeBody)
