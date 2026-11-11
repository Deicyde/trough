---
declaration: section
origin: cited
lean: MetaMathlibExt.trinomialLaurent, MetaMathlibExt.linearLaurent, MetaMathlibExt.centralTrinomial, MetaMathlibExt.generalizedMotzkin, MetaMathlibExt.a005717, MetaMathlibExt.a005773, MetaMathlibExt.trinomialLaurent_one_one_powers, MetaMathlibExt.centralTrinomial_one_one_values
statement: formalized
---

# Generalized Motzkin numbers modulo primes

34 results, 9 proved and 25 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html).

## The symmetric trinomial Laurent polynomial

For integers $a$ and $b$, this is the Laurent
polynomial $a x^{-1} + b + a x$ with integer coefficients, used to define the generalized central
trinomial coefficients and the generalized Motzkin numbers.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Definitions.

Formalized by `MetaMathlibExt.trinomialLaurent`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#trinomial-laurent).

## Laurent polynomials of degree at most one

For integers $\alpha, \beta, \gamma$, this is the
Laurent polynomial $\alpha x^{-1} + \beta + \gamma x$ with integer coefficients.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Lemma 1. The degree-one hypotheses of Lemma 1 are imposed on the coefficients in the statements that use this polynomial.

Formalized by `MetaMathlibExt.linearLaurent`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#linear-laurent).

## Generalized central trinomial coefficients

For integers $a, b$ and a natural number $n$,
the generalized central trinomial coefficient $T_n^{(a/b)}$ is the constant term of the Laurent
polynomial $(a x^{-1} + b + a x)^n$.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Definitions.

Formalized by `MetaMathlibExt.centralTrinomial`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#central-trinomial).

## Generalized Motzkin numbers

For integers $a, b$ and a natural number $n$, the generalized
Motzkin number $M^{(a,b)}_n$ is the constant term of the Laurent polynomial
$(a x^{-1} + b + a x)^n (1 - x^2)$ with integer coefficients.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Definitions.

Formalized by `MetaMathlibExt.generalizedMotzkin`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#generalized-motzkin).

## OEIS A005717

For a natural number $n$, $a_n$ is the constant term of the Laurent
polynomial $x (x^{-1} + 1 + x)^n$ with integer coefficients.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Definitions.

Formalized by `MetaMathlibExt.a005717`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#a005717).

## OEIS A005773

For a natural number $n$, $a_n$ is the constant term of the Laurent
polynomial $(1 + x)(x^{-1} + 1 + x)^n$ with integer coefficients.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Definitions.

Formalized by `MetaMathlibExt.a005773`, a definition declared in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#a005773).

## The first five powers of $x^{-1} + 1 + x$

In the ring of Laurent polynomials over
$\mathbb{Z}$,
$(x^{-1} + 1 + x)^0 = 1$,
$(x^{-1} + 1 + x)^1 = x^{-1} + 1 + x$,
$(x^{-1} + 1 + x)^2 = x^{-2} + 2x^{-1} + 3 + 2x + x^2$,
$(x^{-1} + 1 + x)^3 = x^{-3} + 3x^{-2} + 6x^{-1} + 7 + 6x + 3x^2 + x^3$ and
$(x^{-1} + 1 + x)^4 = x^{-4} + 4x^{-3} + 10x^{-2} + 16x^{-1} + 19 + 16x + 10x^2 + 4x^3 + x^4$.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Definitions.

Formalized by `MetaMathlibExt.trinomialLaurent_one_one_powers`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#trinomial-laurent-one-one-powers).

## First five central trinomial coefficients

The central trinomial coefficients $T_n$, the
constant terms of $(x^{-1} + 1 + x)^n$, are $1, 1, 3, 7, 19$ for $n = 0, 1, 2, 3, 4$.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Definitions.

Formalized by `MetaMathlibExt.centralTrinomial_one_one_values`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#central-trinomial-one-one-values).

## First five generalized Motzkin numbers at $a = b = 1$

The generalized Motzkin numbers
$M_n$ for $a = b = 1$, the constant terms of $(x^{-1} + 1 + x)^n (1 - x^2)$, are $1, 1, 2, 4, 9$
for $n = 0, 1, 2, 3, 4$.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Definitions.

