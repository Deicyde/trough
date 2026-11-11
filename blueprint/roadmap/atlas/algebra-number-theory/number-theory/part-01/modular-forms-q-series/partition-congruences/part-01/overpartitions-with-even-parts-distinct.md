---
declaration: section
origin: cited
lean: MetaMathlibExt.overpartitionPairEvenDistinctGF, MetaMathlibExt.overpartitionPairEvenDistinct, MetaMathlibExt.overpartitionPairEvenDistinctGF_mul_qEulerProduct_sq, MetaMathlibExt.overpartitionPairEvenDistinct_zero, MetaMathlibExt.overpartitionPairEvenDistinct_three_three_congr_neg_six, MetaMathlibExt.overpartitionPairEvenDistinct_congr_neg_two_eleven, MetaMathlibExt.overpartitionPairEvenDistinct_congr_neg_two_nineteen, MetaMathlibExt.overpartitionPairEvenDistinct_congr_neg_one_five
statement: formalized
---

# Overpartitions with even parts distinct

33 results, 15 proved and 18 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html).

## Generating function of $(j, k)$-overpartition pairs with even parts distinct

For natural
numbers $j$ and $k$, let $f_a = \prod_{m \ge 1} (1 - q^{am})$ be the Euler products. This
generating function is the integer power series
$f_4^2 \bigl(\prod_{i \ge 0} (1 + q^{j+ki})\bigr)^2 \, g$, where $g$ is the inverse of $f_1^2$
(whose constant coefficient is $1$) and the infinite products are taken in the coefficientwise
topology. In $q$-Pochhammer notation it is
$(q^4; q^4)_\infty^2 (-q^j; q^k)_\infty^2 / (q; q)_\infty^2$. It is used for $k \ge j \ge 1$.

## Sources

- Adam Paksok and Nipen Saikia, *New Congruences for `[j, k]`-Overpartition Pairs with Even Parts Distinct*, INTEGERS 26 (2026), Article A118, Section 1, Equation (2).

