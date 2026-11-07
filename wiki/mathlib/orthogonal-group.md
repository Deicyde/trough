The **orthogonal group** $\mathrm{O}(n)$ is the group of $n \times n$ matrices whose transpose is their inverse. Over the real numbers these are exactly the matrices of the linear maps of $\mathbb{R}^n$ that preserve lengths and angles: the rotations, the reflections and their composites. It is one of the classical groups, it is the symmetry group of Euclidean geometry with a fixed origin, and it serves as a basic example of a compact [Lie group](trough:LieGroup).

## Definition

Let $R$ be a commutative [ring](trough:Ring). A square [matrix](trough:Matrix) $A$ with entries in $R$ is **orthogonal** if

$$A A^{\mathsf{T}} = I,$$

where $A^{\mathsf{T}}$ is the transpose of $A$ and $I$ is the identity matrix. The orthogonal matrices of size $n$ form the orthogonal group $\mathrm{O}(n, R)$, a subgroup of the [general linear group](trough:Matrix.GeneralLinearGroup) of invertible $n \times n$ matrices; when $R = \mathbb{R}$ one writes simply $\mathrm{O}(n)$.

For square matrices over a commutative ring a one-sided inverse is automatically two-sided, so the condition can be written either way: $A$ is orthogonal exactly when $A A^{\mathsf{T}} = I$, and also exactly when $A^{\mathsf{T}} A = I$. In terms of entries, the first condition says that the rows of $A$ are orthonormal for the standard dot product, and the second says the same of the columns.

The set is a group under matrix multiplication: $I$ is orthogonal, the inverse of $A$ is $A^{\mathsf{T}}$, which is again orthogonal, and if $A$ and $B$ are orthogonal then $(AB)(AB)^{\mathsf{T}} = A B B^{\mathsf{T}} A^{\mathsf{T}} = I$.

## Examples

- **Size one.** $\mathrm{O}(1, R)$ consists of the elements $a \in R$ with $a^2 = 1$; over a field, or more generally an integral domain, this is $\{1, -1\}$, a single element in characteristic $2$.
- **Rotations of the plane.** A $2 \times 2$ matrix over a commutative ring
  is orthogonal with determinant $1$ exactly when it has the form
  $$\begin{pmatrix} a & -c \\ c & a \end{pmatrix}, \qquad a^2 + c^2 = 1.$$
  Over $\mathbb{R}$ one can write $a = \cos\theta$ and $c = \sin\theta$, which gives the rotation by the angle $\theta$. The remaining elements of $\mathrm{O}(2)$ are the reflections in lines through the origin, with matrices of the form $\begin{pmatrix} a & c \\ c & -a \end{pmatrix}$ where $a^2 + c^2 = 1$.
- **Permutation matrices.** Every permutation matrix is orthogonal, since its transpose is the matrix of the inverse permutation. More generally a matrix with exactly one nonzero entry in each row and column, that entry being $\pm 1$, is orthogonal; over the integers these signed permutation matrices are the only orthogonal matrices.
- **Reflections.** For a nonzero column vector $v \in \mathbb{R}^n$, the matrix $I - 2\,v v^{\mathsf{T}} / (v^{\mathsf{T}} v)$ is orthogonal. It is the [reflection](trough:Submodule.reflection) in the hyperplane orthogonal to $v$.

## Properties

- **Determinant.** Since the determinant is multiplicative and a matrix and its transpose have the same determinant, an orthogonal matrix satisfies $\det(A)^2 = 1$. Over a field, or any integral domain, this forces $\det A = \pm 1$. The orthogonal matrices of [determinant](trough:Matrix.det) $1$ form the [special orthogonal group](trough:Matrix.specialOrthogonalGroup) $\mathrm{SO}(n, R)$. Over a field of characteristic other than $2$, and for $n \ge 1$, it is a normal subgroup of index $2$, the kernel of the determinant restricted to $\mathrm{O}(n, R)$.
- **Isometries.** A real matrix $A$ is orthogonal if and only if $(Ax) \cdot (Ay) = x \cdot y$ for all $x, y \in \mathbb{R}^n$, that is, if and only if multiplication by $A$ preserves the dot product, and hence lengths and angles. In a finite-dimensional real [inner product space](trough:InnerProductSpace), the change-of-basis matrix between two orthonormal bases is orthogonal, and its determinant is $1$ or $-1$.
- **Generation by reflections.** By the Euclidean case of the Cartan–Dieudonné theorem, every linear isometry of a finite-dimensional real inner product space of dimension $n$ onto itself is a product of at most $n$ reflections in hyperplanes. In matrix terms, every element of $\mathrm{O}(n)$ is a product of at most $n$ reflection matrices of the kind above (see [decomposition into reflections](trough:LinearIsometryEquiv.reflections_generate)).
- **Topology.** Each entry of a real orthogonal matrix has absolute value at most $1$, so $\mathrm{O}(n)$ is bounded; it is also closed, being the set where the continuous map $A \mapsto A A^{\mathsf{T}}$ takes the value $I$. As a closed and bounded set it is a compact subset of the space of real $n \times n$ matrices. For $n \ge 1$ it has two connected components: $\mathrm{SO}(n)$ and the matrices of determinant $-1$.

## Generalizations

Given a nondegenerate symmetric [bilinear form](trough:LinearMap.BilinForm) on $R^n$ with matrix $B$, the matrices $A$ satisfying $A^{\mathsf{T}} B A = B$ form the orthogonal group of the form; the case $B = I$ is the group described here. Indefinite forms on $\mathbb{R}^n$ give the groups $\mathrm{O}(p, q)$, among them the Lorentz group, and over a general field the orthogonal group of a [quadratic form](trough:QuadraticForm) is studied in the same way. Replacing the transpose by the conjugate transpose gives the [unitary group](trough:Matrix.unitaryGroup) of complex matrices with $A A^{*} = I$, of which the orthogonal group is the real counterpart.

## In Mathlib

Mathlib defines the orthogonal group for an arbitrary commutative ring and for square matrices whose rows and columns are indexed by any finite type, not only by $\{1, \dots, n\}$. It does not give a separate construction: the orthogonal group is the unitary group taken with respect to the trivial involution of the ring, so that the conjugate transpose becomes the plain transpose, and every general fact about unitary matrices applies to it. It is packaged as a set of matrices closed under multiplication and containing the identity, with the group structure, in which the inverse is the transpose, inherited from the unitary construction. The special orthogonal group is defined as the orthogonal matrices of determinant $1$, and Mathlib notes that this is the intended group only when $2$ is invertible in the ring. Coordinate-free statements, such as the generation by reflections, are phrased for linear isometries of an inner product space rather than for matrices.

## Depends on

- [Ring-valued matrix](trough:Matrix)
- [Group](trough:Group)
- [Subgroup](trough:Subgroup)
- [Ring](trough:Ring)
- [General linear group](trough:Matrix.GeneralLinearGroup)
