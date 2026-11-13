---
declaration: section
origin: cited
lean: MetaMathlibExt.doubleExcedanceCount, MetaMathlibExt.doubleExcedanceCount_one, MetaMathlibExt.generalizedEulerianSeries, MetaMathlibExt.generalizedEulerianP, MetaMathlibExt.generalizedEulerianP_zero_left, MetaMathlibExt.cyclicExcedanceEGF_eq, MetaMathlibExt.generalizedEulerianP_eq_sum_perm, MetaMathlibExt.generalizedEulerianP_gamma_nonneg
statement: formalized
---

# Generalized Eulerian polynomials and gamma-positivity

11 results, 5 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/generalized-eulerian-polynomials-and-gamma-posit/index.html).

## Number of double excedances

For a permutation $w$ of $\{0, 1, \dots, n-1\}$, a double
excedance of $w$ is a point $i$ with $w^{-1}(i) < i < w(i)$, and $\mathrm{dexc}(w)$ is the
number of double excedances of $w$.

## Sources

- Pasquale Petrullo and Domenico Senato, *Generalized Eulerian Polynomials with a Nonnegative Gamma Vector*, Journal of Integer Sequences 27 (2024), Article 24.1.5, Section 4.

Formalized by `MetaMathlibExt.doubleExcedanceCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/generalized-eulerian-polynomials-and-gamma-posit/index.html#double-excedance-count).

## The identity has no double excedances

For every $n$, the identity permutation of
$\{0, 1, \dots, n-1\}$ has no double excedances.

## Sources

- Pasquale Petrullo and Domenico Senato, *Generalized Eulerian Polynomials with a Nonnegative Gamma Vector*, Journal of Integer Sequences 27 (2024), Article 24.1.5, Section 4.

Formalized by `MetaMathlibExt.doubleExcedanceCount_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/generalized-eulerian-polynomials-and-gamma-posit/index.html#double-excedance-count-one).

## Generating function of the generalized Eulerian polynomials

For rational numbers
$q$, $t$, $x$, $y$ with $x \ne y$, this is the formal power series in $z$ over $\mathbb{Q}$

$$\mathcal{P}(q, t; x, y; z) = \left(\frac{x - y}{x e^{yz} - y e^{xz}}\right)^q e^{(x+y)qtz}.$$

Here the base has constant term $1$, and its $q$-th power is the binomial series
$(1 + u)^q = \sum_{n \ge 0} \binom{q}{n} u^n$ with $u$ the base minus $1$. For $x = y$ the
denominator is zero and the formula above does not apply.

## Sources

- Pasquale Petrullo and Domenico Senato, *Generalized Eulerian Polynomials with a Nonnegative Gamma Vector*, Journal of Integer Sequences 27 (2024), Article 24.1.5, Equation (2).

Formalized by `MetaMathlibExt.generalizedEulerianSeries`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/generalized-eulerian-polynomials-and-gamma-posit/index.html#generalized-eulerian-series).

## Generalized Eulerian polynomials

For rational numbers $q, t, x, y$ and $n \ge 0$, the
generalized Eulerian polynomial $P_n(q, t; x, y)$ is $n!$ times the coefficient of $z^n$ in the
formal power series over $\mathbb{Q}$

$$\mathcal{P}(q, t; x, y; z) = \left(\frac{x - y}{x e^{yz} - y e^{xz}}\right)^q e^{(x + y) q t z},$$

where the $q$-th power is the binomial series $(1 + u)^q = \sum_{k \ge 0} \binom{q}{k} u^k$
applied to $u = \frac{x - y}{x e^{yz} - y e^{xz}} - 1$. When $x \ne y$ the quotient has constant
term $1$, so $u$ has constant term $0$; for $x = y$ the formula is degenerate and the value of
$P_n$ is a formal convention.

## Sources

- Pasquale Petrullo and Domenico Senato, *Generalized Eulerian Polynomials with a Nonnegative Gamma Vector*, Journal of Integer Sequences 27 (2024), Article 24.1.5, Equation (3).

Formalized by `MetaMathlibExt.generalizedEulerianP`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/generalized-eulerian-polynomials-and-gamma-posit/index.html#generalized-eulerian-p).

## Generalized Eulerian polynomials with zero cycle weight

For all rational numbers
$t, x, y$ and every $n \ge 0$, the generalized Eulerian polynomial satisfies
$P_0(0, t; x, y) = 1$ and $P_n(0, t; x, y) = 0$ for $n \ge 1$.

Indeed, for $q = 0$ the generating function of the polynomials $P_n(0, t; x, y)$ is $1$.

## Sources

- Pasquale Petrullo and Domenico Senato, *Generalized Eulerian Polynomials with a Nonnegative Gamma Vector*, Journal of Integer Sequences 27 (2024), Article 24.1.5, Equation (2).