Formalized by `MetaMathlibExt.overpartitionPairEvenDistinctGF`, a definition declared in [WantedExt/NumberTheory/OverpartitionPairsEvenPartsDistinctWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OverpartitionPairsEvenPartsDistinctWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#overpartition-pair-even-distinct-gf).

## The number of $(j, k)$-overpartition pairs with even parts distinct

For natural numbers
$j$, $k$ and $n$, $\mathrm{bped}_{j,k}(n)$ is the integer coefficient of $q^n$ in the generating
function of $[j, k]$-overpartition pairs with even parts distinct.

Combinatorially, for $1 \le j \le k$, $\mathrm{bped}_{j,k}(n)$ is the number of
$[j, k]$-overpartition pairs of $n$ with even parts distinct, in which the first occurrence of
each distinct part congruent to $j$ modulo $k$ may be overlined.

## Sources

- Adam Paksok and Nipen Saikia, *New Congruences for `[j, k]`-Overpartition Pairs with Even Parts Distinct*, INTEGERS 26 (2026), Article A118, Section 1, Equation (2).

Formalized by `MetaMathlibExt.overpartitionPairEvenDistinct`, a definition declared in [WantedExt/NumberTheory/OverpartitionPairsEvenPartsDistinctWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OverpartitionPairsEvenPartsDistinctWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#overpartition-pair-even-distinct).

## Cleared form of the generating function of $(j, k)$-overpartition pairs with even parts distinct

**Cleared form of the generating function of $[j, k]$-overpartition pairs with even parts
distinct.** For natural numbers $j$ and $k$, let $f_a = \prod_{m \ge 1} (1 - q^{am})$ be the
Euler products and let $G_{j,k}$ be the generating function of $[j, k]$-overpartition pairs with
even parts distinct. Then, as integer power series in $q$,
$G_{j,k} \, f_1^2 = f_4^2 \bigl(\prod_{i \ge 0} (1 + q^{j+ki})\bigr)^2$, where the infinite
product is taken in the coefficientwise topology. In $q$-Pochhammer notation this reads
$G_{j,k} \cdot (q; q)_\infty^2 = (q^4; q^4)_\infty^2 (-q^j; q^k)_\infty^2$.

## Sources

- Adam Paksok and Nipen Saikia, *New Congruences for `[j, k]`-Overpartition Pairs with Even Parts Distinct*, INTEGERS 26 (2026), Article A118, Section 1, Equation (2).

Formalized by `MetaMathlibExt.overpartitionPairEvenDistinctGF_mul_qEulerProduct_sq`, a theorem declared in [WantedExt/NumberTheory/OverpartitionPairsEvenPartsDistinctWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OverpartitionPairsEvenPartsDistinctWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#overpartition-pair-even-distinct-gf-mul).

## The count of overpartition pairs of $0$ with even parts distinct

For natural numbers
$j \ge 1$ and $k \ge 1$, the number $\mathrm{bped}_{j,k}(0)$ of $[j, k]$-overpartition pairs of $0$
with even parts distinct equals $1$ (the pair of empty overpartitions).

## Sources

- Adam Paksok and Nipen Saikia, *New Congruences for `[j, k]`-Overpartition Pairs with Even Parts Distinct*, INTEGERS 26 (2026), Article A118, Section 1, Equation (2).

Formalized by `MetaMathlibExt.overpartitionPairEvenDistinct_zero`, a theorem declared in [WantedExt/NumberTheory/OverpartitionPairsEvenPartsDistinctWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OverpartitionPairsEvenPartsDistinctWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#overpartition-pair-even-distinct-zero).

## Paksok–Saikia congruences for $(3, 3)$-overpartition pairs (Theorem 1)

Let
$\mathrm{bped}_{j,k}(n)$ be the number of $[j, k]$-overpartition pairs of $n$ with even parts
distinct. Let $p > 5$ be a prime with Legendre symbol $\left(\frac{-6}{p}\right) = -1$, and let
$k, m, \alpha, \beta$ be natural numbers with $p \nmid m$. Then
$\mathrm{bped}_{3,3}\bigl(4 \cdot 3^{4\alpha+3} \cdot 5^{2\beta} p^{2k+1} m +
(7 \cdot 3^{4\alpha+2} \cdot 5^{2\beta} p^{2k+2} - 1)/2\bigr) \equiv 0 \pmod{16}$ and
$\mathrm{bped}_{3,3}\bigl(12 \cdot 5^{2\beta} p^{2k+1} m +
(7 \cdot 5^{2\beta} p^{2k+2} - 1)/2\bigr) \equiv 0 \pmod{8}$.

The paper prints $p^{2\alpha+2}$ in place of $p^{2k+2}$ in both congruences (its (6) and (7)); its
proof substitutes $n = p^{2k+1} m + 7(p^{2k+2} - 1)/24$, which gives $p^{2k+2}$, and the printed
exponent fails: at $p = 13$, $k = 1$, $\alpha = \beta = 0$, $m = 2$ the printed argument of the
second congruence is $53319$, and $\mathrm{bped}_{3,3}(53319) \equiv 4 \pmod{8}$.

## Sources

- Adam Paksok and Nipen Saikia, *New Congruences for `[j, k]`-Overpartition Pairs with Even Parts Distinct*, INTEGERS 26 (2026), Article A118, Theorem 1.

Stated but not proved: `MetaMathlibExt.overpartitionPairEvenDistinct_three_three_congr_neg_six` is written with `theorem_wanted` in [WantedExt/NumberTheory/OverpartitionPairsEvenPartsDistinctWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OverpartitionPairsEvenPartsDistinctWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#overpartition-pair-even-distinct-three-t).

## Paksok–Saikia congruences for $(3, 3)$- and $(3, 6)$-overpartition pairs (Theorem 2)

Let
$\mathrm{bped}_{j,k}(n)$ be the number of $[j, k]$-overpartition pairs of $n$ with even parts
distinct. Let $p \ge 5$ be a prime with Legendre symbol $\left(\frac{-2}{p}\right) = -1$, and let
$k, m, \alpha, \beta$ be natural numbers with $p \nmid m$. Then
$\mathrm{bped}_{3,3}\bigl(4 \cdot 3^{4\alpha+3} \cdot 5^{2\beta} p^{2k+1} m +
(11 \cdot 3^{4\alpha+2} \cdot 5^{2\beta} p^{2k+2} - 1)/2\bigr) \equiv 0 \pmod{16}$,
$\mathrm{bped}_{3,3}\bigl(12 \cdot 5^{2\beta} p^{2k+1} m +
(11 \cdot 5^{2\beta} p^{2k+2} - 1)/2\bigr) \equiv 0 \pmod{4}$,
$\mathrm{bped}_{3,6}\bigl(3^{4\alpha+2} \cdot 5^{2\beta} p^{2k+1} (24m + 11p)\bigr) \equiv 0
\pmod{32}$ and
$\mathrm{bped}_{3,6}\bigl(3 \cdot 5^{2\beta} p^{2k+1} (24m + 11p)\bigr) \equiv 0 \pmod{32}$.

The paper prints $p^{2\alpha+2}$ in place of $p^{2k+2}$ in the first two congruences (its (10) and
(11)); the substitution in its proof gives $p^{2k+2}$, and the printed exponent fails: at $p = 5$,
$k = 1$, $\alpha = \beta = 0$, $m = 1$ the printed arguments are $14737$ and $1637$, and
$\mathrm{bped}_{3,3}(14737) \equiv 8 \pmod{16}$, $\mathrm{bped}_{3,3}(1637) \equiv 2 \pmod{4}$.

## Sources

- Adam Paksok and Nipen Saikia, *New Congruences for `[j, k]`-Overpartition Pairs with Even Parts Distinct*, INTEGERS 26 (2026), Article A118, Theorem 2.

Stated but not proved: `MetaMathlibExt.overpartitionPairEvenDistinct_congr_neg_two_eleven` is written with `theorem_wanted` in [WantedExt/NumberTheory/OverpartitionPairsEvenPartsDistinctWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OverpartitionPairsEvenPartsDistinctWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#overpartition-pair-even-distinct-congr-n).

## Paksok–Saikia congruences for $(3, 3)$- and $(3, 6)$-overpartition pairs (Theorem 3)

Let
$\mathrm{bped}_{j,k}(n)$ be the number of $[j, k]$-overpartition pairs of $n$ with even parts
distinct. Let $p \ge 5$ be a prime with Legendre symbol $\left(\frac{-2}{p}\right) = -1$, and let
$k, m, \alpha, \beta$ be natural numbers with $p \nmid m$. Then
$\mathrm{bped}_{3,3}\bigl(4 \cdot 3^{4\alpha+3} \cdot 5^{2\beta} p^{2k+1} m +
(19 \cdot 3^{4\alpha+2} \cdot 5^{2\beta} p^{2k+2} - 1)/2\bigr) \equiv 0 \pmod{16}$,
$\mathrm{bped}_{3,3}\bigl(12 \cdot 5^{2\beta} p^{2k+1} m +
(19 \cdot 5^{2\beta} p^{2k+2} - 1)/2\bigr) \equiv 0 \pmod{8}$,
$\mathrm{bped}_{3,6}\bigl(3^{4\alpha+2} \cdot 5^{2\beta} p^{2k+1} (24m + 19p)\bigr) \equiv 0
\pmod{32}$ and
$\mathrm{bped}_{3,6}\bigl(3 \cdot 5^{2\beta} p^{2k+1} (24m + 19p)\bigr) \equiv 0 \pmod{32}$.

The paper prints $p^{2\alpha+2}$ in place of $p^{2k+2}$ in the first two congruences (its (16) and
(17)); the substitution in its proof gives $p^{2k+2}$, and the printed exponent fails: at $p = 5$,
$k = 1$, $\alpha = \beta = 0$, $m = 1$ the printed arguments are $15637$ and $1737$, and
$\mathrm{bped}_{3,3}(15637) \equiv 8 \pmod{16}$, $\mathrm{bped}_{3,3}(1737) \equiv 4 \pmod{8}$.

## Sources

- Adam Paksok and Nipen Saikia, *New Congruences for `[j, k]`-Overpartition Pairs with Even Parts Distinct*, INTEGERS 26 (2026), Article A118, Theorem 3.

Stated but not proved: `MetaMathlibExt.overpartitionPairEvenDistinct_congr_neg_two_nineteen` is written with `theorem_wanted` in [WantedExt/NumberTheory/OverpartitionPairsEvenPartsDistinctWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OverpartitionPairsEvenPartsDistinctWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#overpartition-pair-even-distinct-congr-n-2).

## Paksok–Saikia congruences for $(3, 3)$- and $(3, 6)$-overpartition pairs (Theorem 4)

Let
$\mathrm{bped}_{j,k}(n)$ be the number of $[j, k]$-overpartition pairs of $n$ with even parts
distinct. Let $p \ge 5$ be a prime with Legendre symbol $\left(\frac{-1}{p}\right) = -1$, and let
$k, m, \alpha, \gamma$ be natural numbers with $p \nmid m$. Then
$\mathrm{bped}_{3,3}\bigl(4 \cdot 3^{4\alpha+2} \cdot 7^{2\gamma} p^{2k+1} m +
(5 \cdot 3^{4\alpha+1} \cdot 7^{2\gamma} p^{2k+2} - 1)/2\bigr) \equiv 0 \pmod{8}$,
$\mathrm{bped}_{3,6}\bigl(3^{4\alpha+2} \cdot 7^{2\gamma} p^{2k+1} (24m + 5p)\bigr) \equiv 0
\pmod{16}$ and
$\mathrm{bped}_{3,6}\bigl(3 \cdot 7^{2\gamma} p^{2k+1} (24m + 5p)\bigr) \equiv 0 \pmod{16}$.

The paper allows $p \ge 3$, but its proof needs $p \nmid 24m + 5p$, which fails for $p = 3$, and
all three congruences fail there: at $k = \alpha = \gamma = 0$, $m = 1$ one has
$\mathrm{bped}_{3,3}(175) \equiv 4 \pmod{8}$, $\mathrm{bped}_{3,6}(1053) \equiv 8 \pmod{16}$ and
$\mathrm{bped}_{3,6}(351) \equiv 8 \pmod{16}$; so $p \ge 5$ is assumed. The paper also prints
$p^{2\alpha+2}$ in place of $p^{2k+2}$ in the first congruence (its (22)); the substitution in its
proof gives $p^{2k+2}$, and the printed exponent fails: at $p = 7$, $k = 1$, $\alpha = \gamma = 0$,
$m = 1$ the printed argument is $12715$, and $\mathrm{bped}_{3,3}(12715) \equiv 4 \pmod{8}$.

## Sources

- Adam Paksok and Nipen Saikia, *New Congruences for `[j, k]`-Overpartition Pairs with Even Parts Distinct*, INTEGERS 26 (2026), Article A118, Theorem 4.

Stated but not proved: `MetaMathlibExt.overpartitionPairEvenDistinct_congr_neg_one_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/OverpartitionPairsEvenPartsDistinctWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OverpartitionPairsEvenPartsDistinctWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#overpartition-pair-even-distinct-congr-n-3).

## Paksok–Saikia congruences for $(3, 3)$- and $(3, 6)$-overpartition pairs (Theorem 5)

Let
$\mathrm{bped}_{j,k}(n)$ be the number of $[j, k]$-overpartition pairs of $n$ with even parts
distinct. Let $p \ge 5$ be a prime with Legendre symbol $\left(\frac{-3}{p}\right) = -1$, and let
$k, m, \alpha, \beta$ be natural numbers with $p \nmid m$. Then
$\mathrm{bped}_{3,3}\bigl(4 \cdot 3^{4\alpha+2} \cdot 5^{2\beta} p^{2k+1} m +
(13 \cdot 3^{4\alpha+1} \cdot 5^{2\beta} p^{2k+2} - 1)/2\bigr) \equiv 0 \pmod{8}$,
$\mathrm{bped}_{3,6}\bigl(3^{4\alpha+2} \cdot 5^{2\beta} p^{2k+1} (24m + 13p)\bigr) \equiv 0
\pmod{16}$ and
$\mathrm{bped}_{3,6}\bigl(3 \cdot 5^{2\beta} p^{2k+1} (24m + 13p)\bigr) \equiv 0 \pmod{16}$.

The paper prints $p^{2\alpha+2}$ in place of $p^{2k+2}$ in the first congruence (its (27)); the
substitution in its proof gives $p^{2k+2}$, and the printed exponent fails: at $p = 5$, $k = 1$,
$\alpha = \beta = 0$, $m = 3$ the printed argument is $13987$, and
$\mathrm{bped}_{3,3}(13987) \equiv 4 \pmod{8}$.

## Sources

- Adam Paksok and Nipen Saikia, *New Congruences for `[j, k]`-Overpartition Pairs with Even Parts Distinct*, INTEGERS 26 (2026), Article A118, Theorem 5.

Stated but not proved: `MetaMathlibExt.overpartitionPairEvenDistinct_congr_neg_three_thirteen` is written with `theorem_wanted` in [WantedExt/NumberTheory/OverpartitionPairsEvenPartsDistinctWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OverpartitionPairsEvenPartsDistinctWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#overpartition-pair-even-distinct-congr-n-4).

## Paksok–Saikia congruences for $(3, 6)$-overpartition pairs (Theorem 6)

Let
$\mathrm{bped}_{j,k}(n)$ be the number of $[j, k]$-overpartition pairs of $n$ with even parts
distinct. Let $p \ge 5$ be a prime with Legendre symbol $\left(\frac{-1}{p}\right) = -1$, and let
$k, m, \alpha$ be natural numbers with $p \nmid m$. Then
$\mathrm{bped}_{3,6}\bigl(3^{4\alpha+2} p^{2k+1} (12m + 5p)\bigr) \equiv 0 \pmod{16}$ and
$\mathrm{bped}_{3,6}\bigl(3 p^{2k+1} (12m + 5p)\bigr) \equiv 0 \pmod{16}$.

The paper allows $p \ge 3$, but its proof needs $p \nmid 24m + 10p$, which fails for $p = 3$, and
both congruences fail there: at $k = \alpha = 0$, $m = 1$ one has
$\mathrm{bped}_{3,6}(729) \equiv 12 \pmod{16}$ and $\mathrm{bped}_{3,6}(243) \equiv 12 \pmod{16}$;
so $p \ge 5$ is assumed. The paper's unused quantifier $\beta$ is dropped.

## Sources

- Adam Paksok and Nipen Saikia, *New Congruences for `[j, k]`-Overpartition Pairs with Even Parts Distinct*, INTEGERS 26 (2026), Article A118, Theorem 6.

Stated but not proved: `MetaMathlibExt.overpartitionPairEvenDistinct_three_six_congr_neg_one_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/OverpartitionPairsEvenPartsDistinctWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OverpartitionPairsEvenPartsDistinctWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#overpartition-pair-even-distinct-three-s).

## Ramanujan's 5-dissection of Euler's product

Let $q$ be a complex number with
$|q| < 1$. For $k \ge 1$ let $f_k = (q^k; q^k)_\infty = \prod_{n \ge 0} (1 - q^k q^{kn})$, and
for complex $a$, $b$ with $|a|, |b| < 1$ let $f(a, b) = \sum_{n \in \mathbb{Z}} a^{n(n+1)/2}
b^{n(n-1)/2}$ be Ramanujan's general theta function; all these products and series converge,
so the raw infinite product and the raw theta sum take these values. For $|x| < 1$ put
$R(x) = f(-x, -x^4) / f(-x^2, -x^3)$. Then
$f_1 = f_{25} \left( R(q^5)^{-1} - q - q^2 R(q^5) \right)$.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, Lemma 5.

Stated but not proved: `MetaMathlibExt.qPochhammerInf_five_dissection` is written with `theorem_wanted` in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#q-pochhammer-inf-five-dissection).

## Ramanujan's 7-dissection of Euler's product

Let $q$ be a complex number with
$|q| < 1$. For $k \ge 1$ let $f_k = (q^k; q^k)_\infty = \prod_{n \ge 0} (1 - q^k q^{kn})$, and
for complex $a$, $b$ with $|a|, |b| < 1$ let $f(a, b) = \sum_{n \in \mathbb{Z}} a^{n(n+1)/2}
b^{n(n-1)/2}$ be Ramanujan's general theta function; all these products and series converge,
so the raw infinite product and the raw theta sum take these values. For $|x| < 1$ put
$A(x) = f(-x^3, -x^4)$, $B(x) = f(-x^2, -x^5)$ and $C(x) = f(-x, -x^6)$. Then
$f_1 = f_{49} \left( B(q^7)/C(q^7) - q A(q^7)/B(q^7) - q^2 + q^5 C(q^7)/A(q^7) \right)$.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, Lemma 6.

Stated but not proved: `MetaMathlibExt.qPochhammerInf_seven_dissection` is written with `theorem_wanted` in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#q-pochhammer-inf-seven-dissection).

## The generating series for $\mathrm{ped}_{9,9}$

For $k \ge 1$ let
$f_k = \prod_{m \ge 1} (1 - q^{km})$, an integer power series in $q$ with constant coefficient $1$.
This is the integer power series

$$\frac{f_4 f_{18}}{f_1 f_9},$$

where the inverse of $f_1 f_9$ is taken in the ring of integer power series. For a natural number
$n$, its coefficient of $q^n$ is denoted $\mathrm{ped}_{9,9}(n)$.

By the source's equation (2), this is the generating function of the $[9, 9]$-overpartitions with
even parts distinct: partitions whose even parts are distinct, in which the first occurrence of
each part divisible by $9$ may be overlined.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, equations (2) and (22).

Formalized by `MetaMathlibExt.pedNineNineSeries`, a definition declared in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#ped-nine-nine-series).

## The partition function $\mathrm{ped}_{9,9}$

For $k \ge 1$ let
$f_k = \prod_{m \ge 1} (1 - q^{km})$, an integer power series in $q$ with constant coefficient $1$.
For a natural number $n$, $\mathrm{ped}_{9,9}(n)$ is the integer coefficient of $q^n$ in the power
series $f_4 f_{18} / (f_1 f_9)$.

By the source's equation (2), $\mathrm{ped}_{9,9}(n)$ is the number of $[9, 9]$-overpartitions of
$n$ with even parts distinct.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, equations (2) and (22).

Formalized by `MetaMathlibExt.pedNineNine`, a definition declared in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#ped-nine-nine).

## The generating series for $\mathrm{ped}_{9,18}$

For $k \ge 1$ let
$f_k = \prod_{m \ge 1} (1 - q^{km})$, an integer power series in $q$ with constant coefficient $1$.
This is the integer power series

$$\frac{f_4 f_{18}^2}{f_1 f_9 f_{36}},$$

where the inverse of $f_1 f_9 f_{36}$ is taken in the ring of integer power series. For a
natural number $n$, its coefficient of $q^n$ is denoted $\mathrm{ped}_{9,18}(n)$.

By the source's equation (2), this is the generating function of the $[9, 18]$-overpartitions with
even parts distinct: partitions whose even parts are distinct, in which the first occurrence of
each part congruent to $9$ modulo $18$ may be overlined.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, equations (2) and (77).

Formalized by `MetaMathlibExt.pedNineEighteenSeries`, a definition declared in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#ped-nine-eighteen-series).

## The partition function $\mathrm{ped}_{9,18}$

For $k \ge 1$ let
$f_k = \prod_{m \ge 1} (1 - q^{km})$, an integer power series in $q$ with constant coefficient $1$.
For a natural number $n$, $\mathrm{ped}_{9,18}(n)$ is the integer coefficient of $q^n$ in the power
series $f_4 f_{18}^2 / (f_1 f_9 f_{36})$.

By the source's equation (2), $\mathrm{ped}_{9,18}(n)$ is the number of $[9, 18]$-overpartitions of
$n$ with even parts distinct.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, equations (2) and (77).

Formalized by `MetaMathlibExt.pedNineEighteen`, a definition declared in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#ped-nine-eighteen).

## Generating function identity for $\mathrm{ped}_{9,9}$

For $k \ge 1$ let
$f_k = \prod_{m \ge 1} (1 - q^{km})$, an integer power series in $q$, and let
$\mathrm{ped}_{9,9}(n)$ be the coefficient of $q^n$ in $f_4 f_{18} / (f_1 f_9)$. Then, as integer
power series in $q$,

$$f_1 f_9 \sum_{n \ge 0} \mathrm{ped}_{9,9}(n) q^n = f_4 f_{18}.$$

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, equation (22).

Formalized by `MetaMathlibExt.pedNineNine_generatingFunction`, a theorem declared in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#ped-nine-nine-generating-function).

## Product identity for the (9, 18)-overpartition generating function

Let
$\mathrm{ped}_{9,18}(n)$ be the number of $[9, 18]$-overpartitions of $n$ with even parts
distinct, and let $f_k = \prod_{m \ge 1} (1 - q^{km})$. Then, as integer power series in $q$,
$f_1 f_9 f_{36} \sum_{n \ge 0} \mathrm{ped}_{9,18}(n) q^n = f_4 f_{18}^2$.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, equation (77).

Formalized by `MetaMathlibExt.pedNineEighteen_generatingFunction`, a theorem declared in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#ped-nine-eighteen-generating-function).

## Values of $\mathrm{ped}_{9,9}$ and $\mathrm{ped}_{9,18}$ at $0$

For $k \ge 1$ let
$f_k = \prod_{m \ge 1} (1 - q^{km})$, an integer power series in $q$, and let
$\mathrm{ped}_{9,9}(n)$ and $\mathrm{ped}_{9,18}(n)$ be the coefficients of $q^n$ in
$f_4 f_{18} / (f_1 f_9)$ and in $f_4 f_{18}^2 / (f_1 f_9 f_{36})$. Then
$\mathrm{ped}_{9,9}(0) = \mathrm{ped}_{9,18}(0) = 1$.

Both values count the empty overpartition.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, equations (22) and (77).

Formalized by `MetaMathlibExt.pedNineNine_zero_and_pedNineEighteen_zero`, a theorem declared in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#ped-nine-nine-zero-and-ped-nine-eighteen).

## Chan's matrix

Chan's matrix $(m_{i,j})_{i,j \ge 1}$ is the integer matrix with first
column $m_{1,1} = 3$, $m_{2,1} = 2$, $m_{3,1} = 1$ and $m_{i,1} = 0$ for $i \ge 4$, and with
$m_{i,j} = 9 m_{i-1,j-1} + 3 m_{i-2,j-1} + m_{i-3,j-1}$ for $i \ge 1$ and $j \ge 2$, where
entries with row index $\le 0$ are taken to be $0$.

The formalization indexes the matrix by all natural numbers, with row $0$ and column $0$ equal
to $0$.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, Section 2 (from H. C. Chan, Int. J. Number Theory 6 (2010), (11)-(19)).

Formalized by `MetaMathlibExt.chanCubicMatrix`, a definition declared in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#chan-cubic-matrix).

## First six rows of Chan's matrix

The upper left $6 \times 6$ block of Chan's matrix
$(m_{i,j})_{i,j \ge 1}$ is lower triangular, and its rows up to the diagonal are $(3)$,
$(2, 27)$, $(1, 27, 243)$, $(0, 18, 324, 2187)$, $(0, 5, 270, 3645, 19683)$ and
$(0, 1, 126, 3645, 39366, 177147)$: for $1 \le j \le i \le 6$, $m_{i,j}$ is the $j$th entry of
the $i$th listed row, and $m_{i,j} = 0$ for $1 \le i < j \le 6$.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, Section 2.

Formalized by `MetaMathlibExt.chanCubicMatrix_first_rows`, a theorem declared in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#chan-cubic-matrix-first-rows).

## Coefficient vectors from Chan's matrix

Let $(m_{i,j})_{i,j \ge 1}$ be Chan's matrix, and
for $i, j \ge 1$ let $a_{i,j} = m_{4i-3,i+j-1}$ and $b_{i,j} = m_{4i-1,i+j-1}$ be the entries of
the infinite matrices $A$ and $B$. The coefficient vectors
$X_\alpha = (x_{\alpha,1}, x_{\alpha,2}, \dots)$ of integers, for $\alpha \ge 0$, are defined by
$X_0 = (1, 0, 0, \dots)$ and, for $j \ge 1$, $x_{\alpha+1,j} = \sum_{i=1}^{3^\alpha} x_{\alpha,i}
a_{i,j}$ if $\alpha$ is even and $x_{\alpha+1,j} = \sum_{i=1}^{3^\alpha} x_{\alpha,i} b_{i,j}$ if
$\alpha$ is odd.

Since Chan's matrix is lower triangular, row $i$ of $A$ or $B$ vanishes beyond column $3i$, so by
induction $x_{\alpha,i} = 0$ for $i > 3^\alpha$; hence $X_{\alpha+1} = X_\alpha A$ for even
$\alpha$ and $X_{\alpha+1} = X_\alpha B$ for odd $\alpha$.

The formalization indexes the vectors from $0$: its value at $(\alpha, i)$ is $x_{\alpha,i+1}$.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, Section 2, equations (3)-(4), and Theorem 8.

Formalized by `MetaMathlibExt.cubicCoeffVector`, a definition declared in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#cubic-coeff-vector).

## Initial values of the cubic coefficient vectors

The coefficient vectors
$X_\alpha = (x_{\alpha,1}, x_{\alpha,2}, \dots)$ built from Chan's matrix satisfy
$(x_{1,1}, \dots, x_{1,5}) = (3, 0, 0, 0, 0)$ and
$(x_{2,1}, \dots, x_{2,5}) = (3, 81, 729, 0, 0)$.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, Theorem 8.

Formalized by `MetaMathlibExt.cubicCoeffVector_one_two`, a theorem declared in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#cubic-coeff-vector-one-two).

## The 2-dissection of $f_1^4$

For $k \ge 1$ let $f_k = \prod_{m \ge 1} (1 - q^{km})$, an
integer power series in $q$. Then

$$f_1^4 f_2^2 f_4^2 f_8^4 = f_4^{12} - 4 q f_2^4 f_8^8.$$

Dividing by $f_2^2 f_4^2 f_8^4$ gives
$f_1^4 = \frac{f_4^{10}}{f_2^2 f_8^4} - 4q \frac{f_2^2 f_8^4}{f_4^2}$.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, Lemma 1, (7).

Stated but not proved: `MetaMathlibExt.qEulerProduct_fourth_two_dissection` is written with `theorem_wanted` in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#q-euler-product-fourth-two-dissection).

## A 3-dissection of a quotient of Euler products

In the ring of integer power series in
$q$, let $f_k = \prod_{m \ge 1} (1 - q^{km})$ denote the Euler products. Then
$f_1^2 f_6 f_9 f_{18} = f_2 f_6 f_9^3 - 2q f_2 f_3 f_{18}^3$. Since every $f_k$ with $k \ge 1$ has
constant term $1$, this is the 3-dissection
$f_1^2 / f_2 = f_9^2 / f_{18} - 2q f_3 f_{18}^2 / (f_6 f_9)$ with denominators cleared.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, Lemma 3, (11).

Stated but not proved: `MetaMathlibExt.qEulerProduct_sq_div_three_dissection` is written with `theorem_wanted` in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#q-euler-product-sq-div-three-dissection).

## Congruences modulo 32 for $\mathrm{ped}_{9,9}$

For $k \ge 1$ let
$f_k = \prod_{m \ge 1} (1 - q^{km})$, an integer power series in $q$, and let
$\mathrm{ped}_{9,9}(n)$ be the coefficient of $q^n$ in $f_4 f_{18} / (f_1 f_9)$. Then for all
natural numbers $\alpha$, $\beta$ and $n$ the following congruences modulo $32$ hold, where
every division is exact.

(18) The coefficient of $q^n$ in
$f_2^2 \sum_{m \ge 0} \mathrm{ped}_{9,9}(3^{4\alpha+2} m + (3^{4\alpha+2} - 1)/2) q^m$ is congruent
to the coefficient of $q^n$ in $4 f_1^3 f_3 f_4 f_6 + 16 q f_2^2 f_6^6$. This is the source's
congruence $\sum_{m \ge 0} \mathrm{ped}_{9,9}(3^{4\alpha+2} m + (3^{4\alpha+2} - 1)/2) q^m \equiv
4 f_1^3 f_3 f_4 f_6 / f_2^2 + 16 q f_6^6$ multiplied by $f_2^2$.

(19) $\mathrm{ped}_{9,9}(4 \cdot 3^{4\alpha+6} n + (19 \cdot 3^{4\alpha+5} - 1)/2) \equiv
\mathrm{ped}_{9,9}(4 \cdot 3^{4\alpha+4} n + (19 \cdot 3^{4\alpha+3} - 1)/2)$.

(20) $\mathrm{ped}_{9,9}(4 \cdot 3^{4\alpha+4} \cdot 5^{2\beta} n +
(19 \cdot 3^{4\alpha+3} \cdot 5^{2\beta} - 1)/2)$ is congruent to the coefficient of $q^n$ in
$16 f_1 f_6^3$.

(21) $\mathrm{ped}_{9,9}(4 \cdot 3^{4\alpha+4} \cdot 5^{2\beta+1} (5n + i) +
(23 \cdot 3^{4\alpha+3} \cdot 5^{2\beta+1} - 1)/2) \equiv 0$ for $i \in \{0, 1, 2, 4\}$.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, Theorem 1.

Stated but not proved: `MetaMathlibExt.pedNineNine_congruences_mod_thirtyTwo` is written with `theorem_wanted` in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#ped-nine-nine-congruences-mod-thirty-two).

## Congruences modulo 16 for $\mathrm{ped}_{9,9}$

For $k \ge 1$ let
$f_k = \prod_{m \ge 1} (1 - q^{km})$, an integer power series in $q$, and let
$\mathrm{ped}_{9,9}(n)$ be the coefficient of $q^n$ in $f_4 f_{18} / (f_1 f_9)$. Then for all
natural numbers $\alpha$, $\beta$, $\gamma$ and $n$ the following congruences modulo $16$ hold,
where every division is exact.

(49) $\mathrm{ped}_{9,9}(4 \cdot 3^{4\alpha+6} n + (13 \cdot 3^{4\alpha+5} - 1)/2) \equiv 0$ and
$\mathrm{ped}_{9,9}(4 \cdot 3^{4\alpha+4} n + (13 \cdot 3^{4\alpha+3} - 1)/2) \equiv 0$.

(50) $\mathrm{ped}_{9,9}(4 \cdot 3^{4\alpha+6} n + (7 \cdot 3^{4\alpha+5} - 1)/2) \equiv
\mathrm{ped}_{9,9}(4 \cdot 3^{4\alpha+4} n + (7 \cdot 3^{4\alpha+3} - 1)/2)$.

(51) $\mathrm{ped}_{9,9}(2 \cdot 3^{4\alpha+5} n + (11 \cdot 3^{4\alpha+4} - 1)/2) \equiv 0$ and
$\mathrm{ped}_{9,9}(2 \cdot 3^{4\alpha+3} n + (11 \cdot 3^{4\alpha+2} - 1)/2) \equiv 0$.

(52) $\mathrm{ped}_{9,9}(2 \cdot 3^{4\alpha+6} n + (11 \cdot 3^{4\alpha+5} - 1)/2) \equiv 0$ and
$\mathrm{ped}_{9,9}(2 \cdot 3^{4\alpha+4} n + (11 \cdot 3^{4\alpha+3} - 1)/2) \equiv 0$.

(53) $\mathrm{ped}_{9,9}(4 \cdot 3^{4\alpha+4} \cdot 5^{2\beta} n +
(7 \cdot 3^{4\alpha+3} \cdot 5^{2\beta} - 1)/2)$ is congruent to the coefficient of $q^n$ in
$8 f_1^7$.

(54) $\mathrm{ped}_{9,9}(4 \cdot 3^{4\alpha+4} \cdot 5^{2\beta+1} (5n + i) +
(11 \cdot 3^{4\alpha+3} \cdot 5^{2\beta+1} - 1)/2) \equiv 0$ for $i \in \{0, 2, 3, 4\}$.

(55) $\mathrm{ped}_{9,9}(4 \cdot 3^{4\alpha+3} \cdot 7^{2\gamma} n +
(5 \cdot 3^{4\alpha+2} \cdot 7^{2\gamma} - 1)/2)$ is congruent to the coefficient of $q^n$ in
$8 f_1^5$.

(56) $\mathrm{ped}_{9,9}(4 \cdot 3^{4\alpha+3} \cdot 7^{2\gamma+1} (7n + j) +
(11 \cdot 3^{4\alpha+2} \cdot 7^{2\gamma+1} - 1)/2) \equiv 0$ for $j \in \{0, 2, 3, 4, 5, 6\}$.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, Theorem 2.

Stated but not proved: `MetaMathlibExt.pedNineNine_congruences_mod_sixteen` is written with `theorem_wanted` in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#ped-nine-nine-congruences-mod-sixteen).

## Further congruences modulo 16 for $\mathrm{ped}_{9,9}$

For $k \ge 1$ let
$f_k = \prod_{m \ge 1} (1 - q^{km})$, an integer power series in $q$, and let
$\mathrm{ped}_{9,9}(n)$ be the coefficient of $q^n$ in $f_4 f_{18} / (f_1 f_9)$. Then for all
natural numbers $\alpha$, $\beta$, $\gamma$ and $n$ the following congruences modulo $16$ hold,
where every division is exact.

(58) $\mathrm{ped}_{9,9}(4 \cdot 3^{4\alpha+3} n + (13 \cdot 3^{4\alpha+2} - 1)/2) \equiv 0$.

(59) $\mathrm{ped}_{9,9}(4 \cdot 3^{4\alpha+3} n + (19 \cdot 3^{4\alpha+2} - 1)/2) \equiv 0$.

(60) $\mathrm{ped}_{9,9}(4 \cdot 3^{4\alpha+3} \cdot 5^{2\beta} n +
(7 \cdot 3^{4\alpha+2} \cdot 5^{2\beta} - 1)/2)$ is congruent to the coefficient of $q^n$ in
$8 f_1^7$.

(61) $\mathrm{ped}_{9,9}(4 \cdot 3^{4\alpha+3} \cdot 5^{2\beta+1} (5n + i) +
(11 \cdot 3^{4\alpha+2} \cdot 5^{2\beta+1} - 1)/2) \equiv 0$ for $i \in \{0, 2, 3, 4\}$.

(62) $\mathrm{ped}_{9,9}(4 \cdot 3^{4\alpha+5} n + (13 \cdot 3^{4\alpha+4} - 1)/2) \equiv 0$.

(63) $\mathrm{ped}_{9,9}(2 \cdot 3^{4\alpha+5} n + (7 \cdot 3^{4\alpha+4} - 1)/2) \equiv
\mathrm{ped}_{9,9}(2 \cdot 3^{4\alpha+3} n + (7 \cdot 3^{4\alpha+2} - 1)/2)$.

(64) $\mathrm{ped}_{9,9}(4 \cdot 3^{4\alpha+4} \cdot 7^{2\gamma} n +
(5 \cdot 3^{4\alpha+3} \cdot 7^{2\gamma} - 1)/2)$ is congruent to the coefficient of $q^n$ in
$8 f_1^5$.

(65) $\mathrm{ped}_{9,9}(4 \cdot 3^{4\alpha+4} \cdot 7^{2\gamma+1} (7n + j) +
(11 \cdot 3^{4\alpha+3} \cdot 7^{2\gamma+1} - 1)/2) \equiv 0$ for $j \in \{0, 2, 3, 4, 5, 6\}$.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, Theorem 3.

Stated but not proved: `MetaMathlibExt.pedNineNine_more_congruences_mod_sixteen` is written with `theorem_wanted` in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#ped-nine-nine-more-congruences-mod-sixte).

## Congruences modulo 64 for (9, 18)-overpartitions with even parts distinct

Let
$\mathrm{ped}_{9,18}(n)$ be the number of $[9, 18]$-overpartitions of $n$ with even parts
distinct, let $f_k = \prod_{m \ge 1} (1 - q^{km})$, and read congruences between integer power
series in $q$ coefficientwise. For all $\alpha \ge 0$ the following hold modulo $64$, where the
statements about single values hold for every $n \ge 0$:
(73) $f_2^2 \sum_{n \ge 0} \mathrm{ped}_{9,18}\bigl(3^{4\alpha+2} n + (3^{4\alpha+3} + 1)/4\bigr)
q^n \equiv 12 f_1^4 f_3^6$;
(74) $\mathrm{ped}_{9,18}\bigl(3^{4\alpha+5} n + (7 \cdot 3^{4\alpha+4} + 1)/4\bigr) \equiv
\mathrm{ped}_{9,18}\bigl(3^{4\alpha+3} n + (7 \cdot 3^{4\alpha+2} + 1)/4\bigr)$;
(75) $\mathrm{ped}_{9,18}\bigl(3^{4\alpha+5} n + (11 \cdot 3^{4\alpha+4} + 1)/4\bigr) \equiv
\mathrm{ped}_{9,18}\bigl(3^{4\alpha+3} n + (11 \cdot 3^{4\alpha+2} + 1)/4\bigr)$;
(76) $\mathrm{ped}_{9,18}\bigl(3^{4\alpha+6} n + (5 \cdot 3^{4\alpha+5} + 1)/4\bigr) \equiv
\mathrm{ped}_{9,18}\bigl(3^{4\alpha+4} n + (5 \cdot 3^{4\alpha+3} + 1)/4\bigr)$.
All divisions by $4$ are exact.

The paper states (73) with $12 f_1^4 f_3^6 / f_2^2$ on the right; here $f_2^2$ is cleared.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, Theorem 4.

Stated but not proved: `MetaMathlibExt.pedNineEighteen_congruences_mod_sixtyFour` is written with `theorem_wanted` in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#ped-nine-eighteen-congruences-mod-sixty).

## Congruences modulo 32 for (9, 18)-overpartitions with even parts distinct

Let
$\mathrm{ped}_{9,18}(n)$ be the number of $[9, 18]$-overpartitions of $n$ with even parts
distinct, let $f_k = \prod_{m \ge 1} (1 - q^{km})$, and read congruences between integer power
series in $q$ coefficientwise. For all $\alpha, \beta \ge 0$ the following hold modulo $32$, where
the statements about single values hold for every $n \ge 0$:
(94) $\mathrm{ped}_{9,18}\bigl(3^{4\alpha+6} n + (3^{4\alpha+5} + 1)/4\bigr) \equiv
\mathrm{ped}_{9,18}\bigl(3^{4\alpha+4} n + (3^{4\alpha+3} + 1)/4\bigr)$;
(95) $\sum_{n \ge 0} \mathrm{ped}_{9,18}\bigl(2 \cdot 3^{4\alpha+3} 5^{2\beta} n +
(7 \cdot 3^{4\alpha+2} 5^{2\beta} + 1)/4\bigr) q^n \equiv 16 f_1^7$;
(96) $\mathrm{ped}_{9,18}\bigl(2 \cdot 3^{4\alpha+3} 5^{2\beta+1} (5n + i) +
(11 \cdot 3^{4\alpha+2} 5^{2\beta+1} + 1)/4\bigr) \equiv 0$ for $i \in \{0, 2, 3, 4\}$;
(97) $\sum_{n \ge 0} \mathrm{ped}_{9,18}\bigl(2 \cdot 3^{4\alpha+3} 5^{2\beta} n +
(19 \cdot 3^{4\alpha+2} 5^{2\beta} + 1)/4\bigr) q^n \equiv 16 f_1 f_6^3$;
(98) $\mathrm{ped}_{9,18}\bigl(2 \cdot 3^{4\alpha+3} 5^{2\beta+1} (5n + j) +
(23 \cdot 3^{4\alpha+2} 5^{2\beta+1} + 1)/4\bigr) \equiv 0$ for $j \in \{0, 1, 2, 4\}$;
(99) $\mathrm{ped}_{9,18}\bigl(2 \cdot 3^{4\alpha+3} n + (23 \cdot 3^{4\alpha+2} + 1)/4\bigr)
\equiv 0$;
(100) $\sum_{n \ge 0} \mathrm{ped}_{9,18}\bigl(2 \cdot 3^{4\alpha+3} 5^{2\beta} n +
(11 \cdot 3^{4\alpha+2} 5^{2\beta} + 1)/4\bigr) q^n \equiv 16 f_2 f_3^3$;
(101) $\mathrm{ped}_{9,18}\bigl(2 \cdot 3^{4\alpha+3} 5^{2\beta+1} (5n + k) +
(7 \cdot 3^{4\alpha+2} 5^{2\beta+1} + 1)/4\bigr) \equiv 0$ for $k \in \{0, 1, 3, 4\}$.
All divisions by $4$ are exact.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, Theorem 5.

Stated but not proved: `MetaMathlibExt.pedNineEighteen_congruences_mod_thirtyTwo` is written with `theorem_wanted` in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#ped-nine-eighteen-congruences-mod-thirty).

## Congruences modulo 16 and 8 for (9, 18)-overpartitions with even parts distinct

Let
$\mathrm{ped}_{9,18}(n)$ be the number of $[9, 18]$-overpartitions of $n$ with even parts
distinct, let $f_k = \prod_{m \ge 1} (1 - q^{km})$, and read congruences between integer power
series in $q$ coefficientwise. For all $\alpha, \beta, \gamma \ge 0$ the following hold, where the
statements about single values hold for every $n \ge 0$:
(105) $\sum_{n \ge 0} \mathrm{ped}_{9,18}\bigl(2 \cdot 3^{4\alpha+4} 5^{2\beta} n +
(13 \cdot 3^{4\alpha+3} 5^{2\beta} + 1)/4\bigr) q^n \equiv 8 f_1^{13} \pmod{16}$;
(106) $\mathrm{ped}_{9,18}\bigl(2 \cdot 3^{4\alpha+4} 5^{2\beta+1} (5n + i) +
(17 \cdot 3^{4\alpha+3} 5^{2\beta+1} + 1)/4\bigr) \equiv 0 \pmod{16}$ for $i \in \{0, 1, 3, 4\}$;
(107) $\sum_{n \ge 0} \mathrm{ped}_{9,18}\bigl(2 \cdot 3^{4\alpha+4} 7^{2\gamma} n +
(5 \cdot 3^{4\alpha+3} 7^{2\gamma} + 1)/4\bigr) q^n \equiv 8 f_1^5 \pmod{16}$;
(108) $\mathrm{ped}_{9,18}\bigl(2 \cdot 3^{4\alpha+4} 7^{2\gamma+1} (7n + j) +
(11 \cdot 3^{4\alpha+3} 7^{2\gamma+1} + 1)/4\bigr) \equiv 0 \pmod{16}$ for
$j \in \{0, 2, 3, 4, 5, 6\}$;
(109) $\mathrm{ped}_{9,18}\bigl(2 \cdot 3^{4\alpha+4} n + (3^{4\alpha+3} + 1)/4\bigr)$ is congruent
to $4$ modulo $8$ if $n = m(3m-1)/2$ for some integer $m$ (a generalized pentagonal number), and
to $0$ modulo $8$ otherwise.
All divisions by $4$ are exact.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, Theorem 6.

Stated but not proved: `MetaMathlibExt.pedNineEighteen_congruences_mod_sixteen` is written with `theorem_wanted` in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#ped-nine-eighteen-congruences-mod-sixtee).

## Congruences modulo 9 and 27 for (9, 18)-overpartitions with even parts distinct

Let
$\mathrm{ped}_{9,18}(n)$ be the number of $[9, 18]$-overpartitions of $n$ with even parts
distinct. For every $n \ge 0$, $\mathrm{ped}_{9,18}(27n + 16)$ and $\mathrm{ped}_{9,18}(27n + 25)$
are divisible by $9$, and $\mathrm{ped}_{9,18}(243n + 142)$, $\mathrm{ped}_{9,18}(243n + 223)$ and
$\mathrm{ped}_{9,18}(729n + 547)$ are divisible by $27$.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, Theorem 7.

Stated but not proved: `MetaMathlibExt.pedNineEighteen_congruences_mod_nine_twentySeven` is written with `theorem_wanted` in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 411](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L411). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#ped-nine-eighteen-congruences-mod-nine-t).

## Congruences modulo 27 for (9, 18)-overpartitions from the cubic coefficient vectors

Let
$\mathrm{ped}_{9,18}(n)$ be the number of $[9, 18]$-overpartitions of $n$ with even parts
distinct, let $f_k = \prod_{m \ge 1} (1 - q^{km})$, let
$X_\alpha = (x_{\alpha,1}, x_{\alpha,2}, \dots)$ be the coefficient vectors built from Chan's
matrix, and read congruences between integer power series in $q$ coefficientwise. For all
$\alpha \ge 0$, modulo $27$,
(124) $\sum_{n \ge 0} \mathrm{ped}_{9,18}\bigl(3^{2\alpha+5} n + (3^{2\alpha+5} + 1)/4\bigr) q^n
\equiv 9 \sum_{i=1}^{3^{2\alpha}} x_{2\alpha,i} \, q^{i-1}
\left(\frac{f_3 f_6}{f_1 f_2}\right)^{4i-3}$ and
(125) $\sum_{n \ge 0} \mathrm{ped}_{9,18}\bigl(3^{2\alpha+6} n + (3^{2\alpha+7} + 1)/4\bigr) q^n
\equiv 9 \sum_{i=1}^{3^{2\alpha+1}} x_{2\alpha+1,i} \, q^{i-1}
\left(\frac{f_3 f_6}{f_1 f_2}\right)^{4i-1}$.
All divisions by $4$ are exact, and $f_1 f_2$ is invertible as a power series because its
constant term is $1$.

The quotient $f_3 f_6 / (f_1 f_2)$ is the generating function of 3-regular cubic partitions.

## Sources

- Harishkumar T, Shruthi Menezes, and M. S. Mahadeva Naika, *On [j, k]-Overpartitions with Even Parts Distinct*, INTEGERS 25 (2025), Article A69, Theorem 8.

Stated but not proved: `MetaMathlibExt.pedNineEighteen_cubicCoeffVector_congruences` is written with `theorem_wanted` in [WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PedOverpartitionsDissectionsWanted.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html#ped-nine-eighteen-cubic-coeff-vector-con).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Overpartitions with even parts distinct](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartitions-with-even-parts-distinct)
