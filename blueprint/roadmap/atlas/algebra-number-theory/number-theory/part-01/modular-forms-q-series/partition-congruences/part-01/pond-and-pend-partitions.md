---
declaration: section
origin: cited
lean: MetaMathlibExt.IsPondParts, MetaMathlibExt.IsPendParts, MetaMathlibExt.pondCount, MetaMathlibExt.pendCount, MetaMathlibExt.pondCount_zero, MetaMathlibExt.pendCount_zero, MetaMathlibExt.isPondParts_isPendParts_examples, MetaMathlibExt.pondCount_congruences
statement: formalized
---

# POND and PEND partitions

23 results, 7 proved and 16 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html).

## The POND condition

A multiset $s$ of natural numbers (the parts of a partition)
satisfies the POND condition when no odd number occurs in $s$ exactly once; equivalently,
every odd part that occurs in $s$ has multiplicity at least $2$, so the odd parts are not
distinct.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Section 1.

Formalized by `MetaMathlibExt.IsPondParts`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#is-pond-parts).

## The PEND condition

A multiset $s$ of natural numbers (the parts of a partition)
satisfies the PEND condition when no even number occurs in $s$ exactly once; equivalently,
every even part that occurs in $s$ has multiplicity at least $2$, so the even parts are not
distinct.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Section 1.

Formalized by `MetaMathlibExt.IsPendParts`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#is-pend-parts).

## Number of POND partitions

For a natural number $n$, $\mathrm{pond}(n)$ is the number of
partitions of $n$ that are POND, that is, in which every odd part that occurs has multiplicity
at least $2$ (OEIS A265256).

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Section 1.

Formalized by `MetaMathlibExt.pondCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#pond-count).

## The PEND partition function

For a natural number $n$, $\mathrm{pend}(n)$ is the number
of PEND partitions of $n$: partitions of $n$ in which every even part that occurs appears at
least twice (OEIS A265254).

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Section 1.

Formalized by `MetaMathlibExt.pendCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#pend-count).

## The number of POND partitions of zero

The number $\mathrm{pond}(0)$ of POND
partitions of $0$ equals $1$: the only partition of $0$ is the empty partition, and it is POND.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Section 1 (OEIS A265256).

Formalized by `MetaMathlibExt.pondCount_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#pond-count-zero).

## PEND partitions of zero

The number of PEND partitions of $0$ is $1$, that is,
$\mathrm{pend}(0) = 1$.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Section 1 (OEIS A265254).

Formalized by `MetaMathlibExt.pendCount_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#pend-count-zero).

## Examples of POND and PEND parts

The multisets of parts $\{1, 1\}$ and $\{2\}$ satisfy
the POND condition, while $\{1\}$ and $\{2, 1\}$ do not; the multisets $\{1\}$ and $\{2, 2\}$
satisfy the PEND condition, while $\{2\}$ and $\{2, 4\}$ do not.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Section 1.

Formalized by `MetaMathlibExt.isPondParts_isPendParts_examples`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#is-pond-parts-is-pend-parts-examples).

## Congruences modulo 2, 3 and 4 for POND partitions

Let $\mathrm{pond}(m)$ be the number
of POND partitions of $m$. For every natural number $n$, $\mathrm{pond}(3n + 2) \equiv 0 \pmod{2}$,
$\mathrm{pond}(27n + 26) \equiv 0 \pmod{3}$ and $\mathrm{pond}(3n + 1) \equiv 0 \pmod{4}$.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Theorem 1 (`jis-2024-24.4.7-thm-1`).

Stated but not proved: `MetaMathlibExt.pondCount_congruences` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#pond-count-congruences).

## Congruence modulo 3 for PEND partitions of 27n + 19

Let $\mathrm{pend}(m)$ be the
number of PEND partitions of $m$. For every natural number $n$,
$\mathrm{pend}(27n + 19) \equiv 0 \pmod{3}$.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Theorem 2 (`jis-2024-24.4.7-thm-2`).

Stated but not proved: `MetaMathlibExt.pendCount_twentySeven_mul_add_nineteen` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#pend-count-twenty-seven-mul-add-nineteen).

