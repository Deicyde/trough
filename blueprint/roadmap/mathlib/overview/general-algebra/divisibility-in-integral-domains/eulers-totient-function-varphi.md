---
article_id: af_e68bb2f066366e6348974b7c
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Nat.totient
mathlib_file: Mathlib/Data/Nat/Totient.lean
---

# Euler's totient function ($\varphi$)

**Euler's totient function**, written $\varphi$, assigns to each positive
[natural number](../numbers/natural-number.md) $n$ the number of integers between $1$ and $n$ that
are coprime to $n$, that is, share no common factor with $n$ other than $1$. It is
one of the basic functions of elementary number theory. It counts the invertible
residues modulo $n$, so it is the exponent in [Euler's theorem](../../../hundred-theorems/part-01/eulers-generalization-of-fermats-little-theorem.md), and it reappears in the theory of
[cyclic groups](../group-theory/part-01/cyclic-group.md), roots of unity and
[cyclotomic polynomials](../../../undergraduate/ring-theory/polynomial-rings/cyclotomic-polynomials-in-q-x.md).

## Definition

For a natural number $n \ge 1$,

$$\varphi(n) = \#\{\, a : 1 \le a \le n,\ \gcd(a, n) = 1 \,\},$$

where $\gcd$ is the [greatest common divisor](greatest-common-divisor.md). Counting
over $0 \le a \le n - 1$ instead gives the same number: the endpoint $n$ is
replaced by $0$, and $\gcd(0, n) = \gcd(n, n) = n$, so either endpoint is counted
exactly when $n = 1$.

An equivalent description uses modular arithmetic. A residue class $a$ modulo $n$
has a multiplicative inverse exactly when $\gcd(a, n) = 1$ (see
[$\mathbb{Z}/n\mathbb{Z}$ and its invertible elements](../../../undergraduate/ring-theory/divisibility-in-integral-domains/z-n-z-and-its-invertible-elements.md)),
so for $n \ge 1$
[the group of units of $\mathbb{Z}/n\mathbb{Z}$ has exactly $\varphi(n)$ elements](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Totient.html#ZMod.card_units_eq_totient).

## Examples

The first values, for $n = 1, 2, \dots, 12$, are

$$1,\ 1,\ 2,\ 2,\ 4,\ 2,\ 6,\ 4,\ 6,\ 4,\ 10,\ 4.$$

For instance $\varphi(12) = 4$, the integers coprime to $12$ in that range being
$1, 5, 7, 11$.

- **Primes.** If $p$ is [prime](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md), every integer from $1$ to $p - 1$
  is coprime to $p$, so [$\varphi(p) = p - 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Totient.html#Nat.totient_prime).
  Conversely, [a number $p \ge 1$ with $\varphi(p) = p - 1$ is prime](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Totient.html#Nat.totient_eq_iff_prime).
- **Prime powers.** Among $1, \dots, p^k$ the integers not coprime to $p^k$ are the
  multiples of $p$, of which there are $p^{k-1}$. Hence, for a prime $p$ and
  $k \ge 1$, [$\varphi(p^k) = p^{k-1}(p - 1)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Totient.html#Nat.totient_prime_pow). For
  example $\varphi(8) = 4$ and $\varphi(9) = 6$.

## Properties

- **Multiplicativity.** If $m$ and $n$ are coprime, then
  [$\varphi(mn) = \varphi(m)\,\varphi(n)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Totient.html#Nat.totient_mul). Thus
  $\varphi(36) = \varphi(4)\,\varphi(9) = 2 \cdot 6 = 12$. Without the coprimality
  hypothesis one still has
  [$\varphi(\gcd(a, b))\,\varphi(ab) = \varphi(a)\,\varphi(b)\,\gcd(a, b)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Totient.html#Nat.totient_gcd_mul_totient_mul)
  for all natural numbers $a$ and $b$.
- **Product formula.** Combining multiplicativity, the value at prime powers and
  [unique factorization](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md) gives
  [Euler's product formula: for every $n \ge 1$, $\varphi(n)$ equals $n$ times the product of $1 - 1/p$ over the distinct primes $p$ dividing $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Totient.html#Nat.totient_eq_mul_prod_factors),
  $$\varphi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right).$$
  For $n = 36$ this is
  $36 \cdot \tfrac12 \cdot \tfrac23 = 12$.
- **Divisor sum.** [Summing $\varphi(d)$ over the divisors $d$ of $n$ gives $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Totient.html#Nat.sum_totient):
  $$\sum_{d \mid n} \varphi(d) = n.$$
  For $n = 12$ the divisors $1, 2, 3, 4, 6, 12$ contribute $1 + 1 + 2 + 2 + 2 + 4 = 12$.
- **Size.** [$\varphi(n) \le n$ for every $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Totient.html#Nat.totient_le), and
  [$\varphi(n) < n$ when $n > 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Totient.html#Nat.totient_lt), since $n$ itself is then
  not coprime to $n$.
- **Parity.** [$\varphi(n)$ is even for $n > 2$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Totient.html#Nat.totient_even): the map
  $a \mapsto n - a$ pairs the integers coprime to $n$, and no such $a$ equals
  $n - a$. Consequently [$\varphi(n) = 1$ exactly when $n = 1$ or $n = 2$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Totient.html#Nat.totient_eq_one_iff).
- **Divisibility.** [If $a$ divides $b$, then $\varphi(a)$ divides $\varphi(b)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Totient.html#Nat.totient_dvd_of_dvd).

## Proofs of the main formulas

Multiplicativity follows from the [Chinese remainder theorem](../ideals-and-quotients/chinese-remainder-theorem.md): for coprime $m$ and $n$
the ring $\mathbb{Z}/mn\mathbb{Z}$ is isomorphic to the product
$\mathbb{Z}/m\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$, and the units of a product
of rings are the pairs of units, so the unit groups have $\varphi(mn)$ and
$\varphi(m)\,\varphi(n)$ elements respectively.

For the divisor sum, sort the integers $1, \dots, n$ by their greatest common
divisor $d$ with $n$. Those with $\gcd(a, n) = d$ are the numbers $a = db$ with
$1 \le b \le n/d$ and $\gcd(b, n/d) = 1$, so there are $\varphi(n/d)$ of them.
Summing over the divisors $d$ of $n$ counts every integer once, and as $d$ runs
over the divisors of $n$ so does $n/d$.

## Applications

- **[Euler's theorem](../../../hundred-theorems/part-01/eulers-generalization-of-fermats-little-theorem.md).** By
  [Lagrange's theorem](../group-theory/part-02/lagranges-theorem.md) applied to the units
  modulo $n$,
  [$a^{\varphi(n)} \equiv 1 \pmod n$ for every natural number $a$ coprime to $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Basic.html#Nat.ModEq.pow_totient).
  For a prime modulus this is [Fermat's little theorem](../../../thousand-plus/number-theory/part-02/fermats-little-theorem.md).
  For example $3^{\varphi(10)} = 3^4 = 81 \equiv 1 \pmod{10}$.
- **Cyclic groups.** In a finite cyclic group of order $n$, for each divisor $d$
  of $n$, [exactly $\varphi(d)$ elements have order $d$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Cyclic.html#IsCyclic.card_orderOf_eq_totient)
  (see [order of an element](../../../undergraduate/group-theory/basic-definitions/order-of-an-element.md)). Taking $d = n$, such a group has
  $\varphi(n)$ generators.
- **Roots of unity.** In an integral domain that contains a primitive $k$-th root
  of unity, [there are exactly $\varphi(k)$ primitive $k$-th roots of unity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/PrimitiveRoots.html#IsPrimitiveRoot.card_primitiveRoots).
- **Cyclotomic polynomials.** Over any nonzero ring, [the $n$-th cyclotomic polynomial has degree $\varphi(n)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Cyclotomic/Basic.html#Polynomial.natDegree_cyclotomic).

## Related concepts

The totient function is a multiplicative [arithmetic function](../number-theory/arithmetic-functions.md),
and the divisor sum identity expresses that its Dirichlet convolution with the
constant function $1$ is the identity function $n \mapsto n$.

## In Mathlib

Mathlib defines the function on all natural numbers:
[$\varphi(n)$ is the number of natural numbers $a$ with $a < n$ that are coprime to $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Totient.html#Nat.totient).
For $n \ge 1$ this agrees with the count over $1, \dots, n$ by the endpoint argument
above. At $n = 0$ the range is empty, so
[$\varphi(0) = 0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Totient.html#Nat.totient_zero), and [$0$ is the only number at which $\varphi$ vanishes](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Totient.html#Nat.totient_eq_zero). With this convention multiplicativity,
the bound $\varphi(n) \le n$, the divisor sum (Mathlib's finite set of divisors of
$0$ is defined to be empty, so the sum is $0$) and Euler's theorem hold for all
natural numbers without excluding $0$. The product formula is stated as an equality
of rational numbers, and it also holds at $n = 0$, where both sides are $0$.
The count of units of $\mathbb{Z}/n\mathbb{Z}$ assumes $n \neq 0$, since the integers
modulo $0$ are the integers themselves.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Natural number](../numbers/natural-number.md)
- [Greatest common divisor](greatest-common-divisor.md)

## Proof depends on

- [Chinese remainder theorem](../ideals-and-quotients/chinese-remainder-theorem.md)
- [$\Z/n\Z$ and its invertible elements](../../../undergraduate/ring-theory/divisibility-in-integral-domains/z-n-z-and-its-invertible-elements.md)

## Sources

- [Mathlib documentation: `Nat.totient`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Totient.html#Nat.totient)
- [Source of `Nat.totient` in Mathlib/Data/Nat/Totient.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Data/Nat/Totient.lean#L35)
- [Mathlib overview: General algebra › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L92)
- [Mathlib undergraduate list: Ring Theory › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L156)
