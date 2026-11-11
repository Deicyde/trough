---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry2Corollary1DerivativeSeries.ramanujan_part1_ch3_entry2_corollary1_derivative_series, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry2Corollary2HarmonicSeries.harmonic_eq_mathlib_harmonic, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry2Corollary2HarmonicSeries.ramanujan_part1_ch3_entry2_corollary2_harmonic_series_mathlib, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry2Corollary2HarmonicSeries.ramanujan_part1_ch3_entry2_corollary2_harmonic_series, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry2Rightsummable.ramanujan_part1_ch3_entry2_rightsummable, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry2.ramanujan_part1_ch3_entry2, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry2Leftsummable.ramanujan_part1_ch3_entry2_leftsummable, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry2Formula23SeriesPair.ramanujan_part1_ch3_entry2_formula23_series_pair
statement: formalized
proof: formalized
---

# Transformations of factorial series

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/transformations-of-factorial-series/index.html).

## Two derivative series with the same sum (Chapter 3, Entry 2, Corollary 1)

Let $R > 1$, let
$f : \mathbb{C} \to \mathbb{C}$ be analytic on the open disc $|w| < R$, and let $z$ be a complex
number with $z + n \ne 0$ for every natural number $n$. Suppose that the double series
$\sum_{j, m \ge 0} \frac{(-1)^j}{z(z+1)\cdots(z+j)} \cdot \frac{f^{(j+m)}(0)}{m!}$ converges
absolutely. Then there is a complex number $c$ such that the series
$\sum_{k \ge 0} \frac{f^{(k)}(0)}{(z+k)\, k!}$ and
$\sum_{k \ge 0} \frac{(-1)^k f^{(k)}(1)}{z(z+1)\cdots(z+k)}$ both converge absolutely with sum $c$.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 2, Corollary 1, printed p. 46 / PDF p. 56.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry2Corollary1DerivativeSeries.ramanujan_part1_ch3_entry2_corollary1_derivative_series`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry2Corollary1DerivativeSeries.lean, line 404](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry2Corollary1DerivativeSeries.lean#L404). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/transformations-of-factorial-series/index.html#ramanujan-part1-ch3-entry2-corollary1-de).

## Agreement of two definitions of the harmonic numbers

For every natural number $n$, the
rational number $\sum_{k=0}^{n-1} \frac{1}{k+1}$ equals Mathlib's harmonic number
$H_n = \sum_{k=0}^{n-1} (k+1)^{-1}$.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry2Corollary2HarmonicSeries.harmonic_eq_mathlib_harmonic`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry2Corollary2HarmonicSeries.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry2Corollary2HarmonicSeries.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/transformations-of-factorial-series/index.html#harmonic-eq-mathlib-harmonic).

## Ramanujan's series for the harmonic numbers, with Mathlib's harmonic numbers