Formalized by `MetaMathlibExt.generalizedMotzkin_one_one_values`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#generalized-motzkin-one-one-values).

## Generalized Motzkin numbers from three central trinomial coefficients

For integers $a$, $b$
let $T_r$ and $M_r$ be the constant terms of $(a x^{-1} + b + a x)^r$ and of
$(a x^{-1} + b + a x)^r (1 - x^2)$, the generalized central trinomial coefficients and generalized
Motzkin numbers. Then for every natural number $n$,

$$
2a^2 M_n = (4a^2 - b^2) T_n + 2b T_{n+1} - T_{n+2}.
$$

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Proposition 1.

Stated but not proved: `MetaMathlibExt.generalizedMotzkin_centralTrinomial_relation` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#generalized-motzkin-central-trinomial-re).

## Recurrence for generalized central trinomial coefficients

Let $a, b$ be integers and let
$T_n$ be the constant term of $(a x^{-1} + b + a x)^n$. For every natural number $n$,

$$(n + 2) T_{n+2} = b (2n + 3) T_{n+1} - (b^2 - 4a^2)(n + 1) T_n.$$

This is the source's recurrence with its index shifted by two, so that every index is a natural
number.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Proposition 2.

Stated but not proved: `MetaMathlibExt.centralTrinomial_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#central-trinomial-recurrence).

## Three-term recurrence for generalized Motzkin numbers

For integers $a$, $b$ let $M_r$ be
the constant term of $(a x^{-1} + b + a x)^r (1 - x^2)$, the generalized Motzkin number. Then for
every natural number $n$,

$$
(n + 4) M_{n+2} = b (2n + 5) M_{n+1} - (b^2 - 4a^2)(n + 1) M_n.
$$

The source states the recurrence for $M_n$ with $n \ge 2$; it is written here at index $n + 2$.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Corollary 1.

Stated but not proved: `MetaMathlibExt.generalizedMotzkin_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#generalized-motzkin-recurrence).

## Mirror symmetry of central trinomial coefficients modulo a prime

Let $a, b$ be integers
and let $T_n$ be the constant term of $(a x^{-1} + b + a x)^n$. For every prime $p > 2$ and every
natural number $k \le (p - 1)/2$,

$$T_{p-1-k} \equiv (b^2 - 4a^2)^{(p-1)/2 - k} \, T_k \pmod p.$$

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Theorem 1.

Stated but not proved: `MetaMathlibExt.centralTrinomial_mod_prime_symmetry` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#central-trinomial-mod-prime-symmetry).

## Reflection symmetry of generalized Motzkin numbers modulo $p$

For integers $a$, $b$ let
$M_r$ be the constant term of $(a x^{-1} + b + a x)^r (1 - x^2)$, the generalized Motzkin number.
Let $p > 3$ be a prime and $k$ a natural number with $k \le (p - 3)/2$. Then

$$
M_{p-3-k} \equiv (b^2 - 4a^2)^{(p-3)/2 - k} \, M_k \pmod p.
$$

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Theorem 2.

Stated but not proved: `MetaMathlibExt.generalizedMotzkin_mod_prime_symmetry` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#generalized-motzkin-mod-prime-symmetry).

## Squared central trinomial coefficient at one less than a prime

Let $a, b$ be integers,
let $T_n$ be the constant term of $(a x^{-1} + b + a x)^n$, and let $p$ be a prime with
$b^2 - 4a^2 \not\equiv 0 \pmod p$. Then $T_{p-1}^2 \equiv 1 \pmod p$.

This is the source's Corollary 2 in an equivalent squared form, which avoids an inverse residue
modulo $p$.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Corollary 2.

Stated but not proved: `MetaMathlibExt.centralTrinomial_prime_minus_one_sq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#central-trinomial-prime-minus-one-sq).

## Primes dividing the Motzkin number $M_{p-2}$

A prime $p$ divides the Motzkin number
$M_{p-2} = M^{(1,1)}_{p-2}$ if and only if $p \equiv 1 \pmod 3$.

For $p = 2$ both sides are false, since $M_0 = 1$.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Proposition 3.

Stated but not proved: `MetaMathlibExt.prime_dvd_motzkin_prime_minus_two_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#prime-dvd-motzkin-prime-minus-two-iff).

## Lucas property for constant terms of powers of linear Laurent polynomials