## Internal congruence modulo 3 for POND partitions

Let $\mathrm{pond}(m)$ be the number
of POND partitions of $m$. For every natural number $n$,
$\mathrm{pond}(27n + 17) \equiv \mathrm{pond}(3n + 2) \pmod{3}$.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Theorem 3 (`jis-2024-24.4.7-thm-3`).

Stated but not proved: `MetaMathlibExt.pondCount_internal_congruence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#pond-count-internal-congruence).

## Internal congruence modulo 3 for PEND partitions

Let $\mathrm{pend}(m)$ be the number
of PEND partitions of $m$. For every natural number $n$,
$\mathrm{pend}(27n + 10) \equiv \mathrm{pend}(3n + 1) \pmod{3}$.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Theorem 4 (`jis-2024-24.4.7-thm-4`).

Stated but not proved: `MetaMathlibExt.pendCount_internal_congruence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#pend-count-internal-congruence).

## Infinite family of congruences modulo 3 for POND partitions

Let $\mathrm{pond}(m)$ be
the number of POND partitions of $m$. For all natural numbers $\alpha \ge 1$ and $n$,
$\mathrm{pond}\left(3^{2\alpha+1} n + (23 \cdot 3^{2\alpha} + 1)/8\right) \equiv 0 \pmod{3}$.

The division by $8$ is exact, since $3^{2\alpha} \equiv 1 \pmod{8}$.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Theorem 5 (`jis-2024-24.4.7-thm-5`).

Stated but not proved: `MetaMathlibExt.pondCount_infinite_family` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#pond-count-infinite-family).

## Infinite family of congruences modulo 3 for PEND partitions

Let $\mathrm{pend}(m)$ be
the number of PEND partitions of $m$. For all natural numbers $\alpha \ge 1$ and $n$,
$\mathrm{pend}\left(3^{2\alpha+1} n + (17 \cdot 3^{2\alpha} - 1)/8\right) \equiv 0 \pmod{3}$.

The division by $8$ is exact, since $3^{2\alpha} \equiv 1 \pmod{8}$.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Theorem 6 (`jis-2024-24.4.7-thm-6`).

Stated but not proved: `MetaMathlibExt.pendCount_infinite_family` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#pend-count-infinite-family).

## 3-dissection of $f_2 / (f_1 f_4)$

Let $f_k = \prod_{m \ge 1} (1 - q^{km})$ denote the
Euler products in $\mathbb{Z}[[q]]$. Then
$f_2 f_3^4 f_9^3 f_{12}^4 f_{18}^3 f_{36}^3 = f_1 f_3^2 f_4 f_{12}^2 f_{18}^{12} +
q f_1 f_3 f_4 f_6^2 f_9^3 f_{12} f_{18}^6 f_{36}^3 + q^2 f_1 f_4 f_6^4 f_9^6 f_{36}^6$.

Since each $f_k$ with $k \ge 1$ has constant term $1$, dividing both sides by
$f_1 f_3^4 f_4 f_9^3 f_{12}^4 f_{18}^3 f_{36}^3$ shows that this is equivalent to
$f_2 / (f_1 f_4) = f_{18}^9 / (f_3^2 f_9^3 f_{12}^2 f_{36}^3) +
q f_6^2 f_{18}^3 / (f_3^3 f_{12}^3) + q^2 f_6^4 f_9^3 f_{36}^3 / (f_3^4 f_{12}^4 f_{18}^3)$.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Lemma 7 (`jis-2024-24.4.7-lem-7`).

Stated but not proved: `MetaMathlibExt.f2_div_f1_f4_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#f2-div-f1-f4-dissection).

## 3-dissection of $f_1 f_2$

Let $f_k = \prod_{m \ge 1} (1 - q^{km})$ denote the Euler
products in $\mathbb{Z}[[q]]$. Then
$f_1 f_2 f_3 f_6 f_9^2 f_{18}^2 = f_6^2 f_9^6 - q f_3 f_6 f_9^3 f_{18}^3 -
2 q^2 f_3^2 f_{18}^6$.

Since each $f_k$ with $k \ge 1$ has constant term $1$, dividing both sides by
$f_3 f_6 f_9^2 f_{18}^2$ shows that this is equivalent to
$f_1 f_2 = f_6 f_9^4 / (f_3 f_{18}^2) - q f_9 f_{18} - 2 q^2 f_3 f_{18}^4 / (f_6 f_9^2)$.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Lemma 8 (`jis-2024-24.4.7-lem-8`).

Stated but not proved: `MetaMathlibExt.f1_f2_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#f1-f2-dissection).

