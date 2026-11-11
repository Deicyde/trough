---
declaration: section
origin: cited
lean: MetaMathlibExt.regularCubicOverlinedSeries, MetaMathlibExt.regularCubicOverlinedCount, MetaMathlibExt.regularCubicOverlinedCount_generatingFunction, MetaMathlibExt.regularCubicOverlinedCount_zero, MetaMathlibExt.f3_f5_quotients_two_dissection, MetaMathlibExt.regularCubicOverlinedCount_mod_four, MetaMathlibExt.regularCubicOverlinedCount_three_prime_mod_twelve, MetaMathlibExt.regularCubicOverlinedCount_three_mod_eighteen_twelve
statement: formalized
---

# ℓ-regular cubic partitions with overlined odd parts

19 results, 4 proved and 15 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part/index.html).

## Generating function of ℓ-regular cubic partitions with odd parts overlined

For a natural
number $\ell$, this is the integer power series

$$\frac{f_2 f_\ell^2 f_{4\ell}}{f_1^2 f_4 f_{2\ell}}, \qquad f_k = \prod_{m \ge 1} (1 - q^{km}).$$

It is meaningful for $\ell \ge 1$, where the denominator has constant term $1$ and so is
invertible. For $\ell > 2$, the range the paper considers, its coefficient of $q^n$ is the number
of $\ell$-regular cubic partitions of $n$ with odd parts overlined.

## Sources

- Pujashree Buragohain and Nipen Saikia, *Some New Congruences for l-Regular Cubic Partitions with Odd Parts Overlined*, INTEGERS 24 (2024), Article A101, Section 1, eq. (2).

Formalized by `MetaMathlibExt.regularCubicOverlinedSeries`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part/index.html#regular-cubic-overlined-series).

## ℓ-regular cubic partitions with odd parts overlined

For natural numbers $\ell$ and $n$,
$a_\ell(n)$ is the coefficient of $q^n$ in the integer power series

$$\frac{f_2 f_\ell^2 f_{4\ell}}{f_1^2 f_4 f_{2\ell}}, \qquad f_k = \prod_{m \ge 1} (1 - q^{km}).$$

The quotient is meaningful for $\ell \ge 1$, where the denominator has constant term $1$. For
$\ell > 2$, the range the paper considers, $a_\ell(n)$ is the number of $\ell$-regular cubic
partitions of $n$ in which the first occurrence of each distinct odd part may be overlined; for
example, $a_3(5) = 18$.

## Sources

- Pujashree Buragohain and Nipen Saikia, *Some New Congruences for l-Regular Cubic Partitions with Odd Parts Overlined*, INTEGERS 24 (2024), Article A101, Section 1, eq. (2).

Formalized by `MetaMathlibExt.regularCubicOverlinedCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part/index.html#regular-cubic-overlined-count).

## Generating function for $\ell$-regular cubic partitions with odd parts overlined

Let
$\ell \ge 1$, write $f_k = \prod_{m \ge 1} (1 - q^{km})$ for the Euler products in the ring of
integer power series in $q$, and let $a_\ell(n)$ be the $n$th coefficient of
$f_2 f_\ell^2 f_{4\ell} / (f_1^2 f_4 f_{2\ell})$ (the denominator has constant term $1$, so it
is invertible). Then

$$
f_1^2 f_4 f_{2\ell} \sum_{n \ge 0} a_\ell(n) q^n = f_2 f_\ell^2 f_{4\ell}.
$$

For $\ell > 2$ the paper identifies $a_\ell(n)$ with the number of $\ell$-regular cubic
partitions of $n$ with odd parts overlined.

## Sources

- Pujashree Buragohain and Nipen Saikia, *Some New Congruences for l-Regular Cubic Partitions with Odd Parts Overlined*, INTEGERS 24 (2024), Article A101, Section 1, eq. (2).

Formalized by `MetaMathlibExt.regularCubicOverlinedCount_generatingFunction`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part/index.html#regular-cubic-overlined-count-generating).

## Constant term of the overlined ℓ-regular cubic partition numbers

For every natural number
$\ell \ge 1$, the coefficient $a_\ell(0)$ of $q^0$ in the generating function of $\ell$-regular
cubic partitions with odd parts overlined equals $1$.

## Sources

- Pujashree Buragohain and Nipen Saikia, *Some New Congruences for l-Regular Cubic Partitions with Odd Parts Overlined*, INTEGERS 24 (2024), Article A101, Section 1, eq. (2).

Formalized by `MetaMathlibExt.regularCubicOverlinedCount_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part/index.html#regular-cubic-overlined-count-zero).

