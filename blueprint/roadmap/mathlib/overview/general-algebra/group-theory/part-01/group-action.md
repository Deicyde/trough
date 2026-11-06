# Group action

A **group action** of a [group](group.md) $G$ on a set $X$ lets each element of $G$
move the points of $X$, in a way that respects the group law: acting by a product is the
same as acting by the factors one after the other. Groups usually arise as groups of
symmetries of something, and an action records exactly that relationship. Actions let one
study a group through the sets it permutes, and a set through its symmetries, and they
underlie the main counting arguments of finite group theory: the orbit–stabilizer theorem,
the [class formula](class-formula.md),
[Burnside's lemma](burnside-lemma.md) and the
Sylow theorems.

## Definition

A (left) action of $G$ on $X$ is a map $G \times X \to X$, written $(g, x) \mapsto g \cdot x$,
such that for all $g, h \in G$ and $x \in X$

$$e \cdot x = x, \qquad (gh) \cdot x = g \cdot (h \cdot x),$$

where $e$ is the identity element. These two axioms are
[the definition of an action](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Action/Defs.html#MulAction). A set with an action of $G$ is called a
$G$-set.

Equivalently, an action is a [homomorphism](group-morphism.md) from $G$ to the
[group of permutations](../part-02/permutation-group-of-a-type.md) of $X$. Each $g$ gives a bijection
$x \mapsto g \cdot x$, whose inverse is the action of $g^{-1}$, so
[each element acts as a permutation of $X$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Action/Basic.html#MulAction.toPerm), and the two axioms say
precisely that [the assignment of $g$ to its permutation is a group homomorphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Action/End.html#MulAction.toPermHom).
Conversely, a homomorphism from $G$ into the monoid of all maps $X \to X$ under composition
(its image then consists of permutations) [defines an action](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Action/End.html#MulAction.ofEndHom).
Composing an action with a homomorphism $H \to G$
[gives an action of $H$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Action/Hom.html#MulAction.compHom); in particular every
[subgroup](subgroup.md) of $G$ acts on every $G$-set by restriction.

Right actions, written $x \cdot g$ with $x \cdot (gh) = (x \cdot g) \cdot h$, are defined
symmetrically; setting $g \cdot x = x \cdot g^{-1}$ turns a right action into a left one.

## Examples

- The permutation group of a set $X$
  [acts on $X$ by evaluation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Action/End.html#Equiv.Perm.applyMulAction), $\sigma \cdot x = \sigma(x)$.
- Every group [acts on itself by left multiplication](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Action/Defs.html#Monoid.toMulAction),
  $g \cdot h = gh$. Since $gh = h$ forces $g = e$, the corresponding homomorphism into the
  permutations of $G$ is injective, which is [Cayley's theorem](../part-02/cayleys-theorem.md).
- A group acts on itself by conjugation,
  [$g \cdot h = ghg^{-1}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/ConjAct.html#ConjAct.toConjAct_smul). Its orbits are the
  [conjugacy classes](../../../../undergraduate/group-theory/basic-definitions/conjugacy-classes.md), and the stabilizer of $h$ is its centralizer.
- For a subgroup $H$ of $G$, left multiplication $g \cdot xH = gxH$ is an action of $G$ on the
  set of left cosets of $H$.
- The [general linear group](../../../../undergraduate/group-theory/classical-automorphism-groups/general-linear-group.md) of invertible $n \times n$ real matrices acts on $\mathbb{R}^n$ by matrix
  multiplication, and the symmetry group of a cube acts on its vertices, edges and faces.

## Orbits, stabilizers and kinds of action

The [orbit](../../../../undergraduate/group-theory/basic-definitions/orbit.md) of a point $x$ is
[the set $G \cdot x = \{ g \cdot x : g \in G \}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Defs.html#MulAction.orbit). Lying in the same
orbit [is an equivalence relation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Defs.html#MulAction.orbitRel), so the orbits partition $X$;
the set of orbits is written $X/G$.

The [stabilizer](../../../../undergraduate/group-theory/basic-definitions/stabilizer-of-a-point.md) of $x$ is
[the subgroup $G_x = \{ g \in G : g \cdot x = x \}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Defs.html#MulAction.stabilizer). Points in one
orbit have conjugate stabilizers:
[$G_{g \cdot x} = g\,G_x\,g^{-1}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Basic.html#MulAction.stabilizer_smul_eq_stabilizer_map_conj).
The [points fixed by every element of $G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Defs.html#MulAction.fixedPoints) are those whose orbit is
a single point.

An action is **transitive** if it has exactly one orbit, that is, $X$ is nonempty and
[any point can be carried to any other](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Action/Pretransitive.html#MulAction.IsPretransitive). It is **faithful**
if [distinct elements of $G$ act differently](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Action/Faithful.html#FaithfulSMul), which for a group means that
only the identity fixes every point; a faithful action then makes the homomorphism to the
permutations of $X$ [injective](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Action/Basic.html#MulAction.toPerm_injective), and conversely. For nonempty
$X$, the action of the permutation group of $X$ on $X$ is both transitive and faithful.

## Orbit–stabilizer theorem

For each point $x$, the map $gG_x \mapsto g \cdot x$ is
[a bijection from the left cosets of $G_x$ onto the orbit of $x$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Quotient.html#MulAction.orbitEquivQuotientStabilizer).
It is well defined and injective because $g \cdot x = h \cdot x$ holds exactly when
$g^{-1}h \in G_x$, and it is surjective by the definition of the orbit. Hence the size of
the orbit is [the index of the stabilizer](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Index.html#MulAction.index_stabilizer) (see
[index of a subgroup](index-of-a-subgroup.md)), and for a finite
group [the size of the orbit times the order of the stabilizer is the order of the group](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Quotient.html#MulAction.card_orbit_mul_card_stabilizer_eq_card_group):

$$|G \cdot x|\,|G_x| = |G|.$$

In particular the size of every orbit divides $|G|$.

## Consequences

Summing the orbit–stabilizer theorem over the orbits gives the
[class formula](class-formula.md), which for the
conjugation action shows for instance that a nontrivial finite $p$-group has a nontrivial
center. Counting pairs $(g, x)$ with $g \cdot x = x$ in two ways gives
[Burnside's lemma](burnside-lemma.md): the
number of orbits is the average number of points fixed by an element. The Sylow theorems
come from actions of a group on its subsets and subgroups; the
[second Sylow theorem](../part-02/second-sylow-theorem.md) says that conjugation acts
transitively on the Sylow $p$-subgroups.

## Generalizations

The axioms make sense for any monoid in place of $G$, giving monoid actions; many
statements, such as the orbit–stabilizer theorem, need inverses. An action of a group on a
vector space by linear maps is a [representation](../../representation-theory/representation.md), and a ring acting
on an abelian group compatibly with both operations gives a [module](../../../linear-algebra/fundamentals/module.md). A
vector space acting freely and transitively on a nonempty set makes that set an
[affine space](../../../geometry/affine-and-euclidean-geometry/affine-space.md); for a general additive group, such a set is called a torsor.

## In Mathlib

Mathlib defines actions for an arbitrary monoid, not only a group, as a structure attached
to the pair of a monoid and a type, with the action written as a scalar multiplication. Its
actions are left actions; a right action is expressed as a left action of the opposite
monoid. A separately declared additive version, for additive monoids, uses its own symbol,
and most results about multiplicative actions are translated to it automatically.
Transitivity is stated as "pretransitivity", which does not require the set to be nonempty,
so any action on the empty set is pretransitive. The statement that the orbit has the size
of the index of the stabilizer uses Mathlib's convention that an infinite set has size 0 and
a subgroup of infinite index has index 0, so it holds for infinite orbits too. Because a group already acts on itself by left
multiplication, the conjugation action is placed on a separate copy of the group, so the two
actions do not clash.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group](group.md)
- [Set](../../../data-structures/sets/set.md)
- [Permutation group of a type](../part-02/permutation-group-of-a-type.md)
- [Group morphism](group-morphism.md)

## Sources

- [Mathlib documentation: `MulAction`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Action/Defs.html#MulAction)
- [Source of `MulAction` in Mathlib/Algebra/Group/Action/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Group/Action/Defs.lean#L121)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L35)
- [Mathlib undergraduate list: Group Theory › Basic definitions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L87)
