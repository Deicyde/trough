---
declaration: section
origin: cited
lean: Real.powerGrowthBadSet, Real.volume_powerGrowthBadSet_lt_top, Complex.wimanTaylorCoefficient, Complex.wimanTerm, Complex.wimanMaximumTerm, Complex.wimanMaximumModulus, Complex.wimanTerm_abs, Complex.wimanMaximumTerm_abs
statement: formalized
proof: formalized
---

# Wiman–Valiron theory

58 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html).

## Power-growth exceptional set

For a function $h : \mathbb{R} \to \mathbb{R}$ and real
numbers $p$ and $x_0$, this is the set of real numbers $x \ge x_0$ such that
$h(x)^p \le h'(x)$, where $h(x)^p$ is the real power and $h'(x)$ is the derivative of $h$ at
$x$, taken to be $0$ where $h$ is not differentiable.

Formalized by `Real.powerGrowthBadSet`, a definition declared in [MathlibExt/Analysis/Calculus/PowerGrowthBadSet.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/PowerGrowthBadSet.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#power-growth-bad-set).

## The power-growth exceptional set has finite measure

Let $p > 1$ and $x_0$ be real
numbers, and let $h : \mathbb{R} \to \mathbb{R}$ be continuously differentiable, with
$h(x) > 0$ for all $x \ge x_0$ and $h$ nondecreasing on $[x_0, \infty)$. Then the
power-growth exceptional set of $h$, the set of $x \ge x_0$ with $h(x)^p \le h'(x)$, has finite
Lebesgue measure.

Formalized by `Real.volume_powerGrowthBadSet_lt_top`, a theorem declared in [MathlibExt/Analysis/Calculus/PowerGrowthBadSet.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/PowerGrowthBadSet.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#volume-power-growth-bad-set-lt-top).

## Wiman Taylor coefficient

For a function $f : \mathbb{C} \to \mathbb{C}$ and
$n \in \mathbb{N}$, the $n$th Taylor coefficient of $f$ at the origin is
$a_n = f^{(n)}(0) / n!$, where $f^{(n)}$ is the $n$th iterated complex derivative of $f$.

Here the derivative at a point where a function is not complex differentiable is taken to be
$0$. For an entire function these are the coefficients of its Taylor series at $0$.

Formalized by `Complex.wimanTaylorCoefficient`, a definition declared in [MathlibExt/Analysis/Complex/Wiman.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-taylor-coefficient).

## Wiman term

For a function $f : \mathbb{C} \to \mathbb{C}$, a real number $r$ and a natural
number $n$, the Wiman term of $f$ at radius $r$ and index $n$ is the real number $|a_n| \, |r|^n$,
where $a_n = f^{(n)}(0) / n!$ is the $n$th Taylor coefficient of $f$ at the origin. It is the
modulus of the $n$th Taylor term of $f$ on the circle of radius $|r|$.

Using $|r|$ makes a negative input denote the same radius as its absolute value, so the Wiman
term is always nonnegative.

Formalized by `Complex.wimanTerm`, a definition declared in [MathlibExt/Analysis/Complex/Wiman.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-term).

## Wiman maximum term

For a function $f : \mathbb{C} \to \mathbb{C}$ and a real number $r$,
the Wiman maximum term $\mu(f, r)$ is the supremum over $n \in \mathbb{N}$ of the Wiman terms
$|a_n| \, |r|^n$, where $a_n = f^{(n)}(0) / n!$ is the $n$th Wiman Taylor coefficient of $f$.

Here the supremum of a set of real numbers that is not bounded above is taken to be $0$.

Formalized by `Complex.wimanMaximumTerm`, a definition declared in [MathlibExt/Analysis/Complex/Wiman.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-maximum-term).

## Wiman maximum modulus

For a function $f : \mathbb{C} \to \mathbb{C}$ and a real number
$r$, the Wiman maximum modulus $M(f, r)$ is the supremum of $|f(z)|$ over all $z \in \mathbb{C}$
with $|z| = |r|$.

Here the supremum of a set of real numbers that is not bounded above is taken to be $0$.

Formalized by `Complex.wimanMaximumModulus`, a definition declared in [MathlibExt/Analysis/Complex/Wiman.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-maximum-modulus).

## Wiman term at the absolute value of the radius

For every function
$f : \mathbb{C} \to \mathbb{C}$, every real number $r$ and every natural number $n$, the Wiman term
of $f$ at radius $|r|$ and index $n$ equals the Wiman term of $f$ at radius $r$ and index $n$.

Formalized by `Complex.wimanTerm_abs`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-term-abs).

## Wiman maximum term at the absolute value of the radius

For every function
$f : \mathbb{C} \to \mathbb{C}$ and every real number $r$, the Wiman maximum term of $f$ at
radius $|r|$ equals the Wiman maximum term of $f$ at radius $r$.

Formalized by `Complex.wimanMaximumTerm_abs`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-maximum-term-abs).

