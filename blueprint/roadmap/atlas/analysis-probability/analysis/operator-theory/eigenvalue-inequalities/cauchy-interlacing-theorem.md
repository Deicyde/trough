---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.CauchyInterlacing.compression, MathlibExt.Analysis.InnerProductSpace.CauchyInterlacing.compression_apply, MathlibExt.Analysis.InnerProductSpace.CauchyInterlacing.compression_isSymmetric, MathlibExt.Analysis.InnerProductSpace.CauchyInterlacing.compression_rayleigh, MathlibExt.Analysis.InnerProductSpace.CauchyInterlacing.exists_submodule_le_finrank_eq, MathlibExt.Analysis.InnerProductSpace.CauchyInterlacing.eigenvalue_compression_le_eigenvalue, MathlibExt.Analysis.InnerProductSpace.CauchyInterlacing.eigenvalue_le_eigenvalue_compression, MathlibExt.Analysis.InnerProductSpace.CauchyInterlacing.cauchy_interlacing
statement: formalized
proof: formalized
---

# Cauchy interlacing theorem

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/cauchy-interlacing-theorem/index.html).

## Compression of an operator to a subspace

The compression of an operator `T` to a subspace `S`: project `T x`
orthogonally back onto `S`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CauchyInterlacing.compression`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/CauchyInterlacing.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CauchyInterlacing.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/cauchy-interlacing-theorem/index.html#compression).

## Action of the compression of an operator

The compression acts by projecting the image back onto the subspace.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CauchyInterlacing.compression_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CauchyInterlacing.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CauchyInterlacing.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/cauchy-interlacing-theorem/index.html#compression-apply).

## Compression of a symmetric operator is symmetric

The compression of a symmetric operator is symmetric.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CauchyInterlacing.compression_isSymmetric`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CauchyInterlacing.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CauchyInterlacing.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/cauchy-interlacing-theorem/index.html#compression-is-symmetric).

## Rayleigh form of a compression

The Rayleigh form of the compression at `y` equals the Rayleigh form
of the original operator at the underlying vector `(y : E)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CauchyInterlacing.compression_rayleigh`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CauchyInterlacing.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CauchyInterlacing.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/cauchy-interlacing-theorem/index.html#compression-rayleigh).

## Subspaces of every smaller dimension inside a given subspace

A subspace of dimension `m` can be thinned to a subspace of any
smaller dimension.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CauchyInterlacing.exists_submodule_le_finrank_eq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CauchyInterlacing.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CauchyInterlacing.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/cauchy-interlacing-theorem/index.html#exists-submodule-le-finrank-eq).

## Cauchy interlacing, upper half

The `k`-th eigenvalue of the
compression to a codimension-one subspace is at most the `k`-th
eigenvalue of the original operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CauchyInterlacing.eigenvalue_compression_le_eigenvalue`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CauchyInterlacing.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CauchyInterlacing.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/cauchy-interlacing-theorem/index.html#eigenvalue-compression-le-eigenvalue).

## Cauchy interlacing, lower half

The `k`-th eigenvalue of the
compression to a codimension-one subspace is at least the `(k+1)`-st
eigenvalue of the original operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CauchyInterlacing.eigenvalue_le_eigenvalue_compression`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CauchyInterlacing.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CauchyInterlacing.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/cauchy-interlacing-theorem/index.html#eigenvalue-le-eigenvalue-compression).

## Cauchy interlacing

For a codimension-one subspace `S`, the
eigenvalues `μₖ` of the compression of a self-adjoint operator `T`
interlace the eigenvalues `λₖ` of `T`:
`λₖ₊₁ ≤ μₖ ≤ λₖ`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CauchyInterlacing.cauchy_interlacing`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CauchyInterlacing.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CauchyInterlacing.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/cauchy-interlacing-theorem/index.html#cauchy-interlacing).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cauchy interlacing theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/cauchy-interlacing-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/eigenvalue-inequalities/cauchy-interlacing-theorem)
