---
declaration: section
origin: cited
lean: MetaMathlibExt.overpartitionOddPartsCount, MetaMathlibExt.overpartitionOddPartsCount_zero, MetaMathlibExt.overpartitionOdd_pentagonal_recurrence, MetaMathlibExt.overpartitionOdd_triangular_recurrence, MetaMathlibExt.overpartitionOdd_square_recurrence, MetaMathlibExt.overpartitionOdd_eq_sum_partition_pentagonal, MetaMathlibExt.partition_pentagonal_sum_even, MetaMathlibExt.distinctEvenPartsCount
statement: formalized
---

# Overpartitions into odd parts

26 results, 7 proved and 19 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html).

## Overpartitions into odd parts

For a natural number $n$, $\mathrm{po}(n)$ is the
number of overpartitions of $n$ all of whose parts are odd.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, title and Section 1 (values `po(0), …, po(10)` listed after Theorem 5).

Formalized by `MetaMathlibExt.overpartitionOddPartsCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#overpartition-odd-parts-count).

## Overpartitions of zero into odd parts

The number $\mathrm{po}(0)$ of overpartitions
of $0$ into odd parts equals $1$: the empty overpartition is the only one.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, value `po(0) = 1` listed after Theorem 5.

Formalized by `MetaMathlibExt.overpartitionOddPartsCount_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#overpartition-odd-parts-count-zero).

## Pentagonal recurrence for overpartitions into odd parts

Let $\mathrm{po}(j)$ be the
number of overpartitions of $j$ into odd parts. For every natural number $n$, the sum
$\sum_k (-1)^k \, \mathrm{po}(n - k(3k+1)/2)$ over the integers $k$ with $k(3k+1)/2 \le n$
equals $(-1)^{\lceil m/2 \rceil}$ if $n = m(3m+1)/2$ for some integer $m$, and $0$ otherwise.

Such an $m$ is unique, since the numbers $m(3m+1)/2$ with $m$ an integer are distinct.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Theorem 3.

Stated but not proved: `MetaMathlibExt.overpartitionOdd_pentagonal_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#overpartition-odd-pentagonal-recurrence).

## Triangular recurrence for overpartitions into odd parts

Write $\mathrm{po}(m)$ for the
number of overpartitions of $m$ into odd parts. For every natural number $n$, the sum
$\sum_{k \ge 0,\ k(k+1)/2 \le n} (-1)^{\lceil k/2 \rceil} \, \mathrm{po}(n - k(k+1)/2)$ equals
$1$ if $n = m(m+1)/2$ for some natural number $m$, and equals $0$ otherwise.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Theorem 4.

Stated but not proved: `MetaMathlibExt.overpartitionOdd_triangular_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#overpartition-odd-triangular-recurrence).

## Square recurrence for overpartitions into odd parts

Write $\mathrm{po}(m)$ for the
number of overpartitions of $m$ into odd parts. For every natural number $n$, the sum
$\mathrm{po}(n) + 2 \sum_{k \ge 1,\ 2k^2 \le n} (-1)^k \, \mathrm{po}(n - 2k^2)$ equals $1$ if
$n = 0$, equals $2$ if $n = m^2$ for some integer $m \ge 1$, and equals $0$ otherwise.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Theorem 5.

Stated but not proved: `MetaMathlibExt.overpartitionOdd_square_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#overpartition-odd-square-recurrence).

## Overpartitions into odd parts from partitions and pentagonal numbers

Let
$\mathrm{po}(m)$ be the number of overpartitions of $m$ into odd parts and $p(m)$ the number
of partitions of $m$. For every natural number $n$,
$\mathrm{po}(n) = \sum_k (-1)^{\lceil k/2 \rceil} p(n - k(3k+1)/2)$, the sum running over
the integers $k$ with $k(3k+1)/2 \le n$.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Theorem 7.

Stated but not proved: `MetaMathlibExt.overpartitionOdd_eq_sum_partition_pentagonal` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#overpartition-odd-eq-sum-partition-penta).

## Parity form of Euler's pentagonal recurrence

Write $p(m)$ for the number of partitions
of $m$. For every positive integer $n$, the sum
$\sum_{k \in \mathbb{Z},\ k(3k+1)/2 \le n} p(n - k(3k+1)/2)$ is even.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Corollary 2.

Stated but not proved: `MetaMathlibExt.partition_pentagonal_sum_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#partition-pentagonal-sum-even).

