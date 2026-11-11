---
declaration: section
origin: cited
lean: MetaMathlibExt.overcubicTripleSeries, MetaMathlibExt.overcubicTripleCount, MetaMathlibExt.overcubicTripleCount_generatingFunction, MetaMathlibExt.overcubicTripleCount_zero, MetaMathlibExt.f1_sq_two_dissection, MetaMathlibExt.one_div_f1_sq_two_dissection, MetaMathlibExt.f1_cube_three_dissection, MetaMathlibExt.overcubicTripleCount_congruences_odd_args
statement: formalized
---

# Overcubic partition triples

15 results, 4 proved and 11 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overcubic-partition-triples/index.html).

## The overcubic partition triple series

The generating function of overcubic partition
triples is the integer power series $f_4^3 / (f_1^6 f_2^3)$ in $q$, where
$f_k = \prod_{j \ge 1} (1 - q^{kj})$; the inverse of $f_1^6 f_2^3$ exists because its constant
coefficient is $1$.

## Sources

- S. Shivaprasada Nayaka, B. N. Dharmendra, and M. C. Mahesh Kumar, *Divisibility Properties for Overcubic Partition Triples*, INTEGERS 24 (2024), Article A80, Section 1; the same generating function is quoted from this paper by Saikia and Sarma (arXiv:2411.00013, eq. (2)) and by Chen, Jin, and Yao (arXiv:2504.06941, eq. (1.1)).

Formalized by `MetaMathlibExt.overcubicTripleSeries`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overcubic-partition-triples/index.html#overcubic-triple-series).

## Number of overcubic partition triples

For a natural number $n$, $\mathrm{bt}(n)$, the
number of overcubic partition triples of $n$, is defined as the integer coefficient of $q^n$ in
the power series $f_4^3 / (f_1^6 f_2^3)$, where $f_k = \prod_{j \ge 1} (1 - q^{kj})$.

## Sources

- S. Shivaprasada Nayaka, B. N. Dharmendra, and M. C. Mahesh Kumar, *Divisibility Properties for Overcubic Partition Triples*, INTEGERS 24 (2024), Article A80, Section 1.

Formalized by `MetaMathlibExt.overcubicTripleCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overcubic-partition-triples/index.html#overcubic-triple-count).

## Generating function for overcubic partition triples

For $k \ge 1$ let
$f_k = \prod_{m \ge 1} (1 - q^{km})$, and let $\mathrm{bt}(n)$, the number of overcubic partition
triples of $n$, be the coefficient of $q^n$ in $f_4^3/(f_1^6 f_2^3)$. Then, as integer power
series in $q$,

$$f_1^6 f_2^3 \sum_{n \ge 0} \mathrm{bt}(n) q^n = f_4^3.$$

## Sources

- S. Shivaprasada Nayaka, B. N. Dharmendra, and M. C. Mahesh Kumar, *Divisibility Properties for Overcubic Partition Triples*, INTEGERS 24 (2024), Article A80, Section 1.

Formalized by `MetaMathlibExt.overcubicTripleCount_generatingFunction`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overcubic-partition-triples/index.html#overcubic-triple-count-generating-functi).

## Overcubic partition triples of $0$

The number $\mathrm{bt}(0)$ of overcubic partition
triples of $0$ equals $1$.

## Sources

- S. Shivaprasada Nayaka, B. N. Dharmendra, and M. C. Mahesh Kumar, *Divisibility Properties for Overcubic Partition Triples*, INTEGERS 24 (2024), Article A80, Section 1.

Formalized by `MetaMathlibExt.overcubicTripleCount_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overcubic-partition-triples/index.html#overcubic-triple-count-zero).

## The 2-dissection of $f_1^2$

For $k \ge 1$ let $f_k = \prod_{m \ge 1} (1 - q^{km})$, an
integer power series in $q$. Then

$$f_1^2 f_4^2 f_8 f_{16}^2 = f_2 f_8^6 - 2 q f_2 f_4^2 f_{16}^4.$$