## Four 2-dissections of quotients of Euler products

Write
$f_k = \prod_{m \ge 1} (1 - q^{km})$ for the Euler products in the ring of integer power series
in $q$. Then

$$
f_3 f_2^2 f_8 f_{12} f_{16} f_{24} f_{48} =
f_1 \left(f_4 f_6 f_{16}^2 f_{24}^3 + q f_6 f_8^3 f_{12} f_{48}^2\right),
$$



$$
f_1^3 f_4 f_6^2 f_{12} = f_3 \left(f_4^4 f_6^2 - 3 q f_2^2 f_{12}^4\right),
$$



$$
f_5 f_2^3 f_8 f_{20} f_{40} = f_1 \left(f_2 f_8^2 f_{20}^3 + q f_4^3 f_{10} f_{40}^2\right),
$$



$$
f_1 f_4 f_8 f_{10}^3 f_{40} = f_5 \left(f_2 f_8^2 f_{20}^3 - q f_4^3 f_{10} f_{40}^2\right).
$$

These are the 2-dissections of $f_3 / f_1$, $f_1^3 / f_3$, $f_5 / f_1$ and $f_1 / f_5$ with the
denominators cleared; for example, the first is
$f_3 / f_1 = \frac{f_4 f_6 f_{16} f_{24}^2}{f_2^2 f_8 f_{12} f_{48}} +
q \frac{f_6 f_8^2 f_{48}}{f_2^2 f_{16} f_{24}}$ multiplied by
$f_1 f_2^2 f_8 f_{12} f_{16} f_{24} f_{48}$.

## Sources

- Pujashree Buragohain and Nipen Saikia, *Some New Congruences for l-Regular Cubic Partitions with Odd Parts Overlined*, INTEGERS 24 (2024), Article A101, Lemma 3, eqs. (9), (10), (13), (14).

Stated but not proved: `MetaMathlibExt.f3_f5_quotients_two_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part/index.html#f3-f5-quotients-two-dissection).

## Congruences modulo 4 for regular cubic partitions with odd parts overlined

Write
$f_k = \prod_{m \ge 1} (1 - q^{km})$ for the Euler products in the ring of integer power series
in $q$. For $\ell \ge 1$ let $a_\ell(n)$ be the $n$th coefficient of
$f_2 f_\ell^2 f_{4\ell} / (f_1^2 f_4 f_{2\ell})$; for $\ell > 2$ this is the number of
$\ell$-regular cubic partitions of $n$ with odd parts overlined. Then for all natural numbers
$k$ and $n$: (i) if $k > 1$, then $4$ divides $a_{2k}(4n + 3)$; (ii) if $k \ge 1$, then $4$
divides $a_{2k+1}(4n + 2)$; (iii) if $k > 0$, then $4$ divides $a_{4k}(4n + 2)$; (iv) if
$k > 0$, then $4$ divides $a_{4k+1}(4n + 3)$.

## Sources

- Pujashree Buragohain and Nipen Saikia, *Some New Congruences for l-Regular Cubic Partitions with Odd Parts Overlined*, INTEGERS 24 (2024), Article A101, Theorem 5, eqs. (17)–(20).

Stated but not proved: `MetaMathlibExt.regularCubicOverlinedCount_mod_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part/index.html#regular-cubic-overlined-count-mod-four).

## Congruences modulo 12 for 3-regular cubic partitions with odd parts overlined

