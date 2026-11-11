---
declaration: section
origin: cited
lean: MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.zeta, MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.zeta_eq_stdAddChar, MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.zeta_isPrimitiveRoot, MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.fourierVec, MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.fourierVec_apply, MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.circulantEigenvalue, MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.circulantEigenvalue_apply, MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.circulant_mulVec_fourierVec
statement: formalized
proof: formalized
---

# Circulant matrices

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html).

## Standard primitive n-th root of unity $e^{2\pi i/n}$

The exponential `exp (2 * π * I / n)`, a primitive `n`-th root for nonzero `n`.
This definition is total: at `n = 0`, it is `exp 0 = 1`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.zeta`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#zeta).

## Standard root of unity as the standard additive character

For nonzero `n`, `zeta n` is the canonical standard character at `1`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.zeta_eq_stdAddChar`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#zeta-eq-std-add-char).

## $e^{2\pi i/n}$ is a primitive n-th root of unity

For nonzero `n`, the exponential is a primitive `n`-th root of unity.

Formalized by `MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.zeta_isPrimitiveRoot`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#zeta-is-primitive-root).

## Fourier vector on the integers modulo n

The `j`-th Fourier vector on `ZMod n`, using the canonical positive character.

Formalized by `MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.fourierVec`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#fourier-vec).

## Exponential formula for Fourier vectors

The character definition of a Fourier vector agrees with its exponential formula.

Formalized by `MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.fourierVec_apply`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#fourier-vec-apply).

## Fourier eigenvalue of a circulant matrix

The `j`-th Fourier eigenvalue of a circulant matrix is its canonical DFT.

Formalized by `MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.circulantEigenvalue`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#circulant-eigenvalue).

## Exponential-sum formula for circulant eigenvalues

The canonical DFT definition agrees with the original negative-exponent eigenvalue sum.

Formalized by `MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.circulantEigenvalue_apply`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#circulant-eigenvalue-apply).

## Fourier vectors are eigenvectors of circulant matrices

Every Fourier vector is an eigenvector of every circulant matrix.

Formalized by `MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.circulant_mulVec_fourierVec`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#circulant-mul-vec-fourier-vec).

## Fourier matrix

The Fourier matrix, whose `j`-th column is the standard character `fourierVec n j`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.fourierMatrix`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#fourier-matrix).

## Entrywise exponential formula for the Fourier matrix

The Fourier matrix agrees entrywise with its original exponential formula.

Formalized by `MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.fourierMatrix_apply`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#fourier-matrix-apply).

## Inverse Fourier matrix

The inverse Fourier matrix, `(1 / n)` times the negative standard character.

Formalized by `MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.fourierMatrixInv`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#fourier-matrix-inv).

## Entrywise exponential formula for the inverse Fourier matrix

The inverse Fourier matrix agrees entrywise with its original exponential formula.

Formalized by `MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.fourierMatrixInv_apply`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#fourier-matrix-inv-apply).

## Fourier matrix acts as n times the inverse DFT

Fourier matrix multiplication is the canonical inverse DFT multiplied by `n`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.fourierMatrix_mulVec_eq_invDFT`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#fourier-matrix-mul-vec-eq-inv-dft).

## Inverse Fourier matrix acts as the DFT divided by n

Inverse Fourier matrix multiplication is the canonical DFT divided by `n`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.fourierMatrixInv_mulVec_eq_dft`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#fourier-matrix-inv-mul-vec-eq-dft).

## Fourier matrix times its inverse is the identity

The Fourier matrix is invertible, with inverse `fourierMatrixInv`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.fourierMatrix_mul_inv`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#fourier-matrix-mul-inv).

## Circulant matrices are diagonalized by the Fourier matrix

Circulant matrices are diagonalized by the Fourier matrix.

Formalized by `MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.circulant_mul_fourierMatrix`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#circulant-mul-fourier-matrix).

## Determinant of a circulant matrix

The determinant of a circulant matrix is the product of its Fourier eigenvalues.

Formalized by `MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.det_circulant`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#det-circulant).

## Zeroth circulant eigenvalue is the sum of entries

The Fourier eigenvalue at `j = 0` is the sum of the entries of `v`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.circulantEigenvalue_zero`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#circulant-eigenvalue-zero).

## Sum of the eigenvalues of a circulant matrix

The Fourier eigenvalues sum to `n * v 0`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.CirculantSpectrum.sum_circulantEigenvalue`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/CirculantSpectrum.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#sum-circulant-eigenvalue).

## Block-circulant matrix over ℤ_n

The block-circulant matrix on `ℤ_n × Fin d` with block `v (p - q)` in position `(p, q)`.

Formalized by `StatMech.Onsager.ons_blockCirculant`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/BlockCirculant.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/BlockCirculant.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#ons-block-circulant).

## Fourier symbol of a block-circulant matrix

The Fourier symbol `∑_k ω ^ (k j) • v k` of a block-circulant matrix at frequency `j`.

Formalized by `StatMech.Onsager.ons_blockSymbol`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/BlockCirculant.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/BlockCirculant.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#ons-block-symbol).

## Two-dimensional block-circulant matrix on the torus

The block-circulant matrix on `(ℤ_L × ℤ_L) × Fin d` with block `v (p - q)` in position `(p, q)`.

Formalized by `StatMech.Onsager.ons_blockCirculant2D`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/BlockCirculant2D.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/BlockCirculant2D.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#ons-block-circulant2-d).

## Fourier symbol of a two-dimensional block-circulant matrix

The Fourier symbol `∑_k ω ^ (k₁ j₁ + k₂ j₂) • v k` at frequency `j`.

Formalized by `StatMech.Onsager.ons_blockSymbol2D`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/BlockCirculant2D.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/BlockCirculant2D.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html#ons-block-symbol2-d).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Circulant matrices](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/circulant-matrices/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/special-matrices/circulant-matrices)
