---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model, MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.alpha1, MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.alpha2, MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.kurtosis, MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.integral_alpha1_mul_alpha2, MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.integral_alpha1_pow_three_mul_alpha2, MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.integral_alpha1_mul_alpha2_pow_three, MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.q1_sq_le_one
statement: formalized
proof: formalized
---

# Latent causal variable model

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html).

## Latent Causal Variable

## Latent causal variable model

The latent causal variable model of O'Connor and Price (2018, Equation 3) on a probability
space: `α_k = q_k π + γ_k` with `π` independent of `(γ₁, γ₂)`, the law of `(γ₁, γ₂)` invariant
under each sign flip, `π` of mean zero and unit variance, and both `α_k` of unit second moment.
Fourth moments are assumed finite.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model`, a structure declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#model).

## Marginal effect on the first trait in the latent causal variable model

The marginal effect `α₁ = q₁ π + γ₁` on trait 1.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.alpha1`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#alpha1).

## Marginal effect on the second trait in the latent causal variable model

The marginal effect `α₂ = q₂ π + γ₂` on trait 2.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.alpha2`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#alpha2).

## Excess kurtosis of the latent effect

The excess kurtosis `κ_π = E(π⁴) - 3` of the effect on the latent variable.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.kurtosis`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#kurtosis).

## Genetic correlation in the latent causal variable model

The genetic correlation is `E(α₁ α₂) = q₁ q₂` (O'Connor and Price 2018, after Equation 1).

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.integral_alpha1_mul_alpha2`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#integral-alpha1-mul-alpha2).

## Mixed fourth moment

**Mixed fourth moment** (O'Connor and Price 2018, Equation 2):
`E(α₁³ α₂) = κ_π q₁³ q₂ + 3 q₁ q₂`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.integral_alpha1_pow_three_mul_alpha2`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#integral-alpha1-pow-three-mul-alpha2).

## Mixed fourth moment $E(\alpha_1 \alpha_2^3)$

The mirror image of Equation 2: `E(α₁ α₂³) = κ_π q₁ q₂³ + 3 q₁ q₂`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.integral_alpha1_mul_alpha2_pow_three`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#integral-alpha1-mul-alpha2-pow-three).

## Mediated coefficient of the first trait is at most one in size

Unit variance of `α₁` forces `q₁² ≤ 1` (the non-mediated part has variance `1 - q₁²`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.q1_sq_le_one`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#q1-sq-le-one).

## Mediated coefficient of the second trait is at most one in size

Unit variance of `α₂` forces `q₂² ≤ 1`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.q2_sq_le_one`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#q2-sq-le-one).

## Fourth moment of the latent effect is at least one

`E(π⁴) ≥ (E π²)² = 1`, so the excess kurtosis is at least `-2`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.one_le_integral_pi_pow_four`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#one-le-integral-pi-pow-four).

## Centred mixed fourth moment $E(\alpha_1^3 \alpha_2)$

The centred mixed fourth moment: `E(α₁³ α₂) - 3 ρ_g = κ_π q₁³ q₂`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.centred_moment_left`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#centred-moment-left).

## Centred mixed fourth moment $E(\alpha_1 \alpha_2^3)$

The centred mixed fourth moment: `E(α₁ α₂³) - 3 ρ_g = κ_π q₁ q₂³`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.centred_moment_right`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#centred-moment-right).

## The centred moments order `q₁²` and `q₂²`

If `κ_π ≠ 0` and `ρ_g = q₁ q₂ ≠ 0`, then
`|E(α₁ α₂³) - 3 ρ_g| ≤ |E(α₁³ α₂) - 3 ρ_g|` iff `q₂² ≤ q₁²`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.abs_centredMoment_le_iff`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#abs-centred-moment-le-iff).

## Excess kurtosis of the latent effect is at least −2

`κ_π ≥ -2`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.neg_two_le_kurtosis`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#neg-two-le-kurtosis).

## The paper's uncentred comparison, under its sign condition

If `κ_π > 0` and
`ρ_g ≠ 0`, then `|E(α₁ α₂³)| ≤ |E(α₁³ α₂)|` iff `q₂² ≤ q₁²` (O'Connor and Price 2018, after
Equation 2, which states the forward implication).

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.abs_moment_le_iff_of_kurtosis_pos`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 427](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L427). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#abs-moment-le-iff-of-kurtosis-pos).

## The uncentred comparison is reversed when `κ_π < 0`

If `κ_π < 0` and `ρ_g ≠ 0`, then
`|E(α₁ α₂³)| ≤ |E(α₁³ α₂)|` iff `q₁² ≤ q₂²`. So the paper's uncentred criterion needs
`κ_π > 0`; the centred criterion `abs_centredMoment_le_iff` does not.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.abs_moment_le_iff_of_kurtosis_neg`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#abs-moment-le-iff-of-kurtosis-neg).

## Genetic causality proportion

The genetic causality proportion `gcp = (log|q₂| - log|q₁|) / (log|q₂| + log|q₁|)`
(O'Connor and Price 2018, Equation 4). Meaningful for `0 < |q₁|, |q₂| ≤ 1` and `ρ_g² < 1`; for
`|q₁| = |q₂| = 1` the denominator vanishes and the value is `0` by the convention `x / 0 = 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.gcp`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 451](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L451). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#gcp).

## Sign of the genetic causality proportion

`gcp ≥ 0` iff `q₂² ≤ q₁²`, for nonzero `q₁, q₂` with `ρ_g² = (q₁ q₂)² < 1`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.gcp_nonneg_iff`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 462](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L462). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#gcp-nonneg-iff).

## Genetic causality proportion solves the defining equation

The genetic causality proportion solves the paper's Equation 1:
`q₂² / q₁² = (ρ_g²) ^ gcp` with `ρ_g = q₁ q₂`, for nonzero `q₁, q₂` with `ρ_g² < 1`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.rpow_gcp`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 478](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L478). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#rpow-gcp).

## Genetic causality proportion is at most 1

`gcp ≤ 1` when `q₁² ≤ 1` (for nonzero `q₁, q₂` with `ρ_g² < 1`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.gcp_le_one`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 498](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L498). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#gcp-le-one).

## Genetic causality proportion is at least −1

`-1 ≤ gcp` when `q₂² ≤ 1` (for nonzero `q₁, q₂` with `ρ_g² < 1`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.neg_one_le_gcp`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 507](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L507). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#neg-one-le-gcp).

## The paper's criterion for `gcp ≥ 0`

**The paper's criterion for `gcp ≥ 0`** (O'Connor and Price 2018, after Equation 2), under
the sign condition `κ_π > 0` that it needs: if `ρ_g ≠ 0`, `ρ_g² < 1` and
`|E(α₁ α₂³)| ≤ |E(α₁³ α₂)|`, then `gcp ≥ 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.LatentCausalVariable.Model.gcp_nonneg_of_abs_moment_le`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean, line 518](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/LatentCausalVariable.lean#L518). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html#gcp-nonneg-of-abs-moment-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Latent causal variable model](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/latent-causal-variable-model/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/statistical-genetics/latent-causal-variable-model)