Dividing by $f_4^2 f_8 f_{16}^2$ gives
$f_1^2 = \frac{f_2 f_8^5}{f_4^2 f_{16}^2} - 2q \frac{f_2 f_{16}^2}{f_8}$.

## Sources

- S. Shivaprasada Nayaka, B. N. Dharmendra, and M. C. Mahesh Kumar, *Divisibility Properties for Overcubic Partition Triples*, INTEGERS 24 (2024), Article A80, Lemma 1, eq. (39).

Stated but not proved: `MetaMathlibExt.f1_sq_two_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overcubic-partition-triples/index.html#f1-sq-two-dissection).

## The 2-dissection of $1/f_1^2$

For $k \ge 1$ let
$f_k = \prod_{m \ge 1} (1 - q^{km})$, an integer power series in $q$. Then

$$f_2^5 f_8 f_{16}^2 = f_1^2 f_8^6 + 2 q f_1^2 f_4^2 f_{16}^4.$$

Dividing by $f_1^2 f_2^5 f_8 f_{16}^2$ gives
$\frac{1}{f_1^2} = \frac{f_8^5}{f_2^5 f_{16}^2} + 2q \frac{f_4^2 f_{16}^2}{f_2^5 f_8}$.

## Sources

- S. Shivaprasada Nayaka, B. N. Dharmendra, and M. C. Mahesh Kumar, *Divisibility Properties for Overcubic Partition Triples*, INTEGERS 24 (2024), Article A80, Lemma 1, eq. (40).

Stated but not proved: `MetaMathlibExt.one_div_f1_sq_two_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overcubic-partition-triples/index.html#one-div-f1-sq-two-dissection).

## The 3-dissection of $f_1^3$

For $k \ge 1$ let $f_k = \prod_{m \ge 1} (1 - q^{km})$, an
integer power series in $q$. Then

$$
f_1^3 f_3 f_6^2 f_9^3 f_{18}^3 = f_6^3 f_9^9 + 4 q^3 f_3^3 f_{18}^9 - 3 q f_3 f_6^2 f_9^6 f_{18}^3.
$$

Dividing by $f_3 f_6^2 f_9^3 f_{18}^3$ gives
$f_1^3 = \frac{f_6 f_9^6}{f_3 f_{18}^3} + 4q^3 \frac{f_3^2 f_{18}^6}{f_6^2 f_9^3} - 3q f_9^3$.

## Sources

- S. Shivaprasada Nayaka, B. N. Dharmendra, and M. C. Mahesh Kumar, *Divisibility Properties for Overcubic Partition Triples*, INTEGERS 24 (2024), Article A80, Lemma 2, eq. (41).

Stated but not proved: `MetaMathlibExt.f1_cube_three_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overcubic-partition-triples/index.html#f1-cube-three-dissection).

## Congruences for overcubic partition triples at odd arguments

Let $\mathrm{bt}(n)$ be the
number of overcubic partition triples of $n$. For all natural numbers $n$ and $\alpha$,
$\mathrm{bt}(8n+7)$ is divisible by $32$, and each of $\mathrm{bt}(8n+5)$, $\mathrm{bt}(72n+33)$,
$\mathrm{bt}(72n+57)$ and $\mathrm{bt}(8 \cdot 9^{\alpha+2} n + 33 \cdot 9^{\alpha+1})$ is divisible
by $8$.

## Sources

- S. Shivaprasada Nayaka, B. N. Dharmendra, and M. C. Mahesh Kumar, *Divisibility Properties for Overcubic Partition Triples*, INTEGERS 24 (2024), Article A80, Theorem 1, eqs. (2)-(6).

Stated but not proved: `MetaMathlibExt.overcubicTripleCount_congruences_odd_args` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overcubic-partition-triples/index.html#overcubic-triple-count-congruences-odd-a).

## Overcubic partition triples of $24n+1$ modulo $4$

For $k \ge 1$ let
$f_k = \prod_{j \ge 1} (1 - q^{kj})$, and let $\mathrm{bt}(m)$ be the number of overcubic
partition triples of $m$, the coefficient of $q^m$ in $f_4^3 / (f_1^6 f_2^3)$. For every natural
number $n$, $\mathrm{bt}(24n+1) \equiv 2 c_n \pmod 4$, where $c_n$ is the coefficient of $q^n$
in $f_1$; equivalently, $\sum_{n \ge 0} \mathrm{bt}(24n+1) q^n \equiv 2 f_1 \pmod 4$
coefficientwise.

This is the case $\alpha = 0$ of the paper's statement.

## Sources

- S. Shivaprasada Nayaka, B. N. Dharmendra, and M. C. Mahesh Kumar, *Divisibility Properties for Overcubic Partition Triples*, INTEGERS 24 (2024), Article A80, Theorem 2, eq. (7), case `α = 0`.

Stated but not proved: `MetaMathlibExt.overcubicTripleCount_twentyFour_mul_add_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overcubic-partition-triples/index.html#overcubic-triple-count-twenty-four-mul-a).

