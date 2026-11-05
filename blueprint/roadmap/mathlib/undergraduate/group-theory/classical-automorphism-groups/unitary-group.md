---
article_id: af_8bdaa7d3a0c7c84e48fe8b8a
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: Matrix.unitaryGroup
mathlib_file: Mathlib/LinearAlgebra/UnitaryGroup.lean
---

# Unitary group

The **unitary group** $U(n)$ is the [group](../../../overview/general-algebra/group-theory/part-01/group.md) of $n \times n$ complex
[matrices](../../../overview/linear-algebra/matrices/ring-valued-matrix.md) $U$ satisfying $U^*U = I$, where $U^*$ is the conjugate
transpose of $U$. These are exactly the matrices of the linear maps of $\mathbb{C}^n$
that preserve the standard Hermitian inner product, so $U(n)$ plays for complex
space the role that the [orthogonal group](orthogonal-group.md) plays for
real Euclidean space. It is a compact [Lie group](../../../overview/geometry/differentiable-manifolds/part-01/lie-group.md), and it is basic to
linear algebra, to the representation theory of finite and compact groups, and to
quantum mechanics, where unitary matrices describe reversible changes of state.

## Definition

For a complex matrix $A$, the conjugate transpose $A^*$ has entries
$(A^*)_{ij} = \overline{A_{ji}}$, where the bar denotes conjugation of
[complex numbers](../../../overview/general-algebra/numbers/complex-number.md). A square matrix $U$ is **unitary** if

$$U^*U = UU^* = I,$$

