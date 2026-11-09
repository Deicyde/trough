# General linear group (Classical automorphism groups)

The **general linear group** $\mathrm{GL}_n(R)$ is the [group](../../../overview/general-algebra/group-theory/part-01/group.md) of invertible
$n \times n$ [matrices](../../../overview/linear-algebra/matrices/ring-valued-matrix.md) with entries in a ring $R$, under matrix
multiplication. Over a [field](../../../overview/general-algebra/field-theory/field.md) $K$ it is the group of all invertible
linear transformations of $K^n$ written in coordinates, so once a basis is chosen,
every group acting linearly on an $n$-dimensional vector space over $K$ maps
homomorphically into $\mathrm{GL}_n(K)$. It is the basic example of a classical group: the special linear, orthogonal and unitary groups
are all subgroups of it, and over finite fields it supplies a large family of
finite groups.

## Definition

Let $R$ be a ring and $n \ge 0$. The
[general linear group $\mathrm{GL}_n(R)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/GeneralLinearGroup/Defs.html#Matrix.GeneralLinearGroup) consists of
the $n \times n$ matrices $A$ over $R$ that have a two-sided inverse, a matrix $B$
with $AB = BA = I$, where $I$ is the identity matrix. Products and inverses of
invertible matrices are invertible, and matrix multiplication is associative, so
these matrices form a group with identity $I$. Equivalently, $\mathrm{GL}_n(R)$ is
the group of units of the matrix ring of $n \times n$ matrices over $R$.

When $R$ is commutative, the [determinant](../../../overview/linear-algebra/matrices/determinant.md) gives a practical test:
[a square matrix is invertible exactly when its determinant is a unit of $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/NonsingularInverse.html#Matrix.isUnit_iff_isUnit_det). Over a field this means $\det A \neq 0$;
over the integers it means $\det A = \pm 1$.

## Examples

- For $n = 1$, a $1 \times 1$ matrix is invertible exactly when its entry is a
  unit, so $\mathrm{GL}_1(R)$ is the group of units $R^\times$.
- For $n \ge 2$ and any ring with $1 \neq 0$, the group is not commutative. The
  matrices
  $$A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$
  are invertible, but $AB$ has first row $(1, 1)$ while $BA$ has first row $(0, 1)$.
  For larger $n$, place $A$ and $B$ in the top-left corner of block-diagonal
  matrices whose remaining diagonal entries are $1$; the products still differ.
- Over the two-element field the group $\mathrm{GL}_2(\mathbb{F}_2)$ has six elements
  and is not commutative, so it is isomorphic to the [symmetric group](../../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md) on three letters.
- $\mathrm{GL}_n(\mathbb{Z})$ is the group of integer matrices with determinant
  $\pm 1$; it is the group of changes of basis of the lattice $\mathbb{Z}^n$.

## Properties

**Linear automorphisms.** For a commutative ring $R$, an invertible matrix acts
on column vectors by multiplication, and this identifies
[$\mathrm{GL}_n(R)$ with the group of invertible linear maps of $R^n$ to itself](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/GeneralLinearGroup/Defs.html#Matrix.GeneralLinearGroup.toLin). More generally, a choice of
[basis](../../../overview/linear-algebra/fundamentals/basis.md) of a module $V$ with $n$ elements
[identifies $\mathrm{GL}_n(R)$ with the group of invertible linear maps of $V$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/GeneralLinearGroup/Defs.html#Matrix.GeneralLinearGroup.toLin'); a different basis changes this
identification by conjugation.

**The determinant.** For a commutative ring $R$,
[the determinant is a group homomorphism from $\mathrm{GL}_n(R)$ to $R^\times$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/GeneralLinearGroup/Defs.html#Matrix.GeneralLinearGroup.det), and for $n \ge 1$
[it is surjective](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/GeneralLinearGroup/Defs.html#Matrix.GeneralLinearGroup.det_surjective): the diagonal
matrix with entries $u, 1, \dots, 1$ has determinant $u$. Its kernel is the
[special linear group](../../linear-algebra/multilinearity/special-linear-group.md): [the matrices of determinant $1$ are exactly the kernel of the determinant](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/GeneralLinearGroup/Defs.html#Matrix.SpecialLinearGroup.range_toGL_eq_ker_det). Hence
$\mathrm{SL}_n(R)$ is a [normal subgroup](../../../overview/general-algebra/group-theory/part-01/normal-subgroup.md), and by the
[first isomorphism theorem](../../../overview/general-algebra/group-theory/part-01/first-isomorphism-theorem.md)
$\mathrm{GL}_n(R) / \mathrm{SL}_n(R) \cong R^\times$ when $n \ge 1$.

**The center.** For a commutative ring $R$,
[the center of $\mathrm{GL}_n(R)$ consists of the scalar matrices $uI$ with $u$ a unit of $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/GeneralLinearGroup/Basic.html#Matrix.GeneralLinearGroup.center_eq_range_scalar): a matrix that
commutes with every invertible matrix must be a multiple of the identity.

**Change of ring.** A homomorphism $f \colon R \to S$ of commutative rings,
applied entry by entry,
[gives a group homomorphism from $\mathrm{GL}_n(R)$ to $\mathrm{GL}_n(S)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/GeneralLinearGroup/Defs.html#Matrix.GeneralLinearGroup.map). Reduction modulo a prime
$p$, from $\mathrm{GL}_n(\mathbb{Z})$ to $\mathrm{GL}_n(\mathbb{F}_p)$, is an instance.

**Order over a finite field.** If $\mathbb{F}$ is a [finite field](../../ring-theory/field-theory/finite-fields.md)
with $q$ elements, then

$$|\mathrm{GL}_n(\mathbb{F})| = (q^n - 1)(q^n - q)(q^n - q^2) \cdots (q^n - q^{n-1}),$$

[the product of $q^n - q^i$ over $0 \le i < n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/GeneralLinearGroup/Card.html#Matrix.card_GL_field). A
square matrix over a field is invertible exactly when its columns are
[linearly independent](../../linear-algebra/fundamentals/linear-independence.md), so $|\mathrm{GL}_n(\mathbb{F})|$
counts the ordered bases of $\mathbb{F}^n$: the first column can be any nonzero
vector ($q^n - 1$ choices), and the $(i+1)$-th column any vector outside the span
of the first $i$ ($q^n - q^i$ choices). Since the determinant maps
$\mathrm{GL}_n(\mathbb{F})$ onto $\mathbb{F}^\times$ for $n \ge 1$, the first
isomorphism theorem makes the index of $\mathrm{SL}_n(\mathbb{F})$ equal to
$|\mathbb{F}^\times| = q - 1$, and [Lagrange's theorem](../../../overview/general-algebra/group-theory/part-02/lagranges-theorem.md)
in the form $|G| = [G : H]\,|H|$ gives
[$|\mathrm{SL}_n(\mathbb{F})| \cdot |\mathbb{F}^\times| = |\mathrm{GL}_n(\mathbb{F})|$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/GeneralLinearGroup/Card.html#Matrix.card_SL_mul_card_units),
so $|\mathrm{SL}_n(\mathbb{F})| = |\mathrm{GL}_n(\mathbb{F})| / (q - 1)$.

## Related concepts

The [general linear group of a module](../../../overview/linear-algebra/fundamentals/general-linear-group.md) is the
coordinate-free version: the invertible linear maps of a module to itself, which
[are the same as its linear automorphisms](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/GeneralLinearGroup/Basic.html#LinearMap.GeneralLinearGroup.generalLinearEquiv).
Its important subgroups include the [special linear group](../../linear-algebra/multilinearity/special-linear-group.md),
the [orthogonal group](orthogonal-group.md) and the
[unitary group](unitary-group.md). Over a linearly ordered commutative ring such as
the real numbers, [the matrices of positive determinant form a subgroup](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/GeneralLinearGroup/Defs.html#Matrix.GLPos); over the reals it has index $2$ when $n \ge 1$. The real and
complex general linear groups are Lie groups (see
[general linear group as a Lie group](../../../overview/geometry/differentiable-manifolds/part-02/general-linear-group-as-a-lie-group.md)),
and once a basis is chosen, a representation of a group on an $n$-dimensional
vector space over $K$ is a homomorphism from the group into $\mathrm{GL}_n(K)$.

## In Mathlib

Mathlib defines the general linear group as the group of units of the monoid of
square matrices: an element is a matrix bundled together with a two-sided inverse.
The rows and columns are labelled by an arbitrary finite type rather than by
$1, \dots, n$, so the usual $\mathrm{GL}_n(R)$ is the case of an index set with $n$
elements, and an empty index set gives the trivial group. The definition needs
only a semiring, not a ring or a commutative ring. The description by
determinants, the determinant homomorphism, the center and the identification
with linear maps are stated for commutative rings, and the counting formula for
finite fields. Cardinalities are natural numbers, with $0$ for an infinite set, so
the relation between the orders of the special and general linear groups holds for
every commutative ring and every $n \ge 1$: when $\mathrm{GL}_n(R)$ is infinite, so
is $\mathrm{SL}_n(R)$ or $R^\times$, and both sides are $0$.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Ring-valued matrix](../../../overview/linear-algebra/matrices/ring-valued-matrix.md)
- [Determinant](../../../overview/linear-algebra/matrices/determinant.md)
- [Ring](../../../overview/general-algebra/rings/ring.md)
- [Invertible elements](../../ring-theory/divisibility-in-integral-domains/invertible-elements.md)

## Proof depends on

- [Lagrange's theorem](../../../overview/general-algebra/group-theory/part-02/lagranges-theorem.md)
- [First isomorphism theorem](../../../overview/general-algebra/group-theory/part-01/first-isomorphism-theorem.md)
- [Linear independence](../../linear-algebra/fundamentals/linear-independence.md)

## Sources

- [Mathlib documentation: `Matrix.GeneralLinearGroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/GeneralLinearGroup/Defs.html#Matrix.GeneralLinearGroup)
- [Source of `Matrix.GeneralLinearGroup` in Mathlib/LinearAlgebra/Matrix/GeneralLinearGroup/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/LinearAlgebra/Matrix/GeneralLinearGroup/Defs.lean#L41)
- [Mathlib undergraduate list: Group Theory › Classical automorphism groups](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L105)
