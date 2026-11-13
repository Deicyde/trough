---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Enumerative.IncompleteBinomialHarmonicSumsWanted.invPowTwoSum, MathlibExt.Combinatorics.Enumerative.IncompleteBinomialHarmonicSumsWanted.centralBinomWeightedSum, MathlibExt.Combinatorics.Enumerative.IncompleteBinomialHarmonicSumsWanted.sum_range_choose_mul_eq_sum_range_choose_add, MathlibExt.Combinatorics.Enumerative.IncompleteBinomialHarmonicSumsWanted.sum_range_choose_two_mul_sub_one_mul_eq, MathlibExt.Combinatorics.Enumerative.IncompleteBinomialHarmonicSumsWanted.sum_range_choose_two_mul_mul_eq, MathlibExt.Combinatorics.Enumerative.IncompleteBinomialHarmonicSumsWanted.sum_range_choose_two_mul_sub_one_mul_harmonic, MathlibExt.Combinatorics.Enumerative.IncompleteBinomialHarmonicSumsWanted.sum_range_choose_two_mul_mul_harmonic
statement: formalized
---

# Kollár's incomplete binomial sums

7 results, 2 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/koll-r-s-incomplete-binomial-sums/index.html).

## Kollár's auxiliary sum $C_n$

For a natural number $n$, $C_n$ is the rational number
$C_n = \sum_{k=1}^{n} \frac{1}{k \, 2^k}$.

Formalized by `MathlibExt.Combinatorics.Enumerative.IncompleteBinomialHarmonicSumsWanted.invPowTwoSum`, a definition declared in [WantedExt/Combinatorics/Enumerative/IncompleteBinomialHarmonicSumsWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/IncompleteBinomialHarmonicSumsWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/koll-r-s-incomplete-binomial-sums/index.html#inv-pow-two-sum).

## Kollár's auxiliary sum $D_n$

For a natural number $n$, $D_n$ is the rational number
$D_n = \sum_{k=1}^{n} \frac{\binom{2k}{k}}{2k \cdot 2^{2k}}$.

Formalized by `MathlibExt.Combinatorics.Enumerative.IncompleteBinomialHarmonicSumsWanted.centralBinomWeightedSum`, a definition declared in [WantedExt/Combinatorics/Enumerative/IncompleteBinomialHarmonicSumsWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/IncompleteBinomialHarmonicSumsWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/koll-r-s-incomplete-binomial-sums/index.html#central-binom-weighted-sum).

## Kollár's recursion for incomplete binomial sums

Let $(a_k)_{k \ge 0}$ be a sequence of
real numbers and let $m$ and $N$ be positive integers with $m \le N$. Then

$$\sum_{k=0}^{m} \binom{N}{k} a_k =
\sum_{k=0}^{m-1} \binom{N-1}{k} (a_k + a_{k+1}) + \binom{N-1}{m} a_m.$$

## Sources

- Richard Kollár, "Incomplete Finite Binomial Sums of Harmonic Numbers", Lemma 1.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.IncompleteBinomialHarmonicSumsWanted.sum_range_choose_mul_eq_sum_range_choose_add` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IncompleteBinomialHarmonicSumsWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/IncompleteBinomialHarmonicSumsWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/koll-r-s-incomplete-binomial-sums/index.html#sum-range-choose-mul-eq-sum-range-choose).

## Kollár's recursion for incomplete binomial sums with top index $2n-1$

Let
$(a_k)_{k \ge 0}$ be a sequence of real numbers, let $n$ be a positive integer and let $m$ be a
natural number with $m \le n$. Then

$$\sum_{k=0}^{m} \binom{2n-1}{k} a_k =
\sum_{k=0}^{m} \binom{2n-2}{k} (a_k + a_{k+1}) - \binom{2n-2}{m} a_{m+1}.$$

## Sources

- Richard Kollár, "Incomplete Finite Binomial Sums of Harmonic Numbers", Corollary 2, equation `Lemma7`.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.IncompleteBinomialHarmonicSumsWanted.sum_range_choose_two_mul_sub_one_mul_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IncompleteBinomialHarmonicSumsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/IncompleteBinomialHarmonicSumsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/koll-r-s-incomplete-binomial-sums/index.html#sum-range-choose-two-mul-sub-one-mul-eq).

## Kollár's recursion for incomplete binomial sums with top index $2n$

Let
$(a_k)_{k \ge 0}$ be a sequence of real numbers and let $m$ and $n$ be positive integers with
$m \le n$. Then

$$\sum_{k=0}^{m} \binom{2n}{k} a_k =
\sum_{k=0}^{m-1} \binom{2n-1}{k} (a_k + a_{k+1}) + \binom{2n-1}{m} a_m.$$

## Sources

- Richard Kollár, "Incomplete Finite Binomial Sums of Harmonic Numbers", Corollary 2, equation `Lemma8`.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.IncompleteBinomialHarmonicSumsWanted.sum_range_choose_two_mul_mul_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IncompleteBinomialHarmonicSumsWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/IncompleteBinomialHarmonicSumsWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/koll-r-s-incomplete-binomial-sums/index.html#sum-range-choose-two-mul-mul-eq).

## Half-range binomial sum of harmonic numbers with top index $2n-1$

Let $H_i$ denote
the $i$-th harmonic number (with $H_0 = 0$), and let Kollár's auxiliary sums be
$C_n = \sum_{k=1}^{n} \frac{1}{k \, 2^k}$ and
$D_n = \sum_{k=1}^{n} \frac{\binom{2k}{k}}{2k \cdot 2^{2k}}$.
For every positive integer $n$,

$$\sum_{i=0}^{n-1} \binom{2n-1}{i} H_i =
2^{2n-2} \left( H_{2n-1} - 2 C_{2n-1} + D_{n-1} \right).$$

## Sources

- Richard Kollár, "Incomplete Finite Binomial Sums of Harmonic Numbers", Theorem 3, equation `oddH`.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.IncompleteBinomialHarmonicSumsWanted.sum_range_choose_two_mul_sub_one_mul_harmonic` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IncompleteBinomialHarmonicSumsWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/IncompleteBinomialHarmonicSumsWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/koll-r-s-incomplete-binomial-sums/index.html#sum-range-choose-two-mul-sub-one-mul-har).

## Half-range binomial sum of harmonic numbers with top index $2n$

Let $H_i$ denote
the $i$-th harmonic number (with $H_0 = 0$), and let Kollár's auxiliary sums be
$C_n = \sum_{k=1}^{n} \frac{1}{k \, 2^k}$ and
$D_n = \sum_{k=1}^{n} \frac{\binom{2k}{k}}{2k \cdot 2^{2k}}$.
For every positive integer $n$,

$$\sum_{i=0}^{n} \binom{2n}{i} H_i =
2^{2n-1} \left( H_{2n} - 2 C_{2n} + D_n \right) + \frac{1}{2} \binom{2n}{n} H_n.$$

## Sources

- Richard Kollár, "Incomplete Finite Binomial Sums of Harmonic Numbers", Theorem 3, equation `evenH`.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.IncompleteBinomialHarmonicSumsWanted.sum_range_choose_two_mul_mul_harmonic` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IncompleteBinomialHarmonicSumsWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/IncompleteBinomialHarmonicSumsWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/koll-r-s-incomplete-binomial-sums/index.html#sum-range-choose-two-mul-mul-harmonic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kollár's incomplete binomial sums](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/koll-r-s-incomplete-binomial-sums/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/koll-r-s-incomplete-binomial-sums)
