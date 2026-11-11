---
declaration: section
origin: cited
lean: MetaMathlibExt.integral_exp_div_one_sub_exp_sub_eq_log_Gamma, MetaMathlibExt.sum_exp_mul_digamma_div_eq_mul_log_one_sub, MetaMathlibExt.eventually_jensen_hyperbolic_of_log_ratio_expansion, MetaMathlibExt.eventually_jensen_hyperbolic_coloredPartitions, MetaMathlibExt.eventually_jensen_hyperbolic_partitions_parts_mod
statement: formalized
---

# Hyperbolicity of Jensen polynomials

5 results, 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/hyperbolicity-of-jensen-polynomials/index.html).

## An integral formula for $\log \Gamma(1/N)$

For every real number $N > 0$,

$$
\int_0^\infty \left( \frac{e^{-x}}{x \left(1 - e^{-N x}\right)} - \frac{1}{N x^2} -
\left( \frac{1}{2} - \frac{1}{N} \right) \frac{e^{-x}}{x} \right) dx =
\log \Gamma\left( \frac{1}{N} \right) + \left( \frac{1}{2} - \frac{1}{N} \right) \log \frac{1}{N} -
\frac{1}{2} \log (2\pi).
$$

## Sources

- Jashan Bal, Fern Haraldson, Joshua Males and Ian Thompson, *Jensen Polynomials Associated with Wright's Circle Method: Hyperbolicity and Turán Inequalities*, INTEGERS 25 (2025), Article A36, Lemma 2.

Stated but not proved: `MetaMathlibExt.integral_exp_div_one_sub_exp_sub_eq_log_Gamma` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/JensenPolynomialsWrightCircleWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/JensenPolynomialsWrightCircleWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/hyperbolicity-of-jensen-polynomials/index.html#integral-exp-div-one-sub-exp-sub-eq-log).

## A twisted sum of digamma values

Let $p$ and $k$ be natural numbers with $1 \le k < p$,
and let $\psi = \Gamma'/\Gamma$ be the digamma function. Then

$$
\sum_{\alpha=1}^{p} e^{2\pi i k \alpha / p} \, \psi\left( \frac{\alpha}{p} \right) =
p \operatorname{Log}\left( 1 - e^{2\pi i k / p} \right),
$$

where $\operatorname{Log}$ is the principal branch of the complex logarithm.

## Sources

- Jashan Bal, Fern Haraldson, Joshua Males and Ian Thompson, *Jensen Polynomials Associated with Wright's Circle Method: Hyperbolicity and Turán Inequalities*, INTEGERS 25 (2025), Article A36, Lemma 3.

Stated but not proved: `MetaMathlibExt.sum_exp_mul_digamma_div_eq_mul_log_one_sub` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/JensenPolynomialsWrightCircleWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/JensenPolynomialsWrightCircleWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/hyperbolicity-of-jensen-polynomials/index.html#sum-exp-mul-digamma-div-eq-mul-log-one-s).

## Hyperbolicity of Jensen polynomials from a log-ratio expansion

Let $\alpha$, $A$ and
$\delta$ be sequences of positive real numbers indexed by $n \in \mathbb{N}$ with
$\delta(n) \to 0$, let $d \ge 1$ be an integer, and for $3 \le j \le d$ let $g_j$ be a real
sequence with $g_j(n) = o(\delta(n)^j)$ as $n \to \infty$. Suppose that for every natural number
$k \le d$,

$$
\log \frac{\alpha(n + k)}{\alpha(n)} = A(n) k - \delta(n)^2 k^2 + \sum_{j=3}^{d} g_j(n) k^j +
o(\delta(n)^d)
$$

as $n \to \infty$. Then for all sufficiently large $n$ the Jensen polynomial
$J_\alpha^{d,n}(X) = \sum_{j=0}^{d} \binom{d}{j} \alpha(n + j) X^j$ is hyperbolic: the number of
its real roots, counted with multiplicity, equals its degree.

