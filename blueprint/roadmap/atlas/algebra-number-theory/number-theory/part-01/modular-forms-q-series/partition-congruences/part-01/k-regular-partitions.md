---
declaration: section
origin: cited
lean: MetaMathlibExt.regularPartitionCount, MetaMathlibExt.regularPartitionCount_four_nine_zero, MetaMathlibExt.regularPartitionCount_of_lt, MetaMathlibExt.regularPartitionCount_four_prime_mod_two, MetaMathlibExt.regularPartitionCount_two_prime_mod_two, MetaMathlibExt.regularPartitionCount_four_nine_mod_twelve, MetaMathlibExt.f9_div_f1_two_dissection, MetaMathlibExt.f3_div_f1_cube_two_dissection
statement: formalized
---

# (ℓ, k)-regular partitions

15 results, 3 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/k-regular-partitions/index.html).

## Number of $(\ell, k)$-regular partitions

For natural numbers $\ell$, $k$ and $n$,
$b_{\ell,k}(n)$ is the number of $(\ell, k)$-regular partitions of $n$, that is, partitions of
$n$ none of whose parts is divisible by $\ell$ or by $k$.

## Sources

- Manjil P. Saikia and James A. Sellers, *Generalizing Recent Results of Kathiravan, Majumdar, Sangale, and Srinivas on `(ℓ, k)`-regular Partitions*, Journal of Integer Sequences 28 (2025), Article 25.6.1, Section 1 (definition of `b_{ℓ,k}(n)`).

Formalized by `MetaMathlibExt.regularPartitionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/k-regular-partitions/index.html#regular-partition-count).

## The $(4, 9)$-regular partition count at zero

The number $b_{4,9}(0)$ of
$(4, 9)$-regular partitions of $0$, that is, partitions of $0$ none of whose parts is divisible by
$4$ or by $9$, equals $1$: the only such partition is the empty partition.

## Sources

- Manjil P. Saikia and James A. Sellers, *Generalizing Recent Results of Kathiravan, Majumdar, Sangale, and Srinivas on `(ℓ, k)`-regular Partitions*, Journal of Integer Sequences 28 (2025), Article 25.6.1, Section 1 (definition of `b_{ℓ,k}(n)`).

Formalized by `MetaMathlibExt.regularPartitionCount_four_nine_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/k-regular-partitions/index.html#regular-partition-count-four-nine-zero).

## For small $n$ every partition is $(\ell, k)$-regular

Let $\ell$, $k$ and $n$ be natural
numbers with $n < \ell$ and $n < k$, and write $b_{\ell,k}(n)$ for the number of
$(\ell, k)$-regular partitions of $n$ (partitions none of whose parts is divisible by $\ell$ or by
$k$) and $p(n)$ for the number of all partitions of $n$. Then every partition of $n$ is
$(\ell, k)$-regular, so $b_{\ell,k}(n) = p(n)$.

## Sources

- Manjil P. Saikia and James A. Sellers, *Generalizing Recent Results of Kathiravan, Majumdar, Sangale, and Srinivas on `(ℓ, k)`-regular Partitions*, Journal of Integer Sequences 28 (2025), Article 25.6.1, Section 1 (definition of `b_{ℓ,k}(n)`).

Formalized by `MetaMathlibExt.regularPartitionCount_of_lt`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/k-regular-partitions/index.html#regular-partition-count-of-lt).

## Parity of $(4, p)$-regular partitions in nonresidue progressions

Let $p \ge 5$ be a
prime and let $r$ be a natural number such that $8r + 1$ is not a square modulo $p$ (a quadratic
nonresidue). Write $b_{4,p}(m)$ for the number of $(4, p)$-regular partitions of $m$, that is,
partitions of $m$ none of whose parts is divisible by $4$ or by $p$. Then
$b_{4,p}(pn + r) \equiv 0 \pmod 2$ for every natural number $n$.

Restricting $r$ to natural numbers loses nothing: every residue class modulo $p$ has a
natural-number representative.

## Sources

- Manjil P. Saikia and James A. Sellers, *Generalizing Recent Results of Kathiravan, Majumdar, Sangale, and Srinivas on `(ℓ, k)`-regular Partitions*, Journal of Integer Sequences 28 (2025), Article 25.6.1, Theorem 1 (`jis-2025-25.6.1-thm-1`).

