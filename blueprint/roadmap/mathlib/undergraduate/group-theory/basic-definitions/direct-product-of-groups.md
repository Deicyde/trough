# Direct product of groups

The **direct product** of two [groups](../../../overview/general-algebra/group-theory/part-01/group.md) $G$ and $H$ is the group
$G \times H$ whose elements are ordered pairs $(g, h)$ with $g \in G$ and
$h \in H$, multiplied one coordinate at a time. It is a basic way to build new
groups from old ones: large groups are
assembled from small ones as products, and many groups are understood by
recognizing them as products of simpler factors, as in the classification of
finite abelian groups.

## Definition

Let $G$ and $H$ be groups. On the set $G \times H$ of ordered pairs define

$$(g_1, h_1)\,(g_2, h_2) = (g_1 g_2,\; h_1 h_2),$$

so that [the product of two pairs is the pair of products](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Notation/Prod.html#Prod.mk_mul_mk).
The identity element is [the pair $(e_G, e_H)$ of identities](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Notation/Prod.html#Prod.one_eq_mk),
and [the inverse of $(g, h)$ is $(g^{-1}, h^{-1})$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Notation/Prod.html#Prod.inv_mk). Each group
axiom holds in $G \times H$ because it holds in each coordinate separately, so
[these operations make $G \times H$ a group](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Prod.html#Prod.instGroup). The same
construction applies to any finite list of groups $G_1 \times \dots \times G_n$.

The direct product comes with two projection homomorphisms
$\pi_1 : G \times H \to G$ and $\pi_2 : G \times H \to H$, and two inclusions
$g \mapsto (g, e)$ and $h \mapsto (e, h)$. The images of the inclusions are the
subgroups $G \times \{e\}$ and $\{e\} \times H$, and
[the kernel of $\pi_1$ is $\{e\} \times H$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Basic.html#MonoidHom.ker_fst).

## Examples

- **The Klein four-group.** $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$
  has four elements, and each of its three non-identity elements has order $2$.
  It is therefore not [cyclic](../../../overview/general-algebra/group-theory/part-01/cyclic-group.md), and it is the smallest group
  that is not cyclic.
- **Cyclic groups of coprime order.** For coprime $m$ and $n$,
  [the ring $\mathbb{Z}/mn\mathbb{Z}$ is isomorphic to $\mathbb{Z}/m\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/ZMod/Basic.html#ZMod.chineseRemainder),
  which is the [Chinese remainder theorem](../../../overview/general-algebra/ideals-and-quotients/chinese-remainder-theorem.md);
  in particular the additive groups are isomorphic, so
  $\mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$.
- **Euclidean space.** The additive group of $\mathbb{R}^n$ is the direct product
  of $n$ copies of the additive group $\mathbb{R}$.
- **Mixed factors.** $\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ is an infinite
  abelian group with exactly one element of order $2$, namely $(0, 1)$.

## Properties

- **Order.** [The number of elements of $G \times H$ is $|G|\,|H|$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/SetTheory/Cardinal/Finite.html#Nat.card_prod)
  when $G$ and $H$ are finite.
- **Order of an element.** If $g$ and $h$ have finite order, then
  [the order of $(g, h)$ is the least common multiple of the orders of $g$ and $h$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/OrderOfElement.html#Prod.orderOf_mk)
  (see [order of an element](order-of-an-element.md)).
- **Commutativity.** [Two pairs commute exactly when their coordinates commute](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Prod.html#Prod.commute_iff),
  so [the product of two abelian groups is abelian](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Prod.html#Prod.instCommGroup).
  Conversely, if $G \times H$ is abelian then so are $G$ and $H$.
- **Cyclic products.** For finite groups $G$ and $H$,
  [$G \times H$ is cyclic if and only if $G$ and $H$ are both cyclic and their orders are coprime](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Cyclic.html#Group.isCyclic_prod_iff).
- **Symmetry.** [$G \times H$ is isomorphic to $H \times G$ by swapping coordinates](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Prod.html#MulEquiv.prodComm),
  and [$(G \times H) \times K$ is isomorphic to $G \times (H \times K)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Prod.html#MulEquiv.prodAssoc).
- **Subgroups and quotients.** For subgroups $A \le G$ and $B \le H$, the set
  $A \times B$ is [a subgroup of $G \times H$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Basic.html#Subgroup.prod) (see
  [subgroup](../../../overview/general-algebra/group-theory/part-01/subgroup.md)); if $A$ and $B$ are
  [normal](../../../overview/general-algebra/group-theory/part-01/normal-subgroup.md), [so is $A \times B$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Basic.html#Subgroup.prod_normal), and
  [the quotient $(G \times H)/(A \times B)$ is isomorphic to $(G/A) \times (H/B)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/QuotientGroup/Basic.html#QuotientGroup.prodMulEquiv).
  Not every subgroup of $G \times H$ has this form: the diagonal
  $\{(g, g)\}$ in $G \times G$ does not, unless $G$ is trivial.

## Universal property

The direct product is the product of $G$ and $H$ in the category of groups. Given
homomorphisms $\varphi : K \to G$ and $\psi : K \to H$ from any group $K$, the map
$k \mapsto (\varphi(k), \psi(k))$ is a homomorphism $K \to G \times H$, and
[composing it with $\pi_1$ gives back $\varphi$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Prod.html#MonoidHom.fst_comp_prod).
Moreover [every homomorphism into $G \times H$ is the one built in this way from its two components](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Prod.html#MonoidHom.prod_unique).
In the other direction, [when the target group is abelian, homomorphisms $\varphi : G \to P$ and $\psi : H \to P$ combine into the homomorphism $(g, h) \mapsto \varphi(g)\,\psi(h)$ on $G \times H$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Prod.html#MonoidHom.coprod);
in fact, for abelian groups the direct product is also the coproduct, so a finite
direct product of abelian groups is often written as a
[direct sum](../../linear-algebra/fundamentals/direct-sum.md) $G \oplus H$.

## Internal direct products

A group $G$ is isomorphic to $N \times K$ for subgroups $N$ and $K$ of $G$ when
$N$ and $K$ are both normal, $N \cap K = \{e\}$, and every element of $G$ is a
product $nk$ with $n \in N$ and $k \in K$. Under these conditions elements of $N$
commute with elements of $K$, and $(n, k) \mapsto nk$ is an isomorphism. In this
case $G$ is called the internal direct product of $N$ and $K$.

## Generalizations

- The product of an arbitrary family of groups, indexed by any set, is
  [again a group under coordinatewise multiplication](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Pi/Basic.html#Pi.group).
- The semidirect product $N \rtimes_\varphi K$ twists the multiplication of
  $N \times K$ by an action $\varphi$ of $K$ on $N$ by automorphisms;
  [for the trivial action it is isomorphic to the direct product](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SemidirectProduct.html#SemidirectProduct.mulEquivProd).
- The same coordinatewise construction gives the
  [product of rings](../../ring-theory/fundamentals/product-of-rings.md) and the
  [product of vector spaces](../../linear-algebra/fundamentals/product-of-vector-spaces.md).

## In Mathlib

Mathlib does not introduce a separate type for the direct product. It uses the
ordinary type of ordered pairs and declares a group structure on it, once and for
all, whenever both factors are groups, so the group structure on $G \times H$
is available without further input. Most of
the surrounding facts, such as the projections, inclusions, the universal
property and the swap and reassociation isomorphisms, are stated for monoids or
even more general structures, and specialize to groups. Sizes and orders are
natural numbers: the number of elements of an infinite set, and the order of
an element of infinite order, are both taken to be $0$; with this convention the formulas for the order of
$G \times H$ and of an element $(g, h)$, and the criterion for $G \times H$ to be
cyclic, hold for all groups, not only finite ones. Products of arbitrary
families are a separate construction, functions from the index set, with their
own group structure.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)

## Sources

- [Mathlib documentation: `Prod.instGroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Prod.html#Prod.instGroup)
- [Source of `Prod.instGroup` in Mathlib/Algebra/Group/Prod.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Group/Prod.lean#L134)
- [Mathlib undergraduate list: Group Theory › Basic definitions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L81)
