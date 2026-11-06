---
article_id: af_4b0611227895fd885c6bd71c
concept: Matrix.specialOrthogonalGroup
---

The **special orthogonal group** $\mathrm{SO}_n(R)$ is the group of $n \times n$
[orthogonal matrices](trough:Matrix.orthogonalGroup) over a commutative
[ring](trough:Ring) $R$ whose [determinant](trough:Matrix.det) equals $1$. Over the
[real numbers](trough:Real) it is the group of rotations of $n$-dimensional
Euclidean space: the linear maps that preserve lengths, angles and orientation. It
is one of the classical matrix groups, next to the
[general linear](trough:Matrix.GeneralLinearGroup),
[special linear](trough:Matrix.SpecialLinearGroup) and
[unitary](trough:Matrix.unitaryGroup) groups, and its small cases, the plane and
spatial rotation groups $\mathrm{SO}(2)$ and $\mathrm{SO}(3)$, appear throughout
geometry and mechanics.

## Definition

Let $R$ be a commutative ring and $n \ge 0$. A square [matrix](trough:Matrix) $A \in M_n(R)$
(an $n \times n$ matrix over $R$) is orthogonal when its transpose is its inverse, that is,
$A^{\mathsf{T}} A = I$ and $A A^{\mathsf{T}} = I$. For square matrices over a
commutative ring one of the two equations implies the other:
[$A$ is orthogonal exactly when $A A^{\mathsf{T}} = I$](lean:Matrix.mem_orthogonalGroup_iff),
and [exactly when $A^{\mathsf{T}} A = I$](lean:Matrix.mem_orthogonalGroup_iff').
The [special orthogonal group](lean:Matrix.specialOrthogonalGroup) is

$$\mathrm{SO}_n(R) = \{\, A \in M_n(R) : A^{\mathsf{T}} A = I \text{ and } \det A = 1 \,\},$$

so [a matrix lies in $\mathrm{SO}_n(R)$ exactly when it is orthogonal and has determinant $1$](lean:Matrix.mem_specialOrthogonalGroup_iff).
Over $\mathbb{R}$ one writes $\mathrm{SO}(n)$.

It is a [subgroup](trough:Subgroup) of the orthogonal group $\mathrm{O}_n(R)$. If
$A$ and $B$ lie in $\mathrm{SO}_n(R)$, then $(AB)^{\mathsf{T}} AB = B^{\mathsf{T}} A^{\mathsf{T}} A B = I$
and [$\det(AB) = \det A \det B$](lean:Matrix.det_mul) $= 1$, so products stay in the
group; it contains $I$, and the inverse of $A$ is $A^{\mathsf{T}}$, which is orthogonal and
[has the same determinant as $A$](lean:Matrix.det_transpose). Equivalently,
$\mathrm{SO}_n(R)$ is the intersection of $\mathrm{O}_n(R)$ with the special linear
group, and it is the kernel of the determinant restricted to $\mathrm{O}_n(R)$, hence
a [normal subgroup](trough:Subgroup.Normal) of $\mathrm{O}_n(R)$.

Over $\mathbb{R}$, a matrix is orthogonal exactly when it preserves the dot
product, $(Ax) \cdot (Ay) = x \cdot y$ for all vectors $x, y$; the extra condition
$\det A = 1$ says that it also preserves orientation.

## Examples

- **Dimension one.** The only $1 \times 1$ matrix of determinant $1$ is $(1)$, so
  $\mathrm{SO}_1(R)$ is trivial.
- **Dimension two.** Over any commutative ring,
  [a $2 \times 2$ matrix lies in $\mathrm{SO}_2(R)$ exactly when it has the form below with $a^2 + b^2 = 1$](lean:Matrix.mem_specialOrthogonalGroup_fin_two_iff):

  $$\begin{pmatrix} a & b \\ -b & a \end{pmatrix}.$$

  Over $\mathbb{R}$ one may write $a = \cos\theta$ and $b = -\sin\theta$, which gives
  the rotation of the plane by the angle $\theta$. Composing rotations adds their
  angles, so $\mathrm{SO}(2)$ is abelian and isomorphic to the circle group of
  [complex numbers](trough:Complex) of modulus $1$, the rotation by $\theta$
  corresponding to $e^{i\theta}$. Over the field with three elements the equation
  $a^2 + b^2 = 1$ has four solutions, and $\mathrm{SO}_2$ is cyclic of order $4$.
- **Dimension three.** By Euler's rotation theorem, every
  element of $\mathrm{SO}(3)$ is a rotation about some axis through the origin.
  The group is not abelian: quarter turns about two perpendicular axes do not
  commute.

## Properties

- **Determinant.** For every orthogonal matrix $A$,
  [$(\det A)^2 = 1$](lean:Matrix.det_of_mem_unitary). (Mathlib proves this for
  unitary matrices over a commutative ring with an involution, as the statement that
  $\det A$ is a unitary element, meaning that $\det A$ times its image under the
  involution is $1$; the orthogonal case is the trivial involution, see below, where
  this says $\det A \cdot \det A = 1$.)
- **Index two.** Over a field of characteristic other than $2$ and for $n \ge 1$,
  the determinant of an orthogonal matrix is therefore $\pm 1$, and the diagonal
  matrix with entries $-1, 1, \dots, 1$ is orthogonal of determinant $-1$. So
  $\mathrm{SO}_n$ has [index](trough:Subgroup.index) $2$ in $\mathrm{O}_n$, the other
  coset consisting of the orthogonal matrices of determinant $-1$. Over a field of
  characteristic $2$, where $-1 = 1$, every orthogonal matrix has determinant $1$,
  so the two groups coincide; the group called special orthogonal in that setting
  is defined in another way.
- **Odd dimension.** Over a field of characteristic other than $2$ and for odd $n$,
  the matrix $-I$ is central, orthogonal and of determinant $-1$, so $\mathrm{O}_n$
  is isomorphic to the [direct product](trough:Prod.instGroup)
  $\mathrm{SO}_n \times \{I, -I\}$, the isomorphism being multiplication.
- **Topology.** For $n \ge 1$, $\mathrm{SO}(n)$ is a compact, connected
  [Lie group](trough:LieGroup) of dimension $n(n-1)/2$, and it is the connected
  component of the identity in $\mathrm{O}(n)$.
- **Orthonormal bases.** In a finite-dimensional real
  [inner product space](trough:InnerProductSpace), the matrix expressing one
  orthonormal basis in terms of another
  [is orthogonal](lean:OrthonormalBasis.toMatrix_orthonormalBasis_mem_orthogonal);
  [its determinant is $1$ when the two bases have the same orientation](lean:OrthonormalBasis.det_to_matrix_orthonormalBasis_of_same_orientation)
  and [$-1$ when they have opposite orientations](lean:OrthonormalBasis.det_to_matrix_orthonormalBasis_of_opposite_orientation).
  Hence the columns of a matrix in $\mathrm{SO}(n)$ form an orthonormal basis of
  $\mathbb{R}^n$ that is positively oriented, that is, has the same
  [orientation](trough:Orientation) as the standard basis, and each such basis
  arises from exactly one matrix in the group.

## Related concepts

- The [orthogonal group](trough:Matrix.orthogonalGroup) drops the determinant
  condition.
- The [special unitary group](trough:Matrix.specialUnitaryGroup) is the complex
  analogue; a real matrix is unitary exactly when it is orthogonal, so
  $\mathrm{SO}(n)$ consists of the real matrices in $\mathrm{SU}(n)$.
- More generally, over a field of characteristic other than $2$, a nondegenerate
  [quadratic form](trough:QuadraticForm) $Q$ has a special orthogonal group, the
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

## Depends on

- [Orthogonal group](trough:Matrix.orthogonalGroup)
- [Determinant](trough:Matrix.det)
- [Subgroup](trough:Subgroup)
