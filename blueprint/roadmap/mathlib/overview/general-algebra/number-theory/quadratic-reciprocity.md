# Quadratic reciprocity

**Quadratic reciprocity** is a theorem of elementary number theory relating two
questions that look unrelated: whether an odd [prime](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md) $q$ is a square modulo a
different odd prime $p$, and whether $p$ is a square modulo $q$. It says the two answers
agree unless both primes are congruent to $3$ modulo $4$, in which case they are
opposite. Together with two supplementary laws it gives an efficient way,
especially in its Jacobi-symbol form, to decide
whether an equation $x^2 \equiv a \pmod p$ has a solution, and it is the simplest
case of the reciprocity laws of algebraic number theory.

## Statement

Let $p$ be a prime and $a$ an [integer](../numbers/integer.md). The
[Legendre symbol](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LegendreSymbol/Basic.html#legendreSym) $\left(\frac{a}{p}\right)$ is $0$ if $p$
divides $a$, $1$ if $a$ is congruent modulo $p$ to the square of an integer not
divisible by $p$, and $-1$ otherwise. In the last two cases $a$ is called a
quadratic residue or a quadratic nonresidue modulo $p$. For fixed $p$ the symbol
is [multiplicative in $a$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LegendreSymbol/Basic.html#legendreSym.mul).

The law of quadratic reciprocity: if $p$ and $q$ are distinct odd primes, then
[$\left(\frac{p}{q}\right)\left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2}\cdot\frac{q-1}{2}}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.html#legendreSym.quadratic_reciprocity).
The exponent is even unless $p \equiv q \equiv 3 \pmod 4$. Equivalently, for odd
primes $p$ and $q$,
[$\left(\frac{q}{p}\right) = (-1)^{\frac{p-1}{2}\cdot\frac{q-1}{2}}\left(\frac{p}{q}\right)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.html#legendreSym.quadratic_reciprocity'),
a form that also holds trivially when $p = q$, since both sides are $0$. Stated
without symbols: if $p \equiv 1 \pmod 4$ and $q$ is an odd prime, then
[$q$ is a square modulo $p$ if and only if $p$ is a square modulo $q$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.html#ZMod.exists_sq_eq_prime_iff_of_mod_four_eq_one);
if $p$ and $q$ are distinct primes both congruent to $3$ modulo $4$, then
[$q$ is a square modulo $p$ if and only if $p$ is not a square modulo $q$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.html#ZMod.exists_sq_eq_prime_iff_of_mod_four_eq_three).

The supplementary laws treat $-1$ and $2$:
[$-1$ is a square modulo a prime $p$ exactly when $p$ is not congruent to $3$ modulo $4$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LegendreSymbol/Basic.html#ZMod.exists_sq_eq_neg_one_iff),
and for an odd prime $p$,
[$2$ is a square modulo $p$ exactly when $p \equiv 1$ or $p \equiv 7 \pmod 8$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.html#ZMod.exists_sq_eq_two_iff).

## Examples

- Since $5 \equiv 1 \pmod 4$, $\left(\frac{3}{5}\right) = \left(\frac{5}{3}\right) = \left(\frac{2}{3}\right) = -1$:
  the nonzero squares modulo $5$ are $1$ and $4$, and $3$ is not among them.
- Both $3$ and $7$ are congruent to $3$ modulo $4$, so
  $\left(\frac{3}{7}\right) = -\left(\frac{7}{3}\right) = -\left(\frac{1}{3}\right) = -1$.
  Indeed the nonzero squares modulo $7$ are $1$, $2$ and $4$.
- To decide whether $37$ is a square modulo the prime $101$, flip and reduce
  repeatedly, using multiplicativity and $37 \equiv 1 \pmod 4$:
  $$\left(\frac{37}{101}\right) = \left(\frac{101}{37}\right) = \left(\frac{27}{37}\right) = \left(\frac{3}{37}\right)^3 = \left(\frac{37}{3}\right)^3 = \left(\frac{1}{3}\right)^3 = 1.$$
  So $x^2 \equiv 37 \pmod{101}$ has a solution; one is $x = 21$, since $21^2 = 441 = 4 \cdot 101 + 37$.
- For a prime $p > 3$, reciprocity gives $\left(\frac{3}{p}\right) = (-1)^{\frac{p-1}{2}}\left(\frac{p}{3}\right)$,
  and checking the residues of $p$ modulo $12$ shows that $3$ is a square modulo
  $p$ if and only if $p \equiv \pm 1 \pmod{12}$.

## Consequences

The law turns a question about $p$ modulo $q$ into a question about $q$ modulo
$p$, and the second number can be reduced modulo $p$. Alternating flips and
reductions, after factoring out powers of $2$ and signs with the supplementary
laws, computes any Legendre symbol, although each step may require factoring a
number; the Jacobi symbol described below removes that need. The law also shows that for a fixed odd prime $q$ the value
$\left(\frac{q}{p}\right)$, as $p$ ranges over the odd primes other than $q$,
depends only on $p$ modulo $4q$, so the primes modulo which $q$ is a square are
described by [congruence](../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in-z.md) conditions. The first supplementary law is the starting
point of several proofs of the theorem that a prime $p \equiv 1 \pmod 4$ is a
[sum of two squares](sum-of-two-squares.md).

## Proof

A short proof goes through Gauss's lemma and a refinement of it known as
Eisenstein's lemma. Let
$p$ be an odd prime. For an odd natural number $a$ not divisible by $p$,
[Eisenstein's lemma](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LegendreSymbol/GaussEisensteinLemmas.html#ZMod.eisenstein_lemma) gives

$$\left(\frac{a}{p}\right) = (-1)^{S(a,p)}, \qquad S(a,p) = \sum_{x=1}^{(p-1)/2} \left\lfloor \frac{xa}{p} \right\rfloor .$$

It follows from [Gauss's lemma](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LegendreSymbol/GaussEisensteinLemmas.html#ZMod.gauss_lemma), which expresses
$\left(\frac{a}{p}\right)$ as $(-1)^{\mu}$, where $\mu$ counts the $x$ among
$1, \dots, \frac{p-1}{2}$ for which the remainder of $ax$ on division by $p$
exceeds $p/2$. Gauss's lemma in turn compares the product of the numbers $ax$
with $\left(\frac{p-1}{2}\right)!$ and uses Euler's criterion,
[$\left(\frac{a}{p}\right) \equiv a^{(p-1)/2} \pmod p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LegendreSymbol/Basic.html#legendreSym.eq_pow),
which is proved from [Fermat's little theorem](../../../thousand-plus/number-theory/part-01/fermats-little-theorem.md)
and the fact that a polynomial of degree $d$ has at most $d$ roots modulo $p$.

Now let $p$ and $q$ be distinct odd primes. The sum $S(q,p)$ counts the lattice
points $(x, y)$ with $1 \le x \le \frac{p-1}{2}$ and $1 \le y \le \frac{q-1}{2}$
lying below the line $py = qx$, and $S(p,q)$ counts those above it. No lattice
point of the rectangle lies on the line, since $qx = py$ would force $p$ to divide $x$. Hence
[$S(q,p) + S(p,q) = \frac{p-1}{2}\cdot\frac{q-1}{2}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LegendreSymbol/GaussEisensteinLemmas.html#ZMod.sum_mul_div_add_sum_mul_div_eq_mul),
and multiplying the two instances of Eisenstein's lemma proves the theorem.

A second proof works in a [field](../field-theory/field.md) of [characteristic](../field-theory/characteristic-of-a-ring.md) $q$ containing a primitive
$p$-th root of unity $\zeta$. The Gauss sum
$g = \sum_{a=1}^{p-1} \left(\frac{a}{p}\right)\zeta^a$ satisfies
$g^2 = (-1)^{\frac{p-1}{2}} p$, while raising to the $q$-th power, the
[Frobenius map](../field-theory/frobenius-morphism.md), which is additive in characteristic $q$, gives
$g^q = \left(\frac{q}{p}\right) g$; here one uses that
$\left(\frac{a}{p}\right)^q = \left(\frac{a}{p}\right)$ because $q$ is odd.
Since $g^2 = \pm p$ is nonzero in characteristic $q \ne p$, $g$ is invertible,
so $g^{q-1} = \left(\frac{q}{p}\right)$. Comparing this with Euler's criterion
for $(-1)^{\frac{p-1}{2}} p$ modulo $q$, using the first supplementary law for
$q$ and the fact that $1 \ne -1$ in characteristic $q$, yields the law.

## Generalizations

The Jacobi symbol extends the Legendre symbol to an odd positive modulus $b$ by
multiplying the Legendre symbols over the prime factors of $b$, counted with
multiplicity. Reciprocity carries over: for odd natural numbers $a$ and $b$,
[the Jacobi symbols satisfy $\left(\frac{a}{b}\right) = (-1)^{\frac{a-1}{2}\cdot\frac{b-1}{2}}\left(\frac{b}{a}\right)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LegendreSymbol/JacobiSymbol.html#jacobiSym.quadratic_reciprocity).
This allows symbols to be computed without factoring. Further generalizations
include cubic and biquadratic reciprocity, the Hilbert reciprocity law for
Hilbert symbols over the rationals, and the Artin reciprocity law of class field theory.

## In Mathlib

Mathlib writes the prime first, so the symbol $\left(\frac{a}{p}\right)$ is a
function of $a$ for each fixed $p$, and it defines this function as the
quadratic character of the field of integers modulo $p$. The exponent in the law
is written with natural-number division rounding down, as the product of
$\lfloor p/2 \rfloor$ and $\lfloor q/2 \rfloor$; for odd primes this equals
$\frac{p-1}{2}\cdot\frac{q-1}{2}$. The proof does not use lattice points. It
derives the law from a statement about arbitrary finite fields: for two finite
fields $F$ and $F'$ of distinct odd characteristics,
[the quadratic character of $F$ at the number of elements of $F'$ equals the quadratic character of $F'$ at $\chi_F(-1)$ times the number of elements of $F$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LegendreSymbol/QuadraticChar/GaussSum.html#quadraticChar_card_card),
where $\chi_F$ is the quadratic character of $F$; this rests on quadratic Gauss
sums. Gauss's and Eisenstein's lemmas are proved separately. The Jacobi symbol is
defined for every natural number modulus, taking value $1$ at modulus $0$, and
its reciprocity law needs no coprimality hypothesis, since both sides vanish when
$a$ and $b$ share a factor.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Prime numbers](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)
- [Congruence in $\Z$](../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in-z.md)

## Proof depends on

- [Fermat's little theorem](../../../thousand-plus/number-theory/part-01/fermats-little-theorem.md)
- [Field](../field-theory/field.md)
- [Characteristic of a ring](../field-theory/characteristic-of-a-ring.md)
- [Frobenius morphism](../field-theory/frobenius-morphism.md)

## Sources

- [Mathlib documentation: `legendreSym.quadratic_reciprocity`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.html#legendreSym.quadratic_reciprocity)
- [Source of `legendreSym.quadratic_reciprocity` in Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.lean#L105)
- [Mathlib overview: General algebra › Number theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L144)
- [Freek Wiedijk's 100 theorems, no. 7](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L38)
- [1000+ theorems list: Q472883](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L476)
- [1000+ theorems project: Q472883](https://1000-plus.github.io/all.html?length=-1#Q472883)
- [Wikipedia: Quadratic reciprocity theorem](https://en.wikipedia.org/wiki/Quadratic_reciprocity_theorem)
- [Wikidata: Q472883](https://www.wikidata.org/wiki/Q472883)
