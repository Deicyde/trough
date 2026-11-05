---
article_id: af_68c2aa70e2727097e1be889e
concept: Representation
---

A **representation** of a [group](trough:Group) $G$ is a way of letting $G$ act on a
vector space by linear maps, compatibly with the group multiplication. It turns
questions about an abstract group into questions of linear algebra, where matrices,
traces and eigenvalues are available. Representations are a main tool for studying
finite groups and for the symmetry arguments of number theory, geometry and physics.

## Definition

Let $k$ be a [field](trough:Field), $G$ a group and $V$ a vector space over $k$. A
[representation of $G$ on $V$](lean:Representation) is a map $\rho$ assigning to each
$g \in G$ a [linear map](trough:LinearMap) $\rho(g) \colon V \to V$ such that

$$\rho(gh) = \rho(g)\,\rho(h) \quad \text{for all } g, h \in G, \qquad \rho(e) = \mathrm{id}_V,$$

where $e$ is the identity of $G$. In other words, $\rho$ is a
[homomorphism](trough:MonoidHom) from $G$ to the linear maps of $V$ under composition.
Since $\rho(g)\rho(g^{-1}) = \rho(g^{-1})\rho(g) = \mathrm{id}_V$,
[each $\rho(g)$ is a bijection](lean:Representation.apply_bijective), so $\rho$ can be
regarded as [a homomorphism from $G$ to the group of invertible linear maps of
$V$](lean:Representation.asGroupHom); conversely, any such homomorphism is a
representation. One often writes $g \cdot v$ for $\rho(g)v$, and calls
$V$ itself the representation when $\rho$ is understood. The dimension of $V$ is the
degree of the representation. If $V$ has finite dimension $n$, a choice of basis turns
each $\rho(g)$ into an invertible matrix, and $\rho$ into a homomorphism from $G$ to the
[general linear group](trough:Matrix.GeneralLinearGroup) of $n \times n$ matrices over $k$.

If $\sigma$ is a representation of $G$ on $W$, a linear map $f \colon V \to W$ is an
[intertwining map](lean:Representation.IntertwiningMap) when
$f(\rho(g)v) = \sigma(g)f(v)$ for all $g$ and $v$. Two representations are
[equivalent](lean:Representation.Equiv) when a bijective intertwining map joins them;
equivalent representations are regarded as the same.

## Examples

- **The trivial representation.** [Every $g$ acts as the identity](lean:Representation.trivial).
- **One-dimensional representations.** A representation on $k$ itself is a homomorphism
  from $G$ to the nonzero elements of $k$ under multiplication. The
  [signature](trough:Equiv.Perm.sign) of a permutation gives such a representation of
  the symmetric group, with each permutation acting by $\pm 1$. For a
  [cyclic group](trough:IsCyclic) of order $n$ with generator $g$ and an $n$-th root of
  unity $\zeta$ in $\mathbb{C}$, letting $g^m$ act by multiplication by $\zeta^m$ gives a
  representation on $\mathbb{C}$.
- **Permutation representations.** If $G$ [acts](trough:MulAction) on a set $X$, let
  $k[X]$ be the vector space with basis $\{e_x : x \in X\}$. This gives a
  [permutation representation](lean:Representation.ofMulAction), in which
  [$g$ sends $e_x$ to $e_{gx}$](lean:Representation.ofMulAction_single).
  The case $X = G$, with $G$ acting on itself by left multiplication, is the
  [regular representation](lean:Representation.leftRegular) on the group algebra $k[G]$.

## Constructions

A subspace $W \subseteq V$ with $\rho(g)W \subseteq W$ for all $g$ is a
[subrepresentation](lean:Subrepresentation), and
[restricting each $\rho(g)$ to $W$ gives a representation of $G$ on $W$](lean:Representation.subrepresentation).
Representations of $G$ can be combined: there are
[direct sums](lean:Representation.directSum), on which $G$ acts in each summand;
[tensor products](lean:Representation.tprod), on which $g$ acts by
$\rho(g) \otimes \sigma(g)$ (see [tensor product](trough:TensorProduct)); and
[duals](lean:Representation.dual), on which $g$ acts on the
[dual space](trough:Module.Dual) by the transpose of $\rho(g^{-1})$.

## Irreducible representations

