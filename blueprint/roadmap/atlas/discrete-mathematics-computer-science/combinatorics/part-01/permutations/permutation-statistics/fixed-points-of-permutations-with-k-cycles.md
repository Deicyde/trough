---
declaration: section
origin: cited
lean: MetaMathlibExt.kPermFixedPointCount, MetaMathlibExt.kPermFixedPointCount_eq_zero_of_lt, MetaMathlibExt.kPermFixedPointCount_zero_zero_zero, MetaMathlibExt.kPermFixedPointCount_eq_choose_mul_derangement, MetaMathlibExt.mul_kPermFixedPointCount, MetaMathlibExt.sum_kPermFixedPointCount, MetaMathlibExt.sum_mul_kPermFixedPointCount, MetaMathlibExt.kPermFixedPoint_variance
statement: formalized
---

# Fixed points of permutations with k cycles

15 results, 3 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/fixed-points-of-permutations-with-k-cycles/index.html).

## Permutations counted by cycles and fixed points

For natural numbers $n$, $k$ and $j$,
$a(n, k, j)$ is the number of permutations of $\{0, 1, \dots, n - 1\}$ with exactly $k$ cycles
(fixed points counted as cycles of length one) and exactly $j$ fixed points.

## Sources

- Moussa Benoumhani, *The Distribution of the Number of Fixed Points in k-Permutations*, INTEGERS 24 (2024), Article A54, Proposition 3 (definition of `a(n, k, j)`).

Formalized by `MetaMathlibExt.kPermFixedPointCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/fixed-points-of-permutations-with-k-cycles/index.html#k-perm-fixed-point-count).

## A permutation has at most as many fixed points as cycles

Write $a(n, k, j)$ for the number
of permutations of an $n$-element set with exactly $k$ cycles (fixed points counted as cycles of
length one) and exactly $j$ fixed points. If $k < j$, then $a(n, k, j) = 0$.

## Sources

- Moussa Benoumhani, *The Distribution of the Number of Fixed Points in k-Permutations*, INTEGERS 24 (2024), Article A54, Proposition 3 (range `0 ≤ j ≤ k` of `a(n, k, j)`).

Formalized by `MetaMathlibExt.kPermFixedPointCount_eq_zero_of_lt`, a theorem declared in [WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/fixed-points-of-permutations-with-k-cycles/index.html#k-perm-fixed-point-count-eq-zero-of-lt).

## Counting the empty permutation

Write $a(n, k, j)$ for the number of permutations of an
$n$-element set with exactly $k$ cycles (fixed points counted as cycles of length one) and exactly
$j$ fixed points. Then $a(0, 0, 0) = 1$: the empty permutation is the only permutation of the
empty set, and it has no cycles and no fixed points.

## Sources

- Moussa Benoumhani, *The Distribution of the Number of Fixed Points in k-Permutations*, INTEGERS 24 (2024), Article A54, Proposition 3 (definition of `a(n, k, j)`, value at `n = k = j = 0`).

Formalized by `MetaMathlibExt.kPermFixedPointCount_zero_zero_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/fixed-points-of-permutations-with-k-cycles/index.html#k-perm-fixed-point-count-zero-zero-zero).

## Fixed points split off a derangement

Write $a(n, k, j)$ for the number of permutations of
an $n$-element set with exactly $k$ cycles (fixed points counted as cycles of length one) and
exactly $j$ fixed points, and $d(m, i) = a(m, i, 0)$ for the number of derangements of an
$m$-element set with $i$ cycles. For all natural numbers $n$, $k$ and $j$ with $j \le k$,
$a(n, k, j) = \binom{n}{j} \, d(n - j, k - j)$, where $n - j$ is read as $0$ when $j > n$.

The paper assumes $n \ge k \ge 1$; the identity holds for all $n$ and all $k \ge j$.

## Sources

- Moussa Benoumhani, *The Distribution of the Number of Fixed Points in k-Permutations*, INTEGERS 24 (2024), Article A54, Proposition 3 (i).