## Wiman maximum modulus at the absolute value of the radius

For every function
$f : \mathbb{C} \to \mathbb{C}$ and every real number $r$, the Wiman maximum modulus of $f$ at
radius $|r|$ equals the Wiman maximum modulus of $f$ at radius $r$.

Formalized by `Complex.wimanMaximumModulus_abs`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-maximum-modulus-abs).

## Wiman term at a negated radius

For every function $f : \mathbb{C} \to \mathbb{C}$, every
real number $r$ and every natural number $n$, the Wiman term of $f$ at radius $-r$ and index $n$
equals the Wiman term of $f$ at radius $r$ and index $n$.

Formalized by `Complex.wimanTerm_neg`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-term-neg).

## The Wiman maximum term is even in the radius

For every function
$f : \mathbb{C} \to \mathbb{C}$ and every real number $r$, the Wiman maximum term of $f$ at
radius $-r$ equals the Wiman maximum term of $f$ at radius $r$.

Formalized by `Complex.wimanMaximumTerm_neg`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-maximum-term-neg).

## The Wiman maximum modulus is even in the radius

For every function
$f : \mathbb{C} \to \mathbb{C}$ and every real number $r$, the Wiman maximum modulus of $f$ at
radius $-r$ equals the Wiman maximum modulus of $f$ at radius $r$.

Formalized by `Complex.wimanMaximumModulus_neg`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-maximum-modulus-neg).

## Transcendental functions

A function $f : \mathbb{C} \to \mathbb{C}$ is
transcendental when there is no complex polynomial $p$ with $f(z) = p(z)$ for all
$z \in \mathbb{C}$.

No analyticity is assumed; results about transcendental entire functions assume it separately.

Formalized by `Complex.IsTranscendental`, a definition declared in [MathlibExt/Analysis/Complex/Wiman.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#is-transcendental).

## Values on a circle are bounded by the maximum modulus

Let $f : \mathbb{C} \to \mathbb{C}$
be continuous, let $r$ be a real number and let $z \in \mathbb{C}$ with $|z| = r$. Then
$|f(z)| \le M(f, r)$, where $M(f, r)$ is the Wiman maximum modulus of $f$ at radius $r$.

Formalized by `Complex.norm_le_wimanMaximumModulus`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#norm-le-wiman-maximum-modulus).

## Cubing a Wiman 2/3 bound

Let $M$ and $\mu$ be real numbers with $M \ge 0$,
$\mu \ge 0$ and $\log \mu \ge 0$, where $\log$ is the real logarithm with $\log 0 = 0$.
If $M \le \mu (\log \mu)^{2/3}$, then $M^3 \le \mu^3 (\log \mu)^2$.

Formalized by `Complex.cube_le_cube_mul_log_sq_of_wiman`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#cube-le-cube-mul-log-sq-of-wiman).

## Absorbing constants into the exponent gap

For every real $C > 0$ there is a real $U > 1$
such that for all reals $\mu$ and $A$ with $U \le \mu \le A$ and
$A \le C \mu \bigl(1 + (\log A)^{81/128}\bigr)$, we have $A \le \mu (\log \mu)^{2/3}$.

The gap $2/3 - 81/128 > 0$ between the exponents absorbs the constant $C$ of the corrected
Rosenbloom estimate once the maximum term $\mu$ is large.

Formalized by `Complex.eventually_absorb_corrected_wiman_exponent`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/CorrectedEstimateAbsorption.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/CorrectedEstimateAbsorption.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#eventually-absorb-corrected-wiman-expone).

## The maximum modulus is attained

Let $f$ be an entire function and let $r \ge 0$. Then
there is a point $z$ with $|z| = r$ such that $|f(w)| \le |f(z)|$ for every $w$ with $|w| = r$,
and the maximum modulus $M(r) = \sup_{|w| = r} |f(w)|$ equals $|f(z)|$.

Formalized by `Complex.exists_mem_sphere_eq_wimanMaximumModulus`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/MaximumModulusAttained.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/MaximumModulusAttained.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#exists-mem-sphere-eq-wiman-maximum-modul).

## Radial majorant

For a function $f : \mathbb{C} \to \mathbb{C}$ with Taylor coefficients
$a_n = f^{(n)}(0) / n!$ at the origin and a real number $r$, the radial majorant of $f$ at $r$ is
$M_f(r) = \sum_{n \ge 0} |a_n| \, |r|^n$, the sum of the radial Taylor terms at radius $|r|$.
By convention $M_f(r) = 0$ when this series diverges.

Formalized by `Complex.wimanMajorant`, a definition declared in [MathlibExt/Analysis/Complex/Wiman/RadialMajorant.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/RadialMajorant.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-majorant).

## Radial Taylor terms are nonnegative

For every function $f : \mathbb{C} \to \mathbb{C}$
with Taylor coefficients $a_n = f^{(n)}(0) / n!$ at the origin, every real $r$ and every
$n \in \mathbb{N}$, we have $0 \le |a_n| \, |r|^n$.

Formalized by `Complex.wimanTerm_nonneg`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/RadialMajorant.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/RadialMajorant.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-term-nonneg).

