---
article_id: af_064ef7e0970e39cb57a15219
concept: Subgroup.card_subgroup_dvd_card
---

**Lagrange's theorem** says that in a finite [group](trough:Group) the order (number of elements) of every
[subgroup](trough:Subgroup) divides the order of the group. It is a basic structural result of
group theory: it places an arithmetic restriction on the possible orders of
subgroups, and several classical facts, [Fermat's little
theorem](trough:ZMod.pow_card_sub_one_eq_one) among them, follow from it in a line.

## Statement

Let $G$ be a finite group and $H$ a subgroup of $G$, and write $|G|$ for the
order of $G$. Then the order $|H|$ of $H$
[divides the order $|G|$ of $G$](lean:Subgroup.card_subgroup_dvd_card). More precisely,

$$|G| = [G : H]\,|H|,$$

where the [index](trough:Subgroup.index) $[G : H]$ is the number of left cosets of $H$ in $G$
([the counting formula](lean:Subgroup.card_mul_index)). In particular the index
[also divides the order of $G$](lean:Subgroup.index_dvd_card).

## Proof

The left cosets $gH$ partition $G$: two cosets are either equal or disjoint, and
every element $g$ lies in its own coset $gH$. Each coset has exactly $|H|$
elements, because $h \mapsto gh$ is a bijection from $H$ onto $gH$. Counting the
elements of $G$ coset by coset gives $|G| = [G : H]\,|H|$.

## Consequences

- **Order of an element.** The [order](trough:orderOf) of an element $g$ is the order
  of the cyclic subgroup it generates, so it
  [divides the order of the group](lean:orderOf_dvd_natCard). Hence
  [$g^{|G|} = e$ for every $g$ in $G$](lean:pow_card_eq_one'), where $e$ is the
  identity element.
- **Groups of prime order.** If $|G| = p$ is prime, an element $g \neq e$
  generates a subgroup whose order divides $p$ and exceeds $1$, so that subgroup
  is all of $G$: [every group of prime order is cyclic](lean:isCyclic_of_prime_card)
  (see [cyclic group](trough:IsCyclic)).
- **[Fermat's little theorem](trough:ZMod.pow_card_sub_one_eq_one).** The nonzero residues modulo a prime $p$ form a
  group of order $p - 1$ under multiplication, so
  [$a^{p-1} \equiv 1 \pmod p$ for every integer $a$ with $p \nmid a$](lean:Int.ModEq.pow_card_sub_one_eq_one).
- **[Euler's theorem](trough:Nat.ModEq.pow_totient).** For $n \ge 1$, the units modulo $n$ form a group of order
  [$\varphi(n)$](trough:Nat.totient), the number of integers in $1, \dots, n$ coprime to $n$, so
  [$a^{\varphi(n)} \equiv 1 \pmod n$ for every natural number $a$ with $\gcd(a, n) = 1$](lean:Nat.ModEq.pow_totient).
- **Chains of subgroups.** If $H \le K \le G$, then
  [the order of $H$ divides the order of $K$](lean:Subgroup.card_dvd_of_le).

## The converse fails

A divisor of $|G|$ need not be the order of any subgroup: the [alternating group](trough:alternatingGroup)
$A_4$ has order $12$ but no subgroup of order $6$. Two partial converses hold.

- [Cauchy's theorem](trough:exists_prime_orderOf_dvd_card): if a prime $p$ divides
  $|G|$, then [$G$ has an element of order $p$](lean:exists_prime_orderOf_dvd_card).
- For prime powers the [first Sylow theorem](trough:Sylow.exists_subgroup_card_pow_prime), in its strong form, gives the full converse: whenever $p^n$
  divides $|G|$ for a prime $p$,
  [$G$ has a subgroup of order $p^n$](lean:Sylow.exists_subgroup_card_pow_prime).

## In Mathlib

Mathlib states the theorem for every group, not only finite ones. It measures
size with the natural-number cardinality, which gives $0$ for an infinite set, so
for an infinite group the statement holds automatically, since every number
divides $0$; for a finite group it is the classical theorem. The index is likewise
the number of cosets as a natural number, so
[it is $0$ exactly when $H$ has infinitely many cosets](lean:Subgroup.index_eq_zero_iff_infinite),
and [an element of infinite order has order $0$](lean:orderOf_eq_zero_iff). With
these conventions the counting formula, the divisibility of the order by the index
and by element orders, and the statement about chains of subgroups hold for every
group. The statement about groups of prime order needs no convention, since its
hypothesis already makes the group finite. Mathlib's statements of Cauchy's theorem
and of the first Sylow theorem assume the group is finite.

## Depends on

- [Group](trough:Group)
- [Subgroup](trough:Subgroup)
- [Index of a subgroup](trough:Subgroup.index)
