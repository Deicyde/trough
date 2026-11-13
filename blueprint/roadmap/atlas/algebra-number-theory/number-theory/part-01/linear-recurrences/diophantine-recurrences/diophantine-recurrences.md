---
declaration: section
origin: cited
lean: MetaMathlibExt.tribonacci_factorialProduct_index_mem
statement: formalized
---

# Diophantine problems in recurrences: its own results

1 result, 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/index.html).

Squares, perfect powers, repdigits, factorials and powers of two among terms of recurrence sequences.

## Tribonacci numbers that are products of factorials

Let $(T_n)_{n \in \mathbb{Z}}$ be the
integer sequence with $T_0 = 0$, $T_1 = T_2 = 1$ and $T_{j+3} = T_{j+2} + T_{j+1} + T_j$ for
every integer $j$. If $n$ is an integer such that $|T_n| = m_1! \, m_2! \cdots m_k!$ for some
$k \ge 1$ and some positive integers $m_1, \dots, m_k$, then
$n \in \{-9, -8, -7, -5, -3, -2, 1, 2, 3, 4, 7\}$.

## Sources

- Adel Alahmadi and Florian Luca, "On Tribonacci Numbers that are Products of Factorials", Journal of Integer Sequences 26 (2023), Article 23.2.2, Theorem 2, lines 121-127, <https://cs.uwaterloo.ca/journals/JIS/VOL26/Luca/luca52.tex>.

Stated but not proved: `MetaMathlibExt.tribonacci_factorialProduct_index_mem` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/TribonacciFactorialProductWanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/TribonacciFactorialProductWanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/index.html#tribonacci-factorial-product-index-mem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Diophantine problems in recurrences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences)
