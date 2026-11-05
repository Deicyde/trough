---
article_id: af_064ef7e0970e39cb57a15219
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Subgroup.card_subgroup_dvd_card
mathlib_file: Mathlib/GroupTheory/Coset/Card.lean
---

# Lagrange's theorem

**Lagrange's theorem** says that in a finite [group](../part-01/group.md) the order (number of elements) of every
[subgroup](../part-01/subgroup.md) divides the order of the group. It is a basic structural result of
group theory: it places an arithmetic restriction on the possible orders of
subgroups, and several classical facts, [Fermat's little theorem](../../../../thousand-plus/number-theory/part-02/fermats-little-theorem.md) among them, follow from it in a line.

## Statement

Let $G$ be a finite group and $H$ a subgroup of $G$, and write $|G|$ for the
order of $G$. Then the order $|H|$ of $H$
[divides the order $|G|$ of $G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Coset/Card.html#Subgroup.card_subgroup_dvd_card). More precisely,

$$|G| = [G : H]\,|H|,$$

where the [index](../part-01/index-of-a-subgroup.md) $[G : H]$ is the number of left cosets of $H$ in $G$
([the counting formula](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Index.html#Subgroup.card_mul_index)). In particular the index
[also divides the order of $G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Index.html#Subgroup.index_dvd_card).

## Proof

The left cosets $gH$ partition $G$: two cosets are either equal or disjoint, and
every element $g$ lies in its own coset $gH$. Each coset has exactly $|H|$
elements, because $h \mapsto gh$ is a bijection from $H$ onto $gH$. Counting the
elements of $G$ coset by coset gives $|G| = [G : H]\,|H|$.

## Consequences

- **Order of an element.** The [order](../../../../undergraduate/group-theory/basic-definitions/order-of-an-element.md) of an element $g$ is the order
  of the cyclic subgroup it generates, so it
  [divides the order of the group](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/OrderOfElement.html#orderOf_dvd_natCard). Hence
  [$g^{|G|} = e$ for every $g$ in $G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/OrderOfElement.html#pow_card_eq_one'), where $e$ is the
  identity element.
- **Groups of prime order.** If $|G| = p$ is prime, an element $g \neq e$
  generates a subgroup whose order divides $p$ and exceeds $1$, so that subgroup
  is all of $G$: [every group of prime order is cyclic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Cyclic/Subgroup.html#isCyclic_of_prime_card)
  (see [cyclic group](../part-01/cyclic-group.md)).
- **[Fermat's little theorem](../../../../thousand-plus/number-theory/part-02/fermats-little-theorem.md).** The nonzero residues modulo a prime $p$ form a
  group of order $p - 1$ under multiplication, so
  [$a^{p-1} \equiv 1 \pmod p$ for every integer $a$ with $p \nmid a$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Basic.html#Int.ModEq.pow_card_sub_one_eq_one).
- **[Euler's theorem](../../../../hundred-theorems/part-01/eulers-generalization-of-fermats-little-theorem.md).** For $n \ge 1$, the units modulo $n$ form a group of order
  [$\varphi(n)$](../../divisibility-in-integral-domains/eulers-totient-function-varphi.md), the number of integers in $1, \dots, n$ coprime to $n$, so
  [$a^{\varphi(n)} \equiv 1 \pmod n$ for every natural number $a$ with $\gcd(a, n) = 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Basic.html#Nat.ModEq.pow_totient).
- **Chains of subgroups.** If $H \le K \le G$, then
  [the order of $H$ divides the order of $K$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Coset/Card.html#Subgroup.card_dvd_of_le).

## The converse fails

A divisor of $|G|$ need not be the order of any subgroup: the [alternating group](alternating-group.md)
$A_4$ has order $12$ but no subgroup of order $6$. Two partial converses hold.

- [Cauchy's theorem](../../../../thousand-plus/algebra/20-group-theory-and-generalizations/part-01/cauchys-theorem-group-theory.md): if a prime $p$ divides
  $|G|$, then [$G$ has an element of order $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Type.html#exists_prime_orderOf_dvd_card).
- For prime powers the [first Sylow theorem](first-sylow-theorem.md), in its strong form, gives the full converse: whenever $p^n$
  divides $|G|$ for a prime $p$,
  [$G$ has a subgroup of order $p^n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Sylow.html#Sylow.exists_subgroup_card_pow_prime).

## In Mathlib

Mathlib states the theorem for every group, not only finite ones. It measures
size with the natural-number cardinality, which gives $0$ for an infinite set, so
for an infinite group the statement holds automatically, since every number
divides $0$; for a finite group it is the classical theorem. The index is likewise
the number of cosets as a natural number, so
[it is $0$ exactly when $H$ has infinitely many cosets](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Index.html#Subgroup.index_eq_zero_iff_infinite),
and [an element of infinite order has order $0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/OrderOfElement.html#orderOf_eq_zero_iff). With
these conventions the counting formula, the divisibility of the order by the index
and by element orders, and the statement about chains of subgroups hold for every
group. The statement about groups of prime order needs no convention, since its
hypothesis already makes the group finite. Mathlib's statements of Cauchy's theorem
and of the first Sylow theorem assume the group is finite.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group](../part-01/group.md)
- [Subgroup](../part-01/subgroup.md)
- [Index of a subgroup](../part-01/index-of-a-subgroup.md)

## Sources

- [Mathlib documentation: `Subgroup.card_subgroup_dvd_card`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Coset/Card.html#Subgroup.card_subgroup_dvd_card)
- [Source of `Subgroup.card_subgroup_dvd_card` in Mathlib/GroupTheory/Coset/Card.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/Coset/Card.lean#L66)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L59)
- [Freek Wiedijk's 100 theorems, no. 71](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L358)
- [1000+ theorems list: Q505798](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L506)
- [1000+ theorems project: Q505798](https://1000-plus.github.io/all.html?length=-1#Q505798)
- [Wikipedia: Lagrange's theorem (group theory)](https://en.wikipedia.org/wiki/Lagrange's_theorem_%28group_theory%29)
- [Wikidata: Q505798](https://www.wikidata.org/wiki/Q505798)
