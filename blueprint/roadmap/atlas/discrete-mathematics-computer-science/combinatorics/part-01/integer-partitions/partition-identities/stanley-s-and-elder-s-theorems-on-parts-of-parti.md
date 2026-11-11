---
declaration: section
origin: cited
lean: MetaMathlibExt.sum_count_eq_sum_card_parts_count_ge, MetaMathlibExt.sum_count_one_eq_sum_card_toFinset, MetaMathlibExt.nColorPartsUpTo, MetaMathlibExt.mem_nColorPartsUpTo, MetaMathlibExt.multisetsWithSizeSum, MetaMathlibExt.mem_multisetsWithSizeSum, MetaMathlibExt.nColorPartitions, MetaMathlibExt.mem_nColorPartitions
statement: formalized
---

# Stanley's and Elder's theorems on parts of partitions

33 results, 10 proved and 23 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html).

## Elder's theorem

Let $n$ and $k$ be natural numbers with $k \ge 1$. The total number of
times the part $k$ occurs, counted with multiplicity, over all partitions of $n$ equals the sum,
over all partitions $\lambda$ of $n$, of the number of distinct parts of $\lambda$ that occur at
least $k$ times in $\lambda$.

The hypothesis $k \ge 1$ is needed: for $k = 0$ and $n = 1$ the left side is $0$ and the right
side is $1$.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Theorem 2 (Elder's theorem).

Stated but not proved: `MetaMathlibExt.sum_count_eq_sum_card_parts_count_ge` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#sum-count-eq-sum-card-parts-count-ge).

## Stanley's theorem

For every natural number $n$, the total number of parts equal to $1$,
counted with multiplicity, over all partitions of $n$ equals the sum, over all partitions
$\lambda$ of $n$, of the number of distinct parts of $\lambda$.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Theorem 1 (Stanley's theorem).

Stated but not proved: `MetaMathlibExt.sum_count_one_eq_sum_card_toFinset` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#sum-count-one-eq-sum-card-to-finset).

## The list of colored parts of size at most $m$

For $m \ge 0$, this is the list of the
colored parts $k_j$, that is, the pairs $(k, j)$ of natural numbers with $1 \le j \le k \le m$,
each listed once, in the order $1_1, 2_1, 2_2, 3_1, 3_2, 3_3, \dots$ (by size $k$, then by
color $j$).

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Section 1 (`n`-color partitions).

Formalized by `MetaMathlibExt.nColorPartsUpTo`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#n-color-parts-up-to).

## Membership in the colored parts of bounded size

For all natural numbers $m$, $k$ and
$j$, the pair $(k, j)$ appears in the list of colored parts of size at most $m$ if and only if
$1 \le j \le k \le m$.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Section 1 (`n`-color partitions).

Formalized by `MetaMathlibExt.mem_nColorPartsUpTo`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#mem-n-color-parts-up-to).

## Multisets of parts with a given size sum

For a list $L$ of pairs of natural numbers, where
the size of a pair $(k, j)$ is $k$, and a natural number $n$, this is the finite set of multisets
of pairs defined by recursion on $L$. For the empty list it is the set containing only the empty
multiset when $n = 0$, and the empty set otherwise. For a list with head $c$ of size $k$ and tail
$L'$, it is the set of all multisets obtained by adding $i$ copies of $c$ to a member of the set
for $L'$ and $n - ik$, where $i$ ranges over the natural numbers with $i \le n$ and $ik \le n$.

When every pair in $L$ has positive size, this is exactly the set of multisets whose elements all
lie in $L$ and whose sizes, counted with multiplicity, sum to $n$.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Section 1 (`n`-color partitions; helper for `C(m)`).

Formalized by `MetaMathlibExt.multisetsWithSizeSum`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#multisets-with-size-sum).

## Membership in the multisets with a given size sum

Let $L$ be a list of pairs of natural
numbers in which every pair $(k, j)$ has size $k \ge 1$, and let $n$ be a natural number. A
multiset $s$ of pairs belongs to the set of multisets drawn from $L$ with size sum $n$ if and only
if every element of $s$ lies in $L$ and the sizes of the elements of $s$, counted with
multiplicity, sum to $n$.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Section 1 (`n`-color partitions; helper for `C(m)`).

Formalized by `MetaMathlibExt.mem_multisetsWithSizeSum`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#mem-multisets-with-size-sum).

## n-color partitions

For a natural number $m$, the $n$-color partitions of $m$ form the
finite set of multisets of colored parts $k_j$, that is pairs $(k, j)$ of natural numbers with
$1 \le j \le k$ (a part of size $k$ comes in $k$ colors), whose sizes $k$, counted with
multiplicity, sum to $m$.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Section 1 (`n`-color partitions; `C(m)` is their number).

Formalized by `MetaMathlibExt.nColorPartitions`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#n-color-partitions).

## Characterization of $n$-color partitions

For every natural number $m$, a multiset $s$ of
pairs of natural numbers is an $n$-color partition of $m$ if and only if every element $(k, j)$ of
$s$ satisfies $1 \le j \le k$ and the sizes $k$ of the elements of $s$, counted with
multiplicity, sum to $m$.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Section 1 (`n`-color partitions).

Formalized by `MetaMathlibExt.mem_nColorPartitions`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#mem-n-color-partitions).

## Small values of the number of n-color partitions

Let $C(m)$ be the number of $n$-color
partitions of $m$, and write $k_j$ for the colored part of size $k$ and color $j$. Then
$C(0) = C(1) = 1$, $C(2) = 3$ and $C(3) = 6$, and the $n$-color partitions of $2$ are exactly
$2_1$, $2_2$ and $1_1 + 1_1$.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Section 1 (`C(m)`, generating function `∏_{m ≥ 1} (1 - q^m)^{-m}`).

Formalized by `MetaMathlibExt.nColorPartitions_card_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#n-color-partitions-card-small).

## Sum of odd divisors

For a natural number $k$, $\sigma_{\mathrm{odd}}(k)$ is the sum of
the odd positive divisors of $k$. By convention $\sigma_{\mathrm{odd}}(0) = 0$.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Corollaries 2, 4, 7, 10, 12 (`σ_odd`).

Formalized by `MetaMathlibExt.sigmaOdd`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#sigma-odd).

## Sum of the even divisors

For a natural number $k$, $\sigma_{\mathrm{even}}(k)$ is the
sum of the even divisors of $k$ (so $\sigma_{\mathrm{even}}(0) = 0$).

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Corollary 3 (`σ_even`).

Formalized by `MetaMathlibExt.sigmaEven`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#sigma-even).

## Odd and even divisor sums of 12 and 9

The sums of the odd and of the even divisors
of $12$ and $9$ are $\sigma_{\mathrm{odd}}(12) = 1 + 3 = 4$,
$\sigma_{\mathrm{even}}(12) = 2 + 4 + 6 + 12 = 24$, $\sigma_{\mathrm{odd}}(9) = 1 + 3 + 9 = 13$
and $\sigma_{\mathrm{even}}(9) = 0$.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Corollaries 3 and 4.

Formalized by `MetaMathlibExt.sigmaOdd_sigmaEven_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#sigma-odd-sigma-even-small).

## Total number of parts of $n$-color partitions via the divisor sum

For $r \ge 0$ let
$C(r)$ be the number of $n$-color partitions of $r$, and let $T_o(r)$ (resp. $T_e(r)$) be the
total number of parts, counted with multiplicity, over the $n$-color partitions of $r$ having an
odd (resp. even) number of parts. Then for every $m \ge 1$,

$$T_o(m) + T_e(m) = \sum_{k=1}^{m} \sigma(k)\, C(m-k),$$

where $\sigma(k)$ is the sum of the divisors of $k$.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Corollary 1.

Stated but not proved: `MetaMathlibExt.nColor_totalParts_eq_sum_sigma` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#n-color-total-parts-eq-sum-sigma).

## Odd-divisor sum via the total number of parts of $n$-color partitions

For $r \ge 0$
let $T_o(r)$ (resp. $T_e(r)$) be the total number of parts, counted with multiplicity, over the
$n$-color partitions of $r$ having an odd (resp. even) number of parts, and let $C(D, r)$ be the
number of $n$-color partitions of $r$ into distinct colored parts. Then for every $m \ge 1$,

$$\sigma_{\mathrm{odd}}(m) = \sum_{k=1}^{m} \bigl(T_o(k) - T_e(k)\bigr)\, C(D, m-k),$$

where $\sigma_{\mathrm{odd}}(m)$ is the sum of the odd divisors of $m$.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Corollary 2.

Stated but not proved: `MetaMathlibExt.sigmaOdd_eq_sum_nColor_partsDiff_mul_distinct` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#sigma-odd-eq-sum-n-color-parts-diff-mul).

## Even divisor sums count the even parts of $n$-color partitions

For $m \ge 1$, let
$A_e(m)$ be the total number of parts of even size, counted with multiplicity, over the
$n$-color partitions of $m$, and for $r \ge 0$ let $C(r)$ be the number of $n$-color partitions
of $r$. Then

$$A_e(m) = \sum_{k=1}^{m} \sigma_{\mathrm{even}}(k) \, C(m - k),$$

where $\sigma_{\mathrm{even}}(k)$ is the sum of the even divisors of $k$.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Corollary 3.

Stated but not proved: `MetaMathlibExt.nColor_evenParts_eq_sum_sigmaEven` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#n-color-even-parts-eq-sum-sigma-even).

## Number of odd parts in n-color partitions as a divisor sum

For $i \ge 0$ let $A_o(i)$ be
the total number of odd parts (parts of odd size, counted with multiplicity) over the $n$-color
partitions of $i$, and let $C(i)$ be the number of $n$-color partitions of $i$. Then for every
$m \ge 1$,

$$
A_o(m) = \sum_{k=1}^{m} \sigma_{\mathrm{odd}}(k)\, C(m-k),
$$

where $\sigma_{\mathrm{odd}}(k)$ is the sum of the odd divisors of $k$.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Corollary 4.

Stated but not proved: `MetaMathlibExt.nColor_oddParts_eq_sum_sigmaOdd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#n-color-odd-parts-eq-sum-sigma-odd).

## Parts of multiplicity at least t in n-color partitions

Let $t \ge 1$. For $i \ge 0$ let
$N^t(i)$ be the number of distinct colored parts occurring at least $t$ times in an $n$-color
partition of $i$, summed over all $n$-color partitions of $i$, and let $C(i)$ be the number of
$n$-color partitions of $i$. Then for every $m \ge t$,

$$
N^t(m) = \sum_{k=1}^{\lfloor m/t \rfloor} k\, C(m - tk).
$$

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Corollary 5.

Stated but not proved: `MetaMathlibExt.nColor_partsMultiplicityGe_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#n-color-parts-multiplicity-ge-eq-sum).

## Parts in a residue class over n-color partitions as a divisor sum

Let $r$ and $k$ be
natural numbers with $0 < k < r$. For $i \ge 0$ let $C(k \bmod r, i)$ be the total number of
parts of size congruent to $k$ modulo $r$, counted with multiplicity, over the $n$-color
partitions of $i$, and let $C(i)$ be the number of $n$-color partitions of $i$. Then for every
$m \ge 1$,

$$
C(k \bmod r, m) = \sum_{j=1}^{m} \Bigl(\sum_{d \mid j,\ d \equiv k \pmod{r}} d\Bigr) C(m-j).
$$

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Corollary 6.

Stated but not proved: `MetaMathlibExt.nColor_partsModEq_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#n-color-parts-mod-eq-eq-sum).

## Odd divisor sums count the parts of distinct $n$-color partitions

Call an $n$-color
partition distinct when no colored part occurs more than once. For $m \ge 1$, let $C_o(D, m)$
(resp. $C_e(D, m)$) be the total number of parts over the distinct $n$-color partitions of $m$
with an odd (resp. even) number of parts, and for $r \ge 0$ let $C(D, r)$ be the number of
distinct $n$-color partitions of $r$. Then

$$C_o(D, m) + C_e(D, m) = \sum_{k=1}^{m} \sigma_{\mathrm{odd}}(k) \, C(D, m - k),$$

where $\sigma_{\mathrm{odd}}(k)$ is the sum of the odd divisors of $k$.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Corollary 7.

Stated but not proved: `MetaMathlibExt.nColor_distinctTotalParts_eq_sum_sigmaOdd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#n-color-distinct-total-parts-eq-sum-sigm).

## Divisor sum via distinct $n$-color partitions

For $r \ge 0$ let $C(r)$ be the number
of $n$-color partitions of $r$, and let $C_o(D, r)$ (resp. $C_e(D, r)$) be the total number of
parts over the $n$-color partitions of $r$ into an odd (resp. even) number of distinct colored
parts. Then for every $m \ge 1$,

$$\sigma(m) = \sum_{k=1}^{m} \bigl(C_o(D, k) - C_e(D, k)\bigr)\, C(m-k),$$

where $\sigma(m)$ is the sum of the divisors of $m$.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Corollary 8.

Stated but not proved: `MetaMathlibExt.sigma_eq_sum_nColor_distinctPartsDiff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#sigma-eq-sum-n-color-distinct-parts-diff).

## Number of parts in n-color partitions into odd parts as a divisor sum

For $i \ge 0$ let
$Q(O, i)$ be the total number of parts, counted with multiplicity, over the $n$-color partitions
of $i$ into odd parts (every part has odd size), and let $C(O, i)$ be the number of such
partitions. Then for every $m \ge 1$,

$$
Q(O, m) = \sum_{k=1}^{m} \sigma_{\mathrm{odd}}(k)\, C(O, m-k),
$$

where $\sigma_{\mathrm{odd}}(k)$ is the sum of the odd divisors of $k$.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Corollary 10.

Stated but not proved: `MetaMathlibExt.nColor_oddPartitionParts_eq_sum_sigmaOdd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#n-color-odd-partition-parts-eq-sum-sigma).

## Odd divisor sums count the parts of $n$-color partitions into odd parts

Say that an
$n$-color partition has odd parts when every part has odd size. For $m \ge 1$, let $U_o(m)$
(resp. $U_e(m)$) be the total number of parts over the $n$-color partitions of $m$ with odd parts
and an odd (resp. even) number of parts, and for $r \ge 0$ let $C(O, r)$ be the number of
$n$-color partitions of $r$ with odd parts. Then

$$U_o(m) + U_e(m) = \sum_{k=1}^{m} \sigma_{\mathrm{odd}}(k) \, C(O, m - k),$$

where $\sigma_{\mathrm{odd}}(k)$ is the sum of the odd divisors of $k$.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Corollary 12.

Stated but not proved: `MetaMathlibExt.nColor_oddPartitionParts_byParity_eq_sum_sigmaOdd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#n-color-odd-partition-parts-by-parity-eq).

## Generating functions for the total number of parts of $n$-color partitions

For
$m \ge 0$ let $T_o(m)$ (resp. $T_e(m)$) be the total number of parts, counted with
multiplicity, over the $n$-color partitions of $m$ having an odd (resp. even) number of parts.
Then, as formal power series in $q$ with rational coefficients,

$$\sum_{m \ge 1} \frac{m q^m}{1 - q^m} =
\prod_{m \ge 1} (1 - q^m)^m \sum_{m \ge 0} \bigl(T_o(m) + T_e(m)\bigr) q^m$$

and

$$\sum_{m \ge 1} \frac{m q^m}{1 + q^m} =
\prod_{m \ge 1} (1 + q^m)^m \sum_{m \ge 0} \bigl(T_o(m) - T_e(m)\bigr) q^m.$$

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Theorem 3.

Stated but not proved: `MetaMathlibExt.nColor_totalParts_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#n-color-total-parts-generating-function).

## Generating function for the even parts of $n$-color partitions

Let $A_e(m)$ be the total
number of parts of even size, counted with multiplicity, over the $n$-color partitions of $m$.
Then, as formal power series in $q$ over $\mathbb{Q}$, with infinite sums and products taken
coefficientwise,

$$
\sum_{m \ge 1} \frac{2m \, q^{2m}}{1 - q^{2m}} =
\Big(\prod_{m \ge 1} (1 - q^m)^m\Big) \sum_{m \ge 0} A_e(m) \, q^m.
$$

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Theorem 4.

Stated but not proved: `MetaMathlibExt.nColor_evenParts_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#n-color-even-parts-generating-function).

## Generating function for the number of odd parts in n-color partitions

For $i \ge 0$ let
$A_o(i)$ be the total number of odd parts (parts of odd size, counted with multiplicity) over the
$n$-color partitions of $i$. Then in the ring $\mathbb{Q}[[q]]$ of formal power series, with
infinite sums and products taken coefficientwise,

$$
\sum_{m \ge 0} \frac{(2m+1)\,q^{2m+1}}{1 - q^{2m+1}} =
\prod_{m \ge 1} (1 - q^m)^m \sum_{i \ge 0} A_o(i)\, q^i.
$$

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Theorem 5.

Stated but not proved: `MetaMathlibExt.nColor_oddParts_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#n-color-odd-parts-generating-function).

## Generating function for colored parts of multiplicity at least $t$

Let $t \ge 1$. For
$m \ge 0$ let $N^t(m)$ be the sum, over all $n$-color partitions of $m$, of the number of
distinct colored parts that occur at least $t$ times. Then, as formal power series in $q$ with
rational coefficients,

$$\sum_{m \ge 1} m q^{mt} = \prod_{m \ge 1} (1 - q^m)^m \sum_{m \ge 0} N^t(m) q^m.$$

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Theorem 6.

Stated but not proved: `MetaMathlibExt.nColor_partsMultiplicityGe_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#n-color-parts-multiplicity-ge-generating).

## Generating function for parts in a residue class over n-color partitions

Let $r$ and
$k$ be natural numbers with $0 < k < r$, and for $i \ge 0$ let $C(k \bmod r, i)$ be the total
number of parts of size congruent to $k$ modulo $r$, counted with multiplicity, over the
$n$-color partitions of $i$. Then in the ring $\mathbb{Q}[[q]]$ of formal power series, with
infinite sums and products taken coefficientwise,

$$
\sum_{m \ge 0} \frac{(rm+k)\,q^{rm+k}}{1 - q^{rm+k}} =
\prod_{m \ge 1} (1 - q^m)^m \sum_{i \ge 0} C(k \bmod r, i)\, q^i.
$$

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Theorem 7.

Stated but not proved: `MetaMathlibExt.nColor_partsModEq_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 389](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L389). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#n-color-parts-mod-eq-generating-function).

## Generating functions for the parts of distinct $n$-color partitions

Call an $n$-color
partition distinct when no colored part occurs more than once, and let $C_o(D, m)$ (resp.
$C_e(D, m)$) be the total number of parts over the distinct $n$-color partitions of $m$ with an
odd (resp. even) number of parts. Then, as formal power series in $q$ over $\mathbb{Q}$, with
infinite sums and products taken coefficientwise, both

$$
\sum_{m \ge 1} \frac{m q^m}{1 + q^m} =
\Big(\prod_{m \ge 1} (1 + q^m)^m\Big)^{-1} \sum_{m \ge 0} \big(C_o(D, m) + C_e(D, m)\big) q^m
$$

and

$$
\sum_{m \ge 1} \frac{m q^m}{1 - q^m} =
\Big(\prod_{m \ge 1} (1 - q^m)^m\Big)^{-1} \sum_{m \ge 0} \big(C_o(D, m) - C_e(D, m)\big) q^m
$$

hold.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Theorem 8.

Stated but not proved: `MetaMathlibExt.nColor_distinctTotalParts_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#n-color-distinct-total-parts-generating).

## Odd-divisor sum via distinct $n$-color partitions and signed partition counts

For
$r \ge 0$ let $C_o(D, r)$ (resp. $C_e(D, r)$) be the total number of parts over the $n$-color
partitions of $r$ into an odd (resp. even) number of distinct colored parts, and let
$C_{e-o}(r) = \sum_\lambda (-1)^{\ell(\lambda)}$, the sum running over all $n$-color partitions
$\lambda$ of $r$, where $\ell(\lambda)$ is the number of parts of $\lambda$ counted with
multiplicity. Then for every $m \ge 1$,

$$\sigma_{\mathrm{odd}}(m) =
\sum_{k=1}^{m} \bigl(C_o(D, k) + C_e(D, k)\bigr)\, C_{e-o}(m-k),$$

where $\sigma_{\mathrm{odd}}(m)$ is the sum of the odd divisors of $m$.

This is the reading given by the paper's derivation from Theorem 8 and Eq. (3). As printed,
with the number $C(D, k)$ of $n$-color partitions of $k$ into distinct colored parts in place
of $C_o(D, k) + C_e(D, k)$, it fails at $m = 3$: $\sigma_{\mathrm{odd}}(3) = 4$, but
$\sum_{k=1}^{3} C(D, k)\, C_{e-o}(3-k) = 1 \cdot (-1) + 2 \cdot (-1) + 5 \cdot 1 = 2$.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Corollary 9.

Stated but not proved: `MetaMathlibExt.sigmaOdd_eq_sum_nColor_distinctTotalParts_mul_signed` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#sigma-odd-eq-sum-n-color-distinct-total).

## Generating function for the number of parts in n-color partitions into odd parts

For
$i \ge 0$ let $Q(O, i)$ be the total number of parts, counted with multiplicity, over the
$n$-color partitions of $i$ into odd parts (every part has odd size). Then in the ring
$\mathbb{Q}[[q]]$ of formal power series, with infinite sums and products taken coefficientwise,

$$
\sum_{m \ge 0} \frac{(2m+1)\,q^{2m+1}}{1 - q^{2m+1}} =
\prod_{m \ge 0} (1 - q^{2m+1})^{2m+1} \sum_{i \ge 0} Q(O, i)\, q^i.
$$

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Theorem 9.

Stated but not proved: `MetaMathlibExt.nColor_oddPartitionParts_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 435](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L435). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#n-color-odd-partition-parts-generating-f).

