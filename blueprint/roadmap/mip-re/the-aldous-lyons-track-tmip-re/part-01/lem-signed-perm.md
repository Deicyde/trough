---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.SignedPerm.toMatrix_mul, MIPRE.Tailored.SignedPerm.toMatrix_injective, MIPRE.Tailored.SignedPerm.toMatrix_inv, MIPRE.Tailored.SignedPerm.toMatrix_negOne, MIPRE.Tailored.SignedPerm.toMatrix_diag, MIPRE.Tailored.SignedPerm.toMatrix_prod, MIPRE.Tailored.SignedPerm.toMatrix_map, MIPRE.Tailored.SignedPerm.toMatrix_mem_unitaryGroup, MIPRE.Tailored.IsSignedPerm.isHermitian, MIPRE.Tailored.IsSignedPerm.isDiag_iff, MIPRE.Tailored.IsSignedPerm.kronecker, MIPRE.Tailored.IsSignedPerm.conjTranspose_eq_transpose
statement: formalized
proof: formalized
---

# Signed permutation matrices

The matrix map is an injective homomorphism from the signed permutations of $\Omega$ to the unitary matrices on $\mathbb{C}^\Omega$. It sends the sign flip to $-{I}$, the signs $s$ to the diagonal $((-1)^{s(j)})_j$, products of signed sets to Kronecker products, and a relabelling of $\Omega$ to the reindexed matrix. A signed permutation matrix has real entries; it is self-adjoint when it is an involution, and it is diagonal exactly when it is a $\pm 1$ diagonal.

## Depends on

- [Signed permutations; II:1008–1069](def-signed-perm.md)

## Proof

Column $j$ of the matrix of $(\sigma, s)$ has a single nonzero entry, $(-1)^{s(j)}$ in row $\sigma(j)$. The product of the matrices of $(\sigma, s)$ and $(\tau, t)$ has, in column $j$, the single entry $(-1)^{s(\tau(j)) + t(j)}$ in row $\sigma\tau(j)$, which is the group law; and the columns determine $(\sigma, s)$. The adjoint is the matrix of the inverse, so the matrix is unitary, and an involution equals its adjoint. A diagonal one has $\sigma = {I}$.

## Lean

Formalized as [`MIPRE.Tailored.SignedPerm.toMatrix_mul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.SignedPerm.toMatrix_mul), [`MIPRE.Tailored.SignedPerm.toMatrix_injective`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.SignedPerm.toMatrix_injective), [`MIPRE.Tailored.SignedPerm.toMatrix_inv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.SignedPerm.toMatrix_inv), [`MIPRE.Tailored.SignedPerm.toMatrix_negOne`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.SignedPerm.toMatrix_negOne), [`MIPRE.Tailored.SignedPerm.toMatrix_diag`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.SignedPerm.toMatrix_diag), [`MIPRE.Tailored.SignedPerm.toMatrix_prod`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.SignedPerm.toMatrix_prod), [`MIPRE.Tailored.SignedPerm.toMatrix_map`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.SignedPerm.toMatrix_map), [`MIPRE.Tailored.SignedPerm.toMatrix_mem_unitaryGroup`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.SignedPerm.toMatrix_mem_unitaryGroup), [`MIPRE.Tailored.IsSignedPerm.isHermitian`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.IsSignedPerm.isHermitian), [`MIPRE.Tailored.IsSignedPerm.isDiag_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.IsSignedPerm.isDiag_iff), [`MIPRE.Tailored.IsSignedPerm.kronecker`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.IsSignedPerm.kronecker), [`MIPRE.Tailored.IsSignedPerm.conjTranspose_eq_transpose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.IsSignedPerm.conjTranspose_eq_transpose).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 159](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L159)