Stated but not proved: `MetaMathlibExt.kPermFixedPointCount_eq_choose_mul_derangement` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/fixed-points-of-permutations-with-k-cycles/index.html#k-perm-fixed-point-count-eq-choose-mul-d).

## Recurrence for permutations counted by cycles and fixed points

Write $a(n, k, j)$ for the
number of permutations of an $n$-element set with exactly $k$ cycles (fixed points counted as
cycles of length one) and exactly $j$ fixed points. For all natural numbers $n$, $k$ and $j$
with $1 \le j \le k$, $j \, a(n, k, j) = n \, a(n - 1, k - 1, j - 1)$, where $n - 1$ is read as
$0$ when $n = 0$.

The paper assumes $n \ge k \ge 1$; the identity holds for all $n$.

## Sources

- Moussa Benoumhani, *The Distribution of the Number of Fixed Points in k-Permutations*, INTEGERS 24 (2024), Article A54, Proposition 3 (iii).

Stated but not proved: `MetaMathlibExt.mul_kPermFixedPointCount` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/fixed-points-of-permutations-with-k-cycles/index.html#mul-k-perm-fixed-point-count).

## Stirling numbers from fixed-point counts

For natural numbers $n$, $k$ and $j$, let
$a(n, k, j)$ be the number of permutations of an $n$-element set with exactly $k$ cycles (fixed
points counted as cycles of length one) and exactly $j$ fixed points. Then for all natural
numbers $n$ and $k$,

$$\sum_{j=0}^{k} a(n, k, j) = c(n, k),$$

where $c(n, k)$ is the unsigned Stirling number of the first kind.

The paper assumes $n \ge k \ge 1$; the identity is stated for all $n$ and $k$.

## Sources

- Moussa Benoumhani, *The Distribution of the Number of Fixed Points in k-Permutations*, INTEGERS 24 (2024), Article A54, Proposition 3 (iv).

Stated but not proved: `MetaMathlibExt.sum_kPermFixedPointCount` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/fixed-points-of-permutations-with-k-cycles/index.html#sum-k-perm-fixed-point-count).

## Total number of fixed points of permutations with a given number of cycles

For natural
numbers $n$, $k$ and $j$, let $a(n, k, j)$ be the number of permutations of an $n$-element set
with exactly $k$ cycles (fixed points counted as cycles of length one) and exactly $j$ fixed
points, and let $c(n, k)$ be the unsigned Stirling number of the first kind. Then for every
natural number $n$ and every $k \ge 1$,

$$\sum_{j=0}^{k} j \, a(n, k, j) = n \, c(n - 1, k - 1),$$

where the right-hand side is read as $0$ when $n = 0$.

Dividing by $c(n, k)$, the number of permutations of an $n$-element set with $k$ cycles, gives the
mean $\mu_{n,k} = n \, c(n - 1, k - 1) / c(n, k)$ of the number of fixed points of a uniformly
random such permutation when $n \ge k$.

## Sources

- Moussa Benoumhani, *The Distribution of the Number of Fixed Points in k-Permutations*, INTEGERS 24 (2024), Article A54, Proposition 4.

Stated but not proved: `MetaMathlibExt.sum_mul_kPermFixedPointCount` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/fixed-points-of-permutations-with-k-cycles/index.html#sum-mul-k-perm-fixed-point-count).

## Variance of the number of fixed points of a permutation with a given number of cycles

Write $a(n, k, j)$ for the number of permutations of an $n$-element set with exactly $k$ cycles
(fixed points counted as cycles of length one) and exactly $j$ fixed points, $c(n, k)$ for the
unsigned Stirling number of the first kind (the number of permutations of an $n$-element set
with $k$ cycles), and $\mu_{n,k} = n \, c(n - 1, k - 1) / c(n, k)$. If $2 \le k \le n$, then
$\frac{1}{c(n, k)} \sum_{j=0}^{k} j^2 \, a(n, k, j) - \mu_{n,k}^2 =
\mu_{n,k} (1 + \mu_{n-1,k-1} - \mu_{n,k})$.

Here $\mu_{n,k}$ is the mean number of fixed points of a uniformly random permutation of an
$n$-element set with $k$ cycles, so the left side is the variance of that number.

