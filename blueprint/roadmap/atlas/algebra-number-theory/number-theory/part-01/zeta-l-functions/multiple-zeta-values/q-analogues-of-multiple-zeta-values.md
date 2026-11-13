---
declaration: section
origin: cited
lean: MetaMathlibExt.szQMZVPartial, MetaMathlibExt.szQMZV, MetaMathlibExt.szQMZV_nil, MetaMathlibExt.szQMZVPartial_cons, MetaMathlibExt.coeff_zero_szQMZV_cons, MetaMathlibExt.coeff_one_szQMZV_singleton_one, MetaMathlibExt.szBlockIndex, MetaMathlibExt.szBlockIndex_nil
statement: formalized
---

# q-analogues of multiple zeta values

132 results, 93 proved and 39 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/index.html).

## Partial sums of Schlesinger–Zudilin qMZVs

For an index $(k_1, \dots, k_r)$ of natural
numbers and a natural number $M$, the partial sum is the formal power series in $q$ over
$\mathbb{Q}$

$$\sum_{M > m_1 > \dots > m_r > 0} \prod_{j=1}^{r} \frac{q^{m_j k_j}}{(1 - q^{m_j})^{k_j}},$$

where the sum runs over integers $m_1, \dots, m_r$ and $1/(1 - q^m)$ is the inverse in
$\mathbb{Q}[[q]]$. For the empty index it equals $1$ for every $M$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of Schlesinger–Zudilin qMZVs (defining sum truncated at `m₁ < M`).

Formalized by `MetaMathlibExt.szQMZVPartial`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-01/index.html#sz-qmzvpartial).

## Schlesinger–Zudilin qMZVs

For an index $k = (k_1, \dots, k_r)$ of natural numbers, the
Schlesinger–Zudilin qMZV $\zeta_q^{SZ}(k)$ is the formal power series in $q$ over $\mathbb{Q}$
whose coefficient of $q^N$, for each $N \ge 0$, is the coefficient of $q^N$ in the partial sum

$$\sum_{N \ge m_1 > \dots > m_r > 0} \prod_{j=1}^{r} \frac{q^{m_j k_j}}{(1 - q^{m_j})^{k_j}}$$

over integers $m_1, \dots, m_r$. In particular $\zeta_q^{SZ}(\emptyset) = 1$.

When the index is empty or $k_1 \ge 1$, the summands with $m_1 > N$ have no term of degree at
most $N$, so $\zeta_q^{SZ}(k)$ is the full series
$\sum_{m_1 > \dots > m_r > 0} \prod_{j} q^{m_j k_j} / (1 - q^{m_j})^{k_j}$. The paper does not
define the value when $k_1 = 0$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of Schlesinger–Zudilin qMZVs (extended version of Ebrahimi-Fard, Manchon and Singer, allowing `kⱼ = 0` for `j ≥ 2`).

Formalized by `MetaMathlibExt.szQMZV`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-01/index.html#sz-qmzv).

## The empty Schlesinger–Zudilin qMZV

The Schlesinger–Zudilin qMZV of the empty index is
$1$: $\zeta_q^{SZ}(\emptyset) = 1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of Schlesinger–Zudilin qMZVs.

Formalized by `MetaMathlibExt.szQMZV_nil`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-01/index.html#sz-qmzv-nil).

## Recursion for partial sums of Schlesinger–Zudilin qMZVs

For natural numbers $k_1$ and
$M$ and an index $\kappa = (k_2, \dots, k_r)$ (possibly empty), write $Z_M(k_1, \kappa)$ and
$Z_m(\kappa)$ for the partial sums of Schlesinger–Zudilin qMZVs with bounds $M$ and $m$. Then

$$Z_M(k_1, \kappa) = \sum_{0 < m < M} \left(\frac{q^m}{1 - q^m}\right)^{k_1} Z_m(\kappa).$$

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of Schlesinger–Zudilin qMZVs.

Formalized by `MetaMathlibExt.szQMZVPartial_cons`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-01/index.html#sz-qmzvpartial-cons).

## Nonempty Schlesinger–Zudilin qMZVs have no constant term

For every nonempty index
$(k_1, \dots, k_r)$ of natural numbers, the constant term of the Schlesinger–Zudilin qMZV
$\zeta_q^{\mathrm{SZ}}(k_1, \dots, k_r)$ is $0$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of Schlesinger–Zudilin qMZVs.

Formalized by `MetaMathlibExt.coeff_zero_szQMZV_cons`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-01/index.html#coeff-zero-sz-qmzv-cons).

## The coefficient of $q$ in $\zeta_q^{\mathrm{SZ}}(1)$

The coefficient of $q$ in the
Schlesinger–Zudilin qMZV $\zeta_q^{\mathrm{SZ}}(1) = \sum_{m > 0} q^m / (1 - q^m)$ is $1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of Schlesinger–Zudilin qMZVs.

Formalized by `MetaMathlibExt.coeff_one_szQMZV_singleton_one`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-01/index.html#coeff-one-sz-qmzv-singleton-one).

## Block indices for Schlesinger–Zudilin qMZVs

For a list of pairs of natural numbers
$(k_1, d_1), \dots, (k_r, d_r)$, the block index is the index
$(k_1, \{0\}^{d_1 - 1}, \dots, k_r, \{0\}^{d_r - 1})$ obtained by concatenating, for
$j = 1, \dots, r$, the entry $k_j$ followed by $d_j - 1$ zeros (no zeros when $d_j = 0$).

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 4 and Theorem 5 (SZ duality), index notation.

Formalized by `MetaMathlibExt.szBlockIndex`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-01/index.html#sz-block-index).

## Block index of the empty list

The block index of the empty list of pairs is the empty
index.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 5, index notation.

Formalized by `MetaMathlibExt.szBlockIndex_nil`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-01/index.html#sz-block-index-nil).

## Recursion for block indices

For natural numbers $k$, $d$ and a list $L$ of pairs of
natural numbers, the block index of the list with first pair $(k, d)$ followed by $L$ is $k$,
followed by $d - 1$ zeros (none when $d = 0$), followed by the block index of $L$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 5, index notation.

Formalized by `MetaMathlibExt.szBlockIndex_cons`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-01/index.html#sz-block-index-cons).

## Partial Ohno–Okuda–Zudilin sums

For an index $(k_1, \dots, k_r)$ of natural numbers and a
natural number $M$, the partial OOZ sum is the formal power series in $q$ over $\mathbb{Q}$

$$\sum_{M > m_1 > \dots > m_r > 0} \prod_{j=1}^{r} \frac{1}{(1 - q^{m_j})^{k_j}},$$

the defining sum of $\zeta_q^{\mathrm{OOZ}}(k_1, \dots, k_r)$ with the factor $q^{m_1}$ removed and
truncated to $m_1 < M$. For the empty index it is $1$, for every $M$ (including $M = 0$).

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of OOZ-qMZVs (inner sums of the defining series).

Formalized by `MetaMathlibExt.oozQMZVPartial`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-01/index.html#ooz-qmzvpartial).

## Ohno–Okuda–Zudilin q-multiple zeta values

For an index $(k_1, \dots, k_r)$ of natural
numbers with $r \ge 1$, the (extended) Ohno–Okuda–Zudilin qMZV is the formal power series in $q$
over $\mathbb{Q}$

$$\zeta_q^{\mathrm{OOZ}}(k_1, \dots, k_r) = \sum_{m_1 > \dots > m_r > 0}
\frac{q^{m_1}}{(1 - q^{m_1})^{k_1} \cdots (1 - q^{m_r})^{k_r}},$$

and $\zeta_q^{\mathrm{OOZ}}(\varnothing) = 1$ for the empty index. The summands with $m_1 > N$
have $q$-adic order greater than $N$, so the coefficient of $q^N$ is computed from the finitely
many summands with $m_1 \le N$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of OOZ-qMZVs (extended version, `k₁ ≥ 1`, `kᵢ ≥ 0`).

Formalized by `MetaMathlibExt.oozQMZV`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-01/index.html#ooz-qmzv).

## The OOZ-qMZV of the empty index

The Ohno–Okuda–Zudilin qMZV of the empty index is $1$:
$\zeta_q^{\mathrm{OOZ}}(\varnothing) = 1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of OOZ-qMZVs.

Formalized by `MetaMathlibExt.oozQMZV_nil`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-01/index.html#ooz-qmzv-nil).

## Nonempty Ohno–Okuda–Zudilin qMZVs have no constant term

For every nonempty index
$(k_1, \dots, k_r)$ of natural numbers, the constant term of the Ohno–Okuda–Zudilin qMZV
$\zeta_q^{\mathrm{OOZ}}(k_1, \dots, k_r)$ is $0$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of OOZ-qMZVs.

Formalized by `MetaMathlibExt.coeff_zero_oozQMZV_cons`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-01/index.html#coeff-zero-ooz-qmzv-cons).

## Coefficients of Schlesinger–Zudilin qMZVs as sums of binomial products

Let $r \ge 0$,
and let $k_1, \dots, k_r$ and $d_1, \dots, d_r$ be positive integers. For every natural number
$N$, the coefficient of $q^N$ in the Schlesinger–Zudilin qMZV
$\zeta_q^{\mathrm{SZ}}(k_1, \{0\}^{d_1 - 1}, \dots, k_r, \{0\}^{d_r - 1})$, whose index lists each
$k_j$ followed by $d_j - 1$ zeros, equals

$$\sum \prod_{j=1}^{r} \binom{n_j - 1}{k_j - 1} \binom{m_j - m_{j+1} - 1}{d_j - 1},$$

where the sum runs over all integers $m_1 > \dots > m_r > 0$ and $n_1, \dots, n_r \ge 1$ with
$m_1 n_1 + \dots + m_r n_r = N$, and where $m_{r+1} = 0$.

These are the coefficients of $X_1^{k_1 - 1} \cdots X_r^{k_r - 1} Y_1^{d_1 - 1} \cdots
Y_r^{d_r - 1} q^N$ on both sides of the paper's identity expressing the generating series
$s(X; Y)$ of these qMZVs as
$\sum \prod_j (1 + X_j)^{n_j - 1} (1 + Y_j)^{m_j - m_{j+1} - 1} q^{m_j n_j}$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 4.

Stated but not proved: `MetaMathlibExt.coeff_szQMZV_szBlockIndex_eq_sum_choose` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-01/index.html#coeff-sz-qmzv-sz-block-index-eq-sum-choo).

## Schlesinger–Zudilin duality

Let $\zeta_q^{SZ}$ denote the Schlesinger–Zudilin qMZV, let
$(k_1, d_1), \dots, (k_r, d_r)$ be pairs of natural numbers with $k_j \ge 1$ and $d_j \ge 1$
for all $j$, and let $\{0\}^n$ denote $n$ zeros. Then

$$\zeta_q^{SZ}(k_1, \{0\}^{d_1 - 1}, \dots, k_r, \{0\}^{d_r - 1}) =
\zeta_q^{SZ}(d_r, \{0\}^{k_r - 1}, \dots, d_1, \{0\}^{k_1 - 1}).$$

That is, $\zeta_q^{SZ}$ takes the same value at the block index of the list of pairs and at
the block index of the reversed list with each pair swapped.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 5 (SZ duality, Zhao).

Stated but not proved: `MetaMathlibExt.szQMZV_szBlockIndex_dual` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-01/index.html#sz-qmzv-sz-block-index-dual).

## Partitions from Schlesinger–Zudilin qMZVs

Let $\zeta_q^{SZ}$ denote the
Schlesinger–Zudilin qMZV, $\{1\}^r$ the index of $r$ ones and $p(N)$ the number of
partitions of $N$. For all natural numbers $N \ge 1$ and $R \ge N$, the coefficient of $q^N$ in
$\sum_{r=1}^{R} \zeta_q^{SZ}(\{1\}^r)$ equals $p(N)$.

Since the summands with $r > N$ have no $q^N$ term, this is the coefficientwise form of
$\sum_{r \ge 1} \zeta_q^{SZ}(\{1\}^r) = \sum_{N \ge 1} p(N) q^N$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Lemma 3.

Stated but not proved: `MetaMathlibExt.sum_coeff_szQMZV_replicate_one_eq_card_partition` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-01/index.html#sum-coeff-sz-qmzv-replicate-one-eq-card).

## Cycle type classifies conjugacy classes of permutations

For every natural number $n$,
there is a bijection from the set of conjugacy classes of the symmetric group $S_n$ to the set
of partitions of $n$ that sends the class of each permutation $\sigma$ to the cycle type of
$\sigma$: the partition of $n$ formed by the lengths of the cycles of $\sigma$, fixed points
counting as cycles of length $1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Lemma 4.

Stated but not proved: `MetaMathlibExt.exists_conjClasses_perm_equiv_partition` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-01/index.html#exists-conj-classes-perm-equiv-partition).

## Number of conjugacy classes of the symmetric group

For every natural number $n$, the
number of conjugacy classes of the symmetric group $S_n$ equals the number $p(n)$ of partitions
of $n$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Lemma 4.

Stated but not proved: `MetaMathlibExt.card_conjClasses_perm_eq_card_partition` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-01/index.html#card-conj-classes-perm-eq-card-partition).

## Class numbers of finite general linear groups via OOZ-qMZVs

Let $K$ be a finite field
with $c$ elements and, for $n \ge 0$, let $a_{n,K}$ be the number of conjugacy classes of
$\mathrm{GL}_n(K)$, so that $a_{0,K} = 1$ because $\mathrm{GL}_0(K)$ is the trivial group. Write
$\{1\}^r$ for the index consisting of $r$ ones and $\zeta_q^{\mathrm{OOZ}}$ for the
Ohno–Okuda–Zudilin qMZV. Then for all natural numbers $N \le R$, $a_{N,K}$ equals the coefficient
of $q^N$ in $\sum_{r=0}^{R} (c - 1)^r \zeta_q^{\mathrm{OOZ}}(\{1\}^r)$.

