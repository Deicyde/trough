---
declaration: section
origin: cited
lean: Matrix.IsHermitian.charpoly_isRealRooted, Matrix.PosSemidef.l2_opNorm_eq_maxRealRoot_charpoly
statement: formalized
proof: formalized
---

# Eigenvalues and spectral norm of Hermitian matrices

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-and-spectral-norm-of-hermitian-matri/index.html).

## Hermitian matrices have real-rooted characteristic polynomials

The characteristic
polynomial of a Hermitian complex matrix is real-rooted.

Formalized by `Matrix.IsHermitian.charpoly_isRealRooted`, a theorem declared in [MathlibExt/Analysis/Matrix/Spectrum.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Matrix/Spectrum.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-and-spectral-norm-of-hermitian-matri/index.html#charpoly-is-real-rooted).

## Spectral norm of a positive semidefinite matrix

Let $A$ be a positive semidefinite
complex square matrix indexed by a nonempty finite set. Then the operator norm of $A$ with
respect to the Euclidean ($\ell^2$) norm equals the largest real part of a root of the
characteristic polynomial of $A$. Since these roots are real, this is its largest root.

Formalized by `Matrix.PosSemidef.l2_opNorm_eq_maxRealRoot_charpoly`, a theorem declared in [MathlibExt/Analysis/Matrix/Spectrum.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Matrix/Spectrum.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-and-spectral-norm-of-hermitian-matri/index.html#l2-op-norm-eq-max-real-root-charpoly).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Eigenvalues and spectral norm of Hermitian matrices](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-and-spectral-norm-of-hermitian-matri/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/eigenvalues-and-canonical-forms/eigenvalues-and-spectral-norm-of-hermitian-matri)
