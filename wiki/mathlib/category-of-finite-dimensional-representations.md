---
article_id: af_569296c9931c573d2508ce31
concept: FDRep
---

The **category of finite-dimensional representations** of a [group](trough:Group) $G$ over a
[field](trough:Field) $k$ has as objects the finite-dimensional
[representations](trough:Representation) of $G$ over $k$, and as morphisms the linear maps that
commute with the action of $G$. Treating representations as the objects of a
[category](trough:CategoryTheory.Category), rather than one at a time, is the natural setting for
the main tools of representation theory: Schur's lemma is a statement about its morphisms,
semisimplicity is a statement about its subobjects, and tensor products and duals of
representations make it a rigid monoidal category.

## Definition

Let $k$ be a field and $G$ a group. An object of the
[category of finite-dimensional representations](lean:FDRep), often written
$\mathrm{FDRep}_k(G)$, is a pair $(V, \rho_V)$ where $V$ is a
[finite-dimensional](trough:FiniteDimensional) vector space over $k$ and
$\rho_V \colon G \to \mathrm{GL}(V)$ is a group homomorphism. A morphism
$f \colon (V, \rho_V) \to (W, \rho_W)$ is a [linear map](trough:LinearMap) $f \colon V \to W$ that
is equivariant, meaning

$$f \circ \rho_V(g) = \rho_W(g) \circ f \quad \text{for every } g \in G.$$

Composition and identities are those of linear maps, and the composite of two equivariant maps is
again equivariant. Two representations are isomorphic in this category exactly when there is a
linear isomorphism between them that intertwines the two actions. The same definition makes sense
for a monoid $G$, with $\rho_V$ a monoid homomorphism into the endomorphisms of $V$; for a group
the maps $\rho_V(g)$ are then automatically invertible, since
$\rho_V(g)\rho_V(g^{-1}) = \rho_V(g^{-1})\rho_V(g) = \rho_V(1)$ is the identity.

## Examples

- The trivial representation $k$, on which every element of $G$ acts as the identity, is the
  unit for the tensor product described below.
- For a finite group $G$, the group algebra $k[G]$ with $G$ acting by left multiplication on basis
  vectors is the regular representation, of dimension $|G|$. More generally, an action of $G$ on a
  finite set $X$ gives a permutation representation on the vector space with basis $X$.
- The sign of a permutation gives a one-dimensional representation of the symmetric group $S_n$,
  on which $\sigma$ acts as multiplication by $\operatorname{sgn}(\sigma)$.
- For the cyclic group of order $n$ with generator $g$, and a primitive $n$-th root of unity
  $\zeta \in \mathbb{C}$, each $j = 0, 1, \dots, n-1$ gives a one-dimensional complex
  representation with $g$ acting as multiplication by $\zeta^j$; no two of these are isomorphic.

## Properties

The morphisms between two objects form a finite-dimensional vector space, and composition is
bilinear, so the category is $k$-linear. It has kernels, cokernels and all finite limits, and it is
an [abelian category](trough:CategoryTheory.Abelian).

**Tensor products and duals.** The tensor product $V \otimes W$ carries the action
$g \mapsto \rho_V(g) \otimes \rho_W(g)$, which makes the category a
[monoidal category](trough:CategoryTheory.MonoidalCategory) with the trivial representation as
unit. The [dual space](trough:Module.Dual) $V^*$ is a representation with $g$ acting by the
transpose of $\rho_V(g^{-1})$, and the space of all linear maps from $V$ to $W$, with $g$ acting by
$\varphi \mapsto \rho_W(g) \circ \varphi \circ \rho_V(g)^{-1}$,
[is isomorphic as a representation to $V^* \otimes W$](lean:FDRep.dualTensorIsoLinHom).
The vectors of this space fixed by $G$ are exactly the morphisms from $V$ to $W$.