## Partitions whose even parts are distinct

For a natural number $n$, $\mathrm{ped}(n)$ is
the number of partitions of $n$ in which every even part occurs exactly once; the odd parts are
unrestricted.

Its generating function is $\sum_{n \ge 0} \mathrm{ped}(n) q^n = (q^4; q^4)_\infty / (q; q)_\infty$.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Section 1 (definition of `ped(n)` before Theorem 1).

Formalized by `MetaMathlibExt.distinctEvenPartsCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#distinct-even-parts-count).

## Partitions whose odd parts are distinct

For a natural number $n$, $\mathrm{pod}(n)$ is
the number of partitions of $n$ in which every odd part occurs exactly once; the even parts are
unrestricted.

Its generating function is
$\sum_{n \ge 0} \mathrm{pod}(n) q^n = (-q; q^2)_\infty / (q^2; q^2)_\infty$.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Section 3 (definition of `pod(n)` before Theorem 6).

Formalized by `MetaMathlibExt.distinctOddPartsCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#distinct-odd-parts-count).

## Partitions with no part congruent to 2 modulo 4

For a natural number $n$, $P_2(n)$ is
the number of partitions of $n$ none of whose parts is congruent to $2$ modulo $4$.

Its generating function is $\sum_{n \ge 0} P_2(n) q^n = (q^2; q^4)_\infty / (q; q)_\infty$.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Section 3 (definition of `P_2(n)` before Theorem 11).

Formalized by `MetaMathlibExt.partsNotTwoModFourCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#parts-not-two-mod-four-count).

## Bipartitions into distinct parts

Let $\operatorname{pd}(m)$ be the number of partitions
of $m$ into distinct parts. For a natural number $n$, $q(n)$ is the number of ordered pairs of
partitions into distinct parts whose sizes add up to $n$, that is,
$q(n) = \sum_{k=0}^{n} \operatorname{pd}(k) \operatorname{pd}(n-k)$.

Its generating function is $\sum_{n \ge 0} q(n) x^n = (-x; x)_\infty^2$, where
$(a; x)_\infty = \prod_{i \ge 0} (1 - a x^i)$.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Section 3 (definition of `q(n)` before Theorem 12).

Formalized by `MetaMathlibExt.distinctPartsBipartitionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#distinct-parts-bipartition-count).

## Values at zero of the restricted partition counts

The number $\operatorname{ped}(0)$ of
partitions of $0$ in which no even part is repeated, the number $\operatorname{pod}(0)$ of
partitions of $0$ in which no odd part is repeated, the number $P_2(0)$ of partitions of $0$ with
no part congruent to $2$ modulo $4$, and the number $q(0)$ of ordered pairs of partitions into
distinct parts with sizes adding up to $0$ are all equal to $1$, as only the empty partition (or
the pair of empty partitions) is counted.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Sections 1 and 3 (definitions of `ped`, `pod`, `P_2`, `q`).

Formalized by `MetaMathlibExt.distinctEvenParts_distinctOddParts_partsNotTwoModFour_bipartition_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#distinct-even-parts-distinct-odd-parts-p).

## Merca's triangular recurrence for partitions with distinct even parts

Let
$\operatorname{ped}(m)$ be the number of partitions of $m$ in which no even part is repeated. For
every $n \ge 0$, the sum $\sum_{j \ge 0} (-1)^{\lceil j/2 \rceil} \operatorname{ped}(n - j(j+1)/2)$
over the $j$ with $j(j+1)/2 \le n$ equals $1$ if $n = k(k+1)$ for some integer $k \ge 0$, and $0$
otherwise.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Theorem 1, quoting M. Merca (via da Silva and Sakai).

Stated but not proved: `MetaMathlibExt.distinctEvenParts_triangular_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#distinct-even-parts-triangular-recurrenc).

## Merca's square recurrence for partitions with distinct even parts

Let
$\operatorname{ped}(m)$ be the number of partitions of $m$ in which no even part is repeated. For
every $n \ge 0$, the sum $\sum_j (-1)^j \operatorname{ped}(n - 2j^2)$ over the integers $j$ with
$2j^2 \le n$ equals $1$ if $n = k(k+1)/2$ for some integer $k \ge 0$, and $0$ otherwise.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Theorem 2, quoting M. Merca (via da Silva and Sakai).

