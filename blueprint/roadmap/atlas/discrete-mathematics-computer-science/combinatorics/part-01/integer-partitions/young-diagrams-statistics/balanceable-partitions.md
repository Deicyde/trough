---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.BalanceableBoundedPartitionsWanted.Combinatorics.Bounded, MathlibExt.Combinatorics.BalanceableBoundedPartitionsWanted.Combinatorics.Balanceable, MathlibExt.Combinatorics.BalanceableBoundedPartitionsWanted.Combinatorics.minimal_balanceable_of_bounded
statement: formalized
---

# Balanceable partitions

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/balanceable-partitions/index.html).

## $k$-bounded partition

A partition of $n$ is $k$-bounded if each of its parts is at most $k$.

For example, $12 = 3 + 2 + 2 + 2 + 2 + 1$ is a $3$-bounded partition of $12$.

Formalized by `MathlibExt.Combinatorics.BalanceableBoundedPartitionsWanted.Combinatorics.Bounded`, a definition declared in [WantedExt/Combinatorics/BalanceableBoundedPartitionsWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BalanceableBoundedPartitionsWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/balanceable-partitions/index.html#bounded).

## Balanceable partition

A partition of $n$ is balanceable if its multiset of parts can be split
as $s_1 + s_2$ into two multisets $s_1$ and $s_2$ whose elements have equal sums.

For example, $12 = (3 + 2 + 1) + (2 + 2 + 2)$ is a balanceable partition of $12$.

Formalized by `MathlibExt.Combinatorics.BalanceableBoundedPartitionsWanted.Combinatorics.Balanceable`, a definition declared in [WantedExt/Combinatorics/BalanceableBoundedPartitionsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BalanceableBoundedPartitionsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/balanceable-partitions/index.html#balanceable).

## Smallest size forcing bounded partitions to be balanceable

For every integer $k \ge 1$, the
smallest positive integer $n$ such that every $k$-bounded partition of $n$ is balanceable is
$2 \operatorname{lcm}(1, 2, \ldots, k)$.

## Sources

- https://projecteuler.net/problem=772. Problem `balanceable_bounded_partitions` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.BalanceableBoundedPartitionsWanted.Combinatorics.minimal_balanceable_of_bounded` is written with `theorem_wanted` in [WantedExt/Combinatorics/BalanceableBoundedPartitionsWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BalanceableBoundedPartitionsWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/balanceable-partitions/index.html#minimal-balanceable-of-bounded).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Balanceable partitions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/balanceable-partitions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/balanceable-partitions)