## Congruences for overcubic partition triples at arguments congruent to 2 modulo 4

Let
$\mathrm{bt}(n)$ be the number of overcubic partition triples of $n$. For all natural numbers $n$
and $\alpha$, both $\mathrm{bt}(16n+14)$ and $\mathrm{bt}(16n+10)$ are divisible by $16$; each of
$\mathrm{bt}(144n+66)$, $\mathrm{bt}(144n+114)$, $\mathrm{bt}(1296n+594)$, $\mathrm{bt}(1296n+1026)$
and $\mathrm{bt}(16 \cdot 9^{\alpha+3} n + 66 \cdot 9^{\alpha+2})$ is divisible by $8$; and
$\mathrm{bt}(432n+306) \equiv \mathrm{bt}(48n+34) \pmod 8$.

The paper's congruence (16), $\mathrm{bt}(432n+18) \equiv \mathrm{bt}(48n+2) \pmod 8$, is omitted:
it fails at $n = 0$.

## Sources

- S. Shivaprasada Nayaka, B. N. Dharmendra, and M. C. Mahesh Kumar, *Divisibility Properties for Overcubic Partition Triples*, INTEGERS 24 (2024), Article A80, Theorem 4, eqs. (9)-(15) and (17).

Stated but not proved: `MetaMathlibExt.overcubicTripleCount_congruences_two_mod_four_args` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overcubic-partition-triples/index.html#overcubic-triple-count-congruences-two-m).

## Congruences for overcubic partition triples at multiples of 4

Let $\mathrm{bt}(n)$ be the
number of overcubic partition triples of $n$. For all natural numbers $n$ and $\alpha$, both
$\mathrm{bt}(32n+28)$ and $\mathrm{bt}(32n+20)$ are divisible by $16$, and each of
$\mathrm{bt}(64n+56)$, $\mathrm{bt}(576n+408)$, $\mathrm{bt}(5184n+216)$, $\mathrm{bt}(5184n+3672)$
and $\mathrm{bt}(64 \cdot 81^{\alpha+2} n + 216 \cdot 81^{\alpha+1})$ is divisible by $8$.

## Sources

- S. Shivaprasada Nayaka, B. N. Dharmendra, and M. C. Mahesh Kumar, *Divisibility Properties for Overcubic Partition Triples*, INTEGERS 24 (2024), Article A80, Theorem 5, eqs. (18)-(24).

Stated but not proved: `MetaMathlibExt.overcubicTripleCount_congruences_four_mul_args` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overcubic-partition-triples/index.html#overcubic-triple-count-congruences-four).

## Overcubic partition triples of $576n+24$ modulo 8

Let $\mathrm{bt}(n)$ be the number of
overcubic partition triples of $n$, and let $f_1 = \prod_{m \ge 1} (1 - q^m)$. For every natural
number $n$, $\mathrm{bt}(576n+24) \equiv 4 c_n \pmod 8$, where $c_n$ is the coefficient of $q^n$
in $f_1$; that is, $\sum_{n \ge 0} \mathrm{bt}(576n+24) q^n \equiv 4 f_1 \pmod 8$.

