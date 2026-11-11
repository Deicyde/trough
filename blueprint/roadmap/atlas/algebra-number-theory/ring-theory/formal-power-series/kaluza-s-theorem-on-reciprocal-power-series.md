---
declaration: section
origin: cited
lean: MathlibExt.Algebra.PowerSeries.KaluzaCoefficientBoundsWanted.HasPositiveLogConvexCoefficients, MathlibExt.Algebra.PowerSeries.KaluzaCoefficientBoundsWanted.HasPositiveLogConvexCoefficients.coeff_pos, MathlibExt.Algebra.PowerSeries.KaluzaCoefficientBoundsWanted.HasPositiveLogConvexCoefficients.sq_coeff_succ_le, MathlibExt.Algebra.PowerSeries.KaluzaCoefficientBoundsWanted.kaluza_coeff_inv_bounds
statement: formalized
proof: formalized
---

# Kaluza's theorem on reciprocal power series

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/kaluza-s-theorem-on-reciprocal-power-series/index.html).

## Positive log-convex coefficients

A real formal power series $f = \sum_n a_n X^n$ has
positive log-convex coefficients if $a_n > 0$ for every natural number $n$ and
$a_{n+1}^2 \le a_n a_{n+2}$ for every natural number $n$. This is the hypothesis of Kaluza's
bounds for the coefficients of the reciprocal series.

## Sources

- László Tóth, *Alternating Sums Concerning Multiplicative Arithmetic Functions*, Journal of Integer Sequences 20, the lemma at lines 553–562 of <https://cs.uwaterloo.ca/journals/JIS/VOL20/Toth/toth25.tex>.

Formalized by `MathlibExt.Algebra.PowerSeries.KaluzaCoefficientBoundsWanted.HasPositiveLogConvexCoefficients`, a definition declared in [MathlibExt/RingTheory/PowerSeries/KaluzaCoefficientBounds.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/PowerSeries/KaluzaCoefficientBounds.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/kaluza-s-theorem-on-reciprocal-power-series/index.html#has-positive-log-convex-coefficients).

## Coefficients of a positive log-convex series are positive

If a real formal power series
$f$ has positive log-convex coefficients, then the coefficient of $X^n$ in $f$ is strictly
positive for every natural number $n$.

Formalized by `MathlibExt.Algebra.PowerSeries.KaluzaCoefficientBoundsWanted.HasPositiveLogConvexCoefficients.coeff_pos`, a theorem declared in [MathlibExt/RingTheory/PowerSeries/KaluzaCoefficientBounds.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/PowerSeries/KaluzaCoefficientBounds.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/kaluza-s-theorem-on-reciprocal-power-series/index.html#coeff-pos).

## Log-convexity of the coefficients

If a real formal power series $f = \sum_n a_n X^n$
has positive log-convex coefficients, then $a_{n+1}^2 \le a_n a_{n+2}$ for every natural
number $n$.

Formalized by `MathlibExt.Algebra.PowerSeries.KaluzaCoefficientBoundsWanted.HasPositiveLogConvexCoefficients.sq_coeff_succ_le`, a theorem declared in [MathlibExt/RingTheory/PowerSeries/KaluzaCoefficientBounds.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/PowerSeries/KaluzaCoefficientBounds.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/kaluza-s-theorem-on-reciprocal-power-series/index.html#sq-coeff-succ-le).

## Kaluza's bounds for the coefficients of a reciprocal power series

Let
$f = \sum_n a_n X^n$ be a real formal power series with positive log-convex coefficients, and
let $f^{-1} = \sum_n b_n X^n$ be its reciprocal in the ring of formal power series. Then
$b_0 = a_0^{-1}$, $b_0 > 0$, and $-a_n / a_0^2 \le b_n \le 0$ for every $n \ge 1$.

The reciprocal is formal; no convergence is assumed.

## Sources

- László Tóth, *Alternating Sums Concerning Multiplicative Arithmetic Functions*, Journal of Integer Sequences 20, the lemma at lines 553–562 of <https://cs.uwaterloo.ca/journals/JIS/VOL20/Toth/toth25.tex>. Tóth attributes the nonpositivity of `bₙ` to T. Kaluza, Satz 3.

Formalized by `MathlibExt.Algebra.PowerSeries.KaluzaCoefficientBoundsWanted.kaluza_coeff_inv_bounds`, a theorem declared in [MathlibExt/RingTheory/PowerSeries/KaluzaCoefficientBounds.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/PowerSeries/KaluzaCoefficientBounds.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/kaluza-s-theorem-on-reciprocal-power-series/index.html#kaluza-coeff-inv-bounds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kaluza's theorem on reciprocal power series](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/formal-power-series/kaluza-s-theorem-on-reciprocal-power-series/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/formal-power-series/kaluza-s-theorem-on-reciprocal-power-series)
