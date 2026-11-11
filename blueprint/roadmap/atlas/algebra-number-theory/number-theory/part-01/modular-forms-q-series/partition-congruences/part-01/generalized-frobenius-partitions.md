---
declaration: section
origin: cited
lean: MetaMathlibExt.frobeniusPartitionRepCount, MetaMathlibExt.frobeniusPartitionRepCount_four_zero_one, MetaMathlibExt.frobeniusPartitionRepCount_four_four_mul_add_three_mod_two, MetaMathlibExt.frobeniusPartitionRepCount_four_two_mul_add_one_mod_two, MetaMathlibExt.frobeniusPartitionRepCount_four_four_mul_add_one_mod_two, MetaMathlibExt.frobeniusPartitionRepCount_four_ten_mul_add_six_mod_five, MetaMathlibExt.frobeniusPartitionRepCount_four_ten_mul_add_one_mod_five, MetaMathlibExt.frobeniusPartitionRepCount_four_two_dissection
statement: formalized
---

# Generalized Frobenius partitions

11 results, 2 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-frobenius-partitions/index.html).

## Frobenius partitions with at most $k$ repetitions

For natural numbers $k$ and $n$,
$\varphi_k(n)$ is the number of generalized Frobenius partitions of $n$ in which each integer
appears at most $k$ times in each row. Concretely, $\varphi_k(n)$ is the number of pairs of
functions $m_1, m_2 \colon \{0, 1, \dots, n\} \to \{0, 1, \dots, k\}$ with
$\sum_i m_1(i) = \sum_i m_2(i)$ and $\sum_i (i + 1)\, m_1(i) + \sum_i i\, m_2(i) = n$.

Here a generalized Frobenius partition of $n$ is a two-rowed array of nonnegative integers with
$r$ columns, both rows nonincreasing, whose entries sum to $n - r$; its entries are at most $n$,
and $m_1(i)$, $m_2(i)$ count how often $i$ appears in the top and bottom rows.

## Sources

- Bipul Kumar Sarmah and Satyajit Gayan, *Congruences for F-partitions with 4 Repetitions*, INTEGERS 25 (2025), Article A17, Section 1 (definition of `φ_k(n)`, after Andrews).

Formalized by `MetaMathlibExt.frobeniusPartitionRepCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-frobenius-partitions/index.html#frobenius-partition-rep-count).

## Initial values of $\varphi_4$

Let $\varphi_4(n)$ be the number of generalized Frobenius
partitions of $n$ in which each integer appears at most $4$ times in each row. Then
$\varphi_4(0) = 1$ (the empty array) and $\varphi_4(1) = 1$ (the single column with both entries
$0$).

## Sources

- Bipul Kumar Sarmah and Satyajit Gayan, *Congruences for F-partitions with 4 Repetitions*, INTEGERS 25 (2025), Article A17, Section 1 (definition of `φ_k(n)`).

Formalized by `MetaMathlibExt.frobeniusPartitionRepCount_four_zero_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-frobenius-partitions/index.html#frobenius-partition-rep-count-four-zero).

## $\varphi_4(4n+3)$ is even

Let $\varphi_4(n)$ be the number of generalized Frobenius
partitions of $n$ in which each integer appears at most $4$ times in each row. For every natural
number $n$, $\varphi_4(4n + 3) \equiv 0 \pmod 2$.

## Sources

- Bipul Kumar Sarmah and Satyajit Gayan, *Congruences for F-partitions with 4 Repetitions*, INTEGERS 25 (2025), Article A17, Theorem 2.

Stated but not proved: `MetaMathlibExt.frobeniusPartitionRepCount_four_four_mul_add_three_mod_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-frobenius-partitions/index.html#frobenius-partition-rep-count-four-four).

## $\varphi_4(2N+1)$ is even when $5 \nmid N$

Let $\varphi_4(n)$ be the number of generalized
Frobenius partitions of $n$ in which each integer appears at most $4$ times in each row. For every
positive integer $N$ not divisible by $5$, $\varphi_4(2N + 1) \equiv 0 \pmod 2$.

## Sources

- Bipul Kumar Sarmah and Satyajit Gayan, *Congruences for F-partitions with 4 Repetitions*, INTEGERS 25 (2025), Article A17, Theorem 3.

Stated but not proved: `MetaMathlibExt.frobeniusPartitionRepCount_four_two_mul_add_one_mod_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-frobenius-partitions/index.html#frobenius-partition-rep-count-four-two-m).