**Simple objects.** The simple objects of the category are the
[irreducible representations](trough:Representation.IsIrreducible). When $k$ is
[algebraically closed](trough:IsAlgClosed), [Schur's lemma](trough:FDRep.finrank_hom_simple_simple)
says that for simple objects $V$ and $W$
[the space of morphisms from $V$ to $W$ has dimension $1$ if $V \cong W$ and $0$ otherwise](lean:FDRep.finrank_hom_simple_simple).

**Semisimplicity.** Suppose now that $G$ is finite and that the characteristic of $k$ does not
divide $|G|$, so that $|G|$ is invertible in $k$. [Maschke's theorem](trough:MonoidAlgebra.Submodule.exists_isCompl)
says that [every submodule of a module over the group algebra $k[G]$ has a complementary submodule](lean:MonoidAlgebra.Submodule.exists_isCompl).
Applied to representations, it shows that every invariant subspace has an invariant complement,
so every object of the category is a direct sum of simple objects and every short exact sequence
splits. If $k$ is moreover algebraically closed, then
[a representation $V$ is simple exactly when its endomorphisms form a one-dimensional space](lean:FDRep.simple_iff_end_is_rank_one).

**Characters.** The [character](trough:FDRep.character) of $V$ is the function
[$\chi_V(g) = \operatorname{tr} \rho_V(g)$](lean:FDRep.character) on $G$.
[Isomorphic representations have the same character](lean:FDRep.char_iso), and
[the character of $V \otimes W$ is the product $\chi_V \chi_W$](lean:FDRep.char_tensor). For a
finite group whose order is invertible in $k$,
[averaging characters computes dimensions of morphism spaces](lean:FDRep.scalar_product_char_eq_finrank_equivariant):

$$\frac{1}{|G|} \sum_{g \in G} \chi_W(g)\,\chi_V(g^{-1}) = \dim_k \operatorname{Hom}_G(V, W),$$

where $\operatorname{Hom}_G(V, W)$ is the space of morphisms from $V$ to $W$ in the category,
that is, the equivariant linear maps, and the right side is read as an element of $k$. Combined with Schur's lemma over an
algebraically closed field, this gives the
[orthogonality of characters](trough:FDRep.char_orthonormal):
[for simple $V$ and $W$ the average of $\chi_V(g)\chi_W(g^{-1})$ over $G$ is $1$ if $V \cong W$ and $0$ otherwise](lean:FDRep.char_orthonormal).

## Related concepts

The category of all representations of $G$ over $k$, without the finiteness condition, contains
this one as a full subcategory. It is equivalent to the category of modules over the group algebra
$k[G]$, a special case of the [category of modules over a ring](trough:ModuleCat). A finite
group can be recovered from its category of finite-dimensional representations together with the
tensor product and the [functor](trough:CategoryTheory.Functor) that forgets the action, as the
group of automorphisms of that functor compatible with tensor products; this is the starting point
of Tannakian reconstruction.

## In Mathlib

Mathlib defines the category for an arbitrary ring $R$ and monoid $G$, as the category of actions
of $G$ on finitely generated $R$-modules; over a field, finitely generated modules are exactly the
finite-dimensional vector spaces. An object is bundled: it carries its module and the monoid
homomorphism from $G$ to the endomorphisms of that module, which can be recovered from it, and over
a commutative ring a representation on a finitely generated module
[can be packaged as an object](lean:FDRep.of). Over a commutative ring the
[morphisms between two objects are, as a module, the same as the morphisms between them in the category of all representations](lean:FDRep.forget₂HomLinearEquiv).
Irreducible representations are the simple objects in the categorical sense, and the hypothesis
on the characteristic is stated as invertibility (or nonvanishing) of $|G|$ in $k$. When $R$ is a
field and $G$ a group, Mathlib records that every object has a dual through a right rigid
structure, and the isomorphism between linear maps and $V^* \otimes W$ above is a separate result.

## Depends on

- [Representation](trough:Representation)
- [Category](trough:CategoryTheory.Category)
- [Finite-dimensionality](trough:FiniteDimensional)
- [Linear map](trough:LinearMap)
