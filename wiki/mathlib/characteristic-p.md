A [ring](trough:Ring) $R$ has **characteristic $p$** when adding the identity element $1$ to itself $n$ times gives $0$ exactly for the multiples $n$ of $p$. The characteristic measures how the [integers](trough:Int) sit inside a ring: in characteristic $0$ they embed faithfully, while in a positive characteristic $p$ the ring arithmetic of whole numbers wraps around modulo $p$. Commutative rings and [fields](trough:Field) of prime characteristic have an algebra of their own, governed by the identity $(x + y)^p = x^p + y^p$, and they appear throughout number theory, algebraic geometry and coding theory.

## Definition

For a [natural number](trough:Nat) $n$, write $n \cdot 1$ for the sum $1 + 1 + \dots + 1$ with $n$ terms in a ring $R$. A natural number $p$ is the characteristic of $R$ if, for every natural number $n$,
$n \cdot 1 = 0$ in $R$ if and only if $p$ divides $n$; this condition is the definition of characteristic $p$.

Every ring has exactly one characteristic. If some positive $n$ satisfies $n \cdot 1 = 0$, the characteristic is the least such $n$; otherwise it is $0$, and the ring has [characteristic zero](trough:CharZero). Equivalently, the characteristic is the nonnegative generator of the kernel of the unique [ring homomorphism](trough:RingHom) from the integers to $R$: an integer $m$ maps to $0$ if and only if $p$ divides $m$. It is also the additive order of $1$, with the convention that an element of infinite additive order has order $0$. The number itself, as a function of the ring, is the subject of the article on the [characteristic of a ring](trough:ringChar).

Many authors reserve the phrase "characteristic $p$" for a prime $p$. For a prime $p$ and a ring with $1 \neq 0$, the condition simplifies: $R$ has characteristic $p$ if and only if $p \cdot 1 = 0$.

## Examples

- For every $n$, the ring $\mathbb{Z}/n\mathbb{Z}$ of integers modulo $n$ has characteristic $n$. In particular the field $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$ has characteristic $p$ for each prime $p$.
- The integers, the [rational numbers](trough:Rat), the [real numbers](trough:Real) and the [complex numbers](trough:Complex) have characteristic $0$.
- A ring has characteristic $1$ exactly when it is the zero ring, the ring in which $1 = 0$.
- The polynomial ring $R[X]$ has the same characteristic as $R$ (see [polynomial](trough:Polynomial)). So $\mathbb{F}_p[X]$ is an infinite ring of characteristic $p$, and so is its field of rational functions, which contains it (see Homomorphisms below): positive characteristic does not force finiteness.
- If $R$ has characteristic $p$ and $S$ has characteristic $q$, then $R \times S$ has characteristic $\operatorname{lcm}(p, q)$. For example $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$ has characteristic $6$.

## Properties

**Reduction modulo $p$.** In a ring of characteristic $p$, $k \cdot 1 = (k \bmod p) \cdot 1$ for every natural number $k$, so the image of the natural numbers is a copy of $\mathbb{Z}/p\mathbb{Z}$ (or of the natural numbers themselves when $p = 0$).

**Domains and fields.** The characteristic of a nonzero ring without zero divisors is either $0$ or a prime number. This covers every integral domain and every field. The reason is short: if the characteristic were $p = ab$ with $1 < a, b < p$, then $(a \cdot 1)(b \cdot 1) = p \cdot 1 = 0$, so one factor would vanish, contradicting the minimality of $p$. The value $1$ is excluded because the ring is nonzero.

**Finite rings.** The natural numbers cannot inject into a finite set, so every finite ring has positive characteristic. Combined with the previous fact, a finite nonzero ring without zero divisors has prime characteristic. So the characteristic $p$ of a finite field is prime, the field is a vector space over $\mathbb{F}_p$ of some finite dimension $n \ge 1$, and $p$ is prime and the field has $p^n$ elements for some positive integer $n$ (see [finite fields](trough:Mathlib.FieldTheory.Finite.Basic)).

**Homomorphisms.** If $f \colon R \to A$ is an injective ring homomorphism and $R$ has characteristic $p$, then $A$ has characteristic $p$. Thus a [subring](trough:Subring) shares the characteristic of the ambient ring, and a field extension shares the characteristic of the base field.

**The binomial identity.** Let $R$ be a commutative ring of prime characteristic $p$. For $0 < k < p$ the binomial coefficient $\binom{p}{k}$ is divisible by $p$, so every middle term of the [binomial theorem](trough:add_pow) vanishes and
$(x + y)^p = x^p + y^p$ for all $x, y$ in $R$. Likewise $(x - y)^p = x^p - y^p$, and by induction $(x + y)^{p^n} = x^{p^n} + y^{p^n}$ for every natural number $n$. Since $(xy)^p = x^p y^p$ and $1^p = 1$ as well, the map $x \mapsto x^p$ is a ring homomorphism from $R$ to itself, the [Frobenius morphism](trough:frobenius).

## Related concepts

The [characteristic of a ring](trough:ringChar) is the number $p$ viewed as a function of $R$. Rings of [characteristic zero](trough:CharZero) are those in which the natural numbers embed. The Frobenius morphism leads to the notion of a perfect field (in prime characteristic, a field on which the Frobenius morphism is surjective) and to the [perfect closure](trough:PerfectClosure) of a field of prime characteristic. Over a field of characteristic $p$ that is not perfect, an irreducible polynomial can fail to be [separable](trough:Polynomial.Separable), as $X^p - t$ does over the field of rational functions $\mathbb{F}_p(t)$; in characteristic zero this cannot happen.

## In Mathlib

Mathlib states "$R$ has characteristic $p$" as a property of the pair $(R, p)$ rather than as a function of $R$, and it does so for any additive structure with a $1$, not only rings; the ring structure enters only in the theorems that need it. The number $p$ is any natural number, so characteristic zero is the case $p = 0$, and primality is a separate hypothesis wherever a theorem needs it. For rings, characteristic $0$ in this sense agrees with the requirement that the map from the natural numbers be injective: a ring has characteristic $0$ in this sense if and only if the natural numbers inject into it. For semirings without negation the two can differ. Mathlib defines the Frobenius map more generally, for the exponential characteristic, which is $p$ in prime characteristic $p$ and $1$ in characteristic zero.

## Depends on

- [Ring](trough:Ring)
- [Natural number](trough:Nat)
- [Integer](trough:Int)