Let
$a_3(n)$ be the number of $3$-regular cubic partitions of $n$ with odd parts overlined, and let
$f_k = \prod_{m \ge 1} (1 - q^{km})$. Let $p \ge 5$ be a prime with Legendre symbol
$\left(\frac{-6}{p}\right) = -1$, and let $\delta \ge 0$. Then for every $n \ge 0$,

$$a_3\left(8p^{2\delta} n + \frac{10p^{2\delta} - 1}{3}\right) \equiv 6c_n \pmod{12},$$

where $c_n$ is the coefficient of $q^n$ in $f_4 f_6$, and for all $n \ge 0$ and all $t$ with
$1 \le t \le p - 1$,

$$a_3\left(8p^{2\delta+2} n + 8p^{2\delta+1} t + \frac{10p^{2\delta+2} - 1}{3}\right)
\equiv 0 \pmod{12}.$$

The divisions by $3$ are exact.

## Sources

- Pujashree Buragohain and Nipen Saikia, *Some New Congruences for l-Regular Cubic Partitions with Odd Parts Overlined*, INTEGERS 24 (2024), Article A101, Theorem 6, eqs. (26), (27).

Stated but not proved: `MetaMathlibExt.regularCubicOverlinedCount_three_prime_mod_twelve` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part/index.html#regular-cubic-overlined-count-three-prim).

## Congruences modulo 18 and 12 for 3-regular cubic partitions with odd parts overlined

Let $a_3(n)$ be the number of $3$-regular cubic partitions of $n$ with odd parts overlined.
For every $n \ge 0$, $a_3(8n + 5)$ is divisible by $18$, and $a_3(16n + 11)$ and
$a_3(16n + 15)$ are divisible by $12$.

## Sources

- Pujashree Buragohain and Nipen Saikia, *Some New Congruences for l-Regular Cubic Partitions with Odd Parts Overlined*, INTEGERS 24 (2024), Article A101, Corollary 1, eqs. (39)–(41).

Stated but not proved: `MetaMathlibExt.regularCubicOverlinedCount_three_mod_eighteen_twelve` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part/index.html#regular-cubic-overlined-count-three-mod).

## Congruences modulo 6 for 3-regular cubic partitions with odd parts overlined

Let
$a_3(n)$ be the number of $3$-regular cubic partitions of $n$ with odd parts overlined, and let
$f_k = \prod_{m \ge 1} (1 - q^{km})$. Let $p \ge 5$ be a prime with Legendre symbol
$\left(\frac{-3}{p}\right) = -1$, and let $\delta \ge 0$. Then for every $n \ge 0$,

$$a_3\left(8p^{2\delta} n + \frac{4p^{2\delta} - 1}{3}\right) \equiv 2c_n \pmod 6,$$

where $c_n$ is the coefficient of $q^n$ in $f_1 f_3$, and for all $n \ge 0$ and all $t$ with
$1 \le t \le p - 1$,

$$a_3\left(8p^{2\delta+2} n + 8p^{2\delta+1} t + \frac{4p^{2\delta+2} - 1}{3}\right)
\equiv 0 \pmod 6.$$

The divisions by $3$ are exact.

## Sources

- Pujashree Buragohain and Nipen Saikia, *Some New Congruences for l-Regular Cubic Partitions with Odd Parts Overlined*, INTEGERS 24 (2024), Article A101, Theorem 7, eq. (46) and the unnumbered congruence after it.

Stated but not proved: `MetaMathlibExt.regularCubicOverlinedCount_three_prime_mod_six` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part/index.html#regular-cubic-overlined-count-three-prim-2).

## Congruences modulo 4 for 4-regular cubic partitions with odd parts overlined

Write
$f_k = \prod_{m \ge 1} (1 - q^{km})$ for the Euler products in the ring of integer power series
in $q$, and $a_4(n)$ for the $n$th coefficient of $f_2 f_4^2 f_{16} / (f_1^2 f_4 f_8)$, the
number of $4$-regular cubic partitions of $n$ with odd parts overlined. Let $p \ge 5$ be a prime
with Legendre symbol $\left(\frac{-2}{p}\right) = -1$ and let $\delta \ge 0$. Then for every
$n \ge 0$, $a_4(4p^{2\delta} n + (3p^{2\delta} - 1)/2)$ is congruent modulo $4$ to twice the
coefficient of $q^n$ in $f_1 f_8$, and for all $n \ge 0$ and $1 \le t \le p - 1$,

