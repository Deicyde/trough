---
declaration: section
origin: cited
lean: Int.wilsonQuotient, Int.mul_wilsonQuotient, Int.factorial_eq_mul_wilsonQuotient_sub_one, MathlibExt.NumberTheory.WilsonFaulhaberWanted.wilson_mod_prime_sq, MathlibExt.NumberTheory.WilsonQuotientsWanted.wilsonQuotientM, MathlibExt.NumberTheory.WilsonQuotientsWanted.wilsonQuotientMPlus, MathlibExt.NumberTheory.WilsonQuotientsWanted.wilsonQuotientZ, MathlibExt.NumberTheory.WilsonQuotientsWanted.wilsonQuotientZPlus
statement: formalized
---

# Wilson quotients

15 results, 7 proved and 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wilson-quotients/index.html).

## Wilson quotient

For a natural number $p$, the Wilson quotient is the integer
$W(p) = \lfloor ((p-1)! + 1) / p \rfloor$ for $p \ge 1$, and $W(0) = 0$.

For a prime $p$, Wilson's theorem $p \mid (p-1)! + 1$ makes the division exact. The definition is
total on $\mathbb{N}$; the source defines $W_p$ only for odd primes $p$.

## Sources

- Y. Matsuno, *A resolution of Kellner's conjectures on Wilson quotients*, arXiv:2607.10106v1, lines 44–51.

