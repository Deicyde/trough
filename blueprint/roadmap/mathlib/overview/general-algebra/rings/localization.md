# Localization

**Localization** is the construction that adjoins inverses to a chosen set of
elements of a commutative [ring](ring.md). Given a multiplicatively closed
subset $S$ of a ring $R$, it produces a ring $S^{-1}R$ of fractions $r/s$ with
$r \in R$ and $s \in S$, in which every element of $S$ becomes invertible, and it
does so in the most economical way. The passage from the integers to the
[rational numbers](../numbers/rational-number.md) is the model case. Localization is one of the basic
tools of commutative algebra and algebraic geometry: it lets one study a ring
"near" a [prime ideal](../ideals-and-quotients/prime-ideal.md) by passing to a [local ring](local-ring.md),
and many properties of rings and modules can be checked one prime at a time.

## Definition

Let $R$ be a commutative ring and $S \subseteq R$ a submonoid of its
multiplicative monoid: $1 \in S$, and $st \in S$ whenever $s, t \in S$. On pairs
$(a, s)$ with $a \in R$ and $s \in S$, declare $(a, s)$ and $(b, t)$ equivalent
when there is some $u \in S$ with

$$u\,t\,a = u\,s\,b.$$

The class of $(a, s)$ is written $a/s$, and the set of classes is the
[localization of $R$ at $S$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/MonoidLocalization/Basic.html#Localization), written $S^{-1}R$. In terms of
the relation Mathlib uses, [two fractions are equal exactly when their pairs are related](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/MonoidLocalization/Basic.html#Localization.mk_eq_mk_iff), and [the pairs $(a, s)$ and $(b, t)$ are related exactly when $u\,t\,a = u\,s\,b$ for some $u \in S$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/MonoidLocalization/Basic.html#Localization.r_iff_exists).
The factor $u$ is needed for the relation to be transitive when $R$ has zero
divisors. If $R$ is an integral domain and $0 \notin S$, it can be cancelled, and
the condition becomes the familiar cross-multiplication rule $ta = sb$.

The operations are those of ordinary fractions:
[$\frac{a}{s} \cdot \frac{b}{t} = \frac{ab}{st}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/MonoidLocalization/Basic.html#Localization.mk_mul) and
[$\frac{a}{s} + \frac{b}{t} = \frac{sb + ta}{st}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Localization/Defs.html#Localization.add_mk).
These make $S^{-1}R$ a commutative ring, and $r \mapsto r/1$ is a
[ring homomorphism](ring-morphism.md) from $R$ to $S^{-1}R$ under which
[the image of every element of $S$ is a unit](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Localization/Defs.html#IsLocalization.map_units).

## Universal property

The localization is characterized by a universal property. Let $g$ be a ring
homomorphism from $R$ to a commutative ring $T$ that sends every element of $S$ to
a unit. Then $g$ factors through $S^{-1}R$:
[there is a ring homomorphism $h$ from $S^{-1}R$ to $T$ with $h(r/1) = g(r)$ for every $r \in R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Localization/Defs.html#IsLocalization.lift_eq), namely $h(a/s) = g(a)\,g(s)^{-1}$, and
[any ring homomorphism from $S^{-1}R$ to $T$ with this property equals $h$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Localization/Defs.html#IsLocalization.lift_unique).

Equivalently, a commutative $R$-[algebra](../algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md) $A$ with structure map $f$ is a
localization of $R$ at $S$ [exactly when three conditions hold](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Localization/Defs.html#isLocalization_iff): $f(s)$ is a unit for each $s \in S$; every element
$z$ of $A$ satisfies $z\,f(s) = f(a)$ for some $a \in R$ and $s \in S$; and
$f(x) = f(y)$ implies $ux = uy$ for some $u \in S$. Any two $R$-algebras with these
properties [are isomorphic as $R$-algebras](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Localization/Basic.html#IsLocalization.algEquiv), so one
may speak of the localization.

## Examples

- **Fractions.** [The rationals are the localization of the integers at the nonzero integers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Localization/FractionRing.html#Rat.isFractionRing). More generally, localizing an integral domain
  at all of its nonzero elements gives its [field of fractions](../field-theory/field-of-fractions-of-an-integral-domain.md),
  which [is a field](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Localization/FractionRing.html#FractionRing.field).
- **Localization at a prime.** For a prime ideal $\mathfrak p$ of $R$, the complement
  $R \setminus \mathfrak p$ is multiplicatively closed, and the
  [localization at it](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Localization/AtPrime/Basic.html#Localization.AtPrime) is written $R_{\mathfrak p}$. For a
  prime number $p$, the ring $\mathbb Z_{(p)}$ consists of the rationals whose
  denominator in lowest terms is prime to $p$.
- **Inverting one element.** For $f \in R$, the
  [localization at the powers of $f$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/MonoidLocalization/Away.html#Localization.Away) is written $R_f$ or
  $R[1/f]$. Inverting $2$ in $\mathbb Z$ gives the dyadic rationals, and inverting
  $x$ in the polynomial ring $k[x]$ over a field gives the Laurent polynomials
  $k[x, x^{-1}]$.
- **Degenerate cases.** If $0 \in S$, the localization
  [is the zero ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Localization/Defs.html#IsLocalization.uniqueOfZeroMem). Less drastically,
  inverting $2$ in $\mathbb Z/6\mathbb Z$ kills $3$, since $2 \cdot 3 = 0$, and the
  result is isomorphic to $\mathbb Z/3\mathbb Z$.

## Properties

- **Kernel.** For $r \in R$,
  [$r/1 = 0$ exactly when $ur = 0$ for some $u \in S$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Localization/Defs.html#IsLocalization.map_eq_zero_iff).
  Hence [the map $R \to S^{-1}R$ is injective exactly when every element of $S$ is cancellable](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Localization/Defs.html#IsLocalization.injective_iff_isRegular), that is, a
  non-zero-divisor.
- **Integral domains.** [Localizing an integral domain at a submonoid of nonzero elements gives an integral domain](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Localization/Defs.html#IsLocalization.isDomain_localization).
- **Prime ideals.** Taking preimages under $r \mapsto r/1$ gives
  [an order-preserving bijection between the prime ideals of $S^{-1}R$ and the prime ideals of $R$ that do not meet $S$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Localization/Ideal.html#IsLocalization.orderIsoOfPrime).
  For $S = R \setminus \mathfrak p$ the primes of $R$ disjoint from $S$ are those
  contained in $\mathfrak p$, so $R_{\mathfrak p}$ has a single [maximal ideal](../ideals-and-quotients/maximal-ideal.md):
  [the localization at a prime ideal is a local ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Localization/AtPrime/Basic.html#Localization.AtPrime.isLocalRing).
- **Finiteness.** [A localization of a Noetherian ring is Noetherian](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Localization/Submodule.html#IsLocalization.isNoetherianRing) (see
  [Noetherian ring](noetherian-ring.md)), since its ideals correspond to certain
  [ideals](../ideals-and-quotients/ideal-of-a-commutative-ring.md) of $R$ in an order-preserving, injective way.
- **Flatness.** [$S^{-1}R$ is a flat $R$-module](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Flat/Localization.html#IsLocalization.flat):
  [tensoring](../../linear-algebra/fundamentals/tensor-product.md) with it preserves injective linear maps. Since
  [the localized module $S^{-1}M$ is isomorphic to $S^{-1}R \otimes_R M$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Localization/BaseChange.html#LocalizedModule.equivTensorProduct), this is
  equivalent to the statement that localizing modules preserves exact sequences.

## Related concepts

Where a [quotient ring](../ideals-and-quotients/quotient-ring.md) forces elements to become
zero, a localization forces them to become invertible, and the two operations
are often combined. The same fractions construction applied to a
[module](../../linear-algebra/fundamentals/module.md) $M$ over $R$ gives the
[localized module](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Module/LocalizedModule/Basic.html#LocalizedModule) $S^{-1}M$. Applied
to a commutative monoid it gives the monoid of fractions; localizing the additive
monoid of natural numbers at all of its elements gives the additive group of
integers, an instance of the Grothendieck group construction. For noncommutative
rings, fractions can be formed at submonoids that satisfy the Ore condition
together with a cancellation condition, the [Ore sets](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/OreLocalization/OreSet.html#OreLocalization.OreSet).
In algebraic geometry the rings $R_f$ are the rings of sections of the structure
sheaf over the basic open subsets of the [spectrum](../../geometry/algebraic-geometry/prime-spectrum.md) of $R$, which makes localization a basic ingredient in
the definition of a [scheme](../../geometry/algebraic-geometry/scheme.md).

## In Mathlib

Mathlib builds the localization in more generality than the ring version. The
basic construction is the localization of a commutative monoid at a submonoid.
Mathlib defines it as an instance of its more general Ore localization, a
quotient of the set of pairs, and when the monoid is the multiplicative monoid of
a commutative ring or semiring it carries the ring structure. Mathlib also
defines a congruence on pairs, the smallest one that identifies $(1, 1)$ with
$(s, s)$ for every $s \in S$, proves that two fractions are equal exactly when
their pairs are related by it, and proves the explicit description with the
factor $u$ as a lemma. Because
reasoning up to isomorphism is awkward in a formal system, most results are stated
not for this particular quotient but for any algebra that satisfies a
characteristic predicate expressing the three conditions above; the quotient
construction, the localization at a prime, the localization away from an element
and the fraction ring are all instances. The fraction ring is defined for every
commutative ring as the localization at its non-zero-divisors, and is a field when
the ring is an integral domain.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Ring](ring.md)
- [Ring morphism](ring-morphism.md)

## Sources

- [Mathlib documentation: `Localization`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/MonoidLocalization/Basic.html#Localization)
- [Source of `Localization` in Mathlib/GroupTheory/MonoidLocalization/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/MonoidLocalization/Basic.lean#L207)
- [Mathlib overview: General algebra › Rings](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L69)
