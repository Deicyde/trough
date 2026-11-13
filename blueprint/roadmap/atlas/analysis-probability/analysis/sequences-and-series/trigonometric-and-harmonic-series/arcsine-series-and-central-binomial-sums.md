---
declaration: section
origin: cited
lean: MetaMathlibExt.arcsin_central_binomial_reciprocal_series, MathlibExt.Analysis.SpecialFunctions.ArcsinTaylorSeries.centralBinomialCoeff, MathlibExt.Analysis.SpecialFunctions.ArcsinTaylorSeries.centralBinomialCoeff_nonneg, MathlibExt.Analysis.SpecialFunctions.ArcsinTaylorSeries.centralBinomialCoeff_le_one, MathlibExt.Analysis.SpecialFunctions.ArcsinTaylorSeries.arcsinSeries, MathlibExt.Analysis.SpecialFunctions.ArcsinTaylorSeries.arcsinIntegralSeries, MathlibExt.Analysis.SpecialFunctions.ArcsinTaylorSeries.arcsinSeries_eq_arcsin, MathlibExt.Analysis.SpecialFunctions.ArcsinTaylorSeries.arcsinIntegralSeries_term_eq
statement: formalized
proof: formalized
---

# Arcsine series and central binomial sums

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arcsine-series-and-central-binomial-sums/index.html).

## Lehmer's central binomial series for arcsin

For every real number $x$ with $|x| < 1$, the
series

$$\sum_{m=1}^{\infty} \frac{(2x)^{2m}}{m \binom{2m}{m}}$$

converges unconditionally, and its sum is $\dfrac{2x}{\sqrt{1 - x^2}} \arcsin x$.

The source attributes the identity to D. H. Lehmer.

## Sources

- B. Sury, Tianming Wang, and Feng-Zhen Zhao, "Identities Involving Reciprocals of Binomial Coefficients," Journal of Integer Sequences 7 (2004), Article 04.2.8, Theorem, lines 365–371, https://cs.uwaterloo.ca/journals/JIS/VOL7/Sury/sury99.tex

