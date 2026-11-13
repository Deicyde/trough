---
declaration: section
origin: cited
lean: MetaMathlibExt.PartitionNumberArray.extendA, MetaMathlibExt.PartitionNumberArray.weightSumAux, MetaMathlibExt.PartitionNumberArray.countSumAux, MetaMathlibExt.PartitionNumberArray.multWeightSum, MetaMathlibExt.PartitionNumberArray.countSum, MetaMathlibExt.PartitionNumberArray.PartitionMultiplicity, MetaMathlibExt.PartitionNumberArray.partCount, MetaMathlibExt.PartitionNumberArray.genStirlingSecond
statement: formalized
proof: formalized
---

# Partition number arrays

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/partition-number-arrays/index.html).

## Extension of a vector by zero

A vector $(a_0, \dots, a_{n-1})$ of natural numbers
extends to the sequence $\mathbb{N} \to \mathbb{N}$ that sends $j$ to $a_j$ for $j < n$ and to $0$
for $j \ge n$.

Formalized by `MetaMathlibExt.PartitionNumberArray.extendA`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/partition-number-arrays/index.html#extend-a).

## Index-weighted partial sum

For $n \in \mathbb{N}$ and a function
$f \colon \mathbb{N} \to \mathbb{N}$, this is the sum $\sum_{i=0}^{n-1} (i + 1)\,f(i)$.

Formalized by `MetaMathlibExt.PartitionNumberArray.weightSumAux`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/partition-number-arrays/index.html#weight-sum-aux).

## Sum of the first n values of a sequence

For a natural number $n$ and a sequence
$f \colon \mathbb{N} \to \mathbb{N}$, this is the natural number $\sum_{i=0}^{n-1} f(i)$.

Formalized by `MetaMathlibExt.PartitionNumberArray.countSumAux`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/partition-number-arrays/index.html#count-sum-aux).

## Weighted size of a multiplicity vector

For $n \in \mathbb{N}$ and nonnegative integers
$a_1, \dots, a_n$, the weighted size is $\sum_{j=1}^{n} j\,a_j$, the sum of the parts of the
partition with $a_j$ parts equal to $j$.

Formalized by `MetaMathlibExt.PartitionNumberArray.multWeightSum`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/partition-number-arrays/index.html#mult-weight-sum).

## Number of parts of an exponent vector

For a vector $(a_1, \dots, a_n)$ of natural
numbers, this is the natural number $\sum_{j=1}^{n} a_j$.

When $a_j$ is the number of parts equal to $j$ in a partition of $n$, this is the number of parts
of the partition.

Formalized by `MetaMathlibExt.PartitionNumberArray.countSum`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/partition-number-arrays/index.html#count-sum).

## Partition multiplicity vectors

A partition multiplicity vector of $n \in \mathbb{N}$
is a tuple $(a_1, \dots, a_n)$ of nonnegative integers with $\sum_{j=1}^{n} j\,a_j = n$. It
encodes the partition of $n$ that has $a_j$ parts equal to $j$.

