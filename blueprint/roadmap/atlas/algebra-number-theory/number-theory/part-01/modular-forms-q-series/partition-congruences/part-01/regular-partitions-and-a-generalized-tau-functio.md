---
declaration: section
origin: cited
lean: MetaMathlibExt.constantCoeff_pentagonalSeries_int, MetaMathlibExt.isUnit_pentagonalSeries_int, MetaMathlibExt.generalizedTau, MetaMathlibExt.generalizedTau_zero, MetaMathlibExt.generalizedTau_one, MetaMathlibExt.generalizedTau_natCast, MetaMathlibExt.generalizedTau_succ_eq_partition_sum, MetaMathlibExt.generalizedTau_succ_modEq_card_frequency_two
statement: formalized
---

# Regular partitions and a generalized tau function

40 results, 6 proved and 34 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html).

## Euler's product has constant term $1$

The constant coefficient of the integer power
series $\prod_{m \ge 1} (1 - X^m)$ in $\mathbb{Z}[[X]]$ is $1$.

## Sources

- Euler's pentagonal number theorem as used in Sriram and Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, identity (1).

Formalized by `MetaMathlibExt.constantCoeff_pentagonalSeries_int`, a theorem declared in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#constant-coeff-pentagonal-series-int).

## Euler's product is a unit in $\mathbb{Z}((X))$

Euler's pentagonal series
$\sum_{k \in \mathbb{Z}} (-1)^k X^{k(3k - 1)/2}$, which equals $\prod_{m \ge 1} (1 - X^m)$, is a
unit of the ring $\mathbb{Z}[[X]]$ of formal power series with integer coefficients, so all its
integer powers are defined.

## Sources

- Sriram and Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Definition 1.1 (negative exponents).

Formalized by `MetaMathlibExt.isUnit_pentagonalSeries_int`, a theorem declared in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#is-unit-pentagonal-series-int).

## Generalized tau function

For an integer $k$ and a natural number $n$, the generalized tau
function $\tau_k(n)$ is the coefficient of $q^n$ in the integer power series
$q \prod_{m \ge 1} (1 - q^m)^k$. For negative $k$ the power is taken in the group of units of
$\mathbb{Z}[[q]]$, where $\prod_{m \ge 1} (1 - q^m)$ is invertible because its constant term is $1$.

The paper requires $k \ne 0$; $k = 0$ gives $\tau_0(1) = 1$ and $\tau_0(n) = 0$ for $n \ne 1$.
$\tau_{24}$ is Ramanujan's tau function, and $\tau_1(n + 1)$ is Euler's $\omega(n)$, the
coefficient of $q^n$ in $\prod_{m \ge 1} (1 - q^m)$.

## Sources

- Sriram and Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Definition 1.1, equation (2).

Formalized by `MetaMathlibExt.generalizedTau`, a definition declared in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#generalized-tau).

## Generalized tau function at zero

For every integer $k$, $\tau_k(0) = 0$, where $\tau_k$
is the generalized tau function: the series $q \prod_{m \ge 1} (1 - q^m)^k$ has no constant term.

## Sources

- Sriram and Christopher, INTEGERS 24 (2024), Article A39, Definition 1.1.

Formalized by `MetaMathlibExt.generalizedTau_zero`, a theorem declared in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#generalized-tau-zero).

## The generalized tau function at $1$

For every integer $k$, $\tau_k(1) = 1$.

## Sources

- Sriram and Christopher, INTEGERS 24 (2024), Article A39, Definition 1.1.

Formalized by `MetaMathlibExt.generalizedTau_one`, a theorem declared in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#generalized-tau-one).

## The generalized tau function for natural exponents

For natural numbers $k$ and $n$,
$\tau_k(n)$ is the coefficient of $q^n$ in the integer power series
$q \bigl(\prod_{m \ge 1} (1 - q^m)\bigr)^k$.

## Sources

