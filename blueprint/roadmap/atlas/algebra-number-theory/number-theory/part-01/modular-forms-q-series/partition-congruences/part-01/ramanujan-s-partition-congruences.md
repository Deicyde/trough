---
declaration: section
origin: cited
lean: MetaMathlibExt.two_mul_choose_two_succ, MetaMathlibExt.jacobiCubeSeries, MetaMathlibExt.coeff_jacobiCubeSeries_triangle, MetaMathlibExt.coeff_jacobiCubeSeries_eq_zero, MetaMathlibExt.pentagonalSeries_pow_three, MetaMathlibExt.dvd_partitionFunction_of_dvd_coeff_pentagonalSeries_pow, MetaMathlibExt.ramanujan_partition_congruence_mod_five, MetaMathlibExt.ramanujan_partition_congruence_mod_seven
statement: formalized
proof: formalized
---

# Ramanujan's partition congruences

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/ramanujan-s-partition-congruences/index.html).

## Twice a triangular number

For every natural number $a$, $2\binom{a+1}{2} = a(a+1)$.

Formalized by `MetaMathlibExt.two_mul_choose_two_succ`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/RamanujanPartitionCongruence.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/Partition/RamanujanPartitionCongruence.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/ramanujan-s-partition-congruences/index.html#two-mul-choose-two-succ).

## Jacobi's cube series

Jacobi's cube series is the formal power series
$J(X) = \sum_{t \ge 0} (-1)^t (2t+1) X^{t(t+1)/2}$ in $\mathbb{Z}[[X]]$: for each natural
number $t$ its coefficient at the triangular number $t(t+1)/2$ is $(-1)^t (2t+1)$, and all its
other coefficients are $0$.

Formalized by `MetaMathlibExt.jacobiCubeSeries`, a definition declared in [MathlibExt/Combinatorics/Enumerative/Partition/RamanujanPartitionCongruence.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/Partition/RamanujanPartitionCongruence.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/ramanujan-s-partition-congruences/index.html#jacobi-cube-series).

## Coefficients of Jacobi's cube series at triangular numbers

Let $J(X)$ be Jacobi's cube
series. For every natural number $t$, the coefficient of $X^{t(t+1)/2}$ in $J(X)$ is
$(-1)^t (2t+1)$.

Formalized by `MetaMathlibExt.coeff_jacobiCubeSeries_triangle`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/RamanujanPartitionCongruence.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/Partition/RamanujanPartitionCongruence.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/ramanujan-s-partition-congruences/index.html#coeff-jacobi-cube-series-triangle).

## Vanishing coefficients of Jacobi's cube series

Let $J(X)$ be Jacobi's cube series. If a
natural number $b$ is not of the form $t(t+1)/2$ for any natural number $t$, then the coefficient
of $X^b$ in $J(X)$ is $0$.

Formalized by `MetaMathlibExt.coeff_jacobiCubeSeries_eq_zero`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/RamanujanPartitionCongruence.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/Partition/RamanujanPartitionCongruence.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/ramanujan-s-partition-congruences/index.html#coeff-jacobi-cube-series-eq-zero).

## Jacobi's cube identity

Let $E(X) = \sum_{k \in \mathbb{Z}} (-1)^k X^{k(3k-1)/2}$ be
Euler's pentagonal series and $J(X) = \sum_{t \ge 0} (-1)^t (2t+1) X^{t(t+1)/2}$ Jacobi's cube
series, both in $\mathbb{Z}[[X]]$. Then $E(X)^3 = J(X)$.

Formalized by `MetaMathlibExt.pentagonalSeries_pow_three`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/RamanujanPartitionCongruence.lean, line 1225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/Partition/RamanujanPartitionCongruence.lean#L1225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/ramanujan-s-partition-congruences/index.html#pentagonal-series-pow-three).

## Partition congruences from a power of Euler's series

Let $p$ be a prime, let $r < p$ be
a natural number, and let $E(X) = \sum_{k \in \mathbb{Z}} (-1)^k X^{k(3k-1)/2}$ be Euler's
pentagonal series in $\mathbb{Z}[[X]]$. If $p$ divides the coefficient of $X^{pm+r}$ in
$E(X)^{p-1}$ for every natural number $m$, then $p$ divides the number of partitions of $pm + r$
for every natural number $m$.

Formalized by `MetaMathlibExt.dvd_partitionFunction_of_dvd_coeff_pentagonalSeries_pow`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/RamanujanPartitionCongruence.lean, line 1358](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/Partition/RamanujanPartitionCongruence.lean#L1358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/ramanujan-s-partition-congruences/index.html#dvd-partition-function-of-dvd-coeff-pent).

## Ramanujan's congruence modulo 5

For every natural number $m$, the number of partitions
of $5m + 4$ is divisible by $5$.

## Sources

- Hartosh Singh Bal and Gaurav Bhatnagar, JIS 27 (2024), Art. 24.1.6, lines 801–804. Live source: https://cs.uwaterloo.ca/journals/JIS/VOL27/Bhatnagar/bhat4.tex

Formalized by `MetaMathlibExt.ramanujan_partition_congruence_mod_five`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/RamanujanPartitionCongruence.lean, line 1469](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/Partition/RamanujanPartitionCongruence.lean#L1469). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/ramanujan-s-partition-congruences/index.html#ramanujan-partition-congruence-mod-five).

## Ramanujan's congruence modulo 7

For every natural number $m$, the number of partitions
of $7m + 5$ is divisible by $7$.

## Sources

- S. Ramanujan, "Some properties of p(n), the number of partitions of n", Proceedings of the Cambridge Philosophical Society 19 (1919), 207–210, where the congruence is stated and proved. The proof follows Ramanujan's argument there: the sixth power of Euler's product is the square of Jacobi's cube series, and a sum of two squares divisible by 7 has both terms divisible by 7.

Formalized by `MetaMathlibExt.ramanujan_partition_congruence_mod_seven`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/RamanujanPartitionCongruence.lean, line 1591](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/Partition/RamanujanPartitionCongruence.lean#L1591). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/ramanujan-s-partition-congruences/index.html#ramanujan-partition-congruence-mod-seven).

## Ramanujan's congruence modulo 11

For every natural number $m$, the number of partitions
of $11m + 6$ is divisible by $11$.

Proof: We follow Hirschhorn's Section 2 residue-section argument, using Euler's
pentagonal number theorem and Jacobi's cube identity.

## Sources

- https://en.wikipedia.org/wiki/Ramanujan%27s_congruences

Formalized by `MetaMathlibExt.ramanujan_partition_congruence_mod_eleven`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/RamanujanPartitionCongruenceModEleven.lean, line 761](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/Partition/RamanujanPartitionCongruenceModEleven.lean#L761). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/ramanujan-s-partition-congruences/index.html#ramanujan-partition-congruence-mod-eleve).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ramanujan's partition congruences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/ramanujan-s-partition-congruences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/ramanujan-s-partition-congruences)
