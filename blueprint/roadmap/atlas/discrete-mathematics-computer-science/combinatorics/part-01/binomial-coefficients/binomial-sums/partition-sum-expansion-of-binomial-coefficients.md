---
declaration: section
origin: cited
lean: MetaMathlibExt.choose_mul_eq_partition_sum_unconditional, MetaMathlibExt.choose_mul_eq_partition_sum
statement: formalized
proof: formalized
---

# Partition-sum expansion of binomial coefficients

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/partition-sum-expansion-of-binomial-coefficients/index.html).

## Partition-sum expansion of $\binom{nm}{l}$, unconditional form

For all natural numbers $n$,
$m$ and $l$, let $P$ be the set of tuples $s = (s_1, \dots, s_m)$ of natural numbers with
$\sum_{j=1}^{m} j\,s_j = l$, and for $s \in P$ write $T_j(s) = s_{j+1} + \dots + s_m$. Then

$$\binom{nm}{l} = \sum_{s \in P} \prod_{j=1}^{m} \binom{n - T_j(s)}{s_j} \binom{m}{j}^{s_j},$$

where $n - T_j(s)$ is read as $0$ when $T_j(s) > n$. No positivity or range conditions on $n$,
$m$ and $l$ are needed.

Formalized by `MetaMathlibExt.choose_mul_eq_partition_sum_unconditional`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PartitionSumBinomialCoefficient.lean, line 629](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/PartitionSumBinomialCoefficient.lean#L629). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/partition-sum-expansion-of-binomial-coefficients/index.html#choose-mul-eq-partition-sum-unconditiona).

## Partition-sum expansion of $\binom{nm}{l}$

Let $n$ and $m$ be positive natural numbers and
let $l$ be a natural number with $1 \le l \le nm$. Let $P$ be the set of tuples
$s = (s_1, \dots, s_m)$ of natural numbers with $\sum_{j=1}^{m} j\,s_j = l$, and for $s \in P$
write $T_j(s) = s_{j+1} + \dots + s_m$. Then

$$\binom{nm}{l} = \sum_{s \in P} \prod_{j=1}^{m} \binom{n - T_j(s)}{s_j} \binom{m}{j}^{s_j},$$

where $n - T_j(s)$ is read as $0$ when $T_j(s) > n$.

## Sources

- Jocelyn Quaintance and Harris Kwong, "Permutations and Combinations of Colored Multisets," Journal of Integer Sequences 13 (2010), Article 10.2.6, Theorem, lines 329–336. <https://cs.uwaterloo.ca/journals/JIS/VOL13/Kwong/kwong6.tex>

Formalized by `MetaMathlibExt.choose_mul_eq_partition_sum`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PartitionSumBinomialCoefficient.lean, line 661](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/PartitionSumBinomialCoefficient.lean#L661). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/partition-sum-expansion-of-binomial-coefficients/index.html#choose-mul-eq-partition-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partition-sum expansion of binomial coefficients](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/partition-sum-expansion-of-binomial-coefficients/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/binomial-coefficients/binomial-sums/partition-sum-expansion-of-binomial-coefficients)
