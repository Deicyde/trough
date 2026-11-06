# Orbit

The **orbit** of a point under a [group action](../../../overview/general-algebra/group-theory/part-01/group-action.md) is the set of all
points the group can move it to. When a group acts on a set, the orbits cut the set
into disjoint pieces, and the size of each piece is tied to the structure of the
group by the orbit–stabilizer theorem. Counting arguments built on orbits underlie
much of finite group theory, including the class equation, Burnside's lemma and the
Sylow theorems.

## Definition

Let a [group](../../../overview/general-algebra/group-theory/part-01/group.md) $G$ act on a [set](../../../overview/data-structures/sets/set.md) $X$, and write $g \cdot x$
for the action of $g \in G$ on $x \in X$. The
[orbit of $x$ is the set](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Defs.html#MulAction.orbit)

$$G \cdot x = \{\, g \cdot x : g \in G \,\}.$$

Thus [a point $y$ lies in the orbit of $x$ exactly when $y = g \cdot x$ for some $g$ in $G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Defs.html#MulAction.mem_orbit_iff).
Taking $g$ to be the identity shows that
[every point lies in its own orbit](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Defs.html#MulAction.mem_orbit_self).

## Examples

- **Rotations of the plane.** The group of rotations about the origin acts on
  $\mathbb{R}^2$. The orbit of a point at distance $r > 0$ from the origin is the
  circle of radius $r$ about the origin, and the orbit of the origin is the origin
  alone.
- **Permutations.** A single permutation $\sigma$ of a finite set generates a cyclic
  group of permutations, whose orbits are the cycles of $\sigma$, each fixed point
  counting as a cycle of length one. For
  $\sigma = (1\,2\,3)(4\,5)$ acting on $\{1, \dots, 6\}$, the orbits are
  $\{1, 2, 3\}$, $\{4, 5\}$ and $\{6\}$.
- **Conjugation.** A group acts on itself by conjugation, $g \cdot h = g h g^{-1}$.
  [The orbit of $h$ under this action is its conjugacy class](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/ConjAct.html#ConjAct.orbit_eq_carrier_conjClasses)
  (see [conjugacy classes](conjugacy-classes.md)).
- **Cosets.** A [subgroup](../../../overview/general-algebra/group-theory/part-01/subgroup.md) $H$ of $G$ acts on $G$ by left
  multiplication. [The orbit of $a$ under this action is the right coset $Ha$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Coset/Basic.html#orbit_subgroup_eq_rightCoset).
- **Transitive actions.** An action is transitive if any point can be moved to any
  other by some group element. On a nonempty set this means there is exactly one
  orbit: for any point $x$,
  [the action is transitive if and only if the orbit of $x$ is all of $X$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Transitive.html#MulAction.isPretransitive_iff_orbit_eq_univ).

## Properties

**Orbits partition the set.** For a group action,
[the orbit of $g \cdot x$ equals the orbit of $x$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Defs.html#MulAction.orbit_smul), and
[two orbits $G \cdot x$ and $G \cdot y$ are equal exactly when $x$ lies in $G \cdot y$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Defs.html#MulAction.orbit_eq_iff).
So two orbits are either equal or disjoint, and
[the relation of lying in a common orbit is an equivalence relation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Defs.html#MulAction.orbitRel)
whose classes are the orbits.
[The orbits together cover $X$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Defs.html#MulAction.univ_eq_iUnion_orbit), and
[$X$ is in bijection with the disjoint union of its orbits](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Defs.html#MulAction.selfEquivSigmaOrbits).
The set of orbits is often written $X/G$.

**Orbit–stabilizer theorem.** Let $G_x = \{\, g \in G : g \cdot x = x \,\}$ be the
[stabilizer](stabilizer-of-a-point.md) of $x$. Two elements $g$ and $h$ send $x$
to the same point exactly when $g^{-1}h \in G_x$, that is, when they lie in the same
left coset of $G_x$. Hence the rule $g G_x \mapsto g \cdot x$ gives
[a bijection between the orbit of $x$ and the set of left cosets of $G_x$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Quotient.html#MulAction.orbitEquivQuotientStabilizer).
In particular [the index of $G_x$ equals the size of the orbit](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Index.html#MulAction.index_stabilizer),
and for a finite group

$$|G \cdot x| \cdot |G_x| = |G|$$

([the counting form](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Quotient.html#MulAction.card_orbit_mul_card_stabilizer_eq_card_group)).
So the size of every orbit of a finite group divides the order of the group.

**Fixed points.** A point is fixed by every element of $G$ exactly when
[its orbit has at most one element](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Basic.html#MulAction.subsingleton_orbit_iff_mem_fixedPoints),
which, since the orbit contains the point, means the orbit is the point alone.

**Counting.** Summing the orbit–stabilizer formula over the orbits of a finite group
acting on a finite set gives the [class formula](../../../overview/general-algebra/group-theory/part-01/class-formula.md)

$$|X| = \sum_{G \cdot x \,\in\, X/G} \frac{|G|}{|G_x|},$$

one representative $x$ being chosen from each orbit. The same bookkeeping, done over
pairs of a group element and a point it fixes, gives
[Burnside's lemma](../../../overview/general-algebra/group-theory/part-01/burnside-lemma.md),
which counts orbits as the average number of fixed points.

**Actions of $p$-groups.** Let $p$ be a prime and let $G$ be a group in which every
element has order a power of $p$. Then
[every finite orbit of $G$ has a power of $p$ as its size](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/PGroup.html#IsPGroup.card_orbit).
Every orbit of size greater than $1$ therefore contributes a multiple of $p$, so for
an action on a finite set
[$|X|$ is congruent modulo $p$ to the number of fixed points](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/PGroup.html#IsPGroup.card_modEq_card_fixedPoints).
This congruence drives standard proofs of
[Cauchy's theorem](../../../thousand-plus/algebra/20-group-theory-and-generalizations/cauchys-theorem-group-theory.md) and of the
[first](../../../overview/general-algebra/group-theory/part-02/first-sylow-theorem.md),
[second](../../../overview/general-algebra/group-theory/part-02/second-sylow-theorem.md) and
[third](../../../overview/general-algebra/group-theory/part-02/third-sylow-theorem.md) Sylow theorems.

## Related concepts

The orbits of the conjugation action are the conjugacy classes, and for that action
the class formula becomes the class equation of a finite group. The orbit of a
subgroup $K$ under the conjugation action of $G$ on its subgroups is the set of
conjugates of $K$; the [second Sylow theorem](../../../overview/general-algebra/group-theory/part-02/second-sylow-theorem.md)
says that in a finite group the Sylow $p$-subgroups form a single such orbit. Orbits are also the
starting point for quotient constructions, where one replaces a space by its set of
orbits.

## In Mathlib

Mathlib defines the orbit for any rule that lets elements of one type act on another,
with no axioms at all: the orbit of $x$ is the image of the map $g \mapsto g \cdot x$.
Most results need more. That a point lies in its own orbit holds for actions of
monoids, while the partition into orbits, the orbit relation and the orbit–stabilizer
theorem need a group. The restriction matters: the natural numbers act on themselves
by multiplication, the orbit of $1$ contains $0$, but the orbit of $0$ is $\{0\}$.
An orbit is a subset of the acted-on type rather than a separate structure. The
orbit–stabilizer theorem is stated as an explicit bijection with the coset space, from
which the counting forms follow; the form with the index holds for every group, using
the convention that an infinite set has size $0$ and a subgroup of infinite index has
index $0$. Mathlib calls a transitive action pretransitive, since it does not require
the set to be nonempty. Additive versions, for actions written with $+$, are generated
from the multiplicative ones.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group action](../../../overview/general-algebra/group-theory/part-01/group-action.md)
- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Set](../../../overview/data-structures/sets/set.md)

## Proof depends on

- [Stabilizer of a point](stabilizer-of-a-point.md)
- [Subgroup](../../../overview/general-algebra/group-theory/part-01/subgroup.md)

## Sources

- [Mathlib documentation: `MulAction.orbit`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Defs.html#MulAction.orbit)
- [Source of `MulAction.orbit` in Mathlib/GroupTheory/GroupAction/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/GroupAction/Defs.lean#L47)
- [Mathlib undergraduate list: Group Theory › Basic definitions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L89)
