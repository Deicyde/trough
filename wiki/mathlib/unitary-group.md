The **unitary group** $U(n)$ is the [group](trough:Group) of $n \times n$ complex
[matrices](trough:Matrix) $U$ satisfying $U^*U = I$, where $U^*$ is the conjugate
transpose of $U$. These are exactly the matrices of the linear maps of $\mathbb{C}^n$
that preserve the standard Hermitian inner product, so $U(n)$ plays for complex
space the role that the [orthogonal group](trough:Matrix.orthogonalGroup) plays for
real Euclidean space. It is a compact [Lie group](trough:LieGroup), and it is basic to
linear algebra, to the representation theory of finite and compact groups, and to
quantum mechanics, where unitary matrices describe reversible changes of state.

## Definition

For a complex matrix $A$, the conjugate transpose $A^*$ has entries
$(A^*)_{ij} = \overline{A_{ji}}$, where the bar denotes conjugation of
[complex numbers](trough:Complex). A square matrix $U$ is **unitary** if

$$U^*U = UU^* = I,$$

that is, if $U$ is invertible with inverse $U^*$. The
set $U(n)$ of unitary $n \times n$ matrices is closed under
products, since $(UV)^*(UV) = V^*U^*UV = I$ and likewise
$(UV)(UV)^* = UVV^*U^* = I$, and under inverses, so it is a
[subgroup](trough:Subgroup) of the [general linear group](trough:Matrix.GeneralLinearGroup)
$GL_n(\mathbb{C})$. For square matrices either equation alone suffices:
$U$ is unitary exactly when $U^*U = I$, and
exactly when $UU^* = I$.

With the inner product $\langle x, y \rangle = \sum_k \overline{x_k}\, y_k$ on
$\mathbb{C}^n$, the $(i, j)$ entry of $U^*U$ is the inner product of the $i$-th and
$j$-th columns of $U$. So $U$ is unitary if and only if its columns form an
orthonormal basis of $\mathbb{C}^n$, and likewise for its rows. Equivalently,
$\langle Ux, Uy \rangle = \langle x, y \rangle$ for all vectors $x$ and $y$. In the
language of [inner product spaces](trough:InnerProductSpace),
the matrix of a linear isometric equivalence with respect to orthonormal bases is unitary,
and in particular
the change-of-basis matrix between two orthonormal bases is unitary.
Mathlib states both facts for finite-dimensional real or complex inner product spaces.

## Examples

- **The circle group.** A $1 \times 1$ matrix $(z)$ is unitary when $\overline{z}z = 1$, that
  is, $|z| = 1$. So $U(1)$ is the group of complex numbers $e^{i\theta}$ of absolute
  value $1$ under multiplication.
- **Diagonal matrices.**
  A diagonal matrix is unitary exactly when its tuple of diagonal entries is unitary in the product ring,
  that is, when every diagonal entry is unitary; over
  $\mathbb{C}$ this means every diagonal entry has absolute value $1$.
- **Real matrices.** A real matrix is unitary exactly when it is orthogonal, so
  $U(n)$ contains the orthogonal group $O(n)$, including all $n \times n$ permutation
  matrices; for $n = 2$ it contains the rotation matrices of the plane.
- **Pauli matrices.** The matrices
  $$\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$
  are unitary and equal to their own conjugate transposes.
- **The group $U(2)$.** Every element of $U(2)$ has the form
  $$U = \begin{pmatrix} a & b \\ -e^{i\varphi}\,\overline{b} & e^{i\varphi}\,\overline{a} \end{pmatrix}, \qquad |a|^2 + |b|^2 = 1,$$
  for complex $a, b$ and real $\varphi$, and then $\det U = e^{i\varphi}$.

## Properties

- **Inverse.** The inverse of $U$ in the group is $U^*$.
- **Determinant.** The determinant of a unitary matrix satisfies $\overline{\det U}\,\det U = 1$,
  so $|\det U| = 1$. The [determinant](trough:Matrix.det) is therefore a
  homomorphism from $U(n)$ to $U(1)$. For $n \ge 1$ it is onto, since
  $\operatorname{diag}(\lambda, 1, \dots, 1)$ is unitary with determinant $\lambda$
  whenever $|\lambda| = 1$; its kernel is the
  [special unitary group](trough:Matrix.specialUnitaryGroup) $SU(n)$.
- **Eigenvalues and diagonalization.** If $Ux = \lambda x$ with $x \neq 0$, then
  $\|x\| = \|Ux\| = |\lambda|\,\|x\|$, so every eigenvalue has absolute value $1$.
  A unitary matrix commutes with its conjugate transpose,
  so it is [normal](trough:IsStarNormal), and by the spectral theorem for normal
  matrices it can be written $VDV^*$ with $V$ unitary and $D$ diagonal with
  entries on the unit circle.
- **Unitary diagonalization.** For a Hermitian matrix $A$ (one with $A^* = A$) with
  real or complex entries,
  there is a unitary $U$ and a real diagonal matrix $D$ with $A = UDU^*$,
  the matrix form of the
  [diagonalization of self-adjoint endomorphisms](trough:LinearMap.IsSymmetric.eigenvectorBasis_apply_self_apply).
- **Bounded entries.** Every entry of a real or complex unitary matrix has absolute value at most $1$.
- **Closure properties.** The transpose of $U$ is unitary exactly when $U$ is,
  and so is the entrywise conjugate of $U$.
  The Kronecker product of two unitary matrices is unitary.
- **Topology.** $U(n)$ is a closed and bounded subset of the space of complex
  $n \times n$ matrices, hence compact. It is connected, has real dimension $n^2$,
  and its center consists of the scalar matrices $\lambda I$ with $|\lambda| = 1$.

## Generalizations

Unitarity makes sense in any ring or monoid with a star operation, an involution
that reverses products:
an element $u$ is unitary when $u^*u = uu^* = 1$, and
the unitary elements embed injectively into the group of invertible elements.
For bounded operators on a Hilbert space, the adjoint plays the role of the
conjugate transpose:
a unitary operator preserves inner products,
and the unitary operators form a group isomorphic to the group of linear isometric automorphisms of the space.
In a C*-algebra,
every point of the spectrum of a unitary element has absolute value $1$.
Other generalizations include the indefinite unitary groups $U(p, q)$, which
preserve a Hermitian form of signature $(p, q)$, and unitary groups over other
fields with an involution, such as a finite field of order $q^2$ with the map
$x \mapsto x^q$.

## In Mathlib

Mathlib defines the unitary group for square matrices indexed by any finite type,
with entries in any commutative ring carrying a star operation, an involution of
the ring. The conjugate transpose is the
star operation on matrices, and over the
complex numbers the star operation is complex conjugation,
so the classical $U(n)$ is the case of complex entries indexed by $n$ elements. The
unitary group is not built separately: it is the set of unitary elements of the
matrix ring, packaged as a submonoid of matrices, and its group structure, with
inverse given by the star operation, comes from the general construction. The
definition asks for both $U^*U = I$ and $UU^* = I$, and the one-sided criteria above
show either suffices.
The orthogonal group is defined as the unitary group for the trivial star operation,
and the special unitary group as the unitary matrices of determinant $1$.

## Depends on

- [Ring-valued matrix](trough:Matrix)
- [Complex number](trough:Complex)
- [Group](trough:Group)
- [Subgroup](trough:Subgroup)
- [General linear group](trough:Matrix.GeneralLinearGroup)
