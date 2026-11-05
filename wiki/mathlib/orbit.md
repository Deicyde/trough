---
article_id: af_0fccc98e5e9bdab0a2823341
concept: MulAction.orbit
---

The **orbit** of a point under a [group action](trough:MulAction) is the set of all
points the group can move it to. When a group acts on a set, the orbits cut the set
into disjoint pieces, and the size of each piece is tied to the structure of the
group by the orbit–stabilizer theorem. Counting arguments built on orbits underlie
much of finite group theory, including the class equation, Burnside's lemma and the
Sylow theorems.

## Definition

Let a [group](trough:Group) $G$ act on a [set](trough:Set) $X$, and write $g \cdot x$
for the action of $g \in G$ on $x \in X$. The
[orbit of $x$ is the set](lean:MulAction.orbit)

$$G \cdot x = \{\, g \cdot x : g \in G \,\}.$$

Thus [a point $y$ lies in the orbit of $x$ exactly when $y = g \cdot x$ for some $g$ in $G$](lean:MulAction.mem_orbit_iff).
Taking $g$ to be the identity shows that
[every point lies in its own orbit](lean:MulAction.mem_orbit_self).

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
  [The orbit of $h$ under this action is its conjugacy class](lean:ConjAct.orbit_eq_carrier_conjClasses)
  (see [conjugacy classes](trough:ConjClasses)).
- **Cosets.** A [subgroup](trough:Subgroup) $H$ of $G$ acts on $G$ by left
  multiplication. [The orbit of $a$ under this action is the right coset $Ha$](lean:orbit_subgroup_eq_rightCoset).
- **Transitive actions.** An action is transitive if any point can be moved to any
  other by some group element. On a nonempty set this means there is exactly one
  orbit: for any point $x$,
  [the action is transitive if and only if the orbit of $x$ is all of $X$](lean:MulAction.isPretransitive_iff_orbit_eq_univ).

## Properties

**Orbits partition the set.** For a group action,
[the orbit of $g \cdot x$ equals the orbit of $x$](lean:MulAction.orbit_smul), and
[two orbits $G \cdot x$ and $G \cdot y$ are equal exactly when $x$ lies in $G \cdot y$](lean:MulAction.orbit_eq_iff).
So two orbits are either equal or disjoint, and
[the relation of lying in a common orbit is an equivalence relation](lean:MulAction.orbitRel)
whose classes are the orbits.
[The orbits together cover $X$](lean:MulAction.univ_eq_iUnion_orbit), and
[$X$ is in bijection with the disjoint union of its orbits](lean:MulAction.selfEquivSigmaOrbits).
The set of orbits is often written $X/G$.

**Orbit–stabilizer theorem.** Let $G_x = \{\, g \in G : g \cdot x = x \,\}$ be the
[stabilizer](trough:MulAction.stabilizer) of $x$. Two elements $g$ and $h$ send $x$
to the same point exactly when $g^{-1}h \in G_x$, that is, when they lie in the same
left coset of $G_x$. Hence the rule $g G_x \mapsto g \cdot x$ gives
[a bijection between the orbit of $x$ and the set of left cosets of $G_x$](lean:MulAction.orbitEquivQuotientStabilizer).
In particular [the index of $G_x$ equals the size of the orbit](lean:MulAction.index_stabilizer),
and for a finite group

$$|G \cdot x| \cdot |G_x| = |G|$$

([the counting form](lean:MulAction.card_orbit_mul_card_stabilizer_eq_card_group)).
So the size of every orbit of a finite group divides the order of the group.

**Fixed points.** A point is fixed by every element of $G$ exactly when
[its orbit has at most one element](lean:MulAction.subsingleton_orbit_iff_mem_fixedPoints),
which, since the orbit contains the point, means the orbit is the point alone.

**Counting.** Summing the orbit–stabilizer formula over the orbits of a finite group
acting on a finite set gives the [class formula](trough:MulAction.selfEquivSigmaOrbitsQuotientStabilizer)

$$|X| = \sum_{G \cdot x \,\in\, X/G} \frac{|G|}{|G_x|},$$

one representative $x$ being chosen from each orbit. The same bookkeeping, done over
pairs of a group element and a point it fixes, gives
[Burnside's lemma](trough:MulAction.sum_card_fixedBy_eq_card_orbits_mul_card_group),
which counts orbits as the average number of fixed points.

**Actions of $p$-groups.** Let $p$ be a prime and let $G$ be a group in which every
element has order a power of $p$. Then
[every finite orbit of $G$ has a power of $p$ as its size](lean:IsPGroup.card_orbit).
Every orbit of size greater than $1$ therefore contributes a multiple of $p$, so for
an action on a finite set
[$|X|$ is congruent modulo $p$ to the number of fixed points](lean:IsPGroup.card_modEq_card_fixedPoints).
This congruence drives standard proofs of
[Cauchy's theorem](trough:exists_prime_orderOf_dvd_card) and of the
[first](trough:Sylow.exists_subgroup_card_pow_prime),
[second](trough:Sylow.isPretransitive_of_finite) and
[third](trough:card_sylow_modEq_one) Sylow theorems.

## Related concepts

The orbits of the conjugation action are the conjugacy classes, and for that action
the class formula becomes the class equation of a finite group. The orbit of a
subgroup $K$ under the conjugation action of $G$ on its subgroups is the set of
conjugates of $K$; the [second Sylow theorem](trough:Sylow.isPretransitive_of_finite)
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

## Depends on

- [Group action](trough:MulAction)
- [Group](trough:Group)
- [Set](trough:Set)

## Proof depends on

- [Stabilizer of a point](trough:MulAction.stabilizer)
- [Subgroup](trough:Subgroup)