## Summability of the radial Taylor terms

Let $f$ be an entire function with Taylor
coefficients $a_n = f^{(n)}(0) / n!$ at the origin. For every real $r$, the series
$\sum_{n \ge 0} |a_n| \, |r|^n$ converges.

Formalized by `Complex.summable_wimanTerm`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/RadialMajorant.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/RadialMajorant.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#summable-wiman-term).

## The radial majorant is nonnegative

For every function $f : \mathbb{C} \to \mathbb{C}$ with
Taylor coefficients $a_n = f^{(n)}(0) / n!$ at the origin and every real number $r$, the radial
majorant $M_f(r) = \sum_{n \ge 0} |a_n| \, |r|^n$ (taken to be $0$ when the series diverges)
satisfies $0 \le M_f(r)$.

Formalized by `Complex.wimanMajorant_nonneg`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/RadialMajorant.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/RadialMajorant.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-majorant-nonneg).

## Each radial Taylor term is at most the radial majorant

Let $f$ be an entire function with
Taylor coefficients $a_n = f^{(n)}(0) / n!$ at the origin, and let
$M_f(r) = \sum_{k \ge 0} |a_k| \, |r|^k$ be its radial majorant. For every real $r$ and every
$n \in \mathbb{N}$, $|a_n| \, |r|^n \le M_f(r)$.

Formalized by `Complex.wimanTerm_le_wimanMajorant`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/RadialMajorant.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/RadialMajorant.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-term-le-wiman-majorant).

## Wiman growth function

Let $f : \mathbb{C} \to \mathbb{C}$ have Taylor coefficients
$a_n = f^{(n)}(0) / n!$ at the origin, and let $M_f(r) = \sum_{n \ge 0} |a_n| \, |r|^n$ be its
radial majorant, taken to be $0$ when the series diverges. For a real number $x$, the Wiman
growth of $f$ at $x$ is $\log M_f(e^x)$, the logarithm of the radial majorant at radius $e^x$,
with the convention $\log 0 = 0$.

Formalized by `Complex.wimanGrowth`, a definition declared in [MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-growth).

## Wiman coefficient measure

For $f : \mathbb{C} \to \mathbb{C}$ with Taylor coefficients
$a_n = f^{(n)}(0)/n!$ at $0$, the Wiman coefficient measure of $f$ is the measure
$\mu_f = \sum_{n \ge 0} |a_n|\,\delta_n$ on $\mathbb{N}$, which gives each $n$ mass $|a_n|$.

