---
declaration: theorem
origin: cited
lean: dimH_image_le_sardMoreiraBound_of_finrank_le
statement: formalized
proof: formalized
---

# Moreira's version of Sard's theorem

> Formalizes Moreira's strengthening of Sard's theorem, bounding the Hausdorff dimension of critical-value images of C^{k+alpha} maps.

*Quoted from the card [LeanPool/projects/sardmoreira.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/sardmoreira.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`hausdorffMeasure_sardMoreiraBound_image_null_of_finrank_le`](https://leanpool.github.io/lean-pool/LeanPool/SardMoreira/MainTheorem.html#hausdorffMeasure_sardMoreiraBound_image_null_of_finrank_le) (theorem), declared in [LeanPool/SardMoreira/MainTheorem.lean, line 700](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SardMoreira/MainTheorem.lean#L700): “Proves Hausdorff-measure nullity for images of points where the derivative rank is bounded by p, at Moreira's Sard bound.” Its source, as the card gives it: “Moreira 2001, http://dmle.icmat.es/pdf/PUBLICACIONSMATEMATIQUES_2001_45_01_06.pdf”
- [`dimH_image_le_sardMoreiraBound_of_finrank_le`](https://leanpool.github.io/lean-pool/LeanPool/SardMoreira/MainTheorem.html#dimH_image_le_sardMoreiraBound_of_finrank_le) (theorem; a main declaration), declared in [LeanPool/SardMoreira/MainTheorem.lean, line 745](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SardMoreira/MainTheorem.lean#L745): “Converts the measure-null theorem into the headline Hausdorff-dimension upper bound for critical-value images.” Its source, as the card gives it: “Moreira 2001, http://dmle.icmat.es/pdf/PUBLICACIONSMATEMATIQUES_2001_45_01_06.pdf”

## Project

- Authors: Yury G. Kudryashov.
- Source: [doi:10.5565/PUBLMAT_45101_06](https://doi.org/10.5565/PUBLMAT_45101_06), [paper](http://dmle.icmat.es/pdf/PUBLICACIONSMATEMATIQUES_2001_45_01_06.pdf).
- Project repository: [urkud/SardMoreira](https://github.com/urkud/SardMoreira).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 28A78, 58C25.
- In Lean Pool: [LeanPool/SardMoreira](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SardMoreira), from the card [LeanPool/projects/sardmoreira.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/sardmoreira.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/sardmoreira.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/sardmoreira.yaml)
- [Lean Pool at 2b205bf9: LeanPool/SardMoreira](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SardMoreira)
