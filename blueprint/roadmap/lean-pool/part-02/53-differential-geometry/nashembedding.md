---
declaration: theorem
origin: cited
lean: NashEmbeddingTheorem.nash_isometric_embedding
statement: formalized
proof: formalized
---

# Nash's smooth isometric embedding theorem

> A Lean 4 / Mathlib formalization of Nash's C^∞ isometric embedding theorem for closed manifolds: every compact smooth manifold without boundary, equipped with a smooth Riemannian metric, admits a smooth injective map into some Euclidean space ℝ^q whose differential pulls the Euclidean inner product back to the given metric. The proof formalized is Günther's (1989), which replaces the Nash-Moser iteration by an elliptic fixed-point argument, following the presentation in A. J. Wassermann's Cambridge Part III lecture notes as the primary source. The development has two layers. The first proves the theorem for the flat torus: a self-contained Sobolev toolkit on 𝕋ⁿ (weighted ℓ² Sobolev spaces on ℤⁿ, Rellich compactness, the Sobolev sup bound, three multiplication theorems, mollifiers, periodization, Fourier inversion and Parseval), the approximation of smooth metrics by realizable ones, Günther's perturbation theorem proved by a contraction in Hˢ, and their assembly into the statement that every smooth 2π-periodic positive-definite matrix field on ℝⁿ is the pullback metric of a smooth periodic immersion that is injective modulo 2πℤⁿ. The second layer reduces the closed-manifold case to the torus: a Whitney embedding from Mathlib is extended to the ambient space, the metric is extended by a pseudo-inverse construction, cut off, symmetrized and periodized, and the torus theorem is applied. No bound on the embedding dimension is claimed. Concrete instances (round spheres of every dimension, products of spheres, the flat torus 𝕊¹ × 𝕊¹) are derived, and the flat-torus instance is shown to reproduce the torus theorem's conclusion, tying the two layers together. Nothing here is claimed to be new.

*Quoted from the card [LeanPool/projects/nashembedding.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/nashembedding.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists one main result, with its informal statement quoted from the card. The scan finds its declaration in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`NashEmbeddingTheorem.nash_isometric_embedding`](https://leanpool.github.io/lean-pool/LeanPool/NashEmbedding/Solution.html#NashEmbeddingTheorem.nash_isometric_embedding) (theorem; a main declaration), declared in [LeanPool/NashEmbedding/Solution.lean, line 38](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NashEmbedding/Solution.lean#L38): “Every compact smooth boundaryless manifold with a smooth Riemannian metric admits a smooth isometric embedding in some finite-dimensional Euclidean space.”

## Project

- Authors: David Wiygul.
- Project repository: [langlerangle/nashembedding](https://github.com/langlerangle/nashembedding), at commit [515a8245](https://github.com/langlerangle/nashembedding/tree/515a8245c51c952db59d81ef840a146ed853e4ea).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 53C24.
- In Lean Pool: [LeanPool/NashEmbedding](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NashEmbedding), from the card [LeanPool/projects/nashembedding.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/nashembedding.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/nashembedding.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/nashembedding.yaml)
- [Lean Pool at 2b205bf9: LeanPool/NashEmbedding](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NashEmbedding)