$$
a_4\left(4p^{2\delta+2} n + 4p^{2\delta+1} t + \frac{3p^{2\delta+2} - 1}{2}\right) \equiv 0
\pmod{4}.
$$

The divisions by $2$ are exact.

## Sources

- Pujashree Buragohain and Nipen Saikia, *Some New Congruences for l-Regular Cubic Partitions with Odd Parts Overlined*, INTEGERS 24 (2024), Article A101, Theorem 8, eq. (49) and the unnumbered congruence after it.

Stated but not proved: `MetaMathlibExt.regularCubicOverlinedCount_four_prime_mod_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part/index.html#regular-cubic-overlined-count-four-prime).

## Congruences modulo 8, 56 and 24 for 4-regular cubic partitions with odd parts overlined

Let $a_4(n)$ be the number of $4$-regular cubic partitions of $n$ with odd parts overlined, that
is, the $n$th coefficient of $f_2 f_4^2 f_{16} / (f_1^2 f_4 f_8)$, where
$f_k = \prod_{m \ge 1} (1 - q^{km})$. Then for every $n \ge 0$, $8$ divides $a_4(4n + 3)$, $56$
divides $a_4(28n + 4j + 3)$ for each $j = 1, \ldots, 6$, and $24$ divides $a_4(36n + 19)$.

## Sources

- Pujashree Buragohain and Nipen Saikia, *Some New Congruences for l-Regular Cubic Partitions with Odd Parts Overlined*, INTEGERS 24 (2024), Article A101, Corollary 2, eqs. (55)–(57).

Stated but not proved: `MetaMathlibExt.regularCubicOverlinedCount_four_mod_eight_fiftySix_twentyFour` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part/index.html#regular-cubic-overlined-count-four-mod-e).

## Congruences modulo 8 for 5-regular cubic partitions with odd parts overlined

Write
$f_k = \prod_{m \ge 1} (1 - q^{km})$ for the Euler products in the ring of integer power series
in $q$, and $a_5(n)$ for the $n$th coefficient of $f_2 f_5^2 f_{20} / (f_1^2 f_4 f_{10})$, the
number of $5$-regular cubic partitions of $n$ with odd parts overlined. Let $p \ge 5$ be a prime
with Legendre symbol $\left(\frac{-3}{p}\right) = -1$, let $s = (p - 1)/6$ if $p \equiv 1 \pmod 6$
and $s = (-p - 1)/6$ otherwise, and let $\delta \ge 0$. Then, comparing coefficients of power
series in $q$,

$$
\sum_{n \ge 0} a_5\left(10p^{2\delta} n + \frac{5p^{2\delta} - 2}{3}\right) q^n \equiv
2 (-1)^{\delta s} f_2^2 \pmod{8},
$$



$$
f_4 \sum_{n \ge 0} a_5\left(40p^{2\delta} n + \frac{65p^{2\delta} - 2}{3}\right) q^n \equiv
4 (-1)^{\delta s} f_1 f_8^2 \pmod{8},
$$

and for all $n \ge 0$ and $1 \le t \le p - 1$,

$$
a_5\left(10p^{2\delta+2} n + 10p^{2\delta+1} t + \frac{5p^{2\delta+2} - 2}{3}\right) \equiv 0
\pmod{8},
$$



$$
a_5\left(40p^{2\delta+2} n + 40p^{2\delta+1} t + \frac{65p^{2\delta+2} - 2}{3}\right) \equiv 0
\pmod{8}.
$$

The divisions by $3$ are exact. With $\psi(q) = f_2^2 / f_1$ and $\psi(q^4) = f_8^2 / f_4$, the
power series congruences are the paper's $\sum_n a_5(\ldots) q^n \equiv 2 (-1)^{\delta s} f_1
\psi(q) \pmod{8}$ and $\sum_n a_5(\ldots) q^n \equiv 4 (-1)^{\delta s} f_1 \psi(q^4) \pmod{8}$,
the second multiplied by $f_4$.

## Sources

- Pujashree Buragohain and Nipen Saikia, *Some New Congruences for l-Regular Cubic Partitions with Odd Parts Overlined*, INTEGERS 24 (2024), Article A101, Theorem 9, eqs. (64)–(67).

Stated but not proved: `MetaMathlibExt.regularCubicOverlinedCount_five_prime_mod_eight` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part/index.html#regular-cubic-overlined-count-five-prime).

## Congruences modulo 16 and 8 for 5-regular cubic partitions with odd parts overlined

Let
$a_5(n)$ be the number of $5$-regular cubic partitions of $n$ with odd parts overlined, that is,
the $n$th coefficient of $f_2 f_5^2 f_{20} / (f_1^2 f_4 f_{10})$, where
$f_k = \prod_{m \ge 1} (1 - q^{km})$. Then for every $n \ge 0$, $16$ divides $a_5(8n + 7)$, and
$8$ divides $a_5(20n + 2j + 1)$ for each $j = 1, \ldots, 9$.

## Sources

- Pujashree Buragohain and Nipen Saikia, *Some New Congruences for l-Regular Cubic Partitions with Odd Parts Overlined*, INTEGERS 24 (2024), Article A101, Corollary 3, eqs. (76), (77).

Stated but not proved: `MetaMathlibExt.regularCubicOverlinedCount_five_mod_sixteen_eight` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part/index.html#regular-cubic-overlined-count-five-mod-s).

## Congruences modulo 4 for 5-regular cubic partitions with odd parts overlined

Write
$f_k = \prod_{m \ge 1} (1 - q^{km})$ for the Euler products in the ring of integer power series
in $q$, and $a_5(n)$ for the $n$th coefficient of $f_2 f_5^2 f_{20} / (f_1^2 f_4 f_{10})$, the
number of $5$-regular cubic partitions of $n$ with odd parts overlined. Let $p \ge 5$ be a prime
with Legendre symbol $\left(\frac{-15}{p}\right) = -1$, let $s = (p - 1)/6$ if
$p \equiv 1 \pmod 6$ and $s = (-p - 1)/6$ otherwise, and let $\delta \ge 0$. Then, comparing
coefficients of power series in $q$,

$$
f_{20} \sum_{n \ge 0} a_5\left(16p^{2\delta+2} n + \frac{122p^{2\delta+2} - 2}{3}\right) q^n
\equiv 2 (-1)^{(\delta+1) s} f_1 f_{40}^2 \pmod{4},
$$

and for all $n \ge 0$ and $1 \le t \le p - 1$,

$$
a_5\left(16p^{2\delta+2} n + 16p^{2\delta+1} t + \frac{122p^{2\delta+2} - 2}{3}\right) \equiv 0
\pmod{4}.
$$

The divisions by $3$ are exact. With $\psi(q^{20}) = f_{40}^2 / f_{20}$, the first congruence is
the paper's $\sum_n a_5(\ldots) q^n \equiv 2 (-1)^{(\delta+1) s} f_1 \psi(q^{20}) \pmod{4}$
multiplied by $f_{20}$.

## Sources

- Pujashree Buragohain and Nipen Saikia, *Some New Congruences for l-Regular Cubic Partitions with Odd Parts Overlined*, INTEGERS 24 (2024), Article A101, Theorem 10, eqs. (80), (81).

Stated but not proved: `MetaMathlibExt.regularCubicOverlinedCount_five_prime_mod_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part/index.html#regular-cubic-overlined-count-five-prime-2).

