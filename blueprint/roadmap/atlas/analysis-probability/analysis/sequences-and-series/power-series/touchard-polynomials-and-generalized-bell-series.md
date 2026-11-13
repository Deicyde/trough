---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry4InnerSummable.ramanujan_part1_ch3_entry4_inner_summable, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry9IiGeneralizedbellgeneratingDefining.generalizedBellGenerating, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry9IiGeneralizedbellgeneratingDefining.ramanujan_part1_ch3_entry9_ii_generalizedbellgenerating_defining, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry4.ramanujan_part1_ch3_entry4, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry5.ramanujan_part1_ch3_entry5, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry9IiGeneralizedbellgenerating.ramanujan_part1_ch3_entry9_ii_generalizedbellgenerating, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Section8Example4Integrable.f, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Section8Example4Integrable.ramanujan_part1_ch3_section8_example4_integrable
statement: formalized
proof: formalized
---

# Touchard polynomials and generalized Bell series

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/touchard-polynomials-and-generalized-bell-series/index.html).

## Absolute convergence of Ramanujan's Bell-type series (Entry 4)

For every complex
number $x$ and every natural number $n$, the series
$\sum_{j=0}^{\infty} \frac{(j+1)^n x^{j+1}}{j!}$ converges absolutely.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 4, formula (4.1), printed pp. 47--48 / PDF pp. 57--58.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry4InnerSummable.ramanujan_part1_ch3_entry4_inner_summable`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry4InnerSummable.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry4InnerSummable.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/touchard-polynomials-and-generalized-bell-series/index.html#ramanujan-part1-ch3-entry4-inner-summabl).

## Ramanujan's generalized Bell function

For complex numbers $a$, $b$, $x$ and a natural
number $n$, the generalized Bell function is
$F(a, b, x; n) = e^{-x} \sum_{k=0}^{\infty} \frac{(a + b(k + 1))^n x^{k+1}}{k!}$.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, definition (9.1).

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry9IiGeneralizedbellgeneratingDefining.generalizedBellGenerating`, a definition declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry9IiGeneralizedbellgeneratingDefining.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry9IiGeneralizedbellgeneratingDefining.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/touchard-polynomials-and-generalized-bell-series/index.html#generalized-bell-generating).

## Convergence of the generalized Bell series

