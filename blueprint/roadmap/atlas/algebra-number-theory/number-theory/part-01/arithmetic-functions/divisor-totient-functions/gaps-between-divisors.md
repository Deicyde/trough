---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ErdosProblem884Wanted.Statement, MathlibExt.NumberTheory.ErdosProblem884Wanted.Statement_refuted
statement: formalized
---

# Gaps between divisors

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/gaps-between-divisors/index.html).

## Divisor-gap sums (Erdős Problem 884)

The statement that there is a real constant $C > 0$
such that for every positive integer $n$, if $d_1 < d_2 < \dots < d_t$ are all the divisors of $n$
in increasing order, then
$\sum_{1 \le i < j \le t} \frac{1}{d_j - d_i} \le
C \left(1 + \sum_{1 \le i < t} \frac{1}{d_{i+1} - d_i}\right)$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem884Wanted.Statement`, a definition declared in [WantedExt/NumberTheory/ErdosProblem884Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem884Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/gaps-between-divisors/index.html#statement).

## Erdős Problem 884 is false (Larsen)

For every real constant $C > 0$ there is a positive
integer $n$ whose divisors $d_1 < d_2 < \dots < d_t$, listed in increasing order, satisfy
$\sum_{1 \le i < j \le t} \frac{1}{d_j - d_i} >
C \left(1 + \sum_{1 \le i < t} \frac{1}{d_{i+1} - d_i}\right)$.

## Sources

- Lean proof of the negative answer to Erdős Problem 884, https://github.com/Jayyhk/erdos-lean/blob/f8a51976fd2e66a52b4928c109fb9ae877a1a507/problems/884/Erdos884.lean.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem884Wanted.Statement_refuted` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem884Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem884Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/gaps-between-divisors/index.html#statement-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gaps between divisors](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/gaps-between-divisors/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/gaps-between-divisors)
