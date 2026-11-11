---
declaration: section
origin: cited
lean: MetaMathlibExt.compositions_parts_one_two_three_eq_tribonacci, MetaMathlibExt.compositions_parts_one_two_three_eq_canonical_tribonacci
statement: formalized
proof: formalized
---

# Compositions with parts 1, 2 and 3

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/compositions-with-parts-1-2-and-3/index.html).

## Compositions with parts $1$, $2$, $3$ are counted by Tribonacci numbers

Let $T$ be a
sequence of natural numbers with $T_1 = T_2 = 1$, $T_3 = 2$ and
$T_m = T_{m-1} + T_{m-2} + T_{m-3}$ for every $m > 3$. Then for every positive integer $n$, the
number of compositions of $n$ (ordered sequences of positive integers with sum $n$) whose parts
are all $1$, $2$ or $3$ is $T_{n+1}$.

The result is due to V. E. Hoggatt, Jr., and M. Bicknell,
"Palindromic compositions," Fibonacci Quarterly 13 (1975), 350–356,
cited as [V] at source lines 429–430.

Proof: Split each nonempty composition by its first part, sum the resulting recurrence over its
length, and use strong induction, following Stanley, Section 1.2, and OEIS A000073.

## Sources

- Yu-hong Guo, "Some Identities For Palindromic Compositions," Journal of Integer Sequences 21 (2018), Article 18.6.6, Theorem citing [V], lines 118–125, https://cs.uwaterloo.ca/journals/JIS/VOL21/Guo/guo19.tex

Formalized by `MetaMathlibExt.compositions_parts_one_two_three_eq_tribonacci`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/CompositionsTribonacci.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/CompositionsTribonacci.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/compositions-with-parts-1-2-and-3/index.html#compositions-parts-one-two-three-eq-trib).

## Compositions with parts $1$, $2$, $3$ and the Tribonacci sequence

For every positive integer
$n$, the number of compositions of $n$ (ordered sequences of positive integers with sum $n$)
whose parts are all $1$, $2$ or $3$ equals $t_{n+2}$, where $t$ is the Tribonacci sequence
given by $t_0 = t_1 = 0$, $t_2 = 1$ and $t_{k+3} = t_{k+2} + t_{k+1} + t_k$ (OEIS A000073).

Proof: Specialize `compositions_parts_one_two_three_eq_tribonacci` to
`T k = tribonacci (k + 1)`, whose initial values and recurrence hold by definition.

Formalized by `MetaMathlibExt.compositions_parts_one_two_three_eq_canonical_tribonacci`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/CompositionsTribonacci.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/CompositionsTribonacci.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/compositions-with-parts-1-2-and-3/index.html#compositions-parts-one-two-three-eq-cano).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Compositions with parts 1, 2 and 3](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/compositions-with-parts-1-2-and-3/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-compositions/compositions-with-parts-1-2-and-3)
