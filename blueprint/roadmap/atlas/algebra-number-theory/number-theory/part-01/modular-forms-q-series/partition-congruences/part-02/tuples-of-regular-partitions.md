---
declaration: section
origin: cited
lean: MetaMathlibExt.lRegularPartitionCount, MetaMathlibExt.kTupleRegularPartitionCount, MetaMathlibExt.kTupleRegularPartitionCount_zero, MetaMathlibExt.kTupleRegularPartitionCount_succ, MetaMathlibExt.tripleRegularPartitionCount, MetaMathlibExt.lRegularPartitionCount_zero, MetaMathlibExt.kTupleRegularPartitionCount_at_zero, MetaMathlibExt.boundedBilateralSeries
statement: formalized
---

# Tuples of ℓ-regular partitions

38 results, 14 proved and 24 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html).

## Number of $\ell$-regular partitions

For natural numbers $\ell$ and $n$, the number of
$\ell$-regular partitions of $n$ is the number of partitions of $n$ none of whose parts is
divisible by $\ell$.

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Introduction (definition of ℓ-regular partitions).

Formalized by `MetaMathlibExt.lRegularPartitionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#l-regular-partition-count).

## Number of $k$-tuples of $\ell$-regular partitions

For natural numbers $\ell$, $k$ and
$n$, the number $T_{\ell,k}(n)$ is defined by recursion on $k$: $T_{\ell,0}(n)$ is $1$ if
$n = 0$ and $0$ otherwise, and

$$T_{\ell,k+1}(n) = \sum_{i=0}^{n} r_\ell(i) \, T_{\ell,k}(n-i),$$

where $r_\ell(i)$ is the number of $\ell$-regular partitions of $i$.

Peeling off the first component in this way, $T_{\ell,k}(n)$ counts the $k$-tuples
$(\lambda_1, \dots, \lambda_k)$ of $\ell$-regular partitions of $n_1, \dots, n_k$ with
$n_1 + \dots + n_k = n$.

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Introduction (definition of `T_{ℓ,k}`).

Formalized by `MetaMathlibExt.kTupleRegularPartitionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#k-tuple-regular-partition-count).

## The empty tuple of $\ell$-regular partitions

For all natural numbers $\ell$ and $n$,
writing $T_{\ell,k}(n)$ for the number of $k$-tuples of $\ell$-regular partitions with total
$n$, we have $T_{\ell,0}(n) = 1$ if $n = 0$ and $T_{\ell,0}(n) = 0$ otherwise.

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Introduction (definition of `T_{ℓ,k}`).

Formalized by `MetaMathlibExt.kTupleRegularPartitionCount_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#k-tuple-regular-partition-count-zero).

## Recurrence for tuples of $\ell$-regular partitions

For all natural numbers $\ell$, $k$
and $n$, writing $r_\ell(i)$ for the number of $\ell$-regular partitions of $i$ and
$T_{\ell,k}(n)$ for the number of $k$-tuples of $\ell$-regular partitions with total $n$,

$$T_{\ell,k+1}(n) = \sum_{i=0}^{n} r_\ell(i) \, T_{\ell,k}(n-i).$$

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Introduction (definition of `T_{ℓ,k}`).

Formalized by `MetaMathlibExt.kTupleRegularPartitionCount_succ`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#k-tuple-regular-partition-count-succ).

## Triples of $\ell$-regular partitions

For natural numbers $\ell$ and $n$,
$T_\ell(n) = T_{\ell,3}(n)$ is the number of triples $(\lambda_1, \lambda_2, \lambda_3)$ of
$\ell$-regular partitions (partitions with no part divisible by $\ell$) whose sizes add up to
$n$.

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Introduction (definition of `T_ℓ`).

Formalized by `MetaMathlibExt.tripleRegularPartitionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#triple-regular-partition-count).

## Zero has one $\ell$-regular partition

For every natural number $\ell$, the number of
$\ell$-regular partitions of $0$ is $1$; the only one is the empty partition.

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Introduction (definition of ℓ-regular partitions).

