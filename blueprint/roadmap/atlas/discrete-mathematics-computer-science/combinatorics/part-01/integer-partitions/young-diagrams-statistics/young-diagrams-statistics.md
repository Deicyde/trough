---
declaration: section
origin: cited
lean: MetaMathlibExt.crank_nonneg_partition_count
statement: formalized
proof: formalized
---

# Young diagrams and partition statistics: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/index.html).

Statistics and structure of a single partition: conjugation, hook lengths, s-cores, perimeter, diagonal sequences, lit cells, rank and crank, max-rook numbers, perfect and double-perfect partitions, and reconstruction of a partition from pairwise products.

## Partitions with non-negative crank

For a partition $\lambda$, let $\omega(\lambda)$ be the
number of parts equal to $1$. The crank of $\lambda$ is its largest part if $\omega(\lambda) = 0$
(the largest part of the empty partition being $0$), and otherwise the number of parts greater
than $\omega(\lambda)$, counted with multiplicity, minus $\omega(\lambda)$. Let $p(k)$ be the
number of partitions of $k$. Then for every natural number $N$, the number of partitions of $N$
with non-negative crank equals

$$\sum_{n \ge 0,\ n(n+1)/2 \le N} (-1)^n \, p\bigl(N - n(n+1)/2\bigr).$$

This is the coefficient-wise form of the generating function for partitions with non-negative
crank. The source notes this result is originally due to Uncu.

## Sources

- George E. Andrews and David Newman, "The Minimal Excludant in Integer Partitions," Journal of Integer Sequences 23 (2020), Article 20.2.3, Theorem (equation 1.11), lines 161–165, https://cs.uwaterloo.ca/journals/JIS/VOL23/Andrews/andrews5.tex

Formalized by `MetaMathlibExt.crank_nonneg_partition_count`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/CrankGeneratingFunction.lean, line 1282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/CrankGeneratingFunction.lean#L1282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/index.html#crank-nonneg-partition-count).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Young diagrams and partition statistics](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics)