Since the summands with $r > N$ have no $q^N$ term, this is the identity of formal power series
$\sum_{n \ge 0} a_{n,K} q^n = \sum_{r \ge 0} (c - 1)^r \zeta_q^{\mathrm{OOZ}}(\{1\}^r)$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 20.

Stated but not proved: `MetaMathlibExt.card_conjClasses_GL_eq_coeff_sum_oozQMZV` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-01/index.html#card-conj-classes-gl-eq-coeff-sum-ooz-qm).

## Partial sums of general qMZVs

Let $(k_1, Q_1), \dots, (k_r, Q_r)$ be pairs of natural
numbers $k_j$ and polynomials $Q_j \in \mathbb{Q}[X]$, and let $M$ be a natural number. The
partial sum is the formal power series in $q$ over $\mathbb{Q}$

$$\sum_{M > m_1 > \dots > m_r > 0} \prod_{j=1}^{r} \frac{Q_j(q^{m_j})}{(1 - q^{m_j})^{k_j}},$$

where the sum runs over integers $m_1, \dots, m_r$ and $1/(1 - q^m)$ is the inverse in
$\mathbb{Q}[[q]]$. For $r = 0$ it equals $1$ for every $M$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of qMZVs (after Bachmann–Kühn), defining sum truncated at `m₁ < M`.

Formalized by `MetaMathlibExt.qMZVPartial`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-01/index.html#q-mzvpartial).

## General q-multiple zeta values

For natural numbers $k_1, \dots, k_r$ and polynomials
$Q_1, \dots, Q_r \in \mathbb{Q}[X]$, the general qMZV $\zeta_q(k_1, \dots, k_r; Q_1, \dots, Q_r)$
is the formal power series in $q$ over $\mathbb{Q}$ whose coefficient of $q^N$, for every $N$, is
the coefficient of $q^N$ in the finite sum
$\sum_{N \ge m_1 > m_2 > \dots > m_r > 0} \prod_{j=1}^{r} Q_j(q^{m_j}) / (1 - q^{m_j})^{k_j}$
over integers $m_1, \dots, m_r$, and $\zeta_q(\varnothing; \varnothing) = 1$.