## 3-dissection of $1 / (f_1 f_2)$

Let $f_k = \prod_{m \ge 1} (1 - q^{km})$ denote the
Euler products in $\mathbb{Z}[[q]]$. Then
$f_3^6 f_6^6 f_9^3 f_{18}^3 = f_1 f_2 f_6^4 f_9^{12} + q f_1 f_2 f_3 f_6^3 f_9^9 f_{18}^3 +
3 q^2 f_1 f_2 f_3^2 f_6^2 f_9^6 f_{18}^6 - 2 q^3 f_1 f_2 f_3^3 f_6 f_9^3 f_{18}^9 +
4 q^4 f_1 f_2 f_3^4 f_{18}^{12}$.

Since each $f_k$ with $k \ge 1$ has constant term $1$, dividing both sides by
$f_1 f_2 f_3^6 f_6^6 f_9^3 f_{18}^3$ shows that this is equivalent to
$1 / (f_1 f_2) = f_9^9 / (f_3^6 f_6^2 f_{18}^3) + q f_9^6 / (f_3^5 f_6^3) +
3 q^2 f_9^3 f_{18}^3 / (f_3^4 f_6^4) - 2 q^3 f_{18}^6 / (f_3^3 f_6^5) +
4 q^4 f_{18}^9 / (f_3^2 f_6^6 f_9^3)$.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Lemma 9 (`jis-2024-24.4.7-lem-9`).

Stated but not proved: `MetaMathlibExt.one_div_f1_f2_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#one-div-f1-f2-dissection).

## 3-dissection of $f_2^2 / f_1$

Let $f_k = \prod_{m \ge 1} (1 - q^{km})$ denote the
Euler products in $\mathbb{Z}[[q]]$. Then
$f_2^2 f_3 f_9 f_{18} = f_1 f_6 f_9^3 + q f_1 f_3 f_{18}^3$.

Since each $f_k$ with $k \ge 1$ has constant term $1$, dividing both sides by
$f_1 f_3 f_9 f_{18}$ shows that this is equivalent to
$f_2^2 / f_1 = f_6 f_9^2 / (f_3 f_{18}) + q f_{18}^2 / f_9$.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Lemma 10 (`jis-2024-24.4.7-lem-10`).

Stated but not proved: `MetaMathlibExt.f2_sq_div_f1_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#f2-sq-div-f1-dissection).

## 3-dissection of $f_2 / f_1^2$

Let $f_k = \prod_{m \ge 1} (1 - q^{km})$ denote the
Euler products in $\mathbb{Z}[[q]]$. Then
$f_2 f_3^8 f_{18}^3 = f_1^2 f_6^4 f_9^6 + 2 q f_1^2 f_3 f_6^3 f_9^3 f_{18}^3 +
4 q^2 f_1^2 f_3^2 f_6^2 f_{18}^6$.

Since each $f_k$ with $k \ge 1$ has constant term $1$, dividing both sides by
$f_1^2 f_3^8 f_{18}^3$ shows that this is equivalent to
$f_2 / f_1^2 = f_6^4 f_9^6 / (f_3^8 f_{18}^3) + 2 q f_6^3 f_9^3 / f_3^7 +
4 q^2 f_6^2 f_{18}^3 / f_3^6$.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Lemma 11 (`jis-2024-24.4.7-lem-11`).

