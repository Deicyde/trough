---
declaration: theorem
origin: cited
lean: LeanPool.Besicovitch.sigmaOne_plane_le_barS
statement: formalized
proof: formalized
---

# A machine-checked bound of 0.6934 for Besicovitch's 1/2-problem

> Proves the planar Besicovitch threshold is at most 6934/10000, improving the published 7/10 record. The development formalizes the finite six-point reduction, thirty rational Gram certificates, the endpoint isolation argument, and Besicovitch's classical lower-bound example.

*Quoted from the card [LeanPool/projects/besicovitchs-1-2.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/besicovitchs-1-2.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`LeanPool.Besicovitch.sigmaOne_plane_le_barS`](https://leanpool.github.io/lean-pool/LeanPool/Besicovitch/Main/RationalBound.html#LeanPool.Besicovitch.sigmaOne_plane_le_barS) (theorem; a main declaration), declared in [LeanPool/Besicovitch/Main/RationalBound.lean, line 32](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Besicovitch/Main/RationalBound.lean#L32): “The planar one-dimensional rectifiability threshold is at most 6934/10000, improving the published upper bound 7/10.”
- [`LeanPool.Besicovitch.forcesOneRectifiability_plane_of_barS_lt`](https://leanpool.github.io/lean-pool/LeanPool/Besicovitch/Main/RationalBound.html#LeanPool.Besicovitch.forcesOneRectifiability_plane_of_barS_lt) (theorem), declared in [LeanPool/Besicovitch/Main/RationalBound.lean, line 26](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Besicovitch/Main/RationalBound.lean#L26): “Every threshold strictly above 6934/10000 forces countable one-rectifiability in the plane.”
- [`LeanPool.Besicovitch.Example.one_half_le_sigmaOne_plane`](https://leanpool.github.io/lean-pool/LeanPool/Besicovitch/Example/LowerBound.html#LeanPool.Besicovitch.Example.one_half_le_sigmaOne_plane) (theorem), declared in [LeanPool/Besicovitch/Example/LowerBound.lean, line 102](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Besicovitch/Example/LowerBound.lean#L102): “The planar threshold is at least one half, witnessed by Besicovitch's purely unrectifiable example.”
- [`LeanPool.Besicovitch.weightedPairScore_le_of_separated`](https://leanpool.github.io/lean-pool/LeanPool/Besicovitch/SixPoint/GramWeightedBound.html#LeanPool.Besicovitch.weightedPairScore_le_of_separated) (theorem), declared in [LeanPool/Besicovitch/SixPoint/GramWeightedBound.lean, line 33](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Besicovitch/SixPoint/GramWeightedBound.lean#L33): “Thirty exact rational Gram certificates prove the weighted six-point score is at most -1/2000 for every separated admissible pair in the unit ball.”

## Project

- Authors: Yongxi Lin.
- Source: *The bound sigma_1(R^2) <= 6934/10000 for Besicovitch's 1/2-problem* by Yongxi Lin.
- Project repository: [CoolRmal/Besicovitchs-1-2](https://github.com/CoolRmal/Besicovitchs-1-2), at commit [17c9597b](https://github.com/CoolRmal/Besicovitchs-1-2/tree/17c9597b2a901bf386d5bb8382d0a74d2069f25b).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 28A75, 28A78, 49Q15, 68V20, 90C05.
- In Lean Pool: [LeanPool/Besicovitch](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Besicovitch), from the card [LeanPool/projects/besicovitchs-1-2.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/besicovitchs-1-2.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/besicovitchs-1-2.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/besicovitchs-1-2.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Besicovitch](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Besicovitch)
