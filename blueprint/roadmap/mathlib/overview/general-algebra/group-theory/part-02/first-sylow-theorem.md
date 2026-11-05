---
article_id: af_40423cdd7a33e06b2f128541
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Sylow.exists_subgroup_card_pow_prime
mathlib_file: Mathlib/GroupTheory/Sylow.lean
---

# First Sylow theorem

The **first Sylow theorem** says that a finite [group](../part-01/group.md) has a
[subgroup](../part-01/subgroup.md) of every prime-power order that divides the order of
the group. It is a partial converse to [Lagrange's theorem](lagranges-theorem.md),
which says that the order of a subgroup divides the order of the group. A general
divisor of $|G|$ need not be the order of any subgroup, but a divisor that is a
power of a single prime always is. Together with the
[second](second-sylow-theorem.md) and [third](third-sylow-theorem.md)
Sylow theorems, it is the basic tool for analysing finite groups of a given order.

## Statement

Let $G$ be a finite group and $p$ a prime. If $p^n$ divides $|G|$, then
[$G$ has a subgroup of order $p^n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.exists_subgroup_card_pow_prime).

Write $|G| = p^k m$ with $p \nmid m$. The case $n = k$ is the usual form of the
theorem: $G$ has a subgroup of order $p^k$, the largest power of $p$ dividing $|G|$.
Such a subgroup is called a **Sylow $p$-subgroup** of $G$. A subgroup whose order is
a power of $p$ is a **$p$-subgroup**.

The case $n = 1$ is
[Cauchy's theorem](../../../../thousand-plus/algebra/20-group-theory-and-generalizations/part-01/cauchys-theorem-group-theory.md): if $p$ divides $|G|$, then
[$G$ has an element of order $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Type.html#exists_prime_orderOf_dvd_card), whose
powers form a subgroup of order $p$.

## Examples

- The [symmetric group](permutation-group-of-a-type.md) $S_3$ has order $6 = 2 \cdot 3$. Each of
  its three transpositions generates a Sylow $2$-subgroup of order $2$, and the
  [alternating group](alternating-group.md) $A_3$, of order $3$, is its Sylow
  $3$-subgroup.
- The alternating group $A_4$ has order $12 = 2^2 \cdot 3$. Its subgroups of order
  $2$, $3$ and $4$ exist as the theorem predicts; the subgroup of order $4$ is the
  Klein four-group, consisting of the identity and the three double transpositions. The
  divisor $6$ is not a prime power, and $A_4$ has no subgroup of order $6$.
- In the [general linear group](../../../../undergraduate/group-theory/classical-automorphism-groups/general-linear-group.md) of invertible
  $d \times d$ matrices over the field with $p$ elements, the upper triangular
  matrices with ones on the diagonal form a subgroup of order $p^{d(d-1)/2}$. This is
  the full power of $p$ in the order
  $$(p^d - 1)(p^d - p)\cdots(p^d - p^{d-1}),$$
  so these matrices form a Sylow $p$-subgroup.

## Consequences

- **Towers of subgroups.** If $p^n$ divides $|G|$, there is a chain of subgroups
  $H_0 \le H_1 \le \dots \le H_n$ with $|H_i| = p^i$ for each $i$
  ([towers of $p$-subgroups](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.exists_orderEmbedding)). In particular a
  group of order $p^n$ has subgroups of every order $p^i$ with $i \le n$.
- **Extending a $p$-subgroup.** A subgroup of order $p^m$ is contained in a
  subgroup of order $p^n$ whenever $m \le n$ and $p^n$ divides $|G|$
  ([the extension statement](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.exists_subgroup_card_pow_prime_ge)). Taking
  $n = k$ shows that every $p$-subgroup lies in some Sylow $p$-subgroup.
- **Maximal $p$-subgroups.** In a finite group, a $p$-subgroup $P$ contained in no
  larger $p$-subgroup
  [has order $p^k$, the full power of $p$ in $|G|$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.card_eq_multiplicity),
  so it is a Sylow $p$-subgroup in the sense above. (Mathlib takes maximality among
  $p$-subgroups as the definition; see In Mathlib.) Moreover,
  [its index $[G : P]$ is not divisible by $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.not_dvd_index);
  Mathlib proves the index statement for any Sylow subgroup of finite index, in
  any group.
- **The other Sylow theorems.** Once Sylow subgroups exist, one can ask how many
  there are and how they are related: they are all conjugate, and their number
  divides $m$ and is congruent to $1$ modulo $p$.

## Proof

The theorem follows by induction on $n$ from the following step: if $H$ is a
subgroup of order $p^n$ and $p^{n+1}$ divides $|G|$, then
[$H$ lies in a subgroup of order $p^{n+1}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.exists_subgroup_card_pow_succ).
Starting from the trivial subgroup, of order $p^0 = 1$, the step is applied $n$
times.

For the step, let $H$ act on the set of left cosets $G/H$ by left multiplication
(see [group action](../part-01/group-action.md)). Every [orbit](../../../../undergraduate/group-theory/basic-definitions/orbit.md) of a
group of order $p^n$ has size a power of $p$, so only the fixed points
contribute an orbit of size not divisible by $p$; hence
[the number of fixed points is congruent to $|G/H|$ modulo $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/PGroup.html#IsPGroup.card_modEq_card_fixedPoints).
Since $|G| = p^n\,[G : H]$ and $p^{n+1}$ divides $|G|$, the
[index](../part-01/index-of-a-subgroup.md) $[G : H]$ is divisible by $p$, so the number of
fixed points is too.

A coset $gH$ is fixed by every element of $H$ exactly when $g^{-1} h g \in H$ for
all $h \in H$, that is, when $g^{-1} H g \subseteq H$. Since $H$ is finite, this
inclusion is an equality, so $g$ lies in the normalizer $N(H) = \{x \in G : xHx^{-1} = H\}$, a subgroup of
$G$ that contains $H$ as a [normal subgroup](../part-01/normal-subgroup.md) (indeed the
largest such subgroup). The fixed cosets are
therefore the cosets of $H$ in $N(H)$, and $p$ divides the order of the
[quotient group](../part-01/quotient-group.md) $N(H)/H$. By Cauchy's theorem
this quotient has a subgroup of order $p$. Its preimage in $N(H)$ is a subgroup
containing $H$, of order $p \cdot p^n = p^{n+1}$.

A different proof counts the subsets of $G$ of size $p^k$
and lets $G$ act on them by left multiplication; it avoids Cauchy's theorem.

## In Mathlib

Mathlib states the theorem for a finite group, measuring the sizes of the group and
the subgroup by their natural-number cardinalities, and supplying the primality of
$p$ as a typeclass assumption rather than as an explicit hypothesis; for a general
prime the user supplies that assumption from a proof of primality. Its stronger form, that the
subgroup of order $p^n$ can be chosen to contain any given subgroup of order $p^m$
with $m \le n$, is the statement the proof actually establishes. Mathlib defines a
Sylow $p$-subgroup not by its order but as a maximal $p$-subgroup, where a
$p$-group is a group in which each element $g$ satisfies $g^{p^i} = e$ for some $i$. This makes
sense in every group, finite or not, and Zorn's lemma then shows that
[every subgroup that is a $p$-group is contained in a Sylow $p$-subgroup](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#IsPGroup.exists_le_sylow)
in any group. For a finite group the two definitions agree: a maximal $p$-subgroup
has order $p^k$, and conversely
[a subgroup of order $p^k$ is a Sylow subgroup](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.ofCard).

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group](../part-01/group.md)
- [Subgroup](../part-01/subgroup.md)
- [Prime numbers](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)

## Proof depends on

- [Lagrange's theorem](lagranges-theorem.md)
- [Group action](../part-01/group-action.md)
- [Orbit](../../../../undergraduate/group-theory/basic-definitions/orbit.md)
- [Index of a subgroup](../part-01/index-of-a-subgroup.md)
- [Normal subgroup](../part-01/normal-subgroup.md)
- [Quotient group](../part-01/quotient-group.md)
- [Cauchy's theorem (group theory)](../../../../thousand-plus/algebra/20-group-theory-and-generalizations/part-01/cauchys-theorem-group-theory.md)

## Sources

- [Mathlib documentation: `Sylow.exists_subgroup_card_pow_prime`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.exists_subgroup_card_pow_prime)
- [Source of `Sylow.exists_subgroup_card_pow_prime` in Mathlib/GroupTheory/Sylow.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/Sylow.lean#L721)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L60)
- [Freek Wiedijk's 100 theorems, no. 72](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L362)
- [1000+ theorems list: Q1057919](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1269)
- [1000+ theorems project: Q1057919](https://1000-plus.github.io/all.html?length=-1#Q1057919)
- [Wikipedia: Sylow theorems](https://en.wikipedia.org/wiki/Sylow_theorems)
- [Wikidata: Q1057919](https://www.wikidata.org/wiki/Q1057919)