Let $p$ be a
prime, let $\alpha$, $\beta$, $\gamma$, $a$, $b$ be integers, and let $n$ be a natural number whose
base-$p$ digits are $d_0, \dots, d_s$ (there are none when $n = 0$, and both products below are
then $1$). Write $\operatorname{ct}(F)$ for the constant term of a Laurent polynomial $F$ and put
$P = \alpha x^{-1} + \beta + \gamma x$. Then

$$
\operatorname{ct}(P^n) \equiv \prod_{i=0}^{s} \operatorname{ct}(P^{d_i}) \pmod p,
$$

and the generalized central trinomial coefficients $T_r = \operatorname{ct}((a x^{-1} + b + a x)^r)$
satisfy $T_n \equiv \prod_{i=0}^{s} T_{d_i} \pmod p$.

The source assumes that $P$ has degree one; here $\alpha$ and $\gamma$ are arbitrary, which
includes that case.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Proposition 4.

Stated but not proved: `MetaMathlibExt.constantTerm_linearLaurent_pow_digits` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#constant-term-linear-laurent-pow-digits).

## Digit decomposition of shifted sums of constant terms modulo a prime

Let $\alpha, \beta,
\gamma$ be integers with $\alpha \ne 0$ or $\gamma \ne 0$, let $a_r$ be the constant term of
$(\alpha x^{-1} + \beta + \gamma x)^r$, let $p$ be a prime, let $h < p$ be a natural number, let
$c_0, c_1, \ldots$ be integers, and let $b_r = \sum_{i=0}^{h} c_i a_{r+i}$. Let $q, k$ be natural
numbers, let $m, n_0 < p$ be natural numbers with $m \ne p - 1$, put
$n = ((qp + m) p^k + p^k - 1) p + n_0$ (in base $p$: the digits of $q$, then $m$, then $k$ digits
$p - 1$, then $n_0$), and let $C = \min(h, p - n_0 - 1)$. Then

$$b_n \equiv a_q \Big( a_m a_{p-1}^k \sum_{i=0}^{C} c_i a_{n_0+i} +
a_{m+1} \sum_{i=p-n_0}^{h} c_i a_{i-(p-n_0)} \Big) \pmod p,$$

where the last sum is empty when $h < p - n_0$.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Lemma 1.

Stated but not proved: `MetaMathlibExt.constantTermLinearCombination_digit_decomposition` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#constant-term-linear-combination-digit-d).

## Digit formula for shifted sums of constant terms, small last digit

Let $\alpha$, $\beta$,
$\gamma$ be integers with $\alpha \ne 0$ or $\gamma \ne 0$, and let $a_r$ be the constant term of
$(\alpha x^{-1} + \beta + \gamma x)^r$. Let $c_0, c_1, c_2, \dots$ be integers, let $h$ be a natural
number, and put $b_r = \sum_{i=0}^{h} c_i a_{r+i}$. Let $p$ be a prime with $h < p$, and let $q$,
$m$, $k$, $n_0$ be natural numbers with $m < p$, $m \ne p - 1$, $n_0 < p$ and $n_0 < p - h$. If
$n = ((qp + m)p^k + p^k - 1)p + n_0$, that is, $n$ is obtained from $q$ by appending the base-$p$
digits $m$, then $k$ digits $p - 1$, then $n_0$, then

$$
b_n \equiv a_q \, a_m \, a_{p-1}^k \sum_{i=0}^{h} c_i a_{n_0+i} \pmod p
\quad \text{and} \quad
b_n \equiv a_{(n - n_0)/p} \, b_{n_0} \pmod p.
$$

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Lemma 1.

Stated but not proved: `MetaMathlibExt.constantTermLinearCombination_small_last_digit` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#constant-term-linear-combination-small-l).

## Density one for zeros of shifted combinations of central trinomial coefficients

Let
$\alpha$ and $\beta$ be integers with $\alpha \neq 0$, and write $a_r$ for the generalized central
trinomial coefficient with parameters $\alpha, \beta$, the constant term of
$(\alpha x^{-1} + \beta + \alpha x)^r$. Let $p$ be a prime, let $h < p$ be a natural number, let
$(c_i)_{i \ge 0}$ be a sequence of integers, and set $b_r = \sum_{i=0}^{h} c_i a_{r+i}$ for
$r \in \mathbb{N}$. If $a_r \equiv 0 \pmod p$ for some $r \in \mathbb{N}$, then the set of
$r \in \mathbb{N}$ with $b_r \equiv 0 \pmod p$ has natural density $1$.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Lemma 2.