When $Q_1(0) = 0$ (the paper's condition $Q_1 \in X \mathbb{Q}[X]$), the summands with
$m_1 > N$ have $q$-adic order greater than $N$, so this is the series
$\sum_{m_1 > \dots > m_r > 0} \prod_{j=1}^{r} Q_j(q^{m_j}) / (1 - q^{m_j})^{k_j}$; for other data
the value is a junk value.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of qMZVs (after Bachmann–Kühn).

Formalized by `MetaMathlibExt.qMZV`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-02/index.html#q-mzv).

## General qMZV of the empty index

The general q-multiple zeta value of the empty data is
$\zeta_q(\varnothing; \varnothing) = 1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of qMZVs.

Formalized by `MetaMathlibExt.qMZV_nil`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-02/index.html#q-mzv-nil).

## Nonempty general qMZVs have no constant term

For every nonempty list
$(k_1, Q_1), \dots, (k_r, Q_r)$ of natural numbers $k_j$ and polynomials $Q_j \in \mathbb{Q}[X]$,
the constant coefficient of the general q-multiple zeta value
$\zeta_q(k_1, \dots, k_r; Q_1, \dots, Q_r)$ is $0$. No condition on $Q_1(0)$ is assumed.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of qMZVs.

Formalized by `MetaMathlibExt.coeff_zero_qMZV_cons`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-02/index.html#coeff-zero-q-mzv-cons).

## Spaces of general qMZVs

For a natural number $d$, $\mathcal{Z}_{q,d}$ is the
$\mathbb{Q}$-subspace of the formal power series $\mathbb{Q}[[q]]$ spanned by the general qMZVs
$\zeta_q(k_1, \dots, k_r; Q_1, \dots, Q_r)$ over all $r \ge 0$, natural numbers $k_1, \dots, k_r$
and polynomials $Q_1, \dots, Q_r \in \mathbb{Q}[X]$ with $\deg Q_j + d \le k_j$ for every $j$
(the zero polynomial counting as degree $0$) and $Q_1(0) = 0$ when $r \ge 1$.

The space $\mathcal{Z}_q := \mathcal{Z}_{q,0}$ is the space of qMZVs (with $k_j \ge 0$); for
$d = 1$ the degree condition forces $k_j \ge 1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of qMZVs (ii) and Definition of `𝒵_{q,d}` (after Bachmann–Kühn).

Formalized by `MetaMathlibExt.qMZVSpace`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-02/index.html#q-mzvspace).

## The constant series one lies in every space of qMZVs

For every natural number $d$, the
constant power series $1$ lies in the $\mathbb{Q}$-span $\mathcal{Z}_{q,d}$ of the general
q-multiple zeta values $\zeta_q(k_1, \dots, k_r; Q_1, \dots, Q_r)$ with $Q_1(0) = 0$ and
$\deg Q_j + d \le k_j$ for all $j$, where the zero polynomial is given degree $0$; it is the
qMZV of the empty index.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of qMZVs (ii).

Formalized by `MetaMathlibExt.one_mem_qMZVSpace`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-02/index.html#one-mem-q-mzvspace).

## Bradley–Zhao q-multiple zeta values

For an index $k = (k_1, \dots, k_r)$ of natural
numbers, the Bradley–Zhao q-multiple zeta value is the general qMZV
$\zeta_q^{BZ}(k) = \zeta_q(k_1, \dots, k_r; X^{k_1 - 1}, \dots, X^{k_r - 1})$, a formal power
series in $q$ over $\mathbb{Q}$, where $k_j - 1$ is truncated at $0$. For an admissible index
($k_1 \ge 2$ and all $k_i \ge 1$) it equals

$$\zeta_q^{BZ}(k) = \sum_{m_1 > \dots > m_r > 0} \prod_{j=1}^{r}
\frac{q^{m_j (k_j - 1)}}{(1 - q^{m_j})^{k_j}};$$

for other indices the value has no intended meaning.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of Bradley–Zhao qMZVs.

Formalized by `MetaMathlibExt.bzQMZV`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-02/index.html#bz-qmzv).

## Bradley–Zhao qMZV of the empty index

The Bradley–Zhao q-multiple zeta value of the
empty index is $\zeta_q^{BZ}(\varnothing) = 1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of Bradley–Zhao qMZVs.

Formalized by `MetaMathlibExt.bzQMZV_nil`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-02/index.html#bz-qmzv-nil).

## Nonempty Bradley–Zhao qMZVs have no constant term

For every nonempty index
$(k_1, \dots, k_r)$ of natural numbers, the constant coefficient of the Bradley–Zhao
q-multiple zeta value $\zeta_q^{BZ}(k_1, \dots, k_r)$ is $0$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of Bradley–Zhao qMZVs.

Formalized by `MetaMathlibExt.coeff_zero_bzQMZV_cons`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-02/index.html#coeff-zero-bz-qmzv-cons).

## Block index of a list of pairs

The block index of a list
$[(a_1, b_1), \dots, (a_r, b_r)]$ of pairs of natural numbers is the index
$(a_1 + 1, \{1\}^{b_1 - 1}, \dots, a_r + 1, \{1\}^{b_r - 1})$, where $\{1\}^n$ stands for $n$
consecutive entries equal to $1$ and $b_j - 1$ is truncated at $0$.

When all $a_j, b_j \ge 1$ this is an admissible index; it corresponds to the word
$x^{a_1} y^{b_1} \cdots x^{a_r} y^{b_r}$ of the space $\mathfrak{h}^0$ of admissible words in
the letters $x, y$, and the duality $\tau$, the anti-automorphism of
$\mathbb{Q}\langle x, y \rangle$ exchanging $x$ and $y$, maps this word to the word of the block
index of $[(b_r, a_r), \dots, (b_1, a_1)]$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 6 and Theorem 7 (BZ duality), index notation.

Formalized by `MetaMathlibExt.bzBlockIndex`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-02/index.html#bz-block-index).

## Block index of a prepended pair

For natural numbers $a, b$ and a list $L$ of pairs of
natural numbers, the block index of the list obtained by prepending $(a, b)$ to $L$ consists of
the entry $a + 1$, followed by $b - 1$ entries equal to $1$ (none when $b = 0$), followed by the
block index of $L$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 7, index notation.

Formalized by `MetaMathlibExt.bzBlockIndex_cons`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-02/index.html#bz-block-index-cons).

## Spanning set of Schlesinger–Zudilin qMZVs

Let $\mathcal{Z}_q$ be the space
$\mathcal{Z}_{q,d}$ of general qMZVs for $d = 0$. Then $\mathcal{Z}_q$ is the $\mathbb{Q}$-span of
the Schlesinger–Zudilin qMZVs $\zeta_q^{\mathrm{SZ}}(k_1, \dots, k_r)$ over all indices of natural
numbers with $k_1 \ge 1$ when $r \ge 1$ (including the empty index, with
$\zeta_q^{\mathrm{SZ}}(\varnothing) = 1$). Moreover, $\mathcal{Z}_q$ is closed under the operator
$q \frac{d}{dq}$: for every $f \in \mathcal{Z}_q$, the series $q f'$ lies in $\mathcal{Z}_q$, where
$f'$ is the formal derivative of $f$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 3.

Stated but not proved: `MetaMathlibExt.qMZVSpace_zero_eq_span_szQMZV` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-02/index.html#q-mzvspace-zero-eq-span-sz-qmzv).

## Spanning set of Bradley–Zhao qMZVs

Let $\mathcal{Z}_{q,1}$ be the space
$\mathcal{Z}_{q,d}$ of general qMZVs for $d = 1$. Then $\mathcal{Z}_{q,1}$ is the
$\mathbb{Q}$-span of the Bradley–Zhao qMZVs $\zeta_q^{\mathrm{BZ}}(k_1, \dots, k_r)$ over all
admissible indices, that is, all indices of natural numbers with $k_i \ge 1$ for every $i$ and
$k_1 \ge 2$ when $r \ge 1$ (including the empty index, with
$\zeta_q^{\mathrm{BZ}}(\varnothing) = 1$).

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 4.

Stated but not proved: `MetaMathlibExt.qMZVSpace_one_eq_span_bzQMZV` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-02/index.html#q-mzvspace-one-eq-span-bz-qmzv).

## Spanning sets of Ohno–Okuda–Zudilin qMZVs

Let $\mathcal{Z}_{q,1}$ and $\mathcal{Z}_q$ be
the spaces $\mathcal{Z}_{q,d}$ of general qMZVs for $d = 1$ and $d = 0$. Then (i)
$\mathcal{Z}_{q,1}$ is the $\mathbb{Q}$-span of the Ohno–Okuda–Zudilin qMZVs
$\zeta_q^{\mathrm{OOZ}}(k_1, \dots, k_r)$ over all indices of natural numbers with $k_i \ge 1$ for
every $i$ and $k_1 \ge 2$ when $r \ge 1$; and (ii) $\mathcal{Z}_q$ is the $\mathbb{Q}$-span of the
$\zeta_q^{\mathrm{OOZ}}(k_1, \dots, k_r)$ over all indices of natural numbers with $k_1 \ge 1$
when $r \ge 1$. Both spanning sets contain the empty index, with
$\zeta_q^{\mathrm{OOZ}}(\varnothing) = 1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 10.

Stated but not proved: `MetaMathlibExt.qMZVSpace_eq_span_oozQMZV` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-02/index.html#q-mzvspace-eq-span-ooz-qmzv).

## Bradley–Zhao duality for q-multiple zeta values

For every $r \ge 0$ and all natural
numbers $a_1, b_1, \dots, a_r, b_r \ge 1$, the Bradley–Zhao q-multiple zeta values satisfy

$$\zeta_q^{BZ}(a_1 + 1, \{1\}^{b_1 - 1}, \dots, a_r + 1, \{1\}^{b_r - 1}) =
\zeta_q^{BZ}(b_r + 1, \{1\}^{a_r - 1}, \dots, b_1 + 1, \{1\}^{a_1 - 1}),$$

where $\{1\}^n$ stands for $n$ consecutive entries equal to $1$.

In terms of words this is $\zeta_q^{BZ} \circ \tau = \zeta_q^{BZ}$ on the space $\mathfrak{h}^0$ of
admissible words, where $\tau$ is the anti-automorphism of $\mathbb{Q}\langle x, y \rangle$
exchanging $x$ and $y$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 7 (BZ duality, Bradley; Seki–Yamamoto).

Stated but not proved: `MetaMathlibExt.bzQMZV_bzBlockIndex_dual` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 374](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-02/index.html#bz-qmzv-bz-block-index-dual).

## q-Ohno relations for Bradley–Zhao qMZVs

Let $(a_1, b_1), \dots, (a_r, b_r)$ be pairs of
positive integers, write $\{1\}^{n}$ for $n$ repetitions of $1$, let
$\mathbf{k} = (a_1 + 1, \{1\}^{b_1 - 1}, \dots, a_r + 1, \{1\}^{b_r - 1})$ be the admissible
index they determine, of depth $\ell$, and let
$\mathbf{k}^\vee = (b_r + 1, \{1\}^{a_r - 1}, \dots, b_1 + 1, \{1\}^{a_1 - 1})$ be its dual, of
depth $\ell^\vee$. Then for every natural number $c$,
$\sum_{\mathbf{c}} \zeta_q^{\mathrm{BZ}}(\mathbf{k} + \mathbf{c}) =
\sum_{\mathbf{c}'} \zeta_q^{\mathrm{BZ}}(\mathbf{k}^\vee + \mathbf{c}')$, where $\mathbf{c}$ runs
over the tuples in $\mathbb{N}^{\ell}$ and $\mathbf{c}'$ over the tuples in $\mathbb{N}^{\ell^\vee}$
whose entries sum to $c$, and indices are added componentwise.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 8 (q-Ohno relations, Okuda–Takeyama).

Stated but not proved: `MetaMathlibExt.sum_bzQMZV_add_eq_sum_bzQMZV_dual_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-02/index.html#sum-bz-qmzv-add-eq-sum-bz-qmzv-dual-add).

## Partitions in Stanley coordinates

For natural numbers $r$ and $N$, $\mathcal{P}_r(N)$ is
the finite set of partitions of $N$ of length $r$ in Stanley coordinates: the pairs of tuples
$((m_1, \dots, m_r), (n_1, \dots, n_r))$ of positive integers with $m_1 > m_2 > \dots > m_r$ and
$m_1 n_1 + \dots + m_r n_r = N$.

All coordinates of such a pair are then at most $N$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of Stanley coordinates and of `𝒫_r(N)` (Section 4).

Formalized by `MetaMathlibExt.stanleyPartitions`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-02/index.html#stanley-partitions).

## Membership criterion for partitions in Stanley coordinates

For natural numbers $r$ and
$N$, a pair $((m_1, \dots, m_r), (n_1, \dots, n_r))$ of $r$-tuples of natural numbers lies in the
set $\mathcal{P}_r(N)$ of partitions of $N$ of length $r$ in Stanley coordinates if and only if
$m_1 > m_2 > \dots > m_r$, every $m_j$ and every $n_j$ is positive, and
$m_1 n_1 + \dots + m_r n_r = N$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of `𝒫_r(N)` (Section 4).

Formalized by `MetaMathlibExt.mem_stanleyPartitions`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-02/index.html#mem-stanley-partitions).

## Transposed partition in Stanley coordinates

For tuples $\mathbf{m} = (m_1, \dots, m_r)$
and $\mathbf{n} = (n_1, \dots, n_r)$ of natural numbers, the transpose
$\rho(\mathbf{m}, \mathbf{n})$ is the pair of tuples
$((n_1 + \dots + n_r, \dots, n_1 + n_2, n_1), (m_r, m_{r-1} - m_r, \dots, m_1 - m_2))$: for
$1 \le j \le r$, the $j$-th entry of the first tuple is $n_1 + \dots + n_{r+1-j}$ and the $j$-th
entry of the second tuple is $m_{r+1-j} - m_{r+2-j}$, where $m_{r+1} := 0$ and subtraction of
natural numbers is truncated at $0$.

On a partition with $m_1 > \dots > m_r$ this reflects its Young diagram in the main diagonal.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Section 4, transposed partition in Stanley coordinates.

Formalized by `MetaMathlibExt.stanleyTranspose`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 433](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L433). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-02/index.html#stanley-transpose).

## Transpose of a one-part partition

For all natural numbers $m$ and $n$, the transpose
$\rho$ in Stanley coordinates sends the pair of one-entry tuples $((m), (n))$ to $((n), (m))$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Section 4, transposed partition in Stanley coordinates.

Formalized by `MetaMathlibExt.stanleyTranspose_fin_one`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-02/index.html#stanley-transpose-fin-one).

## Sums over partitions are invariant under transposition

For all natural numbers $r$ and
$N$ and every function $a$ from pairs of $r$-tuples of natural numbers to $\mathbb{Q}$,
$\sum_{p \in \mathcal{P}_r(N)} a(p) = \sum_{p \in \mathcal{P}_r(N)} a(\rho(p))$, where
$\mathcal{P}_r(N)$ is the set of partitions of $N$ of length $r$ in Stanley coordinates and $\rho$
is the transpose map.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Lemma 1.

Stated but not proved: `MetaMathlibExt.sum_stanleyPartitions_comp_stanleyTranspose` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 452](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L452). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-02/index.html#sum-stanley-partitions-comp-stanley-tran).

## Coefficients of qMZVs as polynomial functions on partitions

Let $r \ge 1$ and let
$(k_1, Q_1), \dots, (k_r, Q_r)$ be pairs of a natural number $k_j$ and a polynomial
$Q_j \in \mathbb{Q}[X]$ with $\deg Q_j \le k_j$ for every $j$ and $Q_1(0) = 0$. For $s, N \ge 0$
let $\mathcal{P}_s(N)$ be the set of pairs $(\mathbf{m}, \mathbf{n})$ of tuples
$\mathbf{m} = (m_1, \dots, m_s)$ and $\mathbf{n} = (n_1, \dots, n_s)$ of positive integers with
$m_1 > \cdots > m_s$ and $m_1 n_1 + \cdots + m_s n_s = N$ (the partitions of $N$ with $s$
distinct parts $m_i$, of multiplicities $n_i$). Then there are polynomials
$f_s \in \mathbb{Q}[X_1, \dots, X_s, Y_1, \dots, Y_s]$, one for each $s \ge 0$, such that for
every $N \ge 0$ the coefficient of $q^N$ in the general qMZV
$\zeta_q(k_1, \dots, k_r; Q_1, \dots, Q_r)$ equals

$$\sum_{s=1}^{r} \sum_{(\mathbf{m}, \mathbf{n}) \in \mathcal{P}_s(N)} f_s(\mathbf{m}, \mathbf{n}),$$

where $f_s(\mathbf{m}, \mathbf{n})$ is the value of $f_s$ at $X_i = m_i$, $Y_i = n_i$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 18.

Stated but not proved: `MetaMathlibExt.exists_mvPolynomial_coeff_qMZV_eq_sum_stanleyPartitions` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 463](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L463). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-03/index.html#exists-mv-polynomial-coeff-q-mzv-eq-sum).

## Polynomial functions on partitions characterize $\mathcal{Z}_q$

Let
$\mathcal{Z}_q = \mathcal{Z}_{q,0}$ be the space of general qMZVs, and for natural numbers $r$
and $N$ let $\mathcal{P}_r(N)$ be the set of partitions of $N$ of length $r$ in Stanley
coordinates. A power series $S = \sum_{N \ge 0} a_N q^N \in \mathbb{Q}[[q]]$ lies in
$\mathcal{Z}_q$ if and only if there are $f_0 \in \mathbb{Q}$, polynomials
$f_r \in \mathbb{Q}[X_1, \dots, X_r, Y_1, \dots, Y_r]$ for $r \ge 1$ and a natural number $R$
with $f_r = 0$ for every $r > R$, such that $a_0 = f_0$ and, for every $N \ge 1$,

$$a_N = \sum_{r=1}^{N} \sum_{(\mathbf{m}, \mathbf{n}) \in \mathcal{P}_r(N)}
f_r(\mathbf{m}, \mathbf{n}),$$

where $f_r(\mathbf{m}, \mathbf{n})$ is the value of $f_r$ at $X_i = m_i$, $Y_i = n_i$.

The sum over $r$ stops at $N$, which loses nothing because $\mathcal{P}_r(N)$ is empty for
$r > N$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 19.

Stated but not proved: `MetaMathlibExt.mem_qMZVSpace_zero_iff_exists_mvPolynomial` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 477](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L477). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-03/index.html#mem-q-mzvspace-zero-iff-exists-mv-polyno).

## Quasi-shuffle product

Fix an alphabet and a product of letters $a \diamond b$, a formal
sum of letters given as a finite list (possibly empty, possibly with repetitions). The
quasi-shuffle product $u \ast v$ of two words $u$ and $v$ is the formal sum of words, recorded as
a list, defined recursively by $\mathbf{1} \ast w = w \ast \mathbf{1} = w$ for the empty word
$\mathbf{1}$ and by
$a u \ast b v = a (u \ast b v) + b (a u \ast v) + (a \diamond b)(u \ast v)$
for letters $a$, $b$ and words $u$, $v$. Here a letter, or a formal sum of letters, written in
front of a formal sum of words is prepended to each of its words, and the terms are listed in
the order of the formula.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, quasi-shuffle products of Section 2 (the induced quasi-shuffle products on `M`, `𝔎`, `𝔥¹`).

Formalized by `MetaMathlibExt.quasiShuffle`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 492](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L492). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-03/index.html#quasi-shuffle).

## The empty word is a left unit for the quasi-shuffle product

For every alphabet, every
product of letters and every word $w$, the quasi-shuffle product of the empty word $\mathbf{1}$
with $w$ is $\mathbf{1} \ast w = w$, the formal sum consisting of the single word $w$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, quasi-shuffle products of Section 2.

Formalized by `MetaMathlibExt.quasiShuffle_nil_left`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 504](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L504). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-03/index.html#quasi-shuffle-nil-left).

## The stuffle product of two letters

For natural numbers $a$ and $b$, viewed as one-letter
words, the quasi-shuffle product with letter product $a \diamond b = a + b$ (the stuffle product)
is $a \ast b = ab + ba + (a + b)$: the two-letter words $ab$ and $ba$ and the one-letter word
$(a + b)$, listed in this order.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of the SZ-stuffle product.

Formalized by `MetaMathlibExt.quasiShuffle_singleton_singleton`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 512](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L512). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-03/index.html#quasi-shuffle-singleton-singleton).

## SZ-qshuffle product

The SZ-qshuffle product $\text{ш}$ of two words in the letters $p$
and $y$ is the formal sum of words, counted with multiplicity, defined recursively by
$\mathbf{1} \mathbin{\text{ш}} w = w \mathbin{\text{ш}} \mathbf{1} = w$ for the empty word
$\mathbf{1}$, and, for words $u, v$,
$y u \mathbin{\text{ш}} v = y (u \mathbin{\text{ш}} v)$,
$p u \mathbin{\text{ш}} y v = y (p u \mathbin{\text{ш}} v)$ and
$p u \mathbin{\text{ш}} p v = p (u \mathbin{\text{ш}} p v) + p (p u \mathbin{\text{ш}} v) +
p (u \mathbin{\text{ш}} v)$,
where a letter in front of a formal sum is prepended to each of its words.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of the SZ-qshuffle product.

Formalized by `MetaMathlibExt.szShuffle`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-03/index.html#sz-shuffle).

## SZ-qshuffle of $y$ with itself

The SZ-qshuffle product of the one-letter word $y$ with
itself is the single word $yy$: $y \mathbin{\text{ш}} y = yy$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of the SZ-qshuffle product.

Formalized by `MetaMathlibExt.szShuffle_y_y`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 536](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L536). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-03/index.html#sz-shuffle-y-y).

## Word of an index

The word of an index $(k_1, \dots, k_r)$ of natural numbers is the word
$p^{k_1} y \cdots p^{k_r} y$ in the letters $p$ and $y$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, identification of SZ-admissible indices with words of `𝔎¹`.

Formalized by `MetaMathlibExt.szWord`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 543](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L543). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-03/index.html#sz-word).

## Word of the empty index

The word of the empty index is the empty word.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, identification of SZ-admissible indices with words of `𝔎¹`.

Formalized by `MetaMathlibExt.szWord_nil`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 550](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L550). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-03/index.html#sz-word-nil).

## Reading an index off a word in $p$ and $y$

For $c \in \mathbb{N}$ and a word $w$ in the
letters $p$ and $y$, the index $R_c(w)$, a finite sequence of natural numbers, is defined
recursively by $R_c(\mathbf{1}) = ()$ for the empty word $\mathbf{1}$, $R_c(p w) = R_{c+1}(w)$,
and $R_c(y w) = (c, R_0(w))$, the index with first entry $c$ followed by the entries of
$R_0(w)$. Thus $R_c(p^{k_1} y\, p^{k_2} y \cdots p^{k_r} y\, p^j) = (c + k_1, k_2, \dots, k_r)$
for $r \ge 1$ and $R_c(p^j) = ()$: the entries are the lengths of the blocks of $p$s before
each $y$, with $c$ added to the first, and trailing $p$s are dropped.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, identification of SZ-admissible indices with words of `𝔎¹`.

Formalized by `MetaMathlibExt.szIndexOfWordAux`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 557](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L557). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-03/index.html#sz-index-of-word-aux).

## Reading off a leading block of $p$s

Write $R_c(w)$ for the index read off a word $w$ in
the letters $p$ and $y$ when $c$ letters $p$ have already been read. For all $c, n \in \mathbb{N}$
and every word $w$, $R_c(p^n y w)$ is the index whose first entry is $c + n$ and whose remaining
entries are those of $R_0(w)$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, identification of SZ-admissible indices with words of `𝔎¹`.

Formalized by `MetaMathlibExt.szIndexOfWordAux_replicate_append`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 566](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L566). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-03/index.html#sz-index-of-word-aux-replicate-append).

## Schlesinger–Zudilin qMZVs of words

Write $\zeta_q^{SZ}$ for the Schlesinger–Zudilin qMZV
of an index of natural numbers. For a word $w$ in the letters $p$ and $y$ with $r$ letters $y$,
let $k_j$ be the number of letters $p$ between the $(j-1)$-st and the $j$-th letter $y$ of $w$
(for $j = 1$, before the first $y$); letters $p$ after the last $y$ are ignored. The value of
$\zeta_q^{SZ}$ on $w$ is $\zeta_q^{SZ}(k_1, \dots, k_r)$. In particular the word
$p^{k_1} y \cdots p^{k_r} y$ is sent to $\zeta_q^{SZ}(k_1, \dots, k_r)$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of the SZ-qshuffle product (ii).

Formalized by `MetaMathlibExt.szQMZVWord`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 579](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L579). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-03/index.html#sz-qmzvword).

## SZ-qMZV of the word of a one-entry index

Write $\zeta_q^{SZ}$ for the Schlesinger–Zudilin
qMZV, extended to words in the letters $p$ and $y$ by sending a word to $\zeta_q^{SZ}$ of the
index read off it: the number of letters $p$ before each letter $y$ since the previous $y$, with
letters $p$ after the last $y$ dropped. For every natural number $k$, the value of
$\zeta_q^{SZ}$ on the word $p^k y$ of the one-entry index $(k)$ is $\zeta_q^{SZ}(k)$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of the SZ-qshuffle product (ii).

Formalized by `MetaMathlibExt.szQMZVWord_szWord_singleton`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 586](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L586). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-03/index.html#sz-qmzvword-sz-word-singleton).

## Quasi-shuffle relations for general qMZVs

Consider words in letters $(k, Q)$ with
$k \in \mathbb{N}$ and $Q \in \mathbb{Q}[X]$, and let $u$ and $v$ be words in which every letter
satisfies $\deg Q \le k$ and the first letter, if any, satisfies $Q(0) = 0$. Let $u \ast v$ be
the quasi-shuffle product of $u$ and $v$ with letter product
$(k_1, Q_1) \diamond (k_2, Q_2) = (k_1 + k_2, Q_1 Q_2)$, a formal sum of words. Then
$\zeta_q(u)\,\zeta_q(v) = \zeta_q(u \ast v)$, where $\zeta_q$ sends a word
$(k_1, Q_1) \cdots (k_r, Q_r)$ to the general qMZV $\zeta_q(k_1, \dots, k_r; Q_1, \dots, Q_r)$
and is extended linearly to formal sums of words.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 2.

Stated but not proved: `MetaMathlibExt.qMZV_mul_eq_sum_quasiShuffle` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 600](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L600). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-03/index.html#q-mzv-mul-eq-sum-quasi-shuffle).

## Stuffle product formula for Schlesinger–Zudilin qMZVs

Write $\zeta_q^{SZ}$ for the
Schlesinger–Zudilin qMZV. Let $v$ and $w$ be finite lists of natural numbers that are
SZ-admissible, that is, each is empty or has first entry at least $1$. Then

$$\zeta_q^{SZ}(v)\,\zeta_q^{SZ}(w) = \sum_{u} \zeta_q^{SZ}(u),$$

where $u$ runs, counted with multiplicity, over the terms of the stuffle product $v \ast w$: the
quasi-shuffle product of $v$ and $w$ as words in the alphabet $\mathbb{N}$ with the product of
letters $a \diamond b = a + b$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 2.

Stated but not proved: `MetaMathlibExt.szQMZV_mul_eq_sum_stuffle` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 611](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L611). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-03/index.html#sz-qmzv-mul-eq-sum-stuffle).

## Shuffle product formula for Schlesinger–Zudilin qMZVs (Singer)

Write $\zeta_q^{SZ}$ for
the Schlesinger–Zudilin qMZV. Let $u$ and $v$ be finite lists of natural numbers that are
SZ-admissible, that is, each is empty or has first entry at least $1$, and let $w_u$ and $w_v$
be their words in the letters $p$ and $y$ (the index $(k_1, \dots, k_r)$ has word
$p^{k_1} y \cdots p^{k_r} y$). Then

$$\zeta_q^{SZ}(u)\,\zeta_q^{SZ}(v) = \sum_{w} \zeta_q^{SZ}(w),$$

where $w$ runs, counted with multiplicity, over the terms of the SZ-qshuffle product
$w_u \mathbin{\text{ш}} w_v$, and $\zeta_q^{SZ}$ of a word is $\zeta_q^{SZ}$ of the index read
off it: the number of letters $p$ before each letter $y$ since the previous $y$, with letters $p$
after the last $y$ dropped.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 3 (Singer).

Stated but not proved: `MetaMathlibExt.szQMZV_mul_eq_sum_szShuffle` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 620](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L620). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-03/index.html#sz-qmzv-mul-eq-sum-sz-shuffle).

## Quasi-shuffle relations for Bradley–Zhao qMZVs

Identify an index $(k_1, \dots, k_r)$
with the word $z_{k_1} \cdots z_{k_r}$, and let $u$ and $v$ be admissible indices: finite,
possibly empty, sequences of positive integers whose first entry, if any, is at least $2$. Let
$u \ast_{BZ} v$ be the quasi-shuffle product of $u$ and $v$ with letter product
$z_a \diamond z_b = z_{a+b} + z_{a+b-1}$, a formal sum of indices. Then
$\zeta_q^{BZ}(u)\,\zeta_q^{BZ}(v) = \zeta_q^{BZ}(u \ast_{BZ} v)$, where the Bradley–Zhao qMZV
$\zeta_q^{BZ}$ is extended linearly to formal sums of indices.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 5.

Stated but not proved: `MetaMathlibExt.bzQMZV_mul_eq_sum_quasiShuffle` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 630](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L630). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-03/index.html#bz-qmzv-mul-eq-sum-quasi-shuffle).

## Analytic properties of general qMZVs

Let $(k_1, Q_1), \dots, (k_r, Q_r)$ be pairs of an
integer $k_j \ge 1$ and a polynomial $Q_j \in \mathbb{Q}[X]$ with $\deg Q_j \le k_j$ for every
$j$ and $Q_1(0) = 0$, and write the general qMZV as
$\zeta_q(k_1, \dots, k_r; Q_1, \dots, Q_r) = \sum_{n \ge 0} c_n q^n$. Then (i) for every complex
$q$ with $|q| < 1$ the series $\sum_{n \ge 0} c_n q^n$ converges absolutely; (ii) the function
$\tau \mapsto \sum_{n \ge 0} c_n e^{2 \pi i n \tau}$ is holomorphic on the upper half-plane
$\{\tau \in \mathbb{C} : \operatorname{Im} \tau > 0\}$; (iii) if $r \ge 1$ and $k_1 \ge 2$, then
$(1 - q)^{k_1 + \cdots + k_r} \sum_{n \ge 0} c_n q^n$ tends to
$\zeta(k_1, \dots, k_r) \prod_{j=1}^{r} Q_j(1)$ as the real number $q$ tends to $1$ from below,
where $\zeta(k_1, \dots, k_r) = \sum_{n_1 > \cdots > n_r > 0} n_1^{-k_1} \cdots n_r^{-k_r}$ is the
multiple zeta value.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 1.

Stated but not proved: `MetaMathlibExt.qMZV_summable_differentiableOn_tendsto` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 647](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L647). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-03/index.html#q-mzv-summable-differentiable-on-tendsto).

## Letters of the Takeyama–Bradley–Zhao model as qMZV data

The letters of the TBZ model
are the symbol $\bar 1$ and the natural numbers $k \ge 1$. The letter $\bar 1$, with summand
$f(\bar 1, m) = q^m / (1 - q^m)$, is sent to the pair $(1, X)$, and the letter $k$, with
summand $f(k, m) = q^{(k-1)m} / (1 - q^m)^k$, is sent to the pair $(k, X^{k-1})$. Here a pair
$(k, Q)$ of a natural number and a rational polynomial stands for the summand
$Q(q^m) / (1 - q^m)^k$ of a general qMZV. The number $0$, which is not a letter of the
model, is sent to $(0, 1)$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of the Takeyama–Bradley–Zhao model (`f(1̄, m)`, `f(k, m)`).

Formalized by `MetaMathlibExt.tbzLetter`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 668](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L668). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-03/index.html#tbz-letter).

## Takeyama–Bradley–Zhao qMZVs

For an index $(k_1, \dots, k_r)$ whose entries are the symbol
$\bar 1$ or natural numbers, the TBZ-qMZV is the general qMZV of the data obtained by replacing
each entry by its pair in the Takeyama–Bradley–Zhao letter encoding. When every natural-number
entry is at least $1$ and $k_1 \ne 1$, this is

$$\zeta_q^{TBZ}(k_1, \dots, k_r) = \sum_{m_1 > \cdots > m_r > 0} f(k_1, m_1) \cdots f(k_r, m_r),$$

with $f(\bar 1, m) = q^m / (1 - q^m)$ and $f(k, m) = q^{(k-1)m} / (1 - q^m)^k$; the empty index
gives $1$. For $k_1 = 1$, or when some entry is $0$, the value is a junk value.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of the Takeyama–Bradley–Zhao model.

Formalized by `MetaMathlibExt.tbzQMZV`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 679](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L679). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-03/index.html#tbz-qmzv).

## TBZ-qMZV of the empty index

The Takeyama–Bradley–Zhao qMZV of the empty index is $1$:
$\zeta_q^{\mathrm{TBZ}}(\varnothing) = 1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of the Takeyama–Bradley–Zhao model.

Formalized by `MetaMathlibExt.tbzQMZV_nil`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 686](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L686). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-04/index.html#tbz-qmzv-nil).

## The TBZ model extends the BZ model

For every index $(k_1, \dots, k_r)$ of natural
numbers, read as a TBZ index without the symbol $\bar 1$, the TBZ-qMZV equals the Bradley–Zhao
qMZV: $\zeta_q^{\mathrm{TBZ}}(k_1, \dots, k_r) = \zeta_q^{\mathrm{BZ}}(k_1, \dots, k_r)$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of the Takeyama–Bradley–Zhao model.

Formalized by `MetaMathlibExt.tbzQMZV_map_some`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 692](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L692). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-04/index.html#tbz-qmzv-map-some).

## The Takeyama–Bradley–Zhao model spans $\mathcal{Z}_q$

Let $\overline{\mathbb{N}}$
consist of the positive integers and one further symbol $\bar 1$. The space
$\mathcal{Z}_q = \mathcal{Z}_{q,0}$ equals the $\mathbb{Q}$-linear span of the TBZ-qMZVs
$\zeta_q^{\mathrm{TBZ}}(k_1, \dots, k_r)$ over all $r \ge 0$ and all
$k_1, \dots, k_r \in \overline{\mathbb{N}}$ with $k_1 \ne 1$ when $r \ge 1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 6.

Stated but not proved: `MetaMathlibExt.qMZVSpace_zero_eq_span_tbzQMZV` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 701](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L701). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-04/index.html#q-mzvspace-zero-eq-span-tbz-qmzv).

## The spaces $\mathcal{Z}^\circ_{q,d}$

For a natural number $d$, the space
$\mathcal{Z}^\circ_{q,d}$ is the $\mathbb{Q}$-linear span, in the formal power series ring
$\mathbb{Q}[[q]]$, of the general qMZVs $\zeta_q(k_1, \dots, k_r; Q_1, \dots, Q_r)$ over all
$r \ge 0$, natural numbers $k_1, \dots, k_r$ and polynomials $Q_1, \dots, Q_r \in \mathbb{Q}[X]$
such that for every $j$ we have $k_j \ge 1$, $\deg Q_j + d \le k_j$ and $Q_j(0) = 0$. Here the
zero polynomial has degree $0$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of `𝒵_{q,d}` and `𝒵°_{q,d}` (after Bachmann–Kühn).

Formalized by `MetaMathlibExt.qMZVSpaceCirc`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 710](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L710). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-04/index.html#q-mzvspace-circ).

## The constant $1$ lies in $\mathcal{Z}^\circ_{q,d}$

For every natural number $d$, the
constant power series $1$ (the qMZV of the empty index) lies in
the space $\mathcal{Z}^\circ_{q,d}$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of `𝒵°_{q,d}`.

Formalized by `MetaMathlibExt.one_mem_qMZVSpaceCirc`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 718](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L718). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-04/index.html#one-mem-q-mzvspace-circ).

## $\mathcal{Z}^\circ_{q,d}$ is contained in $\mathcal{Z}_{q,d}$

For every natural number
$d$, the space $\mathcal{Z}^\circ_{q,d}$ is a subspace of $\mathcal{Z}_{q,d}$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of `𝒵°_{q,d}` (a subspace of `𝒵_{q,d}`).

Formalized by `MetaMathlibExt.qMZVSpaceCirc_le_qMZVSpace`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 725](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L725). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-04/index.html#q-mzvspace-circ-le-q-mzvspace).

## Okounkov polynomials

For $k \in \mathbb{N}$, the Okounkov polynomial
$p_k \in \mathbb{Q}[X]$ is $p_k(X) = X^{k/2}$ if $k$ is even and $p_k(X) = X^{(k-1)/2}(1 + X)$ if
$k$ is odd.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of Okounkov qMZVs.

Formalized by `MetaMathlibExt.okounkovPoly`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 736](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L736). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-04/index.html#okounkov-poly).

## The Okounkov polynomials $p_2$ and $p_3$

The Okounkov polynomials of index $2$ and $3$
are $p_2(X) = X$ and $p_3(X) = X(1 + X)$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of Okounkov qMZVs.

Formalized by `MetaMathlibExt.okounkovPoly_two_three`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 743](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L743). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-04/index.html#okounkov-poly-two-three).

## Okounkov $q$-multiple zeta values

For a natural number $k$ let $p_k$ be Okounkov's
polynomial: $p_k(X) = X^{k/2}$ if $k$ is even and $p_k(X) = X^{(k-1)/2}(1 + X)$ if $k$ is odd.
For an index $(k_1, \dots, k_r)$ of natural numbers, the Okounkov qMZV is the general qMZV
$\zeta_q^{\mathrm{Oko}}(k_1, \dots, k_r) = \zeta_q(k_1, \dots, k_r; p_{k_1}, \dots, p_{k_r})$,
a formal power series in $q$ over $\mathbb{Q}$.

The paper uses it only for indices with every $k_i \ge 2$; for other indices the value is a
placeholder.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of Okounkov qMZVs.

Formalized by `MetaMathlibExt.okounkovQMZV`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 752](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L752). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-04/index.html#okounkov-qmzv).

## Okounkov qMZV of the empty index

The Okounkov $q$-multiple zeta value of the empty
index is $1$: $\zeta_q^{\mathrm{Oko}}(\varnothing) = 1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of Okounkov qMZVs.

Formalized by `MetaMathlibExt.okounkovQMZV_nil`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 759](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L759). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-04/index.html#okounkov-qmzv-nil).

## Okounkov qMZVs span $\mathcal{Z}^\circ_{q,1}$

The space $\mathcal{Z}^\circ_{q,1}$ equals
the $\mathbb{Q}$-linear span of the Okounkov qMZVs $\zeta_q^{\mathrm{Oko}}(k_1, \dots, k_r)$ over
all indices of length $r \ge 0$ with every $k_i \ge 2$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 13 (after Bachmann–Kühn).

Stated but not proved: `MetaMathlibExt.qMZVSpaceCirc_one_eq_span_okounkovQMZV` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 766](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L766). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-04/index.html#q-mzvspace-circ-one-eq-span-okounkov-qmz).

## Eulerian q-series

For natural numbers $k$ and $m \ge 1$, the Eulerian $q$-series is

$$
\sum_{n \ge 1} \frac{n^{k-1}}{(k-1)!} \, q^{mn},
$$

the inner sum of a bi-bracket; here $k - 1$ is read as $0$ when $k = 0$. For $m = 0$ the series
is defined to be $0$.

For $k, m \ge 1$ it equals $P_k(q^m)/(1 - q^m)^k$, where $P_k$ is the $k$-th Eulerian polynomial.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition-Proposition of bi-brackets (Eulerian polynomials).

Formalized by `MetaMathlibExt.eulerianQSeries`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 775](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L775). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-04/index.html#eulerian-qseries).

## Coefficients of the Eulerian q-series

For natural numbers $k$, $m$ and $n$ with $m > 0$
and $n > 0$, the coefficient of $q^{mn}$ in the Eulerian $q$-series
$\sum_{\ell \ge 1} \frac{\ell^{k-1}}{(k-1)!} q^{m\ell}$ is $\frac{n^{k-1}}{(k-1)!}$, where $k - 1$
is read as $0$ when $k = 0$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition-Proposition of bi-brackets.

Formalized by `MetaMathlibExt.coeff_mul_eulerianQSeries`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 783](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L783). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-04/index.html#coeff-mul-eulerian-qseries).

## Partial sums of bi-brackets

For pairs $(k_1, d_1), \dots, (k_r, d_r)$ of natural numbers
and a bound $M \in \mathbb{N}$, the partial bi-bracket is the $q$-series

$$
\sum_{M > m_1 > \dots > m_r > 0} \, \prod_{j=1}^{r} \frac{m_j^{d_j}}{d_j!} E_{k_j}(m_j),
$$

where $E_k(m) = \sum_{n \ge 1} \frac{n^{k-1}}{(k-1)!} q^{mn}$ is the Eulerian $q$-series (with
$k - 1$ read as $0$ when $k = 0$). For $r = 0$ it is $1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition-Proposition of bi-brackets (defining sum truncated at `m₁ < M`).

Formalized by `MetaMathlibExt.biBracketPartial`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 792](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L792). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-04/index.html#bi-bracket-partial).

## Bi-brackets

For integers $k_1, \dots, k_r \ge 1$ and $d_1, \dots, d_r \ge 0$, the
bi-bracket is the $q$-series

$$
g(k_1, \dots, k_r; d_1, \dots, d_r) =
\sum_{m_1 > \dots > m_r > 0} \, \sum_{n_1, \dots, n_r > 0} \, \prod_{j=1}^{r}
\frac{m_j^{d_j}}{d_j!} \frac{n_j^{k_j - 1}}{(k_j - 1)!} \, q^{m_1 n_1 + \dots + m_r n_r},
$$

and $g(\varnothing; \varnothing) = 1$. The summands with $m_1 > N$ have $q$-adic order greater
than $N$, so the coefficient of $q^N$ is that of the finite partial sum over $m_1 \le N$; this
is how the series is defined.

The same formula, with $k_j - 1$ read as $0$, defines a value when some $k_j = 0$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition-Proposition of bi-brackets (after Bachmann).

Formalized by `MetaMathlibExt.biBracket`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 805](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L805). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-04/index.html#bi-bracket).

## Empty bi-bracket

The bi-bracket of the empty index is $1$:
$g(\varnothing; \varnothing) = 1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition-Proposition of bi-brackets.

Formalized by `MetaMathlibExt.biBracket_nil`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 812](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L812). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-04/index.html#bi-bracket-nil).

## Generating series of bi-brackets

For $r \in \mathbb{N}$, the generating series of the
bi-brackets of depth $r$ is the formal power series in the variables $X_1, \dots, X_r$,
$Y_1, \dots, Y_r$ with coefficients in $\mathbb{Q}[[q]]$

$$
g(X_1, \dots, X_r; Y_1, \dots, Y_r) =
\sum_{k_1, \dots, k_r \ge 1} \, \sum_{d_1, \dots, d_r \ge 1}
g(k_1, \dots, k_r; d_1 - 1, \dots, d_r - 1) \prod_{j=1}^{r} X_j^{k_j - 1} Y_j^{d_j - 1},
$$

where $g(k_1, \dots, k_r; d_1, \dots, d_r)$ is the bi-bracket. Equivalently, the coefficient of
$\prod_{j=1}^{r} X_j^{a_j} Y_j^{b_j}$ is $g(a_1 + 1, \dots, a_r + 1; b_1, \dots, b_r)$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 11 (definition of the generating series).

Formalized by `MetaMathlibExt.biBracketGen`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 822](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L822). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-04/index.html#bi-bracket-gen).

## Coefficients of the bi-bracket generating series

For $r \in \mathbb{N}$ and exponents
$a_1, \dots, a_r, b_1, \dots, b_r \ge 0$, the coefficient of $\prod_{j=1}^{r} X_j^{a_j} Y_j^{b_j}$
in the generating series $g(X_1, \dots, X_r; Y_1, \dots, Y_r)$ of bi-brackets of depth $r$ is
the bi-bracket $g(a_1 + 1, \dots, a_r + 1; b_1, \dots, b_r)$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 11.

Formalized by `MetaMathlibExt.coeff_biBracketGen`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 829](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L829). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-04/index.html#coeff-bi-bracket-gen).

## Generating series of Schlesinger–Zudilin qMZVs

For a natural number $r$, the
generating series of SZ-qMZVs of depth $r$ is the formal power series in the $2r$ variables
$X_1, \dots, X_r, Y_1, \dots, Y_r$ with coefficients in $\mathbb{Q}[[q]]$

$$
s(X_1, \dots, X_r; Y_1, \dots, Y_r) = \sum_{k_1, \dots, k_r \ge 1} \sum_{d_1, \dots, d_r \ge 0}
\zeta_q^{\mathrm{SZ}}(k_1, \{0\}^{d_1}, \dots, k_r, \{0\}^{d_r})
\prod_{j=1}^{r} X_j^{k_j - 1} Y_j^{d_j},
$$

where $\{0\}^{d}$ stands for $d$ consecutive zeros.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 4 (definition of the generating series).

Formalized by `MetaMathlibExt.szGen`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 840](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L840). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-04/index.html#sz-gen).

## Coefficients of the SZ generating series

For $r \in \mathbb{N}$ and exponents
$a_1, \dots, a_r, b_1, \dots, b_r \ge 0$, the coefficient of $\prod_{j=1}^{r} X_j^{a_j} Y_j^{b_j}$
in the generating series $s(X_1, \dots, X_r; Y_1, \dots, Y_r)$ of Schlesinger–Zudilin
$q$-multiple zeta values of depth $r$ is
$\zeta_q^{\mathrm{SZ}}(a_1 + 1, \{0\}^{b_1}, \dots, a_r + 1, \{0\}^{b_r})$, where $\{0\}^b$
stands for $b$ consecutive zeros.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 4.

Formalized by `MetaMathlibExt.coeff_szGen`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 848](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L848). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-04/index.html#coeff-sz-gen).

## The logarithm series $\ln(1 + T)$

The formal power series $\ln(1 + T)$ over
$\mathbb{Q}$ is $\sum_{n \ge 1} (-1)^{n+1} T^n / n$; its constant term is $0$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 13 (ii) (the substitution `Xⱼ ↦ ln(Xⱼ + 1)`).

Formalized by `MetaMathlibExt.logOneAddSeries`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 857](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L857). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-05/index.html#log-one-add-series).

## Low-order coefficients of the logarithm series

The power series
$\ln(1 + T) = \sum_{n \ge 1} (-1)^{n+1} T^n / n$ over $\mathbb{Q}$ has constant coefficient $0$
and coefficient $1$ at $T$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 13 (ii).

Formalized by `MetaMathlibExt.coeff_logOneAddSeries_zero_one`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 864](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L864). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-05/index.html#coeff-log-one-add-series-zero-one).

## Bi-bracket generating series as a sum of exponentials

Let $r$ and $N$ be natural numbers
and let $g(X_1, \dots, X_r; Y_1, \dots, Y_r)$ be the generating series of bi-brackets of depth $r$,
a power series in the $2r$ variables over $\mathbb{Q}[[q]]$. The power series over $\mathbb{Q}$
obtained by taking the coefficient of $q^N$ in every coefficient of $g$ equals the finite sum

$$\sum \prod_{j=1}^r e^{m_j Y_j} e^{n_j X_j}$$

over all integers $m_1 > m_2 > \dots > m_r > 0$ and $n_1, \dots, n_r \ge 1$ with
$m_1 n_1 + \dots + m_r n_r = N$, where $e^Z$ is the exponential series evaluated at $Z$.

This is the $q^N$-part of the identity
$g(X; Y) = \sum \prod_j e^{m_j Y_j} e^{n_j X_j} q^{m_j n_j}$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 11 (after Bachmann).

Stated but not proved: `MetaMathlibExt.coeff_biBracketGen_eq_sum_exp` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 876](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L876). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-05/index.html#coeff-bi-bracket-gen-eq-sum-exp).

## Partition relation for bi-brackets

For every natural number $r$, the generating series
$g(X_1, \dots, X_r; Y_1, \dots, Y_r)$ of bi-brackets of depth $r$ satisfies

$$g(X_1, \dots, X_r; Y_1, \dots, Y_r) = g(Y_1 + \dots + Y_r, \dots, Y_1 + Y_2, Y_1;
X_r, X_{r-1} - X_r, \dots, X_1 - X_2),$$

where the right side substitutes linear forms into $g$ simultaneously: for $1 \le i \le r$, the
variable $X_i$ is replaced by $Y_1 + \dots + Y_{r+1-i}$ and the variable $Y_i$ by
$X_{r+1-i} - X_{r+2-i}$, with $X_{r+1} := 0$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 12 (partition relation, after Bachmann).

Stated but not proved: `MetaMathlibExt.biBracketGen_partition_relation` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 895](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L895). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-05/index.html#bi-bracket-gen-partition-relation).

## Translation between bi-brackets and the Schlesinger–Zudilin model

Let $r$ be a natural
number, let $g(X_1, \dots, X_r; Y_1, \dots, Y_r)$ be the generating series of bi-brackets of depth
$r$ and $s(X_1, \dots, X_r; Y_1, \dots, Y_r)$ the generating series of Schlesinger–Zudilin qMZVs of
depth $r$, both power series in the $2r$ variables over $\mathbb{Q}[[q]]$. For a power series $Z$
without constant term, write $e^Z$ and $\ln(1 + Z)$ for the substitution of $Z$ into the
exponential series and into $\ln(1 + T) = \sum_{n \ge 1} (-1)^{n+1} T^n / n$, and put
$S_j = Y_1 + \dots + Y_j$. Then:

(i) $\prod_{j=1}^r e^{X_j} e^{S_j} \cdot s(e^{X_1} - 1, \dots, e^{X_r} - 1; e^{S_1} - 1, \dots,
e^{S_r} - 1) = g(X_1, \dots, X_r; Y_1, \dots, Y_r)$;

(ii) $\prod_{j=1}^r (1 + X_j)(1 + Y_j) \cdot s(X_1, \dots, X_r; Y_1, \dots, Y_r)$ equals
$g(\ln(1 + X_1), \dots, \ln(1 + X_r); \ln(1 + Y_1), \ln(1 + Y_2) - \ln(1 + Y_1), \dots,
\ln(1 + Y_r) - \ln(1 + Y_{r-1}))$.

Part (ii) is stated with the unit $\prod_j (1 + X_j)(1 + Y_j)$ multiplied out instead of inverted.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 13 (translation bi-brackets/SZ model).

Stated but not proved: `MetaMathlibExt.biBracketGen_eq_szGen_subst` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 915](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L915). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-05/index.html#bi-bracket-gen-eq-sz-gen-subst).

## Generating series of OOZ-qMZVs, coefficientwise

Let $r$ and $N$ be natural numbers and
let $k_1, \dots, k_r \ge 1$ and $d_1, \dots, d_r \ge 0$ be integers. Writing $\{0\}^d$ for $d$
consecutive zeros, the coefficient of $q^N$ in the Ohno–Okuda–Zudilin qMZV
$\zeta_q^{\mathrm{OOZ}}(k_1, \{0\}^{d_1}, \dots, k_r, \{0\}^{d_r})$ equals the coefficient of
$q^N$ in

$$\sum q^{m_1} \prod_{j=1}^r \binom{m_j - m_{j+1} - 1}{d_j} \frac{1}{(1 - q^{m_j})^{k_j}},$$

the sum running over integers $N \ge m_1 > m_2 > \dots > m_r > 0$, where $m_{r+1} := 0$ and the
factor $q^{m_1}$ is read as $1$ when $r = 0$.

In the untruncated sum, the summands with $m_1 > N$ have $q$-adic order greater than $N$. Let
$\mathfrak{oz}(X; Y)$ be the paper's generating series of OOZ-qMZVs of depth $r$ in the variables
$X_1, \dots, X_r$ and $Y_1, \dots, Y_r$ over $\mathbb{Q}[[q]]$. The statement compares the
coefficients of $\prod_j X_j^{k_j}/k_j! \, Y_j^{d_j}$ on both sides of the paper's identity
$\mathfrak{oz}(X; Y) = \sum q^{m_1} \prod_j (1 + Y_j)^{m_j - m_{j+1} - 1}
(e^{X_j/(1 - q^{m_j})} - 1)$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 11.

Stated but not proved: `MetaMathlibExt.coeff_oozQMZV_szBlockIndex_eq_sum_choose` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 950](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L950). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-05/index.html#coeff-ooz-qmzv-sz-block-index-eq-sum-cho).

## Brackets, Okounkov qMZVs and Bradley–Zhao qMZVs span $\mathcal{Z}^\circ_{q,1}$

For an
index $k = (k_1, \dots, k_r)$ of natural numbers let $g(k) = g(k_1, \dots, k_r; 0, \dots, 0)$ be
the bracket, that is, the bi-bracket with all $d_j = 0$, and let $\zeta_q^{\mathrm{Oko}}(k)$ and
$\zeta_q^{BZ}(k)$ be the Okounkov and Bradley–Zhao qMZVs. Then the space
$\mathcal{Z}^\circ_{q,1}$ equals the $\mathbb{Q}$-linear span of the brackets $g(k)$, equals the
$\mathbb{Q}$-linear span of the Okounkov qMZVs $\zeta_q^{\mathrm{Oko}}(k)$, and equals the
$\mathbb{Q}$-linear span of the Bradley–Zhao qMZVs $\zeta_q^{BZ}(k)$, where in each case $k$ runs
over all indices of length $r \ge 0$ with every $k_i \ge 2$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 16.

Stated but not proved: `MetaMathlibExt.qMZVSpaceCirc_one_eq_span_bracket_okounkov_bz` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 965](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L965). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-05/index.html#q-mzvspace-circ-one-eq-span-bracket-okou).

## Weighted quasi-shuffle product

Let $A$ be an alphabet and let $d$ assign to any two
letters $a, b \in A$ a finite formal $\mathbb{Q}$-linear combination
$d(a, b) = \sum_c d(a, b)_c \, c$ of letters. The weighted quasi-shuffle product $u \ast v$ of
two words over $A$ is the finite formal $\mathbb{Q}$-linear combination of words defined by
recursion on total length: $\mathbf{1} \ast w = w \ast \mathbf{1} = w$ for the empty word
$\mathbf{1}$, and for letters $a, b$ and words $u, v$,
$a u \ast b v = a (u \ast b v) + b (a u \ast v) + \sum_c d(a, b)_c \, c (u \ast v)$, where
prefixing a letter is extended linearly to combinations of words.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, quasi-shuffle products of Section 2 (with `ℚ`-valued letter product, as for bi-brackets).

Formalized by `MetaMathlibExt.weightedQuasiShuffle`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 979](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L979). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-05/index.html#weighted-quasi-shuffle).

## The empty word is a left unit for the weighted quasi-shuffle

For every alphabet $A$,
every weighted letter product $d$ on $A$ (assigning to two letters a finite formal
$\mathbb{Q}$-linear combination of letters) and every word $v$ over $A$, the weighted
quasi-shuffle product of the empty word $\mathbf{1}$ with $v$ is $v$: $\mathbf{1} \ast v = v$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, quasi-shuffle products of Section 2.

Formalized by `MetaMathlibExt.weightedQuasiShuffle_nil_left`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 993](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L993). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-05/index.html#weighted-quasi-shuffle-nil-left).

## Bachmann's coefficients

For natural numbers $a$, $b$ and $j$,

$$\lambda_{a,b}^j = (-1)^{b-1} \binom{a + b - j - 1}{a - j} \frac{B_{a+b-j}}{(a + b - j)!},$$

where $B_n$ is the $n$-th Bernoulli number with $B_1 = -1/2$ and every subtraction of natural
numbers is truncated at $0$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of the bi-bracket product `⊠` (after Bachmann).

Formalized by `MetaMathlibExt.biBracketLambda`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1003](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1003). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-05/index.html#bi-bracket-lambda).

## Bachmann's coefficient $\lambda_{1,1}^1$

Bachmann's coefficient $\lambda_{1,1}^1$ equals
$-1/2$, the Bernoulli number $B_1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of the bi-bracket product `⊠`.

Formalized by `MetaMathlibExt.biBracketLambda_one_one_one`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1011](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1011). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-05/index.html#bi-bracket-lambda-one-one-one).

## Bachmann's product of bi-bracket letters

Write $z_{k,d}$ for the letter indexed by a pair
$(k, d)$ of natural numbers, and let $\lambda_{a,b}^j$ be Bachmann's coefficients. The product of
the letters $z_{k_1,d_1}$ and $z_{k_2,d_2}$ is the formal $\mathbb{Q}$-linear combination of letters

$$z_{k_1,d_1} \boxtimes z_{k_2,d_2} = \binom{d_1 + d_2}{d_1} \Big( \sum_{j=1}^{k_1}
\lambda_{k_1,k_2}^j z_{j,d_1+d_2} + \sum_{j=1}^{k_2} \lambda_{k_2,k_1}^j z_{j,d_1+d_2} +
z_{k_1+k_2,d_1+d_2} \Big).$$

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of the bi-bracket product `⊠` (after Bachmann).

Formalized by `MetaMathlibExt.biBracketDiamond`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1020](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1020). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-05/index.html#bi-bracket-diamond).

## Bi-brackets form a quasi-shuffle algebra

Let $u$ and $v$ be words in the letters $z_{k,d}$,
indexed by pairs $(k, d)$ of natural numbers, with $k \ge 1$ in every letter. Write
$\sum_w c_w w$ for the quasi-shuffle product of $u$ and $v$ induced by Bachmann's letter product
$\boxtimes$, a formal $\mathbb{Q}$-linear combination of words, and $g(w)$ for the bi-bracket of a
word $w$. Then $g(u) g(v) = \sum_w c_w g(w)$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 10 (i).

Stated but not proved: `MetaMathlibExt.biBracket_mul_eq_sum_weightedQuasiShuffle` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1033](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1033). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-05/index.html#bi-bracket-mul-eq-sum-weighted-quasi-shu).

## The map $T$ of the OOZ quasi-shuffle product

Words are finite sequences of letters
$z_k$ with $k$ a natural number. The map $T$ sends each word to a finite formal
$\mathbb{Q}$-linear combination of words: it sends the empty word $\mathbf{1}$ to $\mathbf{1}$,
and a word $z_n v$ with first letter $z_n$ to $z_n v - z_{n-1} v$, where $n - 1$ is truncated
at $0$ (so $T(z_0 v) = 0$).

In the paper $T$ is defined only on a subspace of the combinations of words; here it is defined
on all words.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of the OOZ quasi-shuffle product.

Formalized by `MetaMathlibExt.oozT`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1043](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1043). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-05/index.html#ooz-t).

## The OOZ map fixes the empty word

Let $T$ be the map of the OOZ quasi-shuffle product,
which sends words in letters $z_k$ ($k$ a natural number) to finite formal $\mathbb{Q}$-linear
combinations of words. Then $T$ sends the empty word $\mathbf{1}$ to itself:
$T(\mathbf{1}) = \mathbf{1}$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of the OOZ quasi-shuffle product.

Formalized by `MetaMathlibExt.oozT_nil`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1051](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1051). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-05/index.html#ooz-t-nil).

## The OOZ map on a one-letter word

Let $T$ be the map of the OOZ quasi-shuffle product,
which sends words in letters $z_k$ ($k$ a natural number) to finite formal $\mathbb{Q}$-linear
combinations of words. Then $T$ sends the one-letter word $z_2$ to $z_2 - z_1$:
$T(z_2) = z_2 - z_1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of the OOZ quasi-shuffle product.

Formalized by `MetaMathlibExt.oozT_singleton_two`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1057](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1057). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-05/index.html#ooz-t-singleton-two).

## Stuffle product of formal linear combinations of words

On words in letters $z_k$
($k$ a natural number), the stuffle product $\ast$ is the quasi-shuffle product with letter
product $z_m \diamond z_n = z_{m+n}$: $\mathbf{1} \ast w = w \ast \mathbf{1} = w$ for the empty
word $\mathbf{1}$, and $z_m u \ast z_n v = z_m (u \ast z_n v) + z_n (z_m u \ast v) +
z_{m+n} (u \ast v)$, counted with multiplicity. It is extended $\mathbb{Q}$-bilinearly to finite
formal $\mathbb{Q}$-linear combinations of words: $A \ast B = \sum_{a, b} A_a B_b \, (a \ast b)$,
where $A_a$ is the coefficient of the word $a$ in $A$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of the stuffle product `∗` on `𝔥¹`.

Formalized by `MetaMathlibExt.stuffleComb`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1064](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1064). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-05/index.html#stuffle-comb).

## The empty word is a left unit for the stuffle product

For every word $b$ in letters
$z_k$ ($k$ a natural number), the stuffle product of the empty word $\mathbf{1}$ with $b$ is
$b$: $\mathbf{1} \ast b = b$, as formal $\mathbb{Q}$-linear combinations of words.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Definition of the stuffle product `∗` on `𝔥¹`.

Formalized by `MetaMathlibExt.stuffleComb_single_nil`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1072](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1072). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-05/index.html#stuffle-comb-single-nil).

## OOZ qMZVs respect the OOZ quasi-shuffle product

Identify words in letters $z_k$ with
lists $(k_1, \dots, k_r)$ of natural numbers, and call such a word admissible if every
$k_i \ge 1$ and, when $r \ge 1$, $k_1 \ge 2$. Let $T$ send the empty word $\mathbf{1}$ to
$\mathbf{1}$ and a word $z_n v$ with first letter $z_n$ to the formal $\mathbb{Q}$-linear
combination $z_n v - z_{n-1} v$ (with $n - 1$ truncated at $0$). Extend $T$ and the
Ohno–Okuda–Zudilin qMZV $\zeta_q^{\mathrm{OOZ}}$ $\mathbb{Q}$-linearly to finite formal
$\mathbb{Q}$-linear combinations of words, and let $\ast$ be the stuffle product (the
quasi-shuffle product with letter product $z_m \diamond z_n = z_{m+n}$) of such combinations.
For all admissible words $u$ and $v$, there is exactly one finite formal $\mathbb{Q}$-linear
combination $w$ of admissible words with $T(w) = T(u) \ast T(v)$, and every finite formal
$\mathbb{Q}$-linear combination $w$ of admissible words with $T(w) = T(u) \ast T(v)$ satisfies
$\zeta_q^{\mathrm{OOZ}}(w) = \zeta_q^{\mathrm{OOZ}}(u) \, \zeta_q^{\mathrm{OOZ}}(v)$.

Thus the OOZ quasi-shuffle product, defined by $T(u \ast_{\mathrm{OOZ}} v) = T(u) \ast T(v)$,
is well defined, and $\zeta_q^{\mathrm{OOZ}}$ is multiplicative for it.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 16 (after Castillo Medina, Ebrahimi-Fard and Manchon).

Stated but not proved: `MetaMathlibExt.oozQMZV_mul_eq_of_oozT_eq_stuffleComb` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1085](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1085). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-05/index.html#ooz-qmzv-mul-eq-of-ooz-t-eq-stuffle-comb).

## Weighted chain sums

Let $o_1, \dots, o_\ell$ be a word of markers, each either a natural
number (a weighted position) or a blank (an unweighted position); let $W$ be the set of weighted
positions and $k_t$ the number at position $t \in W$. For natural numbers $M$ and $R$, the
weighted chain sum of the word at bound $M$ and target $R$ is the natural number

$$\sum \prod_{t \in W} \binom{j_t}{k_t},$$

the sum running over strictly decreasing chains $M > a_1 > a_2 > \dots > a_\ell > 0$ of natural
numbers and multiplicities $j_1, \dots, j_\ell \ge 0$ with $a_1 j_1 + \dots + a_\ell j_\ell = R$.
For the empty word ($\ell = 0$) the sum has a single empty term, so the value is $1$ if $R = 0$
and $0$ otherwise, whatever $M$ is.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 1 (the sums over `m₁ > n₁ > ⋯ > m_r > ⋯ > 0` with multiplicities `j, i ≥ 0`).

Formalized by `MetaMathlibExt.bzChainSum`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-05/index.html#bz-chain-sum).

## Marker word of a list of blocks

A marker is either a weight $k \in \mathbb{N}$ (a weighted
position) or a blank (an unweighted position). The marker word of a list of blocks
$(s_1, k_1), \dots, (s_r, k_r)$ of natural numbers is the concatenation, in order, of the words
consisting of the weight $k_t$ followed by $s_t - 1$ blanks (no blanks when $s_t \le 1$).

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 1 (block `t` of the chain is `m_t > n > ⋯ > n` with `d_t - 1` entries `n`).

Formalized by `MetaMathlibExt.bzChainWord`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-06/index.html#bz-chain-word).

## Chain sum of the single block $(1, 1)$

The marker word of the single block $(1, 1)$ is
one position weighted by $1$, and its chain sum with bound $M = 3$ and target $R = 2$ equals $3$:
it is the sum of $\binom{j}{1} = j$ over $0 < m < 3$ and $j \ge 0$ with $m j = 2$, which is
$2 + 1 = 3$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 1 (case `r = 1`, `k₁ = d₁ = 1`, `N = 2`).

Formalized by `MetaMathlibExt.bzChainSum_bzChainWord_one_one`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-06/index.html#bz-chain-sum-bz-chain-word-one-one).

## Combinatorial form of Bradley–Zhao duality

For a list of blocks
$(s_1, w_1), \dots, (s_r, w_r)$ of positive integers and an integer $N \ge 1$, let
$S_N((s_1, w_1), \dots, (s_r, w_r))$ be the sum of $\binom{j_1}{w_1} \cdots \binom{j_r}{w_r}$
over all strictly decreasing chains $N + 1 > a_1 > \dots > a_n > 0$ of length
$n = s_1 + \dots + s_r$ and all multiplicities $c_1, \dots, c_n \ge 0$ with
$a_1 c_1 + \dots + a_n c_n = N$, where the chain is cut into consecutive blocks of lengths
$s_1, \dots, s_r$ and $j_t$ is the multiplicity of the first entry of block $t$. Let $r \ge 1$
and $k_1, \dots, k_r, d_1, \dots, d_r \ge 1$. Then

$$S_N((d_1, k_1), \dots, (d_r, k_r)) = S_N((k_r, d_r), \dots, (k_1, d_1)).$$

The bound $N + 1$ loses nothing: since $w_1 \ge 1$, a nonzero term has $j_1 \ge 1$ and hence
$a_1 \le N$.

## Sources

- arXiv:2111.00051, Theorem 4.18; the record's formula is garbled and is read from there, and the paper's closing remark (equivalence with BZ duality) is not part of this statement.
- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 1.

Stated but not proved: `MetaMathlibExt.bzChainSum_dual` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-06/index.html#bz-chain-sum-dual).

## The SZ dual index

Identify an index $k = (k_1, \dots, k_r)$ of natural numbers with the
word $p^{k_1} y \cdots p^{k_r} y$ in the letters $p$ and $y$, and let $\tilde\tau$ be the
anti-automorphism of words with $\tilde\tau(p) = y$ and $\tilde\tau(y) = p$ (reverse the word and
swap the letters). Write $\tilde\tau(p^{k_1} y \cdots p^{k_r} y)$ as $p^{a_1} y \cdots p^{a_s} y$
followed by a possibly empty run of letters $p$ (nonempty only when $k_1 = 0$); that run is
dropped, and the SZ dual index is $k^\dagger = (a_1, \dots, a_s)$.

For $k = (k_1, \{0\}^{d_1 - 1}, \dots, k_r, \{0\}^{d_r - 1})$ with all $k_i, d_i \ge 1$, where
$\{0\}^m$ stands for $m$ zeros, this gives
$k^\dagger = (d_r, \{0\}^{k_r - 1}, \dots, d_1, \{0\}^{k_1 - 1})$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 5 (SZ duality, the map `τ̃` and the SZ dual index).

Formalized by `MetaMathlibExt.szDualIndex`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-06/index.html#sz-dual-index).

## The SZ dual of $(2)$

The SZ dual index of the one-entry index $(2)$ is $(1, 0)$, that
is, $(2)^\dagger = (1, 0)$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 5 (SZ dual index).

Formalized by `MetaMathlibExt.szDualIndex_two`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-06/index.html#sz-dual-index-two).

## Bradley–Zhao dual index

For an index $k = (k_1, \dots, k_r)$ of natural numbers, form the
word $x^{k_1 - 1} y \cdots x^{k_r - 1} y$ in two letters $x$ and $y$ (each $k_i - 1$ truncated at
$0$); when all $k_i \ge 1$ this is $z_{k_1} \cdots z_{k_r}$ with $z_k = x^{k-1} y$. Apply the
anti-automorphism $\tau$ of words with $\tau(x) = y$ and $\tau(y) = x$, which reverses a word and
swaps its letters, and write the result as $x^{n_1} y \cdots x^{n_s} y \, x^e$. The BZ dual index
of $k$ is $(n_1 + 1, \dots, n_s + 1)$; the trailing $x^e$ is dropped. For an admissible index
($k_1 \ge 2$ and all $k_i \ge 1$, or empty) $e = 0$, so the dual index is the index of
$\tau(z_{k_1} \cdots z_{k_r})$.

Equivalently, it is the SZ dual index of $(k_1 - 1, \dots, k_r - 1)$ with every entry increased
by one.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 7 (BZ duality, the map `τ`).

Formalized by `MetaMathlibExt.bzDualIndex`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-06/index.html#bz-dual-index).

## Bradley–Zhao dual of $(3)$

The Bradley–Zhao dual index of $(3)$ is $(2, 1)$. In terms of
words in the letters $x$ and $y$, with $z_k = x^{k-1} y$ and $\tau$ the anti-automorphism of words
that reverses a word and swaps $x$ and $y$, this says $\tau(z_3) = \tau(x x y) = x y y = z_2 z_1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 7 (BZ duality).

Formalized by `MetaMathlibExt.bzDualIndex_three`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-06/index.html#bz-dual-index-three).

## The tail part of the map $U$

A word is a finite sequence $z_{k_1} \cdots z_{k_s}$ of
letters $z_k$, $k \in \mathbb{N}$. This map sends the empty word to itself and, for $s \ge 1$,
sends $z_{k_1} \cdots z_{k_s}$ to the formal $\mathbb{Q}$-linear combination of words

$$\sum \binom{k_1 - 1}{n_1 - 1} \cdots \binom{k_s - 1}{n_s - 1} \, z_{n_1} \cdots z_{n_s}$$

over $1 \le n_j \le k_j$ for $1 \le j \le s$ (an empty sum is $0$). The map $U$ from OOZ to BZ
words applies it to the letters after the first.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 12 (i) (after Ebrahimi-Fard, Manchon and Singer, the map `U`).

Formalized by `MetaMathlibExt.oozToBZTail`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-06/index.html#ooz-to-bztail).

## The map $U$ from OOZ to BZ words

A word is a finite sequence $z_{k_1} \cdots z_{k_r}$ of
letters $z_k$, $k \in \mathbb{N}$. The map $U$ sends each word to a formal $\mathbb{Q}$-linear
combination of words: $U(\mathbf{1}) = \mathbf{1}$ for the empty word $\mathbf{1}$, and for
$r \ge 1$

$$U(z_{k_1} \cdots z_{k_r}) = \sum \binom{k_1 - 2}{n_1 - 2} \binom{k_2 - 1}{n_2 - 1} \cdots
\binom{k_r - 1}{n_r - 1} \, z_{n_1} \cdots z_{n_r}$$

where the sum runs over $2 \le n_1 \le k_1$ and $1 \le n_j \le k_j$ for $2 \le j \le r$ (an empty
sum is $0$).

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 12 (i) (after Ebrahimi-Fard, Manchon and Singer, the map `U`).

Formalized by `MetaMathlibExt.oozToBZ`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-06/index.html#ooz-to-bz).

## $U$ fixes the empty index

Write $\mathbf{1}$ for the empty index. The map $U$ from OOZ to
BZ indices sends $\mathbf{1}$ to the $\mathbb{Q}$-linear combination of indices consisting of
$\mathbf{1}$ with coefficient $1$; that is, $U(\mathbf{1}) = \mathbf{1}$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 12 (i).

Formalized by `MetaMathlibExt.oozToBZ_nil`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-06/index.html#ooz-to-bz-nil).

## The map $U$ fixes $z_2$

The map $U$ from OOZ to BZ words sends the one-letter word $z_2$
to itself with coefficient $1$: $U(z_2) = z_2$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 12 (i).

Formalized by `MetaMathlibExt.oozToBZ_two`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-06/index.html#ooz-to-bz-two).

## The tail part of the map $V$

Identify an index $(k_1, \dots, k_s)$ of natural numbers
with the word $p^{k_1} y \cdots p^{k_s} y$ in the letters $p$ and $y$. This map sends the empty
word to itself and, for $s \ge 1$, sends $p^{k_1} y \cdots p^{k_s} y$ to the formal
$\mathbb{Q}$-linear combination of words

$$\sum \binom{k_1}{n_1} \cdots \binom{k_s}{n_s} \, p^{n_1} y \cdots p^{n_s} y$$

over $0 \le n_j \le k_j$ for $1 \le j \le s$. The map $V$ from OOZ to SZ words applies it to the
blocks $p^{k_j} y$ after the first.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 12 (ii) (after Ebrahimi-Fard, Manchon and Singer, the map `V`).

Formalized by `MetaMathlibExt.oozToSZTail`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-06/index.html#ooz-to-sztail).

## The map $V$ from OOZ to SZ words

Identify an index $(k_1, \dots, k_r)$ of natural
numbers with the word $p^{k_1} y \cdots p^{k_r} y$ in the letters $p$ and $y$. The map $V$ sends
each such word to a formal $\mathbb{Q}$-linear combination of words: $V(\mathbf{1}) = \mathbf{1}$
for the empty word $\mathbf{1}$, and for $r \ge 1$

$$V(p^{k_1} y \cdots p^{k_r} y) = \sum \binom{k_1 - 1}{n_1 - 1} \binom{k_2}{n_2} \cdots
\binom{k_r}{n_r} \, p^{n_1} y \cdots p^{n_r} y$$

where the sum runs over $1 \le n_1 \le k_1$ and $0 \le n_j \le k_j$ for $2 \le j \le r$ (an empty
sum is $0$).

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 12 (ii) (after Ebrahimi-Fard, Manchon and Singer, the map `V`).

Formalized by `MetaMathlibExt.oozToSZ`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-06/index.html#ooz-to-sz).

## The map $V$ fixes $py$

The map $V$ from OOZ to SZ words sends the word $py$ (the index
$(1)$) to itself with coefficient $1$: $V(py) = py$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 12 (ii).

Formalized by `MetaMathlibExt.oozToSZ_one`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-06/index.html#ooz-to-sz-one).

## OOZ-qMZVs of admissible indices via BZ-qMZVs

Write $\zeta_q^{\mathrm{OOZ}}$ and
$\zeta_q^{\mathrm{BZ}}$ for the Ohno–Okuda–Zudilin and Bradley–Zhao qMZVs. Let
$k = (k_1, \dots, k_r)$ be an index of natural numbers with all $k_i \ge 1$ and, when $r \ge 1$,
$k_1 \ge 2$ (the empty index is allowed). Write the image of $k$ under the map $U$ from OOZ to BZ
indices as a $\mathbb{Q}$-linear combination $U(k) = \sum_w c_w \, w$ of indices. Then
$\zeta_q^{\mathrm{OOZ}}(k) = \sum_w c_w \, \zeta_q^{\mathrm{BZ}}(w)$.

On admissible indices $\zeta_q^{\mathrm{OOZ}}$ is the restricted OOZ-qMZV
$\zeta_q^{\mathrm{OBZ}}$ of the source.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 12 (i).

Stated but not proved: `MetaMathlibExt.oozQMZV_eq_sum_bzQMZV_oozToBZ` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-06/index.html#ooz-qmzv-eq-sum-bz-qmzv-ooz-to-bz).

## The map $U$ is a bijection on combinations of admissible indices

Call an index
$(k_1, \dots, k_r)$ of natural numbers admissible if all $k_i \ge 1$ and, when $r \ge 1$,
$k_1 \ge 2$; the empty index is admissible. Extend the map $U$ from OOZ to BZ indices
$\mathbb{Q}$-linearly to finite $\mathbb{Q}$-linear combinations of indices. This extension maps
the set of $\mathbb{Q}$-linear combinations of admissible indices bijectively onto itself.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 12 (i).

Stated but not proved: `MetaMathlibExt.bijOn_linearCombination_oozToBZ` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-06/index.html#bij-on-linear-combination-ooz-to-bz).

## OOZ-qMZVs via SZ-qMZVs

Write $\zeta_q^{\mathrm{OOZ}}$ and $\zeta_q^{\mathrm{SZ}}$ for the
Ohno–Okuda–Zudilin and Schlesinger–Zudilin qMZVs. Let $k = (k_1, \dots, k_r)$ be an index of
natural numbers that is empty or has $k_1 \ge 1$ (the entries $k_2, \dots, k_r$ may be $0$).
Write the image of $k$ under the map $V$ from OOZ to SZ indices as a $\mathbb{Q}$-linear
combination $V(k) = \sum_w c_w \, w$ of indices. Then
$\zeta_q^{\mathrm{OOZ}}(k) = \sum_w c_w \, \zeta_q^{\mathrm{SZ}}(w)$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 12 (ii).

Stated but not proved: `MetaMathlibExt.oozQMZV_eq_sum_szQMZV_oozToSZ` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-06/index.html#ooz-qmzv-eq-sum-sz-qmzv-ooz-to-sz).

## The map $V$ is a bijection on combinations of SZ-admissible indices

Call an index
$(k_1, \dots, k_r)$ of natural numbers SZ-admissible if it is empty or $k_1 \ge 1$ (the entries
$k_2, \dots, k_r$ may be $0$). Extend the map $V$ from OOZ to SZ indices $\mathbb{Q}$-linearly to
finite $\mathbb{Q}$-linear combinations of indices. This extension maps the set of
$\mathbb{Q}$-linear combinations of SZ-admissible indices bijectively onto itself.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 12 (ii).

Stated but not proved: `MetaMathlibExt.bijOn_linearCombination_oozToSZ` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1265](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-06/index.html#bij-on-linear-combination-ooz-to-sz).

## Duality for restricted OOZ-qMZVs

Call an index $(k_1, \dots, k_r)$ of natural numbers
admissible if $k_j \ge 1$ for all $j$ and, when $r \ge 1$, $k_1 \ge 2$. Extend
$\zeta_q^{\mathrm{OOZ}}$ and the map $U$ linearly to formal $\mathbb{Q}$-linear combinations of
indices, and let $\tau$ act on such a combination by replacing each index with its BZ dual index.
Let $w$ be an admissible index and let $x$ be a $\mathbb{Q}$-linear combination of admissible
indices with $U(x) = \tau(U(w))$. Then $\zeta_q^{\mathrm{OOZ}}(x) = \zeta_q^{\mathrm{OOZ}}(w)$.

Since $U$ is a bijection on combinations of admissible indices (Proposition 12 (i) of the source),
this is the identity
$\zeta_q^{\mathrm{OOZ}} = \zeta_q^{\mathrm{OOZ}} \circ U^{-1} \circ \tau \circ U$ on
admissible indices.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 17 (i) (after Ebrahimi-Fard, Manchon and Singer).

Stated but not proved: `MetaMathlibExt.sum_oozQMZV_eq_of_oozToBZ_eq_bzDual` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-06/index.html#sum-ooz-qmzv-eq-of-ooz-to-bz-eq-bz-dual).

## Duality for OOZ-qMZVs

Call an index $(k_1, \dots, k_r)$ of natural numbers SZ-admissible
if it is empty or $k_1 \ge 1$. Extend $\zeta_q^{\mathrm{OOZ}}$ and the map $V$ linearly to formal
$\mathbb{Q}$-linear combinations of indices, and let $\tilde\tau$ act on such a combination by
replacing each index with its SZ dual index. Let $w$ be an SZ-admissible index and let $x$ be a
$\mathbb{Q}$-linear combination of SZ-admissible indices with $V(x) = \tilde\tau(V(w))$. Then
$\zeta_q^{\mathrm{OOZ}}(x) = \zeta_q^{\mathrm{OOZ}}(w)$.

Since $V$ is a bijection on combinations of SZ-admissible indices (Proposition 12 (ii) of the
source), this is the identity
$\zeta_q^{\mathrm{OOZ}} = \zeta_q^{\mathrm{OOZ}} \circ V^{-1} \circ \tilde\tau \circ V$ on
SZ-admissible indices.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 17 (ii) (after Ebrahimi-Fard, Manchon and Singer).

Stated but not proved: `MetaMathlibExt.sum_oozQMZV_eq_of_oozToSZ_eq_szDual` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1288](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-06/index.html#sum-ooz-qmzv-eq-of-ooz-to-sz-eq-sz-dual).

## Partial sums of SZ-star qMZVs

For an index $k = (k_1, \dots, k_r)$ of natural numbers and
a bound $M \in \mathbb{N}$, the partial sum is the formal power series in $q$ over $\mathbb{Q}$

$$
\sum_{M \ge m_1 \ge \dots \ge m_r > 0} \prod_{j=1}^{r} \frac{q^{m_j k_j}}{(1 - q^{m_j})^{k_j}};
$$

for the empty index it is $1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 17 (iii) (SZ-star qMZVs, defining sum truncated at `m₁ ≤ M`).

Formalized by `MetaMathlibExt.szStarQMZVPartial`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1299](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-07/index.html#sz-star-qmzvpartial).

## SZ-star qMZVs

For an index $k = (k_1, \dots, k_r)$ of natural numbers, the SZ-star qMZV
$\zeta_q^{SZ,\star}(k)$ is the formal power series in $q$ over $\mathbb{Q}$

$$
\zeta_q^{SZ,\star}(k_1, \dots, k_r) =
\sum_{m_1 \ge \dots \ge m_r > 0} \prod_{j=1}^{r} \frac{q^{m_j k_j}}{(1 - q^{m_j})^{k_j}},
$$

with $\zeta_q^{SZ,\star}(\varnothing) = 1$. Precisely, its coefficient of $q^N$ is defined as the
coefficient of $q^N$ in the partial sum over $N \ge m_1 \ge \dots \ge m_r > 0$. For $k_1 \ge 1$ the
summands with $m_1 > N$ have $q$-adic order $> N$, so this is the coefficient of $q^N$ in the full
sum; for $k_1 = 0$ the full sum is not a formal power series and the value is a junk value.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 17 (iii) (the map `ζ_q^{SZ,⋆}` of SZ-star qMZVs).

Formalized by `MetaMathlibExt.szStarQMZV`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-07/index.html#sz-star-qmzv).

## The empty SZ-star qMZV

The SZ-star qMZV of the empty index is $1$:
$\zeta_q^{SZ,\star}(\varnothing) = 1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 17 (iii).

Formalized by `MetaMathlibExt.szStarQMZV_nil`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1317](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-07/index.html#sz-star-qmzv-nil).

## The coefficient of $q$ in $\zeta_q^{SZ,\star}(1)$

The coefficient of $q$ in the SZ-star
qMZV $\zeta_q^{SZ,\star}(1) = \sum_{m > 0} q^m / (1 - q^m)$ is $1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 17 (iii).

Formalized by `MetaMathlibExt.coeff_one_szStarQMZV_singleton_one`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1325](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-07/index.html#coeff-one-sz-star-qmzv-singleton-one).

## OOZ-qMZVs are SZ-star qMZVs of the dual index

For every index $k = (k_1, \dots, k_r)$ of
natural numbers that is empty or has $k_1 \ge 1$, the Ohno–Okuda–Zudilin qMZV of $k$ equals the
SZ-star qMZV of the SZ dual index $k^\dagger$: $\zeta_q^{OOZ}(k) = \zeta_q^{SZ,\star}(k^\dagger)$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Theorem 17 (iii) (after Ebrahimi-Fard, Manchon and Singer).

Stated but not proved: `MetaMathlibExt.oozQMZV_eq_szStarQMZV_szDualIndex` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1333](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-07/index.html#ooz-qmzv-eq-sz-star-qmzv-sz-dual-index).

## The map from TBZ words to SZ indices

Words in the letters $\bar{1}$ and $k \in \mathbb{N}$
are sent to formal $\mathbb{Q}$-linear combinations of finite sequences of natural numbers (SZ
indices) letter by letter: the empty word goes to the empty index with coefficient $1$, and a
word $x w$ with first letter $x$ goes to the image of $w$ with a new first entry prepended to each
index, where $\bar{1}$ contributes the entry $1$ and a letter $k$ contributes the sum of the two
terms obtained with the entries $k$ and $k - 1$ (subtraction truncated at $0$, so the letter $0$
gives the entry $0$ with coefficient doubled). This is the map $U_{\mathrm{TBZ}}$ on words.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 9 (i) (the map `U_TBZ`).

Formalized by `MetaMathlibExt.tbzToSZ`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-07/index.html#tbz-to-sz).

## The TBZ-to-SZ map on the letter $\bar{1}$

The map $U_{\mathrm{TBZ}}$ sends the one-letter
word $\bar{1}$ to the index $(1)$ with coefficient $1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 9 (i).

Formalized by `MetaMathlibExt.tbzToSZ_bar`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1352](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-07/index.html#tbz-to-sz-bar).

## The map $V_{TBZ}$ from SZ indices to TBZ words

For an index $k = (k_1, \dots, k_r)$ of
natural numbers, $V_{TBZ}(k)$ is the formal $\mathbb{Q}$-linear combination of TBZ words (words in
the letters $\bar 1$ and $j \ge 1$; write $z_a$ for the one-letter word $a$) obtained by replacing
each letter $k_i = 0$ by $z_1 - z_{\bar 1}$ and each letter $k_i \ge 1$ by
$\sum_{j=1}^{k_i} (-1)^{k_i - j} z_{j'}$, where $j' = \bar 1$ for $j = 1$ and $j' = j$ otherwise,
and multiplying out by concatenation of words. The empty index goes to the empty word with
coefficient $1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 9 (ii) (the map `V_TBZ`).

Formalized by `MetaMathlibExt.szToTBZ`, a definition declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-07/index.html#sz-to-tbz).

## The map $V_{TBZ}$ on the index $(1)$

The map $V_{TBZ}$ sends the SZ index $(1)$ to the
one-letter TBZ word $\bar 1$ with coefficient $1$.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 9 (ii).

Formalized by `MetaMathlibExt.szToTBZ_one`, a theorem declared in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1372](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-07/index.html#sz-to-tbz-one).

## TBZ-qMZVs in the SZ model

Let $w = (w_1, \dots, w_r)$ be a TBZ word: each letter is
either $\bar 1$ or a natural number $k \ge 1$, and $w_1$ is not the number $1$. Let
$U_{TBZ}(w) = \sum_v c_v\, v$ be the formal $\mathbb{Q}$-linear combination of SZ indices obtained
by replacing each letter $\bar 1$ by $1$ and each letter $k$ by $k$ or by $k - 1$, summed over all
choices. Then the Takeyama–Bradley–Zhao qMZV of $w$ is the corresponding combination of
Schlesinger–Zudilin qMZVs: $\zeta_q^{TBZ}(w) = \sum_v c_v\, \zeta_q^{SZ}(v)$.

In block form, writing $\{a\}^d$ for $d$ copies of the letter $a$: for $d_1, \dots, d_s \ge 0$ and
$k_1, \dots, k_{s-1} \ge 1$ with $k_1 \ge 2$ if $d_1 = 0$,

$$
\zeta_q^{TBZ}(\{\bar 1\}^{d_1}, k_1, \{\bar 1\}^{d_2}, \dots, k_{s-1}, \{\bar 1\}^{d_s}) =
\sum_{\delta \in \{0,1\}^{s-1}} \zeta_q^{SZ}(\{1\}^{d_1}, k_1 - \delta_1, \{1\}^{d_2}, \dots,
k_{s-1} - \delta_{s-1}, \{1\}^{d_s}).
$$

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 9 (i).

Stated but not proved: `MetaMathlibExt.tbzQMZV_eq_sum_szQMZV_tbzToSZ` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1382](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-07/index.html#tbz-qmzv-eq-sum-sz-qmzv-tbz-to-sz).

## SZ-qMZVs in the TBZ model

Let $k = (k_1, \dots, k_r)$ be an index of natural numbers
that is empty or has $k_1 \ge 1$. Let $V_{TBZ}(k) = \sum_w c_w\, w$ be the formal
$\mathbb{Q}$-linear combination of TBZ words (words in the letters $\bar 1$ and $j \ge 1$; write
$z_a$ for the one-letter word $a$) obtained by replacing each letter $k_i = 0$ by
$z_1 - z_{\bar 1}$ and each letter $k_i \ge 1$ by $\sum_{j=1}^{k_i} (-1)^{k_i - j} z_{j'}$, where
$j' = \bar 1$ for $j = 1$ and $j' = j$ otherwise, and multiplying out by concatenation of words.
Then the Schlesinger–Zudilin qMZV of $k$ is the corresponding combination of
Takeyama–Bradley–Zhao qMZVs: $\zeta_q^{SZ}(k) = \sum_w c_w\, \zeta_q^{TBZ}(w)$, that is,
$\zeta_q^{SZ}(k) = \zeta_q^{TBZ}(V_{TBZ}(k))$ with $\zeta_q^{TBZ}$ extended
$\mathbb{Q}$-linearly.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 9 (ii).

Stated but not proved: `MetaMathlibExt.szQMZV_eq_sum_tbzQMZV_szToTBZ` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1392](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-07/index.html#sz-qmzv-eq-sum-tbz-qmzv-sz-to-tbz).

## Duality for TBZ-qMZVs

Let $w$ be a TBZ word: each letter is either $\bar 1$ or a natural
number $k \ge 1$, and the first letter is not the number $1$. Let $U_{TBZ}(w) = \sum_v c_v\, v$ be
the formal $\mathbb{Q}$-linear combination of SZ indices obtained by replacing each letter $\bar 1$
by $1$ and each letter $k$ by $k$ or by $k - 1$, summed over all choices. For an SZ index
$u = (u_1, \dots, u_s)$ of natural numbers, let $V_{TBZ}(u) = \sum_x d_{u,x}\, x$ be the formal
$\mathbb{Q}$-linear combination of TBZ words obtained by replacing each letter $u_i = 0$ by
$z_1 - z_{\bar 1}$ and each letter $u_i \ge 1$ by $\sum_{j=1}^{u_i} (-1)^{u_i - j} z_{j'}$, where
$z_a$ is the one-letter word $a$, $j' = \bar 1$ for $j = 1$ and $j' = j$ otherwise, and
multiplying out by concatenation of words. Then the Takeyama–Bradley–Zhao qMZVs satisfy

$$
\zeta_q^{TBZ}(w) = \sum_v c_v \sum_x d_{v^\dagger, x}\, \zeta_q^{TBZ}(x),
$$

where $v^\dagger$ is the SZ dual index of $v$; that is,
$\zeta_q^{TBZ} = \zeta_q^{TBZ} \circ V_{TBZ} \circ \tilde\tau \circ U_{TBZ}$ on such words, where
$\tilde\tau$ is the dual-index map and $V_{TBZ}$, $\tilde\tau$ and $\zeta_q^{TBZ}$ are extended
$\mathbb{Q}$-linearly.

## Sources

- Benjamin Brindle, *A Unified Approach to qMZVs*, INTEGERS 24 (2024), Article A6, Proposition 8 (after Takeyama).

Stated but not proved: `MetaMathlibExt.tbzQMZV_eq_sum_tbzQMZV_szToTBZ_szDual` is written with `theorem_wanted` in [WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean, line 1401](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QMultipleZetaValuesWanted.lean#L1401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/part-07/index.html#tbz-qmzv-eq-sum-tbz-qmzv-sz-to-tbz-sz-du).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: q-analogues of multiple zeta values](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/q-analogues-of-multiple-zeta-values)
