# First isomorphism theorem

The **first isomorphism theorem** says that a [group homomorphism](group-morphism.md)
$\varphi \colon G \to H$ identifies the [quotient](quotient-group.md) of $G$ by the
kernel of $\varphi$ with the image of $\varphi$. Every homomorphism therefore factors as a
surjection onto a quotient followed by an isomorphism and an inclusion, and the
question of which groups are homomorphic images of $G$ becomes the question of which
[normal subgroups](normal-subgroup.md) $G$ has. The theorem is also known as the
fundamental theorem on homomorphisms, and it is the first of three
isomorphism theorems, together with the [second](second-isomorphism-theorem.md)
and the [third](third-isomorphism-theorem.md).

## Statement

Let $\varphi \colon G \to H$ be a homomorphism of [groups](group.md), with kernel
$K = \{ g \in G : \varphi(g) = e \}$ and image $\varphi(G)$, a [subgroup](subgroup.md) of $H$.
The kernel [is a normal subgroup of $G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Ker.html#MonoidHom.normal_ker), so the quotient group $G/K$
is defined, and the map

$$G/K \to \varphi(G), \qquad gK \mapsto \varphi(g)$$

is [a well-defined isomorphism of groups](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/QuotientGroup/Basic.html#QuotientGroup.quotientKerEquivRange).
When $\varphi$ is surjective this reads
[$G/\ker\varphi \cong H$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/QuotientGroup/Basic.html#QuotientGroup.quotientKerEquivOfSurjective).

## Proof

Write $\psi(gK) = \varphi(g)$. Two cosets $gK$ and $hK$ are equal exactly when
$g^{-1}h \in K$, that is, when $\varphi(g)^{-1}\varphi(h) = e$, that is, when
$\varphi(g) = \varphi(h)$. Read from left to right this says $\psi$ is well defined; read from
right to left it says $\psi$ is injective. Since multiplication of cosets is
$(gK)(hK) = ghK$ and $\varphi$ preserves products, $\psi$ is a homomorphism, and it maps onto
$\varphi(G)$ by construction. Well-definedness and the homomorphism property are a special
case of a more general fact: a homomorphism that is trivial on a normal subgroup $N$
[descends to a homomorphism on $G/N$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/QuotientGroup/Defs.html#QuotientGroup.lift).

## Examples

- **Trivial cases.** The identity map of $G$ has trivial kernel, giving
  [$G/\{e\} \cong G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/QuotientGroup/Basic.html#QuotientGroup.quotientBot); the map sending everything to $e$ gives $G/G \cong \{e\}$.
- **Integers modulo $n$.** Reduction modulo $n$ is a surjective homomorphism from the
  additive group of [integers](../../numbers/integer.md) onto the integers modulo $n$, with kernel $n\mathbb{Z}$, so
  [$\mathbb{Z}/n\mathbb{Z}$ is isomorphic to the group of residues modulo $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/ZMod/QuotientGroup.html#Int.quotientZMultiplesNatEquivZMod).
- **Sign of a permutation.** The [alternating group](../part-02/alternating-group.md) $A_n$
  [is the kernel](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Alternating.html#alternatingGroup_eq_sign_ker) of the [sign homomorphism](../../../../undergraduate/group-theory/permutation-group/signature.md) from the symmetric
  group $S_n$ to $\{\pm 1\}$, and [the sign is onto when $n \ge 2$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Sign.html#Equiv.Perm.sign_surjective).
  Hence $S_n/A_n \cong \{\pm 1\}$, and $A_n$ has index $2$.
- **Determinant.** The [determinant](../../../linear-algebra/matrices/determinant.md) maps the
  [general linear group](../../../../undergraduate/group-theory/classical-automorphism-groups/general-linear-group.md) $\mathrm{GL}_n(F)$, for $n \ge 1$, over a field $F$ onto the
  multiplicative group $F^\times$, with kernel the [special linear group](../../../../undergraduate/linear-algebra/multilinearity/special-linear-group.md),
  so $\mathrm{GL}_n(F)/\mathrm{SL}_n(F) \cong F^\times$.
- **The circle.** The map $t \mapsto e^{2\pi i t}$ from the additive group of real numbers onto
  the unit circle in $\mathbb{C}$ has kernel $\mathbb{Z}$, so $\mathbb{R}/\mathbb{Z}$ is isomorphic to the circle group.

## Consequences

- **Normal subgroups are kernels.** Conversely, every normal
  subgroup $N$ is a kernel: [the quotient map $G \to G/N$ has kernel exactly $N$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/QuotientGroup/Defs.html#QuotientGroup.ker_mk').
- **Counting.** Comparing sizes on both sides, the [index](index-of-a-subgroup.md) of the kernel
  [equals the order of the image](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Index.html#Subgroup.index_ker). Combined with
  [Lagrange's theorem](../part-02/lagranges-theorem.md) in its product form,
  [the order of a group is the order of a subgroup $L$ times its index](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Index.html#Subgroup.card_mul_index),
  $|G| = |L|\,[G:L]$, this gives
  [$|G| = |\ker\varphi|\,|\varphi(G)|$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Index.html#Subgroup.card_ker_mul_card_range), so for a finite group $G$
  [the order of the image divides $|G|$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Index.html#Subgroup.card_range_dvd).
- **Homomorphic images.** Up to isomorphism, the homomorphic images of $G$ are exactly
  the quotients $G/N$ by normal subgroups $N$. In particular a
  [simple group](simple-group.md) has no images other than itself and the trivial group.

## Generalizations

The same argument works wherever a structure has a notion of quotient by a
"kernel". For rings, the quotient of a ring by the kernel of a ring homomorphism
[is isomorphic to its image](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Quotient/Operations.html#RingHom.quotientKerEquivRange) (see the
[first isomorphism theorem for rings](../../ideals-and-quotients/first-isomorphism-theorem-for-commutative-rings.md)). For modules,
the quotient by the [kernel of a linear map](../../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
[is linearly isomorphic to its range](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Isomorphisms.html#LinearMap.quotKerEquivRange), which for vector spaces
yields the [rank–nullity theorem](../../../../thousand-plus/algebra/15-linear-and-multilinear-algebra-matrix-theory/rank-nullity-theorem.md). At the bottom of the
hierarchy, any function from a set $X$ induces an equivalence relation on $X$, and
[the set of its classes is in bijection with the image](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/Setoid/Basic.html#Setoid.quotientKerEquivRange).
In universal algebra and category theory the theorem takes the form of a factorization
of a morphism through its image.

## In Mathlib

Mathlib gives the theorem as a construction rather than an existence statement: it
builds a specific isomorphism of groups from the quotient by the kernel to the image,
where the image is regarded as a group in its own right, a subgroup of the codomain.
The isomorphism is assembled from a bijective homomorphism, so its inverse is not given
by an explicit formula and the definition is marked noncomputable. A computable variant of the surjective case, an
isomorphism onto the whole codomain, [exists for a homomorphism equipped with a right inverse](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/QuotientGroup/Basic.html#QuotientGroup.quotientKerEquivOfRightInverse). The version for additive
groups is generated automatically from the multiplicative one. In the counting
statements, Mathlib assigns size $0$ to an infinite set and index $0$ to a subgroup of
infinite index, so the statements hold for all groups without finiteness hypotheses. For an
infinite group the statements still say something: the index of the kernel is infinite
exactly when the image is, and the product formula says that the kernel or the image is
infinite. Only the divisibility statement becomes vacuous, since every number divides $0$.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group morphism](group-morphism.md)
- [Normal subgroup](normal-subgroup.md)
- [Quotient group](quotient-group.md)
- [Subgroup](subgroup.md)

## Sources

- [Mathlib documentation: `QuotientGroup.quotientKerEquivRange`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/QuotientGroup/Basic.html#QuotientGroup.quotientKerEquivRange)
- [Source of `QuotientGroup.quotientKerEquivRange` in Mathlib/GroupTheory/QuotientGroup/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/GroupTheory/QuotientGroup/Basic.lean#L130)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L44)
- [1000+ theorems list: Q1065966](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L1291)
- [1000+ theorems list: Q1187646](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L1491)
- [1000+ theorems project: Q1065966](https://1000-plus.github.io/all.html?length=-1#Q1065966)
- [Wikipedia: Isomorphism theorem](https://en.wikipedia.org/wiki/Isomorphism_theorem)
- [Wikidata: Q1065966](https://www.wikidata.org/wiki/Q1065966)
- [1000+ theorems project: Q1187646](https://1000-plus.github.io/all.html?length=-1#Q1187646)
- [Wikipedia: Fundamental theorem on homomorphisms](https://en.wikipedia.org/wiki/Fundamental_theorem_on_homomorphisms)
- [Wikidata: Q1187646](https://www.wikidata.org/wiki/Q1187646)
