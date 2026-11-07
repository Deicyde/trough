For a commutative ring $R$, the **category of algebras over $R$** has as its
objects the associative unital [algebras over $R$](trough:Algebra) and as its
morphisms the homomorphisms of $R$-algebras. It is the natural home for the
constructions of commutative and noncommutative algebra that are characterized
by universal properties, such as polynomial rings, free algebras, tensor algebras
and tensor products, and it sits between the [category of rings](trough:RingCat)
and the [category of $R$-modules](trough:ModuleCat), to both of which it maps by
forgetting structure.

## Definition

An $R$-algebra is a [ring](trough:Ring) $A$, not necessarily commutative, together
with a [ring homomorphism](trough:RingHom) $\iota_A \colon R \to A$ whose image lies
in the centre of $A$. Equivalently, $A$ is a ring and an $R$-module at once, with

$$r(ab) = (ra)b = a(rb) \qquad \text{for all } r \in R,\ a, b \in A.$$

A homomorphism of $R$-algebras $f \colon A \to B$ is a ring homomorphism, sending
$1$ to $1$, with $f(\iota_A(r)) = \iota_B(r)$ for every $r \in R$; equivalently, a
ring homomorphism that is $R$-linear. With composition of functions and the
identity maps, these data form the category of $R$-algebras, often
written $\mathrm{Alg}_R$. It is a [category](trough:CategoryTheory.Category) whose
objects are sets with extra structure and whose morphisms are functions preserving
it.

## Examples

- The ring $R$ itself, with the identity as structure map.
- The [polynomial ring](trough:Polynomial) $R[X]$. For every $R$-algebra $A$,
  sending a homomorphism $R[X] \to A$ to the image of $X$ is a bijection onto $A$,
  so $R[X]$ is the free $R$-algebra on one generator.
- For an $R$-algebra $A$ and a finite index set of size $n$,
  [the square matrices](trough:Matrix) of size $n$ over $A$
  form an $R$-algebra,
  with $r$ acting through the scalar matrix $\iota_A(r) I$. For $n \ge 2$ and
  $A$ nonzero this algebra is not commutative.
- A field extension $L$ of a [field](trough:Field) $K$ is a $K$-algebra.
- The zero ring, in which $0 = 1$, is an $R$-algebra for every $R$.

## Properties

**Initial and terminal objects.** For every $R$-algebra $A$,
the structure map $\iota_A$ is a homomorphism of $R$-algebras, and
it is the only one from $R$ to $A$, so $R$ is an initial object.
Dually, every $R$-algebra has exactly one homomorphism to the zero algebra,
which is therefore terminal.

**Limits.** The category has all small limits, and
the forgetful functor to sets preserves them,
so limits are computed on underlying sets: a product is the Cartesian product with
componentwise operations, and the equalizer of $f, g \colon A \to B$ is the
subalgebra of elements $a$ with $f(a) = g(a)$. Limits are likewise preserved by the
forgetful functors to rings and
to $R$-modules.

**Free objects.** Forgetting part of the structure gives functors
to the category of rings,
to the category of $R$-modules and to sets, and
each of them has a left [adjoint](trough:CategoryTheory.Adjunction). For rings it
sends a ring $A$ to $R \otimes_{\mathbb{Z}} A$. For the other two the adjoints are
free constructions, and these are the two Mathlib provides:
the free algebra functor is left adjoint to the forgetful functor to sets,
sending a set $S$ to the [free algebra](trough:FreeAlgebra) of noncommutative
polynomials in the elements of $S$, and
the tensor algebra functor is left adjoint to the forgetful functor to modules,
sending a module $M$ to its [tensor algebra](trough:TensorAlgebra).

**Isomorphisms.** Isomorphisms in the category correspond exactly to isomorphisms of $R$-algebras,
and a homomorphism whose underlying function is bijective is an isomorphism,
since the inverse function is automatically a homomorphism.

**Tensor products.** The [tensor product](trough:Algebra.TensorProduct.instAlgebra)
$A \otimes_R B$ is again an $R$-algebra, and
with it, and with $R$ as unit, the category is monoidal
([monoidal category](trough:CategoryTheory.MonoidalCategory)); the swap
$a \otimes b \mapsto b \otimes a$ makes it
a symmetric monoidal category. The tensor
product is not in general the coproduct:
homomorphisms $A \otimes_R B \to C$ correspond to pairs of homomorphisms $A \to C$ and $B \to C$ whose images commute elementwise.
Coproducts exist, but they are free products, in which elements of $A$ and $B$
need not commute.

**Change of base.** A ring homomorphism $\varphi \colon R \to S$ makes every
$S$-algebra into an $R$-algebra, with $r$ acting as $\varphi(r)$; this is
the restriction of scalars functor from $S$-algebras
to $R$-algebras. Consequently
isomorphic base rings have equivalent categories of algebras.
Since every ring has a unique ring homomorphism from $\mathbb{Z}$, and it is central,
the category of $\mathbb{Z}$-algebras is equivalent to the category of rings.

## Related concepts

Restricting to commutative algebras gives the category of commutative
$R$-algebras, which is
equivalent to the category of commutative rings equipped with a ring homomorphism from $R$.
There the commutation condition above is automatic, and
the tensor product is the coproduct. Adding
a compatible comultiplication and counit gives
the category of bialgebras over $R$, and adding an antipode
the category of Hopf algebras over $R$.

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

## Depends on

- [Associative algebra over a commutative ring](trough:Algebra)
- [Ring morphism](trough:RingHom)
- [Category](trough:CategoryTheory.Category)
