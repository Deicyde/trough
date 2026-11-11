---
declaration: section
origin: cited
lean: Cslib.MachineLearning.GBLUP.posDef_mul_transpose_add, Cslib.MachineLearning.GBLUP.transpose_mul_add_inv_mul_transpose, Cslib.MachineLearning.GBLUP.mul_ridgeHat_eq_gblupHat, Cslib.MachineLearning.GBLUP.ridgeEstimate_eq, Cslib.MachineLearning.GBLUP.mulVec_ridgeEstimate, Cslib.MachineLearning.GBLUP.markerKernel, Cslib.MachineLearning.GBLUP.markerKernel_apply, Cslib.MachineLearning.GBLUP.kernelMatrix_markerKernel
statement: formalized
proof: formalized
---

# Kernel ridge regression and GBLUP

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/kernel-ridge-regression-and-gblup/index.html).

## Positive definiteness of the GBLUP matrix

For `λ > 0` the GBLUP matrix `ZZᵀ + λI` is positive definite.

Formalized by `Cslib.MachineLearning.GBLUP.posDef_mul_transpose_add`, a theorem declared in [CSLibExt/MachineLearning/Regression/GBLUP.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/GBLUP.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/kernel-ridge-regression-and-gblup/index.html#pos-def-mul-transpose-add).

## Push-through identity for ridge regression

The **push-through identity** `(ZᵀZ + λI)⁻¹ Zᵀ = Zᵀ (ZZᵀ + λI)⁻¹` for `λ > 0`.

Formalized by `Cslib.MachineLearning.GBLUP.transpose_mul_add_inv_mul_transpose`, a theorem declared in [CSLibExt/MachineLearning/Regression/GBLUP.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/GBLUP.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/kernel-ridge-regression-and-gblup/index.html#transpose-mul-add-inv-mul-transpose).

## RR-BLUP = GBLUP

**RR-BLUP = GBLUP** (fitted values): `Z (ZᵀZ + λI)⁻¹ Zᵀ = ZZᵀ (ZZᵀ + λI)⁻¹` for `λ > 0`.

Formalized by `Cslib.MachineLearning.GBLUP.mul_ridgeHat_eq_gblupHat`, a theorem declared in [CSLibExt/MachineLearning/Regression/GBLUP.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/GBLUP.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/kernel-ridge-regression-and-gblup/index.html#mul-ridge-hat-eq-gblup-hat).

## Ridge marker effects are back-solved from GBLUP

The ridge marker effects are back-solved from GBLUP:
`(ZᵀZ + λI)⁻¹ Zᵀ y = Zᵀ (ZZᵀ + λI)⁻¹ y`.

Formalized by `Cslib.MachineLearning.GBLUP.ridgeEstimate_eq`, a theorem declared in [CSLibExt/MachineLearning/Regression/GBLUP.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/GBLUP.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/kernel-ridge-regression-and-gblup/index.html#ridge-estimate-eq).

## RR-BLUP = GBLUP

**RR-BLUP = GBLUP** (predictions): for any genotypes `Z'` (training or new individuals),
`Z' β̂ = Z' Zᵀ (ZZᵀ + λI)⁻¹ y`.

Formalized by `Cslib.MachineLearning.GBLUP.mulVec_ridgeEstimate`, a theorem declared in [CSLibExt/MachineLearning/Regression/GBLUP.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/GBLUP.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/kernel-ridge-regression-and-gblup/index.html#mul-vec-ridge-estimate).

## Linear marker kernel on genotype vectors

The linear marker kernel `k(a, b) = s ⟪a, b⟫ = s ∑ⱼ aⱼ bⱼ` on genotype vectors: the
covariance of genetic values `aᵀβ` and `bᵀβ` when the marker effects `β` are independent with
variance `s`.

Formalized by `Cslib.MachineLearning.GBLUP.markerKernel`, a definition declared in [CSLibExt/MachineLearning/Regression/GBLUP.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/GBLUP.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/kernel-ridge-regression-and-gblup/index.html#marker-kernel).

## Formula for the linear marker kernel

Unfolding `markerKernel`.

Formalized by `Cslib.MachineLearning.GBLUP.markerKernel_apply`, a theorem declared in [CSLibExt/MachineLearning/Regression/GBLUP.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/GBLUP.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/kernel-ridge-regression-and-gblup/index.html#marker-kernel-apply).

## Kernel matrix of the marker kernel

The kernel matrix of the marker kernel between genotypes `Z'` and `Z` is `s Z' Zᵀ`.

Formalized by `Cslib.MachineLearning.GBLUP.kernelMatrix_markerKernel`, a theorem declared in [CSLibExt/MachineLearning/Regression/GBLUP.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/GBLUP.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/kernel-ridge-regression-and-gblup/index.html#kernel-matrix-marker-kernel).

## Positive semidefiniteness of the marker kernel matrix

For `s ≥ 0` the marker kernel is a covariance kernel: its kernel matrix on any inputs is
positive semidefinite.

Formalized by `Cslib.MachineLearning.GBLUP.kernelMatrix_markerKernel_posSemidef`, a theorem declared in [CSLibExt/MachineLearning/Regression/GBLUP.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/GBLUP.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/kernel-ridge-regression-and-gblup/index.html#kernel-matrix-marker-kernel-pos-semidef).

## GP posterior mean = GBLUP

For the marker kernel with variance `s > 0` and noise variance
`σ² > 0`, the predictive-mean matrix `K(Z', Z) (K(Z, Z) + σ² I)⁻¹` of Gaussian-process
regression is `Z' Zᵀ (ZZᵀ + (σ²/s) I)⁻¹`.

Formalized by `Cslib.MachineLearning.GBLUP.gpMean_markerKernel`, a theorem declared in [CSLibExt/MachineLearning/Regression/GBLUP.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/GBLUP.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/kernel-ridge-regression-and-gblup/index.html#gp-mean-marker-kernel).

## GP posterior mean = RR-BLUP

With the marker kernel, the GP predictive mean at genotypes
`Z'` is `Z' β̂` for the ridge marker effects `β̂` with `λ = σ²/s`.

Formalized by `Cslib.MachineLearning.GBLUP.gpMean_markerKernel_mulVec`, a theorem declared in [CSLibExt/MachineLearning/Regression/GBLUP.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/GBLUP.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/kernel-ridge-regression-and-gblup/index.html#gp-mean-marker-kernel-mul-vec).

## The GBLUP posterior

If the genetic values `Z' β` of individuals with genotypes `Z'` and
the phenotypes `y = Z β + ε` of the training individuals are jointly Gaussian with the covariance
of the marker kernel (marker-effect variance `s > 0`, residual variance `σ² > 0`), then given `y`
the genetic values are Gaussian with mean `Z' Zᵀ (ZZᵀ + (σ²/s) I)⁻¹ y`, which is the RR-BLUP
prediction `Z' β̂` (`gpMean_markerKernel_mulVec`), and covariance
`s (Z' Z'ᵀ - Z' Zᵀ (ZZᵀ + (σ²/s) I)⁻¹ Z Z'ᵀ)`.

Formalized by `Cslib.MachineLearning.GBLUP.condDistrib_markerKernel`, a theorem declared in [CSLibExt/MachineLearning/Regression/GBLUP.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/GBLUP.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/kernel-ridge-regression-and-gblup/index.html#cond-distrib-marker-kernel).

## Kernel ridge regression = GBLUP = RR-BLUP

In a real RKHS whose kernel has Gram matrix
`ZZᵀ` at the training inputs, the kernel ridge fit (the minimizer of
`∑ᵢ (yᵢ - f xᵢ)² + λ ‖f‖²`, `kernelRidgeRisk_kernelRidgeFit_le`) has fitted values `Z β̂`.

Formalized by `Cslib.MachineLearning.GBLUP.kernelRidgeFit_eq_mulVec_ridgeEstimate`, a theorem declared in [CSLibExt/MachineLearning/Regression/GBLUP.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/GBLUP.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/kernel-ridge-regression-and-gblup/index.html#kernel-ridge-fit-eq-mul-vec-ridge-estima).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kernel ridge regression and GBLUP](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/kernel-ridge-regression-and-gblup/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/machine-learning/supervised-learning/kernel-ridge-regression-and-gblup)
