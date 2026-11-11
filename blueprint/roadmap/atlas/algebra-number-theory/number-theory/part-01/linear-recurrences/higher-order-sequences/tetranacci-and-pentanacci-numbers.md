---
declaration: section
origin: cited
lean: MetaMathlibExt.pentanacciNumber, MetaMathlibExt.tetranacci
statement: formalized
proof: formalized
---

# Tetranacci and pentanacci numbers

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tetranacci-and-pentanacci-numbers/index.html).

## Pentanacci numbers

The pentanacci numbers $a_n$, for natural numbers $n$, are defined by
$a_0 = 1$, $a_1 = 1$, $a_2 = 2$, $a_3 = 4$, $a_4 = 8$ and
$a_{n+5} = a_{n+4} + a_{n+3} + a_{n+2} + a_{n+1} + a_n$ for every $n$, so each term from index
$5$ on is the sum of the five terms before it.

Their ordinary generating function is $1/(1 - t - t^2 - t^3 - t^4 - t^5)$; up to a shift of index
they form OEIS A001591.

Formalized by `MetaMathlibExt.pentanacciNumber`, a definition declared in [MathlibExt/NumberTheory/PentanacciNumber.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PentanacciNumber.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tetranacci-and-pentanacci-numbers/index.html#pentanacci-number).

## Tetranacci sequence

The Tetranacci sequence `0, 0, 0, 1, 1, 2, 4, 8, …` (OEIS A000078), in which
each term after the first four is the sum of its four predecessors.

Formalized by `MetaMathlibExt.tetranacci`, a definition declared in [MathlibExt/NumberTheory/TetranacciSequence.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TetranacciSequence.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tetranacci-and-pentanacci-numbers/index.html#tetranacci).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tetranacci and pentanacci numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tetranacci-and-pentanacci-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/tetranacci-and-pentanacci-numbers)
