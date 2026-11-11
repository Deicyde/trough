---
declaration: section
origin: cited
lean: Polynomial.IsPermutationPolynomial, Polynomial.IsKComplete, Polynomial.isKComplete_iff, Polynomial.isKComplete_mono, Polynomial.isKComplete_zero, Polynomial.isKComplete_succ_iff, Polynomial.isKComplete_self, MathlibExt.FieldTheory.HermiteDickson.hermite_dickson_permutation_criterion
statement: formalized
---

# Permutation polynomials

20 results, 8 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html).

## Permutation polynomial over a finite field

A polynomial $f$ over a finite field $F$ is a
permutation polynomial when its evaluation map $F \to F$, $x \mapsto f(x)$, is bijective.

Formalized by `Polynomial.IsPermutationPolynomial`, a definition declared in [MathlibExt/FieldTheory/Finite/PermutationPolynomial.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/FieldTheory/Finite/PermutationPolynomial.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html#is-permutation-polynomial).

## Polynomial complete to level $k$

Let $F$ be a finite field,
$f \in F[X]$ and $k$ a natural number. The polynomial $f$ is complete to level $k$ ($k$-complete)
when $f + iX$ is a permutation polynomial for every natural number $i \le k$, where $i$ is viewed
as an element of $F$.

The source considers only positive levels $k$; here every natural level is allowed, and
completeness to level $0$ says that $f$ itself is a permutation polynomial.

Formalized by `Polynomial.IsKComplete`, a definition declared in [MathlibExt/FieldTheory/Finite/PermutationPolynomial.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/FieldTheory/Finite/PermutationPolynomial.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html#is-kcomplete).

## Unfolded form of $k$-completeness

Let $F$ be a finite field, $f \in F[X]$ and $k$ a
natural number. Then $f$ is complete to level $k$ if and only if for every natural number
$i \le k$ the map $F \to F$, $x \mapsto (f + iX)(x)$, is bijective, where $i$ is viewed as an
element of $F$.

Formalized by `Polynomial.isKComplete_iff`, a theorem declared in [MathlibExt/FieldTheory/Finite/PermutationPolynomial.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/FieldTheory/Finite/PermutationPolynomial.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html#is-kcomplete-iff).

## Completeness at a lower level

Let $F$ be a finite field, $f \in F[X]$ and let $j \le k$
be natural numbers. If $f$ is complete to level $k$, then $f$ is complete to level $j$.

Formalized by `Polynomial.isKComplete_mono`, a theorem declared in [MathlibExt/FieldTheory/Finite/PermutationPolynomial.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/FieldTheory/Finite/PermutationPolynomial.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html#is-kcomplete-mono).

## Completeness at level zero

Let $F$ be a finite field and $f \in F[X]$. Then $f$ is
complete to level $0$ if and only if $f$ is a permutation polynomial.

Formalized by `Polynomial.isKComplete_zero`, a theorem declared in [MathlibExt/FieldTheory/Finite/PermutationPolynomial.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/FieldTheory/Finite/PermutationPolynomial.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html#is-kcomplete-zero).

## Completeness at the next level

Let $F$ be a finite field, $f \in F[X]$ and $k$ a natural
number. Then $f$ is complete to level $k + 1$ if and only if $f$ is complete to level $k$ and
$f + (k + 1)X$ is a permutation polynomial, where $k + 1$ is viewed as an element of $F$.

Formalized by `Polynomial.isKComplete_succ_iff`, a theorem declared in [MathlibExt/FieldTheory/Finite/PermutationPolynomial.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/FieldTheory/Finite/PermutationPolynomial.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html#is-kcomplete-succ-iff).

## A $k$-complete polynomial is a permutation polynomial

Let $F$ be a finite field,
$f \in F[X]$ and $k$ a natural number. If $f$ is complete to level $k$, then $f$ is a
permutation polynomial.

Formalized by `Polynomial.isKComplete_self`, a theorem declared in [MathlibExt/FieldTheory/Finite/PermutationPolynomial.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/FieldTheory/Finite/PermutationPolynomial.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html#is-kcomplete-self).

## Hermite–Dickson criterion

Let $\mathbb{F}_q$ be a finite field with $q$ elements and
characteristic $p$, and let $f \in \mathbb{F}_q[X]$. Then $f$ is a permutation polynomial of
$\mathbb{F}_q$, that is, $x \mapsto f(x)$ is a bijection of $\mathbb{F}_q$, if and only if $f$
has exactly one root in $\mathbb{F}_q$ and, for every integer $t$ with $1 \le t \le q - 2$ and
$p \nmid t$, the remainder of $f^t$ upon division by $X^q - X$ has degree at most $q - 2$.

## Sources

- Brian G. Kronenthal, "An Integer Sequence Motivated by Generalized Quadrangles", Journal of Integer Sequences 18 (2015), Article 15.7.8, https://cs.uwaterloo.ca/journals/JIS/VOL18/Kronenthal/kron3.tex, Hermite–Dickson statement at lines 120–126.

Formalized by `MathlibExt.FieldTheory.HermiteDickson.hermite_dickson_permutation_criterion`, a theorem declared in [MathlibExt/FieldTheory/HermiteDickson.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/FieldTheory/HermiteDickson.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html#hermite-dickson-permutation-criterion).

## Monomial permutation polynomials of a finite field

Let $K$ be a finite field with $q$
elements and let $d \ge 1$ be an integer. Then $X^d$ is a permutation polynomial of $K$ if and
only if $\gcd(d, q - 1) = 1$.

The hypothesis $d \ge 1$ is needed: for $d = 0$ and $q = 2$ the condition $\gcd(d, q - 1) = 1$
holds, but $X^0 = 1$ is constant.

## Sources

- Chandan Kumar Vishwakarma and Rajesh P. Singh, *A Congruence Identity on Ordered Partitions Using Permutation Polynomials*, INTEGERS 24 (2024), Article A12, Lemma 2.

Stated but not proved: `MetaMathlibExt.isPermutationPolynomial_X_pow_iff_coprime` is written with `theorem_wanted` in [WantedExt/Algebra/OrderedPartitionPermutationPolynomialsWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/OrderedPartitionPermutationPolynomialsWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html#is-permutation-polynomial-x-pow-iff-copr).

## Power-sum criterion for distinct elements of a finite field

Let $K$ be a finite field
with $q$ elements and let $a_1, \dots, a_q \in K$. Then $a_1, \dots, a_q$ are pairwise distinct
if and only if $\sum_{i=1}^{q} a_i^t = 0$ for every $t = 0, 1, \dots, q - 2$ and
$\sum_{i=1}^{q} a_i^{q-1} = -1$, where $0^0 = 1$.

## Sources

- Chandan Kumar Vishwakarma and Rajesh P. Singh, *A Congruence Identity on Ordered Partitions Using Permutation Polynomials*, INTEGERS 24 (2024), Article A12, Lemma 3.

Stated but not proved: `MetaMathlibExt.injective_iff_sum_pow_eq` is written with `theorem_wanted` in [WantedExt/Algebra/OrderedPartitionPermutationPolynomialsWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/OrderedPartitionPermutationPolynomialsWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html#injective-iff-sum-pow-eq).

## Alternating binomial sums of powers

Let $x, y, k \in \mathbb{C}$ and let $n, m$ be
positive integers. If $n = m$, then

$$\sum_{i=0}^{n} (-1)^i \binom{n}{i} (kx + iy)^m = (-1)^n y^n n!,$$

and if $m < n$, then $\sum_{i=0}^{n} (-1)^i \binom{n}{i} (kx + iy)^m = 0$.

## Sources

- Chandan Kumar Vishwakarma and Rajesh P. Singh, *A Congruence Identity on Ordered Partitions Using Permutation Polynomials*, INTEGERS 24 (2024), Article A12, Theorem 3.

Stated but not proved: `MetaMathlibExt.sum_neg_one_pow_choose_mul_pow` is written with `theorem_wanted` in [WantedExt/Algebra/OrderedPartitionPermutationPolynomialsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/OrderedPartitionPermutationPolynomialsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html#sum-neg-one-pow-choose-mul-pow).

## Shifted power-sum permutation polynomials of a prime field

Let $p$ be an odd prime and
let $k, t, a$ be positive integers with $\gcd(a + 1, p - 1) = 1$ and $k \equiv 1 \pmod{p(p-1)}$.
Suppose that $p - 1 \nmid t$ or $p^2 \mid k - 1$. Then the polynomial
$\sum_{n=1}^{k} n^t X^{n+a}$, with coefficients reduced modulo $p$, is a permutation polynomial
of $\mathbb{F}_p$.

## Sources

- Chandan Kumar Vishwakarma and Rajesh P. Singh, *A Congruence Identity on Ordered Partitions Using Permutation Polynomials*, INTEGERS 24 (2024), Article A12, Corollary 1.

Stated but not proved: `MetaMathlibExt.isPermutationPolynomial_sum_pow_mul_X_pow_add` is written with `theorem_wanted` in [WantedExt/Algebra/OrderedPartitionPermutationPolynomialsWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/OrderedPartitionPermutationPolynomialsWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html#is-permutation-polynomial-sum-pow-mul-x).

## Dilated power-sum permutation polynomials of a prime field

Let $p$ be an odd prime and
let $k, t, a$ be positive integers with $p \nmid a$, $\gcd(a, p - 1) = 1$ and
$k \equiv 1 \pmod{p(p-1)}$. Suppose that $p - 1 \nmid t$ or $p^2 \mid k - 1$. Then the
polynomial $\sum_{n=1}^{k} (an)^t X^{an}$, with coefficients reduced modulo $p$, is a
permutation polynomial of $\mathbb{F}_p$.

## Sources

- Chandan Kumar Vishwakarma and Rajesh P. Singh, *A Congruence Identity on Ordered Partitions Using Permutation Polynomials*, INTEGERS 24 (2024), Article A12, Corollary 3.

Stated but not proved: `MetaMathlibExt.isPermutationPolynomial_sum_mul_pow_mul_X_pow_mul` is written with `theorem_wanted` in [WantedExt/Algebra/OrderedPartitionPermutationPolynomialsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/OrderedPartitionPermutationPolynomialsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html#is-permutation-polynomial-sum-mul-pow-mu).

## Rational form of the power-weighted geometric sum

For positive integers $t$ and $k$,
the following identity holds in $\mathbb{Z}[X]$:

$$(1 - X)^{t+1} \sum_{n=1}^{k} n^t X^n =
\sum_{n=1}^{t} \Bigl(\sum_{i=0}^{n-1} (-1)^i \binom{t+1}{i} (n - i)^t\Bigr) X^n +
\sum_{m=1}^{t+1} \Bigl(\sum_{i=m}^{t+1} (-1)^i \binom{t+1}{i} (k + m - i)^t\Bigr) X^{k+m}.$$

Equivalently, for every $x \ne 1$ the value $h_t^k(x) = \sum_{n=1}^{k} n^t x^n$ is the
right-hand side at $x$ divided by $(1 - x)^{t+1}$, which is the form the source states.

## Sources

- Chandan Kumar Vishwakarma and Rajesh P. Singh, *A Congruence Identity on Ordered Partitions Using Permutation Polynomials*, INTEGERS 24 (2024), Article A12, Lemma 4.

Stated but not proved: `MetaMathlibExt.one_sub_X_pow_mul_sum_pow_mul_X_pow` is written with `theorem_wanted` in [WantedExt/Algebra/OrderedPartitionPermutationPolynomialsWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/OrderedPartitionPermutationPolynomialsWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html#one-sub-x-pow-mul-sum-pow-mul-x-pow).

## Vishwakarma–Singh congruence for ordered partitions

Let $p$ be an odd prime and let
$k, s, t$ be positive integers with $s \le p - 2$ and $k \equiv 1 \pmod{p(p-1)}$, such that
$p^2 \mid k - 1$ whenever $p - 1 \mid t$. Let $\mu = \lfloor ks/(p - 1) \rfloor$. Then

$$\sum_{j=1}^{\mu} \sum_{\omega} (\omega_1 \cdots \omega_s)^t \equiv 0 \pmod{p},$$

where for each $j$ the inner sum runs over all $s$-tuples $\omega = (\omega_1, \dots, \omega_s)$
with entries in $\{1, \dots, k\}$ and $\omega_1 + \cdots + \omega_s = j(p - 1)$.

The source states the hypothesis $s \not\equiv 0 \pmod{p}$ in place of $s \le p - 2$, the range
of Hermite's criterion used in its proof; with that hypothesis the claim fails, e.g. for $p = 3$,
$k = 1$, $s = 2$, $t = 1$ the sum is $1$.

## Sources

- Chandan Kumar Vishwakarma and Rajesh P. Singh, *A Congruence Identity on Ordered Partitions Using Permutation Polynomials*, INTEGERS 24 (2024), Article A12, Theorem 1.

Stated but not proved: `MetaMathlibExt.prime_dvd_sum_compositions_prod_pow` is written with `theorem_wanted` in [WantedExt/Algebra/OrderedPartitionPermutationPolynomialsWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/OrderedPartitionPermutationPolynomialsWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html#prime-dvd-sum-compositions-prod-pow).

## Vishwakarma–Singh congruence for ordered partitions, linear case

Let $p$ be an odd
prime and let $k, s$ be positive integers with $s \le p - 2$ and $k \equiv 1 \pmod{p(p-1)}$.
Let $\mu = \lfloor ks/(p - 1) \rfloor$. Then

$$\sum_{j=1}^{\mu} \sum_{\omega} \omega_1 \cdots \omega_s \equiv 0 \pmod{p},$$

where for each $j$ the inner sum runs over all $s$-tuples $\omega = (\omega_1, \dots, \omega_s)$
with entries in $\{1, \dots, k\}$ and $\omega_1 + \cdots + \omega_s = j(p - 1)$.

This is the case $t = 1$ of the source's Theorem 1. The source states the hypothesis
$s \not\equiv 0 \pmod{p}$ in place of $s \le p - 2$; with that hypothesis the claim fails, e.g.
for $p = 3$, $k = 7$, $s = 2$ the sum is $400 \equiv 1 \pmod{3}$.

## Sources

- Chandan Kumar Vishwakarma and Rajesh P. Singh, *A Congruence Identity on Ordered Partitions Using Permutation Polynomials*, INTEGERS 24 (2024), Article A12, Corollary 2.

Stated but not proved: `MetaMathlibExt.prime_dvd_sum_compositions_prod` is written with `theorem_wanted` in [WantedExt/Algebra/OrderedPartitionPermutationPolynomialsWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/OrderedPartitionPermutationPolynomialsWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html#prime-dvd-sum-compositions-prod).

## Vishwakarma–Singh congruence for ordered partitions into multiples

Let $p$ be an odd
prime and let $a, k, s, t$ be positive integers with $\gcd(a, p - 1) = 1$, $s \le p - 2$ and
$k \equiv 1 \pmod{p(p-1)}$, such that $p^2 \mid k - 1$ whenever $p - 1 \mid t$. Let
$\mu = \lfloor aks/(p - 1) \rfloor$. Then

$$\sum_{j=1}^{\mu} \sum_{\omega} (\omega_1 \cdots \omega_s)^t \equiv 0 \pmod{p},$$

where for each $j$ the inner sum runs over all $s$-tuples $\omega = (\omega_1, \dots, \omega_s)$
with entries in $\{an : 1 \le n \le k\}$ and $\omega_1 + \cdots + \omega_s = j(p - 1)$.

The source states this with two differences. It assumes $s \not\equiv 0 \pmod{p}$ in place of
$s \le p - 2$; with that hypothesis the claim fails, e.g. for $a = 1$, $p = 3$, $k = 7$, $s = 2$,
$t = 1$. It takes $\mu = \lfloor ks/(p - 1) \rfloor$; with that bound the claim fails for $a > 1$,
e.g. for $p = 5$, $a = 3$, $k = 21$, $s = t = 1$ the sum is $12$. The bound
$\lfloor aks/(p - 1) \rfloor$ covers every multiple of $p - 1$ up to $aks$, the degree of the
$s$-th power of $\sum_{n=1}^{k} (an)^t X^{an}$, to which the proof applies Hermite's criterion.

## Sources

- Chandan Kumar Vishwakarma and Rajesh P. Singh, *A Congruence Identity on Ordered Partitions Using Permutation Polynomials*, INTEGERS 24 (2024), Article A12, Corollary 4.

Stated but not proved: `MetaMathlibExt.prime_dvd_sum_compositions_mul_prod_pow` is written with `theorem_wanted` in [WantedExt/Algebra/OrderedPartitionPermutationPolynomialsWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/OrderedPartitionPermutationPolynomialsWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html#prime-dvd-sum-compositions-mul-prod-pow).

## Power sums over $\mathbb{Z}/p\mathbb{Z}$

Let $p$ be a prime and $t$ a positive
integer. Then $\sum_{a \in \mathbb{Z}/p\mathbb{Z}} a^t$ equals $-1$ if $p - 1$ divides $t$,
and $0$ otherwise.

## Sources

- Zhiguo Ding and Michael E. Zieve, "Permutation Polynomials of the Form `∑_{n=1}^k h(n) X^n`", Lemma 1.

Stated but not proved: `MathlibExt.Algebra.PermutationPolynomialsWanted.sum_zmod_pow_eq_ite` is written with `theorem_wanted` in [WantedExt/Algebra/PermutationPolynomialsWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PermutationPolynomialsWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html#sum-zmod-pow-eq-ite).

## Permutation polynomials $\sum_{n=1}^k n^t X^n$ over $\mathbb{F}_p$

Let $p$ be an
odd prime and let $k$ and $t$ be positive integers with $k \equiv 1 \pmod{p(p-1)}$.
Suppose that $k \equiv 1 \pmod{p^2}$ or that $p - 1$ does not divide $t$. Then the map
$c \mapsto \sum_{n=1}^{k} n^t c^n$ is a bijection from $\mathbb{Z}/p\mathbb{Z}$ to itself.

Ding and Zieve quote this result from an earlier paper.

## Sources

- Zhiguo Ding and Michael E. Zieve, "Permutation Polynomials of the Form `∑_{n=1}^k h(n) X^n`", Theorem 1.

Stated but not proved: `MathlibExt.Algebra.PermutationPolynomialsWanted.bijective_sum_pow_mul_pow_zmod` is written with `theorem_wanted` in [WantedExt/Algebra/PermutationPolynomialsWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PermutationPolynomialsWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html#bijective-sum-pow-mul-pow-zmod).

## When $\sum_{n=1}^k h(n) X^n$ induces the identity on $\mathbb{F}_q$

Let $p$ be a
prime, $\ell \ge 1$ and $q = p^\ell > 2$, and let $K$ be a finite field of characteristic
$p$ with $q$ elements. Let $k$ be a positive integer with $k \equiv 1 \pmod{p(q-1)}$ and
let $h \in K[X]$, with degree $d$ (taken to be $0$ when $h = 0$) and coefficient $h_i$ of
$X^i$. Then $\sum_{n=1}^{k} h(n)\,c^n = c$ for every $c \in K$ if and only if $h(1) = 1$
and either $k \equiv 1 \pmod{p^2}$ or $\sum_{j=1}^{\lfloor d/(p-1) \rfloor} h_{j(p-1)} = 0$.

## Sources

- Zhiguo Ding and Michael E. Zieve, "Permutation Polynomials of the Form `∑_{n=1}^k h(n) X^n`", Theorem 2.

Stated but not proved: `MathlibExt.Algebra.PermutationPolynomialsWanted.finiteField_sum_eval_mul_pow_eq_id_iff` is written with `theorem_wanted` in [WantedExt/Algebra/PermutationPolynomialsWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PermutationPolynomialsWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html#finite-field-sum-eval-mul-pow-eq-id-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Permutation polynomials](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/permutation-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/FieldTheory/finite-fields/permutation-polynomials)
