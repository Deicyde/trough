---
article_id: af_65dae603bcad3a51819a6860
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Nat.sum_four_squares
mathlib_file: Mathlib/NumberTheory/SumFourSquares.lean
---

# Sum of four squares

**Lagrange's four-square theorem** says that every [natural number](../numbers/natural-number.md) is a sum
of four squares of natural numbers. Four is the least number that works for all
natural numbers, since $7$ is not a sum of three squares, so the theorem settles
completely which count of squares suffices. It is a model case of an additive
problem in number theory, and its proof combines an algebraic identity with a
descent argument on [prime numbers](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md).

## Statement

For every natural number $n$ there are natural numbers $a, b, c, d$ with

$$n = a^2 + b^2 + c^2 + d^2$$

([the four-square theorem](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumFourSquares.html#Nat.sum_four_squares)). Zero is allowed among
$a, b, c, d$, so the theorem equivalently says that every natural number is a sum of
at most four nonzero squares. Since natural numbers are integers, and an integer and its
negative have the same square, the statement is equivalent to its version with $a, b, c, d$
ranging over the [integers](../numbers/integer.md).

## Examples

- $0 = 0^2 + 0^2 + 0^2 + 0^2$ and $1 = 1^2 + 0^2 + 0^2 + 0^2$.
- $7 = 2^2 + 1^2 + 1^2 + 1^2$, and three squares do not suffice: every square is
  congruent to $0$, $1$ or $4$ modulo $8$, and no sum of three of these residues is
  congruent to $7$ modulo $8$.
- $15 = 3^2 + 2^2 + 1^2 + 1^2$ and $23 = 3^2 + 3^2 + 2^2 + 1^2$, two more numbers that
  need four nonzero squares.
- A representation need not be unique: $28 = 4^2 + 2^2 + 2^2 + 2^2 = 5^2 + 1^2 + 1^2 + 1^2$.

## Proof

The proof has three steps.

**Euler's four-square identity.** In every commutative ring,

$$\begin{aligned}
(a^2+b^2+c^2+d^2)(x^2+y^2+z^2+w^2) &= (ax-by-cz-dw)^2 + (ay+bx+cw-dz)^2 \\
&\quad + (az-bw+cx+dy)^2 + (aw+bz-cy+dx)^2
\end{aligned}$$

([the identity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumFourSquares.html#euler_four_squares)), which is checked by expanding both sides.
So a product of two sums of four squares is again one. Since $0$ and $1$ are sums of
four squares and every integer $n \ge 2$ is a product of primes, it suffices to treat
primes.

**A first multiple of $p$.** Let $p$ be a prime. [Every residue class modulo $p$ is a sum of two squares of residues](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Basic.html#ZMod.sq_add_sq). For $p = 2$ this is clear from
$0 = 0^2 + 0^2$ and $1 = 1^2 + 0^2$. For odd $p$ and a residue $c$, the $(p+1)/2$ residues
$x^2$ with $0 \le x \le (p-1)/2$ are distinct, as are the $(p+1)/2$ residues $c-y^2$ with
$0 \le y \le (p-1)/2$, so the two lists, with $p+1$ entries among $p$ classes, share a value,
and $x^2 + y^2 \equiv c$. Taking $c = -1$, with $x$ and $y$ at most $p/2$, shows that
[there are natural numbers $a, b, k$ with $0 < k < p$ and $a^2 + b^2 + 1 = kp$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumFourSquares.html#Int.exists_sq_add_sq_add_one_eq_mul).
Hence some multiple $mp$ with $0 < m < p$ is a sum of four squares.

**Descent.** Let $m$ be the least positive integer such that $mp$ is a sum of four squares
$a^2+b^2+c^2+d^2$, and suppose $m > 1$; then $m < p$.

- If $m$ is even, the four numbers can be split into two pairs whose members have the same
  parity. For such a pair, [if $2u = x^2 + y^2$ for integers $u, x, y$, then $u = \bigl(\tfrac{x-y}{2}\bigr)^2 + \bigl(\tfrac{x+y}{2}\bigr)^2$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumFourSquares.html#Int.sq_add_sq_of_two_mul_sq_add_sq),
  so $(m/2)p$ is a sum of four squares, contradicting minimality.
- If $m$ is odd, replace each of $a, b, c, d$ by the integer congruent to it modulo $m$
  with absolute value less than $m/2$. The four new squares add up to a multiple $rm$ of $m$.
  Applied to the absolute values of the new numbers, which are natural numbers less than $m/2$,
  [a sum of four squares of natural numbers each less than $m/2$ that equals $rm$ forces $r < m$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumFourSquares.html#Int.lt_of_sum_four_squares_eq_mul). If $r = 0$, then $m$ divides $a, b, c, d$,
  so $m^2$ divides $mp$ and $m$ divides $p$, which is impossible. Otherwise Euler's identity,
  with suitable signs, writes $(mp)(rm)$ as a sum of four squares of multiples of $m$; dividing
  each by $m$ writes $rp$ as a sum of four squares with $0 < r < m$, again a contradiction.

So $m = 1$, and [every prime is a sum of four squares](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumFourSquares.html#Nat.Prime.sum_four_squares).

## Related results

- **[Sum of two squares](sum-of-two-squares.md).** Two squares suffice far less often:
  [every prime not congruent to $3$ modulo $4$ is a sum of two squares](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumTwoSquares.html#Nat.Prime.sq_add_sq), and [a positive integer is a sum of two squares if and only if every prime congruent to $3$ modulo $4$ occurs to an even power in its prime factorization](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumTwoSquares.html#Nat.eq_sq_add_sq_iff).
- **Three squares.** Legendre's three-square theorem states that a natural number is a sum of
  three squares if and only if it is not of the form $4^a(8b+7)$ with natural numbers $a, b$.
  Numbers of that form, such as $7$, $15$, $23$ and $28$, need four nonzero squares.
- **Jacobi's four-square theorem** counts the representations: for
  $n \ge 1$, the number of ordered quadruples of integers $(a, b, c, d)$ with
  $a^2+b^2+c^2+d^2 = n$ is eight times the sum of the divisors of $n$ that are not divisible
  by $4$.
- **Waring's problem** asks, for each exponent $k$, for a number of $k$-th powers that
  suffices to write every natural number. The Hilbert–Waring theorem
  says that such a number exists for every $k$, and the four-square theorem answers the case
  $k = 2$ with the optimal value $4$.
- **Fermat polygonal number theorem.** For each $s \ge 3$, every natural number is a sum
  of at most $s$ $s$-gonal numbers; the case $s = 4$ is the four-square theorem.
- **Quaternions.** Euler's identity expresses that [the norm of Hamilton's quaternions is multiplicative](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Quaternion.html#Quaternion.normSq), where for coefficients in a commutative ring the
  norm of $a + bi + cj + dk$ is [$a^2+b^2+c^2+d^2$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Quaternion.html#Quaternion.normSq_def'). The theorem says that the
  [quadratic form](../../linear-algebra/bilinear-and-quadratic-forms/quadratic-form.md) $a^2+b^2+c^2+d^2$ takes every natural number as a value
  on integer inputs.

## In Mathlib

Mathlib states the theorem for natural numbers, with the four squares taken of natural
numbers and zero allowed among them. Euler's identity is proved for an arbitrary commutative
ring, and a separate version for natural numbers replaces each of the four bracketed integers
by its absolute value, so that
[the product of two sums of four squares of natural numbers is a sum of four squares of natural numbers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumFourSquares.html#Nat.euler_four_squares). The prime case is proved first by the descent
above, and the general case follows by induction over products of primes. The fact that every
residue modulo a prime is a sum of two squares is deduced, for odd primes, from a general
counting lemma about two quadratic polynomials over a finite field of odd order.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Natural number](../numbers/natural-number.md)

## Proof depends on

- [Prime numbers](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)
- [Integer](../numbers/integer.md)
- [Congruence in $\Z$](../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in-z.md)

## Sources

- [Mathlib documentation: `Nat.sum_four_squares`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumFourSquares.html#Nat.sum_four_squares)
- [Source of `Nat.sum_four_squares` in Mathlib/NumberTheory/SumFourSquares.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/SumFourSquares.lean#L201)
- [Mathlib overview: General algebra › Number theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L143)
- [Freek Wiedijk's 100 theorems, no. 19](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L95)
- [1000+ theorems list: Q756946](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L851)
- [1000+ theorems project: Q756946](https://1000-plus.github.io/all.html?length=-1#Q756946)
- [Wikipedia: Lagrange's four-square theorem](https://en.wikipedia.org/wiki/Lagrange's_four-square_theorem)
- [Wikidata: Q756946](https://www.wikidata.org/wiki/Q756946)
