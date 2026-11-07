The **orthogonality of characters** is the theorem that the
[characters](trough:FDRep.character) of the
[irreducible representations](trough:Representation.IsIrreducible) of a finite
[group](trough:Group) over the complex numbers (more generally, over an
algebraically closed field whose characteristic does not divide the order of
the group) form an orthonormal family for a natural pairing of functions on the
group. It is the basic computational tool of character theory:
it lets one decide whether a representation is irreducible, find how often each
irreducible representation occurs in a given one, and bound the number of
irreducible representations, all from a finite table of numbers.

## Statement

Let $G$ be a finite group and $k$ an [algebraically closed field](trough:IsAlgClosed)
whose [characteristic](trough:ringChar) does not divide the order $|G|$, so that
$|G|$ is invertible in $k$; the complex numbers are the main example. For
functions $\varphi, \psi \colon G \to k$ put

$$\langle \varphi, \psi \rangle = \frac{1}{|G|} \sum_{g \in G} \varphi(g)\,\psi(g^{-1}).$$

The substitution $g \mapsto g^{-1}$ shows that this pairing is symmetric. If $V$
and $W$ are irreducible finite-dimensional
[representations](trough:Representation) of $G$ over $k$, with characters
$\chi_V$ and $\chi_W$, then
$\langle \chi_V, \chi_W \rangle$ equals $1$ if $V$ and $W$ are isomorphic and $0$ otherwise.

Over the complex numbers the pairing can be written with complex conjugation.
Each $\rho(g)$ has finite order, so its eigenvalues are roots of unity, and the
eigenvalues of $\rho(g^{-1})$ are their inverses, which are their conjugates.
Hence $\chi(g^{-1}) = \overline{\chi(g)}$, and the theorem says that the
irreducible characters are orthonormal for the Hermitian inner product
$\frac{1}{|G|}\sum_g \varphi(g)\overline{\psi(g)}$, which explains the name.

## Examples

- **Cyclic groups.** Let $G$ be [cyclic](trough:IsCyclic) of order $n$ with
  generator $g$, and let $\zeta = e^{2\pi i/n}$. For each $j = 0, \dots, n-1$ the
  rule $g^m \mapsto \zeta^{jm}$ is a one-dimensional representation, hence
  irreducible, and its character is $\chi_j(g^m) = \zeta^{jm}$. Then
  $\langle \chi_j, \chi_l \rangle = \frac1n \sum_{m=0}^{n-1} \zeta^{(j-l)m}$, a
  geometric sum that equals $1$ when $j = l$ and $0$ otherwise, because
  $\zeta^{j-l}$ is then an $n$th root of unity different from $1$.
- **The symmetric group $S_3$.** Over $\mathbb{C}$ it has three irreducible
  representations: the trivial one, the [sign](trough:Equiv.Perm.sign), and the
  two-dimensional standard representation on the vectors in $\mathbb{C}^3$ with
  coordinate sum $0$. On the identity, the three transpositions and the two
  3-cycles their characters take the values $(1,1,1)$, $(1,-1,1)$ and $(2,0,-1)$.
  Every element of $S_3$ is conjugate to its inverse, so all character values
  are real and $\chi(g^{-1}) = \chi(g)$. For the standard character,
  $\langle \chi, \chi \rangle = \frac16(4 + 3 \cdot 0 + 2 \cdot 1) = 1$, while its
  pairing with the trivial character is $\frac16(2 + 0 - 2) = 0$.

## Consequences

- **The general formula.** For finite-dimensional representations $V$ and $W$,
  not necessarily irreducible, and any field $k$ in which $|G|$ is invertible,
  $\langle \chi_W, \chi_V \rangle$ is the dimension of the space of $G$-equivariant linear maps from $V$ to $W$, read as an element of $k$.
  Taking $V$ to be the trivial one-dimensional representation, whose character
  is constantly $1$, the average of $\chi_W$ over $G$ is
  the dimension of the subspace of vectors fixed by $G$,
  again read in $k$.
- **Linear independence.** Under the hypotheses of the statement, characters
  are constant on
  [conjugacy classes](trough:ConjClasses), since
  $\chi_V(hgh^{-1}) = \chi_V(g)$ for all $g, h$. If
  $\chi_1, \dots, \chi_r$ are the characters of pairwise non-isomorphic
  irreducible representations and $\sum_i a_i \chi_i = 0$, pairing with $\chi_j$
  gives $a_j = 0$. So these characters are linearly independent in the space of
  class functions,
  whose dimension is the number of conjugacy classes, and $G$ has at most that
  many irreducible representations up to isomorphism.