Formalized by `MetaMathlibExt.lRegularPartitionCount_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#l-regular-partition-count-zero).

## One tuple of $\ell$-regular partitions of total zero

For all natural numbers $\ell$
and $k$, writing $T_{\ell,k}(n)$ for the number of $k$-tuples of $\ell$-regular partitions
with total $n$, we have $T_{\ell,k}(0) = 1$: the only such tuple of total $0$ is the tuple of
empty partitions.

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Introduction (definition of `T_{ℓ,k}`).

Formalized by `MetaMathlibExt.kTupleRegularPartitionCount_at_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#k-tuple-regular-partition-count-at-zero).

## Bounded bilateral series

Given functions $e, w : \mathbb{Z} \to \mathbb{Z}$, the
bounded bilateral series of $e$ and $w$ is the power series over $\mathbb{Z}$ whose
coefficient of $q^n$, for each natural number $n$, is the sum of $w(m)$ over the integers
$m$ with $-n-1 \le m \le n+1$ and $e(m) = n$.

It agrees with the bilateral series $\sum_{m \in \mathbb{Z}} w(m) q^{e(m)}$ whenever $e$
takes no negative values and, for every natural number $n$, every integer $m$ with $e(m) = n$
satisfies $|m| \le n + 1$, as holds for the quadratic exponents used in Lemmas 1, 3 and 5 of
the source; it is not intended for other exponents.

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Encoding for Lemmas 1, 3, and 5.

Formalized by `MetaMathlibExt.boundedBilateralSeries`, a definition declared in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#bounded-bilateral-series).

## Coefficients of the bounded bilateral series

For all functions
$e, w : \mathbb{Z} \to \mathbb{Z}$ and every natural number $n$, the coefficient of $q^n$ in
the bounded bilateral series of $e$ and $w$ equals the sum of $w(m)$ over the integers $m$
with $-n-1 \le m \le n+1$ and $e(m) = n$.

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Encoding for Lemmas 1, 3, and 5.

Formalized by `MetaMathlibExt.coeff_boundedBilateralSeries`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#coeff-bounded-bilateral-series).

## Truncated one-sided series

For functions $e : \mathbb{N} \to \mathbb{N}$ and
$w : \mathbb{N} \to \mathbb{Z}$, this is the integer power series whose coefficient of $q^n$ is
the sum of $w(m)$ over the integers $m$ with $1 \le m \le n$ and $e(m) = n$.

When $e(m) \ge m$ for every $m \ge 1$, as for the square exponents in Lemma 5 and
Corollary 3, this series is $\sum_{m \ge 1} w(m) q^{e(m)}$.

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Encoding for Lemma 5 and Corollary 3.

Formalized by `MetaMathlibExt.positiveUnilateralSeries`, a definition declared in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#positive-unilateral-series).

## Coefficients of the positive unilateral series

For all functions
$e : \mathbb{N} \to \mathbb{N}$ and $w : \mathbb{N} \to \mathbb{Z}$ and every natural number
$n$, the coefficient of $q^n$ in the positive unilateral series of $e$ and $w$ equals the sum
of $w(m)$ over the natural numbers $m$ with $1 \le m \le n$ and $e(m) = n$.

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Encoding for Lemma 5 and Corollary 3.

Formalized by `MetaMathlibExt.coeff_positiveUnilateralSeries`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#coeff-positive-unilateral-series).

## Congruences modulo 24 for triples of 2-regular partitions

Let $T_2(n)$ be the number of
triples of 2-regular partitions (partitions with no even part) whose sizes add up to $n$. If
$t$ is a positive integer with $\gcd(t, 6) = 1$ and $N \in \{33, 57\}$, then for every natural
number $n$,

$$T_2\left(9n + \frac{N t^2 - 1}{8}\right) \equiv 0 \pmod{24}.$$

Here $N t^2 - 1$ is divisible by $8$, so the fraction is an integer.

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Theorem 1, equation T29n24.

Stated but not proved: `MetaMathlibExt.tripleTwo_mod_twentyFour` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#triple-two-mod-twenty-four).

## The Nath–Saikia–Sarma conjecture

Let $T_2(n)$ be the number of triples of 2-regular
partitions (partitions with no even part) whose sizes add up to $n$. Let $p \ge 5$ be a prime
with Legendre symbol $\left(\frac{-2}{p}\right) = -1$, and let $t$ be a positive integer with
$\gcd(t, 6) = 1$ and $p \mid t$. Then for every natural number $n$ and every $j$ with
$1 \le j \le p - 1$,