## Generating function for parts of a given size in distinct $n$-color partitions

Call an
$n$-color partition distinct when no colored part occurs more than once. For a natural number
$j$, let $Q(D, j, m)$ be the total number of parts of size $j$ (of any color) over the distinct
$n$-color partitions of $m$, and let $C(D, m)$ be the number of distinct $n$-color partitions of
$m$. Then, as formal power series in $q$ over $\mathbb{Q}$,

$$\sum_{m \ge 0} Q(D, j, m) \, q^m = \frac{j q^j}{1 + q^j} \sum_{m \ge 0} C(D, m) \, q^m.$$

The paper assumes $j \ge 1$; for $j = 0$ both sides vanish.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Theorem 11.

Stated but not proved: `MetaMathlibExt.nColor_distinctPartsCountOf_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 448](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L448). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#n-color-distinct-parts-count-of-generati).

## Parts of n-color partitions into odd parts, by parity of the number of parts

For
$i \ge 0$ let $U_o(i)$ (resp. $U_e(i)$) be the total number of parts, counted with multiplicity,
over the $n$-color partitions of $i$ into odd parts (every part has odd size) that have an odd
(resp. even) number of parts. Then in the ring $\mathbb{Q}[[q]]$ of formal power series, with
infinite sums and products taken coefficientwise,

$$
\sum_{m \ge 0} \frac{(2m+1)\,q^{2m+1}}{1 - q^{2m+1}} =
\prod_{m \ge 0} (1 - q^{2m+1})^{2m+1} \sum_{i \ge 0} \bigl(U_o(i) + U_e(i)\bigr) q^i
$$

and

$$
\sum_{m \ge 0} \frac{(2m+1)\,q^{2m+1}}{1 + q^{2m+1}} =
\prod_{m \ge 0} (1 + q^{2m+1})^{2m+1} \sum_{i \ge 0} \bigl(U_o(i) - U_e(i)\bigr) q^i.
$$

The paper's printed definition swaps the subscripts ($U_e$ for an odd number of parts); with it
the second identity fails at $q^1$: the left side has coefficient $1$, the right side
$U_o(1) - U_e(1) = 0 - 1 = -1$.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Theorem 12.

Stated but not proved: `MetaMathlibExt.nColor_oddPartitionParts_byParity_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 465](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L465). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#n-color-odd-partition-parts-by-parity-ge).

