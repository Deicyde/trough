# The category of algebras over a ring

For a commutative ring $R$, the **category of algebras over $R$** has as its
objects the associative unital [algebras over $R$](associative-algebra-over-a-commutative-ring.md) and as its
morphisms the homomorphisms of $R$-algebras. It is the natural home for the
constructions of commutative and noncommutative algebra that are characterized
by universal properties, such as polynomial rings, free algebras, tensor algebras
and tensor products, and it sits between the [category of rings](../rings/the-category-of-rings.md)
and the [category of $R$-modules](../../linear-algebra/fundamentals/the-category-of-modules-over-a-ring.md), to both of which it maps by
forgetting structure.

## Definition

An $R$-algebra is a [ring](../rings/ring.md) $A$, not necessarily commutative, together
with a [ring homomorphism](../rings/ring-morphism.md) $\iota_A \colon R \to A$ whose image lies
in the centre of $A$. Equivalently, $A$ is a ring and an $R$-module at once, with

$$r(ab) = (ra)b = a(rb) \qquad \text{for all } r \in R,\ a, b \in A.$$

A homomorphism of $R$-algebras $f \colon A \to B$ is a ring homomorphism, sending
$1$ to $1$, with $f(\iota_A(r)) = \iota_B(r)$ for every $r \in R$; equivalently, a
ring homomorphism that is $R$-linear. With composition of functions and the
identity maps, these data form [the category of $R$-algebras](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/AlgCat/Basic.html#AlgCat), often
written $\mathrm{Alg}_R$. It is a [category](../category-theory/category.md) whose
objects are sets with extra structure and whose morphisms are functions preserving
it.

## Examples

- The ring $R$ itself, with the identity as structure map.
- The [polynomial ring](../polynomials-and-power-series/polynomial-in-one-indeterminate.md) $R[X]$. For every $R$-algebra $A$,
  [sending a homomorphism $R[X] \to A$ to the image of $X$ is a bijection onto $A$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/AlgebraMap.html#Polynomial.aevalEquiv),
  so $R[X]$ is the free $R$-algebra on one generator.
- For an $R$-algebra $A$ and a finite index set of size $n$,
  [the square matrices](../../linear-algebra/matrices/ring-valued-matrix.md) of size $n$ over $A$
  [form an $R$-algebra](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Matrix/Basic.html#Matrix.instAlgebra),
  with $r$ acting through the scalar matrix $\iota_A(r) I$. For $n \ge 2$ and
  $A$ nonzero this algebra is not commutative.
- A field extension $L$ of a [field](../field-theory/field.md) $K$ is a $K$-algebra.
- The zero ring, in which $0 = 1$, is an $R$-algebra for every $R$.

## Properties

**Initial and terminal objects.** For every $R$-algebra $A$,
[the structure map $\iota_A$ is a homomorphism of $R$-algebras](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Hom.html#Algebra.ofId), and
[it is the only one from $R$ to $A$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Hom.html#Algebra.ext_id), so $R$ is an initial object.
Dually, [every $R$-algebra has exactly one homomorphism to the zero algebra](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Hom.html#uniqueOfRight),
which is therefore terminal.

**Limits.** The category [has all small limits](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/AlgCat/Limits.html#AlgCat.hasLimits), and
[the forgetful functor to sets preserves them](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/AlgCat/Limits.html#AlgCat.forget_preservesLimits),
so limits are computed on underlying sets: a product is the Cartesian product with
componentwise operations, and the equalizer of $f, g \colon A \to B$ is the
subalgebra of elements $a$ with $f(a) = g(a)$. Limits are likewise preserved by the
forgetful functors [to rings](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/AlgCat/Limits.html#AlgCat.forget%E2%82%82Ring_preservesLimits) and
[to $R$-modules](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/AlgCat/Limits.html#AlgCat.forget%E2%82%82Module_preservesLimits).

**Free objects.** Forgetting part of the structure gives functors
[to the category of rings](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/AlgCat/Basic.html#AlgCat.hasForgetToRing),
[to the category of $R$-modules](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/AlgCat/Basic.html#AlgCat.hasForgetToModule) and to sets, and
each of them has a left [adjoint](../category-theory/adjunction.md). For rings it
sends a ring $A$ to $R \otimes_{\mathbb{Z}} A$. For the other two the adjoints are
free constructions, and these are the two Mathlib provides:
[the free algebra functor is left adjoint to the forgetful functor to sets](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/AlgCat/Basic.html#AlgCat.adj),
sending a set $S$ to the [free algebra](free-algebra-of-a-commutative-ring.md) of noncommutative
polynomials in the elements of $S$, and
[the tensor algebra functor is left adjoint to the forgetful functor to modules](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/AlgCat/TensorAlgebra.html#AlgCat.tensorAlgebraAdj),
sending a module $M$ to its [tensor algebra](tensor-algebra-of-a-commutative-ring.md).

**Isomorphisms.** [Isomorphisms in the category correspond exactly to isomorphisms of $R$-algebras](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/AlgCat/Basic.html#algEquivIsoAlgebraIso),
and [a homomorphism whose underlying function is bijective is an isomorphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/AlgCat/Basic.html#AlgCat.forget_reflects_isos),
since the inverse function is automatically a homomorphism.

**Tensor products.** The [tensor product](tensor-product-of-algebras.md)
$A \otimes_R B$ is again an $R$-algebra, and
[with it, and with $R$ as unit, the category is monoidal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/AlgCat/Monoidal.html#AlgCat.instMonoidalCategory)
([monoidal category](../category-theory/monoidal-category.md)); the swap
$a \otimes b \mapsto b \otimes a$ makes it
[a symmetric monoidal category](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/AlgCat/Symmetric.html#AlgCat.instSymmetricCategory). The tensor
product is not in general the coproduct:
[homomorphisms $A \otimes_R B \to C$ correspond to pairs of homomorphisms $A \to C$ and $B \to C$ whose images commute elementwise](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/Maps.html#Algebra.TensorProduct.liftEquiv).
Coproducts exist, but they are free products, in which elements of $A$ and $B$
need not commute.

**Change of base.** A ring homomorphism $\varphi \colon R \to S$ makes every
$S$-algebra into an $R$-algebra, with $r$ acting as $\varphi(r)$; this is
[the restriction of scalars functor](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/AlgCat/Basic.html#AlgCat.restrictScalars) from $S$-algebras
to $R$-algebras. Consequently
[isomorphic base rings have equivalent categories of algebras](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/AlgCat/Basic.html#AlgCat.restrictScalarsEquivalenceOfRingEquiv).
Since every ring has a unique ring homomorphism from $\mathbb{Z}$, and it is central,
[the category of $\mathbb{Z}$-algebras is equivalent to the category of rings](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/AlgCat/Basic.html#AlgCat.intEquivalence).

## Related concepts

Restricting to commutative algebras gives the category of commutative
$R$-algebras, which is
[equivalent to the category of commutative rings equipped with a ring homomorphism from $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/CommAlgCat/Basic.html#commAlgCatEquivUnder).
There the commutation condition above is automatic, and
[the tensor product is the coproduct](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/CommAlgCat/Monoidal.html#CommAlgCat.binaryCofanIsColimit). Adding
a compatible comultiplication and counit gives
[the category of bialgebras over $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/BialgCat/Basic.html#BialgCat), and adding an antipode
[the category of Hopf algebras over $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/HopfAlgCat/Basic.html#HopfAlgCat).

## In Mathlib

Mathlib bundles an object as a type together with a ring structure and an
$R$-algebra structure on it, and wraps each morphism as an algebra homomorphism;
composition and identities are those of functions. The base ring is required to be
a commutative ring and the algebras to be rings, so algebras over semirings, and
nonunital or nonassociative algebras, are not objects of this category. The
algebras live in a universe of types fixed as a parameter. Some results are stated
only when that universe is the one containing $R$: the free algebra and tensor
algebra adjunctions, the monoidal and symmetric monoidal structures, and the
description of commutative algebras and their coproducts.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Associative algebra over a commutative ring](associative-algebra-over-a-commutative-ring.md)
- [Ring morphism](../rings/ring-morphism.md)
- [Category](../category-theory/category.md)

## Sources

- [Mathlib documentation: `AlgCat`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/AlgCat/Basic.html#AlgCat)
- [Source of `AlgCat` in Mathlib/Algebra/Category/AlgCat/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Algebra/Category/AlgCat/Basic.lean#L28)
- [Mathlib overview: General algebra › Algebras over a ring](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L111)