$$T_2\left(9t^2 n + \frac{9t^2 j}{p} + \frac{57t^2 - 1}{8}\right) \equiv 0 \pmod{6}.$$

Both fractions are integers under these hypotheses.

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Corollary 1 (Conjecture conj.nss).

Stated but not proved: `MetaMathlibExt.nathSaikiaSarma_conjecture` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#nath-saikia-sarma-conjecture).

## Congruences modulo 8 and 24 for triples of 2-regular partitions

Let $T_2(n)$ be the
number of triples of $2$-regular partitions (partitions with no even part) whose sizes add up to
$n$. Let $p$ be a prime with $p \equiv 3$, $5$ or $7 \pmod 8$, and let $n$ and $\alpha$ be
natural numbers with $p \nmid n$. Then

$$T_2\left(p^{2\alpha+1} n + \frac{p^{2\alpha+2}-1}{8}\right) \equiv 0 \pmod 8,$$

and if moreover $3 \nmid n$, this value is also $\equiv 0 \pmod{24}$.

The division by $8$ is exact because $p$ is odd.

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Theorem 2, equations thm.p357mod8 and mod24.

Stated but not proved: `MetaMathlibExt.tripleTwo_primePower_mod_eight_and_twentyFour` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#triple-two-prime-power-mod-eight-and-twe).

## Prime-power congruences modulo 24 for triples of 2-regular partitions

Let $T_2(n)$ be
the number of triples of 2-regular partitions (partitions with no even part) whose sizes add up
to $n$. Let $p \ne 3$ be a prime with $p \equiv 3$, $5$ or $7 \pmod 8$. Then for all natural
numbers $n$ and $\alpha$ with $p \nmid n$,

$$T_2\left(9 p^{2\alpha+1} n + \frac{9 p^{2\alpha+2} - 1}{8}\right) \equiv 0 \pmod{24}.$$

Since $p$ is odd, the fraction is an integer.

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Corollary 2, equation cor.9pmod24.

Stated but not proved: `MetaMathlibExt.tripleTwo_nine_primePower_mod_twentyFour` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#triple-two-nine-prime-power-mod-twenty-f).

## A fifth-power Euler product identity

Write $f_k = \prod_{i \ge 1} (1 - q^{ki})$ for the
Euler products, as integer power series in $q$. Then

$$f_1^5 = f_2^2 \sum_{m \in \mathbb{Z}} (6m + 1)\, q^{m(3m+1)/2}.$$

This is the identity $f_1^5 / f_2^2 = \sum_{m \in \mathbb{Z}} (6m + 1)\, q^{m(3m+1)/2}$ with the
denominator cleared. The coefficient of $q^n$ in the sum is computed over the integers $m$ with
$|m| \le n + 1$, which include every solution of $m(3m+1)/2 = n$.

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Lemma 3, equation f15/f22.

Stated but not proved: `MetaMathlibExt.qEulerProduct_fifth_power_identity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#q-euler-product-fifth-power-identity).

## A signed Euler product identity

Write $f_k = \prod_{i \ge 1} (1 - q^{ki})$ for the Euler
products, as integer power series in $q$, and let $(-q;-q)_\infty = \prod_{i \ge 1} (1 - (-q)^i)$
be $f_1$ with $q$ replaced by $-q$. Then

$$(-q;-q)_\infty \, f_1 f_4 = f_2^3.$$

This is the identity $(-q;-q)_\infty = f_2^3 / (f_1 f_4)$ with the denominator cleared.

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Lemma 4, equation f1-q.

Stated but not proved: `MetaMathlibExt.rescale_neg_one_qEulerProduct_identity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#rescale-neg-one-q-euler-product-identity).

## Gauss's theta identity for the Euler products

Write $f_k = \prod_{i \ge 1} (1 - q^{ki})$
for the Euler products, as integer power series in $q$, and let
$\theta = \sum_{m \in \mathbb{Z}} (-1)^m q^{m^2}$. Then $f_1^2 = f_2\, \theta$ and
$\theta = 1 + 2 \sum_{m \ge 1} (-1)^m q^{m^2}$.

The coefficient of $q^n$ in each sum is computed over the indices $m$ with $|m| \le n + 1$
(respectively $1 \le m \le n$), which include every solution of $m^2 = n$.

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Lemma 5, equation f12/f2.