Stated but not proved: `MetaMathlibExt.regularPartitionCount_four_prime_mod_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/k-regular-partitions/index.html#regular-partition-count-four-prime-mod-t).

## Parity of $(2, p)$-regular partitions in nonresidue progressions

Let $p \ge 5$ be a
prime and let $r$ be a natural number such that $24r + 1$ is not a square modulo $p$ (a quadratic
nonresidue). Write $b_{2,p}(m)$ for the number of $(2, p)$-regular partitions of $m$, that is,
partitions of $m$ none of whose parts is divisible by $2$ or by $p$. Then
$b_{2,p}(pn + r) \equiv 0 \pmod 2$ for every natural number $n$.

## Sources

- Manjil P. Saikia and James A. Sellers, *Generalizing Recent Results of Kathiravan, Majumdar, Sangale, and Srinivas on `(ℓ, k)`-regular Partitions*, Journal of Integer Sequences 28 (2025), Article 25.6.1, Theorem 2 (`jis-2025-25.6.1-thm-2`).

Stated but not proved: `MetaMathlibExt.regularPartitionCount_two_prime_mod_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/k-regular-partitions/index.html#regular-partition-count-two-prime-mod-tw).

## Congruences modulo $12$ for $b_{4,9}$ along powers of $2$

Let $b_{4,9}(n)$ be the
number of partitions of $n$ with no part divisible by $4$ or by $9$. For all natural numbers
$\alpha \ge 3$ and $n$, $b_{4,9}(2^\alpha n + 6 \cdot 2^{\alpha - 3} + 1) \equiv 0 \pmod{12}$.

## Sources

- Manjil P. Saikia and James A. Sellers, *Generalizing Recent Results of Kathiravan, Majumdar, Sangale, and Srinivas on `(ℓ, k)`-regular Partitions*, Journal of Integer Sequences 28 (2025), Article 25.6.1, Theorem 3 (`jis-2025-25.6.1-thm-3`).

Stated but not proved: `MetaMathlibExt.regularPartitionCount_four_nine_mod_twelve` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/k-regular-partitions/index.html#regular-partition-count-four-nine-mod-tw).

## The 2-dissection of $f_9/f_1$

Write $f_k = (q^k; q^k)_\infty$ for the Euler products. In
the ring of integer power series in $q$,

$$
f_9 f_2^3 f_6 f_{12} f_{36} = f_1 f_2 f_{12}^4 f_{18} + q f_1 f_4^2 f_6^2 f_{36}^2.
$$

Since each $f_k$ with $k \ge 1$ has constant term $1$ and is therefore invertible, this is the
identity $f_9 / f_1 = f_{12}^3 f_{18} / (f_2^2 f_6 f_{36}) + q f_4^2 f_6 f_{36} / (f_2^3 f_{12})$
with both sides multiplied by $f_1 f_2^3 f_6 f_{12} f_{36}$.

## Sources

- Manjil P. Saikia and James A. Sellers, *Generalizing Recent Results of Kathiravan, Majumdar, Sangale, and Srinivas on `(ℓ, k)`-regular Partitions*, Journal of Integer Sequences 28 (2025), Article 25.6.1, Lemma 7 (`jis-2025-25.6.1-lem-7`).

Stated but not proved: `MetaMathlibExt.f9_div_f1_two_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/k-regular-partitions/index.html#f9-div-f1-two-dissection).

## The 2-dissection of $f_3/f_1^3$

Write $f_k = (q^k; q^k)_\infty$ for the Euler products. In
the ring of integer power series in $q$,

$$
f_3 f_2^9 f_{12}^2 = f_1^3 f_4^6 f_6^3 + 3q f_1^3 f_2^2 f_4^2 f_6 f_{12}^4.
$$

Since each $f_k$ with $k \ge 1$ has constant term $1$ and is therefore invertible, this is the
identity $f_3 / f_1^3 = f_4^6 f_6^3 / (f_2^9 f_{12}^2) + 3q f_4^2 f_6 f_{12}^2 / f_2^7$ with both
sides multiplied by $f_1^3 f_2^9 f_{12}^2$.

## Sources

- Manjil P. Saikia and James A. Sellers, *Generalizing Recent Results of Kathiravan, Majumdar, Sangale, and Srinivas on `(ℓ, k)`-regular Partitions*, Journal of Integer Sequences 28 (2025), Article 25.6.1, Lemma 8 (`jis-2025-25.6.1-lem-8`).

Stated but not proved: `MetaMathlibExt.f3_div_f1_cube_two_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/k-regular-partitions/index.html#f3-div-f1-cube-two-dissection).

## The 2-dissection of $f_3^2/f_1^2$

