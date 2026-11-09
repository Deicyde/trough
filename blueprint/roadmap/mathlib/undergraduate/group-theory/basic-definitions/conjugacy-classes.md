# Conjugacy classes

The **conjugacy classes** of a [group](../../../overview/general-algebra/group-theory/part-01/group.md) are the pieces into which the
group splits when elements that differ only by a change of viewpoint, $a$ and
$gag^{-1}$, are counted as the same. They are the orbits of the group acting on
itself by conjugation. They carry much of the structure of a finite group: the
class equation built from their sizes shows that nontrivial finite groups of
prime-power order have a nontrivial center, a
[normal subgroup](../../../overview/general-algebra/group-theory/part-01/normal-subgroup.md) is a union of them, and their number
equals the number of irreducible complex characters.

## Definition

Let $G$ be a group with identity $e$. Two elements $a, b \in G$ are *conjugate* when
[$b = gag^{-1}$ for some $g \in G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Conj.html#isConj_iff). Conjugacy
[is an equivalence relation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Conj.html#IsConj.setoid): $a = eae^{-1}$, if $b = gag^{-1}$
then $a = g^{-1}bg$, and if moreover $c = hbh^{-1}$ then $c = (hg)a(hg)^{-1}$. Its
equivalence classes are the conjugacy classes of $G$. The class of $a$ is

$$\operatorname{Cl}(a) = \{\, gag^{-1} : g \in G \,\},$$

and the set of all classes is the [quotient of $G$ by conjugacy](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Conj.html#ConjClasses), so
that [two elements have the same class exactly when they are conjugate](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Conj.html#ConjClasses.mk_eq_mk_iff_isConj).
Equivalently, $G$ [acts](../../../overview/general-algebra/group-theory/part-01/group-action.md) on itself by $g \cdot x = gxg^{-1}$, and
[the class of $a$ is the orbit of $a$ under this action](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/ConjAct.html#ConjAct.orbit_eq_carrier_conjClasses)
(see [orbit](orbit.md)).

## Examples

- **Abelian groups.** In a commutative group, $gag^{-1} = a$ for all $g$, so
  [conjugacy is equality](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Conj.html#isConj_iff_eq): every class has one element and
  [the classes correspond one to one with the elements](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Conj.html#ConjClasses.mkEquiv).
- **The identity.** In any group, [the identity is conjugate only to itself](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Conj.html#isConj_one_right),
  so $\{e\}$ is always a class.
- **Symmetric groups.** In the [symmetric group](../../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md) on a finite set,
  [two permutations are conjugate exactly when they have the same cycle type](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Type.html#Equiv.Perm.isConj_iff_cycleType_eq),
  that is, the same multiset of cycle lengths in their
  [decomposition into disjoint cycles](../permutation-group/decomposition-into-cycles-with-disjoint-support.md). For $S_n$,
  [conjugacy amounts to equality of the partitions of $n$ the permutations determine](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Type.html#Equiv.Perm.partition_eq_of_isConj),
  and every partition occurs, so $S_n$ has as many classes as $n$ has partitions. In
  $S_3$ the classes are the identity, the three transpositions and the two
  $3$-cycles, of sizes $1 + 3 + 2 = 6$.
- **Dihedral groups.** For odd $n$ the dihedral group of order $2n$
  [has $(n+3)/2$ conjugacy classes](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Dihedral.html#DihedralGroup.card_conjClasses_odd): the
  identity, the $(n-1)/2$ pairs of mutually inverse nontrivial rotations, and one
  class containing all $n$ reflections.
- **Matrix groups.** In the [general linear group](../classical-automorphism-groups/general-linear-group.md)
  over a field, conjugacy is similarity of invertible matrices. Over an
  algebraically closed field, two invertible matrices are conjugate exactly when
  they have the same Jordan normal form
  up to the order of the blocks.

## Properties

- **Size of a class.** The *centralizer* $C_G(a) = \{ g \in G : ga = ag \}$ is the
  [stabilizer](stabilizer-of-a-point.md) of $a$ under conjugation, and
  [the size of the class of $a$ equals the index of $C_G(a)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Index.html#Subgroup.index_centralizer_eq_ncard)
  (see [index of a subgroup](../../../overview/general-algebra/group-theory/part-01/index-of-a-subgroup.md)).
  For a finite group, [Lagrange's theorem](../../../overview/general-algebra/group-theory/part-02/lagranges-theorem.md)
  then shows that the size of every class divides $|G|$.
- **Central elements.** The *center* $Z(G)$ consists of the elements that commute
  with every element of $G$. An element is central exactly when its class has a
  single element: [sending each element to its class is a bijection from $Z(G)$ onto the one-element classes](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Subgroup/Center.html#ConjClasses.mk_bijOn).
- **The class equation.** For a finite group the classes partition $G$, so
  [their sizes add up to $|G|$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/ClassEquation.html#Group.sum_card_conj_classes_eq_card). Separating
  the one-element classes gives the [class equation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/ClassEquation.html#Group.nat_card_center_add_sum_card_noncenter_eq_card)

  $$|G| = |Z(G)| + \sum_{i=1}^{r} |\operatorname{Cl}(a_i)|,$$

  where $a_1, \dots, a_r$ represent the classes with more than one element. It is
  the [class formula](../../../overview/general-algebra/group-theory/part-01/class-formula.md) for
  the conjugation action. If $|G| = p^n$ with $p$ prime and $n \ge 1$, each
  $|\operatorname{Cl}(a_i)|$ is a power of $p$ greater than $1$ and $p$ divides
  $|G|$, so $p$ divides $|Z(G)|$: [every nontrivial finite group of prime-power order has a nontrivial center](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/PGroup.html#IsPGroup.center_nontrivial).
- **Invariants of a class.** If $y = axa^{-1}$, then $x$ and $y$
  [have the same order](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/OrderOfElement.html#SemiconjBy.orderOf_eq) (see
  [order of an element](order-of-an-element.md)), and
  [a homomorphism sends conjugate elements to conjugate elements](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Conj.html#MonoidHom.map_isConj)
  (see [group morphism](../../../overview/general-algebra/group-theory/part-01/group-morphism.md)).
- **Normal subgroups.** A normal subgroup
  [contains the whole class of each of its elements](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Basic.html#Group.conjugates_subset_normal),
  so it is a union of conjugacy classes; conversely, a subgroup that is a union of
  classes is normal. Since a normal subgroup contains the class $\{e\}$ and its order
  divides $|G|$, class sizes limit the possible normal subgroups. The
  [alternating group](../../../overview/general-algebra/group-theory/part-02/alternating-group.md) $A_5$ has classes of sizes
  $1, 12, 12, 15, 20$, and no sum of these that includes $1$ divides $60$ except
  $1$ and $60$, so $A_5$ is [simple](../../../overview/general-algebra/group-theory/part-01/simple-group.md).
- **Commuting pairs.** For a finite group with $k$ conjugacy classes,
  [the number of ordered pairs of commuting elements is $k\,|G|$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/CardCommute.html#card_comm_eq_card_conjClasses_mul_card),
  so two elements chosen uniformly at random commute with probability $k/|G|$.

## Related concepts

A class function
is a function on $G$ that is constant on each conjugacy class. The characters of
the irreducible complex representations of a finite group form an
orthonormal basis
of the space of class functions, so their number equals the number of conjugacy
classes. Conjugation also acts on subgroups, sending $H$ to $gHg^{-1}$; the
[second Sylow theorem](../../../overview/general-algebra/group-theory/part-02/second-sylow-theorem.md) says that the Sylow
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

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)

## Sources

- [Mathlib documentation: `ConjClasses`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Conj.html#ConjClasses)
- [Source of `ConjClasses` in Mathlib/Algebra/Group/Conj.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Algebra/Group/Conj.lean#L131)
- [Mathlib undergraduate list: Group Theory › Basic definitions](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L92)
