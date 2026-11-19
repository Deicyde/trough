---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.blockDiag, MIPRE.Tailored.isSignedPerm_blockDiag, MIPRE.Tailored.isDiag_blockDiag, MIPRE.Tailored.controlled_eq_blockDiag, MIPRE.Tailored.isSignedPerm_controlled, MIPRE.Tailored.isDiag_controlled, MIPRE.Tailored.encObs_controlled, MIPRE.Tailored.encObs_submatrix, MIPRE.Tailored.encObs_kronecker_one, MIPRE.Tailored.IsSignedPerm.kronecker_one, MIPRE.Tailored.IsSignedPerm.submatrix_equiv, MIPRE.Tailored.isDiag_submatrix_equiv, MIPRE.Tailored.isDiag_kronecker_one
statement: formalized
proof: formalized
---

# Controlled signed permutations

A block-diagonal matrix whose blocks are signed permutation matrices is one; so is a controlled sum $\sum_z F_z \otimes U_z$, where $F_z$ is the computational-basis projector onto the fibre of $z$ under a map $f$ and each $U_z$ is a signed permutation matrix. When the blocks, or the $U_z$, are diagonal, so is the result. The bit observables of a controlled measurement $F_z \otimes Q^z_a$ are the controlled sums of the bit observables of the $Q^z$; those of a measurement relabelled by a bijection of the space, or tensored with the identity on an ancilla, are relabelled, or tensored, likewise; and both operations keep signed permutations and diagonal matrices.

## Depends on

- [Signed permutation matrices](../part-01/lem-signed-perm.md)
- [The bit observables of an encoded measurement](lem-encoded-pvm-obs.md)

## Proof

The controlled sum applies $U_{f(i)}$ on the second factor of the basis state $(i, a)$, so it is the block-diagonal matrix with blocks $U_{f(i)}$. The block-diagonal matrix with blocks the matrices of $(\sigma_i, s_i)$ is the matrix of the signed permutation $(i, a) \mapsto (i, \sigma_i(a))$ with signs $s_i(a)$. The other claims are linearity of the Kronecker product and of relabelling, entry by entry.

## Lean

Formalized as [`MIPRE.Tailored.blockDiag`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.blockDiag), [`MIPRE.Tailored.isSignedPerm_blockDiag`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isSignedPerm_blockDiag), [`MIPRE.Tailored.isDiag_blockDiag`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isDiag_blockDiag), [`MIPRE.Tailored.controlled_eq_blockDiag`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.controlled_eq_blockDiag), [`MIPRE.Tailored.isSignedPerm_controlled`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isSignedPerm_controlled), [`MIPRE.Tailored.isDiag_controlled`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isDiag_controlled), [`MIPRE.Tailored.encObs_controlled`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.encObs_controlled), [`MIPRE.Tailored.encObs_submatrix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.encObs_submatrix), [`MIPRE.Tailored.encObs_kronecker_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.encObs_kronecker_one), [`MIPRE.Tailored.IsSignedPerm.kronecker_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.IsSignedPerm.kronecker_one), [`MIPRE.Tailored.IsSignedPerm.submatrix_equiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.IsSignedPerm.submatrix_equiv), [`MIPRE.Tailored.isDiag_submatrix_equiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isDiag_submatrix_equiv), [`MIPRE.Tailored.isDiag_kronecker_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isDiag_kronecker_one).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1404](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1404)
