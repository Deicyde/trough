---
declaration: section
origin: cited
lean: StatMech.Probability.ptn_val, StatMech.Probability.ptn_sigma, StatMech.Probability.ptn_psi, StatMech.Probability.ptn_expect_prod, StatMech.Probability.ptn_pchar, StatMech.Probability.ptn_orthonormal, StatMech.Probability.ptn_coeff, StatMech.Probability.ptn_expansion
statement: formalized
proof: formalized
---

# PBiased Tensorize

31 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html).

## Zero-one value of a bit

The `0/1` value of a bit.

Formalized by `StatMech.Probability.ptn_val`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-val).

## Standard deviation of a Bernoulli bit

The standard deviation `√(p(1-p))` of a Bernoulli(`p`) bit.

Formalized by `StatMech.Probability.ptn_sigma`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-sigma).

## Normalized Bernoulli bit

The normalized Bernoulli(`p`) bit `ψ(b) = (b - p) / √(p(1-p))`, which has mean `0` and variance
 `1`.

Formalized by `StatMech.Probability.ptn_psi`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-psi).

## Expectations of product functions factor under product measure

Expectations of product functions factor under the product measure.

Formalized by `StatMech.Probability.ptn_expect_prod`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-expect-prod).

## $p$-biased character

The `p`-biased character `φ_S(ω) = ∏_{i ∈ S} ψ(ω i)`.

Formalized by `StatMech.Probability.ptn_pchar`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-pchar).

## Orthonormality of the $p$-biased characters

The `p`-biased characters are orthonormal in `L²(μ_p)`.

Formalized by `StatMech.Probability.ptn_orthonormal`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-orthonormal).

## $p$-biased Fourier coefficient

The `p`-biased Fourier coefficient `f̂(S) = 𝔼_p[f φ_S]`.

Formalized by `StatMech.Probability.ptn_coeff`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-coeff).

## $p$-biased Fourier inversion

Fourier inversion under `μ_p`: `f = ∑_S f̂(S) φ_S` for `0 < p < 1`.

Formalized by `StatMech.Probability.ptn_expansion`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-expansion).

## Parseval's identity under the $p$-biased measure

Parseval's identity under `μ_p`: `𝔼_p[f g] = ∑_S f̂(S) ĝ(S)`.

Formalized by `StatMech.Probability.ptn_parseval`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-parseval).

## $p$-biased variance as Fourier weight off the empty set

The variance under `μ_p` is the Fourier weight off the empty set.

Formalized by `StatMech.Probability.ptn_var_eq_fourierWeight`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-var-eq-fourier-weight).

## $p$-biased influence of a coordinate as Fourier weight

The influence of `e` on a Boolean function under `μ_p` is `∑_{S ∋ e} f̂(S)² / (p(1-p))`.

Formalized by `StatMech.Probability.ptn_infl_eq_fourierWeight`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-infl-eq-fourier-weight).

## $p$-biased total influence as Fourier weight

The total influence of a Boolean function under `μ_p` is `∑_S |S| f̂(S)² / (p(1-p))`.

Formalized by `StatMech.Probability.ptn_totalInfl_eq_fourierWeight`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 438](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-total-infl-eq-fourier-weight).

## $q$-th moment under the $p$-biased measure

The `q`-th moment `𝔼_p |f|^q`.

Formalized by `StatMech.Probability.ptn_qnormPow`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-qnorm-pow).

## $L^q$ norm under the $p$-biased measure

The `L^q(μ_p)` norm `(𝔼_p |f|^q)^{1/q}`.

Formalized by `StatMech.Probability.ptn_qnorm`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 462](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L462). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-qnorm).

## $p$-biased noise operator on the Fourier side

The `p`-biased noise operator on the Fourier side: `T_ρ f = ∑_S ρ^{|S|} f̂(S) φ_S`.

Formalized by `StatMech.Probability.ptn_noiseOp`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 485](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L485). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-noise-op).

## One-coordinate $p$-biased noise kernel

The one-coordinate noise kernel: keep the bit with probability `ρ`, otherwise resample it from
 Bernoulli(`p`).

Formalized by `StatMech.Probability.ptn_kbit`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 557](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L557). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-kbit).

## Product noise kernel on the Boolean cube

The product noise kernel on `{0, 1}^ι`.

Formalized by `StatMech.Probability.ptn_kernel`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 561](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L561). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-kernel).

## $p$-biased noise operator via its Markov kernel

The `p`-biased noise operator `T_ρ f (x) = ∑_y K_ρ(x, y) f y`, defined by its Markov kernel.