## Sources

- Moussa Benoumhani, *The Distribution of the Number of Fixed Points in k-Permutations*, INTEGERS 24 (2024), Article A54, Proposition 4.

Stated but not proved: `MetaMathlibExt.kPermFixedPoint_variance` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/fixed-points-of-permutations-with-k-cycles/index.html#k-perm-fixed-point-variance).

## Newton's inequalities

Let $p(x) = \sum_{j=0}^{n} a_j x^j$ be a real polynomial of degree
$n \ge 2$ that splits over $\mathbb{R}$, that is, all $n$ of its zeros, counted with
multiplicity, are real. Then for every $j$ with $1 \le j \le n - 1$,

$$a_j^2 \ge \frac{j + 1}{j} \cdot \frac{n - j + 1}{n - j} \, a_{j-1} a_{j+1}.$$

## Sources

- Moussa Benoumhani, *The Distribution of the Number of Fixed Points in k-Permutations*, INTEGERS 24 (2024), Article A54, Theorem 1.

Stated but not proved: `MetaMathlibExt.newton_inequality_of_real_roots` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/fixed-points-of-permutations-with-k-cycles/index.html#newton-inequality-of-real-roots).

## Schur's composition theorem for real-rooted polynomials

Let $f = \sum_k a_k x^k$ and
$g = \sum_k c_k x^k$ be real polynomials that split over $\mathbb{R}$, and suppose that the zeros
of $g$ are either all $\le 0$ or all $\ge 0$. Let $d = \min(\deg f, \deg g)$, where the zero
polynomial is given degree $0$. Then the polynomial $\sum_{k=0}^{d} k!\, a_k c_k x^k$ also splits
over $\mathbb{R}$.

The paper asks that the zeros of one of the two polynomials lie on the same side of the origin;
by symmetry this is taken to be $g$, and zeros at $0$ are allowed.

## Sources

- Moussa Benoumhani, *The Distribution of the Number of Fixed Points in k-Permutations*, INTEGERS 24 (2024), Article A54, Theorem 2 (Schur).

Stated but not proved: `MetaMathlibExt.schur_factorial_hadamard_real_roots` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/fixed-points-of-permutations-with-k-cycles/index.html#schur-factorial-hadamard-real-roots).

## Real-rootedness of the derangement cycle polynomial

Write $a(m, k, j)$ for the number of
permutations of an $m$-element set with exactly $k$ cycles (fixed points counted as cycles of
length one) and exactly $j$ fixed points, so that $d(m, k) = a(m, k, 0)$ is the number of
derangements of an $m$-element set with $k$ cycles. For every $n \ge 2$, the real polynomial
$D_n(x) = \sum_{k=1}^{n} d(n + k, k) x^{k-1}$ has only real zeros.

The terms with $k > n$ vanish, so the upper summation limit $n$ loses nothing.

## Sources

- Moussa Benoumhani, *The Distribution of the Number of Fixed Points in k-Permutations*, INTEGERS 24 (2024), Article A54, Theorem 3.

Stated but not proved: `MetaMathlibExt.derangementCyclePolynomial_real_roots` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/fixed-points-of-permutations-with-k-cycles/index.html#derangement-cycle-polynomial-real-roots).

## Positive sequences satisfying Newton's inequalities are unimodal

Let $n$ be a natural
number and let $(a_j)_{j \ge 0}$ be a sequence of real numbers with $a_j > 0$ for every $j \le n$,
such that

$$a_j^2 \ge \frac{j + 1}{j} \cdot \frac{n - j + 1}{n - j} \, a_{j-1} a_{j+1}$$

for every $j$ with $1 \le j \le n - 1$. Then there is an $m \le n$ such that $(a_j)$ is strictly
increasing on $\{0, \dots, m\}$, and either $(a_j)$ is strictly decreasing on $\{m, \dots, n\}$,
or $m < n$, $a_m = a_{m+1}$ and $(a_j)$ is strictly decreasing on $\{m + 1, \dots, n\}$.

