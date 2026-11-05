---
article_id: af_9933b1afe52466d680bc8704
declaration: definition
origin: cited
not_ready: true
---

# Representations of abelian groups

**Representations of abelian groups** are the [representations](../../../overview/general-algebra/representation-theory/representation.md) of a
[group](../../../overview/general-algebra/group-theory/part-01/group.md) whose elements commute, so that the linear maps representing them commute
with one another. Over an [algebraically closed field](../../../overview/general-algebra/field-theory/algebraically-closed-field.md) such as $\mathbb{C}$,
this forces every finite-dimensional [irreducible representation](../../linear-algebra/linear-representations/irreducible-representation.md)
to be one-dimensional, and for a finite group whose order is not divisible by the characteristic
of the field (as over $\mathbb{C}$) it forces every finite-dimensional representation to split
into invariant lines. The representation theory of a finite abelian group is therefore the
study of its characters: it amounts to the simultaneous diagonalization of commuting matrices, and
it is the setting of the [Fourier transform for finite abelian groups](fourier-transform-for-finite-abelian-groups.md).

## Definition

Let $G$ be an abelian group and $k$ a field. A [representation of $G$ on a vector space $V$ over $k$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RepresentationTheory/Basic.html#Representation) is a homomorphism $\rho$ from $G$ to the group of invertible linear maps
of $V$; because $G$ is abelian, $\rho(g)\rho(h) = \rho(h)\rho(g)$ for all $g, h \in G$. A subspace
$W$ is invariant if $\rho(g)W \subseteq W$ for every $g$, and $\rho$ is
[irreducible](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RepresentationTheory/Irreducible.html#Representation.IsIrreducible) when $V \neq 0$ and its only invariant subspaces
are $0$ and $V$.

An invertible linear map of a line is multiplication by a nonzero scalar, so a one-dimensional
representation is the same thing as a [homomorphism](../../../overview/general-algebra/group-theory/part-01/group-morphism.md) $\chi : G \to k^\times$, a
character of $G$; two one-dimensional representations are isomorphic exactly when they define the
same character. Every one-dimensional representation is irreducible.

## Statement

Let $G$ be an abelian group, $k$ an algebraically closed field, and $V$ a finite-dimensional
irreducible representation of $G$ over $k$. Then
[$V$ is one-dimensional](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RepresentationTheory/Irreducible.html#Representation.IsIrreducible.finrank_eq_one_of_isMulCommutative).

Now let $G$ be finite and suppose also that the characteristic of $k$ does not divide $|G|$, as
for $k = \mathbb{C}$. Then:

- Every finite-dimensional representation $V$ is a direct sum of one-dimensional ones.
  Equivalently, $V$ has a basis in which every $\rho(g)$ is a diagonal matrix
  $\operatorname{diag}(\chi_1(g), \dots, \chi_n(g))$ for characters $\chi_1, \dots, \chi_n$.
- Each value $\chi(g)$ of a character is a root of unity, since
  $\chi(g)^{|G|} = \chi(g^{|G|}) = 1$; for $k = \mathbb{C}$ these are the
  [complex roots of unity](../abelian-group/complex-roots-of-unity.md).
- $G$ has exactly $|G|$ characters, so exactly $|G|$ irreducible representations up to
  isomorphism. For $k = \mathbb{C}$,
  [the number of homomorphisms from $G$ to $\mathbb{C}^\times$ equals $|G|$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/FiniteAbelian/Duality.html#CommGroup.card_monoidHom_of_hasEnoughRootsOfUnity); the count uses only that the
  field contains a primitive $m$-th root of unity for each $m$ dividing $|G|$, which every
  algebraically closed field of characteristic not dividing $|G|$ does.

## Proof

Since $G$ is abelian, each $\rho(h)$ commutes with every $\rho(g)$, so
[$\rho(h)$ is itself a morphism of representations from $V$ to $V$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RepresentationTheory/Rep/Basic.html#Rep.applyAsHom). By
[Schur's lemma](../../linear-algebra/linear-representations/schurs-lemma.md), when $V$ is finite-dimensional and
irreducible over an algebraically closed field,
[every linear map of $V$ commuting with all $\rho(g)$ is multiplication by a unique scalar](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RepresentationTheory/Irreducible.html#Representation.IsIrreducible.algebraMap_intertwiningMap_bijective_of_isAlgClosed):
such a map $T$ has an eigenvalue $\lambda$, and the kernel of $T - \lambda$ is a nonzero invariant
subspace, hence all of $V$. So every $\rho(h)$ is a scalar, every subspace of $V$ is invariant, and
irreducibility leaves only a line.

For finite $G$ with $|G|$ nonzero in $k$, [Maschke's theorem](maschke-theorem.md) gives every
invariant subspace an invariant complement, and induction on the dimension splits $V$ into
irreducible pieces, which are lines. A nonzero vector from each line gives the diagonalizing
basis. Alternatively, each $\rho(g)$ is annihilated by $x^{|G|} - 1$, which has distinct roots, so it is [diagonalizable](../../linear-algebra/structure-theory-of-endomorphisms/diagonalization.md),
and commuting diagonalizable maps can be diagonalized in a common basis. For the count, $G$ is a
product of cyclic groups by the [structure theorem](../../../overview/general-algebra/group-theory/part-02/structure-of-finitely-generated-abelian-groups.md); a character of a [cyclic group](../../../overview/general-algebra/group-theory/part-01/cyclic-group.md) of order $n$ sends a generator to any of the $n$ distinct $n$-th roots of
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
  [the number $|G|^{-1} \sum_{g} \chi(g^{-1}) \operatorname{tr} \rho(g)$ equals, as an element of $k$, the dimension of the space of morphisms of representations from $\chi$ to $V$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RepresentationTheory/Character.html#Representation.card_inv_mul_sum_char_mul_char_eq_finrank); in characteristic $0$ it
  is that dimension itself. When $k$ is also algebraically closed, so that $V$ decomposes as in
  the statement, that dimension is the number of times $\chi$ occurs among
  $\chi_1, \dots, \chi_n$. Here $g \mapsto \operatorname{tr}\rho(g)$ is the
  [character](../../../overview/general-algebra/representation-theory/character.md) of $\rho$; for a one-dimensional representation this trace
  is the character $\chi$ itself, so the two uses of the word agree.
- **A characterization of abelian groups.** A finite group all of whose irreducible complex
  representations are one-dimensional is abelian: its regular representation is faithful and
  splits into lines, so in a suitable basis it consists of diagonal matrices, which commute.
- **Agreement with the general theory.** For any finite group, the isomorphism classes of irreducible
  complex representations are as many as the [conjugacy classes](../basic-definitions/conjugacy-classes.md), which in an abelian
  group are single elements.

## Related concepts

The characters of a finite abelian group form its [dual group](dual-groups.md),
and the [orthogonality of characters](../../../overview/general-algebra/representation-theory/orthogonality-of-characters.md), together with their count,
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
the group algebra: [for a finite group whose order is nonzero in the field $k$, every submodule of a module over $k[G]$ has a complementary submodule](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RepresentationTheory/Maschke.html#MonoidAlgebra.Submodule.exists_isCompl). The count of characters belongs to the
duality theory of finite commutative groups, with values in the units of any commutative monoid
containing enough roots of unity. For commuting linear maps, Mathlib proves that
[if each of a commuting family of endomorphisms of a finite-dimensional space has generalized eigenspaces spanning the space, then their simultaneous generalized eigenspaces span it](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Eigenspace/Pi.html#Module.End.iSup_iInf_maxGenEigenspace_eq_top_of_iSup_maxGenEigenspace_eq_top_of_commute).
Mathlib does not state that a representation of a finite abelian group splits into
one-dimensional pieces or is diagonalizable in a single basis, does not identify the irreducible
representations up to isomorphism with the characters, and does not prove the converse
characterization of abelian groups.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Representation](../../../overview/general-algebra/representation-theory/representation.md)
- [Irreducible representation](../../linear-algebra/linear-representations/irreducible-representation.md)
- [Group morphism](../../../overview/general-algebra/group-theory/part-01/group-morphism.md)
- [Algebraically closed field](../../../overview/general-algebra/field-theory/algebraically-closed-field.md)

## Proof depends on

- [Schur's lemma (Linear representations)](../../linear-algebra/linear-representations/schurs-lemma.md)
- [Maschke theorem](maschke-theorem.md)
- [Structure of finitely generated abelian groups](../../../overview/general-algebra/group-theory/part-02/structure-of-finitely-generated-abelian-groups.md)
- [Cyclic group](../../../overview/general-algebra/group-theory/part-01/cyclic-group.md)

## Sources

- [Mathlib undergraduate list: Group Theory › Representation theory of finite groups](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L112)
- [Reference given by Mathlib's undergraduate list](https://proofwiki.org/wiki/Irreducible_Representations_of_Abelian_Group)