Write $f_k = (q^k; q^k)_\infty$ for the Euler products.
In the ring of integer power series in $q$,

$$
f_3^2 f_2^5 f_8 f_{12} f_{24} = f_1^2 f_4^4 f_6 f_{12}^3 + 2q f_1^2 f_2 f_4 f_6^2 f_8^2 f_{24}^2.
$$

Since each $f_k$ with $k \ge 1$ has constant term $1$ and is therefore invertible, this is the
identity $f_3^2 / f_1^2 = f_4^4 f_6 f_{12}^2 / (f_2^5 f_8 f_{24}) +
2q f_4 f_6^2 f_8 f_{24} / (f_2^4 f_{12})$ with both sides multiplied by
$f_1^2 f_2^5 f_8 f_{12} f_{24}$.

## Sources

- Manjil P. Saikia and James A. Sellers, *Generalizing Recent Results of Kathiravan, Majumdar, Sangale, and Srinivas on `(ℓ, k)`-regular Partitions*, Journal of Integer Sequences 28 (2025), Article 25.6.1, Lemma 9 (`jis-2025-25.6.1-lem-9`).

Stated but not proved: `MetaMathlibExt.f3_sq_div_f1_sq_two_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/k-regular-partitions/index.html#f3-sq-div-f1-sq-two-dissection).

## The 2-dissections of $1/f_1^4$, $1/f_1^8$ and $1/f_1^{12}$

Write
$f_k = (q^k; q^k)_\infty$ for the Euler products. In the ring of integer power series in $q$,
the following three identities hold:

$$
f_2^{14} f_8^4 = f_1^4 f_4^{14} + 4q f_1^4 f_2^4 f_4^2 f_8^8,
$$



$$
f_2^{28} f_8^8 = f_1^8 f_4^{28} + 8q f_1^8 f_2^4 f_4^{16} f_8^8 + 16q^2 f_1^8 f_2^8 f_4^4 f_8^{16},
$$



$$
f_2^{42} f_8^{12} = f_1^{12} f_4^{42} + 12q f_1^{12} f_2^4 f_4^{30} f_8^8 +
48q^2 f_1^{12} f_2^8 f_4^{18} f_8^{16} + 64q^3 f_1^{12} f_2^{12} f_4^6 f_8^{24}.
$$

Since each $f_k$ with $k \ge 1$ has constant term $1$ and is therefore invertible, dividing by
$f_1^4 f_2^{14} f_8^4$, $f_1^8 f_2^{28} f_8^8$ and $f_1^{12} f_2^{42} f_8^{12}$ respectively turns
these into the 2-dissections
$1/f_1^4 = f_4^{14}/(f_2^{14} f_8^4) + 4q f_4^2 f_8^4/f_2^{10}$,
$1/f_1^8 = f_4^{28}/(f_2^{28} f_8^8) + 8q f_4^{16}/f_2^{24} + 16q^2 f_4^4 f_8^8/f_2^{20}$ and
$1/f_1^{12} = f_4^{42}/(f_2^{42} f_8^{12}) + 12q f_4^{30}/(f_2^{38} f_8^4) +
48q^2 f_4^{18} f_8^4/f_2^{34} + 64q^3 f_4^6 f_8^{12}/f_2^{30}$.

## Sources

- Manjil P. Saikia and James A. Sellers, *Generalizing Recent Results of Kathiravan, Majumdar, Sangale, and Srinivas on `(ℓ, k)`-regular Partitions*, Journal of Integer Sequences 28 (2025), Article 25.6.1, Lemma 10 (`jis-2025-25.6.1-lem-10`).

Stated but not proved: `MetaMathlibExt.one_div_f1_pow_four_eight_twelve_two_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/k-regular-partitions/index.html#one-div-f1-pow-four-eight-twelve-two-dis).

## The 2-dissection of $1/(f_1 f_3)$

Write $f_k = (q^k; q^k)_\infty$ for the Euler
products. In the ring of integer power series in $q$,

$$
f_2^4 f_4 f_6^4 f_8^2 f_{12} f_{24}^2 =
f_1 f_3 f_2^2 f_8^4 f_{12}^6 + q f_1 f_3 f_4^6 f_6^2 f_{24}^4.
$$

Since each $f_k$ with $k \ge 1$ has constant term $1$ and is therefore invertible, this is the
identity $1 / (f_1 f_3) = f_8^2 f_{12}^5 / (f_2^2 f_4 f_6^4 f_{24}^2) +
q f_4^5 f_{24}^2 / (f_2^4 f_6^2 f_8^2 f_{12})$ with both sides multiplied by
$f_1 f_3 f_2^4 f_4 f_6^4 f_8^2 f_{12} f_{24}^2$.