- Sriram and Christopher, INTEGERS 24 (2024), Article A39, Definition 1.1.

Formalized by `MetaMathlibExt.generalizedTau_natCast`, a theorem declared in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#generalized-tau-nat-cast).

## Partition formulas for the generalized tau function

Let $k \ge 1$ and $n \ge 0$ be natural
numbers. For a partition $\lambda$ of $n$ and a part $a$ of $\lambda$, write $f_a$ for the number
of times $a$ occurs in $\lambda$. Then

$$\tau_k(n + 1) = \sum_{\lambda} \prod_{a} (-1)^{f_a} \binom{k}{f_a},$$

where $\lambda$ runs over the partitions of $n$ with $f_a \le k$ for every part $a$ and the
product runs over the distinct parts $a$ of $\lambda$, and

$$\tau_{-k}(n + 1) = \sum_{\lambda} \prod_{a} \binom{f_a + k - 1}{k - 1},$$

where $\lambda$ runs over all partitions of $n$ and the product again runs over the distinct parts
$a$ of $\lambda$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Theorem 1.

Stated but not proved: `MetaMathlibExt.generalizedTau_succ_eq_partition_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#generalized-tau-succ-eq-partition-sum).

## Parity of the generalized tau function via part frequencies

Let $k \ge 1$ and $n \ge 0$ be
natural numbers, and let $A$ be the set of integers $a$ with $1 \le a \le k$ and $\binom{k}{a}$
odd. Then $\tau_k(n + 1)$ is congruent modulo $2$ to the number of partitions of $n$ in which the
number of times each part occurs lies in $A$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Theorem 2.

Stated but not proved: `MetaMathlibExt.generalizedTau_succ_modEq_card_frequency_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#generalized-tau-succ-mod-eq-card-frequen).

## Parity of the $4$-regular partition function

For a positive integer $n$, let $R_4(n)$ be
the number of partitions of $n$ with no part divisible by $4$. Then $R_4(n)$ is odd if and only if
$n$ is a triangular number, that is, $n = m(m + 1)/2$ for some integer $m \ge 0$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Theorem 3.

Stated but not proved: `MetaMathlibExt.odd_card_four_regular_iff_triangular` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#odd-card-four-regular-iff-triangular).

## Parity of $\tau_{14}$ and $\tau_6$ at odd arguments

Let $\tau_k(m)$ be the generalized
tau function, the coefficient of $q^m$ in $q \prod_{j \ge 1} (1 - q^j)^k$, and let $R_8(n)$ be
the number of partitions of $n$ in which no part is divisible by $8$. For every positive integer
$n$: (a) $\tau_{14}(2n + 1) \equiv R_8(n) \pmod 2$; (b) $\tau_6(2n + 1)$ is odd if and only if
$n$ is a triangular number, that is, $n = m(m + 1)/2$ for some natural number $m$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Theorem 4.

Stated but not proved: `MetaMathlibExt.generalizedTau_fourteen_six_odd_index_mod_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#generalized-tau-fourteen-six-odd-index-m).

## $2^s$-regular partitions and the generalized tau function modulo 2

Let $s$ be a positive
integer and $n$ a natural number. Let $R_{2^s}(n)$ be the number of partitions of $n$ in which no
part is divisible by $2^s$, and let $\tau_k(m)$ be the generalized tau function, the coefficient
of $q^m$ in $q \prod_{j \ge 1} (1 - q^j)^k$. Then $R_{2^s}(n) \equiv \tau_{2^s - 1}(n + 1) \pmod 2$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Theorem 5.

Stated but not proved: `MetaMathlibExt.card_two_pow_regular_modEq_generalizedTau` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#card-two-pow-regular-mod-eq-generalized).

## Ramanujan's $\tau$ modulo $3$ via $9$-regular partitions

Let $\tau = \tau_{24}$ be
Ramanujan's tau function, where $\tau_k$ is the generalized tau function, and let $R_9(m)$ be
the number of partitions of $m$ with no part divisible by $9$. For every integer $n \ge 1$,
$\tau(n + 1) \equiv R_9(n/3) \pmod 3$ if $3$ divides $n$, and $\tau(n + 1) \equiv 0 \pmod 3$
otherwise.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Theorem 6.

Stated but not proved: `MetaMathlibExt.ramanujanTau_succ_modEq_nine_regular` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#ramanujan-tau-succ-mod-eq-nine-regular).

## Ramanujan's congruence $\tau(3n) \equiv 0 \pmod 3$

Let $\tau = \tau_{24}$ be Ramanujan's
tau function, where $\tau_k$ is the generalized tau function. For every integer $n \ge 1$,
$\tau(3n) \equiv 0 \pmod 3$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Corollary 1.

Stated but not proved: `MetaMathlibExt.ramanujanTau_three_mul_modEq_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#ramanujan-tau-three-mul-mod-eq-zero).

