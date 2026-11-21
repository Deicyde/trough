---
declaration: theorem
origin: cited
lean: Triangular.triangular_ht_bound, Triangular.Auto.tendsto_truncatedForm, Triangular.Auto.triangularHilbert_unique_extension
statement: formalized
proof: formalized
---

# The symmetric triangular Hilbert form

> Proves the symmetric L³ estimate and principal-value existence for the triangular Hilbert form on complex Schwartz inputs, and its unique bounded trilinear extension to L³. The proof develops matrix trace estimates, Gaussian scale kernels, heat-flow identities and the passage from finite lattice sums to the Euclidean estimate. As an application it reduces continuous periodic Fourier convergence to the triangular estimate through localized modulated kernel estimates. Lean Pool's CarlesonLT project proves the convergence theorem for periodic functions that are square-integrable on a period.

*Quoted from the card [LeanPool/projects/triangular-hilbert.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/triangular-hilbert.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Triangular.triangular_ht_bound`](https://leanpool.github.io/lean-pool/LeanPool/Triangular/Theorems.html#Triangular.triangular_ht_bound) (theorem; a main declaration), declared in [LeanPool/Triangular/Theorems.lean, line 28](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/Triangular/Theorems.lean#L28): “The norm of the triangular Hilbert trilinear form is at most an absolute constant times the product of the three L³ norms for complex Schwartz inputs.”
- [`Triangular.Auto.tendsto_truncatedForm`](https://leanpool.github.io/lean-pool/LeanPool/Triangular/Auto/TriangularHT.html#Triangular.Auto.tendsto_truncatedForm) (theorem; a main declaration), declared in [LeanPool/Triangular/Auto/TriangularHT.lean, line 990](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/Triangular/Auto/TriangularHT.lean#L990): “The trilinear truncations converge to the principal value as the cutoff decreases to zero.”
- [`Triangular.Auto.triangularHilbert_unique_extension`](https://leanpool.github.io/lean-pool/LeanPool/Triangular/Auto/TriangularHT.html#Triangular.Auto.triangularHilbert_unique_extension) (theorem; a main declaration), declared in [LeanPool/Triangular/Auto/TriangularHT.lean, line 952](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/Triangular/Auto/TriangularHT.lean#L952): “The principal-value form extends uniquely to a continuous complex trilinear form on L³, with the same norm bound.”

## Project

- Authors: Joris Roos.
- Source: [manuscript](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/paper.pdf).
- Project repository: [roos-j/lean-triangular](https://github.com/roos-j/lean-triangular), at commit [9edcdf82](https://github.com/roos-j/lean-triangular/tree/9edcdf82f32466c0275ba6d67f5b37876c23ed0c).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 42B20, 42A20.
- In Lean Pool: [LeanPool/Triangular](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/Triangular), from the card [LeanPool/projects/triangular-hilbert.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/triangular-hilbert.yaml).

## Sources

- [Lean Pool at 307e3125: LeanPool/projects/triangular-hilbert.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/triangular-hilbert.yaml)
- [Lean Pool at 307e3125: LeanPool/Triangular](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/Triangular)