The paper's "SLC" conclusion is not stated (the abbreviation is not defined in the extracted
statement).

## Sources

- Moussa Benoumhani, *The Distribution of the Number of Fixed Points in k-Permutations*, INTEGERS 24 (2024), Article A54, Corollary 1.

Stated but not proved: `MetaMathlibExt.unimodal_of_newton_inequalities` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/fixed-points-of-permutations-with-k-cycles/index.html#unimodal-of-newton-inequalities).

## Unimodality of fixed-point counts for permutations with a given number of cycles

Write
$a(n, k, j)$ for the number of permutations of an $n$-element set with exactly $k$ cycles (fixed
points counted as cycles of length one) and exactly $j$ fixed points. If $k \le n$, then there is
an $m \le k$ such that $j \mapsto a(n, k, j)$ is weakly increasing on $\{0, \dots, m\}$ and weakly
decreasing on $\{m, \dots, k\}$, and every $i \le k$ with $a(n, k, i) = a(n, k, m)$ is $m$ or
$m + 1$.

The paper's "SLC" conclusion is not stated (the abbreviation is not defined in the extracted
statement).

## Sources

- Moussa Benoumhani, *The Distribution of the Number of Fixed Points in k-Permutations*, INTEGERS 24 (2024), Article A54, Corollary 2.

Stated but not proved: `MetaMathlibExt.kPermFixedPointCount_unimodal` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/fixed-points-of-permutations-with-k-cycles/index.html#k-perm-fixed-point-count-unimodal).

## Central limit theorem for polynomials with nonpositive real zeros

Let $(Q_n)_{n \ge 0}$
be real polynomials such that every $Q_n$ has only real zeros and all of them are $\le 0$. Put
$\mu_n = Q_n'(1) / Q_n(1)$ and $\sigma_n^2 = Q_n'(1) / Q_n(1) + Q_n''(1) / Q_n(1) - \mu_n^2$, and
let $\sigma_n = \sqrt{\sigma_n^2}$. If $\sigma_n^2 \to \infty$ as $n \to \infty$, then for every
real $x$, the sum of the coefficients of $X^j$ in $Q_n$ over the indices $0 \le j \le \deg Q_n$
with $(j - \mu_n) / \sigma_n \le x$, divided by $Q_n(1)$, tends to $\Phi(x)$ as $n \to \infty$,
where $\Phi$ is the distribution function of the standard normal distribution.

The source asks for negative zeros; zeros at $0$ are also allowed here, since $Q_n = X^m R_n$ only
shifts the coefficient distribution by $m$ and leaves $\sigma_n^2$ unchanged. The local limit
theorem that accompanies this result in the source is not stated.

## Sources

- Moussa Benoumhani, *The Distribution of the Number of Fixed Points in k-Permutations*, INTEGERS 24 (2024), Article A54, Theorem 5.

Stated but not proved: `MetaMathlibExt.coeff_tendsto_gaussian_cdf_of_neg_real_roots` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/fixed-points-of-permutations-with-k-cycles/index.html#coeff-tendsto-gaussian-cdf-of-neg-real-r).

## Real zeros of the fixed-point polynomial

Write $a(n, k, j)$ for the number of permutations
of an $n$-element set with exactly $k$ cycles (fixed points counted as cycles of length one) and
exactly $j$ fixed points. If $1 \le k \le n$, then the real polynomial
$P(x) = \sum_{j=0}^{k} a(n, k, j) x^j$ has only real zeros.

## Sources

- Moussa Benoumhani, *The Distribution of the Number of Fixed Points in k-Permutations*, INTEGERS 24 (2024), Article A54, Theorem 4.

Stated but not proved: `MetaMathlibExt.kPermFixedPointPolynomial_real_roots` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FixedPointsKPermutationsWanted.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/fixed-points-of-permutations-with-k-cycles/index.html#k-perm-fixed-point-polynomial-real-roots).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fixed points of permutations with k cycles](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/fixed-points-of-permutations-with-k-cycles/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/permutations/permutation-statistics/fixed-points-of-permutations-with-k-cycles)