Formalized by `Complex.wimanCoefficientMeasure`, a definition declared in [MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-coefficient-measure).

## Tilted coefficient measure

Let $f : \mathbb{C} \to \mathbb{C}$ have Taylor coefficients
$a_n = f^{(n)}(0)/n!$, and let $\mu_f$ be its coefficient measure on $\mathbb{N}$, with mass $|a_n|$
at $n$. For a real number $x$, the tilted coefficient measure $\mu_{f,x}$ is the exponential tilt of
$\mu_f$ by $n \mapsto xn$: the measure with density $e^{xn} / \int e^{xm}\,d\mu_f(m)$ with respect
to $\mu_f$.

Formalized by `Complex.wimanTiltedMeasure`, a definition declared in [MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-tilted-measure).

## Point masses of the Wiman coefficient measure

Let $f : \mathbb{C} \to \mathbb{C}$ and
$a_n = f^{(n)}(0)/n!$. For every $n \in \mathbb{N}$, the Wiman coefficient measure $\mu_f$ of $f$
gives the singleton $\{n\}$ mass $\mu_f(\{n\}) = |a_n|$.

Formalized by `Complex.wimanCoefficientMeasure_singleton`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-coefficient-measure-singleton).

## Exponential moments of the Wiman coefficient measure are finite

Let $f$ be an entire
function and let $\mu_f$ be its Wiman coefficient measure on $\mathbb{N}$, which gives each
$n \in \mathbb{N}$ mass $|a_n|$, where $a_n = f^{(n)}(0)/n!$. For every real $x$, the function
$n \mapsto e^{xn}$ is integrable with respect to $\mu_f$.

Formalized by `Complex.integrable_exp_mul_wimanCoefficientMeasure`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#integrable-exp-mul-wiman-coefficient-mea).

## The exponential-integrability set of the Wiman coefficient measure is the whole line

Let
$f$ be an entire function and let $\mu_f$ be its Wiman coefficient measure on $\mathbb{N}$. The set
of real $t$ for which $n \mapsto e^{tn}$ is integrable with respect to $\mu_f$ is all of
$\mathbb{R}$.

Formalized by `Complex.integrableExpSet_wimanCoefficientMeasure_eq_univ`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#integrable-exp-set-wiman-coefficient-mea).

## Every real parameter is interior to the exponential-integrability set

Let $f$ be an
entire function and let $\mu_f$ be its Wiman coefficient measure on $\mathbb{N}$. Every real $x$
lies in the interior of the set of real $t$ for which $n \mapsto e^{tn}$ is integrable with
respect to $\mu_f$.

Formalized by `Complex.mem_interior_integrableExpSet_wimanCoefficientMeasure`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#mem-interior-integrable-exp-set-wiman-co).

## Exponential moments of the Wiman coefficient measure equal the Wiman majorant

Let $f$ be
an entire function with Taylor coefficients $a_n = f^{(n)}(0)/n!$ at $0$, and let $\mu_f$ be its
Wiman coefficient measure on $\mathbb{N}$. For every real $x$,

$$\int e^{xn}\,d\mu_f(n) = M_f(e^x),$$

where $M_f(r) = \sum_{n \ge 0} |a_n|\,|r|^n$ is the Wiman majorant of $f$.

Formalized by `Complex.integral_exp_mul_wimanCoefficientMeasure`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#integral-exp-mul-wiman-coefficient-measu).

## Moment generating function of the coefficient measure

Let $f$ be an entire function with
Taylor coefficients $a_n = f^{(n)}(0)/n!$, and let $\mu_f$ be its coefficient measure on
$\mathbb{N}$, which has mass $|a_n|$ at $n$. For every real $x$, the moment generating function of
$n \mapsto n$ under $\mu_f$ at $x$, namely $\int e^{xn}\,d\mu_f(n)$, equals the radial majorant
$M_f(e^x)$, where $M_f(r) = \sum_n |a_n|\,|r|^n$.

Formalized by `Complex.wiman_mgf_eq_majorant`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-mgf-eq-majorant).

## The Wiman growth is the cumulant generating function of the coefficient measure

