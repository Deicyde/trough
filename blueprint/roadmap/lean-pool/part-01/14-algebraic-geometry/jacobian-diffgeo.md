---
declaration: theorem
origin: cited
lean: genus_eq_zero_iff_homeo, Jacobian.ofCurve_inj
statement: formalized
proof: formalized
---

# The Jacobian of a Compact Riemann Surface

> Constructs the Jacobian of a compact Riemann surface as the period-lattice quotient of the dual of holomorphic 1-forms, and proves the surrounding theory it needs: the genus as the dimension of the space of holomorphic 1-forms, discreteness and full rank 2g of the period lattice, the Abel-Jacobi map and its injectivity in positive genus, functoriality (pushforward, pullback, degree, and the projection formula), Riemann-Roch, Serre duality via Laurent tails, the residue theorem, the Dolbeault-Cech comparison, and finite dimensionality of the first cohomology by a Schwartz/Montel argument. The headline no-hack guard is that the genus vanishes exactly when the surface is homeomorphic to the sphere.

*Quoted from the card [LeanPool/projects/jacobian-diffgeo.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/jacobian-diffgeo.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`genus_eq_zero_iff_homeo`](https://leanpool.github.io/lean-pool/LeanPool/JacobianDiffgeo/GenusSphereHeadline/Basic.html#genus_eq_zero_iff_homeo) (theorem; a main declaration), declared in [LeanPool/JacobianDiffgeo/GenusSphereHeadline/Basic.lean, line 128](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/JacobianDiffgeo/GenusSphereHeadline/Basic.lean#L128): “A compact connected Riemann surface has genus zero if and only if it is homeomorphic to the 2-sphere.”
- [`Jacobian.ofCurve_inj`](https://leanpool.github.io/lean-pool/LeanPool/JacobianDiffgeo/CechCount/Final.html#Jacobian.ofCurve_inj) (theorem; a main declaration), declared in [LeanPool/JacobianDiffgeo/CechCount/Final.lean, line 120](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/JacobianDiffgeo/CechCount/Final.lean#L120): “The Abel-Jacobi map of a compact Riemann surface of positive genus is injective: two points with the same image coincide.”
- [`Jacobian.pushforward_pullback`](https://leanpool.github.io/lean-pool/LeanPool/JacobianDiffgeo/Challenge.html#Jacobian.pushforward_pullback) (lemma), declared in [LeanPool/JacobianDiffgeo/Challenge.lean, line 147](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/JacobianDiffgeo/Challenge.lean#L147): “For a non-constant holomorphic map between compact Riemann surfaces, the pushforward composed with the pullback on Jacobians is multiplication by the degree of the map.”

## Project

- Authors: Rado Kirov.
- Source: *Jacobians of compact Riemann surfaces (AI challenge)* by Kevin Buzzard, [https://gist.github.com/kbuzzard/778bc714030b3e974ab5f4038783d1a9](https://gist.github.com/kbuzzard/778bc714030b3e974ab5f4038783d1a9).
- Project repository: [rkirov/jacobian-fable](https://github.com/rkirov/jacobian-fable).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 14H40, 30F30, 32G20.
- In Lean Pool: [LeanPool/JacobianDiffgeo](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/JacobianDiffgeo), from the card [LeanPool/projects/jacobian-diffgeo.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/jacobian-diffgeo.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/jacobian-diffgeo.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/jacobian-diffgeo.yaml)
- [Lean Pool at 2b205bf9: LeanPool/JacobianDiffgeo](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/JacobianDiffgeo)
