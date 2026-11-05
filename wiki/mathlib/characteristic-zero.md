---
article_id: af_a4a3125832e544c81e987af6
concept: CharZero
---

A [ring](trough:Ring) has **characteristic zero** when no positive multiple of its identity element vanishes: $1 + 1 + \cdots + 1 \neq 0$ however many terms are added. The rational, real and complex numbers all have this property, while the integers modulo $n$ for $n \geq 1$ and every [finite field](trough:Mathlib.FieldTheory.Finite.Basic) do not. Characteristic zero is the setting in which the familiar arithmetic of the integers and the rationals survives inside a ring, so that distinct integers remain distinct in the ring and, in a field, one may divide by nonzero integers. It is one of the two cases in the classification of fields by their [characteristic](trough:ringChar), the other being [characteristic $p$](trough:CharP) for a prime $p$.

## Definition

For a ring $R$ and a [natural number](trough:Nat) $n$, write $n \cdot 1$ for the sum of $n$ copies of the identity $1$ of $R$. The ring $R$ has characteristic zero if [the map $n \mapsto n \cdot 1$ from the natural numbers to $R$ is injective](lean:CharZero). In a ring this is the same as asking that $n \cdot 1 \neq 0$ for every $n \geq 1$: injectivity gives [$n \cdot 1 = 0$ exactly when $n = 0$](lean:Nat.cast_eq_zero), and conversely, since $m \cdot 1 = n \cdot 1$ with $m \le n$ forces $(n - m) \cdot 1 = 0$ after subtracting, [the condition $n \cdot 1 \neq 0$ for all $n \geq 1$ implies injectivity](lean:charZero_of_inj_zero).

The characteristic of a ring is the least $n \geq 1$ with $n \cdot 1 = 0$, or $0$ if there is no such $n$. Thus [a ring has characteristic zero exactly when its characteristic is $0$](lean:CharP.ringChar_zero_iff_CharZero).

## Examples

- The [integers](trough:Int), the [rational numbers](trough:Rat), the [real numbers](trough:Real) and the [complex numbers](trough:Complex) have characteristic zero; for instance [$\mathbb{Z}$ does](lean:Int.instCharZero), [$\mathbb{Q}$ does](lean:Rat.instCharZero) and [$\mathbb{C}$ does](lean:Complex.instCharZero).
- Every nontrivial [ordered ring](trough:IsOrderedRing) [has characteristic zero](lean:IsOrderedRing.toCharZero), since $0 < 1 < 1 + 1 < \cdots$ is a strictly increasing sequence. This covers $\mathbb{R}$ and all its subrings.
- If $R$ has characteristic zero, [so does the polynomial ring $R[X]$](lean:Polynomial.charZero) (see [polynomial](trough:Polynomial)).
- If $R$ has characteristic zero, [so does the product $R \times S$ for any ring $S$](lean:Prod.charZero_of_left). For example $\mathbb{Q} \times \mathbb{Z}/2\mathbb{Z}$ has characteristic zero although it contains a nonzero element $a$ with $a + a = 0$.
- The ring $\mathbb{Z}/n\mathbb{Z}$ with $n \geq 1$ does not have characteristic zero, since $n \cdot 1 = 0$ there. More generally, [a ring of characteristic zero is infinite](lean:CharZero.infinite), because the elements $n \cdot 1$ are pairwise distinct, so no finite ring has characteristic zero. The converse fails: the polynomial ring over $\mathbb{Z}/p\mathbb{Z}$ is infinite and has characteristic $p$.

## Properties

