---
declaration: section
origin: cited
lean: ProbabilityTheory.binomProbHalf, ProbabilityTheory.gaussianApproxHalf, ProbabilityTheory.localDMLIndex, ProbabilityTheory.localDMLIndex_tendsto_atTop, ProbabilityTheory.n_sub_localDMLIndex_tendsto_atTop, ProbabilityTheory.localDMLIndex_ratio_half, ProbabilityTheory.factorial_eq_stirlingSeq_mul, ProbabilityTheory.binomProb_div_gaussianApprox_eq
statement: formalized
proof: formalized
---

# Local de Moivre–Laplace theorem

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/local-de-moivre-laplace-theorem/index.html).

## Binomial point mass with success probability one half

The point mass `P(B_n = k) = C(n,k) / 2ⁿ` for a `Binomial(n, 1/2)` success count `B_n`.

Formalized by `ProbabilityTheory.binomProbHalf`, a definition declared in [MathlibExt/Probability/LocalDeMoivreLaplace.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/LocalDeMoivreLaplace.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/local-de-moivre-laplace-theorem/index.html#binom-prob-half).

## Gaussian approximation to the symmetric binomial point mass

The Gaussian (local CLT) approximation to `binomProbHalf n k`,
`√(2/(π n)) · exp(-(k - n/2)² / (n/2))`.

Formalized by `ProbabilityTheory.gaussianApproxHalf`, a definition declared in [MathlibExt/Probability/LocalDeMoivreLaplace.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/LocalDeMoivreLaplace.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/local-de-moivre-laplace-theorem/index.html#gaussian-approx-half).

## Lattice index in the local De Moivre–Laplace theorem

The integer index `k = ⌊n/2 + x·√n/2⌋` corresponding to the parameter `x` in the local
DeMoivre–Laplace statement: it picks the lattice point near `n/2 + x √n / 2`, so that
`(2k - n)/√n ≈ x`.

Formalized by `ProbabilityTheory.localDMLIndex`, a definition declared in [MathlibExt/Probability/LocalDeMoivreLaplace.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/LocalDeMoivreLaplace.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/local-de-moivre-laplace-theorem/index.html#local-dmlindex).

## The De Moivre–Laplace index tends to infinity

The index `localDMLIndex x n` tends to infinity as `n → ∞`, for any fixed `x : ℝ`.

Formalized by `ProbabilityTheory.localDMLIndex_tendsto_atTop`, a lemma declared in [MathlibExt/Probability/LocalDeMoivreLaplace.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/LocalDeMoivreLaplace.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/local-de-moivre-laplace-theorem/index.html#local-dmlindex-tendsto-at-top).

## The complementary De Moivre–Laplace index tends to infinity

The complementary index `n - localDMLIndex x n` also tends to infinity, so both `k` and
`n - k` are eventually arbitrarily large.

Formalized by `ProbabilityTheory.n_sub_localDMLIndex_tendsto_atTop`, a lemma declared in [MathlibExt/Probability/LocalDeMoivreLaplace.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/LocalDeMoivreLaplace.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/local-de-moivre-laplace-theorem/index.html#n-sub-local-dmlindex-tendsto-at-top).

## The De Moivre–Laplace index over n tends to one half

The ratio `localDMLIndex x n / n` tends to `1/2` as `n → ∞`, because the correction
`x √n / 2` is `o(n)`.

Formalized by `ProbabilityTheory.localDMLIndex_ratio_half`, a lemma declared in [MathlibExt/Probability/LocalDeMoivreLaplace.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/LocalDeMoivreLaplace.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/local-de-moivre-laplace-theorem/index.html#local-dmlindex-ratio-half).

## Factorial in terms of the Stirling sequence

Rewriting of `m!` in terms of Mathlib's `Stirling.stirlingSeq`:
`m! = stirlingSeq(m) · √(2m) · (m/e)^m`.

Formalized by `ProbabilityTheory.factorial_eq_stirlingSeq_mul`, a lemma declared in [MathlibExt/Probability/LocalDeMoivreLaplace.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/LocalDeMoivreLaplace.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/local-de-moivre-laplace-theorem/index.html#factorial-eq-stirling-seq-mul).

## Stirling decomposition of the binomial-to-Gaussian ratio

Algebraic rewriting of the ratio `binomProbHalf n k / gaussianApproxHalf n k` using
Stirling's formula, separating it into a Stirling-sequence factor, a square-root factor,
a power-of-`n` factor, and an exponential correction.

Formalized by `ProbabilityTheory.binomProb_div_gaussianApprox_eq`, a lemma declared in [MathlibExt/Probability/LocalDeMoivreLaplace.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/LocalDeMoivreLaplace.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/local-de-moivre-laplace-theorem/index.html#binom-prob-div-gaussian-approx-eq).

## Cubic bound on the symmetric entropy residual

Third-order Taylor bound for the symmetric entropy expansion:
`|(1+u) log(1+u) + (1-u) log(1-u) - u²| ≤ 6 |u|³` whenever `|u| < 1/2`. Used to control the
deviation of the binomial coefficient from its Gaussian approximation.

Formalized by `ProbabilityTheory.entropy_residual_bound`, a lemma declared in [MathlibExt/Probability/LocalDeMoivreLaplace.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/LocalDeMoivreLaplace.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/local-de-moivre-laplace-theorem/index.html#entropy-residual-bound).

## Deviation bound for the De Moivre–Laplace index

Eventually, the deviation `|2k - n|` for `k = localDMLIndex x n` is at most `|x| √n + 2`,
since `k = ⌊n/2 + x √n / 2⌋`.

Formalized by `ProbabilityTheory.localDMLIndex_deviation_bound`, a lemma declared in [MathlibExt/Probability/LocalDeMoivreLaplace.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/LocalDeMoivreLaplace.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/local-de-moivre-laplace-theorem/index.html#local-dmlindex-deviation-bound).

## Logarithm of the binomial power factor

Identity rewriting the logarithm of the power factor `nⁿ / (kᵏ (n-k)^{n-k} 2ⁿ)` plus the
Gaussian exponent `(k - n/2)² / (n/2)` as `-(n/2) · ((1+u) log(1+u) + (1-u) log(1-u) - u²)`,
where `u = (2k - n)/n`. This combines the log-binomial expansion with the Gaussian correction.

Formalized by `ProbabilityTheory.log_power_factor_formula`, a lemma declared in [MathlibExt/Probability/LocalDeMoivreLaplace.lean, line 404](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/LocalDeMoivreLaplace.lean#L404). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/local-de-moivre-laplace-theorem/index.html#log-power-factor-formula).

## Binomial point mass is equivalent to a fixed Gaussian value

For any binomial success-index sequence whose standardized displacement converges to
`x`, the point mass is equivalent to the Gaussian expression evaluated at the fixed limit `x`.
The number of trials may follow any natural-valued sequence tending to infinity.

Formalized by `ProbabilityTheory.binomProbHalf_isEquivalent_fixedGaussian`, a theorem declared in [MathlibExt/Probability/LocalDeMoivreLaplace.lean, line 655](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/LocalDeMoivreLaplace.lean#L655). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/local-de-moivre-laplace-theorem/index.html#binom-prob-half-is-equivalent-fixed-gaus).

## Local limit theorem for the simple random walk

The source's random-walk local limit theorem: every integer displacement sequence with
`2 kₙ / √(2n) → x` has point mass equivalent to `(√(π n))⁻¹ exp(-x²/2)`.
The scaling hypothesis itself implies that `n + kₙ` is a valid success index eventually.

Formalized by `ProbabilityTheory.local_deMoivreLaplace_half_of_tendsto`, a theorem declared in [MathlibExt/Probability/LocalDeMoivreLaplace.lean, line 680](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/LocalDeMoivreLaplace.lean#L680). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/local-de-moivre-laplace-theorem/index.html#local-de-moivre-laplace-half-of-tendsto).

## Standardized displacement of the rounded index converges

The rounded success index has standardized displacement converging to `x`.

Formalized by `ProbabilityTheory.localDMLIndex_standardized_tendsto`, a lemma declared in [MathlibExt/Probability/LocalDeMoivreLaplace.lean, line 727](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/LocalDeMoivreLaplace.lean#L727). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/local-de-moivre-laplace-theorem/index.html#local-dmlindex-standardized-tendsto).

## The corrected binomial power factor tends to one

The product of the power factor `nⁿ / (kᵏ (n-k)^{n-k} 2ⁿ)` with the Gaussian correction
`exp((k - n/2)² / (n/2))`, evaluated at `k = localDMLIndex x n`, tends to `1` as `n → ∞`.
This is the key analytic estimate behind the local DeMoivre–Laplace limit theorem.

Formalized by `ProbabilityTheory.dml_power_factor_tendsto_one`, a lemma declared in [MathlibExt/Probability/LocalDeMoivreLaplace.lean, line 759](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/LocalDeMoivreLaplace.lean#L759). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/local-de-moivre-laplace-theorem/index.html#dml-power-factor-tendsto-one).

## The complementary index over n tends to one half

Companion to `localDMLIndex_ratio_half`: the ratio `(n - k) / n` for `k = localDMLIndex x n`
also tends to `1/2`.

Formalized by `ProbabilityTheory.n_sub_localDMLIndex_ratio_half`, a lemma declared in [MathlibExt/Probability/LocalDeMoivreLaplace.lean, line 769](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/LocalDeMoivreLaplace.lean#L769). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/local-de-moivre-laplace-theorem/index.html#n-sub-local-dmlindex-ratio-half).

## Binomial point mass is equivalent to its Gaussian approximation

The binomial point mass and its Gaussian approximation are asymptotically equivalent along
the sequence `k = localDMLIndex x n`:
`binomProbHalf n k ~ gaussianApproxHalf n k` as `n → ∞`. Combines Stirling's formula with the
power-factor and entropy estimates.

Formalized by `ProbabilityTheory.binomProbHalf_isEquivalent_gaussianApproxHalf`, a theorem declared in [MathlibExt/Probability/LocalDeMoivreLaplace.lean, line 788](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/LocalDeMoivreLaplace.lean#L788). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/local-de-moivre-laplace-theorem/index.html#binom-prob-half-is-equivalent-gaussian-a).

## Local De Moivre–Laplace theorem for $p = 1/2$

Canonical rounded-sequence corollary of the local De Moivre–Laplace theorem: for any
`x ∈ ℝ`, the binomial point mass divided by its moving Gaussian approximation along
`localDMLIndex x` tends to `1`. The arbitrary integer-displacement statement with the fixed
Gaussian value at `x` is `local_deMoivreLaplace_half_of_tendsto`.

Formalized by `ProbabilityTheory.local_deMoivreLaplace_half`, a theorem declared in [MathlibExt/Probability/LocalDeMoivreLaplace.lean, line 804](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/LocalDeMoivreLaplace.lean#L804). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/local-de-moivre-laplace-theorem/index.html#local-de-moivre-laplace-half).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Local de Moivre–Laplace theorem](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/local-de-moivre-laplace-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/central-limit-theorems/local-de-moivre-laplace-theorem)
