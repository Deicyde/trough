---
declaration: section
origin: cited
lean: MetaMathlibExt.TIntegrand, MetaMathlibExt.IsPolyTFamily, MetaMathlibExt.tsum_div_centralBinom_mul_eq_multisection, MetaMathlibExt.tsum_div_mul_centralBinom_mul_eq_multisection, MetaMathlibExt.tsum_div_sq_mul_centralBinom_mul_eq_multisection, MetaMathlibExt.centralBinomReciprocalH, MetaMathlibExt.centralBinomReciprocalH_zero, MetaMathlibExt.arcsinAntiderivQCoeff
statement: formalized
---

# Series of reciprocal central binomial coefficients

36 results, 27 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html).

## Integrand of the antiderivative condition

Let $S$ be a sequence of real polynomials
indexed by the natural numbers, with terms $S(l)$. For a natural number $l$ and a real number
$x$, the integrand is

$$\frac{8x^l - S(l)(x)}{\sqrt{x}\,(4 - x)},$$

where $\sqrt{x} = 0$ for $x < 0$ and a quotient with denominator $0$ is $0$.

Formalized by `MetaMathlibExt.TIntegrand`, a definition declared in [MathlibExt/NumberTheory/PolynomialTL1.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PolynomialTL1.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#tintegrand).

## Polynomial family defined by an antiderivative

Let $S$ and $T$ be sequences of real
polynomials indexed by the natural numbers, with terms $S(l)$ and $T(l)$. The pair $(S, T)$
satisfies this predicate when $T(0) = 0$; for every $l \ge 1$ the polynomial $T(l)$ is nonzero
and has degree $l - 1$; and for every $l \ge 1$ and every real $x$ with $0 < x < 4$, the function
$y \mapsto 2\sqrt{y}\,T(l)(y)$ is differentiable at $x$ with derivative

$$\frac{8x^l - S(l)(x)}{\sqrt{x}\,(4 - x)}.$$

The term $T(l)$ stands for the polynomial $T_{l-1}$ of the source, so $T(0) = 0$ encodes the
convention $T_{-1} = 0$, and the derivative condition expresses $T_{l-1}(x)$ as
$\frac{1}{2\sqrt{x}}$ times an antiderivative of the displayed integrand.

Formalized by `MetaMathlibExt.IsPolyTFamily`, a definition declared in [MathlibExt/NumberTheory/PolynomialTL1.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PolynomialTL1.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#is-poly-tfamily).

## Multisection formula for $\sum_k x^k / \binom{2mk}{mk}$

Let $m \ge 1$ be a natural number
and $x$ a complex number with $|x| < 4^m$. Write $H(y) = \sum_{n \ge 0} y^n / \binom{2n}{n}$,
$w = e^{2\pi i/m}$, and let $x^{1/m}$ be the principal $m$-th root of $x$. Then

$$
\sum_{k \ge 0} \frac{x^k}{\binom{2mk}{mk}} = \frac{1}{m} \sum_{j=0}^{m-1} H(w^j x^{1/m}).
$$

## Sources

- Rimer Zurita, *Elementary Functions Associated with Series Involving Reciprocals of Central Binomial Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.6.8, Theorem 7 (`jis-2024-24.6.8-thm-7`).

Stated but not proved: `MetaMathlibExt.tsum_div_centralBinom_mul_eq_multisection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#tsum-div-central-binom-mul-eq-multisecti).

## Multisection formula for $\sum_k x^k / (k \binom{2mk}{mk})$

Let $m \ge 1$ be a natural
number and $x$ a complex number with $|x| < 4^m$. Write
$L(y) = \sum_{n \ge 1} y^n / (n \binom{2n}{n})$, $w = e^{2\pi i/m}$, and let $x^{1/m}$ be the
principal $m$-th root of $x$. Then

$$
\sum_{k \ge 1} \frac{x^k}{k \binom{2mk}{mk}} = \sum_{j=0}^{m-1} L(w^j x^{1/m}).
$$

## Sources

- Rimer Zurita, *Elementary Functions Associated with Series Involving Reciprocals of Central Binomial Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.6.8, Theorem 8 (`jis-2024-24.6.8-thm-8`).

Stated but not proved: `MetaMathlibExt.tsum_div_mul_centralBinom_mul_eq_multisection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#tsum-div-mul-central-binom-mul-eq-multis).

## Multisection formula for $\sum_k x^k / (k^2 \binom{2mk}{mk})$

Let $m \ge 1$ be a natural
number and $x$ a complex number with $|x| < 4^m$. Write
$K(y) = \sum_{n \ge 1} y^n / (n^2 \binom{2n}{n})$, $w = e^{2\pi i/m}$, and let $x^{1/m}$ be the
principal $m$-th root of $x$. Then

$$
\sum_{k \ge 1} \frac{x^k}{k^2 \binom{2mk}{mk}} = m \sum_{j=0}^{m-1} K(w^j x^{1/m}).
$$

## Sources

- Rimer Zurita, *Elementary Functions Associated with Series Involving Reciprocals of Central Binomial Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.6.8, Theorem 10 (`jis-2024-24.6.8-thm-10`).

Stated but not proved: `MetaMathlibExt.tsum_div_sq_mul_centralBinom_mul_eq_multisection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#tsum-div-sq-mul-central-binom-mul-eq-mul).

## Closed form of the reciprocal central binomial series

For every real number $x$, let

$$
H(x) = \frac{4\sqrt{x}\,\arcsin(\sqrt{x}/2)}{(4 - x)\sqrt{4 - x}} + \frac{4}{4 - x}.
$$

The formula is meant for $0 \le x < 4$, where by the paper
$H(x) = \sum_{n \ge 0} x^n / \binom{2n}{n}$.

## Sources

- Rimer Zurita, *Elementary Functions Associated with Series Involving Reciprocals of Central Binomial Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.6.8, Section 2.

Formalized by `MetaMathlibExt.centralBinomReciprocalH`, a definition declared in [WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#central-binom-reciprocal-h).

## The closed form $H$ equals $1$ at $0$

The function
$H(x) = \frac{4\sqrt{x}\,\arcsin(\sqrt{x}/2)}{(4 - x)\sqrt{4 - x}} + \frac{4}{4 - x}$ of a real
variable satisfies $H(0) = 1$.

## Sources

- Rimer Zurita, *Elementary Functions Associated with Series Involving Reciprocals of Central Binomial Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.6.8, Section 2.

Formalized by `MetaMathlibExt.centralBinomReciprocalH_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#central-binom-reciprocal-h-zero).

## Coefficients of Zurita's Q-polynomials

For natural numbers $l \ge 1$ and $k$, the rational
number $q_k = q_{l,k}$ is given by $q_l = -4/l$, by $q_k = \frac{4k + 6}{k} q_{k+1}$ for
$1 \le k < l$, by $q_0 = -12 q_1$, and by $q_k = 0$ for $k > l$. These are the coefficients of
Zurita's polynomial $Q_l$. For $l = 0$ the definition gives $q_{0,k} = 0$ for every $k$.

## Sources

- Rimer Zurita, *Elementary Functions Associated with Series Involving Reciprocals of Central Binomial Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.6.8, Definition 1.

Formalized by `MetaMathlibExt.arcsinAntiderivQCoeff`, a definition declared in [WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#arcsin-antideriv-qcoeff).

## Leading coefficient of a Q-polynomial

For every natural number $l \ge 1$, the coefficient
$q_l = q_{l,l}$ of $x^l$ in Zurita's polynomial $Q_l$ equals $-4/l$.

## Sources

- Rimer Zurita, *Elementary Functions Associated with Series Involving Reciprocals of Central Binomial Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.6.8, Definition 1.

Formalized by `MetaMathlibExt.arcsinAntiderivQCoeff_self`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#arcsin-antideriv-qcoeff-self).

## Recursion for the coefficients of a Q-polynomial

Write $q_k = q_{l,k}$ for the coefficient
of $x^k$ in Zurita's polynomial $Q_l$. For all natural numbers $k$ and $l$ with $1 \le k < l$,

$$q_k = \frac{4k + 6}{k}\, q_{k+1}.$$

## Sources

- Rimer Zurita, *Elementary Functions Associated with Series Involving Reciprocals of Central Binomial Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.6.8, Definition 1.

Formalized by `MetaMathlibExt.arcsinAntiderivQCoeff_of_lt`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#arcsin-antideriv-qcoeff-of-lt).

## Constant coefficient of a Q-polynomial

For every natural number $l \ge 1$, the constant
coefficient $q_0$ and the coefficient $q_1$ of $x$ in Zurita's polynomial $Q_l$ satisfy
$q_0 = -12 q_1$.

## Sources

- Rimer Zurita, *Elementary Functions Associated with Series Involving Reciprocals of Central Binomial Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.6.8, Definition 1.

Formalized by `MetaMathlibExt.arcsinAntiderivQCoeff_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#arcsin-antideriv-qcoeff-zero).

## Zurita's Q-polynomials

For a natural number $l \ge 1$, $Q_l$ is the polynomial with
rational coefficients $Q_l(x) = \sum_{i=0}^{l} q_i x^i$, where $q_l = -4/l$,
$q_i = \frac{4i + 6}{i} q_{i+1}$ for $1 \le i < l$, and $q_0 = -12 q_1$. For $l = 0$ it is the
constant polynomial $Q_0 = 8$.

## Sources

- Rimer Zurita, *Elementary Functions Associated with Series Involving Reciprocals of Central Binomial Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.6.8, Definition 1.

Formalized by `MetaMathlibExt.arcsinAntiderivQ`, a definition declared in [WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#arcsin-antideriv-q).

## Zurita's arcsine antiderivative constants

For a natural number $l \ge 1$, the rational
constant $C_l$ is $C_l = -q_0/2$, where $q_0$ is the constant coefficient of Zurita's polynomial
$Q_l$. For $l = 0$ it is $C_0 = -4$.

## Sources

- Rimer Zurita, *Elementary Functions Associated with Series Involving Reciprocals of Central Binomial Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.6.8, Definition 1.

Formalized by `MetaMathlibExt.arcsinAntiderivC`, a definition declared in [WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#arcsin-antideriv-c).

## The first two arcsine antiderivative constants

Zurita's constants satisfy $C_1 = -24$
and $C_2 = -120$, as in Table 1 of the paper.

## Sources

- Rimer Zurita, *Elementary Functions Associated with Series Involving Reciprocals of Central Binomial Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.6.8, Definition 1 and Table 1.

Formalized by `MetaMathlibExt.arcsinAntiderivC_one_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#arcsin-antideriv-c-one-two).

## Coefficients of Zurita's polynomial $S_l$

For natural numbers $l$ and $k$, the rational
number $s_k$ (which depends on $l$) is $0$ when $k > l$, and when $k \le l$ it is
$s_k = \frac{8}{1 - 2l} \prod_{i=k}^{l-1} \frac{8(i + 1)}{2i - 1}$. Equivalently, $s_l = 8/(1 - 2l)$
and $s_k = \frac{8(k + 1)}{2k - 1} s_{k+1}$ for $0 \le k < l$.

## Sources

- Rimer Zurita, *Elementary Functions Associated with Series Involving Reciprocals of Central Binomial Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.6.8, Definition 3.

Formalized by `MetaMathlibExt.arcsinAntiderivSCoeff`, a definition declared in [WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#arcsin-antideriv-scoeff).

## Leading coefficient of an S-polynomial

For every natural number $l$, the coefficient
$s_l = s_{l,l}$ of $x^l$ in Zurita's polynomial $S_l$ equals $8/(1 - 2l)$.

## Sources

- Rimer Zurita, *Elementary Functions Associated with Series Involving Reciprocals of Central Binomial Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.6.8, Definition 3.

Formalized by `MetaMathlibExt.arcsinAntiderivSCoeff_self`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#arcsin-antideriv-scoeff-self).

## Recursion for the coefficients of an S-polynomial

Write $s_k = s_{l,k}$ for the
coefficient of $x^k$ in Zurita's polynomial $S_l$. For all natural numbers $k$ and $l$ with
$k < l$,

$$s_k = \frac{8(k + 1)}{2k - 1}\, s_{k+1}.$$

## Sources

- Rimer Zurita, *Elementary Functions Associated with Series Involving Reciprocals of Central Binomial Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.6.8, Definition 3.

Formalized by `MetaMathlibExt.arcsinAntiderivSCoeff_of_lt`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#arcsin-antideriv-scoeff-of-lt).

## Zurita's S-polynomials

For a natural number $l$, $S_l$ is the polynomial with rational
coefficients $S_l(x) = \sum_{i=0}^{l} s_i x^i$, where $s_l = 8/(1 - 2l)$ and
$s_i = \frac{8(i + 1)}{2i - 1} s_{i+1}$ for $0 \le i < l$.

## Sources

- Rimer Zurita, *Elementary Functions Associated with Series Involving Reciprocals of Central Binomial Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.6.8, Definition 3.

Formalized by `MetaMathlibExt.arcsinAntiderivS`, a definition declared in [WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#arcsin-antideriv-s).

## Antiderivative of $x^l H(x)$

Let $l \ge 1$, let $Q_l$ and $C_l$ be Zurita's polynomial and
constant, and let $H$ be the closed form of the reciprocal central binomial series. Then there
is a polynomial $P$ with rational coefficients such that $P(0) = 0$ and
$2(4 - x) P'(x) = 8x^l - Q_l(x)$ as polynomials. Moreover, for every such $P$ and every real
number $x$ with $0 < x < 4$, the real function

$$
F(y) = P(y) + C_l \arcsin(\sqrt{y}/2)^2 +
\frac{\arcsin(\sqrt{y}/2)\,\sqrt{y}}{\sqrt{4 - y}}\, Q_l(y)
$$

has derivative $x^l H(x)$ at $x$.

Such a $P$ is unique: it is the paper's polynomial $P_l$ (Definition 2), and $F$ is an
antiderivative of $x^l H(x)$ on $0 < x < 4$.

## Sources

- Rimer Zurita, *Elementary Functions Associated with Series Involving Reciprocals of Central Binomial Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.6.8, Lemma 5 (`jis-2024-24.6.8-lem-5`).

Stated but not proved: `MetaMathlibExt.hasDerivAt_arcsinAntiderivP_pow_mul_centralBinomReciprocalH` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#has-deriv-at-arcsin-antideriv-p-pow-mul).

## Antiderivative of $x^{l - 1/2} H(x)$

Let $l \ge 0$, let $S_l$ be Zurita's polynomial, and
let $H$ be the closed form of the reciprocal central binomial series. Then there is a polynomial
$T$ with rational coefficients such that $(4 - x)(2x T'(x) + T(x)) = 8x^l - S_l(x)$ as
polynomials. Moreover, for every such $T$ and every real number $x$ with $0 < x < 4$, the real
function

$$
G(y) = T(y)\sqrt{y} + \frac{\arcsin(\sqrt{y}/2)}{\sqrt{4 - y}}\, S_l(y)
$$

has derivative $\frac{x^l}{\sqrt{x}} H(x)$ at $x$.

Such a $T$ is unique: it is the paper's polynomial $T_{l-1}$ (Definition 4, with $T_{-1} = 0$).

## Sources

- Rimer Zurita, *Elementary Functions Associated with Series Involving Reciprocals of Central Binomial Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.6.8, Lemma 6 (`jis-2024-24.6.8-lem-6`).

Stated but not proved: `MetaMathlibExt.hasDerivAt_arcsinAntiderivT_pow_mul_centralBinomReciprocalH` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CentralBinomialReciprocalMultisectionWanted.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#has-deriv-at-arcsin-antideriv-t-pow-mul).

## Coefficients of Zurita's polynomial $S_n$

For a natural number $n$, the rational numbers
$s_0, s_1, s_2, \dots$ are defined by $s_0 = 1/(1/2 - n)$ and
$s_k = \frac{k - 1 - n}{k - n + 1/2}\, s_{k-1}$ for every $k \ge 1$. Their first $n + 1$ terms are
the coefficients of $S_n(x) = \sum_{k=0}^{n} s_k x^k$.

## Sources

- Rimer Zurita, *Power Series Associated with Reciprocals of Generalized Central Binomial Coefficients*, INTEGERS 26 (2026), Article A2, Definition 1.

Formalized by `MetaMathlibExt.zuritaSCoeff`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#zurita-scoeff).

## Zurita's constant $c_n$

For a natural number $n$, let $s_n$ be the coefficient of $x^n$
in Zurita's polynomial $S_n(x) = \sum_{k=0}^n s_k x^k$. Then $c_n$ is the rational number
$s_n/2 - 1$. For $n = 1$ this gives $c_1 = 1$, the paper's convention.

## Sources

- Rimer Zurita, *Power Series Associated with Reciprocals of Generalized Central Binomial Coefficients*, INTEGERS 26 (2026), Article A2, Definition 2.

Formalized by `MetaMathlibExt.zuritaC`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#zurita-c).

## Reversed coefficients of Zurita's polynomial $T_{n-2}$

Fix a natural number $n$, let
$s_0, s_1, \dots$ be the coefficients of $S_n$ and let $c_n = s_n/2 - 1$. The rational numbers
$u_0, u_1, \dots$ are defined by $u_0 = -s_{n-1}/2 - c_n$ and
$u_{i+1} = \frac{(k + 1 - n)\, u_i + s_k/2}{k - n}$ with $k = n - 2 - i$, where the index
subtractions $n - 1$ and $n - 2 - i$ are truncated at $0$. For $n \ge 2$ they list the
coefficients of $T_{n-2}$ backwards, $t_{n-2-i} = u_i$ for $0 \le i \le n - 2$; thus
$t_{n-2} = -s_{n-1}/2 - c_n$ and $t_{k-1} = ((k + 1 - n) t_k + s_k/2)/(k - n)$ for
$k = n - 2, \dots, 1$.

## Sources

- Rimer Zurita, *Power Series Associated with Reciprocals of Generalized Central Binomial Coefficients*, INTEGERS 26 (2026), Article A2, Definition 2.

Formalized by `MetaMathlibExt.zuritaTCoeffRev`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#zurita-tcoeff-rev).

## Coefficients of Zurita's polynomial $T_{n-2}$

For natural numbers $n$ and $k$,
$t_k = u_{n-2-k}$, where $n - 2 - k$ is truncated at $0$ and $u_0, u_1, \dots$ are the reversed
coefficients of $T_{n-2}$: with $s_j$ the coefficients of $S_n$ and $c_n = s_n/2 - 1$,
$u_0 = -s_{n-1}/2 - c_n$ and $u_{i+1} = ((m + 1 - n) u_i + s_m/2)/(m - n)$ for
$m = n - 2 - i$, the indices $n - 1$ and $n - 2 - i$ being truncated at $0$. For $k \le n - 2$
these are the coefficients of $T_{n-2}(x) = \sum_{k=0}^{n-2} t_k x^k$; for $k > n - 2$,
$t_k = u_0$.

## Sources

- Rimer Zurita, *Power Series Associated with Reciprocals of Generalized Central Binomial Coefficients*, INTEGERS 26 (2026), Article A2, Definition 2.

Formalized by `MetaMathlibExt.zuritaTCoeff`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#zurita-tcoeff).

## Zurita's coefficients $m_k$

For a natural number $n$, the rational numbers
$m_0, m_1, \dots$ are defined by $m_0 = 2/(2n - 1)$ and
$m_k = \frac{2(k - n)}{2k - 2n + 1}\, m_{k-1}$ for $k \ge 1$. Zurita's polynomial $M_{n-1}$ is
$M_{n-1}(x) = \sum_{k=0}^{n-1} m_k x^k$.

## Sources

- Rimer Zurita, *Power Series Associated with Reciprocals of Generalized Central Binomial Coefficients*, INTEGERS 26 (2026), Article A2, Definition 3.

Formalized by `MetaMathlibExt.zuritaMCoeff`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#zurita-mcoeff).

## Zurita's constant $d_n$

For a natural number $n$, let $m_0, m_1, \dots$ be Zurita's
coefficients, given by $m_0 = 2/(2n - 1)$ and $m_k = \frac{2(k - n)}{2k - 2n + 1}\, m_{k-1}$ for
$k \ge 1$, so that $M_{n-1}(x) = \sum_{k=0}^{n-1} m_k x^k$ for $n \ge 1$. Then $d_n$ is the
rational number $m_{n-1}/2$ for $n \ge 1$, and $d_0 = m_0/2 = -1$. For $n = 1$ this gives
$d_1 = 1$, the paper's convention.

## Sources

- Rimer Zurita, *Power Series Associated with Reciprocals of Generalized Central Binomial Coefficients*, INTEGERS 26 (2026), Article A2, Definition 4.

Formalized by `MetaMathlibExt.zuritaD`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#zurita-d).

## Coefficients of Zurita's polynomial $N_{n-2}$

For natural numbers $n$ and $k$, let $m_k$
be Zurita's coefficient, given by $m_0 = 2/(2n - 1)$ and
$m_k = \frac{2(k - n)}{2k - 2n + 1}\, m_{k-1}$ for $k \ge 1$. This is the rational number
$m_k / (2(k - n + 1))$, taken to be $0$ when $k = n - 1$. For $k \le n - 2$ it is the
coefficient of $x^k$ in $N_{n-2}(x) = \frac12 \sum_{i=0}^{n-2} \frac{m_i x^i}{i - n + 1}$.

## Sources

- Rimer Zurita, *Power Series Associated with Reciprocals of Generalized Central Binomial Coefficients*, INTEGERS 26 (2026), Article A2, Definition 4.

Formalized by `MetaMathlibExt.zuritaNCoeff`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#zurita-ncoeff).

## Values from Zurita's Tables 1-4

For $n = 2$ the coefficients $s_0, s_1, s_2$ of $S_2$ are
$-2/3$, $-8/3$ and $16/3$, and the constants $c_2$ and $c_4$ equal $5/3$ and $93/35$. For $n = 3$
the coefficients $t_0, t_1$ of $T_1$ are $-1/10$ and $-3/5$, the coefficients $m_0, m_1, m_2$ of
$M_2$ are $2/5$, $8/15$ and $16/15$, the constant $d_3$ equals $8/15$, and the coefficients of
$x^0$ and $x^1$ in $N_1$ are $-3/30$ and $-8/30$.

In polynomial form: $S_2(x) = -2/3 - (8/3)x + (16/3)x^2$, $T_1(x) = -1/10 - (3/5)x$,
$M_2(x) = 2/5 + (8/15)x + (16/15)x^2$ and $N_1(x) = -(8x + 3)/30$.

## Sources

- Rimer Zurita, *Power Series Associated with Reciprocals of Generalized Central Binomial Coefficients*, INTEGERS 26 (2026), Article A2, Tables 1-4.

Formalized by `MetaMathlibExt.zurita_table_values`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#zurita-table-values).

## Zurita's polynomial $S_n$

For a natural number $n$ and a real number $x$,
$S_n(x) = \sum_{k=0}^{n} s_k x^k$, where $s_0 = 1/(1/2 - n)$ and
$s_k = \frac{k - 1 - n}{k - n + 1/2}\, s_{k-1}$ for $k \ge 1$ are the coefficients of $S_n$.

## Sources

- Rimer Zurita, *Power Series Associated with Reciprocals of Generalized Central Binomial Coefficients*, INTEGERS 26 (2026), Article A2, Definition 1.

Formalized by `MetaMathlibExt.zuritaS`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#zurita-s).

## Zurita's polynomial $T_{n-2}$

For a natural number $n$ and a real number $x$,
$T_{n-2}(x) = \sum_{k=0}^{n-2} t_k x^k$, where $t_0, t_1, \dots$ are the coefficients of
Zurita's polynomial $T_{n-2}$; for $n \le 1$ the sum is empty and $T_{n-2}(x) = 0$. For
$n \ge 2$ these coefficients are given by $t_{n-2} = -s_{n-1}/2 - c_n$ and
$t_{k-1} = ((k + 1 - n) t_k + s_k/2)/(k - n)$ for $k = n - 2, \dots, 1$, where
$s_0 = 1/(1/2 - n)$ and $s_k = \frac{k - 1 - n}{k - n + 1/2}\, s_{k-1}$ for $k \ge 1$ are the
coefficients of Zurita's polynomial $S_n$, and $c_n = s_n/2 - 1$.

## Sources

- Rimer Zurita, *Power Series Associated with Reciprocals of Generalized Central Binomial Coefficients*, INTEGERS 26 (2026), Article A2, Definition 2.

Formalized by `MetaMathlibExt.zuritaT`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#zurita-t).

## Zurita's polynomial $M_{n-1}$

For a natural number $n$, let $m_0, m_1, \dots$ be Zurita's
coefficients, given by $m_0 = 2/(2n - 1)$ and $m_k = \frac{2(k - n)}{2k - 2n + 1}\, m_{k-1}$ for
$k \ge 1$. Then $M_{n-1}$ is the real polynomial function
$M_{n-1}(x) = \sum_{k=0}^{n-1} m_k x^k$ (so $M_{-1} = 0$).

## Sources

- Rimer Zurita, *Power Series Associated with Reciprocals of Generalized Central Binomial Coefficients*, INTEGERS 26 (2026), Article A2, Definition 3.

Formalized by `MetaMathlibExt.zuritaM`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#zurita-m).

## Zurita's polynomial $N_{n-2}$

For a natural number $n$, let $m_0, m_1, \dots$ be Zurita's
coefficients, given by $m_0 = 2/(2n - 1)$ and $m_k = \frac{2(k - n)}{2k - 2n + 1}\, m_{k-1}$ for
$k \ge 1$. Then $N_{n-2}$ is the real polynomial function
$N_{n-2}(x) = \frac12 \sum_{k=0}^{n-2} \frac{m_k x^k}{k - n + 1}$, which is $0$ for $n \le 1$.

## Sources

- Rimer Zurita, *Power Series Associated with Reciprocals of Generalized Central Binomial Coefficients*, INTEGERS 26 (2026), Article A2, Definition 4.

Formalized by `MetaMathlibExt.zuritaN`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#zurita-n).

## Zurita's antiderivative of $x^{-n-1/2}\arcsin(\sqrt{x})/(1-x)^{3/2}$

Let $n \ge 1$, let
$c_n$ be Zurita's constant and let $S_n$ and $T_{n-2}$ be Zurita's polynomials (with
$T_{-1} = 0$). For every real $x$ with $0 < x < 1$, the function

$$
F(y) = \log|y - 1| + c_n \log y + \frac{T_{n-2}(y)}{y^{n-1}} +
\frac{\arcsin(\sqrt{y})\, S_n(y)}{y^{n-1/2} \sqrt{1 - y}}
$$

has derivative $x^{-n-1/2} \arcsin(\sqrt{x}) / (1 - x)^{3/2}$ at $x$.

## Sources

- Rimer Zurita, *Power Series Associated with Reciprocals of Generalized Central Binomial Coefficients*, INTEGERS 26 (2026), Article A2, Lemma 1.

Stated but not proved: `MetaMathlibExt.hasDerivAt_zurita_antiderivative_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#has-deriv-at-zurita-antiderivative-one).

## Zurita's antiderivative of $x^{-n-1/2}\arcsin(\sqrt{x})/\sqrt{1-x}$

Let $n \ge 1$, let
$d_n$ be Zurita's constant and let $M_{n-1}$ and $N_{n-2}$ be Zurita's polynomials (with
$N_{-1} = 0$). For every real $x$ with $0 < x < 1$, the function

$$
G(y) = d_n \log y - \frac{\arcsin(\sqrt{y}) \sqrt{y(1 - y)}\, M_{n-1}(y)}{y^n} +
\frac{N_{n-2}(y)}{y^{n-1}}
$$

has derivative $x^{-n-1/2} \arcsin(\sqrt{x}) / \sqrt{1 - x}$ at $x$.

## Sources

- Rimer Zurita, *Power Series Associated with Reciprocals of Generalized Central Binomial Coefficients*, INTEGERS 26 (2026), Article A2, Lemma 2.

Stated but not proved: `MetaMathlibExt.hasDerivAt_zurita_antiderivative_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#has-deriv-at-zurita-antiderivative-two).

## Zurita's series $\sum_{k > n} 4^k x^k / ((k - n)\binom{2k}{k})$

Let $n \ge 1$, let
$S_n(x) = \sum_{k=0}^n s_k x^k$ and $T_{n-2}$ be Zurita's polynomials (with $T_{-1} = 0$), and
let $x$ be real with $0 < x < 1$. Then

$$
\sum_{k > n} \frac{4^k x^k}{(k - n)\binom{2k}{k}} = x\, T_{n-2}(x) +
\sqrt{\frac{x}{1 - x}}\, \arcsin(\sqrt{x})\, S_n(x) +
\sum_{k=0}^{n-1} \Bigl(1 - \frac{4^k}{\binom{2k}{k}}\Bigr) \frac{x^k}{k - n} -
\Bigl(\frac12 \sum_{k=1}^{n} \frac{4^k s_{n-k}}{k \binom{2k}{k}}\Bigr) x^n.
$$

The source prints the range $|x| < 4$. The statement here is restricted to $0 < x < 1$, inside
the range $|x| < 1$ that the source's Theorem 1 gives in this case; since
$\binom{2k}{k} \le 4^k$, the series diverges for $x \ge 1$.

## Sources

- Rimer Zurita, *Power Series Associated with Reciprocals of Generalized Central Binomial Coefficients*, INTEGERS 26 (2026), Article A2, Corollary 1.

Stated but not proved: `MetaMathlibExt.tsum_four_pow_div_sub_mul_centralBinom` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#tsum-four-pow-div-sub-mul-central-binom).

## Zurita's series $\sum_{k > n} 4^k x^k / ((k - n)^2\binom{2k}{k})$

For $j \ge 1$ write
Zurita's polynomials as $S_j(x) = \sum_{k=0}^{j} s^{(j)}_k x^k$,
$T_{j-2}(x) = \sum_{k=0}^{j-2} t^{(j)}_k x^k$ and $M_{j-1}(x) = \sum_{k=0}^{j-1} m^{(j)}_k x^k$.
Let $n \ge 1$, let $x$ be real with $0 < x < 1$, and put

$$
r_k = \frac{t^{(n)}_{k-1}}{k - n} +
\frac{1}{2(k - n)} \sum_{l=0}^{k-1} s^{(n)}_l\, m^{(n-l)}_{k-l-1} +
\frac{4^k}{(k - n)^2} \Bigl(4^{-k} - \frac{1}{\binom{2k}{k}}\Bigr)
$$

for $1 \le k \le n - 1$ and

$$
q = -\frac{2^{2n+1}}{\binom{2n}{n}} + \sum_{l=0}^{n-2} s^{(n)}_l \Bigl(
\frac{4^{n-l}}{(n - l)\binom{2(n-l)}{n-l}} -
\frac12 \sum_{p=1}^{n-l-1} \frac{4^p\, m^{(n-l)}_{n-l-1-p}}{p(2p + 1)\binom{2p}{p}}\Bigr).
$$

Then

$$
\sum_{k > n} \frac{4^k x^k}{(k - n)^2 \binom{2k}{k}} =
\frac{2^{2n+1} x^n}{\binom{2n}{n}} \arcsin(\sqrt{x})^2 -
\arcsin(\sqrt{x}) \sqrt{x(1 - x)} \sum_{k=0}^{n-1} s^{(n)}_k M_{n-k-1}(x)\, x^k +
\sum_{k=1}^{n-1} r_k x^k + q x^n.
$$

## Sources

- Rimer Zurita, *Power Series Associated with Reciprocals of Generalized Central Binomial Coefficients*, INTEGERS 26 (2026), Article A2, Corollary 2.

Stated but not proved: `MetaMathlibExt.tsum_four_pow_div_sub_sq_mul_centralBinom` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedCentralBinomialArcsinWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html#tsum-four-pow-div-sub-sq-mul-central-bin).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Series of reciprocal central binomial coefficients](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/series-of-reciprocal-central-binomial-coefficien)
