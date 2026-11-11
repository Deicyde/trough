---
declaration: section
origin: cited
lean: MetaMathlibExt.overpartition_mul_five_mod_five, Nat.Overpartition.natCard_eq_card_subtype, Nat.threeSquareRepresentationCount_eq_natCard, MetaMathlibExt.overpartition_card_mul_five_modEq, MetaMathlibExt.overpartition_three_pow_congr_zero_mod_512, MetaMathlibExt.eulerFunction_six_cube_nine_six_div_eq, MetaMathlibExt.eulerFunction_one_div_two_sq_eq
statement: formalized
---

# Overpartition congruences

7 results, 4 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartition-congruences/index.html).

## Overpartitions of $5n$ modulo $5$, explicit form

For every integer $n \ge 1$, the number of
pairs $(P, S)$, where $P$ is a finite multiset of positive integers with sum $5n$ and $S$ is a
finite set of natural numbers each belonging to $P$, is congruent modulo $5$ to $(-1)^n$ times the
number of ordered triples $(x, y, z)$ of integers with $x^2 + y^2 + z^2 = n$.

These pairs encode the overpartitions of $5n$: $P$ is the multiset of parts and $S$ is the set of
overlined part sizes.

## Sources

- Liuquan Wang, "Another Proof of a Conjecture by Hirschhorn and Sellers on Overpartitions," Journal of Integer Sequences 17 (2014), Article 14.9.8, Theorem, lines 110–114. <https://cs.uwaterloo.ca/journals/JIS/VOL17/Wang2/wang15.tex>

Formalized by `MetaMathlibExt.overpartition_mul_five_mod_five`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/OverpartitionCongruence.lean, line 1910](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/OverpartitionCongruence.lean#L1910). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartition-congruences/index.html#overpartition-mul-five-mod-five).

## Overpartitions as pairs of a multiset and a set

For every natural number $m$, the number
of overpartitions of $m$ equals the number of pairs $(P, S)$ in which $P$ is a finite multiset of
positive integers with sum $m$ and $S$ is a finite set of natural numbers each belonging to $P$.

Formalized by `Nat.Overpartition.natCard_eq_card_subtype`, a lemma declared in [MathlibExt/Combinatorics/Enumerative/Partition/OverpartitionCongruence.lean, line 2094](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/OverpartitionCongruence.lean#L2094). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartition-congruences/index.html#nat-card-eq-card-subtype).

## The three-square count counts all integer solutions

For every natural number $n$, the
three-square representation count $r_3(n)$ equals the number of ordered triples $(x, y, z)$ of
integers with $x^2 + y^2 + z^2 = n$.

Formalized by `Nat.threeSquareRepresentationCount_eq_natCard`, a lemma declared in [MathlibExt/Combinatorics/Enumerative/Partition/OverpartitionCongruence.lean, line 2132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/OverpartitionCongruence.lean#L2132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartition-congruences/index.html#three-square-representation-count-eq-nat).

## Overpartitions of $5n$ modulo $5$

For every integer $n \ge 1$, the number of
overpartitions of $5n$ is congruent modulo $5$ to $(-1)^n r_3(n)$, where $r_3(n)$ is the number of
ordered triples $(x, y, z)$ of integers with $x^2 + y^2 + z^2 = n$.

Formalized by `MetaMathlibExt.overpartition_card_mul_five_modEq`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/OverpartitionCongruence.lean, line 2197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/OverpartitionCongruence.lean#L2197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartition-congruences/index.html#overpartition-card-mul-five-mod-eq).

## Liang's congruences modulo 512 for overpartitions

For all natural numbers $\alpha$ and $n$,
the number $\overline{p}(m)$ of overpartitions of $m$ satisfies
$\overline{p}(3^{8\alpha+7}(24n+5)) \equiv 0 \pmod{512}$ and
$\overline{p}(3^{8\alpha+7}(24n+13)) \equiv 0 \pmod{512}$.

## Sources

- Xue Liang, *Congruences Modulo 512 for the Overpartition Function*, INTEGERS 25 (2025), Article A76, Theorem 1.

Stated but not proved: `MetaMathlibExt.overpartition_three_pow_congr_zero_mod_512` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OverpartitionModFiveTwelveWanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OverpartitionModFiveTwelveWanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartition-congruences/index.html#overpartition-three-pow-congr-zero-mod-5).

## Eta-quotient identity in the powers $q^3$, $q^6$, $q^9$ and $q^{18}$

Let $q$ be a complex
number with $|q| < 1$, and for each integer $k \ge 1$ write $E_k = (q^k; q^k)_\infty$, the
infinite q-Pochhammer symbol $\prod_{n=0}^{\infty} (1 - q^{k(n+1)})$. Then

$$
\frac{E_6^3 E_9^6}{E_3^3 E_{18}^3} =
  \frac{E_6^8 E_9}{E_3^4 E_{18}^2} - q^3 \, \frac{E_{18}^6}{E_9^3}.
$$

## Sources

- Xue Liang, *Congruences Modulo 512 for the Overpartition Function*, INTEGERS 25 (2025), Article A76, Lemma 1, identity (10). Identity (9) of the same lemma is `ramanujanPsi_three_dissection` (`OverpartitionSpt2CongruencesWanted`).

Stated but not proved: `MetaMathlibExt.eulerFunction_six_cube_nine_six_div_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OverpartitionModFiveTwelveWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OverpartitionModFiveTwelveWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartition-congruences/index.html#euler-function-six-cube-nine-six-div-eq).

## Three-dissection of $(q;q)_\infty / (q^2;q^2)_\infty^2$

Let $q$ be a complex number
with $|q| < 1$, and for each integer $k \ge 1$ write $E_k = (q^k; q^k)_\infty$, the infinite
q-Pochhammer symbol $\prod_{n=0}^{\infty} (1 - q^{k(n+1)})$. Then

$$
\frac{E_1}{E_2^2} = \frac{E_3^2 E_9^3}{E_6^6} - q \, \frac{E_3^3 E_{18}^3}{E_6^7} +
  q^2 \, \frac{E_3^4 E_{18}^6}{E_6^8 E_9^3}.
$$

## Sources

- Xue Liang, *Congruences Modulo 512 for the Overpartition Function*, INTEGERS 25 (2025), Article A76, Lemma 1, identity (11).

Stated but not proved: `MetaMathlibExt.eulerFunction_one_div_two_sq_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OverpartitionModFiveTwelveWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/OverpartitionModFiveTwelveWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartition-congruences/index.html#euler-function-one-div-two-sq-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Overpartition congruences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartition-congruences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/overpartition-congruences)
