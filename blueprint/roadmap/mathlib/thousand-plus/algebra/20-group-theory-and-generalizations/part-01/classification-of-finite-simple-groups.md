---
article_id: af_a9d2672d3ecc556269ffce58
declaration: theorem
origin: cited
not_ready: true
---

# Classification of finite simple groups

The **classification of finite simple groups** is the theorem that every finite
[simple group](../../../../overview/general-algebra/group-theory/part-01/simple-group.md) belongs to one of a few explicitly described infinite families or
is one of 26 sporadic groups. Since every finite [group](../../../../overview/general-algebra/group-theory/part-01/group.md) is assembled from simple
groups by repeated extensions, the theorem gives a complete list of the building
blocks of finite group theory. Its proof is among the longest in mathematics.

## Statement

A group is simple if it is nontrivial and its only [normal subgroups](../../../../overview/general-algebra/group-theory/part-01/normal-subgroup.md) are the trivial
subgroup and the whole group ([the definition](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Subgroup/Simple.html#IsSimpleGroup)). The classification
states that every finite simple group is isomorphic to a group in one of the
following four classes:

1. the [cyclic groups](../../../../overview/general-algebra/group-theory/part-01/cyclic-group.md) $\mathbb{Z}/p$ of prime order $p$;
2. the [alternating groups](../../../../overview/general-algebra/group-theory/part-02/alternating-group.md) $A_n$ with $n \ge 5$;
3. the finite simple groups of Lie type, which come in sixteen families: six
   classical families (the projective special linear, unitary and symplectic
   groups, and three families of orthogonal groups, over
   [finite fields](../../../../undergraduate/ring-theory/field-theory/part-01/finite-fields.md)) and ten exceptional
   families, five of them twisted;
4. the 26 sporadic groups, which fit into none of the families above.

The Tits group, a subgroup of index $2$ in one of the twisted groups of Lie type,
is sometimes counted as a 27th sporadic group and sometimes placed with the groups
of Lie type.

## Examples

- Every group of prime order is simple, since by
  [Lagrange's theorem](../../../../overview/general-algebra/group-theory/part-02/lagranges-theorem.md) its only subgroups are the trivial one and the whole
  group ([groups of prime order are simple](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Cyclic.html#isSimpleGroup_of_prime_card)).
  Conversely, [an abelian group is simple exactly when its order is prime](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Cyclic.html#CommGroup.is_simple_iff_prime_card),
  which settles the abelian case of the classification (see
  [classification of abelian simple groups](../../../../overview/general-algebra/group-theory/part-02/classification-of-abelian-simple-groups.md)).
- [The alternating group on at least five letters is simple](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Alternating/Simple.html#alternatingGroup.isSimpleGroup)
  (see [alternating groups on 5 letters or more are simple](../../../../overview/general-algebra/group-theory/part-02/alternating-groups-on-5-letters-or-more-are-simp.md)). The smallest
  non-abelian simple group is $A_5$, of order $60$.
- For a prime power $q$, the projective special linear group $\mathrm{PSL}_2(q)$
  has order $q(q^2 - 1)/\gcd(2, q - 1)$ and is simple when $q \ge 4$:
  [over a finite field with at least four elements, the projective special linear group of $2 \times 2$ matrices is simple](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Projectivization/PSL/PSL2.html#Matrix.ProjectiveSpecialLinearGroup.rank_two_simple).
  The group $\mathrm{PSL}_2(7)$, of order $168$, is the second smallest
  non-abelian simple group.
- The sporadic groups include the five Mathieu groups $M_{11}$, $M_{12}$, $M_{22}$,
  $M_{23}$, $M_{24}$ and the Monster, the largest sporadic group, whose order is
  about $8 \times 10^{53}$.

The alternating groups and the groups of Lie type overlap in a few small cases:
$A_5$ is isomorphic to both $\mathrm{PSL}_2(4)$ and $\mathrm{PSL}_2(5)$, $A_6$ to
$\mathrm{PSL}_2(9)$, and $A_8$ to $\mathrm{PSL}_4(2)$. A few small groups produced by
the Lie-type constructions are not simple and are excluded from class 3; for
instance $\mathrm{PSL}_2(2) \cong S_3$ and $\mathrm{PSL}_2(3) \cong A_4$.

## Consequences

Every finite group has a composition series, a chain of subgroups each normal in
the next with simple successive quotients, and by the
[Jordan–Hölder theorem](../part-02/jordan-holder-theorem.md) the multiset of these
quotients (the composition factors of the group), up to isomorphism, does not depend on the chain chosen. The
classification therefore reduces many questions about all finite groups to a
check over the known simple groups. Results proved in this way include the
Schreier conjecture, that the outer automorphism group of every finite simple
group is solvable; the fact that every finite simple group can be generated by two
elements; and the classification of the finite doubly transitive permutation
groups.

Composition factors also detect solvability. A group
is [solvable](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Solvable.html#Group.IsSolvable) when its derived series reaches the trivial
group, and solvability passes to and from extensions:
[a group is solvable exactly when a normal subgroup and the corresponding quotient are](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Solvable.html#Group.isSolvable_iff_subgroup_quotient). A finite group is thus solvable
exactly when all its composition factors are cyclic of prime order, because
[a simple group is solvable if and only if it is commutative](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Solvable.html#IsSimpleGroup.comm_iff_isSolvable),
and [a commutative simple group has prime order](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Cyclic.html#CommGroup.is_simple_iff_prime_card), hence is cyclic.

## Proof

Only an outline can be given. A non-abelian finite simple group is not a
$p$-group, since [a finite $p$-group is simple only when it has order $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/PGroup.html#IsPGroup.isSimpleGroup_iff_card_eq); by
[Burnside's theorem](burnsides-theorem.md) its order even has at least three
distinct prime factors. The starting point is the
[Feit–Thompson theorem](feit-thompson-theorem.md), that every finite group of odd order is solvable; hence every
non-abelian finite simple group has even order and contains an involution, an
element of order $2$. The Brauer–Fowler theorem shows that only finitely many
simple groups can have a given group as the centralizer of an involution, so a
simple group can in principle be pinned down by the structure of such a
centralizer. The proof then splits into cases according to the structure of the
Sylow $2$-subgroups (which exist by the
[first Sylow theorem](../../../../overview/general-algebra/group-theory/part-02/first-sylow-theorem.md)) and the local subgroups (normalizers of
nontrivial $p$-subgroups) of a minimal counterexample, a finite simple group of
least order that is not on the list. In each case one either
derives a contradiction or determines the local structure precisely enough to
identify the group with a known simple group.

## In Mathlib

Mathlib does not contain the classification, nor the Feit–Thompson theorem it
relies on. It has the basic notions the statement uses:
[simple groups](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Subgroup/Simple.html#IsSimpleGroup), with no finiteness assumed, and
[solvable groups](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Solvable.html#Group.IsSolvable), defined through the derived series. It
proves the abelian case for groups of any size, measuring cardinality so that an
infinite group counts as having order $0$, which is not prime; the simplicity of
the alternating groups on five or more letters; and the simplicity of the
projective special linear groups of $2 \times 2$ matrices, in a version that
[covers every field other than those with two or three elements](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Projectivization/PSL/PSL2.html#Matrix.ProjectiveSpecialLinearGroup.rank_two_simple'),
infinite fields included. Its
[Jordan–Hölder theorem](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/JordanHolder.html#CompositionSeries.jordan_holder) is proved for an
abstract lattice with a notion of maximality, and the source notes that providing
this structure for the lattice of subgroups of a group is still to be done.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group](../../../../overview/general-algebra/group-theory/part-01/group.md)
- [Simple group](../../../../overview/general-algebra/group-theory/part-01/simple-group.md)
- [Cyclic group](../../../../overview/general-algebra/group-theory/part-01/cyclic-group.md)
- [Alternating group](../../../../overview/general-algebra/group-theory/part-02/alternating-group.md)
- [Normal subgroup](../../../../overview/general-algebra/group-theory/part-01/normal-subgroup.md)
- [Finite fields](../../../../undergraduate/ring-theory/field-theory/part-01/finite-fields.md)

## Proof depends on

- [Feit–Thompson theorem](feit-thompson-theorem.md)
- [First Sylow theorem](../../../../overview/general-algebra/group-theory/part-02/first-sylow-theorem.md)
- [Burnside's theorem](burnsides-theorem.md)

## Sources

- [1000+ theorems list: Q1340623](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1618)
- [1000+ theorems project: Q1340623](https://1000-plus.github.io/all.html?length=-1#Q1340623)
- [Wikipedia: Classification of finite simple groups](https://en.wikipedia.org/wiki/Classification_of_finite_simple_groups)
- [Wikidata: Q1340623](https://www.wikidata.org/wiki/Q1340623)