Let
$H_k = \sum_{i=0}^{k-1} (i+1)^{-1}$ be Mathlib's $k$-th harmonic number. For every complex number
$x$, the series $\sum_{k \ge 1} \frac{H_k x^k}{k!}$ and
$\sum_{k \ge 1} \frac{(-1)^{k-1} x^k}{k!\, k}$ converge absolutely, and
$\sum_{k=1}^{\infty} \frac{H_k x^k}{k!} = e^x \sum_{k=1}^{\infty} \frac{(-1)^{k-1} x^k}{k!\, k}$.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry2Corollary2HarmonicSeries.ramanujan_part1_ch3_entry2_corollary2_harmonic_series_mathlib`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry2Corollary2HarmonicSeries.lean, line 467](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry2Corollary2HarmonicSeries.lean#L467). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/transformations-of-factorial-series/index.html#ramanujan-part1-ch3-entry2-corollary2-ha).

## Ramanujan's series for the harmonic numbers (Chapter 3, Entry 2, Corollary 2)

Let
$H_k = \sum_{i=1}^{k} \frac{1}{i}$ be the $k$-th harmonic number. For every complex number $x$, the
series $\sum_{k \ge 1} \frac{H_k x^k}{k!}$ and $\sum_{k \ge 1} \frac{(-1)^{k-1} x^k}{k!\, k}$
converge absolutely, and $\sum_{k=1}^{\infty} \frac{H_k x^k}{k!} =
e^x \sum_{k=1}^{\infty} \frac{(-1)^{k-1} x^k}{k!\, k}$.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 2, formula (2.3) and Corollary 2, printed pp. 46--47 / PDF pp. 56--57.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry2Corollary2HarmonicSeries.ramanujan_part1_ch3_entry2_corollary2_harmonic_series`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry2Corollary2HarmonicSeries.lean, line 484](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry2Corollary2HarmonicSeries.lean#L484). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/transformations-of-factorial-series/index.html#ramanujan-part1-ch3-entry2-corollary2-ha-2).

## Convergence of the right side of Ramanujan's Chapter 3, Entry 2

For all complex numbers
$x$ and $z$ such that $z + r \ne 0$ for every natural number $r$, the series
$\sum_{j \ge 0} \frac{(-1)^j x^{j+1}}{z(z+1)\cdots(z+j)}$ converges absolutely.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 2, formula (2.1), printed p. 46 / PDF p. 56.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry2Rightsummable.ramanujan_part1_ch3_entry2_rightsummable`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry2Rightsummable.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry2Rightsummable.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/transformations-of-factorial-series/index.html#ramanujan-part1-ch3-entry2-rightsummable).

## Ramanujan's exponential transformation of a factorial series (Chapter 3, Entry 2)

For all
complex numbers $x$ and $z$ such that $z + r \ne 0$ for every natural number $r$, the series
$\sum_{j \ge 0} \frac{x^{j+1}}{(z+j)\, j!}$ converges absolutely, and its sum is
$e^x \sum_{j \ge 0} \frac{(-1)^j x^{j+1}}{z(z+1)\cdots(z+j)}$.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 2, formula (2.1), printed p. 46 / PDF p. 56.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry2.ramanujan_part1_ch3_entry2`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry2.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry2.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/transformations-of-factorial-series/index.html#ramanujan-part1-ch3-entry2).

## Convergence of the left side of Ramanujan's Chapter 3, Entry 2

For all complex numbers
$x$ and $z$ such that $z + r \ne 0$ for every natural number $r$, the series
$\sum_{j \ge 0} \frac{x^{j+1}}{(z+j)\, j!}$ converges absolutely.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 2, formula (2.1), printed p. 46 / PDF p. 56.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry2Leftsummable.ramanujan_part1_ch3_entry2_leftsummable`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry2.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry2.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/transformations-of-factorial-series/index.html#ramanujan-part1-ch3-entry2-leftsummable).

## Ramanujan's companion series transformation (Chapter 3, Entry 2, formula (2.3))

Let $x$
and $z$ be complex numbers with $z \ne -(n+1)$ for every natural number $n$. Then the series
$\sum_{j \ge 0} \frac{(-1)^j x^{j+1}}{(z+j+1)\, j!}$ converges absolutely, say with sum $S$, and
the series $\sum_{j \ge 0} \frac{x^{j+1}}{(z+1)(z+2)\cdots(z+j+1)}$ converges absolutely with sum
$e^x S$.

The identity follows from Entry 2 applied with $-x$ and $z + 1$ in place of $x$ and $z$, using
$e^x e^{-x} = 1$.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 2, formula (2.3) and Corollary 2, printed pp. 46--47 / PDF pp. 56--57.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry2Formula23SeriesPair.ramanujan_part1_ch3_entry2_formula23_series_pair`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry2Formula23SeriesPair.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry2Formula23SeriesPair.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/transformations-of-factorial-series/index.html#ramanujan-part1-ch3-entry2-formula23-ser).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Transformations of factorial series](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/transformations-of-factorial-series/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/sequences-and-series/power-series/transformations-of-factorial-series)
