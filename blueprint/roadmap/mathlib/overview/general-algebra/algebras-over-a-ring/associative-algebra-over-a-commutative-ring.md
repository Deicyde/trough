---
article_id: af_a7323adfbb834937f0549d54
declaration: class
origin: cited
mathlib: true
mathlib_declaration: Algebra
mathlib_file: Mathlib/Algebra/Algebra/Defs.lean
---

# Associative algebra over a commutative ring

An **associative algebra over a commutative ring** $R$, or **$R$-algebra**, is a
[ring](../rings/ring.md) $A$ whose elements can also be multiplied by scalars from $R$,
in a way compatible with the multiplication of $A$. Polynomial rings, matrix rings,
rings of endomorphisms of a [module](../../linear-algebra/fundamentals/module.md) and field extensions are all
algebras over a suitable base, and the notion lets one study such rings together with
their linear structure over $R$. Most of commutative algebra and algebraic geometry is
phrased in terms of $R$-algebras.

## Definition

Let $R$ be a commutative ring. An $R$-algebra is a ring $A$ (associative, with
identity, not necessarily commutative) together with a
[ring homomorphism](../rings/ring-morphism.md) $\eta \colon R \to A$, the structure map, whose
[image lies in the centre of $A$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Defs.html#Algebra): that is,
[$\eta(r)\,a = a\,\eta(r)$ for all $r \in R$ and $a \in A$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Defs.html#Algebra.commutes).
Scalar multiplication is then defined by
[$r \cdot a = \eta(r)\,a$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Defs.html#Algebra.smul_def), and the structure map is recovered
from it as [$\eta(r) = r \cdot 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Defs.html#Algebra.algebraMap_eq_smul_one).

Equivalently, an $R$-algebra is a ring $A$ that is also an $R$-module, such that for
all $r \in R$ and $a, b \in A$

$$(r \cdot a)\,b = r \cdot (ab) = a\,(r \cdot b).$$

An algebra satisfies [the first identity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Defs.html#Algebra.smul_mul_assoc) and
[the second](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Defs.html#Algebra.mul_smul_comm); conversely,
[a module structure on a ring satisfying both identities comes from an algebra structure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Defs.html#Algebra.ofModule),
with structure map $r \mapsto r \cdot 1$. In other words, multiplication
$A \times A \to A$ is $R$-bilinear.

A homomorphism of $R$-algebras $f \colon A \to B$ is a ring homomorphism that
[commutes with the structure maps](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Hom.html#AlgHom), $f(\eta_A(r)) = \eta_B(r)$; such a
map is [$R$-linear](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Hom.html#AlgHom.toLinearMap), and conversely an $R$-linear map that
preserves $1$ and products [is an algebra homomorphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Hom.html#AlgHom.ofLinearMap).
A subalgebra is a subring that
[contains the image of the structure map](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Subalgebra/Basic.html#Subalgebra). The $R$-algebras and their
homomorphisms form [the category of $R$-algebras](the-category-of-algebras-over-a-ring.md).

## Examples

- **Rings over the integers.** Every ring $A$ is a $\mathbb{Z}$-algebra through the
  unique ring homomorphism $\mathbb{Z} \to A$, whose image is central, and
  [no other $\mathbb{Z}$-algebra structure on $A$ exists](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Basic.html#int_algebra_subsingleton).
  Thus $\mathbb{Z}$-algebras are just rings.
- **Commutative algebras.** If $R$ and $S$ are commutative, then
  [any ring homomorphism $R \to S$ makes $S$ an $R$-algebra](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Defs.html#RingHom.toAlgebra),
  [with that homomorphism as its structure map](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Defs.html#RingHom.algebraMap_toAlgebra).
  So a commutative $R$-algebra is the same thing as a commutative ring $S$ with a ring
  homomorphism $R \to S$. Examples are a [quotient ring](../ideals-and-quotients/quotient-ring.md)
  $R/I$, a [localization](../rings/localization.md) of $R$, and an extension field $L$ of a
  [field](../field-theory/field.md) $K$, which is a $K$-algebra.
- **Polynomials.** If $A$ is an $R$-algebra, the
  [polynomial ring](../polynomials-and-power-series/polynomial-in-one-indeterminate.md)
  [$A[X]$ is an $R$-algebra](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/AlgebraMap.html#Polynomial.algebraOfAlgebra), with
  $r$ acting on coefficients; in particular $R[X]$ is an $R$-algebra. The same holds for
  [polynomials in several indeterminates](../polynomials-and-power-series/polynomial-in-several-indeterminates.md).
- **Matrices.** For a finite index set with $n$ elements and an $R$-algebra $A$, the
  $n \times n$ [matrices](../../linear-algebra/matrices/ring-valued-matrix.md)
  [with entries in $A$ form an $R$-algebra](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Matrix/Basic.html#Matrix.instAlgebra),
  with $\eta(r)$ the scalar matrix $r I$. For $n \ge 2$ and $A = R$ nonzero this algebra
  is not commutative, though $\eta(R)$ is still central.
- **Endomorphisms.** For an $R$-module $M$, the
  [$R$-linear maps](../../linear-algebra/fundamentals/linear-map.md)
  [$M \to M$ form an $R$-algebra](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Basic.html#Module.End.instAlgebra) under
  composition, with $\eta(r)$ the map $m \mapsto rm$ (see
  [algebra of endomorphisms](../../../undergraduate/linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)).
- **Products.** A [product of $R$-algebras is an $R$-algebra](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Pi.html#Pi.algebra),
  operations taken componentwise.
- **Number systems.** The [complex numbers](../numbers/complex-number.md) form a commutative
  $\mathbb{R}$-algebra of dimension $2$, and the quaternions a noncommutative
  $\mathbb{R}$-algebra of dimension $4$ in which every nonzero element is invertible.

## Properties

- The structure map need not be injective. For $n \ge 1$ the ring
  $\mathbb{Z}/n\mathbb{Z}$ is a $\mathbb{Z}$-algebra whose structure map has kernel
  $n\mathbb{Z}$, and the zero ring is an algebra over
  every $R$. The map is injective exactly when
  [distinct scalars act differently on $A$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Basic.html#faithfulSMul_iff_algebraMap_injective).
- If $R$ is the zero ring then
  [every $R$-algebra is the zero ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Defs.html#Algebra.subsingleton), since
  $1 = \eta(1) = \eta(0) = 0$ in $A$.
- **Restriction of scalars.** If $A$ is an $R$-algebra and $g \colon S \to R$ is a ring
  homomorphism from a commutative ring $S$, then
  [$A$ becomes an $S$-algebra with structure map $\eta \circ g$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Defs.html#Algebra.compHom).
- New algebras arise from old ones as quotients by two-sided ideals and as
  [tensor products](tensor-product-of-algebras.md). Others are built from
  other data: [free algebras](free-algebra-of-a-commutative-ring.md) from a set of generators and
  [tensor algebras](tensor-algebra-of-a-commutative-ring.md) from an $R$-module;
  quotients of the tensor algebra give the
  [exterior algebra](exterior-algebra.md) and
  [Clifford algebras](clifford-algebra.md).

## Generalizations

Dropping associativity gives non-associative algebras, of which
[Lie algebras](lie-algebra.md) are the main example; dropping the identity gives
non-unital algebras, such as the continuous functions with compact support on the real line. In both
cases the definition through a module structure and the two compatibility identities
still makes sense, while the definition through a central structure map does not:
without an identity there is no element $1$ for $r$ to act on, and without
associativity the identity $(r \cdot a)\,b = r \cdot (ab)$ no longer follows from
$r \cdot a = \eta(r)\,a$. Over a noncommutative base ring $k$
the usual substitute is a ring $A$ with a ring homomorphism $k \to A$ whose image
need not be central.

## In Mathlib

Mathlib defines algebras with more generality than the textbook version: the base $R$
is a commutative semiring and $A$ a semiring, so that, for instance, every semiring is
an algebra over the natural numbers. An algebra structure is extra data attached to a
pair of existing types rather than a new type, so one ring can carry algebra structures
over several bases at once. The data are a scalar multiplication and a ring
homomorphism from $R$ to $A$, required to land in the centre and to induce the scalar
multiplication. Keeping the scalar multiplication as data lets an algebra structure
reuse a scalar action that already exists, so that the two actions agree by definition
rather than only up to a proof, and [two algebra structures with the same structure map are equal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Defs.html#Algebra.algebra_ext).
Every algebra is automatically a module, every commutative ring is automatically an
algebra over itself, and every ring is automatically an algebra over the integers. Non-unital and non-associative algebras are not
instances of this definition; Mathlib describes them by a module structure together
with the two compatibility identities above.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Ring](../rings/ring.md)
- [Ring morphism](../rings/ring-morphism.md)
- [Module](../../linear-algebra/fundamentals/module.md)

## Sources

- [Mathlib documentation: `Algebra`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Defs.html#Algebra)
- [Source of `Algebra` in Mathlib/Algebra/Algebra/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Algebra/Defs.lean#L91)
- [Mathlib overview: General algebra › Algebras over a ring](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L110)
- [Mathlib undergraduate list: Ring Theory › Algebra](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L139)
