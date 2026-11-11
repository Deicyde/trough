---
declaration: section
origin: cited
lean: MetaMathlibExt.oddDesignatedSummandsSeries, MetaMathlibExt.oddDesignatedSummandsCount, MetaMathlibExt.oddDesignatedSummandsCount_generatingFunction, MetaMathlibExt.oddDesignatedSummandsCount_zero, MetaMathlibExt.f1_mul_f3_two_dissection, MetaMathlibExt.oddDesignatedSummandsCount_two_pow_mul_four_mul_add_three, MetaMathlibExt.oddDesignatedSummandsCount_two_pow_mul_eight_mul_add_seven, MetaMathlibExt.oddDesignatedSummandsCount_two_dissection
statement: formalized
---

# Partitions with designated summands

23 results, 4 proved and 19 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html).

## Generating function of odd designated-summand partitions

For $k \ge 1$ let
$f_k = \prod_{m \ge 1} (1 - q^{km})$ be the Euler product. This is the integer power series
$f_4 f_6^2 / (f_1 f_3 f_{12})$ in $q$, where the denominator $f_1 f_3 f_{12}$ is invertible
because its constant coefficient is $1$. It is the generating function
$\sum_{n \ge 0} \mathrm{PD}_2(n) q^n$ of the numbers $\mathrm{PD}_2(n)$ of partitions of $n$ with
designated summands into odd parts.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Section 2, eq. (1) (quoting G. E. Andrews, R. P. Lewis, and J. Lovejoy, *Partitions with designated summands*, Acta Arith. 105 (2002)).

Formalized by `MetaMathlibExt.oddDesignatedSummandsSeries`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-series).

## The odd designated-summand partition function

For a natural number $n$, the integer
$\mathrm{PD}_2(n)$ is defined as the coefficient of $q^n$ in the integer power series
$f_4 f_6^2 / (f_1 f_3 f_{12})$, where $f_k = \prod_{m \ge 1} (1 - q^{km})$ is the Euler product
(the denominator has constant coefficient $1$, so it is invertible). It counts the partitions of
$n$ with designated summands in which all parts are odd.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Sections 1-2, eq. (1).

Formalized by `MetaMathlibExt.oddDesignatedSummandsCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-count).

## Generating function for partitions with designated summands into odd parts

Let
$f_k = \prod_{m \ge 1} (1 - q^{km})$ in the ring of integer power series in $q$, and let $PD_2(n)$
be the number of partitions of $n$ with designated summands in which every part is odd, defined as
the coefficient of $q^n$ in $f_4 f_6^2 / (f_1 f_3 f_{12})$. Then
$f_1 f_3 f_{12} \sum_{n \ge 0} PD_2(n) q^n = f_4 f_6^2$.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Section 2, eq. (1).

Formalized by `MetaMathlibExt.oddDesignatedSummandsCount_generatingFunction`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-count-generating).

## Odd designated-summand partitions of zero

The odd designated-summand partition function
satisfies $\mathrm{PD}_2(0) = 1$.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Section 2, eq. (1).

Formalized by `MetaMathlibExt.oddDesignatedSummandsCount_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-count-zero).

## The 2-dissection of $f_1 f_3$

Let $f_k = \prod_{m \ge 1} (1 - q^{km})$ denote the Euler
products in the ring of integer power series in $q$. Then

$$f_1 f_2 f_3 f_4^2 f_6 f_8^2 f_{12}^2 f_{24}^2 = f_2^2 f_8^4 f_{12}^6 - q f_4^6 f_6^2 f_{24}^4.$$

Since every $f_k$ with $k \ge 1$ has constant term $1$ and so is invertible, this is Hirschhorn's
identity $f_1 f_3 = \frac{f_2 f_8^2 f_{12}^4}{f_4^2 f_6 f_{24}^2} -
q \frac{f_4^4 f_6 f_{24}^2}{f_2 f_8^2 f_{12}^2}$ (*The Power of q*, eq. (30.12.1)) multiplied
through by $f_2 f_4^2 f_6 f_8^2 f_{12}^2 f_{24}^2$.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Lemma 3.

