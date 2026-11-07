The **dual group** of a finite abelian [group](trough:Group) $G$ is the group $\widehat{G}$ of
its characters: the [homomorphisms](trough:MonoidHom) from $G$ to the multiplicative group
$\mathbb{C}^\times$ of nonzero complex numbers, multiplied pointwise. A finite abelian group has
exactly as many characters as elements, and it can be recovered from its dual. The dual group is
the setting for Fourier analysis on finite abelian
groups,
for Dirichlet characters in number theory, and for the representations of abelian
groups,
whose irreducible complex representations correspond to the characters.

## Definition

Let $G$ be a finite abelian group of order $n$. A **character** of $G$ is a map
$\chi : G \to \mathbb{C}^\times$ with $\chi(gh) = \chi(g)\chi(h)$ for all $g, h \in G$. Since
$g^n = e$ for every $g$, each value $\chi(g)$ satisfies $\chi(g)^n = 1$, so it is an $n$-th
[root of unity](trough:Complex.mem_rootsOfUnity); in particular $|\chi(g)| = 1$ and
$\chi(g)^{-1} = \overline{\chi(g)}$.

The product of two characters is $(\chi\psi)(g) = \chi(g)\psi(g)$, the identity is the trivial
character $g \mapsto 1$, and the inverse of $\chi$ is $g \mapsto \overline{\chi(g)}$. In general,
the homomorphisms from a group into a commutative group form a commutative group under pointwise
multiplication; the dual group $\widehat{G}$ is this group for the
target $\mathbb{C}^\times$.

## Examples

- **Cyclic groups.** If $G$ is cyclic of order $n$ with generator $g$, a character is fixed by
  $\chi(g)$, which may be any $n$-th root of unity. Thus
  the dual of a cyclic group of order $n$ is isomorphic to the group of $n$-th roots of
  unity, itself cyclic of order $n$. Writing
  $\zeta = e^{2\pi i/n}$, the characters are $\chi_k(g^j) = \zeta^{jk}$ for $k = 0, \dots, n-1$.
- **The Klein four-group.** For $V = \{e, a, b, c\}$ with $a^2 = b^2 = e$ and $ab = c$, each
  character takes values $\pm 1$. Besides the trivial character there are three, one for each
  element $x \in \{a, b, c\}$, sending $x$ to $1$ and the other two non-identity elements to $-1$.
- **Products.** A character of $G_1 \times \dots \times G_k$ is a product of characters of the
  factors, so the dual of a finite product is the product of the
  duals (see [direct product of groups](trough:Prod.instGroup)).
- **Dirichlet characters.** The characters of the group of units modulo $m$ correspond to the
  Dirichlet characters modulo $m$: extend each by zero to the residues not coprime to $m$.

## Properties

Let $G$ be a finite abelian group.

- **Size and shape.** $\widehat{G}$ has the same order as
  $G$; indeed
  $\widehat{G}$ is isomorphic to $G$,
  though no isomorphism is canonical: one depends on choices of generators.
- **Separation.** If $g \neq e$, some character $\chi$ has
  $\chi(g) \neq 1$.
- **Double duality.** Each $g \in G$ defines a character of $\widehat{G}$ by
  $\chi \mapsto \chi(g)$, and this evaluation map is an isomorphism from $G$ onto the dual of
  $\widehat{G}$; Mathlib states it as the inverse
  isomorphism, from the double dual to $G$. Unlike the isomorphism
  $G \cong \widehat{G}$, it involves no choices.
- **Orthogonality.** For a character $\chi$,
  $$\sum_{g \in G} \chi(g) = \begin{cases} |G| & \text{if } \chi \text{ is trivial,} \\ 0 & \text{otherwise}\end{cases}$$
  (the character sum formula), and dually $\sum_{\chi} \chi(g)$ is $|G|$
  for $g = e$ and $0$ otherwise. Hence for the inner product
  $\langle f_1, f_2 \rangle = |G|^{-1} \sum_g f_1(g)\overline{f_2(g)}$ distinct characters are
  orthogonal and each has norm $1$; as there are $|G|$ of them, they form an orthonormal basis of
  the space of complex functions on $G$.
- **Subgroups.** For a subgroup $H$, its annihilator $H^\perp$ is the subgroup of characters
  trivial on $H$. It is the dual of $G/H$, so
  $|H^\perp|$ equals the index $[G : H]$
  (see [index](trough:Subgroup.index)), and
  $H \mapsto H^\perp$ is an inclusion-reversing bijection between the subgroups of $G$ and those
  of $\widehat{G}$. An element lies in $H$
  exactly when every character trivial on $H$ is trivial at
  it, and
  every character of $H$ extends to a character of $G$.

## Proof

For a cyclic group of order $n$ the dual is cyclic of order $n$, as in the examples. The dual of a
product is the product of the duals. By the [structure theorem for finitely generated abelian
groups](trough:AddCommGroup.equiv_free_prod_directSum_zmod), a finite abelian group $G$ is a
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
form a group, but they factor through the [abelianization](trough:Abelianization) and so only see
it; the full theory is replaced by [characters](trough:FDRep.character) of higher-dimensional
representations. The double duality isomorphism parallels the
[isomorphism of a finite-dimensional vector space with its bidual](trough:Module.evalEquiv). For a
locally compact abelian [topological group](trough:IsTopologicalGroup) the dual is the group of
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
complex values: the number of characters equals the order of the group,
the group is isomorphic to its double dual, and the characters
form a basis of the complex functions on the group. The two forms are
developed separately. For topological groups Mathlib defines the Pontryagin
dual as the continuous homomorphisms into the circle with the compact-open
topology, but it does not prove the Pontryagin duality theorem.

## Depends on

- [Group](trough:Group)
- [Group morphism](trough:MonoidHom)
- [Complex roots of unity](trough:Complex.mem_rootsOfUnity)

## Proof depends on

- [Cyclic group](trough:IsCyclic)
- [Direct product of groups](trough:Prod.instGroup)
- [Structure of finitely generated abelian groups](trough:AddCommGroup.equiv_free_prod_directSum_zmod)