Formalized by `MetaMathlibExt.arcsin_central_binomial_reciprocal_series`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ArcsinCentralBinomialReciprocal.lean, line 956](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ArcsinCentralBinomialReciprocal.lean#L956). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arcsine-series-and-central-binomial-sums/index.html#arcsin-central-binomial-reciprocal-serie).

## Normalized central binomial coefficient

For a natural number $n$, the normalized central
binomial coefficient is the real number $c_n = \binom{2n}{n}/2^{2n} = \binom{2n}{n}/4^n$.

Formalized by `MathlibExt.Analysis.SpecialFunctions.ArcsinTaylorSeries.centralBinomialCoeff`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arcsine-series-and-central-binomial-sums/index.html#central-binomial-coeff).

## Normalized central binomial coefficients are nonnegative

For every natural number $n$,
$0 \le \binom{2n}{n}/4^n$.

Formalized by `MathlibExt.Analysis.SpecialFunctions.ArcsinTaylorSeries.centralBinomialCoeff_nonneg`, a lemma declared in [MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arcsine-series-and-central-binomial-sums/index.html#central-binomial-coeff-nonneg).

## Normalized central binomial coefficients are at most one

For every natural number $n$,
$\binom{2n}{n}/4^n \le 1$.

Formalized by `MathlibExt.Analysis.SpecialFunctions.ArcsinTaylorSeries.centralBinomialCoeff_le_one`, a lemma declared in [MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arcsine-series-and-central-binomial-sums/index.html#central-binomial-coeff-le-one).

## Arcsine Taylor series

Let $c_n = \binom{2n}{n}/4^n$. For real $t$, the arcsine Taylor
series is

$$S(t) = \sum_{n=0}^{\infty} \frac{c_n\, t^{2n+1}}{2n+1},$$

with the convention that the sum is $0$ when the series is not summable.

Formalized by `MathlibExt.Analysis.SpecialFunctions.ArcsinTaylorSeries.arcsinSeries`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arcsine-series-and-central-binomial-sums/index.html#arcsin-series).

## Integrated arcsine series

Let $c_n = \binom{2n}{n}/4^n$. For real $t$, the integrated
arcsine series is

$$F(t) = \sum_{n=0}^{\infty} \frac{c_n\, t^{2n+1}}{(2n+1)^2},$$

with the convention that the sum is $0$ when the series is not summable.

Each term is the antiderivative vanishing at $0$ of the corresponding term $c_n t^{2n}/(2n+1)$
of $S(t)/t$, where $S(t) = \sum_{n \ge 0} c_n t^{2n+1}/(2n+1)$ is the arcsine Taylor series.

Formalized by `MathlibExt.Analysis.SpecialFunctions.ArcsinTaylorSeries.arcsinIntegralSeries`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arcsine-series-and-central-binomial-sums/index.html#arcsin-integral-series).

## Taylor series of the arcsine

For every real $t$ with $|t| < 1$,

$$\arcsin t = \sum_{n=0}^{\infty} \frac{\binom{2n}{n}}{4^n} \cdot \frac{t^{2n+1}}{2n+1}.$$

Formalized by `MathlibExt.Analysis.SpecialFunctions.ArcsinTaylorSeries.arcsinSeries_eq_arcsin`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arcsine-series-and-central-binomial-sums/index.html#arcsin-series-eq-arcsin).

## Terms of the integrated arcsine series

Let $c_n = \binom{2n}{n}/4^n$ be the normalized
central binomial coefficient. For every natural number $n$ and every real $t$,

$$\frac{c_n\, t^{2n+1}}{(2n+1)^2} = \frac{\binom{2n}{n}\, t^{2n+1}}{2^{2n}\,(2n+1)^2}.$$

Formalized by `MathlibExt.Analysis.SpecialFunctions.ArcsinTaylorSeries.arcsinIntegralSeries_term_eq`, a lemma declared in [MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arcsine-series-and-central-binomial-sums/index.html#arcsin-integral-series-term-eq).

## Bound on the terms of the integrated arcsine series

Write $c_k = \binom{2k}{k}/4^k$ for
the normalized central binomial coefficient. For every real number $t$ with $|t| \le 1$ and every
natural number $k$, $\left|\frac{c_k\, t^{2k+1}}{(2k+1)^2}\right| \le \frac{1}{(k+1)^2}$.

Formalized by `MathlibExt.Analysis.SpecialFunctions.ArcsinTaylorSeries.norm_arcsinIntegralSeries_term_le`, a lemma declared in [MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arcsine-series-and-central-binomial-sums/index.html#norm-arcsin-integral-series-term-le).

## Summability of the integrated arcsine series

Write $c_n = \binom{2n}{n}/4^n$ for the
normalized central binomial coefficient. For every real number $t$ with $|t| \le 1$, the series
$\sum_{n=0}^{\infty} \frac{c_n\, t^{2n+1}}{(2n+1)^2}$ converges absolutely.

Formalized by `MathlibExt.Analysis.SpecialFunctions.ArcsinTaylorSeries.summable_arcsinIntegralSeries_term`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arcsine-series-and-central-binomial-sums/index.html#summable-arcsin-integral-series-term).

## The integrated arcsine series vanishes at the origin

The integrated arcsine series
$F(t) = \sum_{n \ge 0} \binom{2n}{n} 4^{-n}\, t^{2n+1}/(2n+1)^2$ satisfies $F(0) = 0$.

Formalized by `MathlibExt.Analysis.SpecialFunctions.ArcsinTaylorSeries.arcsinIntegralSeries_zero`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean, line 398](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean#L398). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arcsine-series-and-central-binomial-sums/index.html#arcsin-integral-series-zero).

## Continuity of the integrated arcsine series

The integrated arcsine series
$F(t) = \sum_{n \ge 0} \binom{2n}{n} 4^{-n}\, t^{2n+1}/(2n+1)^2$ is continuous on the closed
interval $[-1, 1]$.

Formalized by `MathlibExt.Analysis.SpecialFunctions.ArcsinTaylorSeries.continuousOn_arcsinIntegralSeries`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arcsine-series-and-central-binomial-sums/index.html#continuous-on-arcsin-integral-series).

## Summability of the arcsine series

Write $c_n = \binom{2n}{n}/4^n$ for the normalized
central binomial coefficient. For every real number $y$ with $|y| < 1$, the series
$\sum_{n=0}^{\infty} \frac{c_n\, y^{2n+1}}{2n+1}$ converges absolutely.

Formalized by `MathlibExt.Analysis.SpecialFunctions.ArcsinTaylorSeries.summable_arcsinSeries_term`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean, line 496](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean#L496). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arcsine-series-and-central-binomial-sums/index.html#summable-arcsin-series-term).

## Derivative of the integrated arcsine series

Let
$F(t) = \sum_{n \ge 0} \binom{2n}{n} 4^{-n}\, t^{2n+1}/(2n+1)^2$ be the integrated arcsine
series. For every real $y$ with $|y| < 1$ and $y \neq 0$, $F$ is differentiable at $y$ with
$F'(y) = \arcsin(y)/y$.

Formalized by `MathlibExt.Analysis.SpecialFunctions.ArcsinTaylorSeries.hasDerivAt_arcsinIntegralSeries`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean, line 545](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/ArcsinTaylorSeries.lean#L545). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arcsine-series-and-central-binomial-sums/index.html#has-deriv-at-arcsin-integral-series).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arcsine series and central binomial sums](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arcsine-series-and-central-binomial-sums/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arcsine-series-and-central-binomial-sums)