Stated but not proved: `MetaMathlibExt.f1_mul_f3_two_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#f1-mul-f3-two-dissection).

## $\mathrm{PD}_2(2^\alpha (4n + 3))$ is divisible by 4

Write $\mathrm{PD}_2(m)$ for the
number of partitions of $m$ with designated summands in which every part is odd. For all natural
numbers $\alpha$ and $n$, $\mathrm{PD}_2(2^\alpha (4n + 3)) \equiv 0 \pmod 4$.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Theorem 1.

Stated but not proved: `MetaMathlibExt.oddDesignatedSummandsCount_two_pow_mul_four_mul_add_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-count-two-pow-mu).

## $\mathrm{PD}_2(2^\alpha (8n + 7))$ is divisible by 8

Write $\mathrm{PD}_2(m)$ for the
number of partitions of $m$ with designated summands in which every part is odd. For all natural
numbers $\alpha$ and $n$, $\mathrm{PD}_2(2^\alpha (8n + 7)) \equiv 0 \pmod 8$.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Theorem 2.

Stated but not proved: `MetaMathlibExt.oddDesignatedSummandsCount_two_pow_mul_eight_mul_add_seven` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-count-two-pow-mu-2).

## The 2-dissection of the generating function of $\mathrm{PD}_2$

Write $\mathrm{PD}_2(m)$ for
the number of partitions of $m$ with designated summands in which every part is odd, and write
$f_k = \prod_{j \ge 1} (1 - q^{kj})$ for the Euler product. In the ring of integer power series in
$q$, $f_1^2 f_3^2 f_{12}^2 \sum_{n \ge 0} \mathrm{PD}_2(2n) q^n = f_4^2 f_6^4$ and
$f_1^4 f_4^2 f_6^2 \sum_{n \ge 0} \mathrm{PD}_2(2n + 1) q^n = f_2^6 f_{12}^2$.

These are $\sum_{n} \mathrm{PD}_2(2n) q^n = f_4^2 f_6^4 / (f_1^2 f_3^2 f_{12}^2)$ and
$\sum_{n} \mathrm{PD}_2(2n + 1) q^n = f_2^6 f_{12}^2 / (f_1^4 f_4^2 f_6^2)$ with denominators
cleared.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Theorem 3.

Stated but not proved: `MetaMathlibExt.oddDesignatedSummandsCount_two_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-count-two-dissec).

## The 4-dissection of the generating function of $PD_2$

Let
$f_k = \prod_{m \ge 1} (1 - q^{km})$ in the ring of integer power series in $q$, and let $PD_2(n)$
be the number of partitions of $n$ with designated summands in which every part is odd. Then
$f_1^8 f_3^4 f_4^4 f_6^4 f_{12}^4 \sum_{n \ge 0} PD_2(4n) q^n =
f_1^4 f_4^8 f_6^{12} + q f_2^{12} f_3^4 f_{12}^8$,
$f_1^8 f_3^2 f_4^4 \sum_{n \ge 0} PD_2(4n + 1) q^n = f_2^{12} f_6^2$,
$f_1^6 f_3^2 \sum_{n \ge 0} PD_2(4n + 2) q^n = 2 f_2^6 f_6^2$, and
$f_1^4 f_3^2 \sum_{n \ge 0} PD_2(4n + 3) q^n = 4 f_4^4 f_6^2$.

Since every $f_k$ with $k \ge 1$ is invertible, these are the source's quotient formulas for the
four generating functions $\sum_{n \ge 0} PD_2(4n + r) q^n$, $r = 0, 1, 2, 3$, with denominators
cleared.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Theorem 4.

Stated but not proved: `MetaMathlibExt.oddDesignatedSummandsCount_four_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-count-four-disse).

## The 2-dissection of $\mathrm{PD}_2$ modulo 4

Write $\mathrm{PD}_2(m)$ for the number of
partitions of $m$ with designated summands in which every part is odd, and write
$f_k = \prod_{j \ge 1} (1 - q^{kj})$ for the Euler product, an integer power series in $q$. For
every natural number $n$, the $n$th coefficient of
$f_1^2 f_3^2 \sum_{k \ge 0} \mathrm{PD}_2(2k) q^k$ is congruent modulo $4$ to the $n$th coefficient
of $f_4^2$, and $\mathrm{PD}_2(2n + 1)$ is congruent modulo $4$ to the $n$th coefficient of $f_6^2$.

