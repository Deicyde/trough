The **third Sylow theorem** says that in a finite [group](trough:Group) $G$ the number of Sylow
$p$-subgroups, for a [prime](trough:Prime) $p$, is congruent to $1$ modulo $p$ and divides the
order of $G$. Together with the [first](trough:Sylow.exists_subgroup_card_pow_prime) and
[second](trough:Sylow.isPretransitive_of_finite) Sylow theorems it is the basic counting tool of
finite group theory: the two arithmetic conditions often leave only one possible value for the
number of Sylow subgroups, and when that value is $1$ the unique Sylow $p$-subgroup is a
[normal subgroup](trough:Subgroup.Normal).

## Statement

Let $G$ be a finite group of order $p^n m$, where $p$ is prime and $p \nmid m$. A $p$-group is a
group in which every element has order a power of $p$. A Sylow $p$-subgroup of $G$ is a maximal
$p$-subgroup: a [subgroup](trough:Subgroup) that is a $p$-group and is contained in no larger
such subgroup. In a finite group these are exactly the subgroups of order $p^n$; in particular
every Sylow $p$-subgroup has order $p^n$, and the first Sylow
theorem shows that they exist. Write $n_p$ for the number of Sylow $p$-subgroups. Then

$$n_p \equiv 1 \pmod p \qquad \text{and} \qquad n_p \mid m.$$

The congruence $n_p \equiv 1 \pmod p$ (see [congruence](trough:Int.ModEq))
implies at once that $p$ does not divide $n_p$. For any Sylow
$p$-subgroup $P$, with normalizer $N_G(P)$ (the set of elements $g$ with $gPg^{-1} = P$),
the number of Sylow $p$-subgroups equals the index of $N_G(P)$,
and $n_p$ divides the index of $P$, which is $m$ by
[Lagrange's theorem](trough:Subgroup.card_subgroup_dvd_card) (see [index](trough:Subgroup.index)).

## Examples

- In the [symmetric group](trough:Equiv.Perm) $S_3$ there are three subgroups of order $2$, and $3 \equiv 1 \pmod 2$;
  there is one subgroup of order $3$.
- In the [alternating group](trough:alternatingGroup) $A_5$, of order $60$, there are six
  subgroups of order $5$, ten of order $3$ and five of order $4$, matching
  $6 \equiv 1 \pmod 5$, $10 \equiv 1 \pmod 3$ and $5 \equiv 1 \pmod 2$.
- For a group of order $15$, $n_3$ divides $5$ and is $1$ modulo $3$, so $n_3 = 1$; likewise
  $n_5$ divides $3$ and is $1$ modulo $5$, so $n_5 = 1$. Both Sylow subgroups are therefore
  normal, and the group is the direct product of cyclic groups of orders $3$ and $5$, hence
  [cyclic](trough:IsCyclic).

## Consequences

- **Uniqueness and normality.** By the second Sylow theorem all Sylow $p$-subgroups are
  conjugate, so a Sylow $p$-subgroup is normal exactly when it is the only one:
  a normal Sylow $p$-subgroup is unique, and
  a unique Sylow $p$-subgroup is normal.
- **Simplicity tests.** If the two conditions force $n_p = 1$ for some prime $p$ dividing $|G|$
  with $p^n < |G|$, then $G$ is not [simple](trough:IsSimpleGroup). For instance, in a group of
  order $20$, $n_5$ divides $4$ and is $1$ modulo $5$, so $n_5 = 1$ and no group of order $20$ is
  simple. Arguments of this kind, refined by counting elements, settle the simplicity question for
  most small orders.

## Proof

Let $P$ be a Sylow $p$-subgroup and let $P$ act on the set of all Sylow $p$-subgroups by
conjugation, a [group action](trough:MulAction). When a $p$-group acts on a finite set, every
[orbit](trough:MulAction.orbit) has size a power of $p$, by the orbit–stabilizer relation, so the
orbits of size greater than $1$ contribute multiples of $p$, and
the size of the set is congruent modulo $p$ to the number of fixed points.
It remains to show that $P$ is the only fixed point.

A Sylow subgroup $Q$ is fixed when $P$ normalizes $Q$. In that case $PQ$ is a subgroup in which
$Q$ is normal, and its order $|P|\,|Q| / |P \cap Q|$ is a power of $p$. Maximality of $Q$ gives
$PQ = Q$, so $P \le Q$; in other words,
$Q$ is fixed by $P$ exactly when $P \le Q$. Since $P$
and $Q$ have the same order, $Q = P$. Hence $n_p \equiv 1 \pmod p$.

For the divisibility, let all of $G$ act by conjugation instead. By the second Sylow theorem this
action has a single orbit, and the [stabilizer](trough:MulAction.stabilizer) of $P$ is
its normalizer, so the orbit–stabilizer theorem gives
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

## Depends on

- [Group](trough:Group)
- [Subgroup](trough:Subgroup)
- [Prime numbers](trough:Prime)
- [Congruence in $\Z$](trough:Int.ModEq)

## Proof depends on

- [First Sylow theorem](trough:Sylow.exists_subgroup_card_pow_prime)
- [Group action](trough:MulAction)
- [Orbit](trough:MulAction.orbit)
- [Stabilizer of a point](trough:MulAction.stabilizer)
- [Second Sylow theorem](trough:Sylow.isPretransitive_of_finite)
- [Normal subgroup](trough:Subgroup.Normal)
- [Lagrange's theorem](trough:Subgroup.card_subgroup_dvd_card)
- [Index of a subgroup](trough:Subgroup.index)
