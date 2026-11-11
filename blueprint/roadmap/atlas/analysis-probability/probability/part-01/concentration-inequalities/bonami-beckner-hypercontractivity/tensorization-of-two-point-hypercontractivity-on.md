---
declaration: section
origin: cited
lean: StatMech.Probability.bnt_uexp, StatMech.Probability.bnt_qnormPow, StatMech.Probability.bnt_qnorm, StatMech.Probability.bnt_noiseKernel, StatMech.Probability.bnt_noiseOp, StatMech.Probability.bnt_uexp_eq_expect, StatMech.Probability.bnt_noiseOp_eq_boolNoiseOp, StatMech.Probability.bnt_VectorTwoPoint
statement: formalized
proof: formalized
---

# Tensorization of two-point hypercontractivity on the uniform cube

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/tensorization-of-two-point-hypercontractivity-on/index.html).

## Uniform expectation on the Boolean cube

The expectation of `f` under the uniform measure on `ι → Bool`. This is `𝔼 ω, f ω`
(`Finset.expect`).

Formalized by `StatMech.Probability.bnt_uexp`, a definition declared in [MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/tensorization-of-two-point-hypercontractivity-on/index.html#bnt-uexp).

## q-th moment under the uniform measure on the cube

`E|f|^q` under the uniform measure.

Formalized by `StatMech.Probability.bnt_qnormPow`, a definition declared in [MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/tensorization-of-two-point-hypercontractivity-on/index.html#bnt-qnorm-pow).

## $L^q$ norm under the uniform measure on the cube

The `L^q` norm `(E|f|^q)^(1/q)` under the uniform measure.

Formalized by `StatMech.Probability.bnt_qnorm`, a definition declared in [MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/tensorization-of-two-point-hypercontractivity-on/index.html#bnt-qnorm).

## Noise kernel on the Boolean cube

The noise kernel: `∏ i, (1 + ρ)/2` or `(1 - ρ)/2` according as `x i = y i` or not.

Formalized by `StatMech.Probability.bnt_noiseKernel`, a definition declared in [MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/tensorization-of-two-point-hypercontractivity-on/index.html#bnt-noise-kernel).

## Noise operator on the Boolean cube

The noise operator `T_ρ f x = ∑ y, bnt_noiseKernel ρ x y * f y`: for `ρ ∈ [-1, 1]`, the
expectation of `f y` where each coordinate of `y` equals that of `x` with probability
`(1 + ρ)/2`.

Formalized by `StatMech.Probability.bnt_noiseOp`, a definition declared in [MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/tensorization-of-two-point-hypercontractivity-on/index.html#bnt-noise-op).

## Uniform expectation on the cube equals the finite average

`bnt_uexp` is the uniform average `Finset.expect`.

Formalized by `StatMech.Probability.bnt_uexp_eq_expect`, a theorem declared in [MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/tensorization-of-two-point-hypercontractivity-on/index.html#bnt-uexp-eq-expect).

## Agreement of the two noise operators on the Boolean cube

On `Fin n → Bool`, `bnt_noiseOp` is the noise operator `BooleanCube.boolNoiseOp`.

Formalized by `StatMech.Probability.bnt_noiseOp_eq_boolNoiseOp`, a theorem declared in [MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/tensorization-of-two-point-hypercontractivity-on/index.html#bnt-noise-op-eq-bool-noise-op).

## Vector-valued two-point hypercontractive inequality

The vector-valued two-point inequality at noise `ρ`, with `q = 1 + ρ²`: for all `n` and
`u v : (Fin n → Bool) → ℝ`, the average of `‖((1+ρ)/2) u + ((1-ρ)/2) v‖₂²` and
`‖((1-ρ)/2) u + ((1+ρ)/2) v‖₂²` is at most `((‖u‖_q^q + ‖v‖_q^q) / 2)^(2/q)`.

Formalized by `StatMech.Probability.bnt_VectorTwoPoint`, a definition declared in [MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/tensorization-of-two-point-hypercontractivity-on/index.html#bnt-vector-two-point).

## Induction step of hypercontractivity tensorization

The induction step of tensorization: `‖T_ρ g‖₂ ≤ ‖g‖_(1+ρ²)` in dimension `n` implies the
same in dimension `n + 1`.

Formalized by `StatMech.Probability.bnt_TensorStep`, a definition declared in [MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/tensorization-of-two-point-hypercontractivity-on/index.html#bnt-tensor-step).

## Vector two-point inequality implies the tensorization step

The vector two-point inequality gives the tensorization step.

Formalized by `StatMech.Probability.bnt_tensorStep_of_vec`, a theorem declared in [MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/tensorization-of-two-point-hypercontractivity-on/index.html#bnt-tensor-step-of-vec).

## Hypercontractivity from the vector two-point inequality

Hypercontractivity `‖T_ρ f‖₂ ≤ ‖f‖_(1+ρ²)` on `Fin n → Bool`, from the vector two-point
inequality.

Formalized by `StatMech.Probability.bnt_hypercontractivity`, a theorem declared in [MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/tensorization-of-two-point-hypercontractivity-on/index.html#bnt-hypercontractivity).

## Hypercontractivity from the tensorization step

Hypercontractivity `‖T_ρ f‖₂ ≤ ‖f‖_(1+ρ²)` on `Fin n → Bool`, from the tensorization step.

Formalized by `StatMech.Probability.bnt_hypercontractivity_of_twoPoint`, a theorem declared in [MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Hypercontractivity/BonamiTensorize.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/tensorization-of-two-point-hypercontractivity-on/index.html#bnt-hypercontractivity-of-two-point).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tensorization of two-point hypercontractivity on the uniform cube](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/tensorization-of-two-point-hypercontractivity-on/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/tensorization-of-two-point-hypercontractivity-on)