A representation is [irreducible](trough:Representation.IsIrreducible) when
[it is nonzero and its only subrepresentations are $0$ and the whole space](lean:Representation.IsIrreducible).
Irreducible representations are the building blocks of the theory.

- **Schur's lemma.** [An intertwining map between irreducible representations is either
  zero or bijective](lean:Representation.IsIrreducible.bijective_or_eq_zero). If $k$ is
  [algebraically closed](trough:IsAlgClosed) and $V$ is irreducible and
  finite-dimensional, then [the intertwining maps from $V$ to itself form a
  one-dimensional space](lean:Representation.IsIrreducible.finrank_intertwiningMap_self),
  so each is a scalar multiple of the identity (see [Schur's lemma](trough:FDRep.finrank_hom_simple_simple)).
- **Commutative groups.** Over an algebraically closed field,
  [every finite-dimensional irreducible representation of a commutative group is
  one-dimensional](lean:Representation.IsIrreducible.finrank_eq_one_of_isMulCommutative).
- **[Maschke's theorem](trough:MonoidAlgebra.Submodule.exists_isCompl).** If $G$ is finite
  and $|G| \neq 0$ in $k$, every subrepresentation has a complementary subrepresentation,
  so every finite-dimensional representation is a direct sum of irreducible ones.

Both hypotheses of Maschke's theorem matter. Over a field of prime characteristic $p$,
the cyclic group of order $p$ acts on $k^2$ with generator acting by
$(x, y) \mapsto (x + y, y)$; the line $y = 0$ is invariant, but it is the only invariant
line, so it has no invariant complement. The same matrix gives a representation of the
integers on $\mathbb{C}^2$ with the same defect.

## Modules over the group algebra

A representation $\rho$ extends linearly to
[an algebra homomorphism from the group algebra $k[G]$ to the linear maps of $V$](lean:Representation.asAlgebraHom),
which makes $V$ a module over $k[G]$. Conversely,
[a $k[G]$-module $M$ is a representation of $G$, with $g$ acting as multiplication by the basis element $g$](lean:Representation.ofModule).
Under this dictionary [subrepresentations are submodules](lean:Subrepresentation.subrepresentationSubmoduleOrderIso), and
[a representation is irreducible exactly when its module is simple](lean:Representation.irreducible_iff_isSimpleModule_asModule),
so representation theory becomes part of [module](trough:Module) theory. In the module
form, Maschke's theorem says that
[every submodule of a $k[G]$-module has a complementary submodule](lean:MonoidAlgebra.Submodule.exists_isCompl),
for $G$ finite and $|G| \neq 0$ in $k$.

## Related concepts

The [character](trough:FDRep.character) of a finite-dimensional representation is the
function $g \mapsto \operatorname{tr} \rho(g)$; for finite groups over $\mathbb{C}$ it
determines the representation up to equivalence, and the
[orthogonality of characters](trough:FDRep.char_orthonormal) organizes the irreducible
ones. Finite-dimensional representations and intertwining maps form a
[category](trough:FDRep). A representation is a [group action](trough:MulAction) by
linear maps; variants require continuity for topological groups, or replace $G$ by a
[Lie algebra](trough:LieAlgebra) or an associative algebra.

## In Mathlib

Mathlib defines a representation for any monoid $G$, any semiring $k$ and any module $V$
over $k$, as a monoid homomorphism from $G$ to the $k$-linear maps of $V$ under
composition. The definition is an abbreviation for this type of homomorphisms rather than
a structure, so $V$ stays a separate parameter; invertibility of each $\rho(g)$ is not
assumed and follows when $G$ is a group. Irreducibility and semisimplicity are stated for
vector spaces over a field. Intertwining maps and equivalences are bundled structures.
The module over the group algebra lives on a separate copy of $V$, so that the original
scalar action of $k$ and the new action of $k[G]$ do not clash; likewise, the
representation built from a $k[G]$-module acts on a copy of that module. Bundled categories of
representations, in which an object packages a module with its representation, sit on
top of this definition, and Maschke's theorem is proved in its module form with the
hypothesis that $|G|$ is nonzero in $k$, from which every such representation is shown to
be semisimple.

## Depends on

- [Group](trough:Group)
- [Field](trough:Field)
- [Module](trough:Module)
- [Linear map](trough:LinearMap)
- [Group morphism](trough:MonoidHom)
