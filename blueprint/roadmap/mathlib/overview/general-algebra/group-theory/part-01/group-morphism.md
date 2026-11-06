# Group morphism

A **group morphism**, or group homomorphism, is a map between two [groups](group.md) that
respects the group operation. Morphisms are how groups are compared: they
describe when one group is a copy of another, when one is a quotient of
another, and how a group can be represented by permutations or matrices. Much of
group theory, from [normal subgroups](normal-subgroup.md) to the
[first](first-isomorphism-theorem.md),
[second](second-isomorphism-theorem.md) and
[third](third-isomorphism-theorem.md) isomorphism theorems,
is organized around them.

## Definition

Let $G$ and $H$ be groups. A map $f \colon G \to H$ is a group morphism if

$$f(xy) = f(x)\,f(y) \quad \text{for all } x, y \in G.$$

For monoids $M$ and $N$, the same definition with the extra requirement
$f(1_M) = 1_N$ defines a [morphism of monoids](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Hom/Defs.html#MonoidHom); in a monoid the
identity condition does not follow from multiplicativity. For groups it is
automatic: from $f(e)f(e) = f(e)$ one cancels $f(e)$ in $H$ and gets
$f(e) = e$, so [a product-preserving map into a group already preserves the identity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Hom/Defs.html#MonoidHom.mk').
An isomorphism is a morphism that has an inverse morphism. The inverse map of a
bijective morphism is automatically a morphism, since
$f(f^{-1}(u)f^{-1}(v)) = uv$, so
[every bijective morphism is an isomorphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Equiv/Defs.html#MulEquiv.ofBijective).

## Examples

- The identity map of $G$ is a morphism, and so is the trivial map sending every
  element to the identity of $H$.
- The inclusion of a [subgroup](subgroup.md) $K \le G$ into $G$ is an injective morphism.
- For a normal subgroup $N$ of $G$, the
  [map sending $g$ to its coset $gN$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/QuotientGroup/Defs.html#QuotientGroup.mk') is a surjective
  morphism onto the [quotient group](quotient-group.md) $G/N$.
- The exponential function is a morphism from the real numbers under addition to
  the positive reals under multiplication, since $e^{x+y} = e^x e^y$; it is an
  isomorphism with inverse the natural logarithm.
- The [signature](../../../../undergraduate/group-theory/permutation-group/signature.md) of a permutation of a finite set,
  which is $1$ for even and $-1$ for odd permutations,
  [is a morphism to the group $\{1, -1\}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Sign.html#Equiv.Perm.sign). Its kernel is the
  [alternating group](../part-02/alternating-group.md).
- Since $\det(AB) = \det(A)\det(B)$, the [determinant](../../../linear-algebra/matrices/determinant.md) is a
  morphism from the invertible $n \times n$ matrices over a field $K$ to the
  nonzero elements of $K$. Mathlib records the
  [determinant as a monoid morphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Determinant/Basic.html#Matrix.detMonoidHom) on all square
  matrices over a commutative ring.

## Properties

A morphism preserves all of the group structure, not only products. It
[sends the identity to the identity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Hom/Defs.html#map_one), it
[sends inverses to inverses](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Hom/Defs.html#map_inv), $f(x^{-1}) = f(x)^{-1}$, and
consequently [it commutes with integer powers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Hom/Defs.html#map_zpow):

$$f(x^n) = f(x)^n \quad \text{for all } n \in \mathbb{Z}.$$

The [composite of two morphisms is a morphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Hom/Defs.html#MonoidHom.comp), and the
[identity map is a morphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Hom/Defs.html#MonoidHom.id), so groups and their morphisms
form a [category](../../category-theory/category.md).

Two subgroups are attached to every morphism $f \colon G \to H$.

- The **kernel** is $\ker f = \{ x \in G : f(x) = e \}$. It is
  [a subgroup of $G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Ker.html#MonoidHom.ker), and in fact
  [a normal subgroup](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Ker.html#MonoidHom.normal_ker), because
  $f(gxg^{-1}) = f(g)f(x)f(g)^{-1} = e$ whenever $f(x) = e$.
  The kernel measures how far $f$ is from injective:
  [$f$ is injective exactly when its kernel is trivial](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Ker.html#MonoidHom.ker_eq_bot_iff),
  since $f(x) = f(y)$ holds if and only if $x^{-1}y$ lies in the kernel.
- The **image** $f(G)$ is [a subgroup of $H$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Ker.html#MonoidHom.range), equal to
  all of $H$ [precisely when $f$ is surjective](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Ker.html#MonoidHom.range_eq_top).

More generally, [the image of a subgroup of $G$ is a subgroup of $H$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Map.html#Subgroup.map),
[the preimage of a subgroup of $H$ is a subgroup of $G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Map.html#Subgroup.comap), and
[the preimage of a normal subgroup is normal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Basic.html#Subgroup.Normal.comap). The
[first isomorphism theorem](first-isomorphism-theorem.md) ties the two
subgroups together: [$G / \ker f$ is isomorphic to the image of $f$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/QuotientGroup/Basic.html#QuotientGroup.quotientKerEquivRange).
Every normal subgroup $N$ of $G$
[is the kernel of the quotient map $G \to G/N$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/QuotientGroup/Defs.html#QuotientGroup.ker_mk'),
so normal subgroups are exactly the kernels of morphisms.

## Related concepts

A [group action](group-action.md) of $G$ on a set $X$ amounts to a morphism
from $G$ to the group of [permutations of $X$](../part-02/permutation-group-of-a-type.md), and a
linear [representation](../../representation-theory/representation.md) is a morphism from $G$ to the
invertible linear maps of a vector space. Morphisms of other algebraic
structures follow the same pattern: a [ring morphism](../../rings/ring-morphism.md) preserves
addition, multiplication and the unit, and a [linear map](../../../linear-algebra/fundamentals/linear-map.md)
preserves addition and scalar multiplication. The
[abelianization](abelianization.md) and [free groups](free-group.md)
are characterized by universal properties:
[morphisms from the abelianization of $G$ to an abelian group $A$ correspond to morphisms $G \to A$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Abelianization/Defs.html#Abelianization.lift),
and [morphisms from the free group on a set $S$ to a group $H$ correspond to arbitrary maps $S \to H$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/FreeGroup/Basic.html#FreeGroup.lift).

## In Mathlib

Mathlib has no separate notion of group morphism: it uses the morphisms of
monoids, which preserve the product and the identity, for groups as well. The
definition asks only for a multiplication and an identity element on each side,
so the same structure covers monoids, groups and many intermediate cases, and a
group morphism must come with a proof that it preserves the identity, which the
constructor mentioned above supplies from multiplicativity. The kernel, as a subgroup, is defined
whenever the source is a group; the target needs only a multiplication with an
identity element. Morphisms are
bundled: a morphism is a function packaged with the proofs of its properties,
and general results are usually stated for any type of maps that behaves like
morphisms, so they apply equally to isomorphisms and to ring morphisms. The
additive version, for groups written with $+$, is a parallel structure, and most
of its definitions and theorems are generated automatically from the
multiplicative ones.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group](group.md)

## Sources

- [Mathlib documentation: `MonoidHom`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Hom/Defs.html#MonoidHom)
- [Source of `MonoidHom` in Mathlib/Algebra/Group/Hom/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Group/Hom/Defs.lean#L357)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L34)
- [Mathlib undergraduate list: Group Theory › Basic definitions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L80)
