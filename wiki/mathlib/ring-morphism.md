A **ring morphism**, or ring homomorphism, is a map between two [rings](trough:Ring)
that respects addition, multiplication and the multiplicative identity. Ring
morphisms are the means of comparing rings: reduction of integers modulo $n$,
evaluation of polynomials at a point and passage to a
[quotient ring](trough:Ideal.Quotient.ring) are all ring morphisms, and the
notions of [ideal](trough:Ideal), quotient and isomorphism of rings are
organized around them.

## Definition

Let $R$ and $S$ be rings with identity. A map $f \colon R \to S$ is a
ring morphism if, for all $x, y \in R$,

$$f(x + y) = f(x) + f(y), \qquad f(xy) = f(x)\,f(y), \qquad f(1) = 1.$$

The first condition says that $f$ is a morphism of additive groups, so it also
gives $f(0) = 0$: from $f(0) = f(0 + 0) = f(0) + f(0)$ one cancels $f(0)$. The
second and third say that $f$ is a [morphism of multiplicative monoids](trough:MonoidHom).
The condition $f(1) = 1$ does not follow from the other two. The zero map
$\mathbb{Z} \to \mathbb{Z}$ preserves sums and products but sends $1$ to $0$,
and the map $x \mapsto (x, 0)$ from $\mathbb{Z}$ to $\mathbb{Z} \times \mathbb{Z}$
preserves sums and products but sends $1$ to $(1, 0)$, which is not the identity
$(1, 1)$. A map that preserves only sums and products is called a morphism of
rings without identity.

An isomorphism of rings is a ring morphism with an inverse ring morphism. As for
groups, the inverse map of a bijective ring morphism automatically preserves the
operations, so every bijective ring morphism is an isomorphism.

## Examples

- The identity map of a ring is a ring morphism, and
  the composite of two ring morphisms is a ring morphism,
  so rings and their morphisms form a [category](trough:RingCat).
- For every ring $R$ there is a ring morphism from the
  [integers](trough:Int) to $R$, sending $n$ to $n \cdot 1$,
  and any two ring morphisms from $\mathbb{Z}$ to $R$ are equal.
  Its image is the smallest subring of $R$, and for $R = \mathbb{Z}/n\mathbb{Z}$ this
  morphism is reduction modulo $n$.
- For an ideal $I$ of a commutative ring $R$, the
  map sending $x$ to its class $x + I$ is a
  surjective ring morphism from $R$ onto the quotient ring $R/I$, and
  its kernel is $I$.
- For a commutative ring $R$ and an element $a \in R$,
  evaluation at $a$ is a ring morphism from the
  [polynomial ring](trough:Polynomial) $R[X]$ to $R$, sending $p$ to the
  [value](trough:Polynomial.eval) $p(a)$.
- For rings $R$ and $S$, the
  projection from the product ring $R \times S$ to $R$ is a
  ring morphism (see [product of rings](trough:Pi.ring), of which $R \times S$ is
  the case of two factors).
- If $R$ is a commutative ring of prime [characteristic](trough:CharP) $p$, the
  binomial coefficients $\binom{p}{k}$ with $0 < k < p$ vanish in $R$, so
  $(x + y)^p = x^p + y^p$ and the
  map $x \mapsto x^p$ is a ring morphism of $R$ to itself, the
  [Frobenius morphism](trough:frobenius).
- Complex conjugation is a ring isomorphism of the complex
  numbers to themselves; it fixes every real number, so it is even an isomorphism
  of algebras over the real numbers.

## Properties

Let $f \colon R \to S$ be a ring morphism. Besides $f(0) = 0$ and $f(1) = 1$, it
preserves negatives and
differences, $f(x - y) = f(x) - f(y)$, and
natural-number powers, $f(x^n) = f(x)^n$. Since
$f(u)f(u^{-1}) = f(u^{-1})f(u) = f(1) = 1$, it
sends units to units, with $f(u)^{-1} = f(u^{-1})$.

If $S$ is not the zero ring then neither is $R$, because $f(1) = 1 \neq 0 = f(0)$
forces $1 \neq 0$ in $R$; equivalently,
a ring with a morphism to a nonzero ring is nonzero.
A ring morphism from a [field](trough:Field) $K$ to a nonzero ring is
injective: its kernel is an ideal of $K$ not
containing $1$, hence zero. Mathlib proves this for every simple ring, a nonzero
ring whose only two-sided ideals are $0$ and the whole ring, which includes all
fields and division rings.

For the rest of this section $R$ and $S$ are commutative. Two sets are
attached to $f$: an ideal of $R$ and a subring of $S$.

- The **kernel** $\ker f = \{ x \in R : f(x) = 0 \}$ is
  an ideal of $R$, and
  $f$ is injective exactly when its kernel is zero,
  since $f(x) = f(y)$ if and only if $x - y \in \ker f$. If $S$ is nonzero and has
  no zero divisors, for instance if $S$ is a field, then
  the kernel is a prime ideal.
- The **image** $f(R)$ is a subring of $S$ (see
  [subring](trough:Subring)).

More generally, the preimage of an ideal of $S$ is an ideal of $R$, and
the preimage of a prime ideal is a prime ideal (see
[prime ideal](trough:Ideal.IsPrime)). The image of an ideal need not be an
ideal: the image of $\mathbb{Z}$ under the inclusion into $\mathbb{Q}$ is not
an ideal of $\mathbb{Q}$. The
[first isomorphism theorem](trough:RingHom.quotientKerEquivOfSurjective) joins
kernel and image: $R / \ker f$ is isomorphic to the image of $f$.
Since every ideal is the kernel of its quotient map, the ideals of $R$ are
exactly the kernels of ring morphisms out of $R$.

## Related concepts

A ring morphism $i \colon R \to S$ from a commutative ring $R$ whose image
commutes with every element of $S$
makes $S$ an algebra over $R$, with $r \cdot s = i(r)\,s$;
see [associative algebra](trough:Algebra). Ring morphisms are in particular
[monoid morphisms](trough:MonoidHom) for multiplication and group morphisms for
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

## Depends on

- [Ring](trough:Ring)
- [Group morphism](trough:MonoidHom)
