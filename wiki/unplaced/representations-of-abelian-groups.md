**Representations of abelian groups** are the [representations](trough:Representation) of a
[group](trough:Group) whose elements commute, so that the linear maps representing them commute
with one another. Over an [algebraically closed field](trough:IsAlgClosed) such as $\mathbb{C}$,
this forces every finite-dimensional [irreducible representation](trough:Representation.IsIrreducible)
to be one-dimensional, and for a finite group whose order is not divisible by the characteristic
of the field (as over $\mathbb{C}$) it forces every finite-dimensional representation to split
into invariant lines. The representation theory of a finite abelian group is therefore the
study of its characters: it amounts to the simultaneous diagonalization of commuting matrices, and
it is the setting of the Fourier transform for finite abelian
groups.

## Definition

Let $G$ be an abelian group and $k$ a field. A representation of $G$ on a vector space $V$ over
$k$ is a homomorphism $\rho$ from $G$ to the group of invertible linear maps
of $V$; because $G$ is abelian, $\rho(g)\rho(h) = \rho(h)\rho(g)$ for all $g, h \in G$. A subspace
$W$ is invariant if $\rho(g)W \subseteq W$ for every $g$, and $\rho$ is
irreducible when $V \neq 0$ and its only invariant subspaces
are $0$ and $V$.

An invertible linear map of a line is multiplication by a nonzero scalar, so a one-dimensional
representation is the same thing as a [homomorphism](trough:MonoidHom) $\chi : G \to k^\times$, a
character of $G$; two one-dimensional representations are isomorphic exactly when they define the
same character. Every one-dimensional representation is irreducible.

## Statement

Let $G$ be an abelian group, $k$ an algebraically closed field, and $V$ a finite-dimensional
irreducible representation of $G$ over $k$. Then
$V$ is one-dimensional.

Now let $G$ be finite and suppose also that the characteristic of $k$ does not divide $|G|$, as
for $k = \mathbb{C}$. Then:

- Every finite-dimensional representation $V$ is a direct sum of one-dimensional ones.
  Equivalently, $V$ has a basis in which every $\rho(g)$ is a diagonal matrix
  $\operatorname{diag}(\chi_1(g), \dots, \chi_n(g))$ for characters $\chi_1, \dots, \chi_n$.
- Each value $\chi(g)$ of a character is a root of unity, since
  $\chi(g)^{|G|} = \chi(g^{|G|}) = 1$; for $k = \mathbb{C}$ these are the
  [complex roots of unity](trough:Complex.mem_rootsOfUnity).
- $G$ has exactly $|G|$ characters, so exactly $|G|$ irreducible representations up to
  isomorphism. For $k = \mathbb{C}$,
  the number of homomorphisms from $G$ to $\mathbb{C}^\times$ equals
  $|G|$; the count uses only that the
  field contains a primitive $m$-th root of unity for each $m$ dividing $|G|$, which every
  algebraically closed field of characteristic not dividing $|G|$ does.

## Proof

