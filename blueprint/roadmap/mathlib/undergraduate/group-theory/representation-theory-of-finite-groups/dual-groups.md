---
article_id: af_c822a925bd9b15894ec09a65
declaration: definition
origin: cited
not_ready: true
---

# Dual groups

The **dual group** of a finite abelian [group](../../../overview/general-algebra/group-theory/part-01/group.md) $G$ is the group $\widehat{G}$ of
its characters: the [homomorphisms](../../../overview/general-algebra/group-theory/part-01/group-morphism.md) from $G$ to the multiplicative group
$\mathbb{C}^\times$ of nonzero complex numbers, multiplied pointwise. A finite abelian group has
exactly as many characters as elements, and it can be recovered from its dual. The dual group is
the setting for [Fourier analysis on finite abelian groups](fourier-transform-for-finite-abelian-groups.md),
for Dirichlet characters in number theory, and for the [representations of abelian groups](representations-of-abelian-groups.md),
whose irreducible complex representations correspond to the characters.

## Definition

Let $G$ be a finite abelian group of order $n$. A **character** of $G$ is a map
$\chi : G \to \mathbb{C}^\times$ with $\chi(gh) = \chi(g)\chi(h)$ for all $g, h \in G$. Since
$g^n = e$ for every $g$, each value $\chi(g)$ satisfies $\chi(g)^n = 1$, so it is an $n$-th
[root of unity](../abelian-group/complex-roots-of-unity.md); in particular $|\chi(g)| = 1$ and
$\chi(g)^{-1} = \overline{\chi(g)}$.

