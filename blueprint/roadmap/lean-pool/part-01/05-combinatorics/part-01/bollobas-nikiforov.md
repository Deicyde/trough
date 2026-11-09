---
declaration: theorem
origin: cited
lean: BollobasNikiforov.lambda1_sq_add_lambda2_sq_le
statement: formalized
proof: formalized
---

# The Bollobás–Nikiforov conjecture

> Proves the Bollobás–Nikiforov conjecture (2007): every finite noncomplete simple graph G on at least two vertices satisfies λ₁(G)² + λ₂(G)² ≤ 2 (1 - 1/ω(G)) |E(G)|, where λ₁ ≥ λ₂ are the two largest adjacency eigenvalues and ω(G) is the clique number. The inequality is derived from a weighted spectral inequality for symmetric entrywise nonnegative matrices supported on the edges of G, which in turn rests on a complete positivity theorem for planar Gram matrices and a rank-two Gram inequality. The rank-two Gram inequality also identifies the conic parameter of Coutinho, Spier and Zhang with the clique number. The supporting library develops the completely positive cone and its closedness, the Motzkin–Straus inequality in completely positive form, total nonnegativity of truncated-square and convex kernels via Cauchy–Binet, weighted Laplacian updates, Schur complements, Perron eigenvectors, the Schur product theorem and Cauchy interlacing over Mathlib.

