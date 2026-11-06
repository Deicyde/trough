# Burnside lemma

**Burnside's lemma**, also called the Cauchy–Frobenius lemma or the orbit-counting
lemma, says that when a finite [group](group.md) acts on a finite set, the number
of [orbits](../../../../undergraduate/group-theory/basic-definitions/orbit.md) equals the average number of points fixed by an
element of the group. It is the basic tool for counting objects up to symmetry:
colourings of a necklace up to rotation, of a cube up to rigid motion, or graphs up
to relabelling of their vertices. It is also the first step towards the
Pólya enumeration theorem.

## Statement

Let $G$ be a finite group with a [group action](group-action.md) on a finite set $X$.
For $g \in G$ write

$$X^g = \{\, x \in X : g \cdot x = x \,\}$$

for [the set of points fixed by $g$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Defs.html#MulAction.fixedBy). Two points lie in the
same orbit when one is carried to the other by some element of $G$; this
[relation of lying in a common orbit](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Defs.html#MulAction.orbitRel) is an equivalence
relation, and $X/G$ denotes its set of classes, the orbits. Then
[the fixed-point counts sum to the number of orbits times the order of $G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Quotient.html#MulAction.sum_card_fixedBy_eq_card_orbits_mul_card_group):

$$\sum_{g \in G} |X^g| = |X/G| \cdot |G|, \qquad\text{equivalently}\qquad |X/G| = \frac{1}{|G|} \sum_{g \in G} |X^g|.$$

## Examples

- **Necklaces.** Colour the four beads of a square necklace black or white, and
  regard two colourings as the same when a rotation takes one to the other. The
  rotation group has order $4$. The identity fixes all $16$ colourings, the
  quarter turns in either direction fix only the $2$ one-coloured necklaces, and
  the half turn fixes the $4$ colourings in which opposite beads agree. So there
  are $(16 + 2 + 4 + 2)/4 = 6$ necklaces.
- **Transitive actions.** If the action has a single orbit, the average number of
  fixed points is $1$. When $|X| \ge 2$ the identity fixes more than one point, so
  some element of $G$ fixes no point at all: every transitive permutation group
  of degree at least $2$ contains a fixed-point-free element.
- **Conjugation.** Let $G$ act on itself by conjugation. The orbits are the
  [conjugacy classes](../../../../undergraduate/group-theory/basic-definitions/conjugacy-classes.md), and the points fixed by $g$ are the elements
  commuting with $g$. Summing over $g$ counts commuting ordered pairs, so
  [the number of commuting pairs equals the number of conjugacy classes times $|G|$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/CardCommute.html#card_comm_eq_card_conjClasses_mul_card).
  Equivalently, two elements chosen independently and uniformly from $G$ commute
  with probability $k(G)/|G|$, where $k(G)$ is the number of conjugacy classes.

## Proof

Count the set of pairs $(g, x) \in G \times X$ with $g \cdot x = x$ in two ways.
Grouping the pairs by $g$ gives $\sum_{g} |X^g|$. Grouping them by $x$ gives
$\sum_{x} |G_x|$, where the [stabilizer](../../../../undergraduate/group-theory/basic-definitions/stabilizer-of-a-point.md)
$G_x = \{\, g : g \cdot x = x \,\}$ is
[a subgroup of $G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Defs.html#MulAction.stabilizer). By the orbit-stabilizer theorem,
[the size of the orbit of $x$ times the order of $G_x$ is $|G|$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Quotient.html#MulAction.card_orbit_mul_card_stabilizer_eq_card_group),
so $|G_x| = |G| / |G \cdot x|$. The points of a single orbit $O$ therefore
contribute $|O| \cdot |G|/|O| = |G|$ to the second sum, and the total is
$|X/G| \cdot |G|$.

The same argument can be phrased without arithmetic. Points in one orbit have
[isomorphic stabilizers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Basic.html#MulAction.stabilizerEquivStabilizerOfOrbitRel), and
assembling these identifications with the orbit-stabilizer correspondence yields
[a bijection between the set of fixed pairs and the product of $X/G$ with $G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Quotient.html#MulAction.sigmaFixedByEquivOrbitsProdGroup).
Burnside's lemma is the comparison of the sizes of the two sides.

## Related concepts

- The [class formula](class-formula.md) uses the
  same orbit-stabilizer counting to write
  [$|X|$ as a sum, over the orbits, of $|G|$ divided by the order of a stabilizer](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/CardCommute.html#MulAction.card_eq_sum_card_group_div_card_stabilizer).
- When $G$ is a $p$-group for a prime $p$, every orbit with more than one point
  has size a positive power of $p$, so
  [$|X|$ is congruent modulo $p$ to the number of points fixed by all of $G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/PGroup.html#IsPGroup.card_modEq_card_fixedPoints).
  Mathlib states this for any group in which every element has order a power of
  $p$, acting on a finite set.
- The Pólya enumeration theorem refines Burnside's lemma for
  colourings, recording in a polynomial how many colourings of each type there are
  up to symmetry.

## In Mathlib

Mathlib states the lemma for a group acting on a type, assuming the group, each set
of fixed points and the set of orbits are finite rather than assuming the whole
type is finite; with a finite group and finitely many orbits this comes to the
same thing, since each orbit is no larger than the group. The orbits are the
classes of the orbit relation. To stay within the natural numbers the identity is
stated multiplied out, as a sum equal to a product, with no division. It is
derived from a bijection, built using choice and recorded separately as a
definition, so the counting statement is a direct consequence of comparing
cardinalities. An additive version
for additive groups is generated automatically. The commuting-pairs consequence is
stated for every group, with the convention that an infinite set has cardinality
$0$, so it is trivially true for infinite groups.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group](group.md)
- [Group action](group-action.md)
- [Orbit](../../../../undergraduate/group-theory/basic-definitions/orbit.md)

## Proof depends on

- [Stabilizer of a point](../../../../undergraduate/group-theory/basic-definitions/stabilizer-of-a-point.md)

## Sources

- [Mathlib documentation: `MulAction.sum_card_fixedBy_eq_card_orbits_mul_card_group`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Quotient.html#MulAction.sum_card_fixedBy_eq_card_orbits_mul_card_group)
- [Source of `MulAction.sum_card_fixedBy_eq_card_orbits_mul_card_group` in Mathlib/GroupTheory/GroupAction/Quotient.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/GroupAction/Quotient.lean#L260)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L37)
