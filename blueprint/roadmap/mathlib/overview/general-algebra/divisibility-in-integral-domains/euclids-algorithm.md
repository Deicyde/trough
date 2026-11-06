---
article_id: af_a797589fc5552e55da1054cb
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Nat.xgcd
mathlib_file: Mathlib/Data/Int/GCD.lean
---

# Euclid's' algorithm

**Euclid's algorithm** computes the [greatest common divisor](greatest-common-divisor.md) of two
[natural numbers](../numbers/natural-number.md) by repeated division with remainder. Its refinement, the
**extended Euclidean algorithm**, also produces [integers](../numbers/integer.md) $x$ and $y$ with
$\gcd(a, b) = ax + by$. The algorithm is fast, needs nothing beyond division with remainder, and the coefficients it returns give
[Bézout's identity](../../../hundred-theorems/part-03/bezouts-theorem.md) in explicit form, inverses in modular arithmetic,
and solutions of linear equations in integers.

## Definition

Let $a$ and $b$ be natural numbers. Put $r_0 = a$ and $r_1 = b$. As long as the current
remainder $r_k$ is nonzero, divide the previous one by it,

$$r_{k-1} = q_k\, r_k + r_{k+1}, \qquad 0 \le r_{k+1} < r_k,$$

which defines the quotient $q_k$ and the next remainder $r_{k+1}$. From $r_1$ on the
remainders strictly decrease, so some $r_{n+1}$ is $0$; the algorithm stops at the first such index and returns
$r_n$. This is the last nonzero remainder, except when $a = b = 0$ and the output is $0$.

The output is $\gcd(a, b)$. For $b > 0$ the equation $a = qb + r$ shows that a number divides
both $a$ and $b$ exactly when it divides both $b$ and $r$, so $\gcd(a, b) = \gcd(b, r)$, where
$r$ is the remainder of $a$ modulo $b$. The pair of consecutive remainders therefore keeps the
same common divisors at every step, and at the end the pair $(r_n, 0)$ has greatest common
divisor $r_n$.

The extended algorithm carries two further sequences alongside the remainders: $s_0 = 1$,
$t_0 = 0$, $s_1 = 0$, $t_1 = 1$, and

$$s_{k+1} = s_{k-1} - q_k s_k, \qquad t_{k+1} = t_{k-1} - q_k t_k.$$

By induction $r_k = a s_k + b t_k$ for every $k$, since the same linear recurrence holds for
all three sequences. At the last nonzero remainder this reads $\gcd(a, b) = a s_n + b t_n$.
In Mathlib the extended algorithm on natural numbers is
[a function returning a pair of integer coefficients](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/GCD.html#Nat.xgcd), and its two components
$x$ and $y$ satisfy [$\gcd(a, b) = ax + by$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/GCD.html#Nat.gcd_eq_gcd_ab).

## Examples

For $a = 385$ and $b = 133$ the divisions are

$$385 = 2 \cdot 133 + 119, \quad 133 = 1 \cdot 119 + 14, \quad 119 = 8 \cdot 14 + 7, \quad 14 = 2 \cdot 7 + 0,$$

so $\gcd(385, 133) = 7$. The coefficient sequences run $s = 1, 0, 1, -1, 9, -19$ and
$t = 0, 1, -2, 3, -26, 55$, and the row of the last nonzero remainder gives

$$7 = 385 \cdot 9 + 133 \cdot (-26).$$

The final row, with remainder $0$, records $0 = 133 \cdot 55 - 385 \cdot 19$, and indeed
$19 = 133/7$ and $55 = 385/7$.

To invert $7$ modulo $40$, run the algorithm on $40$ and $7$: the divisions
$40 = 5 \cdot 7 + 5$, $7 = 1 \cdot 5 + 2$, $5 = 2 \cdot 2 + 1$ end at remainder $1$, and
substituting back gives $1 = 3 \cdot 40 - 17 \cdot 7$. Hence $7 \cdot (-17) \equiv 1 \pmod{40}$,
and $23$, the residue of $-17$, is the inverse of $7$ modulo $40$.

## Properties

- **Speed.** From the second division on, every two steps the remainder drops below half
  its earlier value: $r_{k+1} < r_{k-1}/2$ for $k \ge 2$, and also for $k = 1$ when $a \ge b$.
  The number of divisions is therefore at most about twice the
  number of binary digits of $b$. Lamé's theorem sharpens this: for $a \ge b \ge 1$ the
  number of divisions is at most five times the number of decimal digits of $b$.
  For $a > b \ge 1$, if the algorithm needs $n$ divisions then $a \ge F_{n+2}$ and
  $b \ge F_{n+1}$, where $F_1 = F_2 = 1$ are the first Fibonacci numbers; consecutive
  Fibonacci numbers, whose quotients are all $1$ except the last, attain this bound.
- **Linear combinations.** For integers $a$ and $b$, a natural number $n$ can be written as
  $ax + by$ with integers $x, y$
  [exactly when $\gcd(a, b)$ divides $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/GCD.html#Int.gcd_dvd_iff), and when $a \neq 0$
  [$\gcd(a, b)$ is the least positive number of this form](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/GCD.html#Int.gcd_least_linear).
  Running the extended algorithm on $|a|$ and $|b|$, changing the signs of the two
  coefficients to match those of $a$ and $b$, and multiplying them by $n/\gcd(a, b)$ solves
  $ax + by = n$ whenever a solution exists.
- **Modular inverses.** If $n$ and $k$ are coprime and $k > 1$, the coefficient of $n$ in
  $1 = nx + ky$ reduced modulo $k$ is an inverse of $n$: there is
  [an $m$ with $0 \le m < k$ and $nm \equiv 1 \pmod k$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/GCD.html#Nat.exists_mul_mod_eq_one_of_coprime).
  This is how inverses are computed in practice, and it underlies the constructive proof of
  the [Chinese remainder theorem](../ideals-and-quotients/chinese-remainder-theorem.md).
- **Euclid's lemma.** For integers $a$, $b$, $c$, multiplying $1 = ax + cy$ by $b$ shows that
  [if $a$ divides $bc$ and $\gcd(a, c) = 1$, then $a$ divides $b$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/GCD.html#Int.dvd_of_dvd_mul_left_of_gcd_one),
  the key step towards the uniqueness of prime factorizations.
- **Continued fractions.** For $a, b > 0$ the quotients $q_1, \dots, q_n$ are the partial
  quotients of the [continued fraction](../numbers/continued-fraction.md) of $a/b$; for the example above,
  $385/133 = 2 + 1/(1 + 1/(8 + 1/2))$.

## Generalizations

The algorithm uses only division with remainder, so it runs in every
[Euclidean domain](euclidean-domain.md), where a size function replaces the usual order
on remainders. Examples are the integers ([a Euclidean domain](../../../undergraduate/ring-theory/divisibility-in-integral-domains/z-is-a-euclidean-ring.md)) and
[polynomials in one variable over a field](../polynomials-and-power-series/k-x-is-euclidean.md). The
[general version](../../../hundred-theorems/part-03/greatest-common-divisor-algorithm.md) rests on the same step,
[$\gcd(a, b) = \gcd(b \bmod a, a)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Basic.html#EuclideanDomain.gcd_val); its output
[divides both inputs](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Basic.html#EuclideanDomain.gcd_dvd) and
[is divisible by every common divisor](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Basic.html#EuclideanDomain.dvd_gcd). The
[extended version](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Defs.html#EuclideanDomain.xgcd) again returns coefficients with
[$\gcd(a, b) = a x + b y$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Basic.html#EuclideanDomain.gcd_eq_gcd_ab). In such a ring the greatest
common divisor is determined only up to a unit factor, and the algorithm picks one. For the
integers, the coefficients can be read off from those for the absolute values, giving
[Bézout's identity over the integers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/GCD.html#Int.gcd_eq_gcd_ab). In rings that are not
Euclidean, such as polynomials in two variables, a greatest common divisor may exist without
being a combination $ax + by$.

## In Mathlib

Mathlib runs the extended algorithm on two natural numbers and returns the two coefficients
as integers, since one of them is usually negative. The recursion keeps two triples, each a
remainder with its two coefficients; each step forms a new triple from the two and drops the
older one; the first division divides the second input by the first, so when the first input is
the larger one the opening step merely swaps the two. Whatever coefficients the recursion starts
from, [its final remainder is the greatest common divisor](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/GCD.html#Nat.xgcdAux_fst), and started
from the triples for the two inputs it
[returns that divisor together with the coefficient pair](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/GCD.html#Nat.xgcdAux_val). The greatest
common divisor of natural numbers comes from Lean's core library, which computes it by the
same recursion and sets $\gcd(0, b) = b$. Accordingly, when the first input is $0$
[the first coefficient is $0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/GCD.html#Nat.gcdA_zero_left) and
[the second is $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/GCD.html#Nat.gcdB_zero_left), while for a nonzero first input and second input
$0$ [the first coefficient is $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/GCD.html#Nat.gcdA_zero_right) and
[the second is $0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/GCD.html#Nat.gcdB_zero_right). The integer versions reduce to the natural ones
by adjusting signs, and the Euclidean-domain versions are separate definitions written for
any such ring with decidable equality.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Natural number](../numbers/natural-number.md)
- [Integer](../numbers/integer.md)
- [Greatest common divisor](greatest-common-divisor.md)

## Sources

- [Mathlib documentation: `Nat.xgcd`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/GCD.html#Nat.xgcd)
- [Source of `Nat.xgcd` in Mathlib/Data/Int/GCD.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Data/Int/GCD.lean#L60)
- [Mathlib overview: General algebra › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L91)
- [Mathlib undergraduate list: Ring Theory › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L150)