This is the $\alpha = 0$ case of the paper's statement.

## Sources

- S. Shivaprasada Nayaka, B. N. Dharmendra, and M. C. Mahesh Kumar, *Divisibility Properties for Overcubic Partition Triples*, INTEGERS 24 (2024), Article A80, Theorem 6, eq. (25), case `α = 0`.

Stated but not proved: `MetaMathlibExt.overcubicTripleCount_fiveHundredSeventySix_mul_add_twentyFour` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overcubic-partition-triples/index.html#overcubic-triple-count-five-hundred-seve).

## Congruences for overcubic partition triples at arguments congruent to 8 modulo 16

Let
$\mathrm{bt}(n)$ be the number of overcubic partition triples of $n$. For all natural numbers $n$
and $\alpha$, each of $\mathrm{bt}(64n+40)$, $\mathrm{bt}(576n+264)$, $\mathrm{bt}(576n+456)$ and
$\mathrm{bt}(64 \cdot 9^{\alpha+2} n + 264 \cdot 9^{\alpha+1})$ is divisible by $8$.

## Sources

- S. Shivaprasada Nayaka, B. N. Dharmendra, and M. C. Mahesh Kumar, *Divisibility Properties for Overcubic Partition Triples*, INTEGERS 24 (2024), Article A80, Theorem 8, eqs. (27)-(30).

Stated but not proved: `MetaMathlibExt.overcubicTripleCount_congruences_eight_mod_sixteen_args` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overcubic-partition-triples/index.html#overcubic-triple-count-congruences-eight).

## Overcubic partition triples of $192n+8$ modulo $4$

For $k \ge 1$ let
$f_k = \prod_{j \ge 1} (1 - q^{kj})$, and let $\mathrm{bt}(m)$ be the number of overcubic
partition triples of $m$, the coefficient of $q^m$ in $f_4^3 / (f_1^6 f_2^3)$. For every natural
number $n$, $\mathrm{bt}(192n+8) \equiv 2 c_n \pmod 4$, where $c_n$ is the coefficient of $q^n$
in $f_1$; equivalently, $\sum_{n \ge 0} \mathrm{bt}(192n+8) q^n \equiv 2 f_1 \pmod 4$
coefficientwise.

This is the case $\alpha = 0$ of the paper's statement.

## Sources

- S. Shivaprasada Nayaka, B. N. Dharmendra, and M. C. Mahesh Kumar, *Divisibility Properties for Overcubic Partition Triples*, INTEGERS 24 (2024), Article A80, Theorem 9, eq. (31), case `α = 0`.

Stated but not proved: `MetaMathlibExt.overcubicTripleCount_oneHundredNinetyTwo_mul_add_eight` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overcubic-partition-triples/index.html#overcubic-triple-count-one-hundred-ninet).

## Congruences for overcubic partition triples at multiples of 16

Let $\mathrm{bt}(n)$ be the
number of overcubic partition triples of $n$. For all natural numbers $n$ and $\alpha$, each of
$\mathrm{bt}(64n+48)$, $\mathrm{bt}(128n+80)$, $\mathrm{bt}(128n+96)$, $\mathrm{bt}(256n+160)$ and
$\mathrm{bt}(256 \cdot 2^{\alpha} n + 192)$ is divisible by $4$, and
$\mathrm{bt}(256n+32) \equiv \mathrm{bt}(128n+16) \pmod 4$.

## Sources

- S. Shivaprasada Nayaka, B. N. Dharmendra, and M. C. Mahesh Kumar, *Divisibility Properties for Overcubic Partition Triples*, INTEGERS 24 (2024), Article A80, Theorem 11, eqs. (33)-(38).

Stated but not proved: `MetaMathlibExt.overcubicTripleCount_congruences_sixteen_mul_args` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OvercubicPartitionTriplesWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overcubic-partition-triples/index.html#overcubic-triple-count-congruences-sixte).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Overcubic partition triples](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overcubic-partition-triples/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overcubic-partition-triples)
