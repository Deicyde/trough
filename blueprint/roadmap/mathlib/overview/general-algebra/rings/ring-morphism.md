# Ring morphism

A **ring morphism**, or ring homomorphism, is a map between two [rings](ring.md)
that respects addition, multiplication and the multiplicative identity. Ring
morphisms are the means of comparing rings: reduction of integers modulo $n$,
evaluation of polynomials at a point and passage to a
[quotient ring](../ideals-and-quotients/quotient-ring.md) are all ring morphisms, and the
notions of [ideal](../ideals-and-quotients/ideal-of-a-commutative-ring.md), quotient and isomorphism of rings are
organized around them.

## Definition

Let $R$ and $S$ be rings with identity. A map $f \colon R \to S$ is a
[ring morphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Hom/Defs.html#RingHom) if, for all $x, y \in R$,

$$f(x + y) = f(x) + f(y), \qquad f(xy) = f(x)\,f(y), \qquad f(1) = 1.$$

The first condition says that $f$ is a morphism of additive groups, so it also
gives $f(0) = 0$: from $f(0) = f(0 + 0) = f(0) + f(0)$ one cancels $f(0)$. The
second and third say that $f$ is a [morphism of multiplicative monoids](../group-theory/part-01/group-morphism.md).
The condition $f(1) = 1$ does not follow from the other two. The zero map
$\mathbb{Z} \to \mathbb{Z}$ preserves sums and products but sends $1$ to $0$,
and the map $x \mapsto (x, 0)$ from $\mathbb{Z}$ to $\mathbb{Z} \times \mathbb{Z}$
preserves sums and products but sends $1$ to $(1, 0)$, which is not the identity
$(1, 1)$. A map that preserves only sums and products is called a morphism of
[rings without identity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Hom/Defs.html#NonUnitalRingHom).

An isomorphism of rings is a ring morphism with an inverse ring morphism. As for
groups, the inverse map of a bijective ring morphism automatically preserves the
operations, so [every bijective ring morphism is an isomorphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Equiv.html#RingEquiv.ofBijective).

## Examples

- The [identity map of a ring is a ring morphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Hom/Defs.html#RingHom.id), and
  [the composite of two ring morphisms is a ring morphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Hom/Defs.html#RingHom.comp),
  so rings and their morphisms form a [category](the-category-of-rings.md).
- For every ring $R$ there is a ring morphism from the
  [integers](../numbers/integer.md) to $R$, [sending $n$ to $n \cdot 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/Cast/Lemmas.html#Int.castRingHom),
  and [any two ring morphisms from $\mathbb{Z}$ to $R$ are equal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/Cast/Lemmas.html#RingHom.ext_int).
  Its image is the smallest subring of $R$, and for $R = \mathbb{Z}/n\mathbb{Z}$ this
  morphism is reduction modulo $n$.
- For an ideal $I$ of a commutative ring $R$, the
  [map sending $x$ to its class $x + I$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Quotient/Defs.html#Ideal.Quotient.mk) is a
  [surjective](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Quotient/Defs.html#Ideal.Quotient.mk_surjective) ring morphism from $R$ onto the quotient ring $R/I$, and
  [its kernel is $I$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Quotient/Operations.html#Ideal.mk_ker).
- For a commutative ring $R$ and an element $a \in R$,
  [evaluation at $a$ is a ring morphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Eval/Defs.html#Polynomial.evalRingHom) from the
  [polynomial ring](../polynomials-and-power-series/polynomial-in-one-indeterminate.md) $R[X]$ to $R$, sending $p$ to the
  [value](../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/polynomial-functions.md) $p(a)$.
- For rings $R$ and $S$, the
  [projection from the product ring $R \times S$ to $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Prod.html#RingHom.fst) is a
  ring morphism (see [product of rings](../../../undergraduate/ring-theory/fundamentals/product-of-rings.md), of which $R \times S$ is
  the case of two factors).
- If $R$ is a commutative ring of prime [characteristic](../field-theory/characteristic-p.md) $p$, the
  binomial coefficients $\binom{p}{k}$ with $0 < k < p$ vanish in $R$, so
  $(x + y)^p = x^p + y^p$ and the
  [map $x \mapsto x^p$ is a ring morphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Lemmas.html#frobenius) of $R$ to itself, the
  [Frobenius morphism](../field-theory/frobenius-morphism.md).
- [Complex conjugation is a ring isomorphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Complex/Module.html#Complex.conjAe) of the complex
  numbers to themselves; it fixes every real number, so it is even an isomorphism
  of algebras over the real numbers.

## Properties

Let $f \colon R \to S$ be a ring morphism. Besides $f(0) = 0$ and $f(1) = 1$, it
[preserves negatives](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Hom/Defs.html#RingHom.map_neg) and
[differences](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Hom/Defs.html#RingHom.map_sub), $f(x - y) = f(x) - f(y)$, and
[natural-number powers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Hom/Defs.html#RingHom.map_pow), $f(x^n) = f(x)^n$. Since
$f(u)f(u^{-1}) = f(u^{-1})f(u) = f(1) = 1$, it
[sends units to units](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Units/Hom.html#IsUnit.map), with $f(u)^{-1} = f(u^{-1})$.

If $S$ is not the zero ring then neither is $R$, because $f(1) = 1 \neq 0 = f(0)$
forces $1 \neq 0$ in $R$; equivalently,
[a ring with a morphism to a nonzero ring is nonzero](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Hom/Defs.html#RingHom.domain_nontrivial).
A ring morphism from a [field](../field-theory/field.md) $K$ to a nonzero ring is
[injective](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/SimpleRing/Basic.html#RingHom.injective): its kernel is an ideal of $K$ not
containing $1$, hence zero. Mathlib proves this for every simple ring, a nonzero
ring whose only two-sided ideals are $0$ and the whole ring, which includes all
fields and division rings.

For the rest of this section $R$ and $S$ are commutative. Two sets are
attached to $f$: an ideal of $R$ and a subring of $S$.

- The **kernel** $\ker f = \{ x \in R : f(x) = 0 \}$ is
  [an ideal of $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Maps.html#RingHom.ker), and
  [$f$ is injective exactly when its kernel is zero](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Maps.html#RingHom.injective_iff_ker_eq_bot),
  since $f(x) = f(y)$ if and only if $x - y \in \ker f$. If $S$ is nonzero and has
  no zero divisors, for instance if $S$ is a field, then
  [the kernel is a prime ideal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Maps.html#RingHom.ker_isPrime).
- The **image** $f(R)$ is [a subring of $S$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Subring/Basic.html#RingHom.range) (see
  [subring](subring.md)).

More generally, [the preimage of an ideal of $S$ is an ideal of $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Maps.html#Ideal.comap), and
[the preimage of a prime ideal is a prime ideal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Maps.html#Ideal.comap_isPrime) (see
[prime ideal](../ideals-and-quotients/prime-ideal.md)). The image of an ideal need not be an
ideal: the image of $\mathbb{Z}$ under the inclusion into $\mathbb{Q}$ is not
an ideal of $\mathbb{Q}$. The
[first isomorphism theorem](../ideals-and-quotients/first-isomorphism-theorem-for-commutative-rings.md) joins
kernel and image: [$R / \ker f$ is isomorphic to the image of $f$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Quotient/Operations.html#RingHom.quotientKerEquivRange).
Since every ideal is the kernel of its quotient map, the ideals of $R$ are
exactly the kernels of ring morphisms out of $R$.

## Related concepts

A ring morphism $i \colon R \to S$ from a commutative ring $R$ whose image
commutes with every element of $S$
[makes $S$ an algebra over $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Defs.html#RingHom.toAlgebra'), with $r \cdot s = i(r)\,s$;
see [associative algebra](../algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md). Ring morphisms are in particular
[monoid morphisms](../group-theory/part-01/group-morphism.md) for multiplication and group morphisms for
addition, and the kernel, image and first isomorphism theorem above parallel
those of group theory.

## In Mathlib

Mathlib defines ring morphisms in greater generality than rings with identity:
the source and target need only be semirings in which multiplication is not
assumed associative, so negatives are not required and the same structure serves
for semirings such as the natural numbers. Because addition need not be cancellative
in this setting, a morphism is required to preserve $0$ as well as $1$, sums and
products. Morphisms are bundled: a morphism is a function packaged with proofs of
these four properties, and it can be viewed as a monoid morphism, an additive
monoid morphism or a morphism without identity. General results are usually
stated for any type of maps that behaves like ring morphisms, so they apply
equally to ring isomorphisms and to morphisms of algebras. Mathlib's ideals of a
noncommutative ring are left ideals; the kernel is moreover recorded as a
two-sided ideal, and the injectivity criterion and the first isomorphism theorem
are stated without commutativity. The Frobenius morphism is defined for a
commutative semiring of exponential characteristic $p$, which covers both prime
characteristic $p$ and characteristic zero with $p = 1$.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Ring](ring.md)
- [Group morphism](../group-theory/part-01/group-morphism.md)

## Sources

- [Mathlib documentation: `RingHom`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Hom/Defs.html#RingHom)
- [Source of `RingHom` in Mathlib/Algebra/Ring/Hom/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Algebra/Ring/Hom/Defs.lean#L303)
- [Mathlib overview: General algebra › Rings](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L66)
- [Mathlib undergraduate list: Ring Theory › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L128)
