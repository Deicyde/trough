A **group action** of a [group](trough:Group) $G$ on a set $X$ lets each element of $G$
move the points of $X$, in a way that respects the group law: acting by a product is the
same as acting by the factors one after the other. Groups usually arise as groups of
symmetries of something, and an action records exactly that relationship. Actions let one
study a group through the sets it permutes, and a set through its symmetries, and they
underlie the main counting arguments of finite group theory: the orbit–stabilizer theorem,
the [class formula](trough:MulAction.selfEquivSigmaOrbitsQuotientStabilizer),
[Burnside's lemma](trough:MulAction.sum_card_fixedBy_eq_card_orbits_mul_card_group) and the
Sylow theorems.

## Definition

A (left) action of $G$ on $X$ is a map $G \times X \to X$, written $(g, x) \mapsto g \cdot x$,
such that for all $g, h \in G$ and $x \in X$

$$e \cdot x = x, \qquad (gh) \cdot x = g \cdot (h \cdot x),$$

where $e$ is the identity element. These two axioms are
the definition of an action. A set with an action of $G$ is called a
$G$-set.

Equivalently, an action is a [homomorphism](trough:MonoidHom) from $G$ to the
[group of permutations](trough:Equiv.Perm) of $X$. Each $g$ gives a bijection
$x \mapsto g \cdot x$, whose inverse is the action of $g^{-1}$, so
each element acts as a permutation of $X$, and the two axioms say
precisely that the assignment of $g$ to its permutation is a group homomorphism.
Conversely, a homomorphism from $G$ into the monoid of all maps $X \to X$ under composition
(its image then consists of permutations) defines an action.
Composing an action with a homomorphism $H \to G$
gives an action of $H$; in particular every
[subgroup](trough:Subgroup) of $G$ acts on every $G$-set by restriction.

Right actions, written $x \cdot g$ with $x \cdot (gh) = (x \cdot g) \cdot h$, are defined
symmetrically; setting $g \cdot x = x \cdot g^{-1}$ turns a right action into a left one.

## Examples

- The permutation group of a set $X$
  acts on $X$ by evaluation, $\sigma \cdot x = \sigma(x)$.
- Every group acts on itself by left multiplication,
  $g \cdot h = gh$. Since $gh = h$ forces $g = e$, the corresponding homomorphism into the
  permutations of $G$ is injective, which is [Cayley's theorem](trough:Equiv.Perm.subgroupOfMulAction).
- A group acts on itself by conjugation,
  $g \cdot h = ghg^{-1}$. Its orbits are the
  [conjugacy classes](trough:ConjClasses), and the stabilizer of $h$ is its centralizer.
- For a subgroup $H$ of $G$, left multiplication $g \cdot xH = gxH$ is an action of $G$ on the
  set of left cosets of $H$.
- The [general linear group](trough:Matrix.GeneralLinearGroup) of invertible $n \times n$ real matrices acts on $\mathbb{R}^n$ by matrix
  multiplication, and the symmetry group of a cube acts on its vertices, edges and faces.

## Orbits, stabilizers and kinds of action

The [orbit](trough:MulAction.orbit) of a point $x$ is
the set $G \cdot x = \{ g \cdot x : g \in G \}$. Lying in the same
orbit is an equivalence relation, so the orbits partition $X$;
the set of orbits is written $X/G$.

The [stabilizer](trough:MulAction.stabilizer) of $x$ is
the subgroup $G_x = \{ g \in G : g \cdot x = x \}$. Points in one
orbit have conjugate stabilizers:
$G_{g \cdot x} = g\,G_x\,g^{-1}$.
The points fixed by every element of $G$ are those whose orbit is
a single point.

An action is **transitive** if it has exactly one orbit, that is, $X$ is nonempty and
any point can be carried to any other. It is **faithful**
if distinct elements of $G$ act differently, which for a group means that
only the identity fixes every point; a faithful action then makes the homomorphism to the
permutations of $X$ injective, and conversely. For nonempty
$X$, the action of the permutation group of $X$ on $X$ is both transitive and faithful.

## Orbit–stabilizer theorem

For each point $x$, the map $gG_x \mapsto g \cdot x$ is
a bijection from the left cosets of $G_x$ onto the orbit of $x$.
It is well defined and injective because $g \cdot x = h \cdot x$ holds exactly when
$g^{-1}h \in G_x$, and it is surjective by the definition of the orbit. Hence the size of
the orbit is the index of the stabilizer (see
[index of a subgroup](trough:Subgroup.index)), and for a finite
group the size of the orbit times the order of the stabilizer is the order of the group:

$$|G \cdot x|\,|G_x| = |G|.$$

In particular the size of every orbit divides $|G|$.

## Consequences

Summing the orbit–stabilizer theorem over the orbits gives the
[class formula](trough:MulAction.selfEquivSigmaOrbitsQuotientStabilizer), which for the
conjugation action shows for instance that a nontrivial finite $p$-group has a nontrivial
center. Counting pairs $(g, x)$ with $g \cdot x = x$ in two ways gives
[Burnside's lemma](trough:MulAction.sum_card_fixedBy_eq_card_orbits_mul_card_group): the
number of orbits is the average number of points fixed by an element. The Sylow theorems
come from actions of a group on its subsets and subgroups; the
[second Sylow theorem](trough:Sylow.isPretransitive_of_finite) says that conjugation acts
transitively on the Sylow $p$-subgroups.

## Generalizations

The axioms make sense for any monoid in place of $G$, giving monoid actions; many
statements, such as the orbit–stabilizer theorem, need inverses. An action of a group on a
vector space by linear maps is a [representation](trough:Representation), and a ring acting
on an abelian group compatibly with both operations gives a [module](trough:Module). A
vector space acting freely and transitively on a nonempty set makes that set an
[affine space](trough:AddTorsor); for a general additive group, such a set is called a torsor.

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

## Depends on

- [Group](trough:Group)
- [Set](trough:Set)
- [Permutation group of a type](trough:Equiv.Perm)
- [Group morphism](trough:MonoidHom)