## Parity of $\varphi_4(4n+1)$

Let $\varphi_4(n)$ be the number of generalized Frobenius
partitions of $n$ in which each integer appears at most $4$ times in each row. For every natural
number $n$, $\varphi_4(4n + 1)$ is odd if and only if $2n = 5k(3k + 1)$ for some integer $k$,
that is, $n = 5k(3k \pm 1)/2$ for some integer $k$.

## Sources

- Bipul Kumar Sarmah and Satyajit Gayan, *Congruences for F-partitions with 4 Repetitions*, INTEGERS 25 (2025), Article A17, Theorem 4.

Stated but not proved: `MetaMathlibExt.frobeniusPartitionRepCount_four_four_mul_add_one_mod_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-frobenius-partitions/index.html#frobenius-partition-rep-count-four-four-2).

## $\varphi_4(10n+6)$ is divisible by $5$

Let $\varphi_4(n)$ be the number of generalized
Frobenius partitions of $n$ in which each integer appears at most $4$ times in each row. For every
natural number $n$, $\varphi_4(10n + 6) \equiv 0 \pmod 5$.

## Sources

- Bipul Kumar Sarmah and Satyajit Gayan, *Congruences for F-partitions with 4 Repetitions*, INTEGERS 25 (2025), Article A17, Theorem 5.

Stated but not proved: `MetaMathlibExt.frobeniusPartitionRepCount_four_ten_mul_add_six_mod_five` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-frobenius-partitions/index.html#frobenius-partition-rep-count-four-ten-m).

## $\varphi_4(10n+1)$ modulo $5$

Let $\varphi_4(n)$ be the number of generalized Frobenius
partitions of $n$ in which each integer appears at most $4$ times in each row, and let $n$ be a
natural number. If $n = k(3k + 1)$ for an integer $k$, then
$\varphi_4(10n + 1) \equiv k + 1 \pmod 5$; if there is no such integer $k$, then
$\varphi_4(10n + 1) \equiv 0 \pmod 5$.

## Sources

- Bipul Kumar Sarmah and Satyajit Gayan, *Congruences for F-partitions with 4 Repetitions*, INTEGERS 25 (2025), Article A17, Theorem 6.

Stated but not proved: `MetaMathlibExt.frobeniusPartitionRepCount_four_ten_mul_add_one_mod_five` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-frobenius-partitions/index.html#frobenius-partition-rep-count-four-ten-m-2).

## The 2-dissection of the generating function of $\varphi_4$

Let $\varphi_4(n)$ be the
number of generalized Frobenius partitions of $n$ in which each integer appears at most $4$ times
in each row, and let $f_k = \prod_{m \ge 1} (1 - q^{km})$ in the ring of integer power series in
$q$. Then

$$f_1^{12} f_4^4 f_5 f_{10}^2 \sum_{n \ge 0} \varphi_4(2n)\, q^n =
f_1^3 f_2^{10} f_4^2 f_5^2 f_{10} + 2q f_2^{15} f_5 f_{20}^2 - 8q f_1^5 f_4^{10} f_{10}^3$$

and

$$f_1^6 f_4^2 f_5^2 \sum_{n \ge 0} \varphi_4(2n + 1)\, q^n = f_2^7 f_{10}^2.$$

Dividing by the Euler products on the left gives the quotient forms of the source, for example
$\sum_{n \ge 0} \varphi_4(2n + 1)\, q^n = f_2^7 f_{10}^2 / (f_1^6 f_4^2 f_5^2)$.

## Sources

- Bipul Kumar Sarmah and Satyajit Gayan, *Congruences for F-partitions with 4 Repetitions*, INTEGERS 25 (2025), Article A17, Theorem 1, eqs. (3) and (4).

Stated but not proved: `MetaMathlibExt.frobeniusPartitionRepCount_four_two_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-frobenius-partitions/index.html#frobenius-partition-rep-count-four-two-d).

