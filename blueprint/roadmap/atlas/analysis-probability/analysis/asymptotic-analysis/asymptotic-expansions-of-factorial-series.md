---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry5Digamma.chapter6Section13ExampleCTerm, MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry5Digamma.chapter6Section13ExampleCSum, MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry5Digamma.summable_chapter6Section13ExampleCTerm, MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry5Digamma.chapter6Section13ExampleCTerm_succ, MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry5Digamma.chapter6Section13ExampleCSum_eq, MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry5Digamma.isBigO_chapter6Section13ExampleCSum_sub_sum_bell, MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry5Digamma.ramanujan_part1_ch6_entry5_digamma, MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry3Psisummable.ramanujan_part1_ch3_entry3_psisummable_general
statement: formalized
proof: formalized
---

# Asymptotic expansions of factorial series

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html).

## Terms of Ramanujan's factorial series

For a real number $x$ and a natural number $j$,
the $j$-th term of Ramanujan's factorial series is $(-1)^j / ((x + 1)(x + 2) \cdots (x + j + 1))$,
read as $0$ when the denominator vanishes.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry5Digamma.chapter6Section13ExampleCTerm`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry5Digamma.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry5Digamma.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html#chapter6-section13-example-cterm).

## Ramanujan's factorial series

For a real number $x$, $C(x)$ is the sum
$\sum_{j \ge 0} (-1)^j / ((x + 1)(x + 2) \cdots (x + j + 1))$ of Ramanujan's factorial series,
where a term is read as $0$ when its denominator vanishes and the sum is taken to be $0$ when
the series is not summable.

The series is summable for every $x > 0$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry5Digamma.chapter6Section13ExampleCSum`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry5Digamma.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry5Digamma.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html#chapter6-section13-example-csum).

## Convergence of Ramanujan's factorial series

For every real $x > 0$, the series
$\sum_{j \ge 0} (-1)^j / ((x + 1)(x + 2) \cdots (x + j + 1))$ is summable.

Its $j$-th term is bounded in absolute value by $1 / (j + 1)!$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry5Digamma.summable_chapter6Section13ExampleCTerm`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry5Digamma.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry5Digamma.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html#summable-chapter6-section13-example-cter).

## Recursion for the terms of Ramanujan's factorial series

Write
$c_j(x) = (-1)^j / ((x + 1)(x + 2) \cdots (x + j + 1))$ for the $j$-th term of Ramanujan's
factorial series, with division by $0$ read as $0$. For every real $x$ and every natural number
$j$, $c_{j+1}(x) = -\frac{1}{x + 1} \, c_j(x + 1)$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry5Digamma.chapter6Section13ExampleCTerm_succ`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry5Digamma.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry5Digamma.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html#chapter6-section13-example-cterm-succ).

## Functional equation of Ramanujan's factorial series

