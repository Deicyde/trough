**Maschke's theorem** says that a [representation](trough:Representation) of a finite
[group](trough:Group) $G$ over a [field](trough:Field) $k$ whose
[characteristic](trough:ringChar) does not divide the order of $G$ splits along every
invariant subspace: each subrepresentation has an invariant complement. It is the
starting point of the representation theory of finite groups. It reduces the study of
finite-dimensional representations to that of
[irreducible representations](trough:Representation.IsIrreducible), and so makes the theory
of [characters](trough:FDRep.character) and the structure of the group algebra accessible.

## Statement

Let $G$ be a finite group of order $|G|$ and $k$ a field in which $|G| \neq 0$, that is,
whose characteristic is $0$ or a prime not dividing $|G|$. Let $V$ be a vector space over
$k$ on which $G$ acts by linear maps, and let $W \subseteq V$ be a subspace with
$gW \subseteq W$ for all $g \in G$. Then there is a subspace $U \subseteq V$, also stable
under every $g \in G$, such that

$$V = W \oplus U.$$

In the language of modules: a representation of $G$ over $k$ is the same thing as a
[module](trough:Module) over the group algebra $k[G]$, the vector space with basis $G$ and
multiplication extending that of $G$, and invariant subspaces are its submodules. Under the
same hypotheses on $G$ and $k$, the theorem says that
every submodule of a $k[G]$-module has a complementary submodule:
a submodule meeting it only in $0$ and spanning the whole module together with it. A module
with this property is called semisimple.

## Proof

Choose any complementary subspace $U_0$ of $W$, ignoring the group action; this is possible
because every subspace of a vector space has a complement.
Let $\pi \colon V \to W$ be the projection onto $W$ along $U_0$. It is linear and fixes $W$
pointwise, but need not commute with the action of $G$. Average it over the group:

$$\pi'(v) = \frac{1}{|G|} \sum_{g \in G} g\,\pi(g^{-1} v).$$

The division is allowed because $|G| \neq 0$ in $k$. Reindexing the sum shows
$\pi'(hv) = h\,\pi'(v)$ for every $h \in G$. Since $W$ is invariant, $\pi'$ takes values in
$W$, and each term of the sum fixes every $w \in W$, so $\pi'(w) = w$. Thus $\pi'$ is a
projection onto $W$ that commutes with $G$, and its [kernel](trough:LinearMap.ker)
$U = \ker \pi'$ is an invariant complement of $W$.

The same computation works over any commutative ring $k$ in which $|G|$ is invertible: if a
$k[G]$-linear map has a $k$-linear left inverse, then
averaging that left inverse over $G$ gives a $k[G]$-linear left inverse.
Over a field, where $k$-linear left inverses of injective maps always exist, it follows that
every injective homomorphism of $k[G]$-modules has a left inverse that is itself a homomorphism of $k[G]$-modules.

## Examples

- **Swapping two coordinates.** Let the group of order $2$ act on $k^2$ by exchanging the
  coordinates. The line spanned by $(1, 1)$ is invariant. If the characteristic of $k$ is
  not $2$, the line spanned by $(1, -1)$ is an invariant complement. In characteristic $2$
  these two lines coincide, the line spanned by $(1, 1)$ is the only invariant line, and it
  has no invariant complement.
- **A modular example.** Over a field of prime characteristic $p$, the cyclic group
  of order $p$ acts on $k^2$ with a generator acting by the matrix with rows $(1, 1)$ and
  $(0, 1)$. The line spanned by the first basis vector is the only invariant line, so it has
  no invariant complement. The hypothesis on the characteristic cannot be dropped.
- **Infinite groups.** The same matrix defines an action of the integers on $\mathbb{C}^2$,
  with the same unique invariant line. Finiteness of the group cannot be dropped either, even
  in characteristic $0$.

## Consequences

- **Complete reducibility.** Under the hypotheses of the theorem every $k[G]$-module is
  semisimple, and a semisimple module is
  the sum of an independent family of simple submodules
  (nonzero submodules whose only submodules are $0$ and themselves), that is, their [direct sum](trough:DirectSum.IsInternal). Since
  a representation is irreducible exactly when the corresponding $k[G]$-module is simple,
  every finite-dimensional representation of $G$ is a direct sum of finitely many
  irreducible representations.
- **Structure of the group algebra.** Taking $V = k[G]$ shows that $k[G]$ is a semisimple
  ring. When $k$ is moreover algebraically closed, the
  [Wedderburn–Artin theorem](trough:IsSimpleRing.exists_algEquiv_matrix_divisionRing) shows that
  this finite-dimensional semisimple algebra is isomorphic to a product of full matrix algebras over $k$.
  Comparing dimensions writes $|G|$ as a sum of squares of the sizes of these matrix
  algebras, which are the dimensions of the irreducible representations.
- **Converse.** If the characteristic of $k$ divides $|G|$, then $k[G]$ is not semisimple:
  the sum $N$ of all elements of $G$ satisfies $N^2 = |G|\,N = 0$, so it spans a nonzero
  nilpotent ideal, which a semisimple ring cannot have.

## Related concepts

Together with [Schur's lemma](trough:FDRep.finrank_hom_simple_simple), Maschke's theorem is
the basis of the character theory of finite groups: over the complex numbers every
finite-dimensional representation of a finite group decomposes into irreducible ones, whose
multiplicities can be read off from its character. For finite-dimensional complex
representations, an alternative proof averages an inner product instead of a projection, which makes every element of $G$
act unitarily, and then takes the [orthogonal complement](trough:Submodule.orthogonal) of $W$.
The same averaging idea, with a sum replaced by an integral against an invariant measure,
proves complete reducibility for finite-dimensional continuous complex representations of
compact groups.

## In Mathlib

Mathlib states the theorem for an arbitrary module over the group algebra, with no
finite-dimensionality assumption and no separately given vector space structure. The group
algebra is the monoid algebra of finitely supported functions from $G$ to $k$. The
hypothesis on the characteristic is phrased as the image of the natural number $|G|$ in $k$
being nonzero, which for a field is the same as the characteristic not dividing $|G|$, and
a complement is expressed in the lattice of submodules: the two submodules have zero
intersection and their sum is everything. The averaging step is proved over any
commutative ring in which $|G|$ is invertible. The consequences that every $k[G]$-module is
semisimple, that $k[G]$ is a semisimple ring, and that
every representation of $G$ over $k$ is semisimple are recorded as instances derived from
the theorem.

## Depends on

- [Group](trough:Group)
- [Field](trough:Field)
- [Characteristic of a ring](trough:ringChar)
- [Representation](trough:Representation)
- [Complementary subspaces](trough:Submodule.exists_isCompl)
- [Module](trough:Module)

## Proof depends on

- [Linear map](trough:LinearMap)
- [Kernel of a linear map](trough:LinearMap.ker)