Let $f$
be an entire function and let $\mu_f$ be its Wiman coefficient measure on $\mathbb{N}$. For every
real $x$, the cumulant generating function of $n \mapsto n$ under $\mu_f$ at $x$, namely
$\log \int e^{xn}\,d\mu_f(n)$, equals the Wiman growth $G_f(x) = \log M_f(e^x)$, where $M_f$ is
the Wiman majorant of $f$.

Formalized by `Complex.wiman_cgf_eq_growth`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-cgf-eq-growth).

## A nonzero Taylor coefficient makes the Wiman coefficient measure nonzero

Let
$f : \mathbb{C} \to \mathbb{C}$ and $a_n = f^{(n)}(0)/n!$. If $a_n \ne 0$ for some $n$, then the
Wiman coefficient measure $\mu_f$ of $f$ is not the zero measure.

Formalized by `Complex.wimanCoefficientMeasure_ne_zero`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-coefficient-measure-ne-zero).

## The Wiman tilted measure is a probability measure

Let $f$ be an entire function such that
$f^{(n)}(0)/n! \ne 0$ for some $n$, and let $\mu_f$ be its Wiman coefficient measure on
$\mathbb{N}$. For every real $x$, the Wiman tilted measure of $f$ at $x$, which has density
$n \mapsto e^{xn} / \int e^{xm}\,d\mu_f(m)$ with respect to $\mu_f$, is a probability measure.

Formalized by `Complex.isProbabilityMeasure_wimanTiltedMeasure`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#is-probability-measure-wiman-tilted-meas).

## Atoms of the tilted coefficient measure

Let $f$ be an entire function with Taylor
coefficients $a_n = f^{(n)}(0)/n!$, radial majorant $M_f(r) = \sum_n |a_n|\,|r|^n$ and Taylor terms
$T_n(r) = |a_n|\,|r|^n$. For every real $x$ and every $n \in \mathbb{N}$, the tilted coefficient
measure $\mu_{f,x}$ gives the singleton $\{n\}$ mass $T_n(e^x) / M_f(e^x)$ (with the convention
$t/0 = 0$).

Formalized by `Complex.wimanTiltedMeasure_singleton`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-tilted-measure-singleton).

## Atomic form of the tilted coefficient measure

Let $f$ be an entire function with Taylor
coefficients $a_n = f^{(n)}(0)/n!$, radial majorant $M_f(r) = \sum_n |a_n|\,|r|^n$ and Taylor terms
$T_n(r) = |a_n|\,|r|^n$. For every real $x$, the tilted coefficient measure $\mu_{f,x}$ equals
$\sum_{n \in \mathbb{N}} \frac{T_n(e^x)}{M_f(e^x)}\,\delta_n$, the measure on $\mathbb{N}$ with mass
$T_n(e^x) / M_f(e^x)$ at each $n$ (with the convention $t/0 = 0$).

Formalized by `Complex.wimanTiltedMeasure_eq_sum`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/CoefficientExponentialFamily.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-tilted-measure-eq-sum).

## The logarithmic majorant is $C^2$

Let $f$ be an entire function with Taylor
coefficients $a_n$ at the origin, and let $\Phi(x) = \log \sum_{n \ge 0} |a_n| e^{nx}$ be the
logarithm of its radial Taylor majorant at radius $e^x$ (with $\log 0 = 0$). Then $\Phi$ is
twice continuously differentiable on $\mathbb{R}$.

Formalized by `Complex.contDiff_two_wimanGrowth`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/CumulantMoments.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/CumulantMoments.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#cont-diff-two-wiman-growth).

## Derivative of the logarithmic majorant as a mean

Let $f$ be an entire function whose
Taylor coefficients $a_n$ at the origin are not all zero, and let
$\Phi(x) = \log \sum_{n \ge 0} |a_n| e^{nx}$. For real $x$, let $\nu_x$ be the coefficient
measure tilted at $x$, the probability measure on $\mathbb{N}$ with
$\nu_x(\{n\}) = |a_n| e^{nx} / \sum_{m \ge 0} |a_m| e^{mx}$. Then
$\Phi'(x) = \int n \, d\nu_x(n)$, the mean of $n$ under $\nu_x$.

Formalized by `Complex.deriv_wimanGrowth_eq_expectation`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/CumulantMoments.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/CumulantMoments.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#deriv-wiman-growth-eq-expectation).