## 9-regular partitions modulo 3 and the divisor sum

Let $R_9(m)$ denote the number of
partitions of $m$ in which no part is divisible by $9$, and let $\sigma(m)$ be the sum of the
positive divisors of $m$. For every positive integer $n$, $R_9(n) \equiv \sigma(3n + 1) \pmod 3$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Corollary 2.

Stated but not proved: `MetaMathlibExt.card_nine_regular_modEq_sigma` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#card-nine-regular-mod-eq-sigma).

## Ramanujan's $\tau$ modulo $5$ via $25$-regular partitions

Let $\tau = \tau_{24}$ be
Ramanujan's tau function, where $\tau_k$ is the generalized tau function, and let $R_{25}(n)$ be
the number of partitions of $n$ with no part divisible by $25$. For every integer $n \ge 1$,
$\tau(n + 1) \equiv R_{25}(n) \pmod 5$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Theorem 7.

Stated but not proved: `MetaMathlibExt.ramanujanTau_succ_modEq_twentyfive_regular` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#ramanujan-tau-succ-mod-eq-twentyfive-reg).

## 25-regular partitions modulo 5 and the divisor sum

Let $R_{25}(m)$ denote the number of
partitions of $m$ in which no part is divisible by $25$, and let $\sigma(m)$ be the sum of the
positive divisors of $m$. For every positive integer $n$,
$R_{25}(n) \equiv (n + 1) \, \sigma(n + 1) \pmod 5$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Corollary 3.

Stated but not proved: `MetaMathlibExt.card_twentyfive_regular_modEq_mul_sigma` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#card-twentyfive-regular-mod-eq-mul-sigma).

## Ramanujan's $\tau$ modulo $7$ via triangular numbers

Let $\tau = \tau_{24}$ be Ramanujan's
tau function, where $\tau_k$ is the generalized tau function. For every integer $n \ge 1$,
$\tau(n + 1)$ is congruent modulo $7$ to the sum of $(-1)^{m + r} (2m + 1)(2r + 1)$ over all
pairs of integers $m, r \ge 0$ with $m(m + 1)/2 + 7r(r + 1)/2 = n$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Theorem 8.

Stated but not proved: `MetaMathlibExt.ramanujanTau_succ_modEq_triangular_sum_seven` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#ramanujan-tau-succ-mod-eq-triangular-sum).

## Ramanujan's $\tau$ modulo $11$ via pentagonal numbers

Let $\tau = \tau_{24}$ be Ramanujan's
tau function, where $\tau_k$ is the generalized tau function, and let $P(r) = r(3r - 1)/2$ for
integers $r$. For every integer $n \ge 1$, $\tau(n + 1)$ is congruent modulo $11$ to the sum of
$(-1)^{l + m + s + r}$ over all quadruples of integers $(l, m, s, r)$ with
$P(l) + P(m) + 11P(s) + 11P(r) = n$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Theorem 9.