The product of two characters is $(\chi\psi)(g) = \chi(g)\psi(g)$, the identity is the trivial
character $g \mapsto 1$, and the inverse of $\chi$ is $g \mapsto \overline{\chi(g)}$. In general,
[the homomorphisms from a group into a commutative group form a commutative group under pointwise multiplication](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Hom/Instances.html#MonoidHom.instCommGroup); the dual group $\widehat{G}$ is this group for the
target $\mathbb{C}^\times$.

## Examples

- **Cyclic groups.** If $G$ is cyclic of order $n$ with generator $g$, a character is fixed by
  $\chi(g)$, which may be any $n$-th root of unity. Thus
  [the dual of a cyclic group of order $n$ is isomorphic to the group of $n$-th roots of unity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Basic.html#IsCyclic.monoidHom_mulEquiv_rootsOfUnity), itself cyclic of order $n$. Writing
  $\zeta = e^{2\pi i/n}$, the characters are $\chi_k(g^j) = \zeta^{jk}$ for $k = 0, \dots, n-1$.
- **The Klein four-group.** For $V = \{e, a, b, c\}$ with $a^2 = b^2 = e$ and $ab = c$, each
  character takes values $\pm 1$. Besides the trivial character there are three, one for each
  element $x \in \{a, b, c\}$, sending $x$ to $1$ and the other two non-identity elements to $-1$.
- **Products.** A character of $G_1 \times \dots \times G_k$ is a product of characters of the
  factors, so [the dual of a finite product is the product of the duals](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/BigOperators/Pi.html#Pi.monoidHomMulEquiv) (see [direct product of groups](../basic-definitions/direct-product-of-groups.md)).
- **Dirichlet characters.** The characters of the group of units modulo $m$ correspond to the
  Dirichlet characters modulo $m$: extend each by zero to the residues not coprime to $m$.

## Properties

Let $G$ be a finite abelian group.

- **Size and shape.** [$\widehat{G}$ has the same order as $G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/FiniteAbelian/Duality.html#CommGroup.card_monoidHom_of_hasEnoughRootsOfUnity); indeed
  [$\widehat{G}$ is isomorphic to $G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/FiniteAbelian/Duality.html#CommGroup.monoidHom_mulEquiv_of_hasEnoughRootsOfUnity),
  though no isomorphism is canonical: one depends on choices of generators.
- **Separation.** [If $g \neq e$, some character $\chi$ has $\chi(g) \neq 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/FiniteAbelian/Duality.html#CommGroup.exists_apply_ne_one_of_hasEnoughRootsOfUnity).
- **Double duality.** Each $g \in G$ defines a character of $\widehat{G}$ by
  $\chi \mapsto \chi(g)$, and [this evaluation map is an isomorphism from $G$ onto the dual of $\widehat{G}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/FiniteAbelian/Duality.html#CommGroup.monoidHomMonoidHomEquiv); Mathlib states it as the inverse
  isomorphism, from the double dual to $G$. Unlike the isomorphism
  $G \cong \widehat{G}$, it involves no choices.
- **Orthogonality.** For a character $\chi$,
  $$\sum_{g \in G} \chi(g) = \begin{cases} |G| & \text{if } \chi \text{ is trivial,} \\ 0 & \text{otherwise}\end{cases}$$
  ([the character sum formula](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/IntegralDomain.html#sum_hom_units)), and dually $\sum_{\chi} \chi(g)$ is $|G|$
  for $g = e$ and $0$ otherwise. Hence for the inner product
  $\langle f_1, f_2 \rangle = |G|^{-1} \sum_g f_1(g)\overline{f_2(g)}$ distinct characters are
  orthogonal and each has norm $1$; as there are $|G|$ of them, they form an orthonormal basis of
  the space of complex functions on $G$.
- **Subgroups.** For a subgroup $H$, its annihilator $H^\perp$ is the subgroup of characters
  trivial on $H$. It is the dual of $G/H$, so
  [$|H^\perp|$ equals the index $[G : H]$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/FiniteAbelian/Duality.html#CommGroup.card_subgroupOrderIsoSubgroupMonoidHom)
  (see [index](../../../overview/general-algebra/group-theory/part-01/index-of-a-subgroup.md)), and
  [$H \mapsto H^\perp$ is an inclusion-reversing bijection between the subgroups of $G$ and those of $\widehat{G}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/FiniteAbelian/Duality.html#CommGroup.subgroupOrderIsoSubgroupMonoidHom). An element lies in $H$
  [exactly when every character trivial on $H$ is trivial at it](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/FiniteAbelian/Duality.html#CommGroup.forall_monoidHom_apply_eq_one_iff), and
  [every character of $H$ extends to a character of $G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/FiniteAbelian/Duality.html#MonoidHom.domRestrict_surjective).

## Proof

For a cyclic group of order $n$ the dual is cyclic of order $n$, as in the examples. The dual of a
product is the product of the duals. By the [structure theorem for finitely generated abelian groups](../../../overview/general-algebra/group-theory/part-02/structure-of-finitely-generated-abelian-groups.md), a finite abelian group $G$ is a
product of cyclic groups,
so $\widehat{G} \cong G$ and $|\widehat{G}| = |G|$. Separation follows the same way: if
$g \neq e$, some coordinate of $g$ in a cyclic factor is nontrivial, and a character of that
factor detects it. Then the evaluation map $G \to \widehat{\widehat{G}}$ is injective by
separation and is a bijection because both sides have order $|G|$. For orthogonality, if
$\chi(h) \neq 1$, then multiplying the sum by $\chi(h)$ permutes its terms, so the sum is $0$. For the dual relation, if $g \neq e$, separation gives
$\chi_0$ with $\chi_0(g) \neq 1$, and multiplying the sum by $\chi_0(g)$ permutes its terms.

For a subgroup $H$, restriction of characters is a homomorphism $\widehat{G} \to \widehat{H}$
whose kernel is $H^\perp$. A character trivial on $H$ is the same as a character of $G/H$, so
$|H^\perp| = |G/H| = [G : H]$. The image then has order $|G|/[G : H] = |H| = |\widehat{H}|$, so
restriction is surjective. Applying the count to $H^\perp$ inside $\widehat{G}$ and using double
duality, the elements of $G$ killed by every character in $H^\perp$ form a subgroup of order
$|H|$ that contains $H$, hence equal to $H$; this gives the bijection.

## Related concepts

For a finite group $G$ that is not abelian, the homomorphisms $G \to \mathbb{C}^\times$ still
form a group, but they factor through the [abelianization](../../../overview/general-algebra/group-theory/part-01/abelianization.md) and so only see
it; the full theory is replaced by [characters](../../../overview/general-algebra/representation-theory/character.md) of higher-dimensional
representations. The double duality isomorphism parallels the
[isomorphism of a finite-dimensional vector space with its bidual](../../../overview/linear-algebra/finite-dimensional-vector-spaces/isomorphism-with-bidual.md). For a
locally compact abelian [topological group](../../../overview/topology/topological-algebra/topological-group.md) the dual is the group of
continuous homomorphisms into the unit circle; Pontryagin duality extends double duality to that
setting, and the dual of the integers is the circle.

## In Mathlib

Mathlib has no declaration named for the dual group of a finite abelian group; it works with the
group of homomorphisms directly, in two parallel forms. The multiplicative form, used above, takes
homomorphisms from a finite commutative group into the units of any commutative monoid that
contains a primitive root of unity of order the exponent of $G$ (the least common multiple of
the orders of its elements) and whose roots of unity of that
order form a cyclic group; the complex numbers qualify, so these results are more general than
the statements here. The character sum formula is stated more generally, for
homomorphisms from any finite group into the multiplicative monoid of an integral domain such as
$\mathbb{C}$; a character as defined here becomes one after composing with the inclusion of
$\mathbb{C}^\times$ in $\mathbb{C}$. The additive form takes characters of a finite additive abelian group with
complex values: [the number of characters equals the order of the group](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/FiniteAbelian/PontryaginDuality.html#AddChar.card_eq),
[the group is isomorphic to its double dual](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/FiniteAbelian/PontryaginDuality.html#AddChar.doubleDualEquiv), and [the characters form a basis of the complex functions on the group](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/FiniteAbelian/PontryaginDuality.html#AddChar.complexBasis). The two forms are
developed separately. For topological groups Mathlib defines [the Pontryagin dual](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/PontryaginDual.html#PontryaginDual) as the continuous homomorphisms into the circle with the compact-open
topology, but it does not prove the Pontryagin duality theorem.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Group morphism](../../../overview/general-algebra/group-theory/part-01/group-morphism.md)
- [Complex roots of unity](../abelian-group/complex-roots-of-unity.md)

## Proof depends on

- [Cyclic group](../../../overview/general-algebra/group-theory/part-01/cyclic-group.md)
- [Direct product of groups](../basic-definitions/direct-product-of-groups.md)
- [Structure of finitely generated abelian groups](../../../overview/general-algebra/group-theory/part-02/structure-of-finitely-generated-abelian-groups.md)

## Sources

- [Mathlib undergraduate list: Group Theory › Representation theory of finite groups](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L113)
- [Reference given by Mathlib's undergraduate list](https://kconrad.math.uconn.edu/blurbs/grouptheory/charthy.pdf)