Formalized by `MetaMathlibExt.PartitionNumberArray.PartitionMultiplicity`, a structure declared in [MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/partition-number-arrays/index.html#partition-multiplicity).

## Number of parts of a partition

Let $(a_1, \dots, a_n)$ be a partition multiplicity
vector of $n$, that is, nonnegative integers with $\sum_{j=1}^{n} j\,a_j = n$, where $a_j$
counts the parts equal to $j$. Its part count is $\sum_{j=1}^{n} a_j$.

Formalized by `MetaMathlibExt.PartitionNumberArray.partCount`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/partition-number-arrays/index.html#part-count).

## Generalized Stirling numbers of the second kind with parameter k

For a positive
integer $k$, the numbers $S_2(k; n, m)$, for natural numbers $n$ and $m$, are defined by
$S_2(k; 0, 0) = 1$, by $S_2(k; 0, m) = 0$ and $S_2(k; m, 0) = 0$ for $m \ge 1$, and by

$$S_2(k; n + 1, m + 1) = ((k - 1)n + m + 1)\, S_2(k; n, m + 1) + S_2(k; n, m).$$

Formalized by `MetaMathlibExt.PartitionNumberArray.genStirlingSecond`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/partition-number-arrays/index.html#gen-stirling-second).

## Factorial product of a sequence

For a natural number $n$ and a sequence
$g \colon \mathbb{N} \to \mathbb{N}$, this is the natural number
$\prod_{i=0}^{n-1} g(i)!\,\bigl((i+1)!\bigr)^{g(i)}$.

Formalized by `MetaMathlibExt.PartitionNumberArray.denomProdAux`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/partition-number-arrays/index.html#denom-prod-aux).

## Finite power product

For $n \in \mathbb{N}$ and functions
$g, f \colon \mathbb{N} \to \mathbb{N}$, this is the product $\prod_{i=0}^{n-1} f(i)^{g(i)}$,
with the convention $0^0 = 1$.

Formalized by `MetaMathlibExt.PartitionNumberArray.powProdAux`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/partition-number-arrays/index.html#pow-prod-aux).

## Denominator of the M3 partition number

Let $p$ be a partition of $n$ with multiplicity
vector $(a_1, \dots, a_n)$, so that exactly $a_j$ parts of $p$ equal $j$ and $\sum_j j a_j = n$.
The $M_3$ denominator of $p$ is the natural number $\prod_{j=1}^{n} a_j!\,(j!)^{a_j}$.

Formalized by `MetaMathlibExt.PartitionNumberArray.m3DenomProd`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/partition-number-arrays/index.html#m3-denom-prod).

## The M3 partition number

Let $p$ be a partition of $n$ with multiplicity vector
$(a_1, \dots, a_n)$, so that exactly $a_j$ parts of $p$ equal $j$ and $\sum_j j a_j = n$. The
number $M_3(p)$ is the quotient of $n!$ by $\prod_{j=1}^{n} a_j!\,(j!)^{a_j}$ in natural-number
division.

This division is exact, so $M_3(p) = n! / \prod_{j=1}^{n} a_j!\,(j!)^{a_j}$.

Formalized by `MetaMathlibExt.PartitionNumberArray.M3`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/partition-number-arrays/index.html#m3).

## Product of powers over a partition

Let $p$ be a partition of $n$ with multiplicity
vector $(a_1, \dots, a_n)$, so that exactly $a_j$ parts of $p$ equal $j$ and $\sum_j j a_j = n$.
For natural numbers $f_1, \dots, f_n$, the product of powers of $f$ over $p$ is the natural
number $\prod_{j=1}^{n} f_j^{a_j}$.

Formalized by `MetaMathlibExt.PartitionNumberArray.arrayPowProd`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/partition-number-arrays/index.html#array-pow-prod).

## The hat M32 partition number array

Let $k$ be a positive integer and let $p$ be a
partition of $n$ with multiplicity vector $(a_1, \dots, a_n)$, so that exactly $a_j$ parts of $p$
equal $j$ and $\sum_j j a_j = n$. Write $S_2(k; j, 1)$ for the generalized Stirling numbers of
the second kind with parameter $k$. The entry $\widehat{M}_{32}(k; p)$ is the natural number
$\prod_{j=1}^{n} S_2(k; j, 1)^{a_j}$.

Formalized by `MetaMathlibExt.PartitionNumberArray.hatM32`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/partition-number-arrays/index.html#hat-m32).

## The partition number array $M_{32}(k)$

Let $k$ be a positive integer and let
$a = (a_1, \dots, a_n)$ be a partition multiplicity vector of $n$, that is, nonnegative integers
with $\sum_{j=1}^{n} j\,a_j = n$, where $a_j$ counts the parts equal to $j$. Then
$M_{32}(k; a) = M_3(a) \prod_{j=1}^{n} S_2(k; j, 1)^{a_j}$, where $M_3(a)$ is $n!$ divided by
$\prod_{j=1}^{n} a_j!\,(j!)^{a_j}$ (the division is exact), and
$S_2(k; j, 1) = \prod_{i=1}^{j-1} ((k - 1)i + 1)$ is the first column of the generalized
Stirling numbers of the second kind.

Formalized by `MetaMathlibExt.PartitionNumberArray.M32`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/partition-number-arrays/index.html#m32).

## Absolute first column of the generalized Stirling numbers of the first kind

For
positive integers $k$ and $j$, the absolute value $|S_1(k; j, 1)|$ is defined as the quotient
$(j + k - 2)!/(k - 1)!$.

Formalized by `MetaMathlibExt.PartitionNumberArray.stirlingFirstAbsFirstCol`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/partition-number-arrays/index.html#stirling-first-abs-first-col).

## The M31 partition number array

Let $k$ be a positive integer and let $p$ be a
partition of $n$ with multiplicity vector $(a_1, \dots, a_n)$, so that exactly $a_j$ parts of $p$
equal $j$ and $\sum_j j a_j = n$. Write $M_3(p)$ for the M3 partition number of $p$, and for
$j \ge 1$ write $c_j = (j + k - 2)!/(k - 1)!$, the absolute value of the generalized Stirling
number of the first kind $S_1(k; j, 1)$. The entry $M_{31}(k; p)$ is the natural number
$M_3(p) \prod_{j=1}^{n} c_j^{a_j}$.

Formalized by `MetaMathlibExt.PartitionNumberArray.M31`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PartitionNumberArray.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/partition-number-arrays/index.html#m31).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partition number arrays](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/partition-number-arrays/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/set-partitions/partition-number-arrays)
