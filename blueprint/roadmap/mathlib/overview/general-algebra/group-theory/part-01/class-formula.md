# Class formula

The **class formula** describes how a set on which a [group](group.md) acts
breaks up into pieces. The set is the disjoint union of its
[orbits](../../../../undergraduate/group-theory/basic-definitions/orbit.md), and each orbit is a copy of the set of cosets of
the [stabilizer](../../../../undergraduate/group-theory/basic-definitions/stabilizer-of-a-point.md) of any of its points. For a finite
group acting on a finite set this turns into a counting rule: the size of the set
is a sum of [indices](index-of-a-subgroup.md) of subgroups, and each term divides
the order of the group. Applied to the action of a group on itself by
conjugation, it gives the class equation, the standard tool for proving that
nontrivial groups of prime power order have a nontrivial centre.

## Statement

Let $G$ be a group acting on a set $X$ (see [group action](group-action.md)).
The orbits $G \cdot x = \{ g \cdot x : g \in G \}$ partition $X$; write $X/G$
for the set of orbits and choose one point $x_\omega$ in each orbit $\omega$.
Let $G_x = \{ g \in G : g \cdot x = x \}$ be the stabilizer of $x$. Then
[there is a bijection](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Quotient.html#MulAction.selfEquivSigmaOrbitsQuotientStabilizer)

$$X \;\cong\; \coprod_{\omega \in X/G} G / G_{x_\omega},$$

between $X$ and the disjoint union, over all orbits, of the sets of left cosets
of the chosen stabilizers. If $G$ and $X$ are finite, counting both sides
[gives the class formula](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/CardCommute.html#MulAction.card_eq_sum_card_group_div_card_stabilizer)

$$|X| \;=\; \sum_{\omega \in X/G} \frac{|G|}{|G_{x_\omega}|} \;=\; \sum_{\omega \in X/G} [G : G_{x_\omega}].$$

The choice of representatives does not matter: points of the same orbit have
conjugate stabilizers, which have the same index.

## Proof

Sending each point to its orbit shows that $X$ is
[the disjoint union of its orbits](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Defs.html#MulAction.selfEquivSigmaOrbits). It
remains to identify a single orbit $G \cdot x$ with $G/G_x$. The map
$gG_x \mapsto g \cdot x$ is well defined and injective, because
$g \cdot x = h \cdot x$ holds exactly when $g^{-1}h \in G_x$, that is, when
$gG_x = hG_x$; it is surjective by the definition of the orbit. This is the
[orbit–stabilizer theorem](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Quotient.html#MulAction.orbitEquivQuotientStabilizer), and in
the finite case it reads
[$|G \cdot x| \, |G_x| = |G|$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Quotient.html#MulAction.card_orbit_mul_card_stabilizer_eq_card_group).
Assembling these bijections orbit by orbit gives the statement, and
[Lagrange's theorem](../part-02/lagranges-theorem.md) turns the number of
cosets into $|G|/|G_x|$.

## Examples

- **Colourings of a square.** The cyclic group of order $4$, acting on the
  $16$ ways to colour the corners of a square black or white by rotating the
  square, has six orbits. The two one-colour colourings are fixed by every
  rotation, so each forms an orbit of size $1$. The colouring with two opposite
  black corners is fixed by the half-turn, so its stabilizer has index $2$.
  The colourings with one black corner, three black corners, or two adjacent
  black corners have trivial stabilizers and orbits of size $4$. The formula
  checks out as $16 = 1 + 1 + 2 + 4 + 4 + 4$.
- **Transitive actions.** If there is a single orbit, the formula says that
  $X$ is a copy of $G/G_x$ for any $x$, so the
  [index of a stabilizer is the size of the set](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Index.html#MulAction.index_stabilizer_of_transitive).
- **Conjugation.** A group acts on itself by $g \cdot h = ghg^{-1}$. The orbits
  are the [conjugacy classes](../../../../undergraduate/group-theory/basic-definitions/conjugacy-classes.md) and the stabilizer of $h$ is its
  centralizer $C_G(h)$, so in a finite group
  [the class of $h$ has $|G|/|C_G(h)|$ elements](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Quotient.html#ConjClasses.card_carrier).

## Consequences

- **The class equation.** For a finite group $G$ with centre $Z(G)$, the
  conjugacy classes with one element are exactly the elements of the centre, and
  collecting them gives
  [the class equation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/ClassEquation.html#Group.nat_card_center_add_sum_card_noncenter_eq_card)
  $$|G| \;=\; |Z(G)| + \sum_{i} |\mathrm{cl}(h_i)| \;=\; |Z(G)| + \sum_{i} [G : C_G(h_i)],$$
  where $h_i$ runs over representatives of the conjugacy classes with more than
  one element, $\mathrm{cl}(h_i)$ is the class of $h_i$, and the second equality
  is the count of a conjugacy class from the previous section.
- **Fixed points of $p$-groups.** Fix a prime $p$. A finite group is a
  $p$-group if its order is a power of $p$; more generally, a group is a
  $p$-group if every element has order a power of $p$. If $G$ is a $p$-group and
  $X$ is finite, every orbit has size a power of $p$, being the index of a
  subgroup of $G$, and only the fixed points give
  orbits of size $1$. Hence
  [$|X|$ is congruent modulo $p$ to the number of fixed points](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/PGroup.html#IsPGroup.card_modEq_card_fixedPoints).
  In particular,
  [if $p$ does not divide $|X|$, the action has a fixed point](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/PGroup.html#IsPGroup.nonempty_fixed_point_of_prime_not_dvd_card).
- **Centres of $p$-groups.** Applying the previous point to conjugation shows
  that [a nontrivial finite $p$-group has a nontrivial centre](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/PGroup.html#IsPGroup.center_nontrivial).
  If $|G| = p^2$, the quotient $G/Z(G)$ then has order $1$ or $p$, so it is
  cyclic, and
  [a group whose quotient by its centre is cyclic is commutative](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Cyclic.html#isMulCommutative_of_isCyclic_quotient_center_self).
  Hence
  [every group of order $p^2$ is commutative](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/PGroup.html#IsPGroup.isMulCommutative_of_card_eq_prime_sq).
- **Counting orbits.** Summing the orders of the stabilizers over all points leads to the
  [Burnside lemma](burnside-lemma.md),
  which counts the orbits of a finite group action by averaging numbers of fixed
  points. Arguments of the same kind drive the proofs of
  [Cauchy's theorem](../../../../thousand-plus/algebra/20-group-theory-and-generalizations/cauchys-theorem-group-theory.md), the
  [first Sylow theorem](../part-02/first-sylow-theorem.md) and the
  [third](../part-02/third-sylow-theorem.md).

## In Mathlib

Mathlib states the class formula first as a bijection rather than an equation,
and for an arbitrary group acting on an arbitrary type, finite or not. The
representative of each orbit is the one supplied by the axiom of choice; a
companion version accepts any function that picks a point in each orbit. The
counting form assumes that the group and the set are finite and writes each term
as a quotient of natural numbers, $|G|$ divided by the order of the stabilizer,
which is exact because the stabilizer's order divides $|G|$. The class equation
is stated for finite groups, with the sum running over the conjugacy classes
that have more than one element; each term is the number of elements of the
class rather than the index of its centralizer, and the size of the centre is
counted the same way. A $p$-group in Mathlib is a group in which
every element has order a power of $p$, so the fixed-point congruence needs
only the set, not the group, to be finite.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group action](group-action.md)
- [Orbit](../../../../undergraduate/group-theory/basic-definitions/orbit.md)
- [Stabilizer of a point](../../../../undergraduate/group-theory/basic-definitions/stabilizer-of-a-point.md)
- [Index of a subgroup](index-of-a-subgroup.md)

## Proof depends on

- [Lagrange's theorem](../part-02/lagranges-theorem.md)

## Sources

- [Mathlib documentation: `MulAction.selfEquivSigmaOrbitsQuotientStabilizer`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Quotient.html#MulAction.selfEquivSigmaOrbitsQuotientStabilizer)
- [Source of `MulAction.selfEquivSigmaOrbitsQuotientStabilizer` in Mathlib/GroupTheory/GroupAction/Quotient.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/GroupAction/Quotient.lean#L226)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L36)
- [Mathlib undergraduate list: Group Theory › Basic definitions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L91)
