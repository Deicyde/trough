**Localization** is the construction that adjoins inverses to a chosen set of
elements of a commutative [ring](trough:Ring). Given a multiplicatively closed
subset $S$ of a ring $R$, it produces a ring $S^{-1}R$ of fractions $r/s$ with
$r \in R$ and $s \in S$, in which every element of $S$ becomes invertible, and it
does so in the most economical way. The passage from the integers to the
[rational numbers](trough:Rat) is the model case. Localization is one of the basic
tools of commutative algebra and algebraic geometry: it lets one study a ring
"near" a [prime ideal](trough:Ideal.IsPrime) by passing to a [local ring](trough:IsLocalRing),
and many properties of rings and modules can be checked one prime at a time.

## Definition

Let $R$ be a commutative ring and $S \subseteq R$ a submonoid of its
multiplicative monoid: $1 \in S$, and $st \in S$ whenever $s, t \in S$. On pairs
$(a, s)$ with $a \in R$ and $s \in S$, declare $(a, s)$ and $(b, t)$ equivalent
when there is some $u \in S$ with

$$u\,t\,a = u\,s\,b.$$

The class of $(a, s)$ is written $a/s$, and the set of classes is the
localization of $R$ at $S$, written $S^{-1}R$. In terms of
the relation Mathlib uses, two fractions are equal exactly when their pairs are
related, and the pairs $(a, s)$ and $(b, t)$ are
related exactly when $u\,t\,a = u\,s\,b$ for some $u \in S$.
The factor $u$ is needed for the relation to be transitive when $R$ has zero
divisors. If $R$ is an integral domain and $0 \notin S$, it can be cancelled, and
the condition becomes the familiar cross-multiplication rule $ta = sb$.

The operations are those of ordinary fractions:
$\frac{a}{s} \cdot \frac{b}{t} = \frac{ab}{st}$ and
$\frac{a}{s} + \frac{b}{t} = \frac{sb + ta}{st}$.
These make $S^{-1}R$ a commutative ring, and $r \mapsto r/1$ is a
[ring homomorphism](trough:RingHom) from $R$ to $S^{-1}R$ under which
the image of every element of $S$ is a unit.

## Universal property

The localization is characterized by a universal property. Let $g$ be a ring
homomorphism from $R$ to a commutative ring $T$ that sends every element of $S$ to
a unit. Then $g$ factors through $S^{-1}R$:
there is a ring homomorphism $h$ from $S^{-1}R$ to $T$ with $h(r/1) = g(r)$ for
every $r \in R$, namely $h(a/s) = g(a)\,g(s)^{-1}$, and
any ring homomorphism from $S^{-1}R$ to $T$ with this property equals
$h$.

Equivalently, a commutative $R$-[algebra](trough:Algebra) $A$ with structure map $f$ is a
localization of $R$ at $S$ exactly when three conditions
hold: $f(s)$ is a unit for each $s \in S$; every element
$z$ of $A$ satisfies $z\,f(s) = f(a)$ for some $a \in R$ and $s \in S$; and
$f(x) = f(y)$ implies $ux = uy$ for some $u \in S$. Any two $R$-algebras with these
properties are isomorphic as $R$-algebras, so one
may speak of the localization.

## Examples

- **Fractions.** The rationals are the localization of the integers at the nonzero
  integers. More generally, localizing an integral domain
  at all of its nonzero elements gives its [field of fractions](trough:IsFractionRing),
  which is a field.
- **Localization at a prime.** For a prime ideal $\mathfrak p$ of $R$, the complement
  $R \setminus \mathfrak p$ is multiplicatively closed, and the
  localization at it is written $R_{\mathfrak p}$. For a
  prime number $p$, the ring $\mathbb Z_{(p)}$ consists of the rationals whose
  denominator in lowest terms is prime to $p$.
- **Inverting one element.** For $f \in R$, the
  localization at the powers of $f$ is written $R_f$ or
  $R[1/f]$. Inverting $2$ in $\mathbb Z$ gives the dyadic rationals, and inverting
  $x$ in the polynomial ring $k[x]$ over a field gives the Laurent polynomials
  $k[x, x^{-1}]$.
- **Degenerate cases.** If $0 \in S$, the localization
  is the zero ring. Less drastically,
  inverting $2$ in $\mathbb Z/6\mathbb Z$ kills $3$, since $2 \cdot 3 = 0$, and the
  result is isomorphic to $\mathbb Z/3\mathbb Z$.

## Properties

- **Kernel.** For $r \in R$,
  $r/1 = 0$ exactly when $ur = 0$ for some $u \in S$.
  Hence the map $R \to S^{-1}R$ is injective exactly when every element of $S$ is
  cancellable, that is, a
  non-zero-divisor.
- **Integral domains.** Localizing an integral domain at a submonoid of nonzero
  elements gives an integral domain.
- **Prime ideals.** Taking preimages under $r \mapsto r/1$ gives
  an order-preserving bijection between the prime ideals of $S^{-1}R$ and the
  prime ideals of $R$ that do not meet $S$.
  For $S = R \setminus \mathfrak p$ the primes of $R$ disjoint from $S$ are those
  contained in $\mathfrak p$, so $R_{\mathfrak p}$ has a single [maximal ideal](trough:Ideal.IsMaximal):
  the localization at a prime ideal is a local ring.
- **Finiteness.** A localization of a Noetherian ring is
  Noetherian (see
  [Noetherian ring](trough:IsNoetherianRing)), since its ideals correspond to certain
  [ideals](trough:Ideal) of $R$ in an order-preserving, injective way.
- **Flatness.** $S^{-1}R$ is a flat $R$-module:
  [tensoring](trough:TensorProduct) with it preserves injective linear maps. Since
  the localized module $S^{-1}M$ is isomorphic to
  $S^{-1}R \otimes_R M$, this is
  equivalent to the statement that localizing modules preserves exact sequences.

## Related concepts

Where a [quotient ring](trough:Ideal.Quotient.ring) forces elements to become
zero, a localization forces them to become invertible, and the two operations
are often combined. The same fractions construction applied to a
[module](trough:Module) $M$ over $R$ gives the
localized module $S^{-1}M$. Applied
to a commutative monoid it gives the monoid of fractions; localizing the additive
monoid of natural numbers at all of its elements gives the additive group of
integers, an instance of the Grothendieck group construction. For noncommutative
rings, fractions can be formed at submonoids that satisfy the Ore condition
together with a cancellation condition, the Ore sets.
In algebraic geometry the rings $R_f$ are the rings of sections of the structure
sheaf over the basic open subsets of the [spectrum](trough:PrimeSpectrum) of $R$, which makes localization a basic ingredient in
the definition of a [scheme](trough:AlgebraicGeometry.Scheme).

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

## Depends on

- [Ring](trough:Ring)
- [Ring morphism](trough:RingHom)