Stated but not proved: `MetaMathlibExt.symmetricConstantTerm_zero_density_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#symmetric-constant-term-zero-density-one).

## Zero density of shifted combinations of central trinomial coefficients

Let $\alpha$ and
$\beta$ be integers with $\alpha \neq 0$, and write $a_r$ for the generalized central trinomial
coefficient with parameters $\alpha, \beta$, the constant term of
$(\alpha x^{-1} + \beta + \alpha x)^r$. Let $p$ be a prime, let $h < p$ be a natural number, let
$(c_i)_{i \ge 0}$ be a sequence of integers, and set $b_r = \sum_{i=0}^{h} c_i a_{r+i}$ for
$r \in \mathbb{N}$. Suppose that $a_r \not\equiv 0 \pmod p$ for every $r \in \mathbb{N}$. For
$p - h \le r \le p - 1$ put $C_r = \min(h, p - r - 1)$, $S_r = \sum_{i=0}^{C_r} c_i a_{r+i}$ and
$S'_r = \sum_{i=C_r+1}^{h} c_i a_{i-(p-r)}$. Let $N_0$ be the number of $r$ with $0 \le r < p - h$
and $b_r \equiv 0 \pmod p$, let $N_1$ be the number of pairs $(r, m)$ with $p - h \le r \le p - 1$
and $0 \le m \le p - 2$ such that $a_m S_r \equiv -a_{m+1} S'_r \pmod p$, and let $N_2$ be the
number of pairs $(r, m)$ in that range such that $a_m S_r \equiv -a_{p-1} a_{m+1} S'_r \pmod p$.
Then the set of $r \in \mathbb{N}$ with $b_r \equiv 0 \pmod p$ has natural density

$$\frac{N_0}{p} + \frac{N_1}{(p-1)(p+1)} + \frac{N_2}{(p-1)p(p+1)}.$$

No assumption $p > 2$ is made.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Lemma 2.

Stated but not proved: `MetaMathlibExt.symmetricConstantTerm_zero_density_formula` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#symmetric-constant-term-zero-density-for).

## Generalized Motzkin numbers modulo $p$ with last digit below $p - 2$

For integers $a$, $b$
let $T_r$ and $M_r$ be the constant terms of $(a x^{-1} + b + a x)^r$ and of
$(a x^{-1} + b + a x)^r (1 - x^2)$, the generalized central trinomial coefficients and generalized
Motzkin numbers. Let $p > 2$ be a prime with $b^2 - 4a^2 \not\equiv 0 \pmod p$, and let
$q$, $n_0$ be natural numbers with $n_0 < p - 2$. If $n = qp + n_0$, then

$$
2a^2 M_n \equiv 2a^2 \, T_q \, M_{n_0} \pmod p.
$$

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Proposition 5(i).

Stated but not proved: `MetaMathlibExt.generalizedMotzkin_digit_below_prime_minus_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#generalized-motzkin-digit-below-prime-mi).

## Generalized Motzkin numbers modulo $p$ with last digit $p - 2$

For integers $a$, $b$ let
$T_r$ and $M_r$ be the constant terms of $(a x^{-1} + b + a x)^r$ and of
$(a x^{-1} + b + a x)^r (1 - x^2)$, the generalized central trinomial coefficients and generalized
Motzkin numbers. Let $p > 2$ be a prime with $b^2 - 4a^2 \not\equiv 0 \pmod p$, and let
$q$, $m$, $k$ be natural numbers with $m < p - 1$. If $n = ((qp + m)p^k + p^k - 1)p + p - 2$, that
is, $n$ is obtained from $q$ by appending the base-$p$ digits $m$, then $k$ digits $p - 1$, then
$p - 2$, then

$$
2a^2 M_n \equiv T_q \left( b \, T_m \, T_{p-1}^{k+1} - T_{m+1} \right) \pmod p.
$$

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Proposition 5(ii).