Stated but not proved: `MetaMathlibExt.ramanujanTau_succ_modEq_pentagonal_sum_eleven` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#ramanujan-tau-succ-mod-eq-pentagonal-sum).

## Ramanujan's $\tau$ modulo $13$ via $\tau_{11}$

Let $\tau = \tau_{24}$ be Ramanujan's tau
function, where $\tau_k$ is the generalized tau function, and let $P(r) = r(3r - 1)/2$ for
integers $r$. For every integer $n \ge 1$,

$$\tau(n + 1) \equiv \sum_{13P(r) \le n} (-1)^r \tau_{11}(n - 13P(r) + 1) \pmod{13},$$

the sum running over all integers $r$ with $13P(r) \le n$.

The source record prints $\tau_{11}(s)$ in place of $\tau_{11}(s + 1)$, where $n = 13P(r) + s$;
that version is false at $n = 1$. The shifted index comes from the identity
$\prod_{m \ge 1} (1 - q^m)^{11} (1 - q^{13m}) = \sum_{r, s} (-1)^r \tau_{11}(s + 1) q^{13P(r) + s}$,
which follows from Definition 1.1 and is used in the proof.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Theorem 10.

Stated but not proved: `MetaMathlibExt.ramanujanTau_succ_modEq_pentagonal_tau_eleven` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#ramanujan-tau-succ-mod-eq-pentagonal-tau).

## Ramanujan's $\tau$ modulo $17$ via $\tau_7$

Let $\tau = \tau_{24}$ be Ramanujan's tau
function, where $\tau_k$ is the generalized tau function, and let $P(r) = r(3r - 1)/2$ for
integers $r$. For every integer $n \ge 1$,

$$\tau(n + 1) \equiv \sum_{17P(r) \le n} (-1)^r \tau_7(n - 17P(r) + 1) \pmod{17},$$

the sum running over all integers $r$ with $17P(r) \le n$.

The source record prints $\tau_7(s)$ in place of $\tau_7(s + 1)$, where $n = 17P(r) + s$;
that version is false at $n = 1$. The shifted index comes from the identity
$\prod_{m \ge 1} (1 - q^m)^7 (1 - q^{17m}) = \sum_{r, s} (-1)^r \tau_7(s + 1) q^{17P(r) + s}$,
which follows from Definition 1.1 and is used in the proof.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Theorem 11.

Stated but not proved: `MetaMathlibExt.ramanujanTau_succ_modEq_pentagonal_tau_seven` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#ramanujan-tau-succ-mod-eq-pentagonal-tau-2).

## Ramanujan's $\tau$ modulo $19$ via $\tau_5$

Let $\tau = \tau_{24}$ be Ramanujan's tau
function, where $\tau_k$ is the generalized tau function, and let $P(r) = r(3r - 1)/2$ for
integers $r$. For every integer $n \ge 1$,

$$\tau(n + 1) \equiv \sum_{19P(r) \le n} (-1)^r \tau_5(n - 19P(r) + 1) \pmod{19},$$

the sum running over all integers $r$ with $19P(r) \le n$.

The source record prints $\tau_5(s)$ in place of $\tau_5(s + 1)$, where $n = 19P(r) + s$;
that version is false at $n = 1$. The shifted index comes from the identity
$\prod_{m \ge 1} (1 - q^m)^5 (1 - q^{19m}) = \sum_{r, s} (-1)^r \tau_5(s + 1) q^{19P(r) + s}$,
which follows from Definition 1.1 and is used in the proof.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Theorem 12.