## Second derivative of the logarithmic majorant as a variance

Let $f$ be an entire
function whose Taylor coefficients $a_n$ at the origin are not all zero, and let
$\Phi(x) = \log \sum_{n \ge 0} |a_n| e^{nx}$. For real $x$, let $\nu_x$ be the coefficient
measure tilted at $x$, the probability measure on $\mathbb{N}$ with
$\nu_x(\{n\}) = |a_n| e^{nx} / \sum_{m \ge 0} |a_m| e^{mx}$. Then $\Phi''(x)$ is the variance
of $n$ under $\nu_x$.

Formalized by `Complex.iteratedDeriv_two_wimanGrowth_eq_variance`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/CumulantMoments.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/CumulantMoments.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#iterated-deriv-two-wiman-growth-eq-varia).

## The logarithmic majorant has nonnegative second derivative

Let $f$ be an entire
function whose Taylor coefficients $a_n$ at the origin are not all zero, and let
$\Phi(x) = \log \sum_{n \ge 0} |a_n| e^{nx}$. Then $\Phi''(x) \ge 0$ for every real $x$.

Formalized by `Complex.iteratedDeriv_two_wimanGrowth_nonneg`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/CumulantMoments.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/CumulantMoments.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#iterated-deriv-two-wiman-growth-nonneg).

## The Taylor terms are bounded above

Let $f$ be an entire function with Taylor
coefficients $a_n$ at the origin, and let $r$ be real. Then the set of Taylor terms
$\{|a_n|\,|r|^n : n \in \mathbb{N}\}$ is bounded above.

Formalized by `Complex.bddAbove_range_wimanTerm`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/MaximumTermAttained.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/MaximumTermAttained.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#bdd-above-range-wiman-term).

## Each Taylor term is at most the maximum term

Let $f$ be an entire function with Taylor
coefficients $a_n$ at the origin and maximum term $\mu(r) = \sup_k |a_k|\,|r|^k$. For every real
$r$ and every $n \in \mathbb{N}$, $|a_n|\,|r|^n \le \mu(r)$.

Formalized by `Complex.wimanTerm_le_wimanMaximumTerm`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/MaximumTermAttained.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/MaximumTermAttained.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-term-le-wiman-maximum-term).

## Bounding the maximum term

Let $f$ be an entire function with Taylor coefficients $a_n$
at the origin and maximum term $\mu(r) = \sup_n |a_n|\,|r|^n$. For all real $r$ and $c$,
$\mu(r) \le c$ if and only if $|a_n|\,|r|^n \le c$ for every $n \in \mathbb{N}$.

Formalized by `Complex.wimanMaximumTerm_le_iff`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/MaximumTermAttained.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/MaximumTermAttained.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-maximum-term-le-iff).

## The maximum term is attained by a Taylor term

Let $f$ be an entire function with Taylor
coefficients $a_n$ at the origin and maximum term $\mu(r) = \sup_n |a_n|\,|r|^n$. For every real
$r$ there is an $n \in \mathbb{N}$ with $|a_n|\,|r|^n = \mu(r)$.

Formalized by `Complex.exists_wimanTerm_eq_wimanMaximumTerm`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/MaximumTermAttained.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/MaximumTermAttained.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#exists-wiman-term-eq-wiman-maximum-term).

## Corrected Rosenbloom estimate

Let $f$ be an entire function with Taylor coefficients
$a_n = f^{(n)}(0)/n!$, radial majorant $M_f(r) = \sum_n |a_n|\,|r|^n$, maximum term
$\mu_f(r) = \sup_n |a_n|\,|r|^n$ and logarithmic majorant $g_f(x) = \log M_f(e^x)$. For every real
$x$, $M_f(e^x) \le 8\,\mu_f(e^x)\,\bigl(1 + \sqrt{g_f''(x)}\bigr)$.

The additive $1$ keeps the estimate valid when $g_f''(x) = 0$.

Formalized by `Complex.wimanMajorant_le_eight_mul_maximumTerm`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/CorrectedRosenbloom.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/CorrectedRosenbloom.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-majorant-le-eight-mul-maximum-term).

## Cauchy's inequality for the maximum term

