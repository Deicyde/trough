The theorem on the **orthonormal basis of irreducible characters** is the central
theorem of the character theory of finite groups: for a finite [group](trough:Group) $G$, the
[characters](trough:FDRep.character) of the
[irreducible](trough:Representation.IsIrreducible) complex representations of $G$,
one for each isomorphism class, form an orthonormal basis of the space of
class functions
on $G$. Orthonormality means that irreducible representations can be told apart,
and multiplicities computed, by evaluating sums over the group; completeness means
that they span the class functions. Together the two parts show that there are
exactly as many isomorphism classes of irreducible representations as
[conjugacy classes](trough:ConjClasses). Together they reduce much of the study of
representations of a finite group to linear algebra with a small table of numbers.

## Statement

Let $G$ be a finite group and let $\mathcal{C}(G)$ be the complex vector space of
class functions $G \to \mathbb{C}$, that is, functions constant on each conjugacy
class. Equip it with the inner product

$$\langle f_1, f_2 \rangle = \frac{1}{|G|} \sum_{g \in G} f_1(g)\,\overline{f_2(g)}.$$

The character of a finite-dimensional representation $\rho \colon G \to \mathrm{GL}(V)$
is $\chi_V(g) = \operatorname{tr} \rho(g)$, and it
is a class function. Let $V_1, \dots, V_r$ be a set of
representatives of the isomorphism classes of irreducible complex representations
of $G$, with characters $\chi_1, \dots, \chi_r$. The theorem has two parts.

1. **Orthonormality.** $\langle \chi_i, \chi_j \rangle = 1$ if $i = j$ and $0$
   otherwise.
2. **Completeness.** $\chi_1, \dots, \chi_r$ span $\mathcal{C}(G)$.

Since the eigenvalues of each $\rho(g)$ are roots of unity, $\overline{\chi(g)} = \chi(g^{-1})$,
and the first part can be written without complex conjugation. In that form it
holds over any algebraically closed field $k$ in which $|G|$ is invertible: for
irreducible finite-dimensional representations $V$ and $W$ of $G$ over $k$,
the sum $\frac{1}{|G|}\sum_{g} \chi_V(g)\,\chi_W(g^{-1})$ is $1$ if $V \cong W$
and $0$ otherwise. These are the
[orthogonality relations](trough:FDRep.char_orthonormal).

## Examples

- **The symmetric group $S_3$.** It has three conjugacy classes (the identity, the
  three transpositions, the two $3$-cycles) and three irreducible representations:
  the trivial one, the sign, and a $2$-dimensional one from the action on the plane
  $x_1 + x_2 + x_3 = 0$. On the three classes their characters take the values
  $(1, 1, 1)$, $(1, -1, 1)$ and $(2, 0, -1)$. For the last one,
  $\langle \chi, \chi \rangle = \frac{1}{6}(4 + 3 \cdot 0 + 2 \cdot 1) = 1$, and
  its inner product with the trivial character is $\frac{1}{6}(2 + 0 - 2) = 0$.
- **Abelian groups.** Over an algebraically closed field,
  every irreducible finite-dimensional representation of a commutative group is
  one-dimensional,
  so the irreducible characters of a finite abelian group are its homomorphisms
  to the nonzero complex numbers, which make up the
  dual group.
  Every function is a class function here, and the theorem says these characters
  form an orthonormal basis of all functions $G \to \mathbb{C}$. For a finite abelian
  group written additively,
  two characters have normalized inner product $1$ if they are equal and $0$
  otherwise,
  the complex characters form a basis of the functions on the
  group, whose
  vectors are the characters themselves, and
  there are exactly as many characters as elements.

## Consequences

- **Number of irreducible representations.** The indicator functions of the
  conjugacy classes form a basis of $\mathcal{C}(G)$, so $r$ equals the number of
  conjugacy classes of $G$.
- **Multiplicities.** By complete reducibility, every finite-dimensional complex representation is
  $V \cong V_1^{m_1} \oplus \dots \oplus V_r^{m_r}$, so $\chi_V = \sum_i m_i \chi_i$ and
  $m_i = \langle \chi_V, \chi_i \rangle$. Hence a representation is determined up to
  isomorphism by its character; the converse, that
  isomorphic representations have the same character, holds
  over any field.
