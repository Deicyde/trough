The **first Sylow theorem** says that a finite [group](trough:Group) has a
[subgroup](trough:Subgroup) of every prime-power order that divides the order of
the group. It is a partial converse to [Lagrange's theorem](trough:Subgroup.card_subgroup_dvd_card),
which says that the order of a subgroup divides the order of the group. A general
divisor of $|G|$ need not be the order of any subgroup, but a divisor that is a
power of a single prime always is. Together with the
[second](trough:Sylow.isPretransitive_of_finite) and [third](trough:card_sylow_modEq_one)
Sylow theorems, it is the basic tool for analysing finite groups of a given order.

## Statement

Let $G$ be a finite group and $p$ a prime. If $p^n$ divides $|G|$, then
$G$ has a subgroup of order $p^n$.

Write $|G| = p^k m$ with $p \nmid m$. The case $n = k$ is the usual form of the
theorem: $G$ has a subgroup of order $p^k$, the largest power of $p$ dividing $|G|$.
Such a subgroup is called a **Sylow $p$-subgroup** of $G$. A subgroup whose order is
a power of $p$ is a **$p$-subgroup**.

The case $n = 1$ is
[Cauchy's theorem](trough:exists_prime_orderOf_dvd_card): if $p$ divides $|G|$, then
$G$ has an element of order $p$, whose
powers form a subgroup of order $p$.

## Examples

- The [symmetric group](trough:Equiv.Perm) $S_3$ has order $6 = 2 \cdot 3$. Each of
  its three transpositions generates a Sylow $2$-subgroup of order $2$, and the
  [alternating group](trough:alternatingGroup) $A_3$, of order $3$, is its Sylow
  $3$-subgroup.
- The alternating group $A_4$ has order $12 = 2^2 \cdot 3$. Its subgroups of order
  $2$, $3$ and $4$ exist as the theorem predicts; the subgroup of order $4$ is the
  Klein four-group, consisting of the identity and the three double transpositions. The
  divisor $6$ is not a prime power, and $A_4$ has no subgroup of order $6$.
- In the [general linear group](trough:Matrix.GeneralLinearGroup) of invertible
  $d \times d$ matrices over the field with $p$ elements, the upper triangular
  matrices with ones on the diagonal form a subgroup of order $p^{d(d-1)/2}$. This is
  the full power of $p$ in the order
  $$(p^d - 1)(p^d - p)\cdots(p^d - p^{d-1}),$$
  so these matrices form a Sylow $p$-subgroup.

## Consequences

- **Towers of subgroups.** If $p^n$ divides $|G|$, there is a chain of subgroups
  $H_0 \le H_1 \le \dots \le H_n$ with $|H_i| = p^i$ for each $i$
  (towers of $p$-subgroups). In particular a
  group of order $p^n$ has subgroups of every order $p^i$ with $i \le n$.
- **Extending a $p$-subgroup.** A subgroup of order $p^m$ is contained in a
  subgroup of order $p^n$ whenever $m \le n$ and $p^n$ divides $|G|$
  (the extension statement). Taking
  $n = k$ shows that every $p$-subgroup lies in some Sylow $p$-subgroup.
- **Maximal $p$-subgroups.** In a finite group, a $p$-subgroup $P$ contained in no
  larger $p$-subgroup
  has order $p^k$, the full power of $p$ in $|G|$,
  so it is a Sylow $p$-subgroup in the sense above. (Mathlib takes maximality among
  $p$-subgroups as the definition; see In Mathlib.) Moreover,
  its index $[G : P]$ is not divisible by $p$;
  Mathlib proves the index statement for any Sylow subgroup of finite index, in
  any group.
- **The other Sylow theorems.** Once Sylow subgroups exist, one can ask how many
  there are and how they are related: they are all conjugate, and their number
  divides $m$ and is congruent to $1$ modulo $p$.

## Proof

The theorem follows by induction on $n$ from the following step: if $H$ is a
subgroup of order $p^n$ and $p^{n+1}$ divides $|G|$, then
$H$ lies in a subgroup of order $p^{n+1}$.
Starting from the trivial subgroup, of order $p^0 = 1$, the step is applied $n$
times.

For the step, let $H$ act on the set of left cosets $G/H$ by left multiplication
(see [group action](trough:MulAction)). Every [orbit](trough:MulAction.orbit) of a
group of order $p^n$ has size a power of $p$, so only the fixed points
contribute an orbit of size not divisible by $p$; hence
the number of fixed points is congruent to $|G/H|$ modulo $p$.
Since $|G| = p^n\,[G : H]$ and $p^{n+1}$ divides $|G|$, the
[index](trough:Subgroup.index) $[G : H]$ is divisible by $p$, so the number of
fixed points is too.

A coset $gH$ is fixed by every element of $H$ exactly when $g^{-1} h g \in H$ for
all $h \in H$, that is, when $g^{-1} H g \subseteq H$. Since $H$ is finite, this
inclusion is an equality, so $g$ lies in the normalizer $N(H) = \{x \in G : xHx^{-1} = H\}$, a subgroup of
$G$ that contains $H$ as a [normal subgroup](trough:Subgroup.Normal) (indeed the
largest such subgroup). The fixed cosets are
therefore the cosets of $H$ in $N(H)$, and $p$ divides the order of the
[quotient group](trough:QuotientGroup.Quotient.group) $N(H)/H$. By Cauchy's theorem
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
every subgroup that is a $p$-group is contained in a Sylow $p$-subgroup
in any group. For a finite group the two definitions agree: a maximal $p$-subgroup
has order $p^k$, and conversely
a subgroup of order $p^k$ is a Sylow subgroup.

## Depends on

- [Group](trough:Group)
- [Subgroup](trough:Subgroup)
- [Prime numbers](trough:Prime)

## Proof depends on

- [Lagrange's theorem](trough:Subgroup.card_subgroup_dvd_card)
- [Group action](trough:MulAction)
- [Orbit](trough:MulAction.orbit)
- [Index of a subgroup](trough:Subgroup.index)
- [Normal subgroup](trough:Subgroup.Normal)
- [Quotient group](trough:QuotientGroup.Quotient.group)
- [Cauchy's theorem (group theory)](trough:exists_prime_orderOf_dvd_card)
