---
article_id: af_a7323adfbb834937f0549d54
concept: Algebra
---

An **associative algebra over a commutative ring** $R$, or **$R$-algebra**, is a
[ring](trough:Ring) $A$ whose elements can also be multiplied by scalars from $R$,
in a way compatible with the multiplication of $A$. Polynomial rings, matrix rings,
rings of endomorphisms of a [module](trough:Module) and field extensions are all
algebras over a suitable base, and the notion lets one study such rings together with
their linear structure over $R$. Most of commutative algebra and algebraic geometry is
phrased in terms of $R$-algebras.

## Definition

Let $R$ be a commutative ring. An $R$-algebra is a ring $A$ (associative, with
identity, not necessarily commutative) together with a
[ring homomorphism](trough:RingHom) $\eta \colon R \to A$, the structure map, whose
[image lies in the centre of $A$](lean:Algebra): that is,
[$\eta(r)\,a = a\,\eta(r)$ for all $r \in R$ and $a \in A$](lean:Algebra.commutes).
Scalar multiplication is then defined by
[$r \cdot a = \eta(r)\,a$](lean:Algebra.smul_def), and the structure map is recovered
from it as [$\eta(r) = r \cdot 1$](lean:Algebra.algebraMap_eq_smul_one).

Equivalently, an $R$-algebra is a ring $A$ that is also an $R$-module, such that for
all $r \in R$ and $a, b \in A$

$$(r \cdot a)\,b = r \cdot (ab) = a\,(r \cdot b).$$

An algebra satisfies [the first identity](lean:Algebra.smul_mul_assoc) and
[the second](lean:Algebra.mul_smul_comm); conversely,
[a module structure on a ring satisfying both identities comes from an algebra structure](lean:Algebra.ofModule),
with structure map $r \mapsto r \cdot 1$. In other words, multiplication
$A \times A \to A$ is $R$-bilinear.

A homomorphism of $R$-algebras $f \colon A \to B$ is a ring homomorphism that
[commutes with the structure maps](lean:AlgHom), $f(\eta_A(r)) = \eta_B(r)$; such a
map is [$R$-linear](lean:AlgHom.toLinearMap), and conversely an $R$-linear map that
preserves $1$ and products [is an algebra homomorphism](lean:AlgHom.ofLinearMap).
A subalgebra is a subring that
[contains the image of the structure map](lean:Subalgebra). The $R$-algebras and their
homomorphisms form [the category of $R$-algebras](trough:AlgCat).

## Examples

- **Rings over the integers.** Every ring $A$ is a $\mathbb{Z}$-algebra through the
  unique ring homomorphism $\mathbb{Z} \to A$, whose image is central, and
  [no other $\mathbb{Z}$-algebra structure on $A$ exists](lean:int_algebra_subsingleton).
  Thus $\mathbb{Z}$-algebras are just rings.
- **Commutative algebras.** If $R$ and $S$ are commutative, then
  [any ring homomorphism $R \to S$ makes $S$ an $R$-algebra](lean:RingHom.toAlgebra),
  [with that homomorphism as its structure map](lean:RingHom.algebraMap_toAlgebra).
  So a commutative $R$-algebra is the same thing as a commutative ring $S$ with a ring
  homomorphism $R \to S$. Examples are a [quotient ring](trough:Ideal.Quotient.ring)
  $R/I$, a [localization](trough:Localization) of $R$, and an extension field $L$ of a
  [field](trough:Field) $K$, which is a $K$-algebra.
- **Polynomials.** If $A$ is an $R$-algebra, the
  [polynomial ring](trough:Polynomial)
  [$A[X]$ is an $R$-algebra](lean:Polynomial.algebraOfAlgebra), with
  $r$ acting on coefficients; in particular $R[X]$ is an $R$-algebra. The same holds for
  [polynomials in several indeterminates](trough:MvPolynomial).
- **Matrices.** For a finite index set with $n$ elements and an $R$-algebra $A$, the
  $n \times n$ [matrices](trough:Matrix)
  [with entries in $A$ form an $R$-algebra](lean:Matrix.instAlgebra),
  with $\eta(r)$ the scalar matrix $r I$. For $n \ge 2$ and $A = R$ nonzero this algebra
  is not commutative, though $\eta(R)$ is still central.
- **Endomorphisms.** For an $R$-module $M$, the
  [$R$-linear maps](trough:LinearMap)
  [$M \to M$ form an $R$-algebra](lean:Module.End.instAlgebra) under
  composition, with $\eta(r)$ the map $m \mapsto rm$ (see
  [algebra of endomorphisms](trough:Module.End.instAlgebra)).
- **Products.** A [product of $R$-algebras is an $R$-algebra](lean:Pi.algebra),
  operations taken componentwise.
- **Number systems.** The [complex numbers](trough:Complex) form a commutative
  $\mathbb{R}$-algebra of dimension $2$, and the quaternions a noncommutative
  $\mathbb{R}$-algebra of dimension $4$ in which every nonzero element is invertible.

## Properties

- The structure map need not be injective. For $n \ge 1$ the ring
  $\mathbb{Z}/n\mathbb{Z}$ is a $\mathbb{Z}$-algebra whose structure map has kernel
  $n\mathbb{Z}$, and the zero ring is an algebra over
  every $R$. The map is injective exactly when
  [distinct scalars act differently on $A$](lean:faithfulSMul_iff_algebraMap_injective).
- If $R$ is the zero ring then
  [every $R$-algebra is the zero ring](lean:Algebra.subsingleton), since
  $1 = \eta(1) = \eta(0) = 0$ in $A$.
- **Restriction of scalars.** If $A$ is an $R$-algebra and $g \colon S \to R$ is a ring
  homomorphism from a commutative ring $S$, then
  [$A$ becomes an $S$-algebra with structure map $\eta \circ g$](lean:Algebra.compHom).
- New algebras arise from old ones as quotients by two-sided ideals and as
  [tensor products](trough:Algebra.TensorProduct.instAlgebra). Others are built from
  other data: [free algebras](trough:FreeAlgebra) from a set of generators and
  [tensor algebras](trough:TensorAlgebra) from an $R$-module;
  quotients of the tensor algebra give the
  [exterior algebra](trough:ExteriorAlgebra) and
  [Clifford algebras](trough:CliffordAlgebra).

## Generalizations

Dropping associativity gives non-associative algebras, of which
[Lie algebras](trough:LieAlgebra) are the main example; dropping the identity gives
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
rather than only up to a proof, and [two algebra structures with the same structure map are equal](lean:Algebra.algebra_ext).
Every algebra is automatically a module, every commutative ring is automatically an
algebra over itself, and every ring is automatically an algebra over the integers. Non-unital and non-associative algebras are not
instances of this definition; Mathlib describes them by a module structure together
with the two compatibility identities above.

## Depends on

- [Ring](trough:Ring)
- [Ring morphism](trough:RingHom)
- [Module](trough:Module)
