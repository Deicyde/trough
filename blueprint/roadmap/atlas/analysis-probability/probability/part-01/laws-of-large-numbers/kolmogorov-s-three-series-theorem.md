---
declaration: section
origin: cited
lean: ProbabilityTheory.eLpNorm_one_le_sqrt_integral_sq, ProbabilityTheory.ae_tendsto_sum_of_indep_centered_L1bdd, ProbabilityTheory.KolmogorovThreeSeries.truncatedRV, ProbabilityTheory.KolmogorovThreeSeries.truncatedRV_apply, ProbabilityTheory.KolmogorovThreeSeries.measurable_truncatedRV, ProbabilityTheory.KolmogorovThreeSeries.iIndepFun_truncatedRV, ProbabilityTheory.KolmogorovThreeSeries.abs_truncatedRV_le, ProbabilityTheory.KolmogorovThreeSeries.abs_truncatedRV_le_abs
statement: formalized
proof: formalized
---

# Kolmogorov's three-series theorem

39 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html).

## $L^1$ norm bounded by the square root of the second moment

If `∫ ‖f‖² dμ ≤ C` for an `L²` function on a probability space, then
`‖f‖₁ ≤ √C`.

Formalized by `ProbabilityTheory.eLpNorm_one_le_sqrt_integral_sq`, a lemma declared in [MathlibExt/Probability/KolmogorovThreeSeries.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovThreeSeries.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#e-lp-norm-one-le-sqrt-integral-sq).

## Almost-sure convergence of L¹-bounded sums of independent centered variables

Let
$Z_0, Z_1, \dots$ be independent integrable real random variables on a probability space with
$E[Z_n] = 0$ for every $n$, and let $S_n = \sum_{k \le n} Z_k$. If there is a constant $R \ge 0$
with $E|S_n| \le R$ for every $n$, then $S_n$ converges almost surely to a finite limit.

This is a key step toward the Kolmogorov three-series theorem: $(S_n)$ is a martingale for the
natural filtration, so the $L^1$-bounded martingale convergence theorem applies.

Formalized by `ProbabilityTheory.ae_tendsto_sum_of_indep_centered_L1bdd`, a theorem declared in [MathlibExt/Probability/KolmogorovThreeSeries.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovThreeSeries.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#ae-tendsto-sum-of-indep-centered-l1bdd).

## Truncation of a random variable

For a sequence $X_0, X_1, \dots$ of real-valued functions
on $\Omega$, a threshold $A \in \mathbb{R}$ and an index $n$, the truncation of $X_n$ at $A$ is
$Y_n = X_n \mathbf{1}_{\{|X_n| \le A\}}$, that is, $Y_n(\omega) = X_n(\omega)$ when
$|X_n(\omega)| \le A$ and $Y_n(\omega) = 0$ otherwise.

This is the key construction in the Kolmogorov three-series theorem.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.truncatedRV`, a definition declared in [MathlibExt/Probability/KolmogorovThreeSeries.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovThreeSeries.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#truncated-rv).

## Formula for the truncated random variable

The canonical truncation is the identity inside the cutoff and zero outside it.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.truncatedRV_apply`, a theorem declared in [MathlibExt/Probability/KolmogorovThreeSeries.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovThreeSeries.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#truncated-rv-apply).

## Truncation preserves measurability

The canonical truncation of a measurable random variable is measurable.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.measurable_truncatedRV`, a theorem declared in [MathlibExt/Probability/KolmogorovThreeSeries.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovThreeSeries.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#measurable-truncated-rv).

## Truncation preserves independence

Truncation preserves independence.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.iIndepFun_truncatedRV`, a theorem declared in [MathlibExt/Probability/KolmogorovThreeSeries.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovThreeSeries.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#i-indep-fun-truncated-rv).

## Truncation is bounded by a nonnegative cutoff

A canonical truncation is bounded by a nonnegative cutoff in absolute value.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.abs_truncatedRV_le`, a theorem declared in [MathlibExt/Probability/KolmogorovThreeSeries.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovThreeSeries.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#abs-truncated-rv-le).

## Truncation is bounded by the absolute cutoff

A canonical truncation is bounded by the absolute value of any cutoff.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.abs_truncatedRV_le_abs`, a theorem declared in [MathlibExt/Probability/KolmogorovThreeSeries.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovThreeSeries.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#abs-truncated-rv-le-abs).

## Truncation fixes values within the cutoff

Truncation fixes points inside or on the cutoff.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.truncatedRV_eq_of_abs_le`, a theorem declared in [MathlibExt/Probability/KolmogorovThreeSeries.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovThreeSeries.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#truncated-rv-eq-of-abs-le).

## Almost sure convergence of centered truncated sums

If the truncated variables have summable variances, then almost surely
the partial sums of the centered truncations converge:
`∑ (Yᵢ - E[Yᵢ])` converges a.s.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.ae_tendsto_centered_of_indep_summableVar`, a theorem declared in [MathlibExt/Probability/KolmogorovThreeSeries.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovThreeSeries.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#ae-tendsto-centered-of-indep-summable-va).

## Truncations eventually agree with the variables

Let $X_0, X_1, \dots$ be real-valued
functions on a probability space $(\Omega, P)$, let $A$ be a real number, and let
$Y_n = X_n \mathbf{1}_{\{|X_n| \le A\}}$ be the truncation of $X_n$ at $A$. If
$\sum_n P(|X_n| > A) < \infty$, then for almost every $\omega$ we have $X_n(\omega) = Y_n(\omega)$
for all sufficiently large $n$.

This follows from the first Borel–Cantelli lemma.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.ae_eventually_truncation_eq`, a theorem declared in [MathlibExt/Probability/KolmogorovThreeSeries.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovThreeSeries.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#ae-eventually-truncation-eq).

## Eventually equal series inherit almost-everywhere convergence

Let $\mu$ be a measure on
$\Omega$ and let $f_n, g_n : \Omega \to \mathbb{R}$ ($n \ge 0$) be functions such that for
$\mu$-almost every $\omega$ we have $f_n(\omega) = g_n(\omega)$ for all sufficiently large $n$. If
there is a function $S : \Omega \to \mathbb{R}$ with $\sum_{i < n} f_i(\omega) \to S(\omega)$ as
$n \to \infty$ for $\mu$-almost every $\omega$, then there is a function $T : \Omega \to \mathbb{R}$
with $\sum_{i < n} g_i(\omega) \to T(\omega)$ as $n \to \infty$ for $\mu$-almost every $\omega$.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.ae_tendsto_of_ae_eventually_eq_and_ae_tendsto`, a theorem declared in [MathlibExt/Probability/KolmogorovThreeSeries.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovThreeSeries.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#ae-tendsto-of-ae-eventually-eq-and-ae-te).

## Truncated sums converge almost surely

Let $X_0, X_1, \dots$ be independent real random
variables on a probability space $(\Omega, P)$, let $A > 0$, and let
$Y_n = X_n \mathbf{1}_{\{|X_n| \le A\}}$ be the truncation of $X_n$ at $A$. If the series
$\sum_n E[Y_n]$ converges absolutely and $\sum_n \operatorname{Var}(Y_n) < \infty$, then there is
a function $S : \Omega \to \mathbb{R}$ with $\sum_{i < n} Y_i(\omega) \to S(\omega)$ as
$n \to \infty$ for almost every $\omega$.

This combines the convergence of the centered truncated sums with the convergence of the series
of means.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.ae_tendsto_truncated_of_conditions`, a theorem declared in [MathlibExt/Probability/KolmogorovThreeSeries.lean, line 413](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovThreeSeries.lean#L413). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#ae-tendsto-truncated-of-conditions).

## Kolmogorov's three-series theorem (sufficiency direction)

Let $X_0, X_1, \dots$ be
independent real random variables on a probability space $(\Omega, P)$, fix $A > 0$, and write
$Y_n = X_n \mathbf{1}_{\{|X_n| \le A\}}$ for the truncations. If
$\sum_n P(|X_n| > A) < \infty$, the series $\sum_n E[Y_n]$ converges absolutely, and
$\sum_n \operatorname{Var}(Y_n) < \infty$, then there is a function $S : \Omega \to \mathbb{R}$
with $\sum_{i < n} X_i(\omega) \to S(\omega)$ as $n \to \infty$ for almost every $\omega$; that
is, $\sum_n X_n$ converges almost surely.

The classical theorem only requires the series $\sum_n E[Y_n]$ to converge; here it must converge
absolutely.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.kolmogorov_three_series_sufficiency`, a theorem declared in [MathlibExt/Probability/KolmogorovThreeSeries.lean, line 450](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovThreeSeries.lean#L450). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#kolmogorov-three-series-sufficiency).

## Kolmogorov three-series theorem, necessity, first series

Let $(X_n)_{n \ge 0}$ be a
sequence of independent measurable real random variables on a probability space
$(\Omega, \mu)$ whose partial sums converge almost surely: there is a function
$S : \Omega \to \mathbb{R}$ such that $\sum_{i < n} X_i(\omega) \to S(\omega)$ as $n \to \infty$
for $\mu$-almost every $\omega$. Then for every $A > 0$ the tail probabilities are summable:
$\sum_n \mu(\{\omega : |X_n(\omega)| > A\}) < \infty$.

Proof: argue by contradiction via the second Borel–Cantelli lemma. If the tail probabilities
summed to $\infty$, the events $\{|X_n| > A\}$ would occur infinitely often with probability
one; but almost-sure convergence of the partial sums forces $X_n \to 0$ almost surely, hence
eventually $|X_n| \le A$.

Formalized by `ProbabilityTheory.summable_tail_prob_of_ae_tendsto`, a theorem declared in [MathlibExt/Probability/ThreeSeriesTailProb.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ThreeSeriesTailProb.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#summable-tail-prob-of-ae-tendsto).

## Divergent tail probabilities prevent almost-sure convergence of partial sums

Let
$(X_n)_{n \ge 0}$ be a sequence of independent measurable real random variables on a probability
space $(\Omega, \mu)$, and let $A > 0$. If $\sum_n \mu(\{\omega : |X_n(\omega)| > A\}) = \infty$,
then there is no function $S : \Omega \to \mathbb{R}$ such that, for $\mu$-almost every $\omega$,
the partial sums $\sum_{i < n} X_i(\omega)$ converge to $S(\omega)$ as $n \to \infty$.

Formalized by `ProbabilityTheory.not_ae_tendsto_partial_sum_of_tsum_tail_prob_eq_top`, a theorem declared in [MathlibExt/Probability/ThreeSeriesTailProb.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ThreeSeriesTailProb.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#not-ae-tendsto-partial-sum-of-tsum-tail).

## Pair of coordinates from two independent copies

The pair of the `n`-th coordinates of two independent copies.

Formalized by `MathlibExt.Probability.ThreeSeriesNecessity.pairRV`, a definition declared in [MathlibExt/Probability/ThreeSeriesNecessity.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ThreeSeriesNecessity.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#pair-rv).

## Symmetrized random variable

The symmetrized variable `Z n (ω, ω') = Y n ω - Y n ω'`.

Formalized by `MathlibExt.Probability.ThreeSeriesNecessity.symmRV`, a definition declared in [MathlibExt/Probability/ThreeSeriesNecessity.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ThreeSeriesNecessity.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#symm-rv).

## Expectation of a product of independent functions factors

If `f` and `g` are independent, the expectation of a product of functions of
`f` and `g` factors.

Formalized by `MathlibExt.Probability.ThreeSeriesNecessity.integral_mul_of_indep_comp`, a theorem declared in [MathlibExt/Probability/ThreeSeriesNecessity.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ThreeSeriesNecessity.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#integral-mul-of-indep-comp).

## Fourth-moment bound for sums of bounded independent variables

Fourth-moment induction for sums of independent centered bounded random
variables: `E[S⁴] ≤ 3 E[S²]² + B² E[S²]`, together with the variance-of-sum
identity and `E[S] = 0`.

Formalized by `MathlibExt.Probability.ThreeSeriesNecessity.integral_pow_four_le`, a theorem declared in [MathlibExt/Probability/ThreeSeriesNecessity.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ThreeSeriesNecessity.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#integral-pow-four-le).

## Three-series necessity, second half of the variance step

For a
uniformly bounded independent sequence whose partial sums converge almost
surely, the variances are summable. Proved by symmetrization: the
symmetrized sums are centered, so Paley–Zygmund gives a uniform lower
bound on block-tail probabilities, contradicting convergence in
measure unless the variances are summable.

Formalized by `MathlibExt.Probability.ThreeSeriesNecessity.summable_variance_of_bounded_ae_tendsto`, a theorem declared in [MathlibExt/Probability/ThreeSeriesNecessity.lean, line 511](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ThreeSeriesNecessity.lean#L511). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#summable-variance-of-bounded-ae-tendsto).

## Mean step of three-series necessity

For a uniformly bounded
independent sequence with summable variances whose partial sums converge
almost surely, the partial sums of the means converge (to some limit).
Proved by centering and applying the canonical centered-sum convergence
theorem with an `L¹` bound from the total variance. The mean partial sums
are the difference of the two convergent series at a single sample point.

Formalized by `MathlibExt.Probability.ThreeSeriesNecessity.tendsto_sum_integral_of_bounded_ae_tendsto`, a theorem declared in [MathlibExt/Probability/ThreeSeriesNecessity.lean, line 940](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ThreeSeriesNecessity.lean#L940). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#tendsto-sum-integral-of-bounded-ae-tends).

## Kolmogorov three-series necessity, series (2)–(3)

If the partial
sums of an independent sequence `Xₙ` converge almost surely, then for
every `A > 0` the truncations `Yₙ = Xₙ · 1_{|Xₙ| ≤ A}` have convergent
mean partial sums and summable variances. This is the corrected form of
v1's `summable_mean_and_variance_of_ae_tendsto_ax`: v1 claimed the means
themselves are `Summable`, which is false (see
`summable_mean_necessity_false`); only convergence of the mean partial
sums holds. Series (1) uses the public theorem from
`ThreeSeriesTailProb`.

Formalized by `MathlibExt.Probability.ThreeSeriesNecessity.three_series_necessity_mean_variance`, a theorem declared in [MathlibExt/Probability/ThreeSeriesNecessity.lean, line 1094](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ThreeSeriesNecessity.lean#L1094). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#three-series-necessity-mean-variance).

## The `Summable`-means necessity claim in v1 is false

The
deterministic sequence `X k ω = (-1)^k / (k + 1)` on the one-point
probability space `(Unit, dirac ())` has converging partial sums, is
constant (hence measurable and independent), agrees with its truncations
at `A = 1`, and has all variances `0` — yet its means
`∫ truncatedRV X 1 k = (-1)^k / (k + 1)` are not `Summable`, since
`Summable.abs` would force summability of the harmonic series. This is
why the ported necessity theorem above states convergence of the mean
partial sums rather than `Summable` of the means. The statement records
convergence of both the original and the truncated partial sums: the
truncated form is the hypothesis of v1's (false) unproved lemma, and the original
form is what the corrected assembly theorem needs.

Formalized by `MathlibExt.Probability.ThreeSeriesNecessity.summable_mean_necessity_false`, a theorem declared in [MathlibExt/Probability/ThreeSeriesNecessity.lean, line 1126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ThreeSeriesNecessity.lean#L1126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#summable-mean-necessity-false).

## Scalar truncation function

Scalar truncation is canonical truncation of the identity sequence.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.truncationFun`, an abbreviation declared in [MathlibExt/Probability/Truncation.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Truncation.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#truncation-fun).

## Truncation vanishes outside the closed band

Truncation of a value strictly outside the closed band is zero.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.truncatedRV_eq_zero_of_abs_gt`, a theorem declared in [MathlibExt/Probability/Truncation.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Truncation.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#truncated-rv-eq-zero-of-abs-gt).

## Canonical truncation preserves nonnegativity

Canonical truncation preserves nonnegativity.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.truncatedRV_nonneg_of_nonneg`, a theorem declared in [MathlibExt/Probability/Truncation.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Truncation.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#truncated-rv-nonneg-of-nonneg).

## Scalar truncation fixes values within the cutoff

Scalar truncation fixes values inside or on the cutoff.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.truncationFun_eq_self_of_abs_le`, a theorem declared in [MathlibExt/Probability/Truncation.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Truncation.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#truncation-fun-eq-self-of-abs-le).

## Scalar truncation vanishes beyond the cutoff

Scalar truncation kills values strictly outside the cutoff.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.truncationFun_eq_zero_of_abs_gt`, a theorem declared in [MathlibExt/Probability/Truncation.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Truncation.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#truncation-fun-eq-zero-of-abs-gt).

## Scalar truncation preserves nonnegativity

Scalar truncation preserves nonnegativity.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.truncationFun_nonneg_of_nonneg`, a theorem declared in [MathlibExt/Probability/Truncation.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Truncation.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#truncation-fun-nonneg-of-nonneg).

## Canonical truncation factors through scalar truncation

Canonical truncation factors through its scalar specialization.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.truncatedRV_eq_comp`, a theorem declared in [MathlibExt/Probability/Truncation.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Truncation.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#truncated-rv-eq-comp).

## Measurability of scalar truncation

The scalar specialization of canonical truncation is measurable.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.measurable_truncationFun`, a theorem declared in [MathlibExt/Probability/Truncation.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Truncation.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#measurable-truncation-fun).

## Measurability of a truncated random variable

Canonical truncation needs measurability only of the selected variable.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.measurable_truncatedRV_of_measurable`, a theorem declared in [MathlibExt/Probability/Truncation.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Truncation.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#measurable-truncated-rv-of-measurable).

## Truncation leaves a family bounded by the cutoff unchanged

A family bounded by the cutoff is unchanged by canonical truncation.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.truncatedRV_eq_of_bdd`, a theorem declared in [MathlibExt/Probability/Truncation.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Truncation.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#truncated-rv-eq-of-bdd).

## Truncation preserves almost-sure limits of bounded partial sums

A uniformly bounded family keeps its almost-sure partial-sum limit under
canonical truncation, on the same measure.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.ae_tendsto_truncatedRV_of_bdd`, a theorem declared in [MathlibExt/Probability/Truncation.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Truncation.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#ae-tendsto-truncated-rv-of-bdd).

## Truncated random variables lie in every Lp space

Canonical truncation is in every `Lᵖ` on a finite measure space.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.memLp_truncatedRV`, a theorem declared in [MathlibExt/Probability/Truncation.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Truncation.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#mem-lp-truncated-rv).

## Integrability of truncated random variables

Canonical truncation is integrable on a finite measure space.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.integrable_truncatedRV`, a theorem declared in [MathlibExt/Probability/Truncation.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Truncation.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#integrable-truncated-rv).

## Variance bound for a truncated random variable

The variance of canonical truncation is at most `A²`.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.variance_truncatedRV_le`, a theorem declared in [MathlibExt/Probability/Truncation.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Truncation.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#variance-truncated-rv-le).

## Mean bound for a truncated random variable

The absolute mean of canonical truncation is at most `|A|`.

Formalized by `ProbabilityTheory.KolmogorovThreeSeries.abs_integral_truncatedRV_le`, a theorem declared in [MathlibExt/Probability/Truncation.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Truncation.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html#abs-integral-truncated-rv-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kolmogorov's three-series theorem](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/laws-of-large-numbers/kolmogorov-s-three-series-theorem)
