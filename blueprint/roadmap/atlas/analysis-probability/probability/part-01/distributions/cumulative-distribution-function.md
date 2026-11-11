---
declaration: section
origin: cited
lean: MathlibExt.Probability.CdfContinuityPoints.measure_singleton_eq_cdf_sub_leftLim, MathlibExt.Probability.CdfContinuityPoints.continuousAt_cdf_iff_measure_singleton_eq_zero, MathlibExt.Probability.CdfContinuityPoints.cdf_continuousAt_singleton_null, MathlibExt.Probability.CdfContinuityPoints.cdf_continuousAt_frontier_Iic_null, MathlibExt.Probability.CdfContinuityPoints.measure_Ioc_eq_ofReal_cdf, MathlibExt.Probability.CdfContinuityPoints.dense_cdf_continuityPoints
statement: formalized
proof: formalized
---

# Cumulative distribution function

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/cumulative-distribution-function/index.html).

## Atoms are the jumps of the cdf

Let $\mu$ be a probability measure on $\mathbb{R}$ with
cumulative distribution function $F(y) = \mu((-\infty, y])$, and for $x \in \mathbb{R}$ let
$F(x^-) = \lim_{y \to x^-} F(y)$ be its left limit at $x$. Then $\mu(\{x\})$ equals the jump
$F(x) - F(x^-)$, which is a nonnegative real number since $F$ is nondecreasing.

Formalized by `MathlibExt.Probability.CdfContinuityPoints.measure_singleton_eq_cdf_sub_leftLim`, a theorem declared in [MathlibExt/Probability/CdfContinuityPoints.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CdfContinuityPoints.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/cumulative-distribution-function/index.html#measure-singleton-eq-cdf-sub-left-lim).

## The cdf is continuous exactly at the non-atoms

Let $\mu$ be a probability measure on
$\mathbb{R}$ with cumulative distribution function $F(y) = \mu((-\infty, y])$. For every
$x \in \mathbb{R}$, $F$ is continuous at $x$ if and only if $\mu(\{x\}) = 0$.

Formalized by `MathlibExt.Probability.CdfContinuityPoints.continuousAt_cdf_iff_measure_singleton_eq_zero`, a theorem declared in [MathlibExt/Probability/CdfContinuityPoints.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CdfContinuityPoints.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/cumulative-distribution-function/index.html#continuous-at-cdf-iff-measure-singleton).

## No atom at a continuity point of the cdf

Let $\mu$ be a probability measure on
$\mathbb{R}$ with cumulative distribution function $F(y) = \mu((-\infty, y])$. If $F$ is
continuous at a point $x \in \mathbb{R}$, then $\mu(\{x\}) = 0$.

Formalized by `MathlibExt.Probability.CdfContinuityPoints.cdf_continuousAt_singleton_null`, a theorem declared in [MathlibExt/Probability/CdfContinuityPoints.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CdfContinuityPoints.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/cumulative-distribution-function/index.html#cdf-continuous-at-singleton-null).

## Continuity points of the cdf have null boundary

Let $\mu$ be a probability measure on
$\mathbb{R}$ with cumulative distribution function $F(y) = \mu((-\infty, y])$. If $F$ is
continuous at a point $x \in \mathbb{R}$, then the boundary of the half-line $(-\infty, x]$,
which is $\{x\}$, has $\mu$-measure zero.

Formalized by `MathlibExt.Probability.CdfContinuityPoints.cdf_continuousAt_frontier_Iic_null`, a theorem declared in [MathlibExt/Probability/CdfContinuityPoints.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CdfContinuityPoints.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/cumulative-distribution-function/index.html#cdf-continuous-at-frontier-iic-null).

## Mass of a half-open interval via the cdf

Let $\mu$ be a probability measure on
$\mathbb{R}$ with cumulative distribution function $F(y) = \mu((-\infty, y])$. For all
$a, b \in \mathbb{R}$, the measure $\mu((a, b])$ equals $\max(F(b) - F(a), 0)$, as an extended
nonnegative real.

Formalized by `MathlibExt.Probability.CdfContinuityPoints.measure_Ioc_eq_ofReal_cdf`, a theorem declared in [MathlibExt/Probability/CdfContinuityPoints.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CdfContinuityPoints.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/cumulative-distribution-function/index.html#measure-ioc-eq-of-real-cdf).

## The continuity points of the cdf are dense

Let $\mu$ be a probability measure on
$\mathbb{R}$ with cumulative distribution function $F(y) = \mu((-\infty, y])$. The set of
points $x \in \mathbb{R}$ at which $F$ is continuous is dense in $\mathbb{R}$.

This follows from the fact that a monotone function has only countably many discontinuities.

Formalized by `MathlibExt.Probability.CdfContinuityPoints.dense_cdf_continuityPoints`, a theorem declared in [MathlibExt/Probability/CdfContinuityPoints.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CdfContinuityPoints.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/cumulative-distribution-function/index.html#dense-cdf-continuity-points).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cumulative distribution function](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/cumulative-distribution-function/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/distributions/cumulative-distribution-function)
