---
article_id: af_f3e1b61e5577621a224cb0bc
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: lucas_lehmer_sufficiency
mathlib_file: Mathlib/NumberTheory/LucasLehmer.lean
---

# Lucas-Lehmer primality test

The **Lucas-Lehmer primality test** decides whether a Mersenne number $2^p - 1$
is [prime](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md) by iterating the map $x \mapsto x^2 - 2$ modulo that number.
It needs only $p - 2$ squarings of numbers smaller than $2^p - 1$, far fewer
operations than trial division, so that primality is far cheaper to decide for
Mersenne numbers than for general numbers of the same size. Mersenne primes
are also of independent interest: by the [perfect number theorem](../../../hundred-theorems/part-03/the-perfect-number-theorem.md)
they correspond to the even perfect numbers.

## Statement

For a natural number $p$, the [Mersenne number](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LucasLehmer.html#mersenne) is
$M_p = 2^p - 1$. The [Lucas-Lehmer sequence](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LucasLehmer.html#LucasLehmer.s) of
[integers](../numbers/integer.md) is defined by

$$s_0 = 4, \qquad s_{i+1} = s_i^2 - 2,$$

so that its first terms are $4, 14, 194, 37634, \dots$
For $p \ge 2$, the test with exponent $p$
[succeeds when $s_{p-2} \equiv 0 \pmod{M_p}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LucasLehmer.html#LucasLehmer.LucasLehmerTest),
that is, when $M_p$ divides $s_{p-2}$ (Mathlib runs the recurrence directly modulo
$M_p$; see In Mathlib). The theorem has two directions.

- **Sufficiency.** [If the test succeeds for an exponent $p \ge 2$, then $M_p$ is prime](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LucasLehmer.html#lucas_lehmer_sufficiency).
- **Necessity.** [If $p \ge 3$ and $M_p$ is prime, then the test succeeds for $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LucasLehmer.html#lucas_lehmer_necessity).

Together they say that for $p \ge 3$, $M_p$ is prime if and only if $M_p$ divides
$s_{p-2}$. In practice only prime exponents are tested, because
[$M_p$ can be prime only when $p$ is prime](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LucasLehmer.html#Nat.Prime.of_mersenne).

## Examples

- For $p = 3, 5, 7, 13$ the residues of $s_{p-2}$ modulo $7, 31, 127, 8191$ are all
  $0$, so these four Mersenne numbers are prime. For $p = 5$ the residues of
  $s_0, s_1, s_2, s_3$ modulo $31$ are $4, 14, 8, 0$.
- For $p = 11$ the residue of $s_9$ modulo $2047$ is $1736$, so $M_{11}$ is
  composite even though $11$ is prime; indeed $2047 = 23 \cdot 89$.
- For $p = 2$ the test fails although $M_2 = 3$ is prime: $s_0 = 4 \equiv 1 \pmod 3$.
  This is why the necessity direction requires $p \ge 3$.

The reduction modulo $M_p$ is cheap in binary, because
[every natural number $k$ is congruent modulo $2^n - 1$ to the sum of its quotient and remainder on division by $2^n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LucasLehmer.html#modEq_mersenne), so reducing amounts to shifting
and adding.

## Proof

Both directions work in the [ring](../rings/ring.md) $X_q = (\mathbb{Z}/q\mathbb{Z})[\sqrt 3]$,
whose elements are pairs $a + b\sqrt 3$ with $a, b$ integers modulo $q$, multiplied
using $\sqrt 3^{\,2} = 3$. Put $\omega = 2 + \sqrt 3$ and $\bar\omega = 2 - \sqrt 3$;
then $\omega\bar\omega = 1$, and induction on $i$ shows that
[$s_i = \omega^{2^i} + \bar\omega^{2^i}$ in $X_q$ for every $i$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LucasLehmer.html#LucasLehmer.X.closed_form).

**Sufficiency.** Suppose the test succeeds but $M_p$ is composite, and let $q$ be
its smallest prime factor. Then [$q^2 \le M_p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Prime/Defs.html#Nat.minFac_sq_le_self), the
statement that the smallest prime factor of a positive number that is not prime has
square at most that number. Since $q$ divides $M_p$, which divides $s_{p-2}$, the
closed form gives $\omega^{2^{p-2}} + \bar\omega^{2^{p-2}} = 0$ in $X_q$; multiplying by
$\omega^{2^{p-2}}$ yields $\omega^{2^{p-1}} = -1$, hence $\omega^{2^p} = 1$. As $M_p$ is
odd, $q > 2$ and $-1 \ne 1$ in $X_q$, so
[$\omega$ has order exactly $2^p$ in the group of units of $X_q$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LucasLehmer.html#LucasLehmer.order_%CF%89)
(see [order of an element](../../../undergraduate/group-theory/basic-definitions/order-of-an-element.md)). But
[the order of an element of a finite group is at most the number of its elements](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/OrderOfElement.html#orderOf_le_card_univ),
and [for $q > 1$ the ring $X_q$ has fewer than $q^2$ units](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LucasLehmer.html#LucasLehmer.X.card_units_lt),
since it has $q^2$ elements and $0$ is not a unit. Hence
$2^p < q^2 \le M_p = 2^p - 1$, a contradiction.

**Necessity.** Let $q = M_p$ be prime with $p \ge 3$. Then
[$2$ is a square modulo $M_p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LucasLehmer.html#legendreSym_mersenne_two), because $M_p \equiv 7 \pmod 8$,
and, since $p$ is prime (because $M_p$ is) and $p \ge 3$, hence odd, [$3$ is not a square modulo $M_p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LucasLehmer.html#legendreSym_mersenne_three),
by [quadratic reciprocity](../number-theory/quadratic-reciprocity.md) together with
$M_p \equiv 3 \pmod 4$ and $M_p \equiv 1 \pmod 3$. The ring $X_q$ has
[characteristic](../field-theory/characteristic-p.md) $q$, and
[for an odd prime $q$ modulo which $3$ is not a square, $(1 + \sqrt 3)^q = 1 - \sqrt 3$ in $X_q$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LucasLehmer.html#LucasLehmer.X.one_add_%CE%B1_pow_q),
since raising to the $q$-th power fixes $\mathbb{Z}/q\mathbb{Z}$ and sends $\sqrt 3$ to
$\sqrt 3 \cdot 3^{(q-1)/2} = -\sqrt 3$. From $(1 + \sqrt 3)^2 = 2\omega$ and the fact that $2$ is a
square one obtains $\omega^{(q+1)/2} = -1$. Here $(q+1)/2 = 2^{p-1}$, and multiplying
$\omega^{2^{p-1}} = -1$ by $\bar\omega^{2^{p-2}}$ gives $\omega^{2^{p-2}} + \bar\omega^{2^{p-2}} = 0$, that is,
$s_{p-2} \equiv 0 \pmod{M_p}$.

## Related concepts

- [Lucas's primality criterion](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LucasPrimality.html#lucas_primality) shows that $n$ is prime when some
  $a$ satisfies $a^{n-1} \equiv 1 \pmod n$ but $a^{(n-1)/r} \not\equiv 1 \pmod n$ for every
  prime $r$ dividing $n - 1$; it suits numbers $n$ for which $n - 1$ is easy to factor,
  while the Lucas-Lehmer test suits numbers for which $n + 1$ is a power of $2$.
- Pépin's test plays the same role for Fermat numbers $F_n = 2^{2^n} + 1$:
  [if $3^{(F_n - 1)/2} \equiv -1 \pmod{F_n}$, then $F_n$ is prime](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Fermat.html#Nat.pepin_primality').

## In Mathlib

Mathlib states the two directions as separate theorems rather than as one
equivalence. The sufficiency direction assumes only $p > 1$, not that $p$ is prime,
and the necessity direction assumes $p \ge 3$; the example $p = 2$ shows that this
bound cannot be lowered. The test itself is phrased as the vanishing of the
recurrence computed directly in the integers modulo $M_p$, and
[for $p \ge 2$ that computation gives the reduction of $s_i$ modulo $M_p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LucasLehmer.html#LucasLehmer.sZMod_eq_s),
so it agrees with the divisibility above. The auxiliary ring $X_q$ is built by hand
as pairs of residues modulo $q$ with the multiplication of $a + b\sqrt 3$, rather than
as a quotient of a polynomial ring, and the sufficiency proof never needs it to be a
field. Mathlib also includes an automatic procedure that evaluates the test for a
given numeral exponent, so the primality of a specific Mersenne number can be proved
by computation inside the system.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Prime numbers](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)
- [Integer](../numbers/integer.md)
- [Congruence in $\Z$](../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in-z.md)

## Proof depends on

- [Ring](../rings/ring.md)
- [Group](../group-theory/part-01/group.md)
- [Order of an element](../../../undergraduate/group-theory/basic-definitions/order-of-an-element.md)
- [Characteristic p](../field-theory/characteristic-p.md)
- [Quadratic reciprocity](../number-theory/quadratic-reciprocity.md)

## Sources

- [Mathlib documentation: `lucas_lehmer_sufficiency`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LucasLehmer.html#lucas_lehmer_sufficiency)
- [Source of `lucas_lehmer_sufficiency` in Mathlib/NumberTheory/LucasLehmer.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/LucasLehmer.lean#L582)
- [Mathlib overview: General algebra › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L93)
