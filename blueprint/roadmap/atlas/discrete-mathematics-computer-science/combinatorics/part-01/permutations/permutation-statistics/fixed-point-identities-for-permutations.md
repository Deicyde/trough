---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Enumerative.PermutationFixedPointIdentitiesWanted.sum_perm_sign_falling_fixedPoints_mul_pow, MathlibExt.Combinatorics.Enumerative.PermutationFixedPointIdentitiesWanted.sum_perm_sign_factorial_fixedPoints_div
statement: formalized
---

# Fixed-point identities for permutations

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/fixed-point-identities-for-permutations/index.html).

## Pain's signed falling-factorial identity for fixed points

Let $n$ and $k$ be natural
numbers with $n \ge 2$, $k \ge 1$ and $k + 1 \le n$, and let $x$ be a real number. For a
permutation $\sigma$ of $\lbrace 0, 1, \dots, n-1 \rbrace$, write $\operatorname{sgn}(\sigma)$ for
its sign and $\operatorname{fix}(\sigma)$ for its number of fixed points, and for a natural number
$m$ write $(m)_k = m(m-1)\cdots(m-k+1)$ for the falling factorial. Then, summing over all
permutations $\sigma$ of this set,

$$\sum_{\sigma} \operatorname{sgn}(\sigma) (\operatorname{fix}(\sigma))_k
x^{\operatorname{fix}(\sigma) - k} = \frac{n!}{(n-k)!} (x-1)^{n-k-1} (x + n - k - 1),$$

where a term with $\operatorname{fix}(\sigma) < k$ is $0$ because then
$(\operatorname{fix}(\sigma))_k = 0$.

The left side is the $k$-th derivative in $x$ of
$\sum_{\sigma} \operatorname{sgn}(\sigma) x^{\operatorname{fix}(\sigma)}$.

## Sources

- Jean-Christophe Pain, "Identities for Permutations with Fixed Points", Theorem 2.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.PermutationFixedPointIdentitiesWanted.sum_perm_sign_falling_fixedPoints_mul_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PermutationFixedPointIdentitiesWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PermutationFixedPointIdentitiesWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/fixed-point-identities-for-permutations/index.html#sum-perm-sign-falling-fixed-points-mul-p).

## Pain's signed factorial-ratio identity for fixed points

Let $n$ and $k$ be natural
numbers with $n \ge 2$ and $k \ge 1$. For a permutation $\sigma$ of
$\lbrace 0, 1, \dots, n-1 \rbrace$, write $\operatorname{sgn}(\sigma)$ for its sign and
$\operatorname{fix}(\sigma)$ for its number of fixed points. Then, summing over all permutations
$\sigma$ of this set,

$$\sum_{\sigma} \operatorname{sgn}(\sigma)
\frac{\operatorname{fix}(\sigma)!}{(\operatorname{fix}(\sigma) + k)!} =
\frac{(-1)^{n+1} \left(n^2 + (k-1)n - (k-1)\right)}{(k-1)! (n+k-1)(n+k)}.$$

## Sources

- Jean-Christophe Pain, "Identities for Permutations with Fixed Points", Theorem 3.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.PermutationFixedPointIdentitiesWanted.sum_perm_sign_factorial_fixedPoints_div` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PermutationFixedPointIdentitiesWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PermutationFixedPointIdentitiesWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/fixed-point-identities-for-permutations/index.html#sum-perm-sign-factorial-fixed-points-div).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fixed-point identities for permutations](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/fixed-point-identities-for-permutations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/permutations/permutation-statistics/fixed-point-identities-for-permutations)