Stated but not proved: `MetaMathlibExt.distinctEvenParts_square_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#distinct-even-parts-square-recurrence).

## Overpartitions into odd parts from partitions with distinct odd parts

Let
$\mathrm{po}(m)$ be the number of overpartitions of $m$ into odd parts and $\mathrm{pod}(m)$
the number of partitions of $m$ whose odd parts are distinct. For every natural number $n$,
$\mathrm{po}(n) = \sum_k \mathrm{pod}(n - k(k+1)/2)$, the sum running over the natural
numbers $k$ with $k(k+1)/2 \le n$.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Theorem 6.

Stated but not proved: `MetaMathlibExt.overpartitionOdd_eq_sum_distinctOddParts_triangular` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#overpartition-odd-eq-sum-distinct-odd-pa).

## Evenness of a triangular sum of partition counts with distinct odd parts

Let
$\operatorname{pod}(m)$ be the number of partitions of $m$ in which no odd part is repeated. For
every $n > 0$, the sum $\sum_{k \ge 0} \operatorname{pod}(n - k(k+1)/2)$ over the $k$ with
$k(k+1)/2 \le n$ is even.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Corollary 1.

Stated but not proved: `MetaMathlibExt.distinctOddParts_triangular_sum_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#distinct-odd-parts-triangular-sum-even).

## Overpartitions into odd parts from overpartitions and squares

Let $\mathrm{po}(m)$
be the number of overpartitions of $m$ into odd parts and $\overline{p}(m)$ the number of
overpartitions of $m$. For every natural number $n$,
$\mathrm{po}(n) = \sum_k (-1)^k \, \overline{p}(n - 2k^2)$, the sum running over the
integers $k$ with $2k^2 \le n$.

With the partition function $p$ in place of $\overline{p}$ the identity fails at $n = 1$:
$\mathrm{po}(1) = 2$ but $p(1) = 1$.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Theorem 8.

Stated but not proved: `MetaMathlibExt.overpartitionOdd_eq_sum_overpartition_square` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#overpartition-odd-eq-sum-overpartition-s).

## Overpartitions of odd numbers into odd parts

Let $\mathrm{po}(m)$ be the number of
overpartitions of $m$ into odd parts and $\overline{p}(m)$ the number of overpartitions of $m$.
For every natural number $n$,
$\mathrm{po}(2n+1) = 2 \sum_k \overline{p}(n - 2k(k+1))$, the sum running over the natural
numbers $k$ with $2k(k+1) \le n$.

With the partition function $p$ in place of $\overline{p}$ the identity fails at $n = 1$.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Theorem 9.

Stated but not proved: `MetaMathlibExt.overpartitionOdd_odd_eq_two_mul_sum_overpartition` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#overpartition-odd-odd-eq-two-mul-sum-ove).

## Overpartitions of even numbers into odd parts

Let $\mathrm{po}(m)$ be the number of
overpartitions of $m$ into odd parts and $\overline{p}(m)$ the number of overpartitions of $m$.
For every natural number $n$,
$\mathrm{po}(2n) = \overline{p}(n) + 2 \sum_k \overline{p}(n - 2k^2)$, the sum running over
the integers $k \ge 1$ with $2k^2 \le n$.

The sum cannot start at $k = 0$: at $n = 0$ that would give
$\overline{p}(0) + 2 \, \overline{p}(0) = 3$, whereas $\mathrm{po}(0) = 1$.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Theorem 10.

Stated but not proved: `MetaMathlibExt.overpartitionOdd_even_eq_sum_overpartition` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#overpartition-odd-even-eq-sum-overpartit).

## Overpartitions into odd parts from partitions with no part congruent to 2 modulo 4

Let $\mathrm{po}(m)$ be the number of overpartitions of $m$ into odd parts and $P_2(m)$ the
number of partitions of $m$ with no part congruent to $2$ modulo $4$. For every natural
number $n$, $\mathrm{po}(n) = \sum_k P_2(n - k(k+1)/2)$, the sum running over the natural
numbers $k$ with $k(k+1)/2 \le n$.

The case $n = 0$ is included: there both sides equal $1$.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Theorem 11.

Stated but not proved: `MetaMathlibExt.overpartitionOdd_eq_sum_partsNotTwoModFour_triangular` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#overpartition-odd-eq-sum-parts-not-two-m).

## Parity of a triangular sum of partitions with no part congruent to 2 modulo 4