Stated but not proved: `MetaMathlibExt.generalizedMotzkin_digit_prime_minus_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#generalized-motzkin-digit-prime-minus-tw).

## Generalized Motzkin numbers modulo $p$ with last digit $p - 1$

For integers $a$, $b$ let
$T_r$ and $M_r$ be the constant terms of $(a x^{-1} + b + a x)^r$ and of
$(a x^{-1} + b + a x)^r (1 - x^2)$, the generalized central trinomial coefficients and generalized
Motzkin numbers. Let $p > 2$ be a prime with $D = b^2 - 4a^2 \not\equiv 0 \pmod p$, let
$q$, $m$, $k$ be natural numbers with $m < p - 1$, and put $\ell = p - 2 - m$. If
$n = ((qp + m)p^k + p^k - 1)p + p - 1$, that is, $n$ is obtained from $q$ by appending the base-$p$
digits $m$, then $k + 1$ digits $p - 1$, then

$$
D^{(p-1)/2} \cdot 2a^2 M_n \equiv
D^{m+1} \, T_q \left( b \, T_\ell - T_{p-1}^{k+1} \, T_{\ell+1} \right) \pmod p.
$$

The source states this congruence with a power of the unit $D$ whose exponent may be negative;
here it is multiplied out so that every exponent is nonnegative.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Proposition 5(iii).

Stated but not proved: `MetaMathlibExt.generalizedMotzkin_digit_prime_minus_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#generalized-motzkin-digit-prime-minus-on).

## Zeros of generalized Motzkin numbers with a small last digit

Let $a, b$ be integers and
let $p > 2$ be a prime with $b^2 - 4a^2 \not\equiv 0 \pmod p$, and suppose that the generalized
central trinomial coefficients satisfy $T^{(a,b)}_r \not\equiv 0 \pmod p$ for every $r < p$. Let
$q, n_0$ be natural numbers with $n_0 < p - 2$ and let $n = qp + n_0$. Then $p$ divides the
generalized Motzkin number $M^{(a,b)}_n$ if and only if $p$ divides $M^{(a,b)}_{n_0}$.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Corollary 3.

Stated but not proved: `MetaMathlibExt.generalizedMotzkin_zero_digit_below_prime_minus_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#generalized-motzkin-zero-digit-below-pri).

## Zeros of generalized Motzkin numbers with last digit $p - 2$

Let $a, b$ be integers and
let $p > 2$ be a prime with $a \not\equiv 0 \pmod p$ and $b^2 - 4a^2 \not\equiv 0 \pmod p$. Write
$T_r = T^{(a,b)}_r$ for the generalized central trinomial coefficients and suppose that
$T_r \not\equiv 0 \pmod p$ for every $r < p$. Let $q, m, k$ be natural numbers with $m < p - 1$
and let

$$n = \bigl((qp + m)p^k + p^k - 1\bigr)p + p - 2.$$

Then $p$ divides the generalized Motzkin number $M^{(a,b)}_n$ if and only if
$b T_m \equiv T_{p-1}^{k+1} T_{m+1} \pmod p$.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Corollary 3. The hypothesis $a \not\equiv 0 \pmod p$ is implicit in the paper, which cancels $2a^2$.

Stated but not proved: `MetaMathlibExt.generalizedMotzkin_zero_digit_prime_minus_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#generalized-motzkin-zero-digit-prime-min).

## Zeros of generalized Motzkin numbers with last digit $p - 1$

Let $a, b$ be integers and
let $p > 2$ be a prime with $a \not\equiv 0 \pmod p$ and $b^2 - 4a^2 \not\equiv 0 \pmod p$. Write
$T_r = T^{(a,b)}_r$ for the generalized central trinomial coefficients and suppose that
$T_r \not\equiv 0 \pmod p$ for every $r < p$. Let $q, m, k$ be natural numbers with $m < p - 1$,
let

$$n = \bigl((qp + m)p^k + p^k - 1\bigr)p + p - 1,$$

and let $\ell = p - 2 - m$. Then $p$ divides the generalized Motzkin number $M^{(a,b)}_n$ if and
only if $b T_\ell \equiv T_{p-1}^{k+1} T_{\ell+1} \pmod p$.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Corollary 3. The hypothesis $a \not\equiv 0 \pmod p$ is implicit in the paper, which cancels $2a^2$.

