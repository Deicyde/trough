# Third Sylow theorem

The **third Sylow theorem** says that in a finite [group](../part-01/group.md) $G$ the number of Sylow
$p$-subgroups, for a [prime](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md) $p$, is congruent to $1$ modulo $p$ and divides the
order of $G$. Together with the [first](first-sylow-theorem.md) and
[second](second-sylow-theorem.md) Sylow theorems it is the basic counting tool of
finite group theory: the two arithmetic conditions often leave only one possible value for the
number of Sylow subgroups, and when that value is $1$ the unique Sylow $p$-subgroup is a
[normal subgroup](../part-01/normal-subgroup.md).

## Statement

Let $G$ be a finite group of order $p^n m$, where $p$ is prime and $p \nmid m$. A $p$-group is a
group in which every element has order a power of $p$. A Sylow $p$-subgroup of $G$ is a maximal
$p$-subgroup: a [subgroup](../part-01/subgroup.md) that is a $p$-group and is contained in no larger
such subgroup. In a finite group these are exactly the subgroups of order $p^n$; in particular
[every Sylow $p$-subgroup has order $p^n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.card_eq_multiplicity), and the first Sylow
theorem shows that they exist. Write $n_p$ for the number of Sylow $p$-subgroups. Then

$$n_p \equiv 1 \pmod p \qquad \text{and} \qquad n_p \mid m.$$

The [congruence $n_p \equiv 1 \pmod p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#card_sylow_modEq_one) (see [congruence](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in-z.md))
implies at once that [$p$ does not divide $n_p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#not_dvd_card_sylow). For any Sylow
$p$-subgroup $P$, with normalizer $N_G(P)$ (the set of elements $g$ with $gPg^{-1} = P$),
[the number of Sylow $p$-subgroups equals the index of $N_G(P)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.card_eq_index_normalizer),
and [$n_p$ divides the index of $P$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.card_dvd_index), which is $m$ by
[Lagrange's theorem](lagranges-theorem.md) (see [index](../part-01/index-of-a-subgroup.md)).

## Examples

- In the [symmetric group](permutation-group-of-a-type.md) $S_3$ there are three subgroups of order $2$, and $3 \equiv 1 \pmod 2$;
  there is one subgroup of order $3$.
- In the [alternating group](alternating-group.md) $A_5$, of order $60$, there are six
  subgroups of order $5$, ten of order $3$ and five of order $4$, matching
  $6 \equiv 1 \pmod 5$, $10 \equiv 1 \pmod 3$ and $5 \equiv 1 \pmod 2$.
- For a group of order $15$, $n_3$ divides $5$ and is $1$ modulo $3$, so $n_3 = 1$; likewise
  $n_5$ divides $3$ and is $1$ modulo $5$, so $n_5 = 1$. Both Sylow subgroups are therefore
  normal, and the group is the direct product of cyclic groups of orders $3$ and $5$, hence
  [cyclic](../part-01/cyclic-group.md).

## Consequences

- **Uniqueness and normality.** By the second Sylow theorem all Sylow $p$-subgroups are
  conjugate, so a Sylow $p$-subgroup is normal exactly when it is the only one:
  [a normal Sylow $p$-subgroup is unique](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.unique_of_normal), and
  [a unique Sylow $p$-subgroup is normal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.normal_of_subsingleton).
- **Simplicity tests.** If the two conditions force $n_p = 1$ for some prime $p$ dividing $|G|$
  with $p^n < |G|$, then $G$ is not [simple](../part-01/simple-group.md). For instance, in a group of
  order $20$, $n_5$ divides $4$ and is $1$ modulo $5$, so $n_5 = 1$ and no group of order $20$ is
  simple. Arguments of this kind, refined by counting elements, settle the simplicity question for
  most small orders.

## Proof

Let $P$ be a Sylow $p$-subgroup and let $P$ act on the set of all Sylow $p$-subgroups by
conjugation, a [group action](../part-01/group-action.md). When a $p$-group acts on a finite set, every
[orbit](../../../../undergraduate/group-theory/basic-definitions/orbit.md) has size a power of $p$, by the orbit–stabilizer relation, so the
orbits of size greater than $1$ contribute multiples of $p$, and
[the size of the set is congruent modulo $p$ to the number of fixed points](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/PGroup.html#IsPGroup.card_modEq_card_fixedPoints).
It remains to show that $P$ is the only fixed point.

A Sylow subgroup $Q$ is fixed when $P$ normalizes $Q$. In that case $PQ$ is a subgroup in which
$Q$ is normal, and its order $|P|\,|Q| / |P \cap Q|$ is a power of $p$. Maximality of $Q$ gives
$PQ = Q$, so $P \le Q$; in other words,
[$Q$ is fixed by $P$ exactly when $P \le Q$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#IsPGroup.sylow_mem_fixedPoints_iff). Since $P$
and $Q$ have the same order, $Q = P$. Hence $n_p \equiv 1 \pmod p$.

For the divisibility, let all of $G$ act by conjugation instead. By the second Sylow theorem this
action has a single orbit, and the [stabilizer](../../../../undergraduate/group-theory/basic-definitions/stabilizer-of-a-point.md) of $P$ is
[its normalizer](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.stabilizer_eq_normalizer), so the orbit–stabilizer theorem gives
$n_p = [G : N_G(P)]$. Since $P \le N_G(P)$, this index divides $[G : P] = m$.

## In Mathlib

Mathlib works with an arbitrary group, finite or not. A Sylow $p$-subgroup is defined as a maximal
$p$-subgroup, where a $p$-group is one in which every element has order a power of $p$, and the
Sylow subgroups form a type of their own on which the group acts by conjugation. The theorem
assumes only that $p$ is prime and that there are finitely many Sylow $p$-subgroups, so it covers
some infinite groups as well; for a finite group this hypothesis holds automatically and the
statement is the classical one. The number of Sylow subgroups is the natural-number cardinality
of that type, which is finite by hypothesis; Mathlib's natural-number cardinality would assign
$0$ to an infinite type, so the finiteness assumption is what makes the count meaningful. The second Sylow theorem and the identification
of $n_p$ with the index of a normalizer are proved under the same finiteness assumption.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group](../part-01/group.md)
- [Subgroup](../part-01/subgroup.md)
- [Prime numbers](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)
- [Congruence in $\Z$](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in-z.md)

## Proof depends on

- [First Sylow theorem](first-sylow-theorem.md)
- [Group action](../part-01/group-action.md)
- [Orbit](../../../../undergraduate/group-theory/basic-definitions/orbit.md)
- [Stabilizer of a point](../../../../undergraduate/group-theory/basic-definitions/stabilizer-of-a-point.md)
- [Second Sylow theorem](second-sylow-theorem.md)
- [Normal subgroup](../part-01/normal-subgroup.md)
- [Lagrange's theorem](lagranges-theorem.md)
- [Index of a subgroup](../part-01/index-of-a-subgroup.md)

## Sources

- [Mathlib documentation: `card_sylow_modEq_one`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#card_sylow_modEq_one)
- [Source of `card_sylow_modEq_one` in Mathlib/GroupTheory/Sylow.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/Sylow.lean#L373)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L62)
