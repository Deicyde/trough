---
declaration: section
origin: cited
lean: MetaMathlibExt.generalized_pell_eq_two_colored_compositions, MetaMathlibExt.narayanaCowsSequence
statement: formalized
proof: formalized
---

# Tribonacci and higher-order sequences: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/index.html).

Tribonacci, tetranacci, pentanacci, k-generalized Fibonacci, Padovan, Perrin and Narayana sequences, dominant roots and Binet forms.

## Generalized Pell numbers count compositions with two-colored ones

Let $k \ge 2$ and
$n \ge 1$ be natural numbers, and let $(P_m)_{m \in \mathbb{Z}}$ be natural numbers with $P_m = 0$
for $2 - k \le m \le 0$, $P_1 = 1$, and $P_m = 2P_{m-1} + P_{m-2} + \dots + P_{m-k}$ for all
$m \ge 2$. Then the number of compositions of $n$ into parts from $\{1, \dots, k\}$, where each
part equal to $1$ carries one of two colors, equals $P_{n+1}$.

## Sources

- Jhon J. Bravo, Jose L. Herrera, and José L. Ramírez, "Combinatorial Interpretation of Generalized Pell Numbers," Journal of Integer Sequences 23 (2020), Article 20.2.1, theorem `C_k(n) = P_{n+1}^{(k)}` for `n ≥ 1`, lines 441–447, https://cs.uwaterloo.ca/journals/JIS/VOL23/Bravo/bravo4.tex.

Formalized by `MetaMathlibExt.generalized_pell_eq_two_colored_compositions`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/GeneralizedPellNumbers.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/GeneralizedPellNumbers.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/index.html#generalized-pell-eq-two-colored-composit).

## Narayana's cows sequence

The sequence $(N_n)_{n \ge 0}$ of natural numbers defined by
$N_0 = 0$, $N_1 = N_2 = 1$ and $N_n = N_{n-1} + N_{n-3}$ for $n \ge 3$.

Formalized by `MetaMathlibExt.narayanaCowsSequence`, a definition declared in [MathlibExt/Combinatorics/Enumerative/NarayanaSequence.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/NarayanaSequence.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/index.html#narayana-cows-sequence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tribonacci and higher-order sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/higher-order-sequences)