Let $f$ be an entire function with Taylor
coefficients $a_n$ at the origin, maximum term $\mu(r) = \sup_n |a_n|\,|r|^n$ and maximum modulus
$M(r) = \sup_{|z| = |r|} |f(z)|$. Then $\mu(r) \le M(r)$ for every real $r > 0$.

Formalized by `Complex.wimanMaximumTerm_le_wimanMaximumModulus`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/MaximumTermLeModulus.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/MaximumTermLeModulus.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-maximum-term-le-wiman-maximum-modu).

## Taylor expansion of an entire function

Let $f$ be an entire function with Taylor
coefficients $a_n = f^{(n)}(0) / n!$ at the origin. For every $z \in \mathbb{C}$, the series
$\sum_{n \ge 0} a_n z^n$ converges unconditionally to $f(z)$.

Formalized by `Complex.hasSum_wimanTaylorCoefficient_mul_pow`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/TaylorExpansion.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/TaylorExpansion.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#has-sum-wiman-taylor-coefficient-mul-pow).

## Transcendental entire functions have infinitely many Taylor coefficients

A transcendental entire function has infinitely many nonzero Taylor coefficients.

Formalized by `Complex.infinite_support_wimanTaylorCoefficient`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/InfiniteTaylorSupport.lean, line 20](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/InfiniteTaylorSupport.lean#L20). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#infinite-support-wiman-taylor-coefficien).

## The maximum modulus is at most the radial Taylor majorant

Let $f$ be an entire function
with Taylor coefficients $a_n$ at the origin and let $r \ge 0$. Then the maximum modulus
$M(r) = \sup_{|z| = r} |f(z)|$ satisfies $M(r) \le \sum_{n \ge 0} |a_n| r^n$.

Formalized by `Complex.wimanMaximumModulus_le_wimanMajorant`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/MaximumModulusLeMajorant.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/MaximumModulusLeMajorant.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-maximum-modulus-le-wiman-majorant).

## The maximum term of a transcendental entire function tends to infinity

Let $f$ be an
entire function that is not a polynomial function, with Taylor coefficients $a_n$ at the origin
and maximum term $\mu(r) = \sup_n |a_n|\,|r|^n$. Then $\mu(r) \to \infty$ as $r \to \infty$.

Formalized by `Complex.tendsto_wimanMaximumTerm_atTop`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/MaximumTermTendsToInfinity.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/MaximumTermTendsToInfinity.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#tendsto-wiman-maximum-term-at-top).

## The maximum term eventually exceeds one

Let $f$ be an entire function that is not a
polynomial function, with Taylor coefficients $a_n$ at the origin and maximum term
$\mu(r) = \sup_n |a_n|\,|r|^n$. Then there is $R$ such that $\mu(r) > 1$ for all real $r \ge R$.

Formalized by `Complex.eventually_one_lt_wimanMaximumTerm`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/MaximumTermTendsToInfinity.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/MaximumTermTendsToInfinity.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#eventually-one-lt-wiman-maximum-term).

## The logarithm of the maximum term is eventually positive

Let $f$ be an entire function
that is not a polynomial function, with Taylor coefficients $a_n$ at the origin and maximum term
$\mu(r) = \sup_n |a_n|\,|r|^n$. Then there is $R$ such that $\log \mu(r) > 0$ for all real
$r \ge R$.

Formalized by `Complex.eventually_pos_log_wimanMaximumTerm`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/MaximumTermTendsToInfinity.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/MaximumTermTendsToInfinity.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#eventually-pos-log-wiman-maximum-term).

## Eventual regularity of the logarithmic majorant

Let $f$ be a transcendental entire
function with Taylor coefficients $a_n$ at the origin, and let
$\Phi(x) = \log \sum_{n \ge 0} |a_n| e^{nx}$. Then $\Phi$ is twice continuously differentiable
on $\mathbb{R}$, $\Phi'(x) \to \infty$ as $x \to \infty$, and there is a real $x_0$ such that
$\Phi(x) > 0$ for every $x \ge x_0$ and both $\Phi$ and $\Phi'$ are nondecreasing on
$[x_0, \infty)$.

