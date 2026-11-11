---
declaration: section
origin: cited
lean: ProbabilityTheory.integrableOn_rpow_mul_exp_neg_mul_Ioi, ProbabilityTheory.integrable_exp_mul_gammaMeasure, ProbabilityTheory.mgf_gammaMeasure_of_lt, ProbabilityTheory.Iio_subset_integrableExpSet_gammaMeasure, ProbabilityTheory.Ioo_subset_interior_integrableExpSet_gammaMeasure, ProbabilityTheory.Gamma_add_nat_eq, ProbabilityTheory.pow_mul_rpow_sub_one, ProbabilityTheory.ae_nonneg_gammaMeasure
statement: formalized
proof: formalized
---

# Gamma distribution

27 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html).

## Integrability of the scaled gamma integrand

For real numbers $a > 0$ and $s > 0$, the
function $x \mapsto x^{a-1} e^{-sx}$ is Lebesgue integrable on the open half-line $(0, \infty)$.

This generalizes the convergence of the integral $\int_0^\infty x^{a-1} e^{-x} \, dx$ defining
$\Gamma(a)$, which is the case $s = 1$.

Formalized by `ProbabilityTheory.integrableOn_rpow_mul_exp_neg_mul_Ioi`, a theorem declared in [MathlibExt/Probability/Distributions/Gamma.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Gamma.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#integrable-on-rpow-mul-exp-neg-mul-ioi).

## Exponential moments of the gamma distribution

Let $a > 0$ and $r > 0$. For every real
$t < r$, the function $x \mapsto e^{tx}$ is integrable with respect to the gamma distribution with
shape $a$ and rate $r$.

Formalized by `ProbabilityTheory.integrable_exp_mul_gammaMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/Gamma.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Gamma.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#integrable-exp-mul-gamma-measure).

## Moment generating function of the gamma distribution

Let $a > 0$ and $r > 0$, and let
$X$ have the gamma distribution with shape $a$ and rate $r$. For every real $t < r$, the moment
generating function of $X$ at $t$ is $\mathbb{E}[e^{tX}] = \left(\frac{r}{r - t}\right)^a$.

Formalized by `ProbabilityTheory.mgf_gammaMeasure_of_lt`, a theorem declared in [MathlibExt/Probability/Distributions/Gamma.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Gamma.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#mgf-gamma-measure-of-lt).

## Half-line of exponential integrability for the gamma distribution

Let $a > 0$ and
$r > 0$, and let $S$ be the set of real $t$ such that $x \mapsto e^{tx}$ is integrable with respect
to the gamma distribution with shape $a$ and rate $r$. Then the half-line $(-\infty, r)$ is
contained in $S$.

Formalized by `ProbabilityTheory.Iio_subset_integrableExpSet_gammaMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/Gamma.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Gamma.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#iio-subset-integrable-exp-set-gamma-meas).

## A neighbourhood of zero of exponential integrability for the gamma distribution

Let
$a > 0$, $r > 0$ and $0 < \varepsilon < r$, and let $S$ be the set of real $t$ such that
$x \mapsto e^{tx}$ is integrable with respect to the gamma distribution with shape $a$ and rate
$r$. Then the interval $(-\varepsilon, \varepsilon)$ is contained in the interior of $S$.

This is the form of hypothesis used to identify a distribution from its moment generating
function on such an interval.

Formalized by `ProbabilityTheory.Ioo_subset_interior_integrableExpSet_gammaMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/Gamma.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Gamma.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#ioo-subset-interior-integrable-exp-set-g).

## Gamma function at $a + k$ via the rising factorial

`Γ(a + k) = a⁽ᵏ⁾ Γ(a)` for `a > 0`.

Formalized by `ProbabilityTheory.Gamma_add_nat_eq`, a lemma declared in [MathlibExt/Probability/Distributions/Gamma.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Gamma.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#gamma-add-nat-eq).

## $r^k r^{a-1} = r^{a+k-1}$ for nonnegative $r$

`rᵏ r^(a - 1) = r^(a + k - 1)` for `r ≥ 0` and `a > 0`.

Formalized by `ProbabilityTheory.pow_mul_rpow_sub_one`, a lemma declared in [MathlibExt/Probability/Distributions/Gamma.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Gamma.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#pow-mul-rpow-sub-one).

## Gamma law is concentrated on the nonnegative reals

The Gamma law is concentrated on `[0, ∞)`.

Formalized by `ProbabilityTheory.ae_nonneg_gammaMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/Gamma.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Gamma.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#ae-nonneg-gamma-measure).

## Integrability of $x^k e^{-cx}$ under the Gamma law

For `a, b > 0` and `c ≥ 0`, `x ↦ x ^ k e^{-c x}` is integrable for `Gamma(a, b)`.

Formalized by `ProbabilityTheory.integrable_pow_mul_exp_neg_mul_gammaMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/Gamma.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Gamma.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#integrable-pow-mul-exp-neg-mul-gamma-mea).

## Gamma integrals

For shape `a > 0`, rate `b > 0` and `c ≥ 0`,
`∫ x ^ k e^{-c x} dGamma(a, b) = a⁽ᵏ⁾ bᵃ / (b + c) ^ (a + k)`.

Formalized by `ProbabilityTheory.integral_pow_mul_exp_neg_mul_gammaMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/Gamma.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Gamma.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#integral-pow-mul-exp-neg-mul-gamma-measu).

## Gamma law has finite first moment

`x ↦ x` is integrable for `Gamma(a, b)`.

Formalized by `ProbabilityTheory.integrable_id_gammaMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/Gamma.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Gamma.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#integrable-id-gamma-measure).

## Gamma law has finite second moment

`x ↦ x²` is integrable for `Gamma(a, b)`.

Formalized by `ProbabilityTheory.integrable_sq_gammaMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/Gamma.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Gamma.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#integrable-sq-gamma-measure).

## Exponential moments of the gamma law are finite exactly below the rate

The exponential moment `E[exp (t X)]` of a gamma `(a, r)` law is finite exactly for
`t < r`.

Formalized by `ProbabilityTheory.integrableExpSet_gammaMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/Gamma.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Gamma.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#integrable-exp-set-gamma-measure).

## Moment generating function determines the gamma law

MGF uniqueness for gamma laws: a real probability law whose MGF equals the gamma `(a, r)`
MGF as a function on all of `ℝ` (both vanish where the exponential moment is infinite) is that
gamma law.

Formalized by `ProbabilityTheory.eq_gammaMeasure_of_mgf_eq`, a theorem declared in [MathlibExt/Probability/Distributions/Gamma.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Gamma.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#eq-gamma-measure-of-mgf-eq).

## Upper incomplete gamma function

The upper incomplete gamma function `Γ(a, x) = ∫_x^∞ t ^ (a - 1) e^{-t} dt` (DLMF 8.2.2).
The domain used below is `a > 0` and `x ≥ 0`, where the integral converges. Outside it the
Bochner integral may be the junk value `0` (for `a ≤ 0`, `x = 0` the integrand is not
integrable).

Formalized by `Real.upperIncompleteGamma`, a definition declared in [MathlibExt/Probability/Distributions/GammaMoments.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GammaMoments.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#upper-incomplete-gamma).

## Upper incomplete gamma function at zero

`Γ(a, 0) = Γ(a)` for `a > 0`.

Formalized by `Real.upperIncompleteGamma_zero`, a theorem declared in [MathlibExt/Probability/Distributions/GammaMoments.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GammaMoments.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#upper-incomplete-gamma-zero).

## Upper incomplete gamma function with shape one

`Γ(1, x) = e^{-x}`.

Formalized by `Real.upperIncompleteGamma_one`, a theorem declared in [MathlibExt/Probability/Distributions/GammaMoments.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GammaMoments.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#upper-incomplete-gamma-one).

## Recurrence for the upper incomplete gamma function

The recurrence `Γ(a + 1, x) = x ^ a e^{-x} + a Γ(a, x)` for `a > 0` and `x ≥ 0`
(DLMF 8.8.2), from integration by parts.

Formalized by `Real.upperIncompleteGamma_add_one`, a theorem declared in [MathlibExt/Probability/Distributions/GammaMoments.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GammaMoments.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#upper-incomplete-gamma-add-one).

## Upper incomplete gamma function at natural shapes

The closed form at natural shapes (DLMF 8.4.8): for `x ≥ 0`,
`Γ(n + 1, x) = n! e^{-x} ∑_{k = 0}^{n} x ^ k / (k!)`.

Formalized by `Real.upperIncompleteGamma_natCast_add_one`, a theorem declared in [MathlibExt/Probability/Distributions/GammaMoments.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GammaMoments.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#upper-incomplete-gamma-nat-cast-add-one).

## Real moments of the gamma law

Real moments of the gamma law: for shape `a > 0`, rate `r > 0` and `p > -a`,
`E[X ^ p] = Γ(a + p) / (Γ(a) r ^ p)`. (The law is carried by `[0, ∞)`, so the values of
`x ^ p` for `x < 0` play no role.)

Formalized by `ProbabilityTheory.integral_rpow_gammaMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/GammaMoments.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GammaMoments.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#integral-rpow-gamma-measure).

## Mean of the gamma law

The mean of the gamma law with shape `a > 0` and rate `r > 0` is `a / r`.

Formalized by `ProbabilityTheory.integral_id_gammaMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/GammaMoments.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GammaMoments.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#integral-id-gamma-measure).

## Second moment of the gamma law

The second moment of the gamma law with shape `a > 0` and rate `r > 0` is
`a (a + 1) / r ^ 2`.

Formalized by `ProbabilityTheory.integral_sq_gammaMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/GammaMoments.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GammaMoments.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#integral-sq-gamma-measure).

## Gamma law has finite second moment

The gamma law has finite second moment.

Formalized by `ProbabilityTheory.memLp_id_gammaMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/GammaMoments.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GammaMoments.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#mem-lp-id-gamma-measure).

## Variance of the gamma law

The variance of the gamma law with shape `a > 0` and rate `r > 0` is `a / r ^ 2`.

Formalized by `ProbabilityTheory.variance_id_gammaMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/GammaMoments.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GammaMoments.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#variance-id-gamma-measure).

## Scaling a gamma random variable

Scaling a gamma variable by `c > 0` keeps its shape and divides its rate by `c`:
`c X ~ Gamma(a, r / c)` when `X ~ Gamma(a, r)`.

Formalized by `ProbabilityTheory.gammaMeasure_map_const_mul`, a theorem declared in [MathlibExt/Probability/Distributions/GammaMoments.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GammaMoments.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#gamma-measure-map-const-mul).

## Upper tail of the gamma law

The upper tail of the gamma law: `P(X > c) = Γ(a, r c) / Γ(a)` for `c ≥ 0`.

Formalized by `ProbabilityTheory.gammaMeasure_real_Ioi`, a theorem declared in [MathlibExt/Probability/Distributions/GammaMoments.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GammaMoments.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#gamma-measure-real-ioi).

## Erlang tail formula

The Erlang tail: for shape `n + 1`, `P(X > c) = e^{-r c} ∑_{k = 0}^{n} (r c) ^ k / (k!)`
when `c ≥ 0`.

Formalized by `ProbabilityTheory.gammaMeasure_real_Ioi_natCast_add_one`, a theorem declared in [MathlibExt/Probability/Distributions/GammaMoments.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GammaMoments.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html#gamma-measure-real-ioi-nat-cast-add-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gamma distribution](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/gamma-distribution/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/distributions/gamma-distribution)