Formalized by `StatMech.Probability.ptn_kop`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 565](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L565). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-kop).

## Kernel and Fourier noise operators agree

The kernel and Fourier definitions of the `p`-biased noise operator agree for `0 < p < 1`.

Formalized by `StatMech.Probability.ptn_kop_eq_noiseOp`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 613](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L613). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-kop-eq-noise-op).

## Tensorization step for $p$-biased hypercontractivity

Induction step of the tensorization: hypercontractivity on `{0, 1}^n` implies it on `{0,
 1}^{n+1}`.

Formalized by `StatMech.Probability.ptn_tensorStep`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 768](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L768). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-tensor-step).

## $p$-biased hypercontractivity on $\{0, 1\}^n$

`p`-biased hypercontractivity on `{0, 1}^n`: `‖T_ρ f‖₂ ≤ ‖f‖_q` for `0 < p < 1`, `1 ≤ q ≤ 2` and
 `ρ² = 4p(1-p)(q - 1)`. The noise rate is not optimal for `p ≠ 1/2`.

Formalized by `StatMech.Probability.ptn_hypercontractivity_fin`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 880](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L880). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-hypercontractivity-fin).

## Fourier form of $p$-biased hypercontractivity on $\{0, 1\}^n$

Fourier form of `ptn_hypercontractivity_fin` on `{0, 1}^n`.

Formalized by `StatMech.Probability.ptn_lowDegreeWeight_fin`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 891](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L891). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-low-degree-weight-fin).

## Fourier form of $p$-biased hypercontractivity on finite index types

`p`-biased hypercontractivity in Fourier form on any finite index type: `∑_S ρ^{2|S|} f̂(S)² ≤
 ‖f‖_q²` for `ρ² = 4p(1-p)(q - 1)`.

Formalized by `StatMech.Probability.ptn_lowDegreeWeight`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 954](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L954). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-low-degree-weight).

## $p$-biased hypercontractivity for a discrete derivative

`p`-biased hypercontractivity applied to the discrete derivative `∂ₑ 1_A`.

Formalized by `StatMech.Probability.ptn_perCoord_hc`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 1026](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L1026). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-per-coord-hc).

## Summed per-coordinate $p$-biased hypercontractive bound

`ptn_perCoord_hc` summed over all coordinates.

Formalized by `StatMech.Probability.ptn_summed_hc`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 1043](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L1043). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-summed-hc).

## Capped per-coordinate estimate under the $p$-biased measure

The capped per-coordinate estimate under `μ_p`: `(1/(p(1-p))) ∑_S |S| ρ^{2(|S|-1)} f̂(S)² ≤
 δ^{2/q - 1} ∑ₑ Infₑ`, with `δ = maxₑ Infₑ`.

Formalized by `StatMech.Probability.ptn_capped_hc`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 1109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L1109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-capped-hc).

## $p$-biased KKL inequality conditional on the capped estimate

The KKL inequality with constant `2` for every `p ∈ (1/2, q)` with `p < 1`, with the capped
 estimate `ptn_capped_hc` as a hypothesis.

Formalized by `StatMech.Probability.ptn_RhoOptimise`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 1120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L1120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-rho-optimise).

## Conditional $p$-biased KKL statement yields KKL with constant $2$

`ptn_RhoOptimise q` gives the KKL inequality with constant `2` at every `p ∈ (1/2, q)`.

Formalized by `StatMech.Probability.ptn_kklHC_of_rhoOptimise`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 1133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L1133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-kkl-hc-of-rho-optimise).

## Conditional KKL gives KKL with constant 2 on $(1/2, q)$ for $q \le 1$

`ptn_RhoOptimise q` implies `kpb_PBiasedHC q`.

Formalized by `StatMech.Probability.ptn_PBiasedHC_of_rhoOptimise`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 1141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L1141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-pbiased-hc-of-rho-optimise).

## Trivial KKL inequality with constant $0$

The KKL inequality with constant `0` holds trivially.

Formalized by `StatMech.Probability.ptn_rhoOptimise_c0`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 1146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L1146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-rho-optimise-c0).

## Sharp-threshold bound from the conditional KKL statement

The sharp-threshold bound `kpb_sharpThreshold` under `ptn_RhoOptimise q`.

Formalized by `StatMech.Probability.ptn_sharpThreshold_of_rhoOptimise`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean, line 1155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/PBiasedTensorize.lean#L1155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html#ptn-sharp-threshold-of-rho-optimise).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: PBiased Tensorize](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/concentration-inequalities/bonami-beckner-hypercontractivity/pbiased-tensorize)