Coefficientwise, these are $\sum_{k} \mathrm{PD}_2(2k) q^k \equiv f_4^2 / (f_1^2 f_3^2) \pmod 4$,
with its denominator cleared, and $\sum_{k} \mathrm{PD}_2(2k + 1) q^k \equiv f_6^2 \pmod 4$.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Theorem 5.

Stated but not proved: `MetaMathlibExt.oddDesignatedSummandsCount_two_dissection_mod_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-count-two-dissec-2).

## Congruences modulo 4 for $\mathrm{PD}_2$ at $4n + 3$, $6n + 3$ and $6n + 5$

Write
$\mathrm{PD}_2(m)$ for the number of partitions of $m$ with designated summands in which every part
is odd. For every natural number $n$, $\mathrm{PD}_2(4n + 3)$, $\mathrm{PD}_2(6n + 3)$ and
$\mathrm{PD}_2(6n + 5)$ are all congruent to $0$ modulo $4$.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Corollary 1.

Stated but not proved: `MetaMathlibExt.oddDesignatedSummandsCount_odd_args_mod_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-count-odd-args-m).

## $PD_2(4n)$ and $PD_2(4n+2)$ modulo 4

Let $f_k = \prod_{m \ge 1} (1 - q^{km})$ in the ring
of integer power series in $q$, and let $PD_2(n)$ be the number of partitions of $n$ with
designated summands in which every part is odd. For every $n \ge 0$, the coefficient of $q^n$ in
$f_6^2 \sum_{k \ge 0} PD_2(4k) q^k$ is congruent modulo $4$ to the coefficient of $q^n$ in
$f_2^6 + q f_6^2 f_{12}^2$, and $PD_2(4n + 2)$ is congruent modulo $4$ to the coefficient of
$q^n$ in $2 f_2^3 f_6$.

Since $f_6$ is invertible, this says $\sum_{n \ge 0} PD_2(4n) q^n \equiv f_2^6 / f_6^2 + q f_{12}^2$
(the source's eq. (3)) and $\sum_{n \ge 0} PD_2(4n + 2) q^n \equiv 2 f_2^3 f_6$ coefficientwise
modulo $4$.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Theorem 6.

Stated but not proved: `MetaMathlibExt.oddDesignatedSummandsCount_four_dissection_mod_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-count-four-disse-2).

## $PD_2(8n+6)$ is divisible by 4

Let $PD_2(n)$ be the number of partitions of $n$ with
designated summands in which every part is odd. For every $n \ge 0$,
$PD_2(8n + 6) \equiv 0 \pmod 4$.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Corollary 2.

Stated but not proved: `MetaMathlibExt.oddDesignatedSummandsCount_eight_mul_add_six` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-count-eight-mul).

## $PD_2(8n)$ and $PD_2(8n+4)$ modulo 4

Let $f_k = \prod_{m \ge 1} (1 - q^{km})$ in the ring
of integer power series in $q$, and let $PD_2(n)$ be the number of partitions of $n$ with
designated summands in which every part is odd. For every $n \ge 0$, the coefficient of $q^n$ in
$f_3^2 \sum_{k \ge 0} PD_2(8k) q^k$ is congruent modulo $4$ to the coefficient of $q^n$ in
$f_1^6$, and $PD_2(8n + 4)$ is congruent modulo $4$ to the coefficient of $q^n$ in $f_6^2$.

Since $f_3$ is invertible, this says $\sum_{n \ge 0} PD_2(8n) q^n \equiv f_1^6 / f_3^2$ and
$\sum_{n \ge 0} PD_2(8n + 4) q^n \equiv f_6^2$ coefficientwise modulo $4$.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Corollary 3.

Stated but not proved: `MetaMathlibExt.oddDesignatedSummandsCount_eight_dissection_mod_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-count-eight-diss).

## $\mathrm{PD}_2(16n + 12)$ is divisible by 4

Write $\mathrm{PD}_2(m)$ for the number of
partitions of $m$ with designated summands in which every part is odd. For every natural number $n$,
$\mathrm{PD}_2(16n + 12) \equiv 0 \pmod 4$.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Corollary 4.