Formalized by `Complex.eventually_wimanGrowth_regular`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/LogMajorantRegularity.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/LogMajorantRegularity.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#eventually-wiman-growth-regular).

## Wiman exceptional set

For a function $f : \mathbb{C} \to \mathbb{C}$ with radial majorant
$M_f$, let $g(x) = \log M_f(e^x)$. For $x_0 \in \mathbb{R}$, the Wiman exceptional set $E_f(x_0)$
is the union of the power-growth bad sets of $g$ and of $g'$ with exponent $9/8$ above $x_0$,
that is, the set of $x \ge x_0$ with $g(x)^{9/8} \le g'(x)$ or $g'(x)^{9/8} \le g''(x)$.

Formalized by `Complex.wimanExceptionalSet`, a definition declared in [MathlibExt/Analysis/Complex/Wiman/TwoPowerBadSets.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/TwoPowerBadSets.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-exceptional-set).

## The Wiman exceptional set has finite measure

Let $f$ be a transcendental entire function,
let $M_f$ be its radial majorant and let $g(x) = \log M_f(e^x)$. For $x_0 \in \mathbb{R}$ let
$E_f(x_0)$ be the Wiman exceptional set, the set of $x \ge x_0$ with $g(x)^{9/8} \le g'(x)$ or
$g'(x)^{9/8} \le g''(x)$. There is $x_0 \in \mathbb{R}$ such that $E_f(x_0)$ has finite Lebesgue
measure and $g''(x) \le g(x)^{81/64}$ for every $x \ge x_0$ outside $E_f(x_0)$.

The exponent $81/64 = (9/8)^2$ comes from composing the two growth bounds.

Formalized by `Complex.exists_finite_wimanExceptionalSet`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/TwoPowerBadSets.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/TwoPowerBadSets.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#exists-finite-wiman-exceptional-set).

## Majorant bound off an exceptional set

Let $f$ be a transcendental entire function with
Taylor coefficients $a_n = f^{(n)}(0)/n!$, radial majorant $M_f(r) = \sum_n |a_n|\,|r|^n$, maximum
term $\mu_f(r) = \sup_n |a_n|\,|r|^n$ and logarithmic majorant $g_f(x) = \log M_f(e^x)$. There are
reals $C > 0$ and $x_0$ such that the Wiman exceptional set $E_f(x_0)$ has finite Lebesgue measure
and, for every real $x \ge x_0$ with $x \notin E_f(x_0)$,
$M_f(e^x) \le C\,\mu_f(e^x)\,\bigl(1 + g_f(x)^{81/128}\bigr)$.

Formalized by `Complex.wimanMajorant_bound_off_exceptionalSet`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/CorrectedMajorantBoundOffExceptionalSet.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/CorrectedMajorantBoundOffExceptionalSet.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#wiman-majorant-bound-off-exceptional-set).

## The maximum term tends to infinity along logarithmic radii

Let $f$ be a transcendental
entire function with Taylor coefficients $a_n$ at the origin and maximum term
$\mu(r) = \sup_{n \ge 0} |a_n| |r|^n$. Then $\mu(e^x) \to \infty$ as $x \to \infty$.

Formalized by `Complex.tendsto_wimanMaximumTerm_exp_atTop`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/Filevych.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/Filevych.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#tendsto-wiman-maximum-term-exp-at-top).

## Wiman's inequality with exponent $2/3$ at arbitrarily large radii

Let $f$ be a
transcendental entire function with Taylor coefficients $a_n$ at the origin, maximum modulus
$M(r) = \sup_{|z| = |r|} |f(z)|$ and maximum term $\mu(r) = \sup_{n \ge 0} |a_n| |r|^n$. Then
for every real $R$ there is a real $r > R$ with $M(r) \le \mu(r) (\log \mu(r))^{2/3}$.

## Sources

- Filevych (2003), Matematychni Studii 20(2), 215–221. This is a strict corollary of, not the full theorem stated in, that paper.

Formalized by `Complex.exists_wiman_radius_two_thirds`, a theorem declared in [MathlibExt/Analysis/Complex/Wiman/Filevych.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Wiman/Filevych.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html#exists-wiman-radius-two-thirds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Wiman–Valiron theory](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/entire-functions/wiman-valiron-theory)
