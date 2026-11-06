# Special unitary group

The **special unitary group** $\mathrm{SU}(n)$ is the group of complex
$n \times n$ unitary matrices whose [determinant](../../../overview/linear-algebra/matrices/determinant.md) equals $1$.
It is the subgroup of the [unitary group](unitary-group.md) $\mathrm{U}(n)$
cut out by the single condition $\det A = 1$, the kernel of the determinant, and it
is one of the basic examples of a compact [Lie group](../../../overview/geometry/differentiable-manifolds/part-01/lie-group.md). The group
$\mathrm{SU}(2)$ is a double cover of the rotation group $\mathrm{SO}(3)$ of
three-dimensional space, and the groups
$\mathrm{SU}(n)$ appear throughout representation theory, geometry and physics.

## Definition

For a complex [matrix](../../../overview/linear-algebra/matrices/ring-valued-matrix.md) $A$, write $A^* = \overline{A}^{\mathsf T}$ for its
conjugate transpose. A square matrix $A$ is unitary when $A^*A = AA^* = I$, that is,
when its inverse is $A^*$. For square matrices over a commutative
[ring](../../../overview/general-algebra/rings/ring.md) with an involution either equation alone suffices:
[$A$ is unitary as soon as $AA^* = I$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.mem_unitaryGroup_iff), and
[likewise as soon as $A^*A = I$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.mem_unitaryGroup_iff').
Throughout, $n \ge 1$, and the
[special unitary group](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.specialUnitaryGroup) is

$$\mathrm{SU}(n) = \{ A \in \mathrm{U}(n) : \det A = 1 \},$$

so [a matrix lies in $\mathrm{SU}(n)$ exactly when it is unitary and has determinant $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.mem_specialUnitaryGroup_iff).
In particular [$\mathrm{SU}(n)$ is contained in $\mathrm{U}(n)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.specialUnitaryGroup_le_unitaryGroup).
Equivalently, $\mathrm{SU}(n)$ is the intersection of $\mathrm{U}(n)$ with the
[special linear group](../../linear-algebra/multilinearity/special-linear-group.md) $\mathrm{SL}_n(\mathbb C)$.

It is a [subgroup](../../../overview/general-algebra/group-theory/part-01/subgroup.md) of $\mathrm{U}(n)$. Since
[$\det(AB) = \det A \det B$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Determinant/Basic.html#Matrix.det_mul), a product of two matrices of
determinant $1$ again has determinant $1$. The inverse of a unitary matrix is its
conjugate transpose, and $\det A^* = \overline{\det A}$, so
[the inverse of an element of $\mathrm{SU}(n)$ is its conjugate transpose](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.star_eq_inv)
and again lies in $\mathrm{SU}(n)$.

## Examples

- **Dimension one.** $\mathrm{U}(1)$ is the unit circle
  $\{ z \in \mathbb C : |z| = 1 \}$, and $\mathrm{SU}(1)$ is the trivial group.
- **Dimension two.** Every element of $\mathrm{SU}(2)$ has the form

  $$\begin{pmatrix} a & -\overline{b} \\ b & \overline{a} \end{pmatrix}, \qquad a, b \in \mathbb C, \quad |a|^2 + |b|^2 = 1,$$

  and every such matrix lies in $\mathrm{SU}(2)$. As a space, $\mathrm{SU}(2)$ is
  therefore the unit sphere $S^3$ in $\mathbb C^2 \cong \mathbb R^4$, and as a group it
  is isomorphic to the group of unit quaternions. It maps onto the rotation group
  $\mathrm{SO}(3)$ by a two-to-one homomorphism with kernel $\{ \pm I \}$.
- **Diagonal matrices.** The diagonal matrices
  $\operatorname{diag}(e^{i\theta_1}, \dots, e^{i\theta_n})$ with
  $\theta_1 + \dots + \theta_n \in 2\pi\mathbb Z$ form an abelian subgroup of
  $\mathrm{SU}(n)$, a torus of dimension $n - 1$.
- **Real matrices.** A real matrix in $\mathrm{SU}(n)$ is an orthogonal matrix of
  determinant $1$, so the [special orthogonal group](special-orthogonal-group.md)
  $\mathrm{SO}(n)$ is a subgroup of $\mathrm{SU}(n)$.

## Properties

- **The determinant of a unitary matrix.** For $A$ unitary,
  [$\det A$ is unitary as an element of the ring, that is, $\overline{\det A}\,\det A = \det A\,\overline{\det A} = 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.det_of_mem_unitary);
  over $\mathbb C$ this says $|\det A| = 1$. The determinant is therefore a group
  homomorphism from $\mathrm{U}(n)$ onto $\mathrm{U}(1)$, surjective because
  $\operatorname{diag}(z, 1, \dots, 1)$ has determinant $z$. Its kernel is
  $\mathrm{SU}(n)$, so $\mathrm{SU}(n)$ is a [normal subgroup](../../../overview/general-algebra/group-theory/part-01/normal-subgroup.md)
  of $\mathrm{U}(n)$ with quotient $\mathrm{U}(1)$.
- **Splitting.** Every unitary matrix $U$ factors uniquely as
  $U = D S$ with $D = \operatorname{diag}(\det U, 1, \dots, 1)$ and
  $S \in \mathrm{SU}(n)$, so $\mathrm{U}(n)$ is a semidirect product of
  $\mathrm{SU}(n)$ and $\mathrm{U}(1)$. The multiplication map
  $\mathrm{U}(1) \times \mathrm{SU}(n) \to \mathrm{U}(n)$, $(\lambda, S) \mapsto \lambda S$,
  is a surjective homomorphism whose kernel is cyclic of order $n$.
- **Centre.** The centre of $\mathrm{SU}(n)$ consists of the scalar matrices
  $\omega I$ with $\omega^n = 1$, a cyclic group of order $n$.
- **Diagonalization.** Every element of $\mathrm{SU}(n)$ is conjugate, within
  $\mathrm{SU}(n)$, to a diagonal matrix whose entries have absolute value $1$ and
  product $1$.
- **Topology.** $\mathrm{SU}(n)$ is a compact, connected and simply connected real
  Lie group of dimension $n^2 - 1$. Its [Lie algebra](../../../overview/general-algebra/algebras-over-a-ring/lie-algebra.md)
  $\mathfrak{su}(n)$ consists of the skew-Hermitian matrices of trace $0$.

## Generalizations

The definition makes sense over any commutative ring $R$ with an involution
$a \mapsto \overline{a}$: the conjugate transpose is formed with that involution,
and the special unitary group consists of the matrices with $A^*A = AA^* = I$ and
determinant $1$. Taking the field with $q^2$ elements, with the involution
$a \mapsto a^q$, gives the finite special unitary groups. When $2$ is invertible
in $R$, taking the trivial involution gives the special orthogonal group, since
then $A^*$ is just the transpose; in characteristic $2$ the matrices with
$A^{\mathsf T}A = I$ and determinant $1$ do not form the usual special orthogonal
group of a quadratic form. Related matrix groups include the [general linear group](general-linear-group.md) and the [orthogonal group](orthogonal-group.md).

## In Mathlib

Mathlib defines the special unitary group in this general form: for any finite
index type and any commutative ring with an involution, it is the set of square
matrices that are unitary and have determinant $1$. On matrices the involution is
[the conjugate transpose](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/ConjTranspose.html#Matrix.star_eq_conjTranspose), and unitary means
that both products with the conjugate transpose are the identity. The set is
built as a submonoid of all square matrices, namely the intersection of the
unitary group with the kernel of
[the determinant, viewed as a homomorphism of multiplicative monoids](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Determinant/Basic.html#Matrix.detMonoidHom);
the group structure is then added, with the conjugate transpose as inverse. The
special orthogonal group is the same construction with the trivial involution.
The documentation of the definition notes that it is only correct when $2$ is
invertible, the same restriction as for the trivial involution described under
Generalizations. Mathlib also allows an empty index type, for which the group is
trivial.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Unitary group](unitary-group.md)
- [Determinant](../../../overview/linear-algebra/matrices/determinant.md)
- [Complex number](../../../overview/general-algebra/numbers/complex-number.md)
- [Subgroup](../../../overview/general-algebra/group-theory/part-01/subgroup.md)

## Sources

- [Mathlib documentation: `Matrix.specialUnitaryGroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/UnitaryGroup.html#Matrix.specialUnitaryGroup)
- [Source of `Matrix.specialUnitaryGroup` in Mathlib/LinearAlgebra/UnitaryGroup.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/UnitaryGroup.lean#L276)
- [Mathlib undergraduate list: Group Theory › Classical automorphism groups](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L110)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Endomorphisms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L226)
