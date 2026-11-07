The **conjugacy classes** of a [group](trough:Group) are the pieces into which the
group splits when elements that differ only by a change of viewpoint, $a$ and
$gag^{-1}$, are counted as the same. They are the orbits of the group acting on
itself by conjugation. They carry much of the structure of a finite group: the
class equation built from their sizes shows that nontrivial finite groups of
prime-power order have a nontrivial center, a
[normal subgroup](trough:Subgroup.Normal) is a union of them, and their number
equals the number of irreducible complex characters.

## Definition

Let $G$ be a group with identity $e$. Two elements $a, b \in G$ are *conjugate* when
$b = gag^{-1}$ for some $g \in G$. Conjugacy
is an equivalence relation: $a = eae^{-1}$, if $b = gag^{-1}$
then $a = g^{-1}bg$, and if moreover $c = hbh^{-1}$ then $c = (hg)a(hg)^{-1}$. Its
equivalence classes are the conjugacy classes of $G$. The class of $a$ is

$$\operatorname{Cl}(a) = \{\, gag^{-1} : g \in G \,\},$$

and the set of all classes is the quotient of $G$ by conjugacy, so
that two elements have the same class exactly when they are conjugate.
Equivalently, $G$ [acts](trough:MulAction) on itself by $g \cdot x = gxg^{-1}$, and
the class of $a$ is the orbit of $a$ under this action
(see [orbit](trough:MulAction.orbit)).

## Examples

- **Abelian groups.** In a commutative group, $gag^{-1} = a$ for all $g$, so
  conjugacy is equality: every class has one element and
  the classes correspond one to one with the elements.
- **The identity.** In any group, the identity is conjugate only to itself,
  so $\{e\}$ is always a class.
- **Symmetric groups.** In the [symmetric group](trough:Equiv.Perm) on a finite set,
  two permutations are conjugate exactly when they have the same cycle type,
  that is, the same multiset of cycle lengths in their
  [decomposition into disjoint cycles](trough:Equiv.Perm.truncCycleFactors). For $S_n$,
  conjugacy amounts to equality of the partitions of $n$ the permutations determine,
  and every partition occurs, so $S_n$ has as many classes as $n$ has partitions. In
  $S_3$ the classes are the identity, the three transpositions and the two
  $3$-cycles, of sizes $1 + 3 + 2 = 6$.
- **Dihedral groups.** For odd $n$ the dihedral group of order $2n$
  has $(n+3)/2$ conjugacy classes: the
  identity, the $(n-1)/2$ pairs of mutually inverse nontrivial rotations, and one
  class containing all $n$ reflections.
- **Matrix groups.** In the [general linear group](trough:Matrix.GeneralLinearGroup)
  over a field, conjugacy is similarity of invertible matrices. Over an
  algebraically closed field, two invertible matrices are conjugate exactly when
  they have the same Jordan normal form
  up to the order of the blocks.

## Properties

- **Size of a class.** The *centralizer* $C_G(a) = \{ g \in G : ga = ag \}$ is the
  [stabilizer](trough:MulAction.stabilizer) of $a$ under conjugation, and
  the size of the class of $a$ equals the index of $C_G(a)$
  (see [index of a subgroup](trough:Subgroup.index)).
  For a finite group, [Lagrange's theorem](trough:Subgroup.card_subgroup_dvd_card)
  then shows that the size of every class divides $|G|$.
- **Central elements.** The *center* $Z(G)$ consists of the elements that commute
  with every element of $G$. An element is central exactly when its class has a
  single element: sending each element to its class is a bijection from $Z(G)$ onto the one-element classes.
- **The class equation.** For a finite group the classes partition $G$, so
  their sizes add up to $|G|$. Separating
  the one-element classes gives the class equation

  $$|G| = |Z(G)| + \sum_{i=1}^{r} |\operatorname{Cl}(a_i)|,$$

  where $a_1, \dots, a_r$ represent the classes with more than one element. It is
  the [class formula](trough:MulAction.selfEquivSigmaOrbitsQuotientStabilizer) for
  the conjugation action. If $|G| = p^n$ with $p$ prime and $n \ge 1$, each
  $|\operatorname{Cl}(a_i)|$ is a power of $p$ greater than $1$ and $p$ divides
  $|G|$, so $p$ divides $|Z(G)|$: every nontrivial finite group of prime-power order has a nontrivial center.
- **Invariants of a class.** If $y = axa^{-1}$, then $x$ and $y$
  have the same order (see
  [order of an element](trough:orderOf)), and
  a homomorphism sends conjugate elements to conjugate elements
  (see [group morphism](trough:MonoidHom)).
- **Normal subgroups.** A normal subgroup
  contains the whole class of each of its elements,
  so it is a union of conjugacy classes; conversely, a subgroup that is a union of
  classes is normal. Since a normal subgroup contains the class $\{e\}$ and its order
  divides $|G|$, class sizes limit the possible normal subgroups. The
  [alternating group](trough:alternatingGroup) $A_5$ has classes of sizes
  $1, 12, 12, 15, 20$, and no sum of these that includes $1$ divides $60$ except
  $1$ and $60$, so $A_5$ is [simple](trough:IsSimpleGroup).
- **Commuting pairs.** For a finite group with $k$ conjugacy classes,
  the number of ordered pairs of commuting elements is $k\,|G|$,
  so two elements chosen uniformly at random commute with probability $k/|G|$.

## Related concepts

A class function
is a function on $G$ that is constant on each conjugacy class. The characters of
the irreducible complex representations of a finite group form an
orthonormal basis
of the space of class functions, so their number equals the number of conjugacy
classes. Conjugation also acts on subgroups, sending $H$ to $gHg^{-1}$; the
[second Sylow theorem](trough:Sylow.isPretransitive_of_finite) says that the Sylow
$p$-subgroups of a finite group form a single class under this action.

## In Mathlib

Mathlib defines conjugacy classes for any monoid, not only for groups: $a$ and $b$
are conjugate when $cac^{-1} = b$ for some invertible element $c$. In a group every
element is invertible, so this is the usual notion. The conjugacy classes form a
quotient type, with a map sending each element to its class and, for each class,
the set of its elements. Sizes are measured with natural-number cardinality, which
is $0$ for an infinite set, and the index of a subgroup is likewise $0$ when it
is infinite; with these conventions the equality between the size of
a class and the index of the centralizer, and the count of commuting pairs, hold
for every group, while the class equation and the partition of $G$ into classes
are stated for finite groups. An additive version covers additive groups.

## Depends on

- [Group](trough:Group)
