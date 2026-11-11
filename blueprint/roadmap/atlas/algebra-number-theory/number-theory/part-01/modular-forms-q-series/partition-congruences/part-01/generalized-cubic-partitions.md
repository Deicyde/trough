---
declaration: section
origin: cited
lean: MetaMathlibExt.generalizedCubicPartitionSeries, MetaMathlibExt.generalizedCubicPartitionCount, MetaMathlibExt.generalizedCubicPartitionCount_generatingFunction, MetaMathlibExt.generalizedCubicPartitionCount_zero, MetaMathlibExt.generalizedCubicPartitionCount_seven_eleven, MetaMathlibExt.generalizedCubicPartitionCount_prime_five_seven_mod_eight, MetaMathlibExt.generalizedCubicPartitionCount_prime_three_seven_mod_eight
statement: formalized
---

# Generalized cubic partitions

7 results, 4 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-cubic-partitions/index.html).

## Generating function of generalized cubic partitions

Let
$f_k = \prod_{m \ge 1} (1 - q^{km})$ be the Euler products. For a natural number $c$, this is
the integer power series $1/(f_1 f_2^{c-1})$ in $q$, the inverse of $f_1 f_2^{c-1}$ (whose
constant term is $1$). For $c \ge 1$ its coefficient of $q^n$ is the number of partitions of
$n$ whose even parts may each come in $c$ colors. For $c = 0$ the exponent $c - 1$ is
truncated to $0$, so the series is then the inverse of $f_1$.

## Sources

- Russelle Guadalupe, *A Note on Congruences for Generalized Cubic Partitions Modulo Primes*, INTEGERS 25 (2025), Article A20, Section 1.

Formalized by `MetaMathlibExt.generalizedCubicPartitionSeries`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/GeneralizedCubicPartitionWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/GeneralizedCubicPartitionWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-cubic-partitions/index.html#generalized-cubic-partition-series).

## Generalized cubic partition numbers

Let $f_k = \prod_{m \ge 1} (1 - q^{km})$ be the
Euler products. For natural numbers $c$ and $n$, $a_c(n)$ is the integer coefficient of $q^n$
in the generating function of generalized cubic partitions, the power series
$1/(f_1 f_2^{c-1})$. For $c \ge 1$ it is the number of partitions of $n$ whose even parts may
each come in $c$ colors; $c = 1$ gives the partition numbers and $c = 2$ Chan's cubic
partition numbers. For $c = 0$ the exponent $c - 1$ is truncated to $0$, so $a_0(n)$ is also
the number of partitions of $n$.

## Sources

- Russelle Guadalupe, *A Note on Congruences for Generalized Cubic Partitions Modulo Primes*, INTEGERS 25 (2025), Article A20, Section 1.

Formalized by `MetaMathlibExt.generalizedCubicPartitionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/GeneralizedCubicPartitionWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/GeneralizedCubicPartitionWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-cubic-partitions/index.html#generalized-cubic-partition-count).

## Generating function identity for generalized cubic partition numbers

Let
$f_k = \prod_{m \ge 1} (1 - q^{km})$ be the Euler products and $a_c(n)$ the generalized cubic
partition numbers. For every natural number $c$,
$f_1 f_2^{c-1} \sum_{n \ge 0} a_c(n) q^n = 1$ as integer power series in $q$, where for
$c = 0$ the exponent $c - 1$ is truncated to $0$.

## Sources

- Russelle Guadalupe, *A Note on Congruences for Generalized Cubic Partitions Modulo Primes*, INTEGERS 25 (2025), Article A20, Section 1.

Formalized by `MetaMathlibExt.generalizedCubicPartitionCount_generatingFunction`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/GeneralizedCubicPartitionWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/GeneralizedCubicPartitionWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-cubic-partitions/index.html#generalized-cubic-partition-count-genera).

## Generalized cubic partitions of zero

For every natural number $c$, the generalized
cubic partition number $a_c(0)$ equals $1$.

## Sources

- Russelle Guadalupe, *A Note on Congruences for Generalized Cubic Partitions Modulo Primes*, INTEGERS 25 (2025), Article A20, Section 1.

Formalized by `MetaMathlibExt.generalizedCubicPartitionCount_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/GeneralizedCubicPartitionWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/GeneralizedCubicPartitionWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-cubic-partitions/index.html#generalized-cubic-partition-count-zero).

## Amdeberhan–Sellers–Singh congruences

For every natural number $n$, the generalized
cubic partition numbers satisfy $a_3(7n + 4) \equiv 0 \pmod{7}$ and
$a_5(11n + 10) \equiv 0 \pmod{11}$.

## Sources

- Russelle Guadalupe, *A Note on Congruences for Generalized Cubic Partitions Modulo Primes*, INTEGERS 25 (2025), Article A20, Theorem 1 (quoting Amdeberhan, Sellers, and Singh), Equations (1) and (2).

Stated but not proved: `MetaMathlibExt.generalizedCubicPartitionCount_seven_eleven` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/GeneralizedCubicPartitionWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/GeneralizedCubicPartitionWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-cubic-partitions/index.html#generalized-cubic-partition-count-seven).

## Generalized cubic partition congruences for primes $p \equiv 5, 7 \pmod 8$

Let $a_c(n)$
be the generalized cubic partition numbers, let $p$ be a prime with $p \equiv 5$ or
$p \equiv 7 \pmod 8$, and let $l$ be a natural number with $p \mid 8l + 3$. Then
$a_{p-4}(pn + l) \equiv 0 \pmod p$ for every natural number $n$.

The source assumes $0 \le l \le p - 1$; the statement for a larger $l$ follows from the one for
$l \bmod p$, which satisfies the same divisibility.

## Sources

- Russelle Guadalupe, *A Note on Congruences for Generalized Cubic Partitions Modulo Primes*, INTEGERS 25 (2025), Article A20, Theorem 2, Equation (9).

Stated but not proved: `MetaMathlibExt.generalizedCubicPartitionCount_prime_five_seven_mod_eight` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/GeneralizedCubicPartitionWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/GeneralizedCubicPartitionWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-cubic-partitions/index.html#generalized-cubic-partition-count-prime).

## Generalized cubic partition congruences modulo primes $p \ge 7$, $p \equiv 3, 7 \pmod 8$

Let $a_c(n)$ be the generalized cubic partition numbers and let $p \ge 7$ be a prime with
$p \equiv 3$ or $p \equiv 7 \pmod 8$. Then
$a_{p-6}\bigl(pn + 13(p^2 - 1)/24\bigr) \equiv 0 \pmod p$ for every natural number $n$.

Since $24 \mid p^2 - 1$, the shift $13(p^2 - 1)/24$ is a natural number.

## Sources

- Russelle Guadalupe, *A Note on Congruences for Generalized Cubic Partitions Modulo Primes*, INTEGERS 25 (2025), Article A20, Theorem 3, Equation (13).

Stated but not proved: `MetaMathlibExt.generalizedCubicPartitionCount_prime_three_seven_mod_eight` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/GeneralizedCubicPartitionWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/GeneralizedCubicPartitionWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-cubic-partitions/index.html#generalized-cubic-partition-count-prime-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized cubic partitions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-cubic-partitions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-cubic-partitions)
