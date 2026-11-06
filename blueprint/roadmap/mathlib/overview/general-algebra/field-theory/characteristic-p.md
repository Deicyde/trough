---
article_id: af_51ae08814d5821a27e42384a
declaration: class
origin: cited
mathlib: true
mathlib_declaration: CharP
mathlib_file: Mathlib/Algebra/CharP/Defs.lean
---

# Characteristic p

A [ring](../rings/ring.md) $R$ has **characteristic $p$** when adding the identity element $1$ to itself $n$ times gives $0$ exactly for the multiples $n$ of $p$. The characteristic measures how the [integers](../numbers/integer.md) sit inside a ring: in characteristic $0$ they embed faithfully, while in a positive characteristic $p$ the ring arithmetic of whole numbers wraps around modulo $p$. Commutative rings and [fields](field.md) of prime characteristic have an algebra of their own, governed by the identity $(x + y)^p = x^p + y^p$, and they appear throughout number theory, algebraic geometry and coding theory.

## Definition

For a [natural number](../numbers/natural-number.md) $n$, write $n \cdot 1$ for the sum $1 + 1 + \dots + 1$ with $n$ terms in a ring $R$. A natural number $p$ is the characteristic of $R$ if, for every natural number $n$,
[$n \cdot 1 = 0$ in $R$ if and only if $p$ divides $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Defs.html#CharP.cast_eq_zero_iff); this condition is [the definition of characteristic $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Defs.html#CharP).

[Every ring has exactly one characteristic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Defs.html#CharP.existsUnique). If some positive $n$ satisfies $n \cdot 1 = 0$, the characteristic is the least such $n$; otherwise it is $0$, and the ring has [characteristic zero](characteristic-zero.md). Equivalently, the characteristic is the nonnegative generator of the kernel of the unique [ring homomorphism](../rings/ring-morphism.md) from the integers to $R$: [an integer $m$ maps to $0$ if and only if $p$ divides $m$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Defs.html#CharP.intCast_eq_zero_iff). It is also [the additive order of $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/OrderOfElement.html#CharP.addOrderOf_one), with the convention that an element of infinite additive order has order $0$. The number itself, as a function of the ring, is the subject of the article on the [characteristic of a ring](characteristic-of-a-ring.md).

Many authors reserve the phrase "characteristic $p$" for a prime $p$. For a prime $p$ and a ring with $1 \neq 0$, the condition simplifies: [$R$ has characteristic $p$ if and only if $p \cdot 1 = 0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Basic.html#CharP.charP_iff_prime_eq_zero).

## Examples

- For every $n$, [the ring $\mathbb{Z}/n\mathbb{Z}$ of integers modulo $n$ has characteristic $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/ZMod/Basic.html#ZMod.charP). In particular the field $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$ has characteristic $p$ for each prime $p$.
- The integers, the [rational numbers](../numbers/rational-number.md), the [real numbers](../numbers/real-number.md) and the [complex numbers](../numbers/complex-number.md) have characteristic $0$.
- [A ring has characteristic $1$ exactly when it is the zero ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Defs.html#ringChar.ringChar_eq_one), the ring in which $1 = 0$.
- [The polynomial ring $R[X]$ has the same characteristic as $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Coeff.html#Polynomial.charP) (see [polynomial](../polynomials-and-power-series/polynomial-in-one-indeterminate.md)). So $\mathbb{F}_p[X]$ is an infinite ring of characteristic $p$, and so is its field of rational functions, which contains it (see Homomorphisms below): positive characteristic does not force finiteness.
- [If $R$ has characteristic $p$ and $S$ has characteristic $q$, then $R \times S$ has characteristic $\operatorname{lcm}(p, q)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Basic.html#Nat.lcm.charP). For example $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$ has characteristic $6$.

## Properties

**Reduction modulo $p$.** In a ring of characteristic $p$, [$k \cdot 1 = (k \bmod p) \cdot 1$ for every natural number $k$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Defs.html#CharP.cast_eq_mod), so the image of the natural numbers is a copy of $\mathbb{Z}/p\mathbb{Z}$ (or of the natural numbers themselves when $p = 0$).

**Domains and fields.** [The characteristic of a nonzero ring without zero divisors is either $0$ or a prime number](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Defs.html#CharP.char_is_prime_or_zero). This covers every integral domain and every field. The reason is short: if the characteristic were $p = ab$ with $1 < a, b < p$, then $(a \cdot 1)(b \cdot 1) = p \cdot 1 = 0$, so one factor would vanish, contradicting the minimality of $p$. The value $1$ is excluded because the ring is nonzero.

**Finite rings.** The natural numbers cannot inject into a finite set, so [every finite ring has positive characteristic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Lemmas.html#CharP.char_ne_zero_of_finite). Combined with the previous fact, [a finite nonzero ring without zero divisors has prime characteristic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Lemmas.html#CharP.char_is_prime). So the characteristic $p$ of a finite field is prime, the field is a vector space over $\mathbb{F}_p$ of some finite dimension $n \ge 1$, and [$p$ is prime and the field has $p^n$ elements for some positive integer $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Basic.html#FiniteField.card) (see [finite fields](../../../undergraduate/ring-theory/field-theory/finite-fields.md)).

**Homomorphisms.** [If $f \colon R \to A$ is an injective ring homomorphism and $R$ has characteristic $p$, then $A$ has characteristic $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Algebra.html#charP_of_injective_ringHom). Thus a [subring](../rings/subring.md) shares the characteristic of the ambient ring, and a field extension shares the characteristic of the base field.

**The binomial identity.** Let $R$ be a commutative ring of prime characteristic $p$. For $0 < k < p$ the binomial coefficient $\binom{p}{k}$ is divisible by $p$, so every middle term of the [binomial theorem](../../../hundred-theorems/part-02/the-binomial-theorem.md) vanishes and
[$(x + y)^p = x^p + y^p$ for all $x, y$ in $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Lemmas.html#add_pow_char). Likewise [$(x - y)^p = x^p - y^p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Lemmas.html#sub_pow_char), and by induction [$(x + y)^{p^n} = x^{p^n} + y^{p^n}$ for every natural number $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Lemmas.html#add_pow_char_pow). Since $(xy)^p = x^p y^p$ and $1^p = 1$ as well, the map $x \mapsto x^p$ is a ring homomorphism from $R$ to itself, the [Frobenius morphism](frobenius-morphism.md).

## Related concepts

The [characteristic of a ring](characteristic-of-a-ring.md) is the number $p$ viewed as a function of $R$. Rings of [characteristic zero](characteristic-zero.md) are those in which the natural numbers embed. The Frobenius morphism leads to the notion of a perfect field (in prime characteristic, a field on which the Frobenius morphism is surjective) and to the [perfect closure](perfect-closure.md) of a field of prime characteristic. Over a field of characteristic $p$ that is not perfect, an irreducible polynomial can fail to be [separable](../polynomials-and-power-series/separable-polynomial.md), as $X^p - t$ does over the field of rational functions $\mathbb{F}_p(t)$; in characteristic zero this cannot happen.

## In Mathlib

Mathlib states "$R$ has characteristic $p$" as a property of the pair $(R, p)$ rather than as a function of $R$, and it does so for any additive structure with a $1$, not only rings; the ring structure enters only in the theorems that need it. The number $p$ is any natural number, so characteristic zero is the case $p = 0$, and primality is a separate hypothesis wherever a theorem needs it. For rings, characteristic $0$ in this sense agrees with the requirement that the map from the natural numbers be injective: [a ring has characteristic $0$ in this sense if and only if the natural numbers inject into it](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Defs.html#CharP.charP_zero_iff_charZero). For semirings without negation the two can differ. Mathlib defines the Frobenius map more generally, for the exponential characteristic, which is $p$ in prime characteristic $p$ and $1$ in characteristic zero.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Ring](../rings/ring.md)
- [Natural number](../numbers/natural-number.md)
- [Integer](../numbers/integer.md)

## Sources

- [Mathlib documentation: `CharP`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Defs.html#CharP)
- [Source of `CharP` in Mathlib/Algebra/CharP/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/CharP/Defs.lean#L36)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L124)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L174)