Stated but not proved: `MetaMathlibExt.qEulerProduct_square_theta_identity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#q-euler-product-square-theta-identity).

## The theta identity for the second Euler product

Write
$f_k = \prod_{i \ge 1} (1 - q^{ki})$ for the Euler products, as integer power series in $q$. Then

$$f_2^2 = f_4 \left(1 + 2 \sum_{n \ge 1} (-1)^n q^{2n^2}\right).$$

This is the identity for $f_2^2 / f_4$ with the denominator cleared.

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Corollary 3, equation f22/f4.

Stated but not proved: `MetaMathlibExt.qEulerProduct_two_square_identity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#q-euler-product-two-square-identity).

## Iterated prime-power congruence for Euler products

For a natural number $l$ write
$f_l = \prod_{i \ge 1} (1 - q^{li})$, an integer power series in $q$. Let $p$ be a prime and let
$k, l, s, m$ be natural numbers with $l \ge 1$, $s \ge 1$, $m \ge 1$ and $s \le k$. Then for
every natural number $n$, the coefficients of $q^n$ in $f_l^{p^k m}$ and in
$f_{l p^s}^{p^{k-s} m}$ are congruent modulo $p^{k-s+1}$.

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Lemma 7, equation cor.modp^k.

Stated but not proved: `MetaMathlibExt.qEulerProduct_iterated_primePower_congruence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#q-euler-product-iterated-prime-power-con).

## Parity of triples of 2-regular partitions

For a natural number $n$, let $T_2(n)$ be the
number of triples of $2$-regular partitions (partitions with no even part) whose sizes add up to
$n$. Then $T_2(n)$ is odd if and only if $n$ is a triangular number, that is, $n = m(m+1)/2$
for some natural number $m$.

Allowing integer $m$ gives no new values, since $m$ and $-m-1$ give the same triangular number.

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Lemma 8, equation mod2.

Stated but not proved: `MetaMathlibExt.tripleTwo_odd_iff_triangular` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#triple-two-odd-iff-triangular).

## Prime-power congruences for $k$-tuples of $\ell$-regular partitions

Write $T_{\ell,k}(n)$
for the number of $k$-tuples of $\ell$-regular partitions with total $n$. Let $p$ be a prime,
let $m$, $\ell$ and $s$ be positive integers, let $\alpha \ge s$ and $r$ be natural numbers
with $1 \le r \le p^s - 1$. Then for every natural number $n$,

$$T_{\ell,p^\alpha m}(p^s n + r) \equiv 0 \pmod{p^{\alpha - s + 1}}.$$

Since $s$ is positive, the hypothesis $\alpha \ge s$ also gives $\alpha \ge 1$.

## Sources

- Bishnu Paudel, James A. Sellers, and Haiyang Wang, *Extending Recent Work of Nath, Saikia, and Sarma on k-Tuple ℓ-Regular Partitions*, INTEGERS 26 (2026), Article A4, Theorem 3, equation thm.gen1.1.

Stated but not proved: `MetaMathlibExt.kTupleRegularPartition_primePower_congruent` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KTupleRegularPartitionsWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#k-tuple-regular-partition-prime-power-co).

## Regular tripartition counts

For natural numbers $\ell$ and $n$, $T_\ell(n)$ is the number
of triples $(\lambda_1, \lambda_2, \lambda_3)$ of integer partitions with
$|\lambda_1| + |\lambda_2| + |\lambda_3| = n$ in which no part of any $\lambda_i$ is divisible by
$\ell$; these triples are the $\ell$-regular tripartitions of $n$.

## Sources

- Mohammed L. Nadji and Moussa Ahmia, *Congruences for l-Regular Tripartitions for l in {2,3}*, INTEGERS 24 (2024), Article A86, Section 1, definition of `T_ℓ(n)` (with generating function `f_ℓ³ / f_1³`, Section 1, eq. (1)).

Formalized by `MetaMathlibExt.regularTripartitionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#regular-tripartition-count).

## The regular tripartition count at zero

For every natural number $\ell$, $T_\ell(0) = 1$,
where $T_\ell(n)$ is the number of $\ell$-regular tripartitions of $n$: the only tripartition of
$0$ is the triple of empty partitions.