## Congruences modulo 4 and 8 for 8-regular cubic partitions with odd parts overlined

Write
$f_k = \prod_{m \ge 1} (1 - q^{km})$ for the Euler products in the ring of integer power series
in $q$, and $a_8(n)$ for the $n$th coefficient of $f_2 f_8^2 f_{32} / (f_1^2 f_4 f_{16})$, the
number of $8$-regular cubic partitions of $n$ with odd parts overlined. Let $p \ge 5$ be a prime
with Legendre symbol $\left(\frac{-3}{p}\right) = -1$, let $s = (p - 1)/6$ if $p \equiv 1 \pmod 6$
and $s = (-p - 1)/6$ otherwise, and let $\delta \ge 0$. Then, comparing coefficients of power
series in $q$,

$$
f_4 \sum_{n \ge 0} a_8\left(4p^{2\delta} n + \frac{13p^{2\delta} - 7}{6}\right) q^n \equiv
2 (-1)^{\delta s} f_1 f_8^2 \pmod{4},
$$



$$
f_1 \sum_{n \ge 0} a_8\left(4p^{2\delta} n + \frac{19p^{2\delta} - 7}{6}\right) q^n \equiv
4 (-1)^{\delta s} f_2^2 f_{16} \pmod{8},
$$

and for all $n \ge 0$ and $1 \le t \le p - 1$,

