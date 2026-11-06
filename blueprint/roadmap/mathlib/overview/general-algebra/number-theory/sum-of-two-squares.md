---
article_id: af_8ec1e80bab443b4219660c45
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Nat.Prime.sq_add_sq
mathlib_file: Mathlib/NumberTheory/SumTwoSquares.lean
---

# Sum of two squares

**Fermat's theorem on sums of two squares** says that an odd [prime number](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)
$p$ can be written as $p = a^2 + b^2$ with integers $a$ and $b$ if and only if
$p \equiv 1 \pmod 4$. Together with $2 = 1^2 + 1^2$, this settles which primes
are sums of two squares, and because such sums are closed under multiplication it
leads to a description of every sum of two squares through its prime
factorization. The theorem is a basic result in the arithmetic of
[quadratic forms](../../linear-algebra/bilinear-and-quadratic-forms/quadratic-form.md) and describes how ordinary primes factor
in the Gaussian integers.

## Statement

Let $p$ be a prime. If $p$ is not congruent to $3$ modulo $4$, that is, if $p = 2$
or $p \equiv 1 \pmod 4$, then
[there are natural numbers $a$ and $b$ with $a^2 + b^2 = p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumTwoSquares.html#Nat.Prime.sq_add_sq).
Conversely, a prime $p \equiv 3 \pmod 4$ is never a sum of two squares: every
square is congruent to $0$ or $1$ modulo $4$, so a sum of two squares is
congruent to $0$, $1$ or $2$ modulo $4$.

The representation is essentially unique: if $p = a^2 + b^2 = c^2 + d^2$ with
$a, b, c, d \ge 0$, then $\{a, b\} = \{c, d\}$. The reason is unique factorization
in the Gaussian integers: an element of norm $p$ is irreducible, so
$p = (a + bi)(a - bi)$ is a factorization into Gaussian primes, and $c + di$, which
also has norm $p$ and divides $p$, must be an associate of $a + bi$ or of $a - bi$.
These associates are $\pm a \pm bi$ and $\pm b \pm ai$.

## Examples

The primes below $50$ that are congruent to $1$ modulo $4$ decompose as

$$5 = 1^2 + 2^2, \quad 13 = 2^2 + 3^2, \quad 17 = 1^2 + 4^2, \quad 29 = 2^2 + 5^2, \quad 37 = 1^2 + 6^2, \quad 41 = 4^2 + 5^2.$$

The primes $3, 7, 11, 19, 23, 31, 43, 47$ are congruent to $3$ modulo $4$ and are
not sums of two squares.

## Proof

The case $p = 2$ is $1^2 + 1^2$, so let $p \equiv 1 \pmod 4$.

**Step 1: $-1$ is a square modulo $p$.** For a prime $p$,
[$-1$ is a square modulo $p$ if and only if $p$ is not congruent to $3$ modulo $4$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LegendreSymbol/Basic.html#ZMod.exists_sq_eq_neg_one_iff).
The direction needed here follows from [Wilson's theorem](../../../hundred-theorems/part-02/wilsons-lemma.md),
$(p-1)! \equiv -1 \pmod p$. Pairing each factor $j \le (p-1)/2$ with
$p - j \equiv -j$ gives

$$(p-1)! \equiv (-1)^{(p-1)/2} \left( \left( \tfrac{p-1}{2} \right)! \right)^2 \pmod p,$$

and since $(p-1)/2$ is even, $k = \left( \tfrac{p-1}{2} \right)!$ satisfies
$k^2 \equiv -1 \pmod p$.

**Step 2: $p$ is not prime in the Gaussian integers.** The Gaussian integers
$\mathbb{Z}[i] = \{x + yi : x, y \in \mathbb{Z}\}$ form a
[Euclidean domain](../divisibility-in-integral-domains/euclidean-domain.md) for the norm $N(x + yi) = x^2 + y^2$,
which is multiplicative. Hence $\mathbb{Z}[i]$ is a
[principal ideal domain](../divisibility-in-integral-domains/principal-ideal-domain.md), and in it every
[irreducible element](../divisibility-in-integral-domains/irreducible-element.md) is prime. Now $p$ divides
$k^2 + 1 = (k + i)(k - i)$ but divides neither factor, since $(k \pm i)/p$ has
imaginary part $\pm 1/p$, which is not an integer. So $p$ is not prime in
$\mathbb{Z}[i]$, and therefore not irreducible. More precisely,
[a prime number stays prime in $\mathbb{Z}[i]$ if and only if it is congruent to $3$ modulo $4$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Zsqrtd/QuadraticReciprocity.html#GaussianInt.prime_iff_mod_four_eq_three_of_nat_prime).

**Step 3: taking norms.** Since $N(p) = p^2 \ne 1$, the element $p$ is neither zero
nor a unit, and since it is not irreducible it can be written as
$p = \alpha \beta$ with neither $\alpha$ nor $\beta$ a unit. Then $N(\alpha) N(\beta) = N(p) = p^2$, and neither norm is $1$,
because the elements of norm $1$ are exactly the units. So $N(\alpha) = p$, and
writing $\alpha = a + bi$ gives $a^2 + b^2 = p$. This step is the statement that
[a prime number that is not irreducible in $\mathbb{Z}[i]$ is a sum of two squares](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Zsqrtd/GaussianInt.html#GaussianInt.sq_add_sq_of_nat_prime_of_not_irreducible).

## Consequences

- **Products.** The identity
  [$(x_1^2 + x_2^2)(y_1^2 + y_2^2) = (x_1 y_1 - x_2 y_2)^2 + (x_1 y_2 + x_2 y_1)^2$, valid in every commutative ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Identities.html#sq_add_sq_mul_sq_add_sq),
  known as the Brahmagupta–Fibonacci identity, expresses the multiplicativity of
  the norm on $\mathbb{Z}[i]$. It shows that
  [the product of two natural numbers that are sums of two squares is again a sum of two squares](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumTwoSquares.html#Nat.sq_add_sq_mul).
  For instance $5 = 1^2 + 2^2$ and $13 = 2^2 + 3^2$ give $65 = 4^2 + 7^2$.
- **Which numbers are sums of two squares.** Combining the theorem with the
  product rule, the [fundamental theorem of arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md),
  and the fact that a prime $q \equiv 3 \pmod 4$ dividing $x^2 + y^2$ divides both $x$
  and $y$ (because $-1$ is not a square modulo $q$) gives the criterion:
  [a positive integer $n$ is a sum of two squares if and only if every prime $q \equiv 3 \pmod 4$ occurs in the prime factorization of $n$ with an even exponent](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumTwoSquares.html#Nat.eq_sq_add_sq_iff).
  Thus $45 = 3^2 \cdot 5 = 6^2 + 3^2$, while $21 = 3 \cdot 7$ is not a sum of two squares.
- **Square roots of $-1$.**
  [A natural number $n$ is a sum of two squares if and only if $n = a^2 b$ for natural numbers $a$ and $b$ such that $-1$ is a square modulo $b$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumTwoSquares.html#Nat.eq_sq_add_sq_iff_eq_sq_mul).
  In particular, [if $-1$ is a square modulo $n$, then $n$ is a sum of two squares](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumTwoSquares.html#Nat.eq_sq_add_sq_of_isSquare_mod_neg_one).
  Conversely, [if $n = x^2 + y^2$ with $x$ and $y$ coprime natural numbers, then $-1$ is a square modulo $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumTwoSquares.html#ZMod.isSquare_neg_one_of_eq_sq_add_sq_of_coprime).
- **Residues modulo a prime.** The corresponding question for residues has no
  obstruction: [for a prime $p$, every residue class modulo $p$ is a sum of two squares of residue classes](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Basic.html#ZMod.sq_add_sq).

## Related concepts

- [Sum of four squares](sum-of-four-squares.md): with four squares there is no
  restriction, since [every natural number is a sum of four squares of natural numbers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumFourSquares.html#Nat.sum_four_squares).
- [Quadratic reciprocity](quadratic-reciprocity.md): the criterion
  in Step 1 for $-1$ to be a square modulo $p$ is the first supplementary law of
  quadratic reciprocity.
- [Pythagorean triples](../../../hundred-theorems/part-01/formula-for-pythagorean-triples.md): the hypotenuse
  of a primitive Pythagorean triple is odd and is a sum of two coprime squares, so
  $-1$ is a square modulo it and hence modulo each of its prime factors $q$. By the
  criterion quoted in Step 1, $q$ is not congruent to $3$ modulo $4$, and since $q$
  is odd, $q \equiv 1 \pmod 4$.

## In Mathlib

Mathlib states the theorem for a natural number $p$ assumed to be prime, with the
single hypothesis that $p$ leaves a remainder other than $3$ on division by $4$;
this covers $p = 2$ and the primes congruent to $1$ modulo $4$ in one statement.
The squares are squares of natural numbers, which loses nothing, since an integer
and its absolute value have the same square. The theorem itself gives only the
existence direction; the impossibility for primes congruent to $3$ modulo $4$
appears in the proof that such primes stay prime in the Gaussian integers and as
a special case of the factorization criterion. The uniqueness of the
representation is not stated in Mathlib. The Gaussian integers are the case
$d = -1$ of Mathlib's rings $\mathbb{Z}[\sqrt{d}]$, made into a Euclidean domain
through the norm. The factorization criterion is stated for every natural number,
including $0$: the number $0$ is $0^2 + 0^2$, it has no prime factors, and its
$q$-adic valuation is defined to be $0$, so both sides hold. Mathlib also uses the
criterion to decide by computation whether a given number is a sum of two squares.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Prime numbers](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)
- [Integer](../numbers/integer.md)
- [Congruence in $\Z$](../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in-z.md)

## Proof depends on

- [Wilson’s Lemma](../../../hundred-theorems/part-02/wilsons-lemma.md)
- [Euclidean domain](../divisibility-in-integral-domains/euclidean-domain.md)
- [Principal ideal domain](../divisibility-in-integral-domains/principal-ideal-domain.md)
- [Irreducible element](../divisibility-in-integral-domains/irreducible-element.md)

## Sources

- [Mathlib documentation: `Nat.Prime.sq_add_sq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/SumTwoSquares.html#Nat.Prime.sq_add_sq)
- [Source of `Nat.Prime.sq_add_sq` in Mathlib/NumberTheory/SumTwoSquares.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/SumTwoSquares.lean#L34)
- [Mathlib overview: General algebra › Number theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L142)
- [Freek Wiedijk's 100 theorems, no. 20](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L99)
- [1000+ theorems list: Q914517](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1070)
- [1000+ theorems project: Q914517](https://1000-plus.github.io/all.html?length=-1#Q914517)
- [Wikipedia: Fermat's theorem on sums of two squares](https://en.wikipedia.org/wiki/Fermat's_theorem_on_sums_of_two_squares)
- [Wikidata: Q914517](https://www.wikidata.org/wiki/Q914517)