Let $F$ denote Ramanujan's generalized Bell
function. For complex numbers $a$, $b$, $x$ and every natural number $n$, the series
$\sum_{k=0}^{\infty} (a + b(k + 1))^n x^{k+1} / k!$ converges absolutely and its sum is
$e^{x} F(a, b, x; n)$.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, definition (9.1) printed p. 53/PDF p. 63 and Entry 9(ii), formula (9.4), printed p. 54/PDF p. 64.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry9IiGeneralizedbellgeneratingDefining.ramanujan_part1_ch3_entry9_ii_generalizedbellgenerating_defining`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry9IiGeneralizedbellgeneratingDefining.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry9IiGeneralizedbellgeneratingDefining.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/touchard-polynomials-and-generalized-bell-series/index.html#ramanujan-part1-ch3-entry9-ii-generalize-2).

## Exponential generating function of Ramanujan's Bell-type series (Entry 4)

Let $F$ be
Ramanujan's generalized Bell function. For all complex numbers $a$ and $x$, let
$f(x, n) = F(0, 1, x; n) = e^{-x} \sum_{j=0}^{\infty} \frac{(j+1)^n x^{j+1}}{j!}$ for natural
numbers $n$, and set $f(x, -1) = 1$. Then the series
$\sum_{n=0}^{\infty} \frac{a^n}{n!} f(x, n-1)$ converges absolutely and its sum is
$e^{x(e^a - 1)}$.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 4, formula (4.1), printed pp. 47--48 / PDF pp. 57--58. The source's `f(x, n) = e^{-x} ∑_{j ≥ 0} (j + 1)ⁿ xʲ⁺¹ / j!` is `generalizedBellGenerating 0 1 x n`.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry4.ramanujan_part1_ch3_entry4`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry4.lean, line 480](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry4.lean#L480). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/touchard-polynomials-and-generalized-bell-series/index.html#ramanujan-part1-ch3-entry4).

## Binomial recurrence for Ramanujan's Bell-type series (Entry 5)

Let $F$ be Ramanujan's
generalized Bell function. For every natural number $n$ and every complex number $x$, write
$f(x, m) = F(0, 1, x; m)$ for natural numbers $m$, and set $f(x, -1) = 1$. Then
$f(x, n) = x \sum_{k=0}^{n} \binom{n}{k} f(x, k-1)$.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 5, printed p. 48 / PDF p. 58.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry5.ramanujan_part1_ch3_entry5`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry5.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry5.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/touchard-polynomials-and-generalized-bell-series/index.html#ramanujan-part1-ch3-entry5).

## Exponential generating function of the generalized Bell function (Entry 9(ii))

Let
$F(a, b, x; n)$ be Ramanujan's generalized Bell function. For all complex numbers $a$, $b$, $x$
and $y$, the series $\sum_{n=0}^{\infty} \frac{y^n}{n!} F(a, b, x; n)$ converges to
$x e^{(a+b)y} e^{x(e^{by} - 1)}$.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, definition (9.1) printed p. 53/PDF p. 63 and Entry 9(ii), formula (9.4), printed p. 54/PDF p. 64. The source's `F(a, b, x; n)` is `generalizedBellGenerating a b x n`.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry9IiGeneralizedbellgenerating.ramanujan_part1_ch3_entry9_ii_generalizedbellgenerating`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry9IiGeneralizedbellgenerating.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry9IiGeneralizedbellgenerating.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/touchard-polynomials-and-generalized-bell-series/index.html#ramanujan-part1-ch3-entry9-ii-generalize).

## Generalized Bell function extended to $n = -1$

For an integer $n \ge -1$ and a complex
number $x$, $f(n, x) = 1$ if $n = -1$, and otherwise $f(n, x)$ is the generalized Bell function
$F(0, 1, x; n) = e^{-x} \sum_{k \ge 0} (k + 1)^n x^{k + 1} / k!$.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Section 8, Example 4 and its correction, printed pp. 51--52 / PDF pp. 61--62.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Section8Example4Integrable.f`, a definition declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Section8Example4Integrable.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Section8Example4Integrable.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/touchard-polynomials-and-generalized-bell-series/index.html#f).

## Integrability of the scaled generalized Bell integrand on $(0, 1)$

Let $f$ be the
generalized Bell function extended to $n = -1$. For every natural number $m$ and every complex
number $x$, the complex-valued function $t \mapsto x f(m - 1, t x)$ of a real variable $t$ is
interval integrable on $[0, 1]$ with respect to Lebesgue measure.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Section 8, Example 4 and its correction, printed pp. 51--52 / PDF pp. 61--62.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Section8Example4Integrable.ramanujan_part1_ch3_section8_example4_integrable`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Section8Example4Integrable.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Section8Example4Integrable.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/touchard-polynomials-and-generalized-bell-series/index.html#ramanujan-part1-ch3-section8-example4-in).

## Ramanujan's integral formula with Bernoulli numbers

Let $f(-1, x) = 1$ and, for natural
numbers $n$, let $f(n, x) = e^{-x} \sum_{j=0}^{\infty} (j + 1)^n x^{j+1} / j!$ for complex $x$.
Let $B_n$ be the Bernoulli numbers, with $B_1 = -1/2$. Then for every natural number $m$ and every
complex number $x$,

$$\int_0^1 x\, f(m - 1, t x)\, dt = \sum_{k=0}^{m} \binom{m}{k} B_{m-k} \frac{f(k, x)}{k + 1}.$$

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Section 8, Example 4 and its correction, printed pp. 51--52 / PDF pp. 61--62.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Section8Example4BernoulliIntegral.ramanujan_part1_ch3_section8_example4_bernoulli_integral`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Section8Example4BernoulliIntegral.lean, line 975](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Section8Example4BernoulliIntegral.lean#L975). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/touchard-polynomials-and-generalized-bell-series/index.html#ramanujan-part1-ch3-section8-example4-be).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Touchard polynomials and generalized Bell series](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/power-series/touchard-polynomials-and-generalized-bell-series/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/sequences-and-series/power-series/touchard-polynomials-and-generalized-bell-series)