$$
a_8\left(4p^{2\delta+2} n + 4p^{2\delta+1} t + \frac{13p^{2\delta+2} - 7}{6}\right) \equiv 0
\pmod{4},
$$



$$
a_8\left(4p^{2\delta+2} n + 4p^{2\delta+1} t + \frac{19p^{2\delta+2} - 7}{6}\right) \equiv 0
\pmod{8}.
$$

The divisions by $6$ are exact. With $\psi(q) = f_2^2 / f_1$ and $\psi(q^4) = f_8^2 / f_4$, the
power series congruences are the paper's $\sum_n a_8(\ldots) q^n \equiv 2 (-1)^{\delta s} f_1
\psi(q^4) \pmod{4}$ and $\sum_n a_8(\ldots) q^n \equiv 4 (-1)^{\delta s} \psi(q) f_{16} \pmod{8}$,
multiplied by $f_4$ and by $f_1$.

## Sources

- Pujashree Buragohain and Nipen Saikia, *Some New Congruences for l-Regular Cubic Partitions with Odd Parts Overlined*, INTEGERS 24 (2024), Article A101, Theorem 11, eqs. (93)–(96).

Stated but not proved: `MetaMathlibExt.regularCubicOverlinedCount_eight_prime_mod_four_eight` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part/index.html#regular-cubic-overlined-count-eight-prim).

## Congruences modulo 16 for 8-regular cubic partitions with odd parts overlined

Write
$f_k = \prod_{m \ge 1} (1 - q^{km})$ for the Euler products in the ring of integer power series
in $q$, and $a_8(n)$ for the $n$th coefficient of $f_2 f_8^2 f_{32} / (f_1^2 f_4 f_{16})$, the
number of $8$-regular cubic partitions of $n$ with odd parts overlined. Let $p \ge 5$ be a prime
with Legendre symbol $\left(\frac{-6}{p}\right) = -1$, let $s = (p - 1)/6$ if $p \equiv 1 \pmod 6$
and $s = (-p - 1)/6$ otherwise, and let $\delta \ge 0$. Then, comparing coefficients of power
series in $q$,

$$
f_8 \sum_{n \ge 0} a_8\left(4p^{2\delta} n + \frac{25p^{2\delta} - 7}{6}\right) q^n \equiv
8 (-1)^{\delta s} f_1 f_{16}^2 \pmod{16},
$$

and for all $n \ge 0$ and $1 \le t \le p - 1$,

$$
a_8\left(4p^{2\delta+2} n + 4p^{2\delta+1} t + \frac{25p^{2\delta+2} - 7}{6}\right) \equiv 0
\pmod{16}.
$$

The divisions by $6$ are exact. With $\psi(q^8) = f_{16}^2 / f_8$, the first congruence is
the paper's $\sum_n a_8(\ldots) q^n \equiv 8 (-1)^{\delta s} f_1 \psi(q^8) \pmod{16}$
multiplied by $f_8$.

## Sources

