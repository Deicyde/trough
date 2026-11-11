---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.isUnit_smul_one, MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.ringInverse_smul_one, MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.cayleyTransform, MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.commute_sub_I_add_I, MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.isUnit_sub_smul_one_of_isSelfAdjoint_of_im_ne_zero, MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.isUnit_add_I_smul_one_of_isSelfAdjoint, MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.isUnit_sub_I_smul_one_of_isSelfAdjoint, MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.isUnit_ringInverse_add_I_of_isSelfAdjoint
statement: formalized
proof: formalized
---

# Cayley transform

26 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html).

## Scalar operators and the Cayley transform

## Nonzero scalar operators are units

A nonzero scalar operator is a unit.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.isUnit_smul_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#is-unit-smul-one).

## Inverse of a scalar operator

The ring inverse of a scalar operator is the scalar operator of the
inverse scalar.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.ringInverse_smul_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#ring-inverse-smul-one).

## Cayley transform of an operator

The Cayley transform of an operator `A`: `(A - i) * (A + i)⁻¹`. The
factor `A + i • 1` is a unit when `A` is self-adjoint on a complete Hilbert space (see
`isUnit_add_I_smul_one_of_isSelfAdjoint` below), in which case the ring
inverse here is the genuine operator inverse.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.cayleyTransform`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#cayley-transform).

## Factors of the Cayley transform commute

The two factors of the Cayley transform commute.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.commute_sub_I_add_I`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#commute-sub-i-add-i).

## Self-adjoint operator minus a non-real scalar is invertible

For a self-adjoint operator, `A - w • 1` is a unit whenever `w` has
nonzero imaginary part. The proof is the norm estimate
`‖(A - w • 1) x‖ ≥ |w.im| * ‖x‖`, read off from the imaginary part of
`⟪(A - w • 1) x, x⟫`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.isUnit_sub_smul_one_of_isSelfAdjoint_of_im_ne_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#is-unit-sub-smul-one-of-is-self-adjoint).

## Self-adjoint operator plus $i$ is invertible

For a self-adjoint operator, `A + i • 1` is a unit.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.isUnit_add_I_smul_one_of_isSelfAdjoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#is-unit-add-i-smul-one-of-is-self-adjoin).

## Self-adjoint operator minus $i$ is invertible

For a self-adjoint operator, `A - i • 1` is a unit.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.isUnit_sub_I_smul_one_of_isSelfAdjoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#is-unit-sub-i-smul-one-of-is-self-adjoin).

## Inverse of a self-adjoint operator plus $i$ is a unit

The inverse of `A + i • 1` is a unit for self-adjoint `A`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.isUnit_ringInverse_add_I_of_isSelfAdjoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#is-unit-ring-inverse-add-i-of-is-self-ad).

## Adjoint of the Cayley transform

The adjoint of the Cayley transform.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.star_cayleyTransform`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#star-cayley-transform).

## Adjoint of the Cayley transform is a left inverse

The Cayley transform of a self-adjoint operator satisfies `U† * U = 1`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.star_mul_self_cayleyTransform`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#star-mul-self-cayley-transform).

## Adjoint of the Cayley transform is a right inverse

The Cayley transform of a self-adjoint operator satisfies `U * U† = 1`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.mul_star_self_cayleyTransform`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#mul-star-self-cayley-transform).

## Cayley transform of a self-adjoint operator is invertible

The Cayley transform of a self-adjoint operator is a unit.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.isUnit_cayleyTransform`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#is-unit-cayley-transform).

## Cayley transform of a self-adjoint operator is unitary

The Cayley transform of a self-adjoint operator is unitary.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.mem_unitary_cayleyTransform`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#mem-unitary-cayley-transform).

## Cayley transform preserves norms of vectors

The Cayley transform of a self-adjoint operator is an isometry.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.norm_cayleyTransform_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#norm-cayley-transform-apply).

## Operator norm of the Cayley transform is one

On a nontrivial space, the Cayley transform has operator norm `1`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.norm_cayleyTransform`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#norm-cayley-transform).

## Formula for one plus the Cayley transform

`1 + U` is `2 • A` times the inverse of `A + i • 1`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.one_add_cayleyTransform`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#one-add-cayley-transform).

## Formula for one minus the Cayley transform

`1 - U` is `2 • (i • 1)` times the inverse of `A + i • 1`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.one_sub_cayleyTransform`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#one-sub-cayley-transform).

## One minus the Cayley transform is invertible

`1 - U` is a unit for the Cayley transform of a self-adjoint operator:
`1` is never in the spectrum of `U`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.isUnit_one_sub_cayleyTransform`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#is-unit-one-sub-cayley-transform).

## Inverse Cayley formula

The inverse Cayley formula: `A = i • (1 + U) * (1 - U)⁻¹`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.eq_cayleyTransform_inv`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#eq-cayley-transform-inv).

## Resolvent factorization for the Cayley transform

The resolvent-type factorization behind the spectral mapping: for
`μ ≠ 1` and `λ = i * (1 + μ) / (1 - μ)`,
`μ • 1 - U = ((μ - 1) • (A - λ • 1)) * (A + i • 1)⁻¹`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.algebraMap_sub_cayleyTransform`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#algebra-map-sub-cayley-transform).

## One is not in the spectrum of the Cayley transform

`1` is never in the spectrum of the Cayley transform.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.one_notMem_spectrum_cayleyTransform`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#one-not-mem-spectrum-cayley-transform).

## Spectral mapping for the Cayley transform, image direction

The image direction of the spectral mapping: if `w` is in the spectrum
of `A`, then `(w - i) / (w + i)` is in the spectrum of `U`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.mem_spectrum_cayleyTransform_of_mem_spectrum`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#mem-spectrum-cayley-transform-of-mem-spe).

## Spectral mapping for the Cayley transform, preimage direction

The preimage direction of the spectral mapping: every point of the
spectrum of `U` is `(w - i) / (w + i)` for some `w` in the spectrum of `A`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.exists_mem_spectrum_of_mem_spectrum_cayleyTransform`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#exists-mem-spectrum-of-mem-spectrum-cayl).

## Spectrum of the Cayley transform

The spectrum of the Cayley transform is the image of the spectrum of `A`
under the Möbius map `λ ↦ (λ - i) / (λ + i)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.spectrum_cayleyTransform`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 482](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L482). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#spectrum-cayley-transform).

## Spectrum of the Cayley transform lies on the unit circle

Points of the spectrum of the Cayley transform lie on the unit circle.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.norm_eq_one_of_mem_spectrum_cayleyTransform`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 493](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L493). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#norm-eq-one-of-mem-spectrum-cayley-trans).

## Eigenvalues of the Cayley transform

The eigenvalue correspondence: for `μ ≠ 1`, `μ` is an eigenvalue of the
Cayley transform `U` iff `i * (1 + μ) / (1 - μ)` is an eigenvalue of `A`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CayleyTransform.ContinuousLinearMap.hasEigenvalue_cayleyTransform_iff`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean, line 499](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CayleyTransform.lean#L499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html#has-eigenvalue-cayley-transform-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cayley transform](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/spectral-theory/cayley-transform)
