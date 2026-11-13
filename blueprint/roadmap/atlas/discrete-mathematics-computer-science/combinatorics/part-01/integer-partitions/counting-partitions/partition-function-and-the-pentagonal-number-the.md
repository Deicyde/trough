---
declaration: section
origin: cited
lean: MetaMathlibExt.partitionFunction, MetaMathlibExt.partitionFunction_zero, MetaMathlibExt.partitionFunction_one, MetaMathlibExt.mk_partitionFunction_eq_genFun, MetaMathlibExt.mk_partitionFunction_mul_pentagonalSeries, MetaMathlibExt.pentagonal_number_theorem
statement: formalized
proof: formalized
---

# Partition function and the pentagonal number theorem

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/partition-function-and-the-pentagonal-number-the/index.html).

## The partition function

For a natural number $n$, $p(n)$ is the number of partitions of
$n$, that is, of ways of writing $n$ as a sum of positive integers, disregarding order.

## Sources

- https://en.wikipedia.org/wiki/Pentagonal_number_theorem ("Pentagonal number theorem").

Formalized by `MetaMathlibExt.partitionFunction`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PentagonalNumber.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PentagonalNumber.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/partition-function-and-the-pentagonal-number-the/index.html#partition-function).

## The partition number of zero

Let $p(n)$ be the number of partitions of $n$. Then
$p(0) = 1$: the only partition of $0$ is the empty one.

Formalized by `MetaMathlibExt.partitionFunction_zero`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PentagonalNumber.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PentagonalNumber.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/partition-function-and-the-pentagonal-number-the/index.html#partition-function-zero).

## The partition number of one

Let $p(n)$ be the number of partitions of $n$. Then
$p(1) = 1$: the only partition of $1$ is $1$ itself.

Formalized by `MetaMathlibExt.partitionFunction_one`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PentagonalNumber.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PentagonalNumber.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/partition-function-and-the-pentagonal-number-the/index.html#partition-function-one).

## Partition generating function with unit weights

Let $p(n)$ be the number of partitions
of $n$. Over the integers, $\sum_{n \ge 0} p(n)\, x^n$ equals the weighted partition generating
function $\sum_{n \ge 0} \sum_{\lambda} \prod_{i} f(i, c_i(\lambda))\, x^n$ with all weights
$f(i, c) = 1$, where $\lambda$ runs over the partitions of $n$, $i$ over the distinct parts of
$\lambda$, and $c_i(\lambda)$ is the number of times $i$ occurs in $\lambda$.

Formalized by `MetaMathlibExt.mk_partitionFunction_eq_genFun`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PentagonalNumber.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PentagonalNumber.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/partition-function-and-the-pentagonal-number-the/index.html#mk-partition-function-eq-gen-fun).

## Euler's identity for the partition generating function

Let $p(n)$ be the number of
partitions of $n$. Over the integers,
$\left(\sum_{n \ge 0} p(n)\, x^n\right) \cdot \sum_{k \in \mathbb{Z}} (-1)^k x^{k(3k-1)/2} = 1$.
By the pentagonal number theorem the second factor equals $\prod_{i \ge 1} (1 - x^i)$.

Formalized by `MetaMathlibExt.mk_partitionFunction_mul_pentagonalSeries`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PentagonalNumber.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PentagonalNumber.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/partition-function-and-the-pentagonal-number-the/index.html#mk-partition-function-mul-pentagonal-ser).

## Euler's pentagonal recurrence for the partition function

Let $p(n)$ be the number of
partitions of $n$, and for an integer $k$ let $g(k) = k(3k - 1)/2$ be the generalized pentagonal
number of $k$. For every natural number $n \ge 1$,
$p(n) = \sum_{k} (-1)^{k+1}\, p(n - g(k))$, where the sum runs over the nonzero integers $k$
with $g(k) \le n$.

## Sources

- https://en.wikipedia.org/wiki/Pentagonal_number_theorem ("Pentagonal number theorem").

Formalized by `MetaMathlibExt.pentagonal_number_theorem`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PentagonalNumber.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PentagonalNumber.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/partition-function-and-the-pentagonal-number-the/index.html#pentagonal-number-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partition function and the pentagonal number theorem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/partition-function-and-the-pentagonal-number-the/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/integer-partitions/counting-partitions/partition-function-and-the-pentagonal-number-the)
