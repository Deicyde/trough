---
declaration: theorem
origin: cited
lean: HadwigerNelsonBounds.hadwiger_nelson_known_bounds
statement: formalized
proof: formalized
---

# Known Bounds for the Hadwiger-Nelson Problem

> Formalizes the currently known bounds 5 <= chi(R^2) <= 7 for the chromatic number of the Euclidean plane. The upper bound constructs an explicit Isbell-style seven-coloring. The lower bound checks Parts' 481-vertex coloring certificate, develops a finite doubled triangular-lattice forcing gadget, proves its exact Euclidean embedding, and closes the four-color contradiction with a spindle construction. The exact chromatic number remains open.

*Quoted from the card [LeanPool/projects/hadwiger-nelson-bounds.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/hadwiger-nelson-bounds.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`HadwigerNelsonBounds.hadwiger_nelson_known_bounds`](https://leanpool.github.io/lean-pool/LeanPool/HadwigerNelsonBounds/PartsSpindle.html#HadwigerNelsonBounds.hadwiger_nelson_known_bounds) (theorem; a main declaration), declared in [LeanPool/HadwigerNelsonBounds/PartsSpindle.lean, line 122](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HadwigerNelsonBounds/PartsSpindle.lean#L122): “The chromatic number of the unit-distance graph on the Euclidean plane lies between five and seven, inclusive.”
- [`HadwigerNelsonBounds.unitDistanceGraph_not_colorable_four`](https://leanpool.github.io/lean-pool/LeanPool/HadwigerNelsonBounds/PartsSpindle.html#HadwigerNelsonBounds.unitDistanceGraph_not_colorable_four) (theorem), declared in [LeanPool/HadwigerNelsonBounds/PartsSpindle.lean, line 85](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HadwigerNelsonBounds/PartsSpindle.lean#L85): “The unit-distance graph on the Euclidean plane admits no proper coloring with four colors.”
- [`HadwigerNelsonBounds.chromaticNumber_le_seven`](https://leanpool.github.io/lean-pool/LeanPool/HadwigerNelsonBounds/IsbellColoring.html#HadwigerNelsonBounds.chromaticNumber_le_seven) (theorem), declared in [LeanPool/HadwigerNelsonBounds/IsbellColoring.lean, line 204](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HadwigerNelsonBounds/IsbellColoring.lean#L204): “An explicit Isbell-style coloring proves that the unit-distance graph on the Euclidean plane is colorable with seven colors.”

## Project

- Authors: Egor Lyfar.
- Source: *A human-verifiable proof of the chromatic number of the plane being at least 5* by Jaan Parts, [arXiv:2010.12661](https://arxiv.org/abs/2010.12661), [https://www.erdosproblems.com/508](https://www.erdosproblems.com/508).
- Project repository: [lyfar/hadwiger-nelson-bounds-lean](https://github.com/lyfar/hadwiger-nelson-bounds-lean).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C15, 52C10.
- In Lean Pool: [LeanPool/HadwigerNelsonBounds](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HadwigerNelsonBounds), from the card [LeanPool/projects/hadwiger-nelson-bounds.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/hadwiger-nelson-bounds.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/hadwiger-nelson-bounds.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/hadwiger-nelson-bounds.yaml)
- [Lean Pool at 2b205bf9: LeanPool/HadwigerNelsonBounds](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HadwigerNelsonBounds)
