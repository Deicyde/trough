---
declaration: section
origin: cited
lean: MetaMathlibExt.truncatedLogPolynomial, MetaMathlibExt.truncatedLogLcm, MetaMathlibExt.truncatedLogLcm_four, MetaMathlibExt.scaledTruncatedLogPolynomial, MetaMathlibExt.map_scaledTruncatedLogPolynomial, MetaMathlibExt.truncatedLogResultantProduct, MetaMathlibExt.truncatedLogAuxProduct, MetaMathlibExt.truncatedLogAuxProduct_one
statement: formalized
---

# Discriminants of truncated logarithmic polynomials

19 results, 10 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia/index.html).

## Truncated logarithmic polynomial

For a natural number $n$, the truncated logarithmic
polynomial is $F_n(x) = 1 + x + \frac{x^2}{2} + \dots + \frac{x^n}{n} \in \mathbb{Q}[x]$.

## Sources

- Cullinan and Gajek-Leonard, *On the Discriminants of Truncated Logarithmic Polynomials*, INTEGERS 25 (2025), Article A39, Section 1.

Formalized by `MetaMathlibExt.truncatedLogPolynomial`, a definition declared in [WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia/index.html#truncated-log-polynomial).

## Least common multiple of $1, \dots, n$

For a natural number $n$, $L_n$ is the least common
multiple $\operatorname{lcm}(1, 2, \dots, n)$ of the integers from $1$ to $n$; in particular
$L_0 = 1$.

## Sources

- Cullinan and Gajek-Leonard, *On the Discriminants of Truncated Logarithmic Polynomials*, INTEGERS 25 (2025), Article A39, Section 1.

Formalized by `MetaMathlibExt.truncatedLogLcm`, a definition declared in [WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia/index.html#truncated-log-lcm).

## Least common multiple of $1, 2, 3, 4$

The least common multiple of the integers from $1$
to $4$ is $L_4 = \operatorname{lcm}(1, 2, 3, 4) = 12$.

## Sources

- Cullinan and Gajek-Leonard, *On the Discriminants of Truncated Logarithmic Polynomials*, INTEGERS 25 (2025), Article A39, Section 1.

Formalized by `MetaMathlibExt.truncatedLogLcm_four`, a theorem declared in [WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia/index.html#truncated-log-lcm-four).

## Scaled truncated logarithmic polynomial

For a natural number $n$, let
$L_n = \operatorname{lcm}(1, 2, \dots, n)$. The scaled truncated logarithmic polynomial is the
integer polynomial $\tilde F_n(x) = L_n + \sum_{j=1}^{n} (L_n / j)\, x^j$, where each quotient
$L_n / j$ is an integer.

## Sources

- Cullinan and Gajek-Leonard, *On the Discriminants of Truncated Logarithmic Polynomials*, INTEGERS 25 (2025), Article A39, Section 1.

Formalized by `MetaMathlibExt.scaledTruncatedLogPolynomial`, a definition declared in [WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia/index.html#scaled-truncated-log-polynomial).

## The scaled truncated logarithmic polynomial is $L_n F_n$

For a natural number $n$, let
$L_n = \operatorname{lcm}(1, 2, \dots, n)$, let $F_n(x) = 1 + x + x^2/2 + \cdots + x^n/n$ be the
truncated logarithmic polynomial and let $\tilde F_n \in \mathbb{Z}[x]$ be the scaled truncated
logarithmic polynomial. Mapping the coefficients of $\tilde F_n$ from $\mathbb{Z}$ to
$\mathbb{Q}$ gives the polynomial $L_n F_n$ in $\mathbb{Q}[x]$.

## Sources

- Cullinan and Gajek-Leonard, *On the Discriminants of Truncated Logarithmic Polynomials*, INTEGERS 25 (2025), Article A39, Section 1.

Formalized by `MetaMathlibExt.map_scaledTruncatedLogPolynomial`, a theorem declared in [WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia/index.html#map-scaled-truncated-log-polynomial).

## Resultant product for truncated logarithmic polynomials

For a natural number $n$, let
$F_n(x) = 1 + x + \frac{x^2}{2} + \dots + \frac{x^n}{n}$, let
$L_n = \operatorname{lcm}(1, \dots, n)$, and let $\tilde F_n = L_n F_n \in \mathbb{Z}[x]$. The
integer $\mathcal{P}_n$ is the resultant $\operatorname{Res}(1 + x + \dots + x^{n-1}, \tilde F_n)$.
For $n \ge 1$ the polynomial $1 + x + \dots + x^{n-1} = F_n'$ is monic, so
$\mathcal{P}_n = \prod_{\theta} \tilde F_n(\theta)$, the product over the roots $\theta$ of $F_n'$.

## Sources

- Cullinan and Gajek-Leonard, *On the Discriminants of Truncated Logarithmic Polynomials*, INTEGERS 25 (2025), Article A39, Equation (5).

Formalized by `MetaMathlibExt.truncatedLogResultantProduct`, a definition declared in [WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia/index.html#truncated-log-resultant-product).

## Auxiliary product for truncated logarithmic discriminants

For a natural number $m$, let
$f_m(x) = \sum_{k=0}^{m-1} x^k$ and $g_m(x) = c_m + \sum_{j=1}^{m-1} \frac{x^j}{j}$ in
$\mathbb{Q}[x]$, where $c_m = \frac{1}{m}$ for $m \ge 1$ and $c_0 = 0$. The rational number $X(m)$
is the resultant $\operatorname{Res}(f_m, g_m)$. For $m \ge 1$, since $f_m$ is monic with roots
$\omega^k$ for $1 \le k \le m-1$, where $\omega$ is a primitive $m$-th root of unity, this is
$X(m) = \prod_{k=1}^{m-1} g_m(\omega^k)$.

## Sources

- Cullinan and Gajek-Leonard, *On the Discriminants of Truncated Logarithmic Polynomials*, INTEGERS 25 (2025), Article A39, Section 4.

Formalized by `MetaMathlibExt.truncatedLogAuxProduct`, a definition declared in [WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia/index.html#truncated-log-aux-product).

## Auxiliary product at $m = 1$

The auxiliary product $X(m)$ takes the value $X(1) = 1$ at
$m = 1$; it is an empty product.

## Sources

- Cullinan and Gajek-Leonard, *On the Discriminants of Truncated Logarithmic Polynomials*, INTEGERS 25 (2025), Article A39, Section 4.

Formalized by `MetaMathlibExt.truncatedLogAuxProduct_one`, a theorem declared in [WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia/index.html#truncated-log-aux-product-one).

## Resultant product at $n = 1$

The resultant product satisfies $\mathcal{P}_1 = 1$; it is an
empty product.

## Sources

- Cullinan and Gajek-Leonard, *On the Discriminants of Truncated Logarithmic Polynomials*, INTEGERS 25 (2025), Article A39, Equation (5).

Formalized by `MetaMathlibExt.truncatedLogResultantProduct_one`, a theorem declared in [WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia/index.html#truncated-log-resultant-product-one).

## Exceptional primes for truncated logarithmic discriminants

For a natural number $m$, the
exceptional set $E_m$ is the set of primes $\ell$ with $m\ell \equiv 1 \pmod 4$ such that the
$\ell$-adic valuation of the auxiliary product $X(m)$ is positive or the $\ell$-adic valuation of
the harmonic number $Y(m) = H_m = 1 + \frac{1}{2} + \dots + \frac{1}{m}$ is positive.

The source's display joins the two valuation conditions with "and", but its text ("all prime
divisors of $X(m)$ and $Y(m)$") and its table ($E_3 = \{11\}$ with $11 \nmid X(3) = 13/36$) use
the union.

## Sources

- Cullinan and Gajek-Leonard, *On the Discriminants of Truncated Logarithmic Polynomials*, INTEGERS 25 (2025), Article A39, Section 4.

Formalized by `MetaMathlibExt.truncatedLogExceptionalPrimes`, a definition declared in [WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia/index.html#truncated-log-exceptional-primes).

## Positivity of the resultant product

For every natural number $n \ge 1$, the resultant
product $\mathcal{P}_n$ is a positive integer.

## Sources

- Cullinan and Gajek-Leonard, *On the Discriminants of Truncated Logarithmic Polynomials*, INTEGERS 25 (2025), Article A39, Lemma 1.

Stated but not proved: `MetaMathlibExt.truncatedLogResultantProduct_pos` is written with `theorem_wanted` in [WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia/index.html#truncated-log-resultant-product-pos).

## Nonsquare discriminants of $F_n$ for positive $n \equiv 0, 2, 3 \pmod 4$

Let
$F_n(x) = 1 + x + x^2/2 + \cdots + x^n/n$ be the truncated logarithmic polynomial and let
$n \ge 1$ be a natural number with $n \equiv 0$, $2$ or $3 \pmod 4$. Then the discriminant of
$F_n$ is not a square in $\mathbb{Q}$.

## Sources

- Cullinan and Gajek-Leonard, *On the Discriminants of Truncated Logarithmic Polynomials*, INTEGERS 25 (2025), Article A39, Proposition 1.

Stated but not proved: `MetaMathlibExt.not_isSquare_discr_truncatedLog_of_mod_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia/index.html#not-is-square-discr-truncated-log-of-mod).

## Nonsquare discriminants of truncated logarithmic polynomials

Let
$F_n(x) = 1 + x + x^2/2 + \cdots + x^n/n$ be the truncated logarithmic polynomial and let
$n \ge 1$. If $n \equiv 0$, $2$ or $3 \pmod 4$, or if $n \equiv 1 \pmod 4$ and $n = p^e$ for a
prime $p$ and an odd $e$, then the discriminant of $F_n$ is not a square in $\mathbb{Q}$.

## Sources

- Cullinan and Gajek-Leonard, *On the Discriminants of Truncated Logarithmic Polynomials*, INTEGERS 25 (2025), Article A39, Theorem 1.

Stated but not proved: `MetaMathlibExt.not_isSquare_discr_truncatedLog` is written with `theorem_wanted` in [WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia/index.html#not-is-square-discr-truncated-log).

## An odd prime $p$ does not divide $\mathcal{P}_{p^{2e}}$

Let $p$ be an odd prime, let
$e \ge 1$, and let $\mathcal{P}_n$ be the truncated logarithmic resultant product. Then $p$ does
not divide $\mathcal{P}_{p^{2e}}$.

## Sources

- Cullinan and Gajek-Leonard, *On the Discriminants of Truncated Logarithmic Polynomials*, INTEGERS 25 (2025), Article A39, Theorem 2.

Stated but not proved: `MetaMathlibExt.not_dvd_truncatedLogResultantProduct_of_even_power` is written with `theorem_wanted` in [WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia/index.html#not-dvd-truncated-log-resultant-product).

## Finiteness of square discriminants of $F_{mq}$ with $mq \equiv 1 \pmod 4$

Let
$F_n(x) = 1 + x + x^2/2 + \cdots + x^n/n$ be the truncated logarithmic polynomial and let
$m \ge 1$ be a natural number. Then there are only finitely many primes $q$ with
$mq \equiv 1 \pmod 4$ such that the discriminant of $F_{mq}$ is a square in $\mathbb{Q}$.

## Sources

- Cullinan and Gajek-Leonard, *On the Discriminants of Truncated Logarithmic Polynomials*, INTEGERS 25 (2025), Article A39, Theorem 3.

Stated but not proved: `MetaMathlibExt.finite_primes_isSquare_discr_truncatedLog` is written with `theorem_wanted` in [WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia/index.html#finite-primes-is-square-discr-truncated).

## A prime $p \equiv 1 \pmod 4$ does not divide $\mathcal{P}_{p^e}$

Let $p$ be a prime with
$p \equiv 1 \pmod 4$, let $e \ge 1$, and let $\mathcal{P}_n$ be the truncated logarithmic
resultant product. Then $p$ does not divide $\mathcal{P}_{p^e}$.

## Sources

- Cullinan and Gajek-Leonard, *On the Discriminants of Truncated Logarithmic Polynomials*, INTEGERS 25 (2025), Article A39, Theorem 4.

Stated but not proved: `MetaMathlibExt.not_dvd_truncatedLogResultantProduct_of_prime_power` is written with `theorem_wanted` in [WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia/index.html#not-dvd-truncated-log-resultant-product-2).

## Discriminants of $F_{p^e}$ for primes $p \equiv 1 \pmod 4$

Let $p$ be a prime with
$p \equiv 1 \pmod 4$, let $e \ge 1$, let $F_n(x) = 1 + x + x^2/2 + \cdots + x^n/n$ be the
truncated logarithmic polynomial and let $\mathcal{P}_n$ be the truncated logarithmic resultant
product. If $e$ is odd, the discriminant of $F_{p^e}$ is not a square in $\mathbb{Q}$. If $e$ is
even, the discriminant of $F_{p^e}$ is not a square in $\mathbb{Q}$ if and only if the integer
$\mathcal{P}_{p^e}$ is not a square in $\mathbb{Q}$.

## Sources

- Cullinan and Gajek-Leonard, *On the Discriminants of Truncated Logarithmic Polynomials*, INTEGERS 25 (2025), Article A39, Corollary 1.

Stated but not proved: `MetaMathlibExt.discr_truncatedLog_prime_power` is written with `theorem_wanted` in [WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia/index.html#discr-truncated-log-prime-power).

## Nonsquare discriminants of $F_{mq}$ for non-exceptional primes $q > m$

Let $m$ be a
natural number, let $E_m$ be the set of exceptional primes for truncated logarithmic
discriminants, and let $F_n(x) = 1 + x + x^2/2 + \cdots + x^n/n$ be the truncated logarithmic
polynomial. If $q$ is a prime with $q \notin E_m$, $q > m$ and $mq \equiv 1 \pmod 4$, then the
discriminant of $F_{mq}$ is not a square in $\mathbb{Q}$.

## Sources

- Cullinan and Gajek-Leonard, *On the Discriminants of Truncated Logarithmic Polynomials*, INTEGERS 25 (2025), Article A39, Theorem 5.

Stated but not proved: `MetaMathlibExt.not_isSquare_discr_truncatedLog_mul_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia/index.html#not-is-square-discr-truncated-log-mul-pr).

## Nonsquare discriminants of $F_{3q}$, $F_{5q}$ and $F_{7q}$

Let
$F_n(x) = 1 + x + x^2/2 + \cdots + x^n/n$ be the truncated logarithmic polynomial. For every
prime $q$, if $n = 3q$, $n = 5q$ or $n = 7q$, then the discriminant of $F_n$ is not a square in
$\mathbb{Q}$.

## Sources

- Cullinan and Gajek-Leonard, *On the Discriminants of Truncated Logarithmic Polynomials*, INTEGERS 25 (2025), Article A39, Proposition 2.

Stated but not proved: `MetaMathlibExt.not_isSquare_discr_truncatedLog_three_five_seven_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TruncatedLogDiscriminantWanted.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia/index.html#not-is-square-discr-truncated-log-three).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Discriminants of truncated logarithmic polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/discriminants-of-truncated-logarithmic-polynomia)