Formalized by `Int.wilsonQuotient`, a definition declared in [MathlibExt/NumberTheory/WilsonQuotient.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/WilsonQuotient.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wilson-quotients/index.html#wilson-quotient).

## Exactness of the Wilson quotient

For every prime $p$, the Wilson quotient $W(p)$ of $p$
satisfies $p \, W(p) = (p-1)! + 1$ in $\mathbb{Z}$.

By Wilson's theorem $p$ divides $(p-1)! + 1$, so the division defining $W(p)$ is exact.

## Sources

- M. Avitabile and S. Mattarei, arXiv:2308.16034, `AH.tex` lines 315–321, which uses $(p-1)! = -1 + p \, w_p$, where $w_p$ is the Wilson quotient.

Formalized by `Int.mul_wilsonQuotient`, a theorem declared in [MathlibExt/NumberTheory/WilsonQuotient.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/WilsonQuotient.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wilson-quotients/index.html#mul-wilson-quotient).

## Factorial form of the Wilson quotient identity

For every prime $p$, the Wilson
quotient $W(p)$ of $p$ satisfies $(p-1)! = p \, W(p) - 1$ in $\mathbb{Z}$.

## Sources

- M. Avitabile and S. Mattarei, arXiv:2308.16034, `AH.tex` lines 315–321, display $(p-1)! = -1 + p \, w_p$, where $w_p$ is the Wilson quotient.

Formalized by `Int.factorial_eq_mul_wilsonQuotient_sub_one`, a theorem declared in [MathlibExt/NumberTheory/WilsonQuotient.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/WilsonQuotient.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wilson-quotients/index.html#factorial-eq-mul-wilson-quotient-sub-one).

## Wilson's theorem modulo $p^2$

Let $p$ be an odd prime and, for $1 \le k \le p - 1$, let
$q_p(k)$ be the Fermat quotient of $k$, the integer with $k^{p-1} = 1 + p\, q_p(k)$. Then

$$
(p - 1)! \equiv -1 + p \sum_{k=1}^{p-1} q_p(k) \pmod{p^2}.
$$

## Sources

- Claire Levaillant, "Wilson's Theorem Modulo `p^2` Derived from Faulhaber Polynomials", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.WilsonFaulhaberWanted.wilson_mod_prime_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/WilsonFaulhaberWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/WilsonFaulhaberWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wilson-quotients/index.html#wilson-mod-prime-sq).

## Morozov's Wilson quotients

For natural numbers $k$ and $n$, $M_k(n)$ is the rational
number

$$M_k(n) = \frac{1 + (-1)^k \, k! \, (n - k - 1)!}{n},$$

where $n - k - 1$ is truncated subtraction of natural numbers and division by $0$ gives $0$.

Formalized by `MathlibExt.NumberTheory.WilsonQuotientsWanted.wilsonQuotientM`, a definition declared in [WantedExt/NumberTheory/WilsonQuotientsWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/WilsonQuotientsWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wilson-quotients/index.html#wilson-quotient-m).

## Morozov's sign-adjusted Wilson quotients

For natural numbers $k$ and $n$, $M_k^+(n)$ is
the rational number

$$M_k^+(n) = \frac{(-1)^k + k! \, (n - k - 1)!}{n},$$

where $n - k - 1$ is truncated subtraction of natural numbers and division by $0$ gives $0$.

Formalized by `MathlibExt.NumberTheory.WilsonQuotientsWanted.wilsonQuotientMPlus`, a definition declared in [WantedExt/NumberTheory/WilsonQuotientsWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/WilsonQuotientsWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wilson-quotients/index.html#wilson-quotient-mplus).

## Morozov's Wilson quotient sum

For a natural number $n$, $Z(n)$ is the rational number
$Z(n) = \sum_{k=0}^{n-1} M_k(n)$, where $M_k(n)$ are Morozov's Wilson quotients.

Formalized by `MathlibExt.NumberTheory.WilsonQuotientsWanted.wilsonQuotientZ`, a definition declared in [WantedExt/NumberTheory/WilsonQuotientsWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/WilsonQuotientsWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wilson-quotients/index.html#wilson-quotient-z).

## Morozov's sign-adjusted Wilson quotient sum

For a natural number $n$, $Z^+(n)$ is the
rational number $\sum_{k=0}^{n-1} M_k^+(n)$, where $M_k^+(n) = ((-1)^k + k!\,(n-k-1)!)/n$ is
Morozov's sign-adjusted quotient.

Formalized by `MathlibExt.NumberTheory.WilsonQuotientsWanted.wilsonQuotientZPlus`, a definition declared in [WantedExt/NumberTheory/WilsonQuotientsWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/WilsonQuotientsWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wilson-quotients/index.html#wilson-quotient-zplus).

## A generalized Wilson criterion for primality

Let $n \ge 1$ and $k < n$ be natural
numbers. Then $(-1)^k \, k! \, (n - k - 1)! \equiv -1 \pmod{n}$ if and only if $n = 1$ or $n$
is prime.

## Sources

- Ivan V. Morozov, "On Quotients of a More General Theorem of Wilson", Corollary 1.

Stated but not proved: `MathlibExt.NumberTheory.WilsonQuotientsWanted.neg_one_pow_mul_factorial_mul_factorial_modEq_neg_one_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/WilsonQuotientsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/WilsonQuotientsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wilson-quotients/index.html#neg-one-pow-mul-factorial-mul-factorial).

## The Wilson quotient sum is an integer

For every natural number $n \ge 1$, Morozov's
Wilson quotient sum $Z(n)$ is an integer.

## Sources

- Ivan V. Morozov, "On Quotients of a More General Theorem of Wilson", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.WilsonQuotientsWanted.exists_int_eq_wilsonQuotientZ` is written with `theorem_wanted` in [WantedExt/NumberTheory/WilsonQuotientsWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/WilsonQuotientsWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wilson-quotients/index.html#exists-int-eq-wilson-quotient-z).

## When the sign-adjusted Wilson quotient sum is a natural number

For every natural number
$n \ge 1$, Morozov's sign-adjusted Wilson quotient sum $Z^+(n)$ is a natural number if and only
if $n$ is even, $n = 1$, or $n$ is prime.

## Sources

- Ivan V. Morozov, "On Quotients of a More General Theorem of Wilson", Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.WilsonQuotientsWanted.exists_nat_eq_wilsonQuotientZPlus_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/WilsonQuotientsWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/WilsonQuotientsWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wilson-quotients/index.html#exists-nat-eq-wilson-quotient-zplus-iff).

## The Wilson quotient sum Z(n) modulo n

Let $n \ge 1$ be a natural number. Morozov's
Wilson quotient sum $Z(n)$ is an integer; moreover $Z(n) \equiv 1 \pmod{n}$ if $n$ is neither
$1$ nor prime, and $Z(n) \equiv -1 \pmod{n}$ if $n = 1$ or $n$ is prime.

## Sources

- Ivan V. Morozov, "On Quotients of a More General Theorem of Wilson", Theorem 3.

Stated but not proved: `MathlibExt.NumberTheory.WilsonQuotientsWanted.exists_int_eq_wilsonQuotientZ_and_modEq` is written with `theorem_wanted` in [WantedExt/NumberTheory/WilsonQuotientsWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/WilsonQuotientsWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wilson-quotients/index.html#exists-int-eq-wilson-quotient-z-and-mod).

## A primality criterion from the Wilson quotient sum Z(2n − 1)

For every natural number
$n \ge 1$, Morozov's Wilson quotient sum $Z(2n - 1)$ is an integer, and it is divisible by $n$
if and only if $n = 1$ or $n$ is prime.

## Sources

- Ivan V. Morozov, "On Quotients of a More General Theorem of Wilson", Theorem 4.

Stated but not proved: `MathlibExt.NumberTheory.WilsonQuotientsWanted.exists_int_eq_wilsonQuotientZ_two_mul_sub_one_modEq_zero_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/WilsonQuotientsWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/WilsonQuotientsWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wilson-quotients/index.html#exists-int-eq-wilson-quotient-z-two-mul).

## The sign-adjusted Wilson quotient sum Z⁺(2n) modulo 2n

Let $n \ge 1$ be a natural
number. Morozov's sign-adjusted Wilson quotient sum $Z^+(2n)$ is an integer; it satisfies
$Z^+(2n) \equiv 0 \pmod{2n}$ if $n = 2$ or $n$ is neither $1$ nor prime, and
$Z^+(2n) \equiv n + 1 \pmod{2n}$ if $n$ is an odd prime.

## Sources

- Ivan V. Morozov, "On Quotients of a More General Theorem of Wilson", Theorem 5, equations (8) and (9).

Stated but not proved: `MathlibExt.NumberTheory.WilsonQuotientsWanted.exists_int_eq_wilsonQuotientZPlus_two_mul_and_modEq` is written with `theorem_wanted` in [WantedExt/NumberTheory/WilsonQuotientsWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/WilsonQuotientsWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wilson-quotients/index.html#exists-int-eq-wilson-quotient-zplus-two).

## A Bernoulli–harmonic congruence for the sign-adjusted Wilson quotient sum

Let $p$ be an
odd prime, let $B_m$ denote the Bernoulli numbers, and let $H_k = \sum_{j=1}^{k} 1/j$ denote the
harmonic numbers, with $H_0 = 0$. Then $p$ divides the numerator, in lowest terms, of the
rational number

$$Z^+(p) - \Bigl(B_{2(p-1)} - B_{p-1} - \sum_{k=0}^{p-1} (-1)^k H_k\Bigr),$$

where $Z^+(p)$ is Morozov's sign-adjusted Wilson quotient sum.

This is the congruence obtained by summing the paper's Equation (7). The printed simplification
of the alternating harmonic sum to $H_{p-1}/2$ is false already at $p = 3$.

## Sources

- Ivan V. Morozov, "On Quotients of a More General Theorem of Wilson", Theorem 6 and Equation (7).

Stated but not proved: `MathlibExt.NumberTheory.WilsonQuotientsWanted.prime_dvd_num_wilsonQuotientZPlus_sub_bernoulli_alternating` is written with `theorem_wanted` in [WantedExt/NumberTheory/WilsonQuotientsWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/WilsonQuotientsWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wilson-quotients/index.html#prime-dvd-num-wilson-quotient-zplus-sub).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Wilson quotients](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wilson-quotients/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wilson-quotients)
