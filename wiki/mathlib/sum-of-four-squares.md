---
article_id: af_65dae603bcad3a51819a6860
concept: Nat.sum_four_squares
---

**Lagrange's four-square theorem** says that every [natural number](trough:Nat) is a sum
of four squares of natural numbers. Four is the least number that works for all
natural numbers, since $7$ is not a sum of three squares, so the theorem settles
completely which count of squares suffices. It is a model case of an additive
problem in number theory, and its proof combines an algebraic identity with a
descent argument on [prime numbers](trough:Prime).

## Statement

For every natural number $n$ there are natural numbers $a, b, c, d$ with

$$n = a^2 + b^2 + c^2 + d^2$$

([the four-square theorem](lean:Nat.sum_four_squares)). Zero is allowed among
$a, b, c, d$, so the theorem equivalently says that every natural number is a sum of
at most four nonzero squares. Since natural numbers are integers, and an integer and its
negative have the same square, the statement is equivalent to its version with $a, b, c, d$
ranging over the [integers](trough:Int).

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

([the identity](lean:euler_four_squares)), which is checked by expanding both sides.
So a product of two sums of four squares is again one. Since $0$ and $1$ are sums of
four squares and every integer $n \ge 2$ is a product of primes, it suffices to treat
primes.

**A first multiple of $p$.** Let $p$ be a prime. [Every residue class modulo $p$ is a
sum of two squares of residues](lean:ZMod.sq_add_sq). For $p = 2$ this is clear from
$0 = 0^2 + 0^2$ and $1 = 1^2 + 0^2$. For odd $p$ and a residue $c$, the $(p+1)/2$ residues
$x^2$ with $0 \le x \le (p-1)/2$ are distinct, as are the $(p+1)/2$ residues $c-y^2$ with
$0 \le y \le (p-1)/2$, so the two lists, with $p+1$ entries among $p$ classes, share a value,
and $x^2 + y^2 \equiv c$. Taking $c = -1$, with $x$ and $y$ at most $p/2$, shows that
[there are natural numbers $a, b, k$ with $0 < k < p$ and $a^2 + b^2 + 1 = kp$](lean:Int.exists_sq_add_sq_add_one_eq_mul).
Hence some multiple $mp$ with $0 < m < p$ is a sum of four squares.

**Descent.** Let $m$ be the least positive integer such that $mp$ is a sum of four squares
$a^2+b^2+c^2+d^2$, and suppose $m > 1$; then $m < p$.

- If $m$ is even, the four numbers can be split into two pairs whose members have the same
  parity. For such a pair, [if $2u = x^2 + y^2$ for integers $u, x, y$, then
  $u = \bigl(\tfrac{x-y}{2}\bigr)^2 + \bigl(\tfrac{x+y}{2}\bigr)^2$](lean:Int.sq_add_sq_of_two_mul_sq_add_sq),
  so $(m/2)p$ is a sum of four squares, contradicting minimality.
- If $m$ is odd, replace each of $a, b, c, d$ by the integer congruent to it modulo $m$
  with absolute value less than $m/2$. The four new squares add up to a multiple $rm$ of $m$.
  Applied to the absolute values of the new numbers, which are natural numbers less than $m/2$,
  [a sum of four squares of natural numbers each less than $m/2$ that equals $rm$ forces
  $r < m$](lean:Int.lt_of_sum_four_squares_eq_mul). If $r = 0$, then $m$ divides $a, b, c, d$,
  so $m^2$ divides $mp$ and $m$ divides $p$, which is impossible. Otherwise Euler's identity,
  with suitable signs, writes $(mp)(rm)$ as a sum of four squares of multiples of $m$; dividing
  each by $m$ writes $rp$ as a sum of four squares with $0 < r < m$, again a contradiction.

So $m = 1$, and [every prime is a sum of four squares](lean:Nat.Prime.sum_four_squares).

## Related results

- **[Sum of two squares](trough:Nat.Prime.sq_add_sq).** Two squares suffice far less often:
  [every prime not congruent to $3$ modulo $4$ is a sum of two
  squares](lean:Nat.Prime.sq_add_sq), and [a positive integer is a sum of two squares if and
  only if every prime congruent to $3$ modulo $4$ occurs to an even power in its prime
  factorization](lean:Nat.eq_sq_add_sq_iff).
- **Three squares.** Legendre's three-square theorem states that a natural number is a sum of
  three squares if and only if it is not of the form $4^a(8b+7)$ with natural numbers $a, b$.
  Numbers of that form, such as $7$, $15$, $23$ and $28$, need four nonzero squares.
- **[Jacobi's four-square theorem](trough:1000:Q3527095)** counts the representations: for
  $n \ge 1$, the number of ordered quadruples of integers $(a, b, c, d)$ with
  $a^2+b^2+c^2+d^2 = n$ is eight times the sum of the divisors of $n$ that are not divisible
  by $4$.
- **Waring's problem** asks, for each exponent $k$, for a number of $k$-th powers that
  suffices to write every natural number. The [Hilbert–Waring theorem](trough:1000:Q657903)
  says that such a number exists for every $k$, and the four-square theorem answers the case
  $k = 2$ with the optimal value $4$.
- **[Fermat polygonal number theorem](trough:1000:Q1146791).** For each $s \ge 3$, every natural number is a sum
  of at most $s$ $s$-gonal numbers; the case $s = 4$ is the four-square theorem.
- **Quaternions.** Euler's identity expresses that [the norm of Hamilton's quaternions is
  multiplicative](lean:Quaternion.normSq), where for coefficients in a commutative ring the
  norm of $a + bi + cj + dk$ is [$a^2+b^2+c^2+d^2$](lean:Quaternion.normSq_def'). The theorem says that the
  [quadratic form](trough:QuadraticForm) $a^2+b^2+c^2+d^2$ takes every natural number as a value
  on integer inputs.

## In Mathlib

Mathlib states the theorem for natural numbers, with the four squares taken of natural
numbers and zero allowed among them. Euler's identity is proved for an arbitrary commutative
ring, and a separate version for natural numbers replaces each of the four bracketed integers
by its absolute value, so that
[the product of two sums of four squares of natural numbers is a sum of four squares of
natural numbers](lean:Nat.euler_four_squares). The prime case is proved first by the descent
above, and the general case follows by induction over products of primes. The fact that every
residue modulo a prime is a sum of two squares is deduced, for odd primes, from a general
counting lemma about two quadratic polynomials over a finite field of odd order.

## Depends on

- [Natural number](trough:Nat)

## Proof depends on

- [Prime numbers](trough:Prime)
- [Integer](trough:Int)
- [Congruence in $\Z$](trough:Int.ModEq)
