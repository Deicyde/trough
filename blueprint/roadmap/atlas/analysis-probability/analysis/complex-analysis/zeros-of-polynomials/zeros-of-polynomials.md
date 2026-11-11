---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ComplementaryPolynomialsWanted.ComplexAnalysis.exists_complementary_polynomial_on_unit_circle, MathlibExt.Analysis.Complex.EnestromKakeya.enestrom_kakeya_zero_localization, MathlibExt.Analysis.Complex.JentzschPowerSeriesWanted.jentzsch_zeros_of_power_series_sections
statement: formalized
---

# Polynomials in the complex plane: its own results

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/zeros-of-polynomials/index.html).

Analytic behaviour of complex polynomials: location of zeros (Eneström–Kakeya, Sendov's problem, Jentzsch), flat and Littlewood polynomials, complementary polynomials and sup norms on the unit circle. Algebraic properties of polynomials go to Algebra; Mahler measure goes to NumberTheory.

## Complementary polynomial on the unit circle

Let $P$ be a complex polynomial with
$|P(z)| \le 1$ for every complex number $z$ with $|z| = 1$. Then there is a complex polynomial $Q$
with $\deg Q \le \deg P$ such that $|P(z)|^2 + |Q(z)|^2 = 1$ for every $z$ with $|z| = 1$. Here
the degree of the zero polynomial is taken to be $0$.

## Sources

- https://link.springer.com/article/10.1007/s00220-025-05302-9. Problem `exists_complementary_polynomial_on_unit_circle` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.ComplementaryPolynomialsWanted.ComplexAnalysis.exists_complementary_polynomial_on_unit_circle` is written with `theorem_wanted` in [WantedExt/Analysis/ComplementaryPolynomialsWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ComplementaryPolynomialsWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/zeros-of-polynomials/index.html#exists-complementary-polynomial-on-unit).

## Eneström–Kakeya theorem

Let $n \ge 1$ and let $a_0, a_1, \dots, a_n$ be positive real
numbers. Then every complex zero $z$ of the polynomial $f(z) = a_0 + a_1 z + \dots + a_n z^n$
satisfies $\rho_1 \le |z| \le \rho_2$, where $\rho_1$ and $\rho_2$ are the minimum and the maximum
of the ratios $a_k / a_{k+1}$ for $0 \le k \le n - 1$.

## Sources

- Karl Dilcher and Larry Ericksen, "Polynomials Whose Coefficients Are Stern Numbers," Journal of Integer Sequences 24 (2021), Article 21.10.3, Theorem 4.1 (quoted there as the classical Eneström–Kakeya theorem). <https://cs.uwaterloo.ca/journals/JIS/VOL24/Dilcher/dilcher51.tex>

Formalized by `MathlibExt.Analysis.Complex.EnestromKakeya.enestrom_kakeya_zero_localization`, a theorem declared in [MathlibExt/Analysis/Complex/EnestromKakeya.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/EnestromKakeya.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/zeros-of-polynomials/index.html#enestrom-kakeya-zero-localization).

## Jentzsch's theorem

Let $(a_k)_{k \ge 0}$ be complex numbers such that the power series
$\sum_{k \ge 0} a_k z^k$ has radius of convergence $1$, and for $n \ge 0$ let
$s_n(z) = \sum_{k=0}^{n} a_k z^k$ be its $n$-th partial sum. Then for every complex $z$ with
$|z| = 1$, every real $\varepsilon > 0$ and every natural number $N$, there are $n \ge N$ and a
root $w$ of the polynomial $s_n$ with $|w - z| < \varepsilon$.

Source: Dilcher and Ericksen, "Polynomials Whose Coefficients Are Stern Numbers", Theorem 4.3
(Jentzsch), https://cs.uwaterloo.ca/journals/JIS/VOL24/Dilcher/dilcher51.tex, lines 381-388.

Formalized by `MathlibExt.Analysis.Complex.JentzschPowerSeriesWanted.jentzsch_zeros_of_power_series_sections`, a theorem declared in [MathlibExt/Analysis/Complex/JentzschPowerSeries.lean, line 566](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/JentzschPowerSeries.lean#L566). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/zeros-of-polynomials/index.html#jentzsch-zeros-of-power-series-sections).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Polynomials in the complex plane](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/zeros-of-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/zeros-of-polynomials)