## Sources

- Mohammed L. Nadji and Moussa Ahmia, *Congruences for l-Regular Tripartitions for l in {2,3}*, INTEGERS 24 (2024), Article A86 (definition of `T_ℓ(n)`).

Formalized by `MetaMathlibExt.regularTripartitionCount_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#regular-tripartition-count-zero).

## The number of $\ell$-regular tripartitions of $1$

For every natural number $\ell \ne 1$,
the number $T_\ell(1)$ of $\ell$-regular tripartitions of $1$ is $3$: the single part $1$ lies in
one of the three components.

## Sources

- Mohammed L. Nadji and Moussa Ahmia, *Congruences for l-Regular Tripartitions for l in {2,3}*, INTEGERS 24 (2024), Article A86 (definition of `T_ℓ(n)`).

Formalized by `MetaMathlibExt.regularTripartitionCount_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#regular-tripartition-count-one).

## Congruences modulo 3 and 6 for 2-regular tripartitions

Let $T_2(m)$ be the number of
$2$-regular tripartitions of $m$. For every natural number $n$, $3 \mid T_2(3n + 1)$ and
$6 \mid T_2(3n + 2)$.

## Sources

- Mohammed L. Nadji and Moussa Ahmia, *Congruences for l-Regular Tripartitions for l in {2,3}*, INTEGERS 24 (2024), Article A86, Corollary 1.

Stated but not proved: `MetaMathlibExt.regularTripartitionCount_two_mod_three_six` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#regular-tripartition-count-two-mod-three).

## Congruences modulo 3 and 9 for 3-regular tripartitions

Let $T_3(m)$ be the number of
$3$-regular tripartitions of $m$. For every natural number $n$, $3 \mid T_3(3n + 1)$ and
$9 \mid T_3(3n + 2)$.

## Sources

- Mohammed L. Nadji and Moussa Ahmia, *Congruences for l-Regular Tripartitions for l in {2,3}*, INTEGERS 24 (2024), Article A86, Corollary 2 (congruences (53), (54)).

Stated but not proved: `MetaMathlibExt.regularTripartitionCount_three_mod_three_nine` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#regular-tripartition-count-three-mod-thr).

## A congruence modulo 6 for 3-regular tripartitions

Let $T_3(m)$ be the number of
$3$-regular tripartitions of $m$. For every natural number $n$, $6 \mid T_3(6n + 4)$.

## Sources

- Mohammed L. Nadji and Moussa Ahmia, *Congruences for l-Regular Tripartitions for l in {2,3}*, INTEGERS 24 (2024), Article A86, Corollary 3 (congruence (64)).

Stated but not proved: `MetaMathlibExt.regularTripartitionCount_three_six_mul_add_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#regular-tripartition-count-three-six-mul).

## Even 2-regular tripartition counts for primes at least 5

Let $T_2(n)$ be the number of
2-regular tripartitions of $n$. For every prime $p \ge 5$, all natural numbers $\alpha$ and $n$,
and every $i$ with $1 \le i \le p - 1$, the number
$T_2\bigl(3 p^{2\alpha+1} (p n + i) + (p^{2\alpha+2} - 1)/8\bigr)$ is even (the division is
exact).

## Sources

- Mohammed L. Nadji and Moussa Ahmia, *Congruences for l-Regular Tripartitions for l in {2,3}*, INTEGERS 24 (2024), Article A86, Theorem 1 (congruence (13)).

Stated but not proved: `MetaMathlibExt.regularTripartitionCount_two_prime_ge_five_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#regular-tripartition-count-two-prime-ge).

## Even 2-regular tripartition counts for odd primes

Let $T_2(n)$ be the number of 2-regular
tripartitions of $n$. For every odd prime $p$, all natural numbers $\alpha$ and $n$, and every $i$
with $1 \le i \le p - 1$, the number
$T_2\bigl(9 p^{2\alpha+1} (p n + i) + (9 p^{2\alpha+2} - 1)/8\bigr)$ is even (the division is
exact).

## Sources

- Mohammed L. Nadji and Moussa Ahmia, *Congruences for l-Regular Tripartitions for l in {2,3}*, INTEGERS 24 (2024), Article A86, Theorem 2 (congruence (21)).

