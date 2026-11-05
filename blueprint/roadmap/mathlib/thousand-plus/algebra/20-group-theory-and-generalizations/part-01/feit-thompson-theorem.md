---
article_id: af_a2dc53437d42295eff959609
declaration: theorem
origin: cited
not_ready: true
---

# Feit–Thompson theorem

The **Feit–Thompson theorem**, also called the odd order theorem, says that every
finite [group](../../../../overview/general-algebra/group-theory/part-01/group.md) of odd order is solvable. Equivalently, every
non-abelian finite [simple group](../../../../overview/general-algebra/group-theory/part-01/simple-group.md) has even order. It is a
cornerstone of the [classification of finite simple groups](classification-of-finite-simple-groups.md):
it guarantees that every non-abelian finite simple group contains an element of
order $2$, so that such groups can be studied through these elements and their
centralizers.

## Statement

A group $G$ is solvable if its derived series
$$G = G^{(0)} \supseteq G^{(1)} \supseteq G^{(2)} \supseteq \cdots, \qquad G^{(k+1)} = [G^{(k)}, G^{(k)}],$$
in which each term is the commutator subgroup of the one before, reaches the trivial
subgroup after finitely many steps ([solvable group](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Solvable.html#Group.IsSolvable),
[derived series](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Solvable.html#Subgroup.derivedSeries)). Equivalently, $G$ has a finite chain
of subgroups $1 = G_0 \le G_1 \le \cdots \le G_n = G$, each
[normal](../../../../overview/general-algebra/group-theory/part-01/normal-subgroup.md) in the next, whose successive
[quotients](../../../../overview/general-algebra/group-theory/part-01/quotient-group.md) $G_{i+1}/G_i$ are abelian.

**Theorem (Feit–Thompson).** If $G$ is a finite group and $|G|$ is odd, then $G$ is
solvable.

The two formulations are equivalent. A finite simple group is solvable exactly when
it is abelian, since [a simple group is solvable if and only if it is commutative](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Solvable.html#IsSimpleGroup.comm_iff_isSolvable), and [an abelian group is simple if and only if its order is prime](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Cyclic.html#CommGroup.is_simple_iff_prime_card).
So the theorem says that the only simple groups of odd order are the cyclic groups
of odd prime order. Conversely, if every simple group of odd order is cyclic of
prime order, then a finite group of odd order is solvable by induction on its order,
because [a group is solvable exactly when a normal subgroup and the corresponding quotient both are](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Solvable.html#Group.isSolvable_iff_subgroup_quotient), and by
[Lagrange's theorem](../../../../overview/general-algebra/group-theory/part-02/lagranges-theorem.md) every subgroup and
quotient of a group of odd order again has odd order.

## Examples

- [Abelian groups are solvable](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Solvable.html#Group.isSolvable_of_comm), and so are groups of
  prime power order, since [every finite $p$-group is nilpotent](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Nilpotent.html#IsPGroup.isNilpotent) and [nilpotent groups](../../../../overview/general-algebra/group-theory/part-01/nilpotent-group.md)
  are solvable. For these groups the theorem has nothing new to say.
- The smallest non-abelian group of odd order has order $21$: it is a semidirect
  product of a cyclic group of order $7$ by a cyclic group of order $3$ acting
  through an automorphism of order $3$. Here solvability is elementary: the
  [third Sylow theorem](../../../../overview/general-algebra/group-theory/part-02/third-sylow-theorem.md) forces the number of subgroups
  of order $7$ to be $1$, so that subgroup is normal, with abelian quotient.
- The hypothesis of odd order cannot be dropped. The [alternating group](../../../../overview/general-algebra/group-theory/part-02/alternating-group.md)
  $A_5$ of order $60$ is [simple](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Alternating/Simple.html#alternatingGroup.isSimpleGroup) and
  non-abelian, so not solvable; more generally the [symmetric group on five or more letters is not solvable](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Solvable.html#Equiv.Perm.not_isSolvable).

## Consequences

- **Involutions in simple groups.** A non-abelian finite simple group has even
  order, so by [Cauchy's theorem](cauchys-theorem-group-theory.md) it
  [contains an element of order $2$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Type.html#exists_prime_orderOf_dvd_card). The
  Brauer–Fowler theorem bounds the order of a finite simple group in terms of the
  order of the centralizer of such an involution, so a given group can occur as
  such a centralizer in only finitely many simple groups. This makes the
  centralizers of involutions a natural means of organizing the classification.
- **Composition factors.** Every composition factor of a group of odd order is cyclic
  of prime order. This restates solvability in terms of composition factors, which
  the [Jordan–Hölder theorem](../part-02/jordan-holder-theorem.md) shows are
  determined by the group.
- **Simple groups of odd order.** A finite group of odd order is simple if and only
  if its order is prime. One direction is the theorem; the other holds because [a group of prime order is simple](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Cyclic.html#isSimpleGroup_of_prime_card).

## Proof

The proof is by minimal counterexample. Suppose $G$ is a group of odd order that is
not solvable and has the smallest order with this property. By the reduction above,
$G$ is a non-abelian simple group, and every proper subgroup of $G$ has smaller odd
order and is therefore solvable. The proof derives a contradiction from this
situation in three broad stages.

1. **Local analysis.** The structure of $G$ is studied through its local
   subgroups, the normalizers of nontrivial subgroups of prime power order. These
   are proper subgroups, since $G$ is simple and not of prime power order, and so
   they are solvable by the minimality of $G$. The tools include Sylow
   theory, transfer and the methods of Hall and Higman for $p$-solvable groups. The
   conclusion is that the maximal subgroups have a very restricted structure, close
   to that of Frobenius groups, and that they are arranged in $G$ in a tightly
   controlled pattern.
2. **Character theory.** Ordinary [characters](../../../../overview/general-algebra/representation-theory/character.md) of $G$ and of
   its maximal subgroups are compared. The central difficulty is a family of
   irreducible characters of $G$, the exceptional characters, attached to characters
   of a maximal subgroup. Induction from that subgroup determines only certain
   differences of them, not the characters themselves, and the theory of coherent
   sets of characters is the tool that recovers them.
   The outcome is a single remaining configuration, in which $G$ has two maximal
   subgroups of Frobenius type attached to a pair of distinct odd primes $p$ and $q$.
3. **Final contradiction.** An argument with generators and relations, combined with
   arithmetic involving $p$ and $q$, rules out this last configuration.

The Feit–Thompson conjecture asserts that there are no distinct primes $p$ and $q$ for which
$$\frac{p^q - 1}{p - 1} \ \text{divides}\ \frac{q^p - 1}{q - 1};$$
a proof of this would shorten the final stage considerably. The conjecture is open.

## Related concepts

- [Burnside's theorem](burnsides-theorem.md), that every group of order $p^a q^b$ with
  $p$ and $q$ prime is solvable, is another solvability criterion from order alone,
  with a classical proof by character theory.
- Finite groups whose Sylow subgroups are all cyclic are solvable; in particular every
  group of squarefree order is.
- The [Schur–Zassenhaus theorem](../part-03/schur-zassenhaus-theorem.md)
  is one of the standard tools of the local analysis of finite groups.

## In Mathlib

Mathlib does not contain the Feit–Thompson theorem. The notions in its statement are
all there: [solvability](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Solvable.html#Group.IsSolvable), defined through the derived series
for arbitrary groups, finite or not, and [simple groups](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Subgroup/Simple.html#IsSimpleGroup),
defined as nontrivial groups whose only normal subgroups are the trivial subgroup and
the whole group. Mathlib proves solvability for several of the classes mentioned above:
abelian groups, nilpotent groups and so finite $p$-groups, and
finite [Z-groups](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/ZGroup.html#IsZGroup), the groups whose Sylow subgroups are all cyclic,
which include [every group of squarefree order](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/ZGroup.html#IsZGroup.of_squarefree). It also has
standard tools from the local analysis, such as [Burnside's normal $p$-complement theorem](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Transfer.html#MonoidHom.ker_transferSylow_isComplement') and [the Schur–Zassenhaus theorem](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SchurZassenhaus.html#Subgroup.exists_right_complement'_of_coprime). The character theory
that the proof needs is only partly developed.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group](../../../../overview/general-algebra/group-theory/part-01/group.md)
- [Simple group](../../../../overview/general-algebra/group-theory/part-01/simple-group.md)
- [Normal subgroup](../../../../overview/general-algebra/group-theory/part-01/normal-subgroup.md)
- [Quotient group](../../../../overview/general-algebra/group-theory/part-01/quotient-group.md)

## Proof depends on

- [Lagrange's theorem](../../../../overview/general-algebra/group-theory/part-02/lagranges-theorem.md)
- [First Sylow theorem](../../../../overview/general-algebra/group-theory/part-02/first-sylow-theorem.md)
- [Character](../../../../overview/general-algebra/representation-theory/character.md)

## Sources

- [1000+ theorems list: Q909517](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1061)
- [1000+ theorems project: Q909517](https://1000-plus.github.io/all.html?length=-1#Q909517)
- [Wikipedia: Feit–Thompson theorem](https://en.wikipedia.org/wiki/Feit%E2%80%93Thompson_theorem)
- [Wikidata: Q909517](https://www.wikidata.org/wiki/Q909517)