*Quoted from the card [LeanPool/projects/bollobas-nikiforov.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/bollobas-nikiforov.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 10 main results, each with its informal statement quoted from the card. The scan finds 10 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`BollobasNikiforov.lambda1_sq_add_lambda2_sq_le`](https://leanpool.github.io/lean-pool/LeanPool/BollobasNikiforov/Main.html#BollobasNikiforov.lambda1_sq_add_lambda2_sq_le) (theorem; a main declaration), declared in [LeanPool/BollobasNikiforov/Main.lean, line 34](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BollobasNikiforov/Main.lean#L34): “For every finite simple graph G on at least two vertices that is not complete, the two largest adjacency eigenvalues satisfy λ₁(G)² + λ₂(G)² ≤ 2 (1 - 1/ω(G)) |E(G)|, with ω(G) the clique number and |E(G)| the number of edges.”
- [`BollobasNikiforov.weighted`](https://leanpool.github.io/lean-pool/LeanPool/BollobasNikiforov/Spectral/Weighted.html#BollobasNikiforov.weighted) (theorem), declared in [LeanPool/BollobasNikiforov/Spectral/Weighted.lean, line 609](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BollobasNikiforov/Spectral/Weighted.lean#L609): “If B is a real symmetric matrix, indexed by a finite type with at least two elements, that is entrywise nonnegative, has zero diagonal and vanishes off the edges of a graph G on that type, then the sum of the squares of its two largest positive eigenvalues is at most (1 - 1/ω(G)) times its squared Frobenius norm.”
- [`BollobasNikiforov.matrix_theorem`](https://leanpool.github.io/lean-pool/LeanPool/BollobasNikiforov/M/Main.html#BollobasNikiforov.matrix_theorem) (theorem), declared in [LeanPool/BollobasNikiforov/M/Main.lean, line 27](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BollobasNikiforov/M/Main.lean#L27): “If planar vectors z₁, …, zₙ lie in a closed half-plane through the origin and X is their Gram matrix, then X ∘ X plus the weighted Laplacian with weights X_ij² on the pairs i < j with X_ij < 0 is completely positive.”
- [`BollobasNikiforov.gram_le`](https://leanpool.github.io/lean-pool/LeanPool/BollobasNikiforov/Spectral/Gram.html#BollobasNikiforov.gram_le) (theorem), declared in [LeanPool/BollobasNikiforov/Spectral/Gram.lean, line 564](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BollobasNikiforov/Spectral/Gram.lean#L564): “For every real positive semidefinite matrix X of rank at most two, ∑\_{i,j} (A_G)\_ij (X_ij)₊² ≤ (1 - 1/ω(G)) ‖X‖\_F², where (·)₊ is the positive part.”
- [`BollobasNikiforov.chiVec3_eq_cliqueNum`](https://leanpool.github.io/lean-pool/LeanPool/BollobasNikiforov/Spectral/Conic.html#BollobasNikiforov.chiVec3_eq_cliqueNum) (theorem), declared in [LeanPool/BollobasNikiforov/Spectral/Conic.lean, line 580](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BollobasNikiforov/Spectral/Conic.lean#L580): “For every graph G on a nonempty finite vertex type, the rank-two conic parameter χ''\_{vec,3}(G) of Coutinho, Spier and Zhang, defined as the supremum of ‖X‖\_F² over positive semidefinite X of rank at most two with nonnegative entries on the edges and unit off-edge mass, equals the clique number ω(G).”
- [`BollobasNikiforov.motzkinStraus`](https://leanpool.github.io/lean-pool/LeanPool/BollobasNikiforov/MS/Basic.html#BollobasNikiforov.motzkinStraus) (lemma), declared in [LeanPool/BollobasNikiforov/MS/Basic.lean, line 451](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BollobasNikiforov/MS/Basic.lean#L451): “Motzkin–Straus inequality; for every entrywise nonnegative vector y, yᵀ A_G y ≤ (1 - 1/ω(G)) (∑ᵢ yᵢ)².”
- [`BollobasNikiforov.posSemidef_hadamard`](https://leanpool.github.io/lean-pool/LeanPool/BollobasNikiforov/Basic/Inner.html#BollobasNikiforov.posSemidef_hadamard) (theorem), declared in [LeanPool/BollobasNikiforov/Basic/Inner.lean, line 214](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BollobasNikiforov/Basic/Inner.lean#L214): “Schur product theorem over the reals; the Hadamard product of two positive semidefinite matrices is positive semidefinite.”
- [`BollobasNikiforov.isClosed_isCompletelyPositive`](https://leanpool.github.io/lean-pool/LeanPool/BollobasNikiforov/CP/Closed.html#BollobasNikiforov.isClosed_isCompletelyPositive) (lemma), declared in [LeanPool/BollobasNikiforov/CP/Closed.lean, line 239](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BollobasNikiforov/CP/Closed.lean#L239): “The cone of completely positive real matrices is closed.”
- [`BollobasNikiforov.IsTotallyNonneg.mul`](https://leanpool.github.io/lean-pool/LeanPool/BollobasNikiforov/TN/Truncated.html#BollobasNikiforov.IsTotallyNonneg.mul) (lemma), declared in [LeanPool/BollobasNikiforov/TN/Truncated.lean, line 922](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BollobasNikiforov/TN/Truncated.lean#L922): “Cauchy–Binet; the product of two totally nonnegative real matrices is totally nonnegative.”
- [`BollobasNikiforov.exists_nonneg_eigenvector_lambdaMax`](https://leanpool.github.io/lean-pool/LeanPool/BollobasNikiforov/Spectral/Perron.html#BollobasNikiforov.exists_nonneg_eigenvector_lambdaMax) (lemma), declared in [LeanPool/BollobasNikiforov/Spectral/Perron.lean, line 109](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BollobasNikiforov/Spectral/Perron.lean#L109): “Perron; a real symmetric entrywise nonnegative matrix on a nonempty finite index type has an entrywise nonnegative unit eigenvector for its largest eigenvalue.”

## Project

- Authors: Gabriel Coutinho, Yinchen Liu, Thomás Jung Spier, Quanyu Tang, Shengtong Zhang.
- Source: *The Bollobás–Nikiforov inequality for nonnegative edge weights* by Gabriel Coutinho, Yinchen Liu, Thomás Jung Spier, Quanyu Tang, Shengtong Zhang.
- Project repository: [ShengtongZhang-alt/BN](https://github.com/ShengtongZhang-alt/BN), at commit [edb5259d](https://github.com/ShengtongZhang-alt/BN/tree/edb5259dfd055ea31b4c46ac9ea4d33a758c2b99).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C50, 15B48, 05C35, 15A18.
- In Lean Pool: [LeanPool/BollobasNikiforov](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BollobasNikiforov), from the card [LeanPool/projects/bollobas-nikiforov.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/bollobas-nikiforov.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/bollobas-nikiforov.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/bollobas-nikiforov.yaml)
- [Lean Pool at 2b205bf9: LeanPool/BollobasNikiforov](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BollobasNikiforov)