Stated but not proved: `MetaMathlibExt.ramanujanTau_succ_modEq_pentagonal_tau_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#ramanujan-tau-succ-mod-eq-pentagonal-tau-3).

## Ramanujan's $\tau$ modulo $23$ via pentagonal numbers

Let $\tau = \tau_{24}$ be
Ramanujan's tau function, where $\tau_k$ is the generalized tau function, and let
$P(r) = r(3r - 1)/2$ for integers $r$. For every integer $n \ge 1$, $\tau(n + 1)$ is congruent
modulo $23$ to the sum of $(-1)^{r + s}$ over all pairs of integers $(r, s)$ with
$P(r) + 23P(s) = n$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Theorem 13.

Stated but not proved: `MetaMathlibExt.ramanujanTau_succ_modEq_pentagonal_sum_twentythree` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#ramanujan-tau-succ-mod-eq-pentagonal-sum-2).

## Ramanujan's $\tau$ modulo $25$ via $5$-regular partitions

Let $\tau = \tau_{24}$ be
Ramanujan's tau function, where $\tau_k$ is the generalized tau function. Let $R_5(m)$ be the
number of partitions of $m$ with no part divisible by $5$, and let $P(t) = t(3t - 1)/2$ for
integers $t$. For every integer $n \ge 1$,

$$\tau(n + 1) \equiv \sum (-1)^{s + t} (2s + 1) R_5\big(n - 5s(s + 1)/2 - 5P(t)\big) \pmod{25},$$

the sum running over all integers $s \ge 0$ and $t$ with $5s(s + 1)/2 + 5P(t) \le n$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Theorem 14.

Stated but not proved: `MetaMathlibExt.ramanujanTau_succ_modEq_five_regular_sum_twentyfive` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#ramanujan-tau-succ-mod-eq-five-regular-s).

## Generalized tau at a prime power modulo the prime

Let $p$ be a prime, let $s \ge 1$ and
$n \ge 0$ be natural numbers, and for an integer $t$ let $P(t) = t(3t - 1)/2$ be the generalized
pentagonal number. Then $\tau_{p^s}(n + 1)$ is congruent modulo $p$ to the sum of $(-1)^t$ over
the integers $t$ with $-n \le t \le n$ and $n = p^s P(t)$.

Since $P$ is injective, this sum has at most one term: $\tau_{p^s}(n + 1) \equiv (-1)^t \pmod{p}$
if $n = p^s P(t)$, and $\tau_{p^s}(n + 1) \equiv 0 \pmod{p}$ if $n$ is not of this form.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Theorem 15.

Stated but not proved: `MetaMathlibExt.generalizedTau_prime_pow_succ_modEq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#generalized-tau-prime-pow-succ-mod-eq).

## Generalized tau function $\tau_{2p}$ modulo $p$

Let $p$ be an odd prime, let $\tau_k$ be
the generalized tau function, and for an integer $r$ let $P(r) = r(3r - 1)/2$ be the generalized
pentagonal number. For every integer $n \ge 0$,

$$\tau_{2p}(n + 1) \equiv \sum (-1)^{r + s} \pmod p,$$

the sum running over the pairs of integers $r, s$ with $|r| \le n$, $|s| \le n$ and
$n = p\,(P(r) + P(s))$.

The paper prints the side condition as $n + 1 = p(P(r) + P(s))$, which is false: at $n = 0$ the
left side is $\tau_{2p}(1) = 1$ while that sum is empty. The identity
$\sum_{n \ge 0} \tau_{2p}(n + 1) q^n \equiv \prod_{m \ge 1} (1 - q^{pm})^2 \pmod p$ from the
paper's proof gives $n = p(P(r) + P(s))$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Theorem 16.

Stated but not proved: `MetaMathlibExt.generalizedTau_two_mul_prime_succ_modEq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#generalized-tau-two-mul-prime-succ-mod-e).

## $\tau_{2p}(n + 1)$ vanishes modulo $p$ when $p \nmid n$

Let $p$ be an odd prime and $n$ a
natural number not divisible by $p$. Then $\tau_{2p}(n + 1) \equiv 0 \pmod{p}$.

The record prints the hypothesis as $p \nmid n + 1$; that is false, and the corollary follows from
Theorem 3.26 (the record's Theorem 16) in its corrected form, which forces $p \mid n$ for a nonzero
residue.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Corollary 4.

Stated but not proved: `MetaMathlibExt.generalizedTau_two_mul_prime_succ_modEq_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#generalized-tau-two-mul-prime-succ-mod-e-2).