- **Irreducibility test.** $\langle \chi_V, \chi_V \rangle = \sum_i m_i^2$, so $V$ is
  irreducible exactly when this number is $1$. Over an algebraically closed field of
  characteristic zero,
  $V$ is irreducible if and only if $\sum_g \chi_V(g)\,\chi_V(g^{-1}) = |G|$.
- **Sum of squares.** The regular representation has character $|G|$ at the
  identity and $0$ elsewhere, so $V_i$ occurs in it $\dim V_i$ times, and
  $|G| = \sum_i (\dim V_i)^2$.
- **Expansion of class functions.** Every class function is
  $f = \sum_i \langle f, \chi_i \rangle\, \chi_i$.
- **Column orthogonality.** Since the character table is a square matrix whose rows
  are orthonormal for the weighted inner product, its columns are orthogonal too:
  $\sum_i \chi_i(g)\,\overline{\chi_i(h)}$ equals the order of the centralizer of $g$
  when $g$ and $h$ are conjugate, and $0$ otherwise.

## Proof

For a finite-dimensional representation over a field $k$ in which $|G|$ is
invertible, the average of its character over $G$
equals the dimension of the subspace of invariant vectors,
read as an element of $k$ (in positive characteristic, only its residue modulo the
characteristic), because $\frac{1}{|G|}\sum_g \rho(g)$ is a projection onto that
subspace. For finite-dimensional representations $V$ and $W$, apply this to the
representation on linear maps from $V$ to $W$, whose character is
$\chi_V(g^{-1})\chi_W(g)$ and whose invariants are the maps commuting with $G$. The
result, again as an element of $k$, is
$\frac{1}{|G|}\sum_g \chi_W(g)\,\chi_V(g^{-1}) = \dim \operatorname{Hom}_G(V, W)$.
For irreducible $V$ and $W$ over an algebraically closed field,
[Schur's lemma](trough:FDRep.finrank_hom_simple_simple) says that
this dimension is $1$ if $V \cong W$ and $0$ otherwise,
which proves orthonormality.

For completeness, let $f$ be a class function orthogonal to every $\chi_i$. On an
irreducible representation $V$, the operator $T = \sum_g \overline{f(g)}\,\rho(g)$
commutes with every $\rho(h)$, because $f$ is constant on conjugacy classes. By
Schur's lemma $T$ is a scalar $\lambda$, and taking traces gives
$\lambda \dim V = |G|\,\overline{\langle f, \chi_V \rangle} = 0$, so $T = 0$. By
[Maschke's theorem](trough:MonoidAlgebra.Submodule.exists_isCompl) every
representation is a direct sum of irreducible ones, so $T = 0$ on the regular
representation as well. Applied to the basis vector of the identity element, it
gives $\sum_g \overline{f(g)}\, g = 0$, so $f = 0$.

## Related concepts

For abelian groups, expanding a function in the basis of characters is the
Fourier transform for finite abelian groups;
the expansion of class functions in irreducible characters extends it to all
finite groups. Under the identification of functions with elements of the group
algebra, class functions are its centre, so the number of irreducible
representations is also the dimension of the centre of the group algebra.

## In Mathlib

Mathlib has characters as plain functions from the group to the field, both for
bundled finite-dimensional representations, where irreducibility is simplicity in
the category of representations, and for unbundled ones. It proves the
orthogonality relations over any algebraically closed field in which the order of
the group is invertible, stated with $\chi_W(g^{-1})$ in place of a complex
conjugate, together with the formula for the pairing of two characters as the
dimension of a space of intertwining maps, which needs only that the order be
invertible, and the irreducibility test over an algebraically closed field of characteristic
zero. For finite abelian
groups, written additively, it proves the abelian case for homomorphisms into the
complex numbers, with the normalized inner product on all functions, but it does
not connect these homomorphisms to irreducible representations.
What it lacks is the theorem for finite groups that are not abelian: it has no space
of class functions and no inner product on one, no statement that the irreducible
characters span the class functions or form a basis of them, no count of
irreducible representations by conjugacy classes, no sum of squares formula, no
column orthogonality, and no proof that $\chi(g^{-1})$ is the complex conjugate of
$\chi(g)$.

## Depends on

- [Character](trough:FDRep.character)
- [Irreducible representation](trough:Representation.IsIrreducible)
- [Orthonormal bases](trough:maximal_orthonormal_iff_basis_of_finiteDimensional)

## Proof depends on

- [Schur's lemma](trough:FDRep.finrank_hom_simple_simple)
- [Maschke theorem](trough:MonoidAlgebra.Submodule.exists_isCompl)
