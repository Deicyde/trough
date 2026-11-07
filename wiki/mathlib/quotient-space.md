The **quotient space** $G/H$ of a [group](trough:Group) $G$ by a
[subgroup](trough:Subgroup) $H$ is the set of left cosets $aH$ of $H$ in $G$.
It is not a group in general, but $G$ acts on it by left multiplication, and
this action is the model for every transitive [group action](trough:MulAction):
by the **orbit-stabilizer theorem**, each [orbit](trough:MulAction.orbit) of an
action of $G$ is a copy of the quotient of $G$ by the
[stabilizer](trough:MulAction.stabilizer) of any of its points. Counting
arguments in finite group theory, from [Lagrange's
theorem](trough:Subgroup.card_subgroup_dvd_card) to the [class
formula](trough:MulAction.selfEquivSigmaOrbitsQuotientStabilizer), rest on this
identification.

## Definition

Let $H$ be a subgroup of a group $G$. Call $a, b \in G$ equivalent when
$a^{-1}b \in H$; this is an equivalence relation whose classes are the left
cosets $aH = \{ah : h \in H\}$. The quotient space $G/H$ is the set of these
classes, so that $aH = bH$ exactly when $a^{-1}b \in H$.
Its number of elements is the [index](trough:Subgroup.index) $[G : H]$.

The group $G$ acts on $G/H$ by
$g \cdot (aH) = (ga)H$. This action is
transitive, since $(ba^{-1}) \cdot
(aH) = bH$, and the stabilizer of the coset $H$ itself is
$H$.

The right cosets $Ha$ form a second quotient space, but nothing new arises in
counting: $Ha \mapsto a^{-1}H$ is a well-defined
bijection from right cosets to left cosets.

## Orbit-stabilizer theorem

Let $G$ act on a set $X$ and let $x \in X$, with orbit $G \cdot x$ and
stabilizer $G_x = \{g \in G : g \cdot x = x\}$. The theorem states that

$$G/G_x \to G \cdot x, \qquad gG_x \mapsto g \cdot x$$

is well defined and a bijection.
Mathlib states the bijection from the orbit to $G/G_x$, and its inverse
sends $gG_x$ to $g \cdot x$.
The map is compatible with the actions:
the image of $g \cdot c$ is $g$ applied to the image of $c$
for every coset $c$. Thus every transitive action of $G$ on a nonempty set is, up
to relabelling the points, the action of $G$ on some quotient space $G/K$.

In terms of size, the index of $G_x$ equals the number of points of the orbit
of $x$. When $G$ is finite,
$|G \cdot x| \cdot |G_x| = |G|$,
so the size of every orbit divides the order of $G$.

## Proof

If $g G_x = h G_x$, then $g^{-1}h$ fixes $x$, so $h \cdot x = g \cdot
(g^{-1}h) \cdot x = g \cdot x$; the map is well defined. Reading the same
computation backwards, $g \cdot x = h \cdot x$ forces $g^{-1}h \in G_x$, so the
map is injective. Every point of the orbit has the form $g \cdot x$, so the map
is surjective. Compatibility with the action is the identity
$(g'g) \cdot x = g' \cdot (g \cdot x)$.

## Examples

- **Integers modulo $n$.** For $n \ge 1$, the quotient of the additive group
  $\mathbb{Z}$ by $n\mathbb{Z}$ consists of the $n$ cosets
  $r + n\mathbb{Z}$ with $0 \le r < n$. Here $n\mathbb{Z}$ is normal, so the
  quotient space is also a group.
- **Permutations.** The [permutation group](trough:Equiv.Perm) $S_3$ acts
  transitively on $\{1, 2, 3\}$, and the stabilizer of $3$ is the subgroup
  $\{e, (1\,2)\}$ of order $2$. Its three cosets correspond to the three
  points, and $6 = 3 \cdot 2$.
- **The sphere.** The [rotation group](trough:Matrix.specialOrthogonalGroup)
  $SO(3)$ acts transitively on the unit sphere in $\mathbb{R}^3$, and the
  stabilizer of the north pole is the group of rotations about the vertical
  axis, a copy of $SO(2)$. The sphere is therefore in bijection with
  $SO(3)/SO(2)$.
- **Conjugation.** Let $G$ act on itself by $g \cdot a = gag^{-1}$. The orbit of
  $a$ is its [conjugacy class](trough:ConjClasses) and the stabilizer is the
  centralizer of $a$, so in a finite group the size of a conjugacy class is the
  index of a centralizer and divides $|G|$.

## Consequences

- **Lagrange's theorem.** Since the cosets of $H$ all have $|H|$ elements and
  partition $G$,
  $|G| = |G/H| \cdot |H|$.
- **Class formula.** Splitting a finite set $X$ into orbits and applying the
  theorem to each orbit writes $|X|$ as a sum of indices $[G : G_x]$, one for
  each orbit; in Mathlib this is
  a bijection between $X$ and the disjoint union of the quotients $G/G_x$,
  one $x$ chosen in each orbit.
- **[Burnside's lemma](trough:MulAction.sum_card_fixedBy_eq_card_orbits_mul_card_group).**
  For a finite group acting on a finite set, the average number of points fixed
  by an element of the group is the number of orbits; its proof counts pairs $(g, x)$ with $g \cdot x = x$ by
  the orbit-stabilizer theorem.

## Related concepts

When $H$ is a [normal subgroup](trough:Subgroup.Normal), the multiplication
$(aH)(bH) = (ab)H$ is well defined and makes $G/H$ the
[quotient group](trough:QuotientGroup.Quotient.group). The
[quotient of a vector space](trough:Submodule.hasQuotient) by a subspace is the
analogous construction in linear algebra, where the additive group is abelian,
so every subspace is a normal subgroup and the quotient is again a vector space. Quotient
spaces of topological or Lie groups by closed subgroups are the homogeneous
spaces of geometry, such as the sphere above.

## In Mathlib

Mathlib defines the quotient of a group by a subgroup for every subgroup, as
the quotient by the left-coset relation; the same notation denotes the quotient
group when the subgroup is normal, and the group structure is then an extra
instance on the same set. The action of $G$ on $G/H$ is a special case of a more
general construction that lets any monoid acting compatibly on $G$ act on the
quotient. The orbit-stabilizer theorem is stated as an explicit bijection,
written in the direction from the orbit to the quotient, with no finiteness
assumption. The numerical version through the index uses natural-number
cardinality, which is $0$ for an infinite set, so it holds for every group: an
infinite orbit and a stabilizer of infinite index both count as $0$. The same
convention makes the formula $|G| = |G/H| \cdot |H|$ hold for every group and
subgroup, with both sides $0$ when $G$ is infinite. The
product formula for orbits and stabilizers assumes that the group is finite.

## Depends on

- [Group](trough:Group)
- [Subgroup](trough:Subgroup)
- [Group action](trough:MulAction)
- [Orbit](trough:MulAction.orbit)
- [Stabilizer of a point](trough:MulAction.stabilizer)