Write
$P_2(m)$ for the number of partitions of $m$ with no part congruent to $2$ modulo $4$. For every
positive integer $n$, the sum $\sum_{k \ge 0,\ k(k+1)/2 \le n} P_2(n - k(k+1)/2)$ is even.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Corollary 3.

Stated but not proved: `MetaMathlibExt.partsNotTwoModFour_triangular_sum_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#parts-not-two-mod-four-triangular-sum-ev).

## Bipartitions into distinct parts from the partition function

Let $q(n)$ be the number of
ordered pairs of partitions into distinct parts whose sizes add up to $n$, and let $p(m)$ be the
number of partitions of $m$. For every $n \ge 0$, $q(n) = \sum_{k \ge 0} p(n - k(k+1)/2)$, where
the sum runs over the $k$ with $k(k+1)/2 \le n$.

The source states this for $n > 0$; it also holds at $n = 0$, where both sides equal $1$.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Theorem 12.

Stated but not proved: `MetaMathlibExt.distinctPartsBipartition_eq_sum_partition_triangular` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#distinct-parts-bipartition-eq-sum-partit).

## Overpartitions into odd parts and partitions into distinct odd parts

Let
$\mathrm{po}(m)$ be the number of overpartitions of $m$ into odd parts and $\mathrm{pdo}(m)$
the number of partitions of $m$ into distinct odd parts. For every natural number $n$, the
sum $\sum_k (-1)^k \, \mathrm{po}(n - k(3k+1)/2)$ over the integers $k$ with
$k(3k+1)/2 \le n$ equals the sum $\sum_k (-1)^k \, \mathrm{pdo}(n - k(3k+1))$ over the
integers $k$ with $k(3k+1) \le n$.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Theorem 13.

Stated but not proved: `MetaMathlibExt.overpartitionOdd_pentagonal_sum_eq_oddDistincts` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#overpartition-odd-pentagonal-sum-eq-odd).

## Pentagonal recurrence for partitions into distinct odd parts

Let $\operatorname{pdo}(m)$
be the number of partitions of $m$ into distinct odd parts. For every $n \ge 0$, the sum
$\sum_k (-1)^k \operatorname{pdo}(n - k(3k+1))$ over the integers $k$ with $k(3k+1) \le n$
equals $(-1)^{\lceil m/2 \rceil}$ if $n = m(3m+1)/2$ for some integer $m$, and $0$ otherwise.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Corollary 4.

Stated but not proved: `MetaMathlibExt.oddDistincts_pentagonal_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#odd-distincts-pentagonal-recurrence).

## Overpartitions into odd parts and partitions into distinct parts

Write $\mathrm{po}(m)$
for the number of overpartitions of $m$ into odd parts and $\mathrm{pd}(m)$ for the number of
partitions of $m$ into distinct parts. For every natural number $n$,
$\sum_{k \ge 0,\ k(k+1)/2 \le n} (-1)^{\lceil k/2 \rceil} \, \mathrm{po}(n - k(k+1)/2) =
\sum_{k \in \mathbb{Z},\ k(3k+1) \le n} (-1)^k \, \mathrm{pd}(n - k(3k+1))$.

The sum on the left runs over $k \ge 0$ only. Taken over all integers $k$ it would double, since
$k$ and $-1 - k$ give the same term, and the identity would fail at $n = 0$.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Theorem 14.

Stated but not proved: `MetaMathlibExt.overpartitionOdd_triangular_sum_eq_distincts` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#overpartition-odd-triangular-sum-eq-dist).

## Pentagonal recurrence for partitions into distinct parts

Let $\operatorname{pd}(m)$ be the
number of partitions of $m$ into distinct parts. For every $n \ge 0$, the sum
$\sum_k (-1)^k \operatorname{pd}(n - k(3k+1))$ over the integers $k$ with $k(3k+1) \le n$ equals
$1$ if $n = m(m+1)/2$ for some integer $m \ge 0$, and $0$ otherwise.

## Sources

- Deepthi G. and S. Chandankumar, *Linear Relations for Overpartitions into Odd Parts*, INTEGERS 26 (2026), Article A60, Corollary 5.

Stated but not proved: `MetaMathlibExt.distincts_pentagonal_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/OverpartitionsOddPartsWanted.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html#distincts-pentagonal-recurrence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Overpartitions into odd parts](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions-into-odd-parts)