Stated but not proved: `MetaMathlibExt.oddDesignatedSummandsCount_sixteen_mul_add_twelve` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-count-sixteen-mu).

## The internal congruence $PD_2(4n) \equiv PD_2(n) \pmod 4$

Let $PD_2(n)$ be the number of
partitions of $n$ with designated summands in which every part is odd. For every $n \ge 0$,
$PD_2(4n) \equiv PD_2(n) \pmod 4$.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Theorem 7.

Stated but not proved: `MetaMathlibExt.oddDesignatedSummandsCount_four_mul_mod_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-count-four-mul-m).

## $PD_2(4^\alpha (6n+5))$ is divisible by 4

Let $PD_2(n)$ be the number of partitions of $n$
with designated summands in which every part is odd. For all $\alpha \ge 0$ and $n \ge 0$,
$PD_2(4^\alpha (6n + 5)) \equiv 0 \pmod 4$.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Theorem 8.

Stated but not proved: `MetaMathlibExt.oddDesignatedSummandsCount_four_pow_mul_six_mul_add_five` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-count-four-pow-m).

## $PD_2(8n+7)$ is divisible by 8

Let $PD_2(n)$ be the number of partitions of $n$ with
designated summands in which every part is odd. For every $n \ge 0$,
$PD_2(8n + 7) \equiv 0 \pmod 8$.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Theorem 9.

Stated but not proved: `MetaMathlibExt.oddDesignatedSummandsCount_eight_mul_add_seven` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-count-eight-mul-2).

## $\mathrm{PD}_2(16n + 14)$ is divisible by 8

Write $\mathrm{PD}_2(m)$ for the number of
partitions of $m$ with designated summands in which every part is odd. For every natural number $n$,
$\mathrm{PD}_2(16n + 14) \equiv 0 \pmod 8$.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Theorem 10.

Stated but not proved: `MetaMathlibExt.oddDesignatedSummandsCount_sixteen_mul_add_fourteen` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-count-sixteen-mu-2).

## $\mathrm{PD}_2(32n + 28)$ is divisible by 8

Write $\mathrm{PD}_2(m)$ for the number of
partitions of $m$ with designated summands in which every part is odd. For every natural number $n$,
$\mathrm{PD}_2(32n + 28) \equiv 0 \pmod 8$.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Theorem 11.

Stated but not proved: `MetaMathlibExt.oddDesignatedSummandsCount_thirtyTwo_mul_add_twentyEight` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-count-thirty-two).

## $\mathrm{PD}_2(64n + 56)$ is divisible by 8

Write $\mathrm{PD}_2(m)$ for the number of
partitions of $m$ with designated summands in which every part is odd. For every natural number $n$,
$\mathrm{PD}_2(64n + 56) \equiv 0 \pmod 8$.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Theorem 12.

Stated but not proved: `MetaMathlibExt.oddDesignatedSummandsCount_sixtyFour_mul_add_fiftySix` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-count-sixty-four).

## Internal congruence $\mathrm{PD}_2(16n) \equiv \mathrm{PD}_2(4n) \pmod 8$

Write
$\mathrm{PD}_2(m)$ for the number of partitions of $m$ with designated summands in which every part
is odd. For every natural number $n$, $\mathrm{PD}_2(16n) \equiv \mathrm{PD}_2(4n) \pmod 8$.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Theorem 13.

Stated but not proved: `MetaMathlibExt.oddDesignatedSummandsCount_sixteen_mul_mod_eight` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-count-sixteen-mu-3).

## $PD_2(48n+26)$ is divisible by 4

Let $PD_2(n)$ be the number of partitions of $n$ with
designated summands in which every part is odd. For every $n \ge 0$,
$PD_2(48n + 26) \equiv 0 \pmod 4$.

## Sources

- James A. Sellers, *New Infinite Families of Congruences Modulo Powers of 2 for 2-Regular Partitions with Designated Summands*, INTEGERS 24 (2024), Article A16, Theorem 14.

Stated but not proved: `MetaMathlibExt.oddDesignatedSummandsCount_fortyEight_mul_add_twentySix` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OddDesignatedSummandsWanted.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html#odd-designated-summands-count-forty-eigh).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partitions with designated summands](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-designated-summands)
