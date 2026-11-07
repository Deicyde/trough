The **stabilizer** of a point under a [group action](trough:MulAction) is the set of group
elements that leave the point where it is. It is always a [subgroup](trough:Subgroup) of the
acting group, and it measures how much symmetry the point retains: the larger the
stabilizer, the smaller the [orbit](trough:MulAction.orbit). This trade-off, the
orbit–stabilizer theorem, turns questions about group actions into questions about
subgroups and their indices, and it is the basic counting tool behind the class equation,
Burnside's lemma and the Sylow theorems.

## Definition

Let a [group](trough:Group) $G$ act on a set $X$, and write $g \cdot x$ for the action of
$g \in G$ on $x \in X$. The stabilizer of $x$ is the subgroup

$$G_x = \{\, g \in G : g \cdot x = x \,\}.$$

Thus an element $g$ lies in $G_x$ exactly when $g \cdot x = x$.
Other common notations are $\operatorname{Stab}_G(x)$ and $\operatorname{Stab}(x)$; the
stabilizer is also called the isotropy group of $x$.

The set $G_x$ is a subgroup. The identity fixes every point. If $g$ and $h$ fix $x$, then
$(gh) \cdot x = g \cdot (h \cdot x) = x$, and applying $g^{-1}$ to both sides of
$g \cdot x = x$ gives $g^{-1} \cdot x = x$.

## Examples

- **Symmetric groups.** The [symmetric group](trough:Equiv.Perm) $S_n$ acts on
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
  $g \cdot aH = gaH$. The stabilizer of the coset $H$ is $H$ itself,
  and the stabilizer of a coset $aH$ is the conjugate $aHa^{-1}$.
- **Conjugation.** A group acts on itself by conjugation, $g \cdot h = g h g^{-1}$, and
  the stabilizer of $h$ under this action is the centralizer of $h$,
  the subgroup of elements that commute with $h$. The orbits of this action are the
  [conjugacy classes](trough:ConjClasses).
- **Free actions.** When $G$ acts on itself by left multiplication, $gh = h$ forces $g$ to be the identity,
  so every stabilizer is trivial. An action is called free when every stabilizer is trivial.

## Properties

**Stabilizers along an orbit.** Stabilizers of points in the same orbit are conjugate: for
every $g$ in $G$,
the stabilizer of $g \cdot x$ is $g G_x g^{-1}$.
Indeed $h$ fixes $g \cdot x$ exactly when $g^{-1} h g$ fixes $x$. Consequently, if
$y = g \cdot x$, then
conjugation by $g$ is
an isomorphism from $G_x$ onto $G_y$.
A stabilizer need not be normal: for the action on $G/H$ the stabilizers are exactly the
conjugates of $H$, and they all equal $H$ only when $H$ is normal.

**Orbit–stabilizer theorem.** Two elements $g$ and $h$ send $x$ to the same point exactly
when $g^{-1}h \in G_x$, that is, when they lie in the same left coset of $G_x$. So
$g G_x \mapsto g \cdot x$ is
a bijection from the set of left cosets of $G_x$ onto the orbit of $x$,
and the index of $G_x$ equals the size of the orbit of $x$.
For a finite group $G$,
the size of the orbit times the order of the stabilizer is the order of $G$:

$$|G \cdot x| \cdot |G_x| = |G|.$$

In particular both factors divide $|G|$, in line with
[Lagrange's theorem](trough:Subgroup.card_subgroup_dvd_card).
For a transitive action, where the orbit is all of $X$,
the index of every stabilizer is the number of points of $X$.
Summing over the orbits of a finite set gives the
[class formula](trough:MulAction.selfEquivSigmaOrbitsQuotientStabilizer), and counting the
pairs $(g, x)$ with $g \cdot x = x$ in two ways, once by points and once by group elements,
gives [Burnside's lemma](trough:MulAction.sum_card_fixedBy_eq_card_orbits_mul_card_group).

**Free actions.** Mathlib expresses freeness as a cancellation law: $g \cdot x = h \cdot x$
implies $g = h$, and each $g$ acts injectively (which is automatic for a group action).
A group action satisfies this law exactly when every stabilizer is trivial.

**Intersections of stabilizers.** For a subset $S$ of $X$,
an element lies in the pointwise stabilizer of $S$ exactly when it fixes every point of $S$,
so the pointwise stabilizer is the intersection of the stabilizers $G_x$ for $x$ in $S$.
Taking $S = X$ gives the kernel of the action, the set of elements that act as the
identity; it is a [normal subgroup](trough:Subgroup.Normal), and the action is faithful
exactly when it is trivial. The setwise stabilizer of $S$ is the stabilizer of $S$ as a
point of the induced action on subsets:
an element $g$ lies in it exactly when, for every $y$ in $X$, $g \cdot y$ lies in $S$ if and only if $y$ does.

## Related concepts

Applied to the action of a group on its subgroups by conjugation, the stabilizer of a
subgroup is its normalizer. Mathlib states this for Sylow subgroups:
the stabilizer of a Sylow $p$-subgroup $P$ under conjugation is the normalizer of $P$.
In a finite group the Sylow $p$-subgroups form a single orbit by the
[second Sylow theorem](trough:Sylow.isPretransitive_of_finite), so by the orbit–stabilizer
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

## Depends on

- [Group action](trough:MulAction)
- [Subgroup](trough:Subgroup)
- [Group](trough:Group)