Stated but not proved: `MetaMathlibExt.generalizedMotzkin_zero_digit_prime_minus_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#generalized-motzkin-zero-digit-prime-min-2).

## Generalized Motzkin numbers vanish modulo a prime with density one

Let $a, b$ be integers
and let $p$ be a prime. If $p$ divides the generalized central trinomial coefficient
$T^{(a,b)}_r$ for some $r < p$, then the set of $n \in \mathbb{N}$ such that $p$ divides the
generalized Motzkin number $M^{(a,b)}_n$ has natural density $1$.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Theorem 3.

Stated but not proved: `MetaMathlibExt.generalizedMotzkin_zero_density_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#generalized-motzkin-zero-density-one).

## Zero density formula for generalized Motzkin numbers modulo a prime

Let $a, b$ be
integers and let $p > 2$ be a prime with $a \not\equiv 0 \pmod p$. Write $T_r = T^{(a,b)}_r$ for
the generalized central trinomial coefficients and $M_n = M^{(a,b)}_n$ for the generalized Motzkin
numbers, and suppose that $T_r \not\equiv 0 \pmod p$ for every $r < p$. Let $A$ be the number of
$r < p - 2$ with $M_r \equiv 0 \pmod p$, let $B$ be the number of $m < p - 1$ with
$b T_m \equiv T_{p-1} T_{m+1} \pmod p$, and let $C$ be the number of $m < p - 1$ with
$b T_m \equiv T_{m+1} \pmod p$. Then the set of $n \in \mathbb{N}$ with $M_n \equiv 0 \pmod p$ has
natural density

$$D_0 = \frac{A}{p} + \frac{2B}{(p-1)(p+1)} + \frac{2C}{(p-1)p(p+1)}.$$

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Theorem 3. The hypothesis $a \not\equiv 0 \pmod p$ is implicit in the paper, which cancels $2a^2$.

Stated but not proved: `MetaMathlibExt.generalizedMotzkin_zero_density_formula` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 412](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L412). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#generalized-motzkin-zero-density-formula).

## Density of each nonzero residue among generalized Motzkin numbers modulo $p$

For integers
$a$, $b$ let $T_r$ and $M_r$ be the constant terms of $(a x^{-1} + b + a x)^r$ and of
$(a x^{-1} + b + a x)^r (1 - x^2)$, the generalized central trinomial coefficients and generalized
Motzkin numbers. Let $p > 2$ be a prime with $a \not\equiv 0 \pmod p$ such that
$T_r \not\equiv 0 \pmod p$ for every $r < p$, and suppose that the residues of $T_0, \dots, T_{p-1}$
generate the unit group $(\mathbb{Z}/p\mathbb{Z})^\times$. Put

$$
D_0 = \frac{N_1}{p} + \frac{2 N_2}{(p - 1)(p + 1)} + \frac{2 N_3}{(p - 1) p (p + 1)},
$$

where $N_1$ is the number of $r < p - 2$ with $M_r \equiv 0 \pmod p$, $N_2$ is the number of
$m < p - 1$ with $b T_m \equiv T_{p-1} T_{m+1} \pmod p$, and $N_3$ is the number of $m < p - 1$
with $b T_m \equiv T_{m+1} \pmod p$. Then for every nonzero residue $z$ modulo $p$, the set of
natural numbers $n$ with $M_n \equiv z \pmod p$ has natural density $(1 - D_0)/(p - 1)$.

The hypothesis $a \not\equiv 0 \pmod p$ is implicit in the source, which cancels $2a^2$.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Theorem 3.

Stated but not proved: `MetaMathlibExt.generalizedMotzkin_nonzero_density` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#generalized-motzkin-nonzero-density).

## Zero density of Motzkin numbers modulo a prime

Let $p$ be a prime, and write
$M_n = M^{(1,1)}_n$ for the Motzkin numbers and $T_r = T^{(1,1)}_r$ for the central trinomial
coefficients. If $T_r \equiv 0 \pmod p$ for some $r < p$, then the set of $n \in \mathbb{N}$ with
$M_n \equiv 0 \pmod p$ has natural density $1$. If instead $T_r \not\equiv 0 \pmod p$ for every
$r < p$ and $p > 2$, let $A$ be the number of $r < p - 2$ with $M_r \equiv 0 \pmod p$, let $B$ be
the number of $m < p - 1$ with $T_m \equiv T_{p-1} T_{m+1} \pmod p$, and let $C$ be the number of
$m < p - 1$ with $T_m \equiv T_{m+1} \pmod p$; then this set has natural density