Formalized by `MetaMathlibExt.generalizedEulerianP_zero_left`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/generalized-eulerian-polynomials-and-gamma-posit/index.html#generalized-eulerian-p-zero-left).

## Exponential generating function of excedances over cyclic permutations

Let $x \ne 1$ be
a rational number. For $n \ge 1$ let $C_n(x) = \sum_{m=0}^{n} C_{n,m} x^m$, where the circular
Eulerian number $C_{n,m}$ is the number of permutations $w$ of $\{0, 1, \dots, n-1\}$ whose points
all lie in a single cycle and which have exactly $m$ excedances, that is, points $i$ with
$w(i) > i$. Then, as formal power series in $z$ over $\mathbb{Q}$,

$$\sum_{n \ge 1} C_n(x) \frac{z^n}{n!} = z + \log \frac{x - 1}{x e^z - e^{xz}},$$

where the quotient has constant term $1$ and $\log$ is the formal logarithm of a power series
with constant term $1$.

## Sources

- Pasquale Petrullo and Domenico Senato, *Generalized Eulerian Polynomials with a Nonnegative Gamma Vector*, Journal of Integer Sequences 27 (2024), Article 24.1.5, Proposition 1 (`jis-2024-24.1.5-prop-1`).

Stated but not proved: `MetaMathlibExt.cyclicExcedanceEGF_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/generalized-eulerian-polynomials-and-gamma-posit/index.html#cyclic-excedance-egf-eq).

## Permutation expansion of the generalized Eulerian polynomials

Let $P_n(q, t; x, y)$ be
the generalized Eulerian polynomial and let $S_n$ be the set of permutations of
$\{0, 1, \dots, n-1\}$. For $w \in S_n$ write $\mathrm{cyc}(w)$ for the number of cycles of $w$
(fixed points counted as cycles), $\mathrm{fix}(w)$ for the number of fixed points of $w$, and
$\mathrm{exc}(w)$ for the number of excedances of $w$, the points $i$ with $w(i) > i$. Then for
all rational numbers $q, t, x, y$ with $x \ne y$ and every $n \ge 0$,

$$
P_n(q, t; x, y) = \sum_{w \in S_n} q^{\mathrm{cyc}(w)} t^{\mathrm{fix}(w)} x^{\mathrm{exc}(w)}
y^{\mathrm{exc}(w^{-1})} (x + y)^{\mathrm{fix}(w)}.
$$

## Sources

- Pasquale Petrullo and Domenico Senato, *Generalized Eulerian Polynomials with a Nonnegative Gamma Vector*, Journal of Integer Sequences 27 (2024), Article 24.1.5, Theorem 2 (`jis-2024-24.1.5-thm-2`).

Stated but not proved: `MetaMathlibExt.generalizedEulerianP_eq_sum_perm` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/generalized-eulerian-polynomials-and-gamma-posit/index.html#generalized-eulerian-p-eq-sum-perm).

## The gamma coefficients of the generalized Eulerian polynomials have nonnegative integer coefficients

**The gamma coefficients of the generalized Eulerian polynomials have nonnegative integer
coefficients.** Fix $n \ge 0$ and let $P_n(q, t; x, y)$ be the generalized Eulerian polynomial.
There are natural numbers $c_{k,i,j}$, for $k, i, j \ge 0$, such that, writing
$\gamma_{n,k}(q, t) = \sum_{i=0}^{n} \sum_{j=0}^{n} c_{k,i,j} q^i t^j$, for all rational numbers
$q, t, x, y$ with $x \ne y$,

$$
P_n(q, t; x, y) = \sum_{k=0}^{\lfloor n/2 \rfloor} \gamma_{n,k}(q, t) x^k y^k (x + y)^{n - 2k}.
$$

That is, the gamma coefficients $\gamma_{n,k}$ are polynomials in $q$ and $t$ with nonnegative
integer coefficients.

## Sources

- Pasquale Petrullo and Domenico Senato, *Generalized Eulerian Polynomials with a Nonnegative Gamma Vector*, Journal of Integer Sequences 27 (2024), Article 24.1.5, Theorem 4 (`jis-2024-24.1.5-thm-4`).

Stated but not proved: `MetaMathlibExt.generalizedEulerianP_gamma_nonneg` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/generalized-eulerian-polynomials-and-gamma-posit/index.html#generalized-eulerian-p-gamma-nonneg).

## Unimodality of the generalized Eulerian polynomials

Let $P_n(q, t; x, y)$ be the
generalized Eulerian polynomial. For all natural numbers $q$, $t$ and $n$ there are a polynomial
$p$ with rational coefficients $p_0, p_1, p_2, \dots$ and an index $m$ such that
$p(x) = P_n(q, t; x, 1)$ for every rational $x \ne 1$, $p_i \le p_{i+1}$ for every $i < m$, and
$p_{i+1} \le p_i$ for every $i \ge m$. That is, $P_n(q, t; x, 1)$ is a unimodal polynomial in $x$.

Only unimodality is asserted, not symmetry of the coefficients.

## Sources

- Pasquale Petrullo and Domenico Senato, *Generalized Eulerian Polynomials with a Nonnegative Gamma Vector*, Journal of Integer Sequences 27 (2024), Article 24.1.5, Corollary 5 (`jis-2024-24.1.5-cor-5`).

Stated but not proved: `MetaMathlibExt.generalizedEulerianP_unimodal` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/generalized-eulerian-polynomials-and-gamma-posit/index.html#generalized-eulerian-p-unimodal).

## The gamma coefficients of the generalized Eulerian polynomials count permutations

Fix
$n \ge 0$ and let $P_n(q, t; x, y)$ be the generalized Eulerian polynomial. For a permutation $w$
of $\{0, 1, \dots, n-1\}$ write $\mathrm{cyc}(w)$ for its number of cycles (fixed points counted
as cycles), $\mathrm{fix}(w)$ for its number of fixed points, $\mathrm{exc}(w)$ for its number of
excedances (points $i$ with $w(i) > i$) and $\mathrm{dexc}(w)$ for its number of double
excedances. For $k \ge 0$ and rational $q, t$ let $\gamma_{n,k}(q, t)$ be the sum of
$q^{\mathrm{cyc}(w)} t^{\mathrm{fix}(w)}$ over the permutations $w$ of $\{0, 1, \dots, n-1\}$
with $\mathrm{exc}(w) = k$ and $\mathrm{dexc}(w) = 0$. Then for all rational $q, t, x, y$ with
$x \ne y$,

$$
P_n(q, t; x, y) = \sum_{k=0}^{\lfloor n/2 \rfloor} \gamma_{n,k}(q, t) x^k y^k (x + y)^{n - 2k},
$$

and for every $k \ge 0$ and all rational $q, t$,
$\gamma_{n,k}(q, t) = \sum_{i=0}^{n} \sum_{j=0}^{n} \gamma_{n,k,i,j} q^i t^j$, where
$\gamma_{n,k,i,j}$ is the number of permutations $w$ of $\{0, 1, \dots, n-1\}$ with
$\mathrm{exc}(w) = k$, $\mathrm{dexc}(w) = 0$, $\mathrm{cyc}(w) = i$ and $\mathrm{fix}(w) = j$.

## Sources

- Pasquale Petrullo and Domenico Senato, *Generalized Eulerian Polynomials with a Nonnegative Gamma Vector*, Journal of Integer Sequences 27 (2024), Article 24.1.5, Theorem 7 (`jis-2024-24.1.5-thm-7`).

Stated but not proved: `MetaMathlibExt.generalizedEulerianP_gamma_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/generalized-eulerian-polynomials-and-gamma-posit/index.html#generalized-eulerian-p-gamma-eq).