Stated but not proved: `MetaMathlibExt.regularTripartitionCount_two_odd_prime_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#regular-tripartition-count-two-odd-prime).

## A congruence modulo 3 for 3-regular tripartitions at primes $p \equiv 3 \pmod 4$

Let
$T_3(m)$ be the number of $3$-regular tripartitions of $m$, and let $p$ be a prime with
$p \equiv 3 \pmod 4$. For all natural numbers $\alpha$ and $n$ and every integer $i$ with
$1 \le i \le p - 1$,

$$
T_3\Bigl(3 p^{2\alpha+1} (p n + i) + \frac{p^{2\alpha+2} - 1}{4}\Bigr) \equiv 0 \pmod 3,
$$

where the division by $4$ is exact.

## Sources

- Mohammed L. Nadji and Moussa Ahmia, *Congruences for l-Regular Tripartitions for l in {2,3}*, INTEGERS 24 (2024), Article A86, Theorem 5 (congruence (55)).

Stated but not proved: `MetaMathlibExt.regularTripartitionCount_three_prime_three_mod_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#regular-tripartition-count-three-prime-t).

## Toh's 3-dissection of $f_2^3 / f_1^3$

For $k \ge 1$ let
$f_k = \prod_{m \ge 1} (1 - q^{km})$ be the Euler product, an integer power series in $q$. Then

$$
f_2^3 f_3^8 f_9 f_{18} = f_1^3 \bigl(f_3^7 f_6 f_9 f_{18} + 3q f_6^4 f_9^6 +
6q^2 f_3 f_6^3 f_9^3 f_{18}^3 + 12q^3 f_3^2 f_6^2 f_{18}^6\bigr).
$$

Since each $f_k$ has constant term $1$ and so is invertible, this is the identity
$f_2^3/f_1^3 = f_6/f_3 + 3q f_6^4 f_9^5/(f_3^8 f_{18}) + 6q^2 f_6^3 f_9^2 f_{18}^2/f_3^7 +
12q^3 f_6^2 f_{18}^5/(f_3^6 f_9)$ with both sides multiplied by $f_1^3 f_3^8 f_9 f_{18}$.

## Sources

- Mohammed L. Nadji and Moussa Ahmia, *Congruences for l-Regular Tripartitions for l in {2,3}*, INTEGERS 24 (2024), Article A86, Lemma 1, eq. (3).

Stated but not proved: `MetaMathlibExt.f2_cube_div_f1_cube_three_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#f2-cube-div-f1-cube-three-dissection).

## The 3-dissection of $1/f_1^3$

For $k \ge 1$ let $f_k = \prod_{m \ge 1} (1 - q^{km})$ be
the Euler product, an integer power series in $q$. Then

$$
f_3^{12} = f_1^3 f_9^3 \bigl(f_1^6 + 9q f_1^3 f_9^3 + 27q^2 f_9^6\bigr)
$$

and

$$
f_3^{14} f_6^4 f_9^3 f_{18}^6 = f_1^3 \bigl(f_6^6 f_9^{18} + 3q f_3 f_6^5 f_9^{15} f_{18}^3 +
9q^2 f_3^2 f_6^4 f_9^{12} f_{18}^6 + 8q^3 f_3^3 f_6^3 f_9^9 f_{18}^9 +
12q^4 f_3^4 f_6^2 f_9^6 f_{18}^{12} + 16q^6 f_3^6 f_{18}^{18}\bigr).
$$

Since each $f_k$ has constant term $1$ and so is invertible, these are the identities
$1/f_1^3 = (f_9^3/f_3^{12})(f_1^6 + 9q f_1^3 f_9^3 + 27q^2 f_9^6)$ and
$1/f_1^3 = f_6^2 f_9^{15}/(f_3^{14} f_{18}^6) + 3q f_6 f_9^{12}/(f_3^{13} f_{18}^3) +
9q^2 f_9^9/f_3^{12} + 8q^3 f_9^6 f_{18}^3/(f_3^{11} f_6) +
12q^4 f_9^3 f_{18}^6/(f_3^{10} f_6^2) + 16q^6 f_{18}^{12}/(f_3^8 f_6^4 f_9^3)$, multiplied by
$f_1^3 f_3^{12}$ and by $f_1^3 f_3^{14} f_6^4 f_9^3 f_{18}^6$ respectively.

## Sources

- Mohammed L. Nadji and Moussa Ahmia, *Congruences for l-Regular Tripartitions for l in {2,3}*, INTEGERS 24 (2024), Article A86, Lemma 3, eq. (6).

Stated but not proved: `MetaMathlibExt.one_div_f1_cube_three_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#one-div-f1-cube-three-dissection).