The source also proves that suitably renormalized Jensen polynomials converge to the Hermite
polynomials; that conclusion is not part of this statement.

## Sources

- Jashan Bal, Fern Haraldson, Joshua Males and Ian Thompson, *Jensen Polynomials Associated with Wright's Circle Method: Hyperbolicity and Turán Inequalities*, INTEGERS 25 (2025), Article A36, Theorem 5, quoted there from Griffin, Ono, Rolen and Zagier.

Stated but not proved: `MetaMathlibExt.eventually_jensen_hyperbolic_of_log_ratio_expansion` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/JensenPolynomialsWrightCircleWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/JensenPolynomialsWrightCircleWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/hyperbolicity-of-jensen-polynomials/index.html#eventually-jensen-hyperbolic-of-log-rati).

## Eventual hyperbolicity for colored partitions

Let $r \ge 1$ and $d \ge 1$ be integers. For
$m \in \mathbb{N}$ let

$$
C_r(m) = \sum_{m_1 + \dots + m_r = m} p(m_1) \cdots p(m_r)
$$

be the number of $r$-colored partitions of $m$, where the sum runs over all $r$-tuples of natural
numbers with sum $m$ and $p$ is the partition function. Then for all sufficiently large $n$ the
Jensen polynomial $J^{d,n}(X) = \sum_{j=0}^{d} \binom{d}{j} C_r(n + j) X^j$ is hyperbolic: the
number of its real roots, counted with multiplicity, equals its degree.

In the source, $C_r(n)$ is the coefficient of $q^{tn}$ in $1/(q^t; q^t)_\infty^r$ for any
$t \ge 1$; the source also proves a Hermite-limit statement and higher order Turán inequalities,
which are not part of this statement.

## Sources

- Jashan Bal, Fern Haraldson, Joshua Males and Ian Thompson, *Jensen Polynomials Associated with Wright's Circle Method: Hyperbolicity and Turán Inequalities*, INTEGERS 25 (2025), Article A36, Theorem 3, part 1.

Stated but not proved: `MetaMathlibExt.eventually_jensen_hyperbolic_coloredPartitions` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/JensenPolynomialsWrightCircleWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/JensenPolynomialsWrightCircleWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/hyperbolicity-of-jensen-polynomials/index.html#eventually-jensen-hyperbolic-colored-par).

## Eventual hyperbolicity for partitions into parts $\equiv a \pmod{p}$

Let $p$ be a prime,
let $a$ be an integer with $1 \le a < p$, and let $d \ge 1$ be an integer. For $m \in \mathbb{N}$
let $b_{a,p}(m)$ be the number of partitions of $m$ all of whose parts are congruent to $a$
modulo $p$. Then for all sufficiently large $n$ the Jensen polynomial
$J^{d,n}(X) = \sum_{j=0}^{d} \binom{d}{j} b_{a,p}(n + j) X^j$ is hyperbolic: the number of its
real roots, counted with multiplicity, equals its degree.

In the source, $b_{a,p}(n)$ is the coefficient of $q^n$ in $1/(q^a; q^p)_\infty$, and the case
$a = 0$ is also admitted there, although $(1; q^p)_\infty = 0$; the source also gives an asymptotic
formula, a Hermite-limit statement and higher order Turán inequalities, which are not part of
this statement.

## Sources

- Jashan Bal, Fern Haraldson, Joshua Males and Ian Thompson, *Jensen Polynomials Associated with Wright's Circle Method: Hyperbolicity and Turán Inequalities*, INTEGERS 25 (2025), Article A36, Theorem 4, part 2.

Stated but not proved: `MetaMathlibExt.eventually_jensen_hyperbolic_partitions_parts_mod` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/JensenPolynomialsWrightCircleWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/JensenPolynomialsWrightCircleWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/hyperbolicity-of-jensen-polynomials/index.html#eventually-jensen-hyperbolic-partitions).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hyperbolicity of Jensen polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/hyperbolicity-of-jensen-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/hyperbolicity-of-jensen-polynomials)
