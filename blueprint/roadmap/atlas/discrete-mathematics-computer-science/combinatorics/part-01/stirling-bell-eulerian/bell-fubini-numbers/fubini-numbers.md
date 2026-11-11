---
declaration: section
origin: cited
lean: MetaMathlibExt.fubiniNumber, MetaMathlibExt.fubiniNumber_eq_sum, MetaMathlibExt.fubiniNumber_zero, MetaMathlibExt.fubiniNumber_one, MetaMathlibExt.fubiniNumber_two, MetaMathlibExt.fubiniNumber_three, MetaMathlibExt.fubiniNumber_eq_factorial_sub_sum_signed_stirling
statement: formalized
proof: formalized
---

# Fubini numbers

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/fubini-numbers/index.html).

## Fubini numbers

The Fubini number (ordered Bell number) of a natural number $n$ is
$F(n) = \sum_{k=0}^{n} S(n,k)\, k!$, where $S(n,k)$ is the Stirling number of the second kind.

$F(n)$ counts the weak orderings, equivalently the ordered set partitions, of an $n$-element set.

Formalized by `MetaMathlibExt.fubiniNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/FubiniNumber.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FubiniNumber.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/fubini-numbers/index.html#fubini-number).

## Fubini numbers as sums of Stirling numbers

For every natural number $n$, the Fubini
number $F(n)$ equals $\sum_{k=0}^{n} S(n,k)\, k!$, where $S(n,k)$ is the Stirling number of the
second kind.

Formalized by `MetaMathlibExt.fubiniNumber_eq_sum`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/FubiniNumber.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FubiniNumber.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/fubini-numbers/index.html#fubini-number-eq-sum).

## Fubini number of zero

The Fubini number $F(0)$ equals $1$: the empty set has exactly
one weak ordering.

Formalized by `MetaMathlibExt.fubiniNumber_zero`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/FubiniNumber.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FubiniNumber.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/fubini-numbers/index.html#fubini-number-zero).

## Fubini number of one

The Fubini number $F(1)$ equals $1$.

Formalized by `MetaMathlibExt.fubiniNumber_one`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/FubiniNumber.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FubiniNumber.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/fubini-numbers/index.html#fubini-number-one).

## Fubini number of two

The Fubini number $F(2)$ equals $3$.

Formalized by `MetaMathlibExt.fubiniNumber_two`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/FubiniNumber.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FubiniNumber.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/fubini-numbers/index.html#fubini-number-two).

## Fubini number of three

The Fubini number $F(3)$ equals $13$.

Formalized by `MetaMathlibExt.fubiniNumber_three`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/FubiniNumber.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FubiniNumber.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/fubini-numbers/index.html#fubini-number-three).

## Alternating recurrence for the Fubini numbers

For every natural number $n$, the Fubini
number $F(n)$ satisfies

$$F(n) = n! - \sum_{j=1}^{n} s(n, n-j)\, F(n-j),$$

where $s(n, k)$ is the signed Stirling number of the first kind.

## Sources

- Benjamin Schreyer, "Rigged Horse Numbers and their Modular Periodicity," Journal of Integer Sequences 28 (2025), Article 25.4.1, Corollary, lines 253–257, https://cs.uwaterloo.ca/journals/JIS/VOL28/Schreyer/schreyer7.tex

Formalized by `MetaMathlibExt.fubiniNumber_eq_factorial_sub_sum_signed_stirling`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/FubiniRecurrence.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FubiniRecurrence.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/fubini-numbers/index.html#fubini-number-eq-factorial-sub-sum-signe).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fubini numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/fubini-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/fubini-numbers)
