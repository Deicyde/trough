The **general linear group** $\mathrm{GL}_n(R)$ is the [group](trough:Group) of invertible
$n \times n$ [matrices](trough:Matrix) with entries in a ring $R$, under matrix
multiplication. Over a [field](trough:Field) $K$ it is the group of all invertible
linear transformations of $K^n$ written in coordinates, so once a basis is chosen,
every group acting linearly on an $n$-dimensional vector space over $K$ maps
homomorphically into $\mathrm{GL}_n(K)$. It is the basic example of a classical group: the special linear, orthogonal and unitary groups
are all subgroups of it, and over finite fields it supplies a large family of
finite groups.

## Definition

Let $R$ be a ring and $n \ge 0$. The
general linear group $\mathrm{GL}_n(R)$ consists of
the $n \times n$ matrices $A$ over $R$ that have a two-sided inverse, a matrix $B$
with $AB = BA = I$, where $I$ is the identity matrix. Products and inverses of
invertible matrices are invertible, and matrix multiplication is associative, so
these matrices form a group with identity $I$. Equivalently, $\mathrm{GL}_n(R)$ is
the group of units of the matrix ring of $n \times n$ matrices over $R$.

When $R$ is commutative, the [determinant](trough:Matrix.det) gives a practical test:
a square matrix is invertible exactly when its determinant is a unit of
$R$. Over a field this means $\det A \neq 0$;
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
  and is not commutative, so it is isomorphic to the [symmetric group](trough:Equiv.Perm) on three letters.
- $\mathrm{GL}_n(\mathbb{Z})$ is the group of integer matrices with determinant
  $\pm 1$; it is the group of changes of basis of the lattice $\mathbb{Z}^n$.

## Properties

**Linear automorphisms.** For a commutative ring $R$, an invertible matrix acts
on column vectors by multiplication, and this identifies
$\mathrm{GL}_n(R)$ with the group of invertible linear maps of
$R^n$ to itself. More generally, a choice of
[basis](trough:Module.Basis) of a module $V$ with $n$ elements
identifies $\mathrm{GL}_n(R)$ with the group of invertible linear maps of
$V$; a different basis changes this
identification by conjugation.

**The determinant.** For a commutative ring $R$,
the determinant is a group homomorphism from $\mathrm{GL}_n(R)$ to
$R^\times$, and for $n \ge 1$
it is surjective: the diagonal
matrix with entries $u, 1, \dots, 1$ has determinant $u$. Its kernel is the
[special linear group](trough:Matrix.SpecialLinearGroup): the matrices of
determinant $1$ are exactly the kernel of the
determinant. Hence
$\mathrm{SL}_n(R)$ is a [normal subgroup](trough:Subgroup.Normal), and by the
[first isomorphism theorem](trough:QuotientGroup.quotientKerEquivRange)
$\mathrm{GL}_n(R) / \mathrm{SL}_n(R) \cong R^\times$ when $n \ge 1$.

**The center.** For a commutative ring $R$,
the center of $\mathrm{GL}_n(R)$ consists of the scalar matrices $uI$ with $u$ a
unit of $R$: a matrix that
commutes with every invertible matrix must be a multiple of the identity.

**Change of ring.** A homomorphism $f \colon R \to S$ of commutative rings,
applied entry by entry,
gives a group homomorphism from $\mathrm{GL}_n(R)$ to
$\mathrm{GL}_n(S)$. Reduction modulo a prime
$p$, from $\mathrm{GL}_n(\mathbb{Z})$ to $\mathrm{GL}_n(\mathbb{F}_p)$, is an instance.

**Order over a finite field.** If $\mathbb{F}$ is a [finite field](trough:Mathlib.FieldTheory.Finite.Basic)
with $q$ elements, then

$$|\mathrm{GL}_n(\mathbb{F})| = (q^n - 1)(q^n - q)(q^n - q^2) \cdots (q^n - q^{n-1}),$$

the product of $q^n - q^i$ over $0 \le i < n$. A
square matrix over a field is invertible exactly when its columns are
[linearly independent](trough:LinearIndependent), so $|\mathrm{GL}_n(\mathbb{F})|$
counts the ordered bases of $\mathbb{F}^n$: the first column can be any nonzero
vector ($q^n - 1$ choices), and the $(i+1)$-th column any vector outside the span
of the first $i$ ($q^n - q^i$ choices). Since the determinant maps
$\mathrm{GL}_n(\mathbb{F})$ onto $\mathbb{F}^\times$ for $n \ge 1$, the first
isomorphism theorem makes the index of $\mathrm{SL}_n(\mathbb{F})$ equal to
$|\mathbb{F}^\times| = q - 1$, and [Lagrange's theorem](trough:Subgroup.card_subgroup_dvd_card)
in the form $|G| = [G : H]\,|H|$ gives
$|\mathrm{SL}_n(\mathbb{F})| \cdot |\mathbb{F}^\times| = |\mathrm{GL}_n(\mathbb{F})|$,
so $|\mathrm{SL}_n(\mathbb{F})| = |\mathrm{GL}_n(\mathbb{F})| / (q - 1)$.

## Related concepts

The [general linear group of a module](trough:LinearMap.GeneralLinearGroup) is the
coordinate-free version: the invertible linear maps of a module to itself, which
are the same as its linear automorphisms.
Its important subgroups include the [special linear group](trough:Matrix.SpecialLinearGroup),
the [orthogonal group](trough:Matrix.orthogonalGroup) and the
[unitary group](trough:Matrix.unitaryGroup). Over a linearly ordered commutative ring such as
the real numbers, the matrices of positive determinant form a
subgroup; over the reals it has index $2$ when $n \ge 1$. The real and
complex general linear groups are Lie groups (see
[general linear group as a Lie group](trough:Units.instLieGroupModelWithCornersSelf)),
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

## Depends on

- [Group](trough:Group)
- [Ring-valued matrix](trough:Matrix)
- [Determinant](trough:Matrix.det)
- [Ring](trough:Ring)
- [Invertible elements](trough:Invertible)

## Proof depends on

- [Lagrange's theorem](trough:Subgroup.card_subgroup_dvd_card)
- [First isomorphism theorem](trough:QuotientGroup.quotientKerEquivRange)
- [Linear independence](trough:LinearIndependent)