## Ramanujan's theta product identity for $ab = cd$

Let
$f(a,b) = \sum_{n \in \mathbb{Z}} a^{n(n+1)/2} b^{n(n-1)/2}$ be Ramanujan's general theta
function. If $a, b, c, d$ are complex numbers with $a \ne 0$, $|ab| < 1$ and $ab = cd$, then

$$f(a,b)\,f(c,d) = f(ad,bc)\,f(ac,bd) + a\,f(c/a, a^2bd)\,f(d/a, a^2bc).$$

In each of the six theta functions the two arguments have product of modulus $|ab|$ or
$|ab|^2$, which is less than $1$, so every series converges.

## Sources

- Bipul Kumar Sarmah and Satyajit Gayan, *Congruences for F-partitions with 4 Repetitions*, INTEGERS 25 (2025), Article A17, Lemma 1, eq. (12), quoting Berndt, *Ramanujan's Notebooks, Part III*, p. 45, Entry 29.

Stated but not proved: `MetaMathlibExt.ramanujanTheta_mul_of_mul_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-frobenius-partitions/index.html#ramanujan-theta-mul-of-mul-eq).

## A 2-dissection of the reciprocal Euler product of levels 1 and 5

Let
$f_k = \prod_{m \ge 1} (1 - q^{km})$ in the ring of integer power series in $q$. Then

$$f_2^{10} f_8^2 f_{10}^3 f_{20} = f_1^3 f_2^3 f_4^4 f_5 f_8^2 f_{10}^2 f_{20} -
2q f_1^3 f_2 f_4^6 f_5 f_8^2 f_{20}^3 + 5q f_1^3 f_2^2 f_4^3 f_5 f_8^2 f_{10}^3 f_{20}^2 +
2q^2 f_1^3 f_4^9 f_5 f_{10} f_{40}^2.$$

Dividing both sides by $f_1^3 f_5 f_2^{10} f_8^2 f_{10}^3 f_{20}$ gives the form in the source,
$1/(f_1^3 f_5) = f_4^4/(f_2^7 f_{10}) - 2q f_4^6 f_{20}^2/(f_2^9 f_{10}^3) +
5q f_4^3 f_{20}/f_2^8 + 2q^2 f_4^9 f_{40}^2/(f_2^{10} f_8^2 f_{10}^2 f_{20})$.

## Sources

- Bipul Kumar Sarmah and Satyajit Gayan, *Congruences for F-partitions with 4 Repetitions*, INTEGERS 25 (2025), Article A17, Lemma 4, eq. (15).

Stated but not proved: `MetaMathlibExt.one_div_f1_cube_f5_two_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-frobenius-partitions/index.html#one-div-f1-cube-f5-two-dissection).

## A level-10 Euler-product identity

Let $f_k = \prod_{m \ge 1} (1 - q^{km})$ in the ring of
integer power series in $q$. Then
$f_2^5 f_5^2 = f_1^5 f_5 f_{10} + 5q f_1^2 f_2 f_{10}^4$.

Dividing both sides by $f_1^5 f_2^2 f_{10}^2$ gives the form in the source,
$f_2^3 f_5^2/(f_1^5 f_{10}^2) = f_5/(f_2^2 f_{10}) + 5q f_{10}^2/(f_1^3 f_2)$.

## Sources

- Bipul Kumar Sarmah and Satyajit Gayan, *Congruences for F-partitions with 4 Repetitions*, INTEGERS 25 (2025), Article A17, Lemma 5, eq. (17).

Stated but not proved: `MetaMathlibExt.f2_cube_f5_sq_quotient_identity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/FrobeniusPartitionsFourRepetitionsWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-frobenius-partitions/index.html#f2-cube-f5-sq-quotient-identity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized Frobenius partitions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-frobenius-partitions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/generalized-frobenius-partitions)
