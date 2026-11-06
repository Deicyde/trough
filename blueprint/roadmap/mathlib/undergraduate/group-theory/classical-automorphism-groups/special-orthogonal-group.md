---
article_id: af_4b0611227895fd885c6bd71c
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: Matrix.specialOrthogonalGroup
mathlib_file: Mathlib/LinearAlgebra/UnitaryGroup.lean
---

# Special orthogonal group

The **special orthogonal group** $\mathrm{SO}_n(R)$ is the group of $n \times n$
[orthogonal matrices](orthogonal-group.md) over a commutative
[ring](../../../overview/general-algebra/rings/ring.md) $R$ whose [determinant](../../../overview/linear-algebra/matrices/determinant.md) equals $1$. Over the
[real numbers](../../../overview/general-algebra/numbers/real-number.md) it is the group of rotations of $n$-dimensional
Euclidean space: the linear maps that preserve lengths, angles and orientation. It
is one of the classical matrix groups, next to the
[general linear](general-linear-group.md),
[special linear](../../linear-algebra/multilinearity/special-linear-group.md) and
[unitary](unitary-group.md) groups, and its small cases, the plane and
spatial rotation groups $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$, appear throughout
geometry and mechanics.

## Definition

Let $R$ be a commutative ring and $n \ge 0$. A square [matrix](../../../overview/linear-algebra/matrices/ring-valued-matrix.md) $A \in M_n(R)$
(an $n \times n$ matrix over $R$) is orthogonal when its transpose is its inverse, that is,
$A^{\mathsf{T}} A = I$ and $A A^{\mathsf{T}} = I$. For square matrices over a
commutative ring one of the two equations implies the other:
[$A$ is orthogonal exactly when $A A^{\mathsf{T}} = I$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.mem_orthogonalGroup_iff),
and [exactly when $A^{\mathsf{T}} A = I$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.mem_orthogonalGroup_iff').
The [special orthogonal group](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.specialOrthogonalGroup) is

$$\mathrm{SO}_n(R) = \{\, A \in M_n(R) : A^{\mathsf{T}} A = I \text{ and } \det A = 1 \,\},$$

so [a matrix lies in $\mathrm{SO}_n(R)$ exactly when it is orthogonal and has determinant $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.mem_specialOrthogonalGroup_iff).
Over $\mathbb{R}$ one writes $\mathrm{SO}(n)$.

It is a [subgroup](../../../overview/general-algebra/group-theory/part-01/subgroup.md) of the orthogonal group $\mathrm{O}_n(R)$. If
$A$ and $B$ lie in $\mathrm{SO}_n(R)$, then $(AB)^{\mathsf{T}} AB = B^{\mathsf{T}} A^{\mathsf{T}} A B = I$
and [$\det(AB) = \det A \det B$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Determinant/Basic.html#Matrix.det_mul) $= 1$, so products stay in the
group; it contains $I$, and the inverse of $A$ is $A^{\mathsf{T}}$, which is orthogonal and
[has the same determinant as $A$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Determinant/Basic.html#Matrix.det_transpose). Equivalently,
$\mathrm{SO}_n(R)$ is the intersection of $\mathrm{O}_n(R)$ with the special linear
group, and it is the kernel of the determinant restricted to $\mathrm{O}_n(R)$, hence
a [normal subgroup](../../../overview/general-algebra/group-theory/part-01/normal-subgroup.md) of $\mathrm{O}_n(R)$.

Over $\mathbb{R}$, a matrix is orthogonal exactly when it preserves the dot
product, $(Ax) \cdot (Ay) = x \cdot y$ for all vectors $x, y$; the extra condition
$\det A = 1$ says that it also preserves orientation.

## Examples

- **Dimension one.** The only $1 \times 1$ matrix of determinant $1$ is $(1)$, so
  $\mathrm{SO}_1(R)$ is trivial.
- **Dimension two.** Over any commutative ring,
  [a $2 \times 2$ matrix lies in $\mathrm{SO}_2(R)$ exactly when it has the form below with $a^2 + b^2 = 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.mem_specialOrthogonalGroup_fin_two_iff):

  $$\begin{pmatrix} a & b \\ -b & a \end{pmatrix}.$$

  Over $\mathbb{R}$ one may write $a = \cos\theta$ and $b = -\sin\theta$, which gives
  the rotation of the plane by the angle $\theta$. Composing rotations adds their
  angles, so $\mathrm{SO}(2)$ is abelian and isomorphic to the circle group of
  [complex numbers](../../../overview/general-algebra/numbers/complex-number.md) of modulus $1$, the rotation by $\theta$
  corresponding to $e^{i\theta}$. Over the field with three elements the equation
  $a^2 + b^2 = 1$ has four solutions, and $\mathrm{SO}_2$ is cyclic of order $4$.
- **Dimension three.** By Euler's rotation theorem, every
  element of $\mathrm{SO}(3)$ is a rotation about some axis through the origin.
  The group is not abelian: quarter turns about two perpendicular axes do not
  commute.

## Properties

- **Determinant.** For every orthogonal matrix $A$,
  [$(\det A)^2 = 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.det_of_mem_unitary). (Mathlib proves this for
  unitary matrices over a commutative ring with an involution, as the statement that
  $\det A$ is a unitary element, meaning that $\det A$ times its image under the
  involution is $1$; the orthogonal case is the trivial involution, see below, where
  this says $\det A \cdot \det A = 1$.)
- **Index two.** Over a field of characteristic other than $2$ and for $n \ge 1$,
  the determinant of an orthogonal matrix is therefore $\pm 1$, and the diagonal
  matrix with entries $-1, 1, \dots, 1$ is orthogonal of determinant $-1$. So
  $\mathrm{SO}_n$ has [index](../../../overview/general-algebra/group-theory/part-01/index-of-a-subgroup.md) $2$ in $\mathrm{O}_n$, the other
  coset consisting of the orthogonal matrices of determinant $-1$. Over a field of
  characteristic $2$, where $-1 = 1$, every orthogonal matrix has determinant $1$,
  so the two groups coincide; the group called special orthogonal in that setting
  is defined in another way.
- **Odd dimension.** Over a field of characteristic other than $2$ and for odd $n$,
  the matrix $-I$ is central, orthogonal and of determinant $-1$, so $\mathrm{O}_n$
  is isomorphic to the [direct product](../basic-definitions/direct-product-of-groups.md)
  $\mathrm{SO}_n \times \{I, -I\}$, the isomorphism being multiplication.
- **Topology.** For $n \ge 1$, $\mathrm{SO}(n)$ is a compact, connected
  [Lie group](../../../overview/geometry/differentiable-manifolds/part-01/lie-group.md) of dimension $n(n-1)/2$, and it is the connected
  component of the identity in $\mathrm{O}(n)$.
- **Orthonormal bases.** In a finite-dimensional real
  [inner product space](../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md), the matrix expressing one
  orthonormal basis in terms of another
  [is orthogonal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/PiL2.html#OrthonormalBasis.toMatrix_orthonormalBasis_mem_orthogonal);
  [its determinant is $1$ when the two bases have the same orientation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Orientation.html#OrthonormalBasis.det_to_matrix_orthonormalBasis_of_same_orientation)
  and [$-1$ when they have opposite orientations](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Orientation.html#OrthonormalBasis.det_to_matrix_orthonormalBasis_of_opposite_orientation).
  Hence the columns of a matrix in $\mathrm{SO}(n)$ form an orthonormal basis of
  $\mathbb{R}^n$ that is positively oriented, that is, has the same
  [orientation](../../linear-algebra/multilinearity/orientation-of-a-r-vector-space.md) as the standard basis, and each such basis
  arises from exactly one matrix in the group.

## Related concepts

- The [orthogonal group](orthogonal-group.md) drops the determinant
  condition.
- The [special unitary group](special-unitary-group.md) is the complex
  analogue; a real matrix is unitary exactly when it is orthogonal, so
  $\mathrm{SO}(n)$ consists of the real matrices in $\mathrm{SU}(n)$.
- More generally, over a field of characteristic other than $2$, a nondegenerate
  [quadratic form](../../../overview/linear-algebra/bilinear-and-quadratic-forms/quadratic-form.md) $Q$ has a special orthogonal group, the
  linear maps of determinant $1$ that preserve $Q$; $\mathrm{SO}_n$ is the case of
  the sum of $n$ squares.

## In Mathlib

Mathlib defines the special orthogonal group for square matrices indexed by any
finite type with decidable equality, with entries in any commutative ring, as a submonoid of the matrices;
the inverse of an element is its transpose, which makes it a group. The definition
reuses the unitary theory: a commutative ring is given the trivial involution, so
the conjugate transpose becomes the transpose, the orthogonal group is the unitary
group for that involution, and the special orthogonal group is the corresponding
special unitary group, the unitary matrices of determinant $1$. Mathlib's own
documentation notes that this definition is the intended one only when $2$ is
invertible, matching the characteristic $2$ caveat above.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Orthogonal group](orthogonal-group.md)
- [Determinant](../../../overview/linear-algebra/matrices/determinant.md)
- [Subgroup](../../../overview/general-algebra/group-theory/part-01/subgroup.md)

## Sources

- [Mathlib documentation: `Matrix.specialOrthogonalGroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.specialOrthogonalGroup)
- [Source of `Matrix.specialOrthogonalGroup` in Mathlib/LinearAlgebra/UnitaryGroup.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/UnitaryGroup.lean#L336)
- [Mathlib undergraduate list: Group Theory › Classical automorphism groups](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L108)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Endomorphisms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L225)
