---
declaration: section
origin: cited
lean: MetaMathlibExt.wintner_mean_value, MetaMathlibExt.euler_product_mean_value, MetaMathlibExt.wintner_mean_value_multivariable
statement: formalized
proof: formalized
---

# Wintner's mean-value theorem

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/wintner-s-mean-value-theorem/index.html).

## Wintner's mean-value theorem

Let $f$ be a complex-valued arithmetic function, let $\mu$
be the Möbius function, and let $\mu * f$ be their Dirichlet convolution,
$(\mu * f)(n) = \sum_{d \mid n} \mu(d) f(n/d)$. If the series $\sum_{n \ge 1} |(\mu * f)(n)|/n$
converges, then

$$\frac{1}{x} \sum_{n=1}^{x} f(n) \to \sum_{n \ge 1} \frac{(\mu * f)(n)}{n}$$

as the integer $x$ tends to infinity.

No multiplicativity, Euler product, quantitative error term, or alternating mean is assumed or
concluded.

## Sources

- László Tóth, *On the Asymptotic Density of k-tuples of Positive Integers with Pairwise Non-Coprime Components*, Journal of Integer Sequences 27 (2024), Article 24.8.5, mean-value definition and Theorem `Th_Wintner_gen`, lines 292–310 (the `k = 1` case identified at lines 297–298 as Wintner's classical theorem; the source theorem itself is Ushiroya's multivariable generalization), <https://cs.uwaterloo.ca/journals/JIS/VOL27/Toth/toth27.tex>.

Formalized by `MetaMathlibExt.wintner_mean_value`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/WintnerMeanValue.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/WintnerMeanValue.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/wintner-s-mean-value-theorem/index.html#wintner-mean-value).

## Euler product for mean values of coordinatewise multiplicative functions

Let $k$ be a natural
number, write $\mathbb{N} = \{0, 1, 2, \dots\}$, and let $f \colon \mathbb{N}^k \to \mathbb{C}$
satisfy $f(a_1 b_1, \dots, a_k b_k) = f(a) f(b)$ for all $a, b \in \mathbb{N}^k$ with
$\gcd(a_i, b_i) = 1$ for every $i$. For a prime $p$ and $\nu = (\nu_1, \dots, \nu_k) \in
\mathbb{N}^k$ write $p^\nu = (p^{\nu_1}, \dots, p^{\nu_k})$, $|\nu| = \nu_1 + \dots + \nu_k$ and

$$
(\mu * f)(p^\nu) = \sum_{d_1 \mid p^{\nu_1}, \dots, d_k \mid p^{\nu_k}}
\mu(d_1) \cdots \mu(d_k) \, f(p^{\nu_1} / d_1, \dots, p^{\nu_k} / d_k),
$$

where $\mu$ is the Möbius function and each $d_i$ runs over the positive divisors of $p^{\nu_i}$.
Suppose that the family $|(\mu * f)(p^\nu)| / p^{|\nu|}$, indexed by the pairs $(p, \nu)$ of a
prime $p$ and a nonzero $\nu \in \mathbb{N}^k$, is summable. Then there is a complex number $M$
such that

$$
\frac{1}{N^k} \sum_{n \in \{1, \dots, N\}^k} f(n) \to M \quad (N \to \infty)
$$

and

$$
M = \prod_p \Bigl(1 - \frac{1}{p}\Bigr)^k \sum_{\nu \in \mathbb{N}^k} \frac{f(p^\nu)}{p^{|\nu|}},
$$

where the product runs over all primes and the product and the inner sums are unconditional (an
unconditional sum that does not converge is read as $0$, a product as $1$).

This is the Wintner–Ushiroya theorem (Ushiroya, Theorem 4; Tóth, Proposition 19) under a
stronger multiplicativity hypothesis: the source asks for $f(a_1 b_1, \dots, a_k b_k) = f(a) f(b)$
only when $\gcd(a_1 \cdots a_k, b_1 \cdots b_k) = 1$. The hypothesis used here forces $f$ to be a
product of one-variable multiplicative functions of the coordinates, and the proof reduces to the
one-variable Wintner theorem in each coordinate. The averages over the cubes $\{1, \dots, N\}^k$
are the diagonal of the source's multi-parameter limit, so they converge to the same value.

## Sources

- László Tóth, "On the Asymptotic Density of k-tuples of Positive Integers with Pairwise Non-Coprime Components," Journal of Integer Sequences 27 (2024), Article 24.8.5, Theorem (unlabeled; multiplicative-function form), equation, lines 314–326, https://cs.uwaterloo.ca/journals/JIS/VOL27/Toth/toth27.tex

Formalized by `MetaMathlibExt.euler_product_mean_value`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/EulerProductMeanValue.lean, line 894](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/EulerProductMeanValue.lean#L894). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/wintner-s-mean-value-theorem/index.html#euler-product-mean-value).

## Wintner's mean-value theorem in several variables

Let $k \ge 1$ and let $f$ be a
complex-valued function on $k$-tuples of natural numbers. For a $k$-tuple
$n = (n_1, \dots, n_k)$ of positive integers put

$$
(\mu * f)(n) = \sum_{d_1 \mid n_1, \dots, d_k \mid n_k}
\mu(d_1) \cdots \mu(d_k) \, f(n_1/d_1, \dots, n_k/d_k),
$$

where $\mu$ is the Möbius function and the $d_i$ run over positive divisors. If the series

$$\sum_{m \in \mathbb{Z}_{\ge 1}^k} \frac{|(\mu * f)(m)|}{m_1 \cdots m_k}$$

converges, then

$$
\frac{1}{x_1 \cdots x_k} \sum_{n_1 = 1}^{x_1} \cdots \sum_{n_k = 1}^{x_k} f(n_1, \dots, n_k)
\to \sum_{m \in \mathbb{Z}_{\ge 1}^k} \frac{(\mu * f)(m)}{m_1 \cdots m_k}
$$

as the integers $x_1, \dots, x_k$ all tend to infinity.

## Sources

- László Tóth, "On the Asymptotic Density of k-tuples of Positive Integers with Pairwise Non-Coprime Components," Journal of Integer Sequences 27 (2024), Article 24.8.5, Theorem `Th_Wintner_gen`, lines 300–311, <https://cs.uwaterloo.ca/journals/JIS/VOL27/Toth/toth27.tex>. Proved by H. Ushiroya (2012) as a generalization of Wintner's classical one-variable theorem.

Formalized by `MetaMathlibExt.wintner_mean_value_multivariable`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/WintnerMeanValueMultivariable.lean, line 849](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/WintnerMeanValueMultivariable.lean#L849). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/wintner-s-mean-value-theorem/index.html#wintner-mean-value-multivariable).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Wintner's mean-value theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/wintner-s-mean-value-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/wintner-s-mean-value-theorem)
