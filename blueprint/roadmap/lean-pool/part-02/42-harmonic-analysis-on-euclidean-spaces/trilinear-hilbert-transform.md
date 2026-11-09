---
declaration: theorem
origin: cited
lean: TrilinearHT.trilinear_ht_bound
statement: formalized
proof: formalized
---

# Boundedness of the trilinear Hilbert transform

> Proves the L³ × L³ × L³ to L¹ bound for the principal-value trilinear Hilbert transform on Schwartz functions, together with its unique bounded extension to L³. Preserves the finite inverse theorem, quantitative quadratic charts, dyadic stopping and projection estimates used by the proof.

*Quoted from the card [LeanPool/projects/trilinear-hilbert-transform.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/trilinear-hilbert-transform.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`TrilinearHT.trilinear_ht_bound`](https://leanpool.github.io/lean-pool/LeanPool/TrilinearHilbertTransform/Theorems.html#TrilinearHT.trilinear_ht_bound) (theorem; a main declaration), declared in [LeanPool/TrilinearHilbertTransform/Theorems.lean, line 33](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/TrilinearHilbertTransform/Theorems.lean#L33): “There is an absolute real constant C such that the L¹ norm of the principal-value integral of f₁(x+t) f₂(x+2t) f₃(x+3t)/t is at most C times the product of the L³ norms, for all complex Schwartz functions.”
- [`TrilinearHT.Auto.tht_main`](https://leanpool.github.io/lean-pool/LeanPool/TrilinearHilbertTransform/Auto/Sec163SummingUpdateLevels/RetainedMinHolds.html#TrilinearHT.Auto.tht_main) (theorem), declared in [LeanPool/TrilinearHilbertTransform/Auto/Sec163SummingUpdateLevels/RetainedMinHolds.lean, line 2554](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/TrilinearHilbertTransform/Auto/Sec163SummingUpdateLevels/RetainedMinHolds.lean#L2554): “The truncations converge pointwise for Schwartz inputs, and the transform has a unique bounded complex trilinear extension from three copies of L³ to L¹, agreeing almost everywhere with the Schwartz transform.”

## Project

- Authors: Joris Roos.
- Source: *Formalization of boundedness of the trilinear Hilbert transform*, [manuscript](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-L3-bound-for-the-trilinear-Hilbert-transform-October-5-2026/paper.pdf).
- Project repository: [roos-j/lean-trilinearht](https://github.com/roos-j/lean-trilinearht), at commit [7b420960](https://github.com/roos-j/lean-trilinearht/tree/7b4209609e6a7fb9d9935973ee8541495f943660).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 42B20, 42B25.
- In Lean Pool: [LeanPool/TrilinearHilbertTransform](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/TrilinearHilbertTransform), from the card [LeanPool/projects/trilinear-hilbert-transform.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/trilinear-hilbert-transform.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/trilinear-hilbert-transform.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/trilinear-hilbert-transform.yaml)
- [Lean Pool at 2b205bf9: LeanPool/TrilinearHilbertTransform](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/TrilinearHilbertTransform)