$$D_0 = \frac{A}{p} + \frac{2B}{(p-1)(p+1)} + \frac{2C}{(p-1)p(p+1)},$$

and $D_0 \ge \frac{2}{p(p-1)}$.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Corollary 4. The paper's conjecture-conditional middle clause is omitted.

Stated but not proved: `MetaMathlibExt.motzkin_zero_density` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 466](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L466). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#motzkin-zero-density).

## Zero density of A005717 modulo a prime

Let $p$ be a prime, let $T_m$ be the central
trinomial coefficient, the constant term of $(x^{-1} + 1 + x)^m$, and let $a_n$ be the constant
term of $x (x^{-1} + 1 + x)^n$ (OEIS A005717). If $T_r \equiv 0 \pmod p$ for some $r < p$, then
the set of $n \in \mathbb{N}$ with $a_n \equiv 0 \pmod p$ has natural density $1$. If instead
$T_r \not\equiv 0 \pmod p$ for every $r < p$ and $p > 2$, let $N_1$ be the number of $m < p - 1$
with $T_m \equiv T_{p-1} T_{m+1} \pmod p$ and let $N_2$ be the number of $m < p - 1$ with
$T_m \equiv T_{m+1} \pmod p$. Then that set has natural density
$D_0 = (N_1 + p N_2) / ((p - 1)(p + 1))$, and $D_0 \ge 1/(p - 1)$.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Proposition 6.

Stated but not proved: `MetaMathlibExt.a005717_zero_density` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 491](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L491). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#a005717-zero-density).

## Zero density of Riordan numbers modulo a prime

Let $p$ be a prime, and write $r_n$ for the
Riordan numbers and $T_m = T^{(1,1)}_m$ for the central trinomial coefficients. If
$T_m \equiv 0 \pmod p$ for some $m < p$, then the set of $n \in \mathbb{N}$ with
$r_n \equiv 0 \pmod p$ has natural density $1$. If instead $T_m \not\equiv 0 \pmod p$ for every
$m < p$ and $p > 2$, let $B$ be the number of $m < p - 1$ with
$3 T_m \equiv T_{p-1} T_{m+1} \pmod p$ and let $C$ be the number of $m < p - 1$ with
$3 T_m \equiv T_{m+1} \pmod p$; then this set has natural density

$$D_0 = \frac{B + pC}{(p-1)(p+1)},$$

and $D_0 \ge \frac{1}{p-1}$.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Proposition 7.

Stated but not proved: `MetaMathlibExt.riordan_zero_density` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 512](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L512). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#riordan-zero-density).

## Zero density of A005773 modulo a prime

Let $p$ be a prime, let $T_m$ be the central
trinomial coefficient, the constant term of $(x^{-1} + 1 + x)^m$, and let $a_n$ be the constant
term of $(1 + x)(x^{-1} + 1 + x)^n$ (OEIS A005773). If $T_r \equiv 0 \pmod p$ for some $r < p$,
then the set of $n \in \mathbb{N}$ with $a_n \equiv 0 \pmod p$ has natural density $1$. If
instead $T_r \not\equiv 0 \pmod p$ for every $r < p$ and $p > 2$, let $N_1$ be the number of
$m < p - 1$ with $T_m \equiv -T_{p-1} T_{m+1} \pmod p$ and let $N_2$ be the number of
$m < p - 1$ with $T_m \equiv -T_{m+1} \pmod p$. Then that set has natural density
$D_0 = (N_1 + p N_2) / ((p - 1)(p + 1))$, and $D_0 \ge 1/(p - 1)$.

## Sources

- Nadav Kohen, *Density and Symmetry in the Generalized Motzkin Numbers Modulo p*, INTEGERS 26 (2026), Article A22, Proposition 8.

Stated but not proved: `MetaMathlibExt.a005773_zero_density` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean, line 533](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/GeneralizedMotzkinModPWanted.lean#L533). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html#a005773-zero-density).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized Motzkin numbers modulo primes](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/generalized-motzkin-numbers-modulo-primes)