- Pujashree Buragohain and Nipen Saikia, *Some New Congruences for l-Regular Cubic Partitions with Odd Parts Overlined*, INTEGERS 24 (2024), Article A101, Theorem 12, eqs. (105), (106).

Stated but not proved: `MetaMathlibExt.regularCubicOverlinedCount_eight_prime_mod_sixteen` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part/index.html#regular-cubic-overlined-count-eight-prim-2).

## Congruences modulo 4 for 9-regular cubic partitions with odd parts overlined

Let
$a_9(n)$ be the number of $9$-regular cubic partitions of $n$ with odd parts overlined, and let
$f_k = \prod_{m \ge 1} (1 - q^{km})$. Let $p \ge 5$ be a prime with Legendre symbol
$\left(\frac{-2}{p}\right) = -1$, and let $\delta \ge 0$. Then for every $n \ge 0$,

$$a_9\left(8p^{2\delta} n + \frac{19p^{2\delta} - 4}{3}\right) \equiv 2c_n \pmod 4,$$

where $c_n$ is the coefficient of $q^n$ in $f_1 f_{18}$, and for all $n \ge 0$ and all $t$ with
$1 \le t \le p - 1$,

$$a_9\left(8p^{2\delta+2} n + 8p^{2\delta+1} t + \frac{19p^{2\delta+2} - 4}{3}\right)
\equiv 0 \pmod 4.$$

The divisions by $3$ are exact.

## Sources

- Pujashree Buragohain and Nipen Saikia, *Some New Congruences for l-Regular Cubic Partitions with Odd Parts Overlined*, INTEGERS 24 (2024), Article A101, Theorem 13, eq. (110) and the unnumbered congruence after it.

Stated but not proved: `MetaMathlibExt.regularCubicOverlinedCount_nine_prime_mod_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part/index.html#regular-cubic-overlined-count-nine-prime).

## Congruence modulo 8 for 9-regular cubic partitions with odd parts overlined

For every
$n \ge 0$, the number $a_9(4n + 3)$ of $9$-regular cubic partitions of $4n + 3$ with odd parts
overlined is divisible by $8$.

## Sources

- Pujashree Buragohain and Nipen Saikia, *Some New Congruences for l-Regular Cubic Partitions with Odd Parts Overlined*, INTEGERS 24 (2024), Article A101, Corollary 4, eq. (118).

Stated but not proved: `MetaMathlibExt.regularCubicOverlinedCount_nine_four_mul_add_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part/index.html#regular-cubic-overlined-count-nine-four).

## Congruences modulo 16 for 16-regular cubic partitions with odd parts overlined

Let
$a_{16}(n)$ be the number of $16$-regular cubic partitions of $n$ with odd parts overlined, and
let $f_k = \prod_{m \ge 1} (1 - q^{km})$. Let $p \ge 5$ be a prime with Legendre symbol
$\left(\frac{-2}{p}\right) = -1$, and let $\delta \ge 0$. Then for every $n \ge 0$,

$$a_{16}\left(4p^{2\delta} n + \frac{11p^{2\delta} - 5}{2}\right) \equiv 8c_n \pmod{16},$$

where $c_n$ is the coefficient of $q^n$ in $f_1 f_{32}$, and for all $n \ge 0$ and all $t$ with
$1 \le t \le p - 1$,

$$a_{16}\left(4p^{2\delta+2} n + 4p^{2\delta+1} t + \frac{11p^{2\delta+2} - 5}{2}\right)
\equiv 0 \pmod{16}.$$

The divisions by $2$ are exact.

## Sources

- Pujashree Buragohain and Nipen Saikia, *Some New Congruences for l-Regular Cubic Partitions with Odd Parts Overlined*, INTEGERS 24 (2024), Article A101, Theorem 14, eq. (119) and the unnumbered congruence after it.

Stated but not proved: `MetaMathlibExt.regularCubicOverlinedCount_sixteen_prime_mod_sixteen` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularCubicOverlinedWanted.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part/index.html#regular-cubic-overlined-count-sixteen-pr).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: ℓ-regular cubic partitions with overlined odd parts](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-cubic-partitions-with-overlined-odd-part)