## Generalized tau at $2p + 1$ modulo $p$

Let $p$ be an odd prime and $n$ a natural number,
and for an integer $j$ let $P(j) = j(3j - 1)/2$ be the generalized pentagonal number. Then
$\tau_{2p + 1}(n + 1)$ is congruent modulo $p$ to the sum of $(-1)^{r + s + t}$ over the triples
of integers $(r, s, t)$ with $-n \le r, s, t \le n$ and $n = P(r) + p(P(s) + P(t))$.

The record prints the condition as $n + 1 = P(r) + p(P(s) + P(t))$; that is false, and the
proof's identity $\sum \tau_{2p+1}(n + 1) q^n \equiv \prod (1 - q^m)(1 - q^{pm})^2 \pmod{p}$
gives the index $n$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Theorem 17.

Stated but not proved: `MetaMathlibExt.generalizedTau_two_mul_prime_add_one_succ_modEq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#generalized-tau-two-mul-prime-add-one-su).

## Generalized tau at $p^2 + 1$ modulo $p$

Let $p$ be an odd prime and $n$ a natural number,
and for an integer $j$ let $P(j) = j(3j - 1)/2$ be the generalized pentagonal number. Then
$\tau_{p^2 + 1}(n + 1)$ is congruent modulo $p$ to the sum of $(-1)^{r + s}$ over the pairs of
integers $(r, s)$ with $-n \le r, s \le n$ and $n = P(r) + p^2 P(s)$.

The record prints the condition as $n + 1 = P(r) + p^2 P(s)$; that is false, and the proof's
identity $\sum \tau_{p^2+1}(n + 1) q^n \equiv \prod (1 - q^m)(1 - q^{p^2 m}) \pmod{p}$ gives the
index $n$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Theorem 18.

Stated but not proved: `MetaMathlibExt.generalizedTau_prime_sq_add_one_succ_modEq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#generalized-tau-prime-sq-add-one-succ-mo).

## A congruence for 9-regular partitions at $4n + 1$

Let $R_9(m)$ denote the number of
partitions of $m$ in which no part is divisible by $9$. For every positive integer $n$,
$R_9(4n + 1) \equiv R_9(n) \pmod 3$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Theorem 19.

Stated but not proved: `MetaMathlibExt.card_nine_regular_four_mul_add_one_modEq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#card-nine-regular-four-mul-add-one-mod-e).

## Iterated congruences for 9-regular partitions modulo 3

Let $R_9(m)$ denote the number of
partitions of $m$ in which no part is divisible by $9$, and let $N_s = (4^s - 1)/3$. For all
positive integers $r$ and $s$, $R_9((r - 1) 4^{s-1} + N_s) \equiv R_9(r) \pmod 3$,
$R_9(N_s) \equiv 1 \pmod 3$, $R_9(4^{s-1} + N_s) \equiv 2 \pmod 3$ and
$R_9(2 \cdot 4^{s-1} + N_s) \equiv 0 \pmod 3$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Corollary 5.

Stated but not proved: `MetaMathlibExt.card_nine_regular_iterate_modEq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#card-nine-regular-iterate-mod-eq).

## Prime-regular partitions and the generalized tau function

Let $p$ be a prime and $n$ a
natural number. Let $R_p(n)$ be the number of partitions of $n$ in which no part is divisible by
$p$, and let $\tau_k(m)$ be the generalized tau function, the coefficient of $q^m$ in
$q \prod_{j \ge 1} (1 - q^j)^k$. Then $R_p(n) \equiv \tau_{p-1}(n + 1) \pmod p$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Theorem 20.

Stated but not proved: `MetaMathlibExt.card_prime_regular_modEq_generalizedTau_pred` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#card-prime-regular-mod-eq-generalized-ta).

