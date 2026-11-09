# Stabilizer of a point

The **stabilizer** of a point under a [group action](../../../overview/general-algebra/group-theory/part-01/group-action.md) is the set of group
elements that leave the point where it is. It is always a [subgroup](../../../overview/general-algebra/group-theory/part-01/subgroup.md) of the
acting group, and it measures how much symmetry the point retains: the larger the
stabilizer, the smaller the [orbit](orbit.md). This trade-off, the
orbit–stabilizer theorem, turns questions about group actions into questions about
subgroups and their indices, and it is the basic counting tool behind the class equation,
Burnside's lemma and the Sylow theorems.

## Definition

Let a [group](../../../overview/general-algebra/group-theory/part-01/group.md) $G$ act on a set $X$, and write $g \cdot x$ for the action of
$g \in G$ on $x \in X$. The [stabilizer of $x$ is the subgroup](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Defs.html#MulAction.stabilizer)

$$G_x = \{\, g \in G : g \cdot x = x \,\}.$$

Thus [an element $g$ lies in $G_x$ exactly when $g \cdot x = x$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Defs.html#MulAction.mem_stabilizer_iff).
Other common notations are $\operatorname{Stab}_G(x)$ and $\operatorname{Stab}(x)$; the
stabilizer is also called the isotropy group of $x$.

The set $G_x$ is a subgroup. The identity fixes every point. If $g$ and $h$ fix $x$, then
$(gh) \cdot x = g \cdot (h \cdot x) = x$, and applying $g^{-1}$ to both sides of
$g \cdot x = x$ gives $g^{-1} \cdot x = x$.

## Examples

- **Symmetric groups.** The [symmetric group](../../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md) $S_n$ acts on
  $\{1, \dots, n\}$, for $n \ge 1$. The stabilizer of $n$ consists of the permutations that fix $n$, and
  restricting them to $\{1, \dots, n-1\}$ identifies it with $S_{n-1}$. Its index in $S_n$
  is $n$, the number of points.
- **Symmetries of a square.** The dihedral group of order $8$ acts on the four vertices of a
  square. The stabilizer of a vertex consists of the identity and the reflection in the
  diagonal through that vertex, so it has order $2$, and $8 = 4 \cdot 2$.
- **Rotations of the sphere.** The group of rotations of $\mathbb{R}^3$ about the origin acts
  on the unit sphere. The stabilizer of the north pole is the group of rotations about the
  vertical axis, and the stabilizer of any other point is the group of rotations about the
  axis through it.
- **Cosets.** A group $G$ acts on the set $G/H$ of left cosets of a subgroup $H$ by
  $g \cdot aH = gaH$. [The stabilizer of the coset $H$ is $H$ itself](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Quotient.html#MulAction.stabilizer_quotient),
  and the stabilizer of a coset $aH$ is the conjugate $aHa^{-1}$.
- **Conjugation.** A group acts on itself by conjugation, $g \cdot h = g h g^{-1}$, and
  [the stabilizer of $h$ under this action is the centralizer of $h$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/ConjAct.html#ConjAct.stabilizer_eq_centralizer),
  the subgroup of elements that commute with $h$. The orbits of this action are the
  [conjugacy classes](conjugacy-classes.md).
- **Free actions.** When $G$ acts on itself by left multiplication, $gh = h$ forces $g$ to be the identity,
  so every stabilizer is trivial. An action is called free when every stabilizer is trivial.

## Properties

**Stabilizers along an orbit.** Stabilizers of points in the same orbit are conjugate: for
every $g$ in $G$,
[the stabilizer of $g \cdot x$ is $g G_x g^{-1}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Basic.html#MulAction.stabilizer_smul_eq_stabilizer_map_conj).
Indeed $h$ fixes $g \cdot x$ exactly when $g^{-1} h g$ fixes $x$. Consequently, if
$y = g \cdot x$, then
[conjugation by $g$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Basic.html#MulAction.stabilizerEquivStabilizer_apply) is
[an isomorphism from $G_x$ onto $G_y$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Basic.html#MulAction.stabilizerEquivStabilizer).
A stabilizer need not be normal: for the action on $G/H$ the stabilizers are exactly the
conjugates of $H$, and they all equal $H$ only when $H$ is normal.

**Orbit–stabilizer theorem.** Two elements $g$ and $h$ send $x$ to the same point exactly
when $g^{-1}h \in G_x$, that is, when they lie in the same left coset of $G_x$. So
$g G_x \mapsto g \cdot x$ is
[a bijection from the set of left cosets of $G_x$ onto the orbit of $x$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Quotient.html#MulAction.orbitEquivQuotientStabilizer),
and [the index of $G_x$ equals the size of the orbit of $x$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Index.html#MulAction.index_stabilizer).
For a finite group $G$,
[the size of the orbit times the order of the stabilizer is the order of $G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Quotient.html#MulAction.card_orbit_mul_card_stabilizer_eq_card_group):

$$|G \cdot x| \cdot |G_x| = |G|.$$

In particular both factors divide $|G|$, in line with
[Lagrange's theorem](../../../overview/general-algebra/group-theory/part-02/lagranges-theorem.md).
For a transitive action, where the orbit is all of $X$,
[the index of every stabilizer is the number of points of $X$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Index.html#MulAction.index_stabilizer_of_transitive).
Summing over the orbits of a finite set gives the
[class formula](../../../overview/general-algebra/group-theory/part-01/class-formula.md), and counting the
pairs $(g, x)$ with $g \cdot x = x$ in two ways, once by points and once by group elements,
gives [Burnside's lemma](../../../overview/general-algebra/group-theory/part-01/burnside-lemma.md).

**Free actions.** Mathlib expresses freeness as a cancellation law: $g \cdot x = h \cdot x$
implies $g = h$, and each $g$ acts injectively (which is automatic for a group action).
[A group action satisfies this law exactly when every stabilizer is trivial](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Basic.html#isCancelSMul_iff_stabilizer_eq_bot).

**Intersections of stabilizers.** For a subset $S$ of $X$,
[an element lies in the pointwise stabilizer of $S$ exactly when it fixes every point of $S$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/FixingSubgroup.html#mem_fixingSubgroup_iff),
so the pointwise stabilizer is the intersection of the stabilizers $G_x$ for $x$ in $S$.
Taking $S = X$ gives the kernel of the action, the set of elements that act as the
identity; it is a [normal subgroup](../../../overview/general-algebra/group-theory/part-01/normal-subgroup.md), and the action is faithful
exactly when it is trivial. The setwise stabilizer of $S$ is the stabilizer of $S$ as a
point of the induced action on subsets:
[an element $g$ lies in it exactly when, for every $y$ in $X$, $g \cdot y$ lies in $S$ if and only if $y$ does](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Pointwise/Stabilizer.html#MulAction.mem_stabilizer_set).

## Related concepts

Applied to the action of a group on its subgroups by conjugation, the stabilizer of a
subgroup is its normalizer. Mathlib states this for Sylow subgroups:
[the stabilizer of a Sylow $p$-subgroup $P$ under conjugation is the normalizer of $P$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.stabilizer_eq_normalizer).
In a finite group the Sylow $p$-subgroups form a single orbit by the
[second Sylow theorem](../../../overview/general-algebra/group-theory/part-02/second-sylow-theorem.md), so by the orbit–stabilizer
theorem their number is the index of the normalizer of any one of them. More generally,
for a transitive action the orbit–stabilizer bijection identifies $X$ with the coset space
$G/G_x$, compatibly with the action of $G$; in this way the unit sphere corresponds to the
rotation group modulo the rotations about one axis.

## In Mathlib

Mathlib defines the stabilizer for an action of a group as a bundled subgroup of the
acting group, so the closure properties above are part of the definition rather than
separate results. Membership unfolds directly to the equation $g \cdot x = x$. For an action
of a monoid, where inverses are unavailable, the same set is provided as a submonoid, and
the additive version, for actions written with $+$, is generated from the multiplicative
one. There is no separate notion of setwise stabilizer: it is the stabilizer of a set under
the induced action on sets, while the pointwise stabilizer of a set is a separate subgroup,
called its fixing subgroup.
Conjugation is set up as an action of a copy of $G$, so the statement about centralizers
compares two subgroups of that copy. The form of the orbit–stabilizer theorem with the
index holds for every group, using the conventions that a subgroup of infinite index has
index $0$ and an infinite set has size $0$; the form with orders assumes the group is
finite.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group action](../../../overview/general-algebra/group-theory/part-01/group-action.md)
- [Subgroup](../../../overview/general-algebra/group-theory/part-01/subgroup.md)
- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)

## Sources

- [Mathlib documentation: `MulAction.stabilizer`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Defs.html#MulAction.stabilizer)
- [Source of `MulAction.stabilizer` in Mathlib/GroupTheory/GroupAction/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/GroupTheory/GroupAction/Defs.lean#L511)
- [Mathlib undergraduate list: Group Theory › Basic definitions](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L88)