## Cui–Gu $p$-dissection of $\psi(q)$

Let $p$ be an odd prime and $q$ a complex number with
$|q| < 1$, let $f(a, b) = \sum_{n \in \mathbb{Z}} a^{n(n+1)/2} b^{n(n-1)/2}$ be Ramanujan's theta
function, and let $\psi(q) = f(q, q^3)$. Then

$$
\psi(q) = \sum_{k=0}^{(p-3)/2} q^{k(k+1)/2}
f\bigl(q^{(p^2 + (2k+1)p)/2}, q^{(p^2 - (2k+1)p)/2}\bigr) + q^{(p^2-1)/8} \psi(q^{p^2}),
$$

and $(m^2 + m)/2 \not\equiv (p^2 - 1)/8 \pmod p$ for every integer $m$ with
$0 \le m \le (p - 3)/2$. All the divisions are exact.

## Sources

- Mohammed L. Nadji and Moussa Ahmia, *Congruences for l-Regular Tripartitions for l in {2,3}*, INTEGERS 24 (2024), Article A86, Lemma 4, eq. (7), quoting S. Cui and N. Gu, *Arithmetic Properties of ℓ-Regular Partitions*, Adv. Appl. Math. 51 (2013), 507–523, Theorem 2.1.

Stated but not proved: `MetaMathlibExt.ramanujanPsi_prime_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#ramanujan-psi-prime-dissection).

## Cui–Gu $p$-dissection of $f_1$

Let $p \ge 5$ be a prime, let $s = (p - 1)/6$ if
$p \equiv 1 \pmod 6$ and $s = (-p - 1)/6$ otherwise, and let $q$ be a complex number with
$|q| < 1$. Write $f_k = (q^k; q^k)_\infty = \prod_{m \ge 1} (1 - q^{km})$, let
$f(a, b) = \sum_{n \in \mathbb{Z}} a^{n(n+1)/2} b^{n(n-1)/2}$ be Ramanujan's theta function, and
let $K$ be the set of integers $k$ with $(1 - p)/2 \le k \le (p - 1)/2$ and $k \ne s$. Then

$$
f_1 = \sum_{k \in K} (-1)^k q^{k(3k+1)/2}
f\bigl(-q^{(3p^2 + (6k+1)p)/2}, -q^{(3p^2 - (6k+1)p)/2}\bigr) +
(-1)^s q^{(p^2-1)/24} f_{p^2}.
$$

All the divisions are exact and all the exponents of $q$ are nonnegative integers.

## Sources

- Mohammed L. Nadji and Moussa Ahmia, *Congruences for l-Regular Tripartitions for l in {2,3}*, INTEGERS 24 (2024), Article A86, Lemma 5, eq. (8), quoting S. Cui and N. Gu, *Arithmetic Properties of ℓ-Regular Partitions*, Adv. Appl. Math. 51 (2013), 507–523, Theorem 2.2. The same identity is Nayaka, Dharmendra and Mahesh Kumar, *Divisibility Properties for Overcubic Partition Triples*, INTEGERS 24 (2024), Article A80, Lemma 4, eq. (43).

Stated but not proved: `MetaMathlibExt.qPochhammer_prime_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#q-pochhammer-prime-dissection).

## The 3-dissection of the 2-regular tripartition generating function

Let $T_2(n)$ be the
number of 2-regular tripartitions of $n$ and $f_k = \prod_{m \ge 1} (1 - q^{km})$. In the ring
$\mathbb{Z}[[q]]$ of integer power series,
$f_1^6 f_3 \sum_{n \ge 0} T_2(3n) q^n = f_1^5 f_2 f_3 + 12 q f_2^2 f_6^5$,
$f_1^8 f_6 \sum_{n \ge 0} T_2(3n + 1) q^n = 3 f_2^4 f_3^5$ and
$f_1^7 \sum_{n \ge 0} T_2(3n + 2) q^n = 6 f_2^3 f_3^2 f_6^2$.