## Generalized Eulerian polynomials at $x = -1$, $y = 1$

Let $P_m(q, t; x, y)$ be the
generalized Eulerian polynomial. For a permutation $w$ write $\mathrm{cyc}(w)$ for its number of
cycles (fixed points counted as cycles), $\mathrm{exc}(w)$ for its number of excedances (points
$i$ with $w(i) > i$) and $\mathrm{dexc}(w)$ for its number of double excedances, and let $D_{2n}$
be the set of derangements (permutations without fixed points) of $\{0, 1, \dots, 2n-1\}$. Then
for all rational numbers $q, t$ and every $n \ge 0$, $P_{2n+1}(q, t; -1, 1) = 0$ and

$$
(-1)^n P_{2n}(q, t; -1, 1) = \sum_{w \in D_{2n}} q^{\mathrm{cyc}(w)} (-1)^{n - \mathrm{exc}(w)}
= \sum_{w \in D_{2n},\ \mathrm{exc}(w) = n,\ \mathrm{dexc}(w) = 0} q^{\mathrm{cyc}(w)},
$$

where the exponent $n - \mathrm{exc}(w)$ is an integer, possibly negative.

## Sources

- Pasquale Petrullo and Domenico Senato, *Generalized Eulerian Polynomials with a Nonnegative Gamma Vector*, Journal of Integer Sequences 27 (2024), Article 24.1.5, Corollary 8 (`jis-2024-24.1.5-cor-8`).

Stated but not proved: `MetaMathlibExt.generalizedEulerianP_neg_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GeneralizedEulerianGammaWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/generalized-eulerian-polynomials-and-gamma-posit/index.html#generalized-eulerian-p-neg-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized Eulerian polynomials and gamma-positivity](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/generalized-eulerian-polynomials-and-gamma-posit/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/eulerian-numbers/generalized-eulerian-polynomials-and-gamma-posit)