Since $G$ is abelian, each $\rho(h)$ commutes with every $\rho(g)$, so
$\rho(h)$ is itself a morphism of representations from $V$ to $V$. By
[Schur's lemma](trough:FDRep.finrank_hom_simple_simple), when $V$ is finite-dimensional and
irreducible over an algebraically closed field,
every linear map of $V$ commuting with all $\rho(g)$ is multiplication by a unique
scalar:
such a map $T$ has an eigenvalue $\lambda$, and the kernel of $T - \lambda$ is a nonzero invariant
subspace, hence all of $V$. So every $\rho(h)$ is a scalar, every subspace of $V$ is invariant, and
irreducibility leaves only a line.

For finite $G$ with $|G|$ nonzero in $k$, [Maschke's theorem](trough:MonoidAlgebra.Submodule.exists_isCompl) gives every
invariant subspace an invariant complement, and induction on the dimension splits $V$ into
irreducible pieces, which are lines. A nonzero vector from each line gives the diagonalizing
basis. Alternatively, each $\rho(g)$ is annihilated by $x^{|G|} - 1$, which has distinct roots, so it is diagonalizable,
and commuting diagonalizable maps can be diagonalized in a common basis. For the count, $G$ is a
product of cyclic groups by the [structure
theorem](trough:AddCommGroup.equiv_free_prod_directSum_zmod); a character of a [cyclic
group](trough:IsCyclic) of order $n$ sends a generator to any of the $n$ distinct $n$-th roots of
unity, and a character of a product is a product of characters of the factors.

## Examples

- **Cyclic shifts.** Let $G = \mathbb{Z}/n$ act on $\mathbb{C}^n$ by having $1$ act as the shift
  $(Tx)_j = x_{j+1}$, indices read modulo $n$. With $\zeta = e^{2\pi i/n}$, the vector
  $(1, \zeta^k, \zeta^{2k}, \dots, \zeta^{(n-1)k})$ satisfies $Tv = \zeta^k v$, and these $n$
  vectors form the basis that diagonalizes $T$. This change of basis is the discrete Fourier
  transform.
- **Rotations of the plane.** Rotation by $2\pi/n$ with $n \ge 3$ gives a representation of
  $\mathbb{Z}/n$ on $\mathbb{R}^2$ with no invariant line, so it is irreducible of dimension $2$:
  the theorem needs an algebraically closed field. Over $\mathbb{C}$ the same matrix has the
  eigenvalues $e^{\pm 2\pi i/n}$ and splits into two characters.
- **Unipotent matrices.** The group $\mathbb{Z}$ acting on $\mathbb{C}^2$ by
  $n \mapsto \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$ fixes the first coordinate line and has
  no other invariant line, so it is not a direct sum of lines. The same matrices with $n$ read
  modulo $p$ give a representation of $\mathbb{Z}/p$ in characteristic $p$ with the same defect.
  Finiteness of $G$ and the condition on the characteristic are both needed for diagonalization.

## Properties

- **Common eigenvectors.** For any abelian group, finite or not, and any nonzero
  finite-dimensional representation over an algebraically closed field, an invariant subspace of
  least positive dimension is irreducible, hence a line: all $\rho(g)$ share an eigenvector.
  Repeating the argument on quotients puts all $\rho(g)$ in upper triangular form at once.
- **Multiplicities.** For finite $G$ and $|G|$ invertible in $k$,
  the number $|G|^{-1} \sum_{g} \chi(g^{-1}) \operatorname{tr} \rho(g)$ equals, as an element of
  $k$, the dimension of the space of morphisms of representations from $\chi$ to
  $V$; in characteristic $0$ it
  is that dimension itself. When $k$ is also algebraically closed, so that $V$ decomposes as in
  the statement, that dimension is the number of times $\chi$ occurs among
  $\chi_1, \dots, \chi_n$. Here $g \mapsto \operatorname{tr}\rho(g)$ is the
  [character](trough:FDRep.character) of $\rho$; for a one-dimensional representation this trace
  is the character $\chi$ itself, so the two uses of the word agree.
- **A characterization of abelian groups.** A finite group all of whose irreducible complex
  representations are one-dimensional is abelian: its regular representation is faithful and
  splits into lines, so in a suitable basis it consists of diagonal matrices, which commute.
- **Agreement with the general theory.** For any finite group, the isomorphism classes of irreducible
  complex representations are as many as the [conjugacy classes](trough:ConjClasses), which in an abelian
  group are single elements.

## Related concepts

The characters of a finite abelian group form its dual
group,
and the [orthogonality of characters](trough:FDRep.char_orthonormal), together with their count,
makes them an orthonormal basis of the space of complex functions on $G$. For nonabelian groups irreducible
representations of higher dimension appear: the symmetric group on three letters has one of
dimension $2$. For the circle group, the continuous one-dimensional complex representations are
$z \mapsto z^m$ for $m \in \mathbb{Z}$, and expanding in them gives Fourier series.

## In Mathlib

Mathlib defines a representation of a monoid $G$ on a module $V$ over $k$ as a monoid
homomorphism from $G$ into the linear endomorphisms of $V$, not into the invertible ones; for a
group the images are invertible automatically. Irreducibility means that the lattice of
subrepresentations has exactly two elements. The one-dimensionality theorem is stated for every
commutative monoid, with no finiteness assumption on $G$, and assumes that $k$ is algebraically
closed and $V$ finite-dimensional. Maschke's theorem is proved in the language of modules over
the group algebra: for a finite group whose order is nonzero in the field $k$, every submodule of
a module over $k[G]$ has a complementary
submodule. The count of characters belongs to the
duality theory of finite commutative groups, with values in the units of any commutative monoid
containing enough roots of unity. For commuting linear maps, Mathlib proves that
if each of a commuting family of endomorphisms of a finite-dimensional space has generalized
eigenspaces spanning the space, then their simultaneous generalized eigenspaces span
it.
Mathlib does not state that a representation of a finite abelian group splits into
one-dimensional pieces or is diagonalizable in a single basis, does not identify the irreducible
representations up to isomorphism with the characters, and does not prove the converse
characterization of abelian groups.

## Depends on

- [Group](trough:Group)
- [Representation](trough:Representation)
- [Irreducible representation](trough:Representation.IsIrreducible)
- [Group morphism](trough:MonoidHom)
- [Algebraically closed field](trough:IsAlgClosed)

## Proof depends on

- [Schur's lemma](trough:FDRep.finrank_hom_simple_simple)
- [Maschke theorem](trough:MonoidAlgebra.Submodule.exists_isCompl)
- [Structure of finitely generated abelian groups](trough:AddCommGroup.equiv_free_prod_directSum_zmod)
- [Cyclic group](trough:IsCyclic)