Since each $f_k$ with $k \ge 1$ is invertible in $\mathbb{Z}[[q]]$, these say
$\sum_{n \ge 0} T_2(3n) q^n = f_2 / f_1 + 12 q f_2^2 f_6^5 / (f_1^6 f_3)$,
$\sum_{n \ge 0} T_2(3n + 1) q^n = 3 f_2^4 f_3^5 / (f_1^8 f_6)$ and
$\sum_{n \ge 0} T_2(3n + 2) q^n = 6 f_2^3 f_3^2 f_6^2 / f_1^7$.

## Sources

- Mohammed L. Nadji and Moussa Ahmia, *Congruences for l-Regular Tripartitions for l in {2,3}*, INTEGERS 24 (2024), Article A86, Lemma 7, eqs. (10)–(12).

Stated but not proved: `MetaMathlibExt.regularTripartitionCount_two_three_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#regular-tripartition-count-two-three-dis).

## Mod 12 congruences for 2-regular tripartitions

Let $T_2(n)$ be the number of 2-regular
tripartitions of $n$. For all natural numbers $\alpha$ and $n$, put
$A_\alpha = \sum_{i=0}^{2\alpha+1} 3^{2i}$ and $B_\alpha = \sum_{i=0}^{2\alpha} 3^{2i}$. Then $12$
divides each of $T_2(3^{4\alpha+4} n + A_\alpha + 3^{4\alpha+3})$,
$T_2(3^{4\alpha+4} n + A_\alpha + 2 \cdot 3^{4\alpha+3})$,
$T_2(3^{4\alpha+2} n + B_\alpha + 3^{4\alpha+1})$ and
$T_2(3^{4\alpha+2} n + B_\alpha + 2 \cdot 3^{4\alpha+1})$.

## Sources

- Mohammed L. Nadji and Moussa Ahmia, *Congruences for l-Regular Tripartitions for l in {2,3}*, INTEGERS 24 (2024), Article A86, Theorem 3, eqs. (31)–(34).

Stated but not proved: `MetaMathlibExt.regularTripartitionCount_two_mod_twelve` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#regular-tripartition-count-two-mod-twelv).

## The 3-dissection of the generating function of 3-regular tripartitions

Let $T_3(n)$ be
the number of $3$-regular tripartitions of $n$, and for $k \ge 1$ let
$f_k = \prod_{m \ge 1} (1 - q^{km})$ be the Euler product. Then, as integer power series in $q$,

$$
f_1^{11} f_2^4 f_3^3 f_6^6 \sum_{n \ge 0} T_3(3n) q^n =
f_2^6 f_3^{18} + 8q f_1^3 f_2^3 f_3^9 f_6^9 + 16q^2 f_1^6 f_6^{18},
$$



$$
f_1^{10} f_2^2 f_6^3 \sum_{n \ge 0} T_3(3n + 1) q^n = 3 f_2^3 f_3^{12} + 12q f_1^3 f_3^3 f_6^9
$$

and

$$
f_1^9 \sum_{n \ge 0} T_3(3n + 2) q^n = 9 f_3^9.
$$

Since each $f_k$ has constant term $1$ and so is invertible, these are the identities
$\sum T_3(3n) q^n = f_2^2 f_3^{15}/(f_1^{11} f_6^6) + 8q f_3^6 f_6^3/(f_1^8 f_2) +
16q^2 f_6^{12}/(f_1^5 f_2^4 f_3^3)$,
$\sum T_3(3n + 1) q^n = 3 f_2 f_3^{12}/(f_1^{10} f_6^3) + 12q f_3^3 f_6^6/(f_1^7 f_2^2)$ and
$\sum T_3(3n + 2) q^n = 9 f_3^9/f_1^9$ with the denominators cleared.

## Sources

- Mohammed L. Nadji and Moussa Ahmia, *Congruences for l-Regular Tripartitions for l in {2,3}*, INTEGERS 24 (2024), Article A86, Theorem 4, eqs. (49)–(51).

Stated but not proved: `MetaMathlibExt.regularTripartitionCount_three_three_dissection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/RegularTripartitionCongruencesWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html#regular-tripartition-count-three-three-d).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tuples of ℓ-regular partitions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/tuples-of-regular-partitions)