## Binomial coefficients $\binom{n+k}{k}$ modulo an odd prime

Let $l$ be an odd prime, $k$
an integer with $1 \le k < l$, $n$ a natural number, and $r$ the remainder of $n$ modulo $l$. If
$r \le l - k - 1$, then $\binom{n+k}{k} \equiv (-1)^r \binom{l-k-1}{r} \pmod l$; otherwise
$\binom{n+k}{k} \equiv 0 \pmod l$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Lemma 1.

Stated but not proved: `MetaMathlibExt.choose_add_modEq_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#choose-add-mod-eq-prime).

## $\tau_{-k}$ and partition convolutions modulo a prime

Let $l$ be an odd prime, let $k$ be a
natural number with $2 \le k < l$, let $n$ be a natural number, and write $p(s)$ for the number of
partitions of $s$. Then

$$\tau_{-k}(n + 1) \equiv \sum_{s=0}^{\lfloor n/l \rfloor} \tau_{l-k}(n - ls + 1)\, p(s) \pmod{l},$$

and the composition sum $\sum p(a_1) p(a_2) \cdots p(a_k)$, taken over all $k$-tuples
$(a_1, \dots, a_k)$ of natural numbers with $a_1 + \cdots + a_k = n$, is congruent modulo $l$ to
the same right-hand side.

The record prints $\tau_{l-k}(t)$ in place of $\tau_{l-k}(t + 1)$, writing $n = t + ls$; that is
false. The proof's identity
$\prod (1 - q^m)^{-k} \equiv \prod (1 - q^m)^{l-k} (1 - q^{lm})^{-1} \pmod{l}$ together with
Definition 1.1 ($\prod (1 - q^m)^j = \sum \tau_j(t + 1) q^t$) gives $\tau_{l-k}(t + 1)$;
Corollary 4.3 (the record's Corollary 6) uses this shifted form, $\omega(t) = \tau_1(t + 1)$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Theorem 21.

Stated but not proved: `MetaMathlibExt.generalizedTau_neg_succ_modEq_partition_convolution` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#generalized-tau-neg-succ-mod-eq-partitio).

## Partition convolution modulo $3$

Let $p(a)$ be the number of partitions of $a$, and let
$\omega(t)$ be the coefficient of $q^t$ in Euler's product $\prod_{m \ge 1} (1 - q^m)$. For every
integer $n \ge 0$,

$$\sum_{a + b = n} p(a)\, p(b) \equiv \sum_{0 \le s \le n/3} \omega(n - 3s)\, p(s) \pmod 3,$$

the left sum running over pairs $(a, b)$ of nonnegative integers and the right one over integers
$s$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Corollary 6.

Stated but not proved: `MetaMathlibExt.partition_convolution_two_modEq_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#partition-convolution-two-mod-eq-three).

## Partition composition sums vanishing modulo a prime

Let $p(a)$ be the number of
partitions of $a$. Let $\ell \ge 5$ be a prime and $m \ge 0$ an integer such that
$m \not\equiv 0 \pmod{\ell}$ and $m \not\equiv (-1)^r \binom{\ell - 3}{r} \pmod{\ell}$ for every
integer $r$ with $0 \le r \le (\ell - 3)/2$. Then every integer $n \ge 0$ with
$n \equiv m \pmod{\ell}$ satisfies

$$\sum_{a_1 + \cdots + a_{\ell - 3} = n} p(a_1) \cdots p(a_{\ell - 3}) \equiv 0 \pmod{\ell},$$

the sum running over all $(\ell - 3)$-tuples $(a_1, \dots, a_{\ell - 3})$ of nonnegative integers
with sum $n$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Corollary 7.

