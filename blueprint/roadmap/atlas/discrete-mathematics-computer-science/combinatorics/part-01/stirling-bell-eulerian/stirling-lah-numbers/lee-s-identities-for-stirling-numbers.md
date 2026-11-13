---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Enumerative.StirlingIdentitiesWanted.stirlingFirst_succ_eq_sum_choose_pow, MathlibExt.Combinatorics.Enumerative.StirlingIdentitiesWanted.stirlingSecond_eq_sum_choose_pow, MathlibExt.Combinatorics.Enumerative.StirlingIdentitiesWanted.stirlingSecond_mul_sub_eq_sum_choose_alternating, MathlibExt.Combinatorics.Enumerative.StirlingIdentitiesWanted.sum_stirlingSecond_factorial_alternating, MathlibExt.Combinatorics.Enumerative.StirlingIdentitiesWanted.stirlingSecond_mul_sub_eq_sum_factorial_negChoose, MathlibExt.Combinatorics.Enumerative.StirlingIdentitiesWanted.stirlingFirst_mul_sub_eq_sum_choose_factorial, MathlibExt.Combinatorics.Enumerative.StirlingIdentitiesWanted.stirlingFirst_mul_sub_eq_sum_stirlingFirst_choose
statement: formalized
---

# Lee's identities for Stirling numbers

7 results, 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/lee-s-identities-for-stirling-numbers/index.html).

## Lee's expansion of shifted Stirling numbers of the first kind

Write $c(n, k)$ for the
unsigned Stirling number of the first kind, the number of permutations of $n$ elements with
exactly $k$ cycles. For natural numbers $m \le n$, the following identity of integers holds:

$$c(n + 1, m + 1) = \sum_{k=m}^{n} (-1)^{n-k} \binom{k}{m}\, n^{k-m}\, c(n, k).$$

## Sources

- Kwankyu Lee, "Some New Identities for Stirling Numbers", Theorem 1.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.StirlingIdentitiesWanted.stirlingFirst_succ_eq_sum_choose_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingIdentitiesWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingIdentitiesWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/lee-s-identities-for-stirling-numbers/index.html#stirling-first-succ-eq-sum-choose-pow).

## Lee's alternating expansion of Stirling numbers of the second kind

Write $S(n, k)$ for
the Stirling number of the second kind, the number of partitions of an $n$-element set into $k$
nonempty blocks. For natural numbers $m \le n$, the following identity of integers holds:

$$S(n, m) = \sum_{k=m}^{n} (-1)^{k-m} \binom{n}{k}\, m^{n-k}\, S(k, m).$$

## Sources

- Kwankyu Lee, "Some New Identities for Stirling Numbers", Theorem 2.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.StirlingIdentitiesWanted.stirlingSecond_eq_sum_choose_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingIdentitiesWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingIdentitiesWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/lee-s-identities-for-stirling-numbers/index.html#stirling-second-eq-sum-choose-pow).

## Lee's identity for Stirling numbers of the second kind from smaller rows

Write $S(n, k)$
for the Stirling number of the second kind, the number of partitions of an $n$-element set into
$k$ nonempty blocks. For natural numbers $k$ and $n$ with $k \ge 1$ and $n \ge k + 1$, the
following identity of integers holds:

$$(n - k)\, S(n, k) = \sum_{j=2}^{n-k+1} (-1)^j \binom{n}{j}\, S(n-j+1, k).$$

This is Lee's Theorem 4 with the denominator $n - k$ cleared.

## Sources

- Kwankyu Lee, "Some New Identities for Stirling Numbers", Theorem 4.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.StirlingIdentitiesWanted.stirlingSecond_mul_sub_eq_sum_choose_alternating` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingIdentitiesWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingIdentitiesWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/lee-s-identities-for-stirling-numbers/index.html#stirling-second-mul-sub-eq-sum-choose-al).

## Lee's factorial-weighted alternating row sum of Stirling numbers of the second kind

Write
$S(a, j)$ for the Stirling number of the second kind, the number of partitions of an $a$-element
set into $j$ nonempty blocks. For every natural number $a \ge 1$, the following identity of
integers holds:

$$\sum_{j=2}^{a} (-1)^j\, (j-2)!\, S(a, j) = a - 1.$$

## Sources

- Kwankyu Lee, "Some New Identities for Stirling Numbers", Lemma 6.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.StirlingIdentitiesWanted.sum_stirlingSecond_factorial_alternating` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingIdentitiesWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingIdentitiesWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/lee-s-identities-for-stirling-numbers/index.html#sum-stirling-second-factorial-alternatin).

## Lee's identity for Stirling numbers of the second kind from higher columns

Write
$S(n, k)$ for the Stirling number of the second kind, the number of partitions of an $n$-element
set into $k$ nonempty blocks. For natural numbers $k$ and $n$ with $k \ge 1$ and $n \ge k + 1$,
the following identity of integers holds:

$$(n - k)\, S(n, k) = \sum_{j=2}^{n-k+1} (j-2)!\, (-1)^j \binom{k+j-1}{j}\, S(n, k+j-1).$$

This is Lee's Theorem 8 with the denominator $n - k$ cleared and the generalized binomial
coefficient written as $\binom{-k}{j} = (-1)^j \binom{k+j-1}{j}$.

## Sources

- Kwankyu Lee, "Some New Identities for Stirling Numbers", Theorem 8.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.StirlingIdentitiesWanted.stirlingSecond_mul_sub_eq_sum_factorial_negChoose` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingIdentitiesWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingIdentitiesWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/lee-s-identities-for-stirling-numbers/index.html#stirling-second-mul-sub-eq-sum-factorial).

## Lee's identity for Stirling numbers of the first kind from smaller rows

Write $c(n, k)$
for the unsigned Stirling number of the first kind, the number of permutations of $n$ elements
with exactly $k$ cycles. For natural numbers $k$ and $n$ with $k \ge 1$ and $n \ge k + 1$, the
following identity of integers holds:

$$(n - k)\, c(n, k) = \sum_{j=2}^{n-k+1} \binom{n}{j}\, (j-2)!\, c(n-j+1, k).$$

This is Lee's Theorem 11 with the denominator $n - k$ cleared.

## Sources

- Kwankyu Lee, "Some New Identities for Stirling Numbers", Theorem 11.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.StirlingIdentitiesWanted.stirlingFirst_mul_sub_eq_sum_choose_factorial` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingIdentitiesWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingIdentitiesWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/lee-s-identities-for-stirling-numbers/index.html#stirling-first-mul-sub-eq-sum-choose-fac).

## Lee's identity for Stirling numbers of the first kind from higher columns

Write $c(n, k)$
for the unsigned Stirling number of the first kind, the number of permutations of $n$ elements
with exactly $k$ cycles. For natural numbers $k$ and $n$ with $k \ge 1$ and $n \ge k + 1$, the
following identity of integers holds:

$$(n - k)\, c(n, k) = \sum_{j=2}^{n-k+1} \binom{k+j-1}{j}\, c(n, k+j-1).$$

This is Lee's Theorem 14 with the denominator $n - k$ cleared.

## Sources

- Kwankyu Lee, "Some New Identities for Stirling Numbers", Theorem 14.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.StirlingIdentitiesWanted.stirlingFirst_mul_sub_eq_sum_stirlingFirst_choose` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/StirlingIdentitiesWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/StirlingIdentitiesWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/lee-s-identities-for-stirling-numbers/index.html#stirling-first-mul-sub-eq-sum-stirling-f).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lee's identities for Stirling numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/lee-s-identities-for-stirling-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/lee-s-identities-for-stirling-numbers)