- **Multiplicities.** Assume moreover that $k$ has characteristic $0$. By
  [Maschke's theorem](trough:MonoidAlgebra.Submodule.exists_isCompl) every
  finite-dimensional representation $V$ is a direct sum
  $W_1^{m_1} \oplus \cdots \oplus W_r^{m_r}$, where $W_1, \dots, W_r$ is a full
  set of pairwise non-isomorphic irreducible representations and some $m_j$ may
  be $0$, and orthogonality gives $m_j = \langle \chi_V, \chi_{W_j} \rangle$
  and $\langle \chi_V, \chi_V \rangle = \sum_j m_j^2$. Hence $V$ is irreducible
  exactly when $\langle \chi_V, \chi_V \rangle = 1$. The character determines
  every multiplicity $m_j$, hence the isomorphism class, so two representations
  with the same character are isomorphic. For example, the permutation representation
  of $S_3$ on $\mathbb{C}^3$ has character $(3, 1, 0)$, the number of fixed
  points, so it is the trivial representation plus the standard one.

## Proof

There are three steps. First, for any finite-dimensional representation
$\rho$ on $U$, the operator $e = \frac{1}{|G|}\sum_g \rho(g)$ is a projection of
$U$ onto the subspace $U^G$ of fixed vectors. The trace of a projection is the
dimension of its image (read in $k$), so the average of $\chi_U$ equals $\dim U^G$.

Second, the space of all linear maps from $W$ to $V$ is a representation, with
$g$ acting by $f \mapsto \rho_V(g) \circ f \circ \rho_W(g)^{-1}$. Its
character at $g$ is $\chi_W(g^{-1})\,\chi_V(g)$, and its
fixed vectors are exactly the $G$-equivariant maps. The first step therefore
gives $\langle \chi_V, \chi_W \rangle = \dim \operatorname{Hom}_G(W, V)$.

Third, [Schur's lemma](trough:FDRep.finrank_hom_simple_simple) over an
algebraically closed field says that for irreducible $V$ and $W$
the space of $G$-equivariant maps between them has dimension $1$ if they are isomorphic and $0$ otherwise.
Combining the second and third steps, $\langle \chi_V, \chi_W \rangle = \dim \operatorname{Hom}_G(W, V)$
is $1$ if $W \cong V$, equivalently $V \cong W$, and $0$ otherwise.

## Related concepts

The irreducible characters are not only orthonormal but span the space of class
functions, so they form an
orthonormal basis of the class functions,
and the number of irreducible representations equals the number of conjugacy
classes. Reading the character table by columns instead of rows gives the second
orthogonality relation: over $\mathbb{C}$, the sum of
$\chi(g)\overline{\chi(h)}$ over all irreducible characters $\chi$ is the order of
the centralizer of $g$ when $g$ and $h$ are conjugate and $0$ otherwise.

## In Mathlib

Mathlib states the theorem for the bundled
[category of finite-dimensional representations](trough:FDRep) of a group over a
field. Irreducibility is expressed as being a simple object of that category,
isomorphism means isomorphism in the category, and the condition on the
characteristic is an assumption that the order of the group is invertible in
the field. The pairing is the one above with $g^{-1}$, with no complex
conjugation, so it makes sense over any field, and the two sides are equal as
elements of the field, the right side being its $1$ or $0$. Mathlib also has
a version for irreducible representations on modules that are not bundled into a category,
where finite-dimensionality is not assumed but follows from irreducibility. The
general formula and the fixed-vector formula do not need the field to be
algebraically closed; their right sides are dimensions cast into the field, so
in positive characteristic they determine a dimension only modulo the
characteristic.

## Depends on

- [Character](trough:FDRep.character)
- [Representation](trough:Representation)
- [Irreducible representation](trough:Representation.IsIrreducible)
- [Algebraically closed field](trough:IsAlgClosed)
- [Characteristic of a ring](trough:ringChar)

## Proof depends on

- [Schur's lemma](trough:FDRep.finrank_hom_simple_simple)
