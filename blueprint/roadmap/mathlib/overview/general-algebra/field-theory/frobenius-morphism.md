# Frobenius morphism

The **Frobenius morphism** (or Frobenius endomorphism) of a commutative ring of
prime [characteristic](characteristic-p.md) $p$ is the map that raises every element to its $p$-th
power. In characteristic $p$ this map preserves sums as well as products, so it is a
[ring homomorphism](../rings/ring-morphism.md) from the ring to itself. In characteristic zero no power
map $x \mapsto x^n$ with $n > 1$ is additive, since $(1+1)^n = 2^n$ differs from
$1^n + 1^n = 2$. It is the basic tool for studying
[finite fields](../../../undergraduate/ring-theory/field-theory/finite-fields.md), whose Galois groups it generates,
and it underlies the notion of a perfect field and much of arithmetic geometry in
positive characteristic.

## Definition

Let $R$ be a commutative ring whose characteristic is a [prime](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md) $p$. The
Frobenius morphism is the map $F \colon R \to R$ given by $F(x) = x^p$, and
[this map is a ring homomorphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Lemmas.html#frobenius). It sends $1$ to $1$ and, because $R$ is
commutative, satisfies $(xy)^p = x^p y^p$. Additivity is the key point: the
[binomial theorem](../../../hundred-theorems/part-02/the-binomial-theorem.md) gives

$$(x+y)^p = \sum_{k=0}^{p} \binom{p}{k} x^k y^{p-k},$$

and for $0 < k < p$ the prime $p$ divides $\binom{p}{k} = \frac{p!}{k!\,(p-k)!}$, since it
divides the numerator but not the denominator. Those terms vanish in $R$, leaving
[$(x+y)^p = x^p + y^p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Lemmas.html#add_pow_char), sometimes called the freshman's dream. Applying
additivity to $(x-y) + y$ gives [$(x-y)^p = x^p - y^p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Lemmas.html#sub_pow_char).

Iterating, [the $n$-fold composite of $F$ with itself is the map $x \mapsto x^{p^n}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Frobenius.html#iterate_frobenius),
which is again a ring homomorphism.

## Examples

- **The field with $p$ elements.** On $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$,
  [the Frobenius morphism is the identity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Basic.html#ZMod.frobenius_zmod). This is a restatement of
  [Fermat's little theorem](../../../thousand-plus/number-theory/part-01/fermats-little-theorem.md) in the form $a^p \equiv a \pmod p$.
- **Finite fields.** If $K$ is a finite field of characteristic $p$ with $p^n$ elements, then
  [$F^n$ is the identity of $K$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Basic.html#FiniteField.frobenius_pow), because every element $a$ of
  $K$ satisfies $a^{p^n} = a$.
- **Polynomials.** On the [polynomial ring](../polynomials-and-power-series/polynomial-in-one-indeterminate.md) $\mathbb{F}_p[t]$ the coefficients
  are fixed, so $F$ sends $f(t)$ to $f(t^p)$. More generally, if $K$ is a finite field with
  $q$ elements, then [$f(X)^q = f(X^q)$ for every polynomial $f$ over $K$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Basic.html#FiniteField.Polynomial.expand_card).
  On $\mathbb{F}_p[t]$, $F$ is injective, since $\mathbb{F}_p[t]$ is an integral domain, but not
  surjective: its image consists of the polynomials in $t^p$.
- **A non-injective case.** In $\mathbb{F}_p[x]/(x^p)$ the class of $x$ is nonzero but its
  $p$-th power is zero, so $F$ has a nonzero kernel.

## Properties

- **Naturality.** Every ring homomorphism $g \colon R \to S$ between rings of characteristic $p$
  [commutes with Frobenius: $g(x^p) = g(x)^p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Frobenius.html#RingHom.map_frobenius).
- **Injectivity.** The kernel of $F$ consists of the elements $x$ with $x^p = 0$, which are
  nilpotent. Hence, [if $R$ has no nonzero nilpotent elements, $F$ is injective](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Reduced.html#frobenius_inj).
  In particular the Frobenius of a [field](field.md) or of an integral domain is injective.
- **Perfect rings.** A ring of characteristic $p$ on which $F$ is bijective is called perfect,
  and then $F$ is an automorphism, [the Frobenius automorphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Perfect.html#frobeniusEquiv). An
  injective map from a finite set to itself is bijective, so
  [every finite commutative ring of characteristic $p$ without nonzero nilpotents is perfect](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Perfect.html#PerfectRing.ofFiniteOfIsReduced);
  this covers all finite fields.
- **Perfect fields.** For a field $K$ of characteristic $p$,
  [bijectivity of $F$ makes $K$ a perfect field](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Perfect.html#PerfectRing.toPerfectField), meaning that
  every irreducible polynomial over $K$ is [separable](../polynomials-and-power-series/separable-polynomial.md), and
  [every perfect field has bijective Frobenius](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Perfect.html#PerfectField.toPerfectRing). Since $F$ is
  injective on a field, $K$ is perfect exactly when every element has a $p$-th root. [Finite fields are perfect](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Perfect.html#PerfectField.ofFinite), and so are
  [algebraically closed fields](algebraically-closed-field.md); the rational function field
  $\mathbb{F}_p(t)$ is not, since $t$ has no $p$-th root.
- **Fixed points.** In a field of characteristic $p$ the elements fixed by $F$ are the roots of
  $X^p - X$. There are at most $p$ of them, and the $p$ elements of the prime subfield (the
  subfield generated by $1$, a copy of $\mathbb{Z}/p\mathbb{Z}$) are among them, so
  [an element is fixed by $F$ exactly when it lies in the prime subfield](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Basic.html#Subfield.mem_bot_iff_pow_eq_self).

## Galois groups of finite fields

Let $L$ be a finite field and $K$ a subfield with $q$ elements, and let $n = [L : K]$ be the
degree of the extension. The map $\sigma(x) = x^q$ is a power of the Frobenius morphism of $L$ and
fixes $K$ pointwise. As a power of the injective Frobenius of a field it is injective, and an
injective map from the finite set $L$ to itself is bijective, so it is
[an automorphism of $L$ over $K$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Basic.html#FiniteField.frobeniusAlgEquivOfAlgebraic). Its
[order in the Galois group is $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Basic.html#FiniteField.orderOf_frobeniusAlgEquivOfAlgebraic), and
[every element of the Galois group equals $\sigma^i$ for exactly one $i$ with $0 \le i < n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Basic.html#FiniteField.bijective_frobeniusAlgEquivOfAlgebraic_pow).
So the Galois group of $L$ over $K$ is a [cyclic group](../group-theory/part-01/cyclic-group.md) of order $n$ generated
by $\sigma$. Since the Galois group has order $n = [L : K]$, the extension is Galois, and the
[Galois correspondence](galois-correspondence.md) gives exactly one
intermediate field of degree $d$ over $K$ for each divisor $d$ of $n$.

## Related concepts

The Frobenius automorphism of a finite field has a counterpart in Galois extensions of number
fields. Each prime $P$ of the upper field lying over a prime $\mathfrak{p}$ of the lower field
that does not ramify has a Frobenius element: the unique Galois automorphism that maps $P$ to
itself and induces $x \mapsto x^{N}$ on the residue field at $P$, where $N$ is the number of
elements of the residue field at $\mathfrak{p}$. Primes over the same $\mathfrak{p}$ give
conjugate elements, so the Frobenius of $\mathfrak{p}$ itself is defined only up to conjugacy. On a scheme over $\mathbb{F}_p$, the absolute Frobenius acts as the identity on the
underlying space and as the $p$-th power map on functions. The [perfect closure](perfect-closure.md)
and the [perfection](../number-theory/perfection-of-a-ring.md) of a ring of characteristic $p$ are the universal ways of
making its Frobenius bijective.

## In Mathlib

Mathlib defines the Frobenius morphism as a bundled ring homomorphism on any commutative
semiring, with the exponent $p$ given explicitly together with the hypothesis that $p$ is the
exponential characteristic of the ring. The exponential characteristic is the characteristic when
that is prime and $1$ when the characteristic is zero, so in characteristic zero the Frobenius
morphism is the identity map, and for a ring such as $\mathbb{Z}/6\mathbb{Z}$, whose
characteristic is neither prime nor zero, it is not defined. The iterated map $x \mapsto x^{p^n}$
has its own definition. A perfect ring is defined by bijectivity of the $p$-th power map, while a
perfect field is defined separately by separability of irreducible polynomials, and the two are
linked by the results above. For an extension of finite fields, the automorphism
$x \mapsto x^q$ with $q$ the size of the base field is a separate object, built as an
automorphism over the base field, and is defined more generally for any algebraic extension of a
finite field.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Ring](../rings/ring.md)
- [Ring morphism](../rings/ring-morphism.md)
- [Characteristic p](characteristic-p.md)
- [Prime numbers](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)

## Proof depends on

- [The Binomial Theorem](../../../hundred-theorems/part-02/the-binomial-theorem.md)

## Sources

- [Mathlib documentation: `frobenius`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Lemmas.html#frobenius)
- [Source of `frobenius` in Mathlib/Algebra/CharP/Lemmas.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/CharP/Lemmas.lean#L324)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L125)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L176)