## Signed odd-divisor sum via $n$-color partitions into odd parts

For $r \ge 0$ let
$U_o(r)$ (resp. $U_e(r)$) be the total number of parts, counted with multiplicity, over the
$n$-color partitions of $r$ in which every part has odd size and the number of parts is odd
(resp. even), and let $C(O, D, r)$ be the number of $n$-color partitions of $r$ into distinct
colored parts all of odd size. Then for every $m \ge 1$,

$$(-1)^{m+1} \sigma_{\mathrm{odd}}(m) =
\sum_{k=1}^{m} \bigl(U_o(k) - U_e(k)\bigr)\, C(O, D, m-k),$$

where $\sigma_{\mathrm{odd}}(m)$ is the sum of the odd divisors of $m$.

The subscripts of $U_o$ and $U_e$ give the parity of the number of parts. With the printed
(swapped) definition of $U_o$ and $U_e$ the identity fails at $m = 1$: the left side is $1$
and the right side is $(0 - 1) \cdot 1 = -1$.

## Sources

- Shruti Sharma and Amandeep Kaur, *Enumerating Parts of n-Color Partitions*, INTEGERS 25 (2025), Article A94, Corollary 13.

Stated but not proved: `MetaMathlibExt.neg_one_pow_mul_sigmaOdd_eq_sum_nColor_oddPartsDiff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean, line 489](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/StanleyElderPartsWanted.lean#L489). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html#neg-one-pow-mul-sigma-odd-eq-sum-n-color).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stanley's and Elder's theorems on parts of partitions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-partitions/partition-identities/stanley-s-and-elder-s-theorems-on-parts-of-parti)