## Sources

- Manjil P. Saikia and James A. Sellers, *Generalizing Recent Results of Kathiravan, Majumdar, Sangale, and Srinivas on `(ℓ, k)`-regular Partitions*, Journal of Integer Sequences 28 (2025), Article 25.6.1, Lemma 11 (`jis-2025-25.6.1-lem-11`).

Stated but not proved: `MetaMathlibExt.one_div_f1_f3_two_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/k-regular-partitions/index.html#one-div-f1-f3-two-dissection).

## Generating function of $b_{4,9}$ at odd arguments

Let $b_{4,9}(n)$ be the number of
partitions of $n$ with no part divisible by $4$ or by $9$, and write $f_k = (q^k; q^k)_\infty$
for the Euler products. In the ring of integer power series in $q$,

$$
f_1^3 f_6 \sum_{n \ge 0} b_{4,9}(2n + 1) q^n = f_2^3 f_3.
$$

Since $f_1$ and $f_6$ have constant term $1$ and are therefore invertible, this says
$\sum_{n \ge 0} b_{4,9}(2n + 1) q^n = f_2^3 f_3 / (f_1^3 f_6)$.

## Sources

- Manjil P. Saikia and James A. Sellers, *Generalizing Recent Results of Kathiravan, Majumdar, Sangale, and Srinivas on `(ℓ, k)`-regular Partitions*, Journal of Integer Sequences 28 (2025), Article 25.6.1, Theorem 12 (`jis-2025-25.6.1-thm-12`).

Stated but not proved: `MetaMathlibExt.regularPartitionCount_four_nine_odd_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/k-regular-partitions/index.html#regular-partition-count-four-nine-odd-ge).

## An internal congruence modulo $4$ for $b_{4,9}$

Let $b_{4,9}(n)$ be the number of
partitions of $n$ with no part divisible by $4$ or by $9$. For every natural number $n$,
$b_{4,9}(16n + 1) \equiv b_{4,9}(4n + 1) \pmod 4$.

## Sources

- Manjil P. Saikia and James A. Sellers, *Generalizing Recent Results of Kathiravan, Majumdar, Sangale, and Srinivas on `(ℓ, k)`-regular Partitions*, Journal of Integer Sequences 28 (2025), Article 25.6.1, Theorem 13 (`jis-2025-25.6.1-thm-13`).

Stated but not proved: `MetaMathlibExt.regularPartitionCount_four_nine_internal_mod_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/k-regular-partitions/index.html#regular-partition-count-four-nine-intern).

## $b_{4,9}(16n + 13)$ is divisible by $4$

Let $b_{4,9}(n)$ be the number of partitions of
$n$ with no part divisible by $4$ or by $9$. For every natural number $n$,
$b_{4,9}(16n + 13) \equiv 0 \pmod 4$.

## Sources

- Manjil P. Saikia and James A. Sellers, *Generalizing Recent Results of Kathiravan, Majumdar, Sangale, and Srinivas on `(ℓ, k)`-regular Partitions*, Journal of Integer Sequences 28 (2025), Article 25.6.1, Theorem 14 (`jis-2025-25.6.1-thm-14`).

Stated but not proved: `MetaMathlibExt.regularPartitionCount_four_nine_sixteen_mul_add_thirteen` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/k-regular-partitions/index.html#regular-partition-count-four-nine-sixtee).

## $b_{4,9}(32n + 25)$ is divisible by $4$

Let $b_{4,9}(n)$ be the number of partitions of
$n$ with no part divisible by $4$ or by $9$. For every natural number $n$,
$b_{4,9}(32n + 25) \equiv 0 \pmod 4$.

## Sources

- Manjil P. Saikia and James A. Sellers, *Generalizing Recent Results of Kathiravan, Majumdar, Sangale, and Srinivas on `(ℓ, k)`-regular Partitions*, Journal of Integer Sequences 28 (2025), Article 25.6.1, Theorem 15 (`jis-2025-25.6.1-thm-15`).

Stated but not proved: `MetaMathlibExt.regularPartitionCount_four_nine_thirtyTwo_mul_add_twentyFive` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/RegularPartitionsLKWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/k-regular-partitions/index.html#regular-partition-count-four-nine-thirty).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: (ℓ, k)-regular partitions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/k-regular-partitions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/k-regular-partitions)