that is, if $U$ is invertible with inverse $U^*$. The
[set $U(n)$ of unitary $n \times n$ matrices](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.unitaryGroup) is closed under
products, since $(UV)^*(UV) = V^*U^*UV = I$ and likewise
$(UV)(UV)^* = UVV^*U^* = I$, and under inverses, so it is a
[subgroup](../../../overview/general-algebra/group-theory/part-01/subgroup.md) of the [general linear group](general-linear-group.md)
$GL_n(\mathbb{C})$. For square matrices either equation alone suffices:
[$U$ is unitary exactly when $U^*U = I$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.mem_unitaryGroup_iff'), and
[exactly when $UU^* = I$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.mem_unitaryGroup_iff).

With the inner product $\langle x, y \rangle = \sum_k \overline{x_k}\, y_k$ on
$\mathbb{C}^n$, the $(i, j)$ entry of $U^*U$ is the inner product of the $i$-th and
$j$-th columns of $U$. So $U$ is unitary if and only if its columns form an
orthonormal basis of $\mathbb{C}^n$, and likewise for its rows. Equivalently,
$\langle Ux, Uy \rangle = \langle x, y \rangle$ for all vectors $x$ and $y$. In the
language of [inner product spaces](../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md),
[the matrix of a linear isometric equivalence with respect to orthonormal bases is unitary](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/PiL2.html#LinearIsometryEquiv.toMatrix_mem_unitaryGroup),
and in particular
[the change-of-basis matrix between two orthonormal bases is unitary](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/PiL2.html#OrthonormalBasis.toMatrix_orthonormalBasis_mem_unitary).
Mathlib states both facts for finite-dimensional real or complex inner product spaces.

## Examples

- **The circle group.** A $1 \times 1$ matrix $(z)$ is unitary when $\overline{z}z = 1$, that
  is, $|z| = 1$. So $U(1)$ is the group of complex numbers $e^{i\theta}$ of absolute
  value $1$ under multiplication.
- **Diagonal matrices.**
  [A diagonal matrix is unitary exactly when its tuple of diagonal entries is unitary in the product ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.diagonal_mem_unitary),
  [that is, when every diagonal entry is unitary](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Star/Unitary.html#Pi.mem_unitary_iff); over
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

- **Inverse.** [The inverse of $U$ in the group is $U^*$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.UnitaryGroup.inv_val).
- **Determinant.** [The determinant of a unitary matrix satisfies $\overline{\det U}\,\det U = 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.det_of_mem_unitary),
  so $|\det U| = 1$. The [determinant](../../../overview/linear-algebra/matrices/determinant.md) is therefore a
  homomorphism from $U(n)$ to $U(1)$. For $n \ge 1$ it is onto, since
  $\operatorname{diag}(\lambda, 1, \dots, 1)$ is unitary with determinant $\lambda$
  whenever $|\lambda| = 1$; its kernel is the
  [special unitary group](special-unitary-group.md) $SU(n)$.
- **Eigenvalues and diagonalization.** If $Ux = \lambda x$ with $x \neq 0$, then
  $\|x\| = \|Ux\| = |\lambda|\,\|x\|$, so every eigenvalue has absolute value $1$.
  A unitary matrix [commutes with its conjugate transpose](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Star/Unitary.html#isStarNormal_of_mem_unitary),
  so it is [normal](../../bilinear-and-quadratic-forms-over-a-vector-space/endomorphisms/normal-endomorphism.md), and by the spectral theorem for normal
  matrices it can be written $VDV^*$ with $V$ unitary and $D$ diagonal with
  entries on the unit circle.
- **Unitary diagonalization.** For a Hermitian matrix $A$ (one with $A^* = A$) with
  real or complex entries,
  [there is a unitary $U$ and a real diagonal matrix $D$ with $A = UDU^*$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Matrix/Spectrum.html#Matrix.IsHermitian.spectral_theorem),
  the matrix form of the
  [diagonalization of self-adjoint endomorphisms](../../../overview/linear-algebra/finite-dimensional-inner-product-spaces-see-also/diagonalization-of-self-adjoint-endomorphisms.md).
- **Bounded entries.** [Every entry of a real or complex unitary matrix has absolute value at most $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/CStarAlgebra/Matrix.html#entry_norm_bound_of_unitary).
- **Closure properties.** [The transpose of $U$ is unitary exactly when $U$ is](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.transpose_mem_unitaryGroup_iff),
  and so is [the entrywise conjugate of $U$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.map_star_mem_unitaryGroup_iff).
  [The Kronecker product of two unitary matrices is unitary](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.kronecker_mem_unitary).
- **Topology.** $U(n)$ is a closed and bounded subset of the space of complex
  $n \times n$ matrices, hence compact. It is connected, has real dimension $n^2$,
  and its center consists of the scalar matrices $\lambda I$ with $|\lambda| = 1$.

## Generalizations

Unitarity makes sense in any ring or monoid with a star operation, an involution
that reverses products:
[an element $u$ is unitary when $u^*u = uu^* = 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Star/Unitary.html#unitary), and
[the unitary elements embed injectively into the group of invertible elements](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Star/Unitary.html#Unitary.toUnits_injective).
For bounded operators on a Hilbert space, the adjoint plays the role of the
conjugate transpose:
[a unitary operator preserves inner products](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Adjoint.html#ContinuousLinearMap.inner_map_map_of_mem_unitary),
and [the unitary operators form a group isomorphic to the group of linear isometric automorphisms of the space](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Adjoint.html#Unitary.linearIsometryEquiv).
In a C*-algebra,
[every point of the spectrum of a unitary element has absolute value $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/CStarAlgebra/Spectrum.html#spectrum.norm_eq_one_of_unitary).
Other generalizations include the indefinite unitary groups $U(p, q)$, which
preserve a Hermitian form of signature $(p, q)$, and unitary groups over other
fields with an involution, such as a finite field of order $q^2$ with the map
$x \mapsto x^q$.

## In Mathlib

Mathlib defines the unitary group for square matrices indexed by any finite type,
with entries in any commutative ring carrying a star operation, an involution of
the ring. The conjugate transpose is the
[star operation on matrices](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/ConjTranspose.html#Matrix.star_eq_conjTranspose), and over the
complex numbers [the star operation is complex conjugation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Complex/Basic.html#Complex.star_def),
so the classical $U(n)$ is the case of complex entries indexed by $n$ elements. The
unitary group is not built separately: it is the set of unitary elements of the
matrix ring, packaged as a submonoid of matrices, and its group structure, with
inverse given by the star operation, comes from the general construction. The
definition asks for both $U^*U = I$ and $UU^* = I$, and the one-sided criteria above
show either suffices.
[The orthogonal group is defined as the unitary group for the trivial star operation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.orthogonalGroup),
and the special unitary group as the unitary matrices of determinant $1$.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Ring-valued matrix](../../../overview/linear-algebra/matrices/ring-valued-matrix.md)
- [Complex number](../../../overview/general-algebra/numbers/complex-number.md)
- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Subgroup](../../../overview/general-algebra/group-theory/part-01/subgroup.md)
- [General linear group (Classical automorphism groups)](general-linear-group.md)

## Sources

- [Mathlib documentation: `Matrix.unitaryGroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.unitaryGroup)
- [Source of `Matrix.unitaryGroup` in Mathlib/LinearAlgebra/UnitaryGroup.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/UnitaryGroup.lean#L102)
- [Mathlib undergraduate list: Group Theory › Classical automorphism groups](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L109)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Endomorphisms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L224)