- **Transfer along homomorphisms.** A [ring homomorphism](trough:RingHom) sends $n \cdot 1$ to $n \cdot 1$. Hence, [if some ring homomorphism maps $R$ into a ring of characteristic zero, then $R$ has characteristic zero](lean:RingHom.charZero), and [a ring containing a copy of a characteristic zero ring, via an injective homomorphism, has characteristic zero](lean:charZero_of_injective_ringHom). In particular every [subring](trough:Subring) of $\mathbb{C}$ has characteristic zero.
- **The integers inside $R$.** In a ring of characteristic zero, [the map $k \mapsto k \cdot 1$ from $\mathbb{Z}$ to $R$ is injective](lean:Int.cast_injective), so $R$ contains a copy of $\mathbb{Z}$.
- **The rationals inside a field.** In a [field](trough:Field), or more generally a division ring, of characteristic zero, every nonzero integer has an inverse, and [the resulting map from $\mathbb{Q}$ is injective](lean:Rat.cast_injective). For a field $K$ of characteristic zero, [the smallest subfield of $K$ is the image of $\mathbb{Q}$](lean:Subfield.bot_eq_of_charZero), and [$K$ is an algebra over $\mathbb{Q}$](lean:DivisionRing.toRatAlgebra) (see [associative algebra](trough:Algebra)). Conversely, [every nontrivial ring that is an algebra over $\mathbb{Q}$ has characteristic zero](lean:algebraRat.charZero).
- **Domains.** The [characteristic of a nontrivial ring without zero divisors is either zero or a prime](lean:CharP.char_is_prime_or_zero). So a field has characteristic zero exactly when its characteristic is not a prime.
- **No elements of order two.** In a ring without zero divisors and of characteristic zero, [$a + a = 0$ holds exactly when $a = 0$](lean:add_self_eq_zero), since $a + a = 2a$ and $2 \neq 0$. In characteristic $2$, by contrast, $a + a = 0$ for every $a$.
- **Separability.** Over a field of characteristic zero the [derivative](trough:Polynomial.derivative) of a polynomial of degree $d \geq 1$ has degree $d - 1$, so it is not zero, and it follows that [every irreducible polynomial is separable](lean:Irreducible.separable) (see [separable polynomial](trough:Polynomial.Separable)). Consequently [every field of characteristic zero is perfect](lean:PerfectField.ofCharZero), and every algebraic extension of such a field is separable. Over the field $\mathbb{F}_p(t)$ of rational functions in $t$ over $\mathbb{Z}/p\mathbb{Z}$, the polynomial $X^p - t$ is irreducible yet has zero derivative, which is why the two cases are treated separately in Galois theory.

## Related concepts

- [Characteristic of a ring](trough:ringChar): the natural number attached to every ring, which is $0$ exactly in the present case.
- [Characteristic $p$](trough:CharP): the condition that $n \cdot 1 = 0$ exactly when $p$ divides $n$. For rings, [having characteristic zero is the same as having characteristic $p$ with $p = 0$](lean:CharP.charP_zero_iff_charZero).
- Mixed characteristic: a commutative ring of characteristic zero is said to have [mixed characteristic $(0, p)$](lean:MixedCharZero) when it has a proper ideal whose [quotient](trough:Ideal.Quotient.ring) has characteristic $p$; the integers and the $p$-adic integers are examples.

## In Mathlib

Mathlib defines characteristic zero as a property of any additive monoid with a distinguished element $1$, not only of rings, and takes injectivity of the map from the natural numbers as the definition. For rings, and more generally whenever subtraction is available, this agrees with the condition that $n \cdot 1 \neq 0$ for $n \geq 1$, but without subtraction the two can differ. Take the two-element set $\{0, 1\}$, with the maximum as addition and the minimum as multiplication. Every positive multiple of $1$ equals $1$, so $0$ is the only natural number sent to $0$, but distinct positive numbers have the same image; this semiring has characteristic $0$ in the sense of the characteristic-$p$ condition without having characteristic zero in Mathlib's sense. Characteristic zero is recorded as a class that the library finds automatically, so the facts above about $\mathbb{Q}$-algebras, separability and perfection apply to a field as soon as its characteristic is known to be zero. The integers modulo $0$ are the integers themselves, and [they have characteristic zero](lean:ZMod.charZero).

## Depends on

- [Ring](trough:Ring)
- [Natural number](trough:Nat)