Stated but not proved: `MetaMathlibExt.partition_composition_sum_modEq_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#partition-composition-sum-mod-eq-zero).

## Ramanujan's congruence modulo $7$

Let $\tau(n) = \tau_{24}(n)$ be Ramanujan's tau
function, the generalized tau function with $k = 24$. For every positive integer $n$,
$\tau(7n) \equiv 0 \pmod 7$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Corollary 8.

Stated but not proved: `MetaMathlibExt.ramanujanTau_seven_mul_modEq_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#ramanujan-tau-seven-mul-mod-eq-zero).

## Vanishing of $\tau_k(n)$ modulo the prime $k - 1$

Let $n \ge 1$ and let $k$ be a natural
number such that $k - 1$ is prime. For an integer $t$ let $P(t) = t(3t - 1)/2$ be the generalized
pentagonal number. If $k - 1$ does not divide $n - 1 - P(t)$ for any integer $t$ with
$P(t) \le n - 1$, then the generalized tau function satisfies $\tau_k(n) \equiv 0 \pmod{k - 1}$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Proposition 1.

Stated but not proved: `MetaMathlibExt.generalizedTau_modEq_zero_of_pentagonal` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#generalized-tau-mod-eq-zero-of-pentagona).

## Divisibility of $n\,\tau_k(n + 1)$ by $|k|$

Let $\tau_k$ be the generalized tau function.
For every positive integer $n$ and every integer $k$ with $|k| \ge 2$,
$n\,\tau_k(n + 1) \equiv 0 \pmod{|k|}$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Proposition 2.

Stated but not proved: `MetaMathlibExt.mul_generalizedTau_succ_modEq_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 417](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#mul-generalized-tau-succ-mod-eq-zero).

## Vanishing of the generalized tau function modulo $|k|/d$

Let $\tau_k(n)$ be the
generalized tau function, the coefficient of $q^n$ in $q \prod_{j \ge 1} (1 - q^j)^k$. Let $k$ be
an integer with $|k| \ge 2$ and $d$ a natural number dividing $|k|$ with $d < |k|$. Then for all
natural numbers $m$ and $r$ with $\gcd(r, |k|/d) = 1$,
$\tau_k(|k| m + d r + 1) \equiv 0 \pmod{|k|/d}$.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Proposition 3.

Stated but not proved: `MetaMathlibExt.generalizedTau_modEq_zero_of_coprime` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#generalized-tau-mod-eq-zero-of-coprime).

## Ramanujan's tau function modulo divisors of $24$

Let $\tau(n) = \tau_{24}(n)$ be
Ramanujan's tau function, the generalized tau function with $k = 24$. For every integer
$m \ge 0$: $\tau(24m + r + 1) \equiv 0 \pmod{24}$ for $r \in \{1, 5, 7, 11, 13, 17, 19, 23\}$;
$\tau(24m + r + 1) \equiv 0 \pmod 6$ for $r \in \{4, 20\}$;
$\tau(24m + r + 1) \equiv 0 \pmod 8$ for $r \in \{3, 6, 9, 15\}$;
$\tau(24m + r + 1) \equiv 0 \pmod 3$ for $r \in \{8, 16\}$; and
$\tau(24m + 13) \equiv 0 \pmod 2$.

The paper prints the moduli of the second, fourth and fifth congruences as $12$, $6$ and $4$,
which is false (for instance $\tau(5) = 4830$ is not divisible by $12$); the moduli used are
$24/\gcd(r, 24)$, which the paper's Proposition 2.4 at $k = 24$ gives. The first and third
congruences are as printed.

## Sources

- S. Sriram and A. David Christopher, *Congruences Relating Regular Partition Functions, a Generalized Tau Function, and Partition Function Weighted Composition Sums*, INTEGERS 24 (2024), Article A39, Proposition 4.

Stated but not proved: `MetaMathlibExt.ramanujanTau_modEq_divisors_twentyfour` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean, line 435](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedTauRegularPartitionWanted.lean#L435). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html#ramanujan-tau-mod-eq-divisors-twentyfour).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Regular partitions and a generalized tau function](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-partitions-and-a-generalized-tau-functio)