Stated but not proved: `MetaMathlibExt.f2_div_f1_sq_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#f2-div-f1-sq-dissection).

## 3-dissection of $f_4 / f_1$

Let $f_k = \prod_{m \ge 1} (1 - q^{km})$ denote the
Euler products in $\mathbb{Z}[[q]]$. Then
$f_3^4 f_4 f_{18}^2 f_{36}^2 = f_1 f_3 f_{12} f_{18}^6 + q f_1 f_6^2 f_9^3 f_{36}^3 +
2 q^2 f_1 f_3 f_6 f_{18}^3 f_{36}^3$.

Since each $f_k$ with $k \ge 1$ has constant term $1$, dividing both sides by
$f_1 f_3^4 f_{18}^2 f_{36}^2$ shows that this is equivalent to
$f_4 / f_1 = f_{12} f_{18}^4 / (f_3^3 f_{36}^2) + q f_6^2 f_9^3 f_{36} / (f_3^4 f_{18}^2) +
2 q^2 f_6 f_{18} f_{36} / f_3^3$.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Lemma 13 (`jis-2024-24.4.7-lem-13`).

Stated but not proved: `MetaMathlibExt.f4_div_f1_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#f4-div-f1-dissection).

## 2-dissection of $f_3^3 / f_1$

Let $f_k = \prod_{m \ge 1} (1 - q^{km})$ denote the
Euler products in $\mathbb{Z}[[q]]$. Then
$f_2^2 f_3^3 f_4 f_{12} - q f_1 f_2^2 f_{12}^4 = f_1 f_4^4 f_6^2$.

Since each $f_k$ with $k \ge 1$ has constant term $1$, dividing both sides by
$f_1 f_2^2 f_4 f_{12}$ shows that this is equivalent to
$f_3^3 / f_1 - q f_{12}^3 / f_4 = f_4^3 f_6^2 / (f_2^2 f_{12})$.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Lemma 15 (`jis-2024-24.4.7-lem-15`).

Stated but not proved: `MetaMathlibExt.f3_cube_div_f1_sub` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#f3-cube-div-f1-sub).

## Prime-power congruence for powers of Euler products

Let $p$ be a prime, let
$j, k, m \ge 1$ be natural numbers, and let $f_m = \prod_{i \ge 1} (1 - q^{mi})$. Then for every
natural number $n$, the coefficient of $q^n$ in $f_m^{p^j k}$ is congruent modulo $p^j$ to the
coefficient of $q^n$ in $f_{pm}^{p^{j-1} k}$.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Lemma 16 (`jis-2024-24.4.7-lem-16`).

Stated but not proved: `MetaMathlibExt.qEulerProduct_pow_prime_pow_congruence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#q-euler-product-pow-prime-pow-congruence).

## Generating function for POND partitions

Let $\mathrm{pond}(n)$ be the number of POND
partitions of $n$, and let $f_k = \prod_{m \ge 1} (1 - q^{km})$. Then, as integer power series
in $q$, $f_2^2 f_3 f_{12} \sum_{n \ge 0} \mathrm{pond}(n) q^n = f_4 f_6^2$. This is the identity
$\sum_{n \ge 0} \mathrm{pond}(n) q^n = f_4 f_6^2 / (f_2^2 f_3 f_{12})$ with the denominator
cleared.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Theorem 17 (`jis-2024-24.4.7-thm-17`).

Stated but not proved: `MetaMathlibExt.pondCount_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#pond-count-generating-function).

## Generating function for PEND partitions

Let $\mathrm{pend}(n)$ be the number of PEND
partitions of $n$, and let $f_k = \prod_{m \ge 1} (1 - q^{km})$. Then, as integer power series
in $q$, $f_1 f_4 f_6 \sum_{n \ge 0} \mathrm{pend}(n) q^n = f_2 f_{12}$. This is the identity
$\sum_{n \ge 0} \mathrm{pend}(n) q^n = f_2 f_{12} / (f_1 f_4 f_6)$ with the denominator cleared.

## Sources

- James A. Sellers, *Elementary Proofs of Congruences for POND and PEND Partitions*, Journal of Integer Sequences 27 (2024), Article 24.4.7, Theorem 18 (`jis-2024-24.4.7-thm-18`).

Stated but not proved: `MetaMathlibExt.pendCount_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/PondPendCongruencesWanted.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html#pend-count-generating-function).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: POND and PEND partitions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/pond-and-pend-partitions)
