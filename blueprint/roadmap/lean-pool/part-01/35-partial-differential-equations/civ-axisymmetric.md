---
declaration: theorem
origin: cited
lean: CIV.mainTheorem, CIV.axisymmetricTheorem
statement: formalized
proof: formalized
---

# Regularity of asymptotically axisymmetric Navier–Stokes solutions

> Proves the Constantin–Ignatova–Vicol regularity theorem for suitable weak solutions of the three-dimensional forced Navier–Stokes equations with analytic forcing, anisotropic Type II bounds on the angular mean, and an axisymmetric core at each time. Includes the fully axisymmetric theorem, meridional smallness, interior spatial analyticity, the nonanalyticity consequence for singular solutions, and the comparison, Serrin, and Gustafson–Kang–Tsai results used in their proofs. Reuses Lean Pool's Caffarelli–Kohn–Nirenberg suitable-solution and analysis library.

*Quoted from the card [LeanPool/projects/civ-axisymmetric.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/civ-axisymmetric.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`CIV.mainTheorem`](https://leanpool.github.io/lean-pool/LeanPool/CIVAxisymmetric/Statements/MainTheorem.html#CIV.mainTheorem) (theorem; a main declaration), declared in [LeanPool/CIVAxisymmetric/Statements/MainTheorem.lean, line 40](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CIVAxisymmetric/Statements/MainTheorem.lean#L40): “A smooth suitable weak solution on the unit parabolic cylinder with globally finite energy, bounded C^2 spatially analytic force, anisotropic Type II bounds on its angular mean, and a positive axisymmetric core at every time is axisymmetric throughout the cylinder and bounded near the origin up to the terminal time.”
- [`CIV.axisymmetricTheorem`](https://leanpool.github.io/lean-pool/LeanPool/CIVAxisymmetric/Statements/AxisymmetricTheorem.html#CIV.axisymmetricTheorem) (theorem; a main declaration), declared in [LeanPool/CIVAxisymmetric/Statements/AxisymmetricTheorem.lean, line 38](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CIVAxisymmetric/Statements/AxisymmetricTheorem.lean#L38): “An axisymmetric smooth suitable weak solution obeying the stated anisotropic Type II bounds and bounded C^2 force is bounded near the origin up to the terminal time.”
- [`CIV.meridionalSmallness`](https://leanpool.github.io/lean-pool/LeanPool/CIVAxisymmetric/Statements/MeridionalSmallnessProp.html#CIV.meridionalSmallness) (theorem), declared in [LeanPool/CIVAxisymmetric/Statements/MeridionalSmallnessProp.lean, line 37](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CIVAxisymmetric/Statements/MeridionalSmallnessProp.lean#L37): “Under the axisymmetric anisotropic hypotheses, the weighted meridional quantity tends uniformly to zero on a smaller cylinder as the terminal time approaches.”
- [`CIV.interiorAnalyticity`](https://leanpool.github.io/lean-pool/LeanPool/CIVAxisymmetric/Statements/InteriorAnalyticity.html#CIV.interiorAnalyticity) (theorem), declared in [LeanPool/CIVAxisymmetric/Statements/InteriorAnalyticity.lean, line 32](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CIVAxisymmetric/Statements/InteriorAnalyticity.lean#L32): “Smooth solutions with locally uniformly spatially analytic forcing are locally uniformly spatially analytic in the interior.”
- [`CIV.forceUnderCore`](https://leanpool.github.io/lean-pool/LeanPool/CIVAxisymmetric/Statements/ForceUnderCore.html#CIV.forceUnderCore) (theorem), declared in [LeanPool/CIVAxisymmetric/Statements/ForceUnderCore.lean, line 40](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CIVAxisymmetric/Statements/ForceUnderCore.lean#L40): “For a smooth suitable weak solution with globally finite energy, bounded C^2 forcing, angular-mean anisotropic bounds, and an axisymmetric core at every time, failure of boundedness near the origin implies that the force is not spatially analytic, is nonzero somewhere in the unit cylinder, and has a nonzero point in every smaller terminal cylinder.”

## Project

- Authors: Scott Armstrong, Vlad Vicol.
- Source: [arXiv:2609.20803](https://arxiv.org/abs/2609.20803).
- Project repository: [scottnarmstrong/CIVAxisymmetric](https://github.com/scottnarmstrong/CIVAxisymmetric), at commit [9f539dc7](https://github.com/scottnarmstrong/CIVAxisymmetric/tree/9f539dc7bf7ddd414d3ef81df539e1bef229f681).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 35Q30, 35B65, 35B33.
- In Lean Pool: [LeanPool/CIVAxisymmetric](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CIVAxisymmetric), from the card [LeanPool/projects/civ-axisymmetric.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/civ-axisymmetric.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/civ-axisymmetric.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/civ-axisymmetric.yaml)
- [Lean Pool at 2b205bf9: LeanPool/CIVAxisymmetric](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CIVAxisymmetric)