Let
$C(x) = \sum_{j \ge 0} (-1)^j / ((x + 1)(x + 2) \cdots (x + j + 1))$ be Ramanujan's factorial
series. For every real $x > 0$, $C(x) = \frac{1}{x + 1} - \frac{C(x + 1)}{x + 1}$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry5Digamma.chapter6Section13ExampleCSum_eq`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry5Digamma.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry5Digamma.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html#chapter6-section13-example-csum-eq).

## Asymptotic expansion of Ramanujan's factorial series

Let
$C(x) = \sum_{j \ge 0} (-1)^j / ((x + 1)(x + 2) \cdots (x + j + 1))$ be Ramanujan's factorial
series and let $B_n$ denote the $n$-th Bell number. For every natural number $N$,

$$C(x) - \sum_{j=0}^{N-1} \frac{(-1)^j B_{j+1}}{x^{j+1}} = O\left(\frac{1}{x^{N+1}}\right)
\quad \text{as } x \to \infty.$$

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry5Digamma.isBigO_chapter6Section13ExampleCSum_sub_sum_bell`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry5Digamma.lean, line 556](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry5Digamma.lean#L556). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html#is-big-o-chapter6-section13-example-csum).

## Convergence and asymptotic expansion of Ramanujan's factorial series

Let
$c_j(x) = (-1)^j / ((x + 1)(x + 2) \cdots (x + j + 1))$, let $C(x) = \sum_{j \ge 0} c_j(x)$,
and let $B_n$ denote the $n$-th Bell number. For all sufficiently large real $x$, $x > 0$ and the
series $\sum_{j \ge 0} c_j(x)$ is summable; and for every natural number $N$,

$$C(x) - \sum_{j=0}^{N-1} \frac{(-1)^j B_{j+1}}{x^{j+1}} = O\left(\frac{1}{x^{N+1}}\right)
\quad \text{as } x \to \infty.$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 6.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch6.Entry5Digamma.ramanujan_part1_ch6_entry5_digamma`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch6Entry5Digamma.lean, line 752](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch6Entry5Digamma.lean#L752). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html#ramanujan-part1-ch6-entry5-digamma).

## Summability of Ramanujan's factorial series in a sector, for every $x$

Let $x$ be a
complex number and let $\varepsilon > 0$ be a real number. Then there is a real number $R$ such
that for every complex number $z$ with $|z| \ge R$ whose principal argument satisfies
$-\pi + \varepsilon \le \arg z \le \pi - \varepsilon$, the series
$\sum_{j=0}^{\infty} \frac{(-1)^j x^{j+1}}{(z+1)(z+2)\cdots(z+j+1)}$ is summable.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry3Psisummable.ramanujan_part1_ch3_entry3_psisummable_general`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry3Psisummable.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry3Psisummable.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html#ramanujan-part1-ch3-entry3-psisummable-g).

## Summability of Ramanujan's factorial series in a sector

Let $x$ be a nonzero complex
number and let $\varepsilon$ be a real number with $0 < \varepsilon < \pi$. Then there is a real
number $R$ such that for every complex number $z$ with $|z| \ge R$ whose principal argument
satisfies $-\pi + \varepsilon \le \arg z \le \pi - \varepsilon$, the series
$\sum_{j=0}^{\infty} \frac{(-1)^j x^{j+1}}{(z+1)(z+2)\cdots(z+j+1)}$ is summable.

The hypotheses $x \neq 0$ and $\varepsilon < \pi$ are not needed for the proof; they are kept to
match the source.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 3, printed p. 47 / PDF p. 57. It follows from `ramanujan_part1_ch3_entry3_psisummable_general`; the hypotheses `x ≠ 0` and `ε < π` are unused and keep the source's shape.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry3Psisummable.ramanujan_part1_ch3_entry3_psisummable`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry3Psisummable.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry3Psisummable.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html#ramanujan-part1-ch3-entry3-psisummable).

## Ramanujan's product series

For complex numbers $a$, $b$, $x$, $z$, Ramanujan's product
series of Entry 9(i) is

$$P(a, b, x; z) = \sum_{j=0}^{\infty} \frac{(-b)^j x^{j+1}}{\prod_{r=0}^{j} (z + a + b(r + 1))}.$$

The definition is totalized: a quotient with vanishing denominator is taken to be $0$, and the sum
of a non-summable series is taken to be $0$. Hence at a pole of the source expression, for example
$a = 0$, $b = 1$, $x = 1$, $z = -1$, where every product contains the vanishing factor
$z + a + b = 0$, every term and so $P$ itself equals $0$, whereas the source expression has a
singularity there. Off the poles, when $b \neq 0$ and $w = (z + a)/b$ is nonzero and satisfies
$|\arg w| \le \pi - \varepsilon$ for some $0 < \varepsilon < \pi$, the closed form of Ramanujan's
product series identifies $P$ with the source's closed form.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry9Odd.entry9_P`, a definition declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry9Odd.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry9Odd.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html#entry9-p).

## Closed form of Ramanujan's product series off the poles

Let $a, b, x, z \in \mathbb{C}$
with $b \neq 0$, let $0 < \varepsilon < \pi$, and put $w = (z + a)/b$. Suppose that $w \neq 0$,
that $-\pi + \varepsilon \le \arg w \le \pi - \varepsilon$, and that $w + r + 1 \neq 0$ for every
natural number $r$. Then Ramanujan's product series $P$ satisfies

$$P(a, b, x; z) = e^{-x} \sum_{m=0}^{\infty} \frac{x^{m+1}}{m!\,(z + a + b(m + 1))}.$$

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry9Odd.entry9_P_closed`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry9Odd.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry9Odd.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html#entry9-p-closed).

## Asymptotic expansion of Ramanujan's product series

Let $a, b, x \in \mathbb{C}$ with
$b \neq 0$, let $0 < \varepsilon < \pi$, and let $n$ be a natural number. Write $F(a, b, x; k)$
for Ramanujan's generalized Bell function and $P(a, b, x; z)$ for Ramanujan's product series.
Then

$$P(a, b, x; z) = \sum_{k=0}^{n} \frac{(-1)^k F(a, b, x; k)}{z^{k+1}} + O(|z|^{-n-2})$$

as $|(z + a)/b| \to \infty$ with $-\pi + \varepsilon \le \arg((z + a)/b) \le \pi - \varepsilon$:
there are real numbers $C$ and $R$ such that the difference of the two sides has absolute value
at most $C / |z|^{n+2}$ for every complex $z$ with $|(z + a)/b| \ge R$ and
$-\pi + \varepsilon \le \arg((z + a)/b) \le \pi - \varepsilon$.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 9(i), definitions printed p. 53 / PDF p. 63 and result printed p. 54 / PDF p. 64.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry9Odd.ramanujan_part1_ch3_entry9_odd`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry9Odd.lean, line 814](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry9Odd.lean#L814). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html#ramanujan-part1-ch3-entry9-odd).

## Entry 3 coefficients as generalized Bell values

Let $F$ be Ramanujan's generalized Bell
function. For every complex number $x$ and every natural number $j$, let
$f(x, j) = e^{-x} \sum_{k=0}^{\infty} \frac{(k+1)^j x^{k+1}}{k!}$. Then
$f(x, j) = F(0, 1, x; j)$.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry3.fCoeff_eq_generalizedBellGenerating`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry3.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry3.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html#f-coeff-eq-generalized-bell-generating).

## Ramanujan's factorial series as the Entry 9 product series at $a = 0$, $b = 1$

Let $P$ be
Ramanujan's Entry 9(i) product series. For all complex numbers $x$ and $z$, let
$\psi(x, z) = \sum_{j=0}^{\infty} t_j$, where $t_j = \frac{(-1)^j x^{j+1}}{(z+1)(z+2)\cdots(z+j+1)}$
when the product in the denominator is nonzero and $t_j = 0$ otherwise. Then
$\psi(x, z) = P(0, 1, x; z)$.

Since division by zero is taken to give zero, the case distinction in $t_j$ changes nothing.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry3.psi_eq_entry9_P`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry3.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry3.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html#psi-eq-entry9-p).

## Asymptotic expansion of Ramanujan's factorial series, for every $x$

Let $x$ be a complex
number. For natural numbers $j$ let
$f(x, j) = e^{-x} \sum_{k=0}^{\infty} \frac{(k+1)^j x^{k+1}}{k!}$, and for complex $z$ let
$\psi(x, z) = \sum_{j=0}^{\infty} t_j$, where
$t_j = \frac{(-1)^j x^{j+1}}{(z+1)(z+2)\cdots(z+j+1)}$ when the denominator is nonzero and
$t_j = 0$ otherwise. Let $\varepsilon$ be a real number with $0 < \varepsilon < \pi$, and let
$S_\varepsilon$ be the set of complex $z$ whose principal argument satisfies
$-\pi + \varepsilon \le \arg z \le \pi - \varepsilon$. Then for every natural number $N$,

$$\psi(x, z) - \sum_{j=0}^{N} \frac{(-1)^j f(x, j)}{z^{j+1}} = O\left(\frac{1}{z^{N+2}}\right)$$

as $|z| \to \infty$ with $z \in S_\varepsilon$.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry3.ramanujan_part1_ch3_entry3_general`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry3.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry3.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html#ramanujan-part1-ch3-entry3-general).

## Ramanujan's asymptotic expansion of a factorial series

Let $x$ be a nonzero complex
number. For natural numbers $j$ let
$f(x, j) = e^{-x} \sum_{k=0}^{\infty} \frac{(k+1)^j x^{k+1}}{k!}$, and for complex $z$ let
$\psi(x, z) = \sum_{j=0}^{\infty} t_j$, where
$t_j = \frac{(-1)^j x^{j+1}}{(z+1)(z+2)\cdots(z+j+1)}$ when the denominator is nonzero and
$t_j = 0$ otherwise. Let $\varepsilon$ be a real number with $0 < \varepsilon < \pi$, and let
$S_\varepsilon$ be the set of complex $z$ whose principal argument satisfies
$-\pi + \varepsilon \le \arg z \le \pi - \varepsilon$. Then for every natural number $N$,

$$\psi(x, z) - \sum_{j=0}^{N} \frac{(-1)^j f(x, j)}{z^{j+1}} = O\left(\frac{1}{z^{N+2}}\right)$$

as $|z| \to \infty$ with $z \in S_\varepsilon$.

The hypothesis $x \neq 0$ is not needed for the proof; it is kept to match the source.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 3, printed p. 47 / PDF p. 57.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry3.ramanujan_part1_ch3_entry3`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry3.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry3.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html#ramanujan-part1-ch3-entry3).

## Convergence of Ramanujan's product series in a sector

Let $a, b, x \in \mathbb{C}$ with
$b \neq 0$ and let $0 < \varepsilon < \pi$. Then there is a real number $R$ such that for every
complex $z$ with $|(z + a)/b| \ge R$ and $-\pi + \varepsilon \le \arg((z + a)/b) \le
\pi - \varepsilon$, the series

$$\sum_{j=0}^{\infty} \frac{(-b)^j x^{j+1}}{\prod_{r=0}^{j} (z + a + b(r + 1))}$$

converges absolutely.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Entry 9(i), definitions printed p. 53 / PDF p. 63 and result printed p. 54 / PDF p. 64. It follows from `Complex.summable_neg_pow_mul_pow_div_prod_add_mul`: the upper sector bound keeps `(z + a) / b` off the negative real axis, so no factor of the denominator vanishes. The hypothesis `hεlt`, the radius (taken to be `0`) and the lower sector bound are unused and keep the source's shape.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Entry9OddProductsummable.ramanujan_part1_ch3_entry9_odd_productsummable`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry9OddProductsummable.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Entry9OddProductsummable.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html#ramanujan-part1-ch3-entry9-odd-productsu).

## Asymptotic expansion of a factorial series

Let $a_0, a_1, \ldots$ be complex numbers, let
$\psi : \mathbb{C} \to \mathbb{C}$, let $\lambda$ be either a real number or $-\infty$, and let
$0 < \varepsilon < \pi/2$. Suppose that for every complex $z$ that is not a negative integer and
satisfies $\operatorname{Re} z > \lambda$, the series

$$\sum_{j=0}^{\infty} \frac{(-1)^j a_j}{(z + 1)(z + 2) \cdots (z + j + 1)}$$

converges absolutely with sum $\psi(z)$. Write $S(n, k)$ for the Stirling numbers of the second
kind and $c_j = \sum_{k=0}^{j} a_k S(j + 1, k + 1)$. Then for every natural number $N$ there are
real numbers $C \ge 0$ and $R > 0$ such that

$$\Big|\psi(z) - \sum_{j=0}^{N} \frac{(-1)^j c_j}{z^{j+1}}\Big| \le \frac{C}{|z|^{N+2}}$$

for every complex $z$ that is not a negative integer, satisfies $\operatorname{Re} z > \lambda$
and $|z| \ge R$, and lies in the sector $|\arg z| \le \pi/2 - \varepsilon$ when
$\lambda = -\infty$, or $|\arg(z - \lambda)| \le \pi/2 - \varepsilon$ when $\lambda$ is real.

For $\lambda = -\infty$ the expansion is stated on the sector $|\arg z| \le \pi/2 - \varepsilon$,
as for real $\lambda$; on the wider sector $|\arg z| \le \pi - \varepsilon$ it fails, for example
for $a_j = j!\,(-2/3)^j$.

Proof: Use convergence at one real point to obtain absolute convergence two units to the right,
then expand each $1/((z + 1)\cdots(z + j + 1))$ termwise in powers of $1/z$ and bound the tail.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Section 8, Example 1, formula (8.1), printed p. 50 / PDF p. 60.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Section8Example1Asymptotic.ramanujan_part1_ch3_section8_example1_asymptotic`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Section8Example1Asymptotic.lean, line 738](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Section8Example1Asymptotic.lean#L738). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html#ramanujan-part1-ch3-section8-example1-as).

## Convergence of a factorial series in a sector, general form

Let $a_0, a_1, \ldots$ be
complex numbers, let $\lambda$ be either a real number or $-\infty$, and let $\varepsilon > 0$.
Suppose that the series

$$\sum_{j=0}^{\infty} \frac{(-1)^j a_j}{(z + 1)(z + 2) \cdots (z + j + 1)}$$

converges absolutely for every complex $z$ that is not a negative integer and satisfies
$\operatorname{Re} z > \lambda$. Then there is a real number $R$ such that the series converges
absolutely for every complex $z$ with $|z| > R$ that lies in the sector
$|\arg(z - \lambda)| \le \pi/2 - \varepsilon$ when $\lambda$ is real, or
$|\arg z| \le \pi - \varepsilon$ when $\lambda = -\infty$.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Section8Example1Summable.ramanujan_part1_ch3_section8_example1_summable_general`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Section8Example1Summable.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Section8Example1Summable.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html#ramanujan-part1-ch3-section8-example1-su).

## Convergence of a factorial series in a sector

Let $a_0, a_1, \ldots$ be complex numbers,
let $\lambda$ be either a real number or $-\infty$, and let $\varepsilon > 0$, with
$\varepsilon < \pi/2$ when $\lambda$ is real and $\varepsilon < \pi$ when $\lambda = -\infty$.
Suppose that the series

$$\sum_{j=0}^{\infty} \frac{(-1)^j a_j}{(z + 1)(z + 2) \cdots (z + j + 1)}$$

converges absolutely for every complex $z$ that is not a negative integer and satisfies
$\operatorname{Re} z > \lambda$. Then there is a real number $R$ such that the series converges
absolutely for every complex $z$ with $|z| > R$ that lies in the sector
$|\arg(z - \lambda)| \le \pi/2 - \varepsilon$ when $\lambda$ is real, or
$|\arg z| \le \pi - \varepsilon$ when $\lambda = -\infty$.

## Sources

- Berndt, Ramanujan's Notebooks Part I, Chapter 3, Section 8, Example 1, formula (8.1), printed p. 50 / PDF p. 60. It follows from `ramanujan_part1_ch3_section8_example1_summable_general`; the upper bound `heps_lt` is unused and keeps the source's shape.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch3.Section8Example1Summable.ramanujan_part1_ch3_section8_example1_summable`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch3Section8Example1Summable.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Ramanujan/Part1Ch3Section8Example1Summable.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html#ramanujan-part1-ch3-section8-example1-su-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Asymptotic expansions of factorial series](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/asymptotic-analysis/asymptotic-expansions-of-factorial-series)
