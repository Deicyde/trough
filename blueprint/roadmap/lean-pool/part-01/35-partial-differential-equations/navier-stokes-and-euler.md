---
declaration: theorem
origin: cited
lean: NavierStokes.Comparator.navier_stokes_breakdown_R3, Euler.euler_breakdown_R3
statement: formalized
proof: formalized
---

# Finite-time breakdown for Navier–Stokes and Euler

> Formalizes forced three-dimensional Navier–Stokes breakdown on Euclidean space and the periodic torus for every positive viscosity, and finite-time singularity formation for unforced Euler from smooth, compactly supported, divergence-free initial data. The Euler result specifies maximal Sobolev lifespan, divergence of the velocity C¹ norm, and divergence of the time integral of the vorticity norm.

*Quoted from the card [LeanPool/projects/navier-stokes-and-euler.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/navier-stokes-and-euler.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`NavierStokes.Comparator.navier_stokes_breakdown_R3`](https://leanpool.github.io/lean-pool/LeanPool/NavierStokesAndEuler/NavierStokes/ComparatorSolution.html#NavierStokes.Comparator.navier_stokes_breakdown_R3) (theorem; a main declaration), declared in [LeanPool/NavierStokesAndEuler/NavierStokes/ComparatorSolution.lean, line 28](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NavierStokesAndEuler/NavierStokes/ComparatorSolution.lean#L28): “For every positive viscosity, there are smooth divergence-free initial data and smooth forcing on ℝ³, with the prescribed spatial and temporal decay, admitting no global smooth Navier–Stokes solution with uniformly bounded kinetic energy.”
- [`NavierStokes.Comparator.navier_stokes_breakdown_periodic`](https://leanpool.github.io/lean-pool/LeanPool/NavierStokesAndEuler/NavierStokes/ComparatorSolution.html#NavierStokes.Comparator.navier_stokes_breakdown_periodic) (theorem), declared in [LeanPool/NavierStokesAndEuler/NavierStokes/ComparatorSolution.lean, line 35](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NavierStokesAndEuler/NavierStokes/ComparatorSolution.lean#L35): “For every positive viscosity, there are smooth periodic divergence-free initial data and smooth periodic forcing with the prescribed temporal decay, admitting no global smooth periodic Navier–Stokes solution.”
- [`Euler.euler_breakdown_R3`](https://leanpool.github.io/lean-pool/LeanPool/NavierStokesAndEuler/Euler/Solution.html#Euler.euler_breakdown_R3) (theorem; a main declaration), declared in [LeanPool/NavierStokesAndEuler/Euler/Solution.lean, line 82](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NavierStokesAndEuler/Euler/Solution.lean#L82): “There exist smooth divergence-free initial data on ℝ³ whose spatial derivatives decay faster than every polynomial and which admit no global smooth unforced Euler solution with uniformly bounded kinetic energy.”
- [`Euler.exists_compact_smooth_euler_singularity`](https://leanpool.github.io/lean-pool/LeanPool/NavierStokesAndEuler/Euler/Solution.html#Euler.exists_compact_smooth_euler_singularity) (theorem), declared in [LeanPool/NavierStokesAndEuler/Euler/Solution.lean, line 96](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NavierStokesAndEuler/Euler/Solution.lean#L96): “There exist nonzero smooth compactly supported divergence-free initial data, a maximal time 0 < Tstar ≤ 1, and an unforced Euler solution on [0, Tstar) in the all-order Sobolev class with bounded kinetic energy. Smooth Sobolev solutions on [0, T] exist exactly when T < Tstar. The velocity C¹ norm has infinite left limsup at Tstar, and the time integral of the spatial supremum of the vorticity norm diverges.”

## Project

- Authors: OpenAI.
- Source: *Finite time blowup for Navier–Stokes and Finite time blowup for the Euler equation* by OpenAI.
- Project repository: [openai/NavierStokesAndEuler](https://github.com/openai/NavierStokesAndEuler), at commit [8937a8f4](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 35Q30, 35Q31, 35B44.
- In Lean Pool: [LeanPool/NavierStokesAndEuler](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NavierStokesAndEuler), from the card [LeanPool/projects/navier-stokes-and-euler.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/navier-stokes-and-euler.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/navier-stokes-and-euler.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/navier-stokes-and-euler.yaml)
- [Lean Pool at 2b205bf9: LeanPool/NavierStokesAndEuler](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NavierStokesAndEuler)
