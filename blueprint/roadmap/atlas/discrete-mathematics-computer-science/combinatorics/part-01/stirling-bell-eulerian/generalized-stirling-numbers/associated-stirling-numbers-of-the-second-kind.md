---
declaration: section
origin: cited
lean: MetaMathlibExt.twoAssocStirlingSecond, MetaMathlibExt.twoAssocStirlingSecond_recurrence, MetaMathlibExt.twoAssocStirlingSecond_eq_zero_of_lt_two_mul
statement: formalized
proof: formalized
---

# Associated Stirling numbers of the second kind

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/associated-stirling-numbers-of-the-second-kind/index.html).

## 2-associated Stirling numbers of the second kind

For natural numbers $n$ and $k$, the
2-associated Stirling number of the second kind is the integer
$S_2(n, k) = \sum_{j=0}^{k} (-1)^j \binom{n}{j} S(n - j, k - j)$, where $S$ denotes the
Stirling numbers of the second kind.

By inclusion and exclusion over singleton blocks, $S_2(n, k)$ is the number of partitions of an
$n$-element set into $k$ blocks, each containing at least two elements.

Formalized by `MetaMathlibExt.twoAssocStirlingSecond`, a definition declared in [MathlibExt/Combinatorics/AssociatedStirlingSecond.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/AssociatedStirlingSecond.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/associated-stirling-numbers-of-the-second-kind/index.html#two-assoc-stirling-second).

## Recurrence for 2-associated Stirling numbers of the second kind

Write $S_2(n, k)$ for
the 2-associated Stirling number of the second kind. For natural numbers $m$ and $k$ with
$1 \le k \le m$, we have $S_2(m + 2, k) = k \, S_2(m + 1, k) + (m + 1) \, S_2(m, k - 1)$.

Formalized by `MetaMathlibExt.twoAssocStirlingSecond_recurrence`, a theorem declared in [MathlibExt/Combinatorics/AssociatedStirlingSecond.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/AssociatedStirlingSecond.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/associated-stirling-numbers-of-the-second-kind/index.html#two-assoc-stirling-second-recurrence).

## Vanishing of 2-associated Stirling numbers of the second kind

For natural numbers
$n$ and $k$ with $n < 2k$, the 2-associated Stirling number of the second kind $S_2(n, k)$
equals $0$.

Formalized by `MetaMathlibExt.twoAssocStirlingSecond_eq_zero_of_lt_two_mul`, a theorem declared in [MathlibExt/Combinatorics/AssociatedStirlingSecond.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/AssociatedStirlingSecond.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/associated-stirling-numbers-of-the-second-kind/index.html#two-assoc-stirling-second-eq-zero-of-lt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Associated Stirling numbers of the second kind](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/associated-stirling-numbers-of-the-second-kind/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/associated-stirling-numbers-of-the-second-kind)
