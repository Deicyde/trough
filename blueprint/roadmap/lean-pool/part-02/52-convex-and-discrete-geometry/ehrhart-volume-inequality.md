---
declaration: theorem
origin: cited
lean: Ehrhart.Volume.ehrhart_volume_inequality_for_sets
statement: formalized
proof: formalized
---

# Ehrhart's sharp volume inequality

> Proves Ehrhart's sharp upper bound for the volume of a centered full-dimensional convex body whose origin is its unique interior lattice point. The development builds the weighted complex-analytic and variational machinery needed for the bound and verifies sharpness using the centered simplex, including its barycenter and exact volume.

*Quoted from the card [LeanPool/projects/ehrhart-volume-inequality.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/ehrhart-volume-inequality.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`Ehrhart.Volume.ehrhart_volume_inequality_for_sets`](https://leanpool.github.io/lean-pool/LeanPool/EhrhartVolumeInequality/Convergence.html#Ehrhart.Volume.ehrhart_volume_inequality_for_sets) (theorem; a main declaration), declared in [LeanPool/EhrhartVolumeInequality/Convergence.lean, line 2148](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EhrhartVolumeInequality/Convergence.lean#L2148): “In every positive dimension, a compact full-dimensional convex set with barycenter zero and origin as its unique interior lattice point has volume at most (n + 1)^n / n!.”
- [`Ehrhart.SimplexVolume.normalizedVolume_centeredSimplex`](https://leanpool.github.io/lean-pool/LeanPool/EhrhartVolumeInequality/Foundations.html#Ehrhart.SimplexVolume.normalizedVolume_centeredSimplex) (theorem), declared in [LeanPool/EhrhartVolumeInequality/Foundations.lean, line 3579](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EhrhartVolumeInequality/Foundations.lean#L3579): “The centered dilation of the standard n-simplex has normalized volume exactly (n + 1)^n / n!, so the volume bound is sharp.”
- [`Ehrhart.SimplexVolume.barycenter_centeredSimplex`](https://leanpool.github.io/lean-pool/LeanPool/EhrhartVolumeInequality/Foundations.html#Ehrhart.SimplexVolume.barycenter_centeredSimplex) (theorem), declared in [LeanPool/EhrhartVolumeInequality/Foundations.lean, line 3756](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EhrhartVolumeInequality/Foundations.lean#L3756): “The centered dilation of the standard simplex has barycenter zero.”
- [`Ehrhart.SimplexVolume.exists_centeredBody_sharp`](https://leanpool.github.io/lean-pool/LeanPool/EhrhartVolumeInequality/Foundations.html#Ehrhart.SimplexVolume.exists_centeredBody_sharp) (theorem), declared in [LeanPool/EhrhartVolumeInequality/Foundations.lean, line 3773](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EhrhartVolumeInequality/Foundations.lean#L3773): “In every positive dimension there exists a centered convex body with a unique interior lattice point that attains the sharp volume bound.”

## Project

- Authors: OpenAI, Dean Cureton.
- Source: *Ten Advances in Mathematics and Theoretical Computer Science* by OpenAI.
- Project repository: [openai/ten-proofs](https://github.com/openai/ten-proofs), at commit [94bc0feb](https://github.com/openai/ten-proofs/tree/94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 52A40, 11H06.
- In Lean Pool: [LeanPool/EhrhartVolumeInequality](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EhrhartVolumeInequality), from the card [LeanPool/projects/ehrhart-volume-inequality.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/ehrhart-volume-inequality.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/ehrhart-volume-inequality.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/ehrhart-volume-inequality.yaml)
- [Lean Pool at 2b205bf9: LeanPool/EhrhartVolumeInequality](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EhrhartVolumeInequality)
