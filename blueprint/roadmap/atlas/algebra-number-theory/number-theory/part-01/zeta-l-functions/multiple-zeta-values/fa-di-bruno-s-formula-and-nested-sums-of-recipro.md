---
declaration: section
origin: cited
lean: MetaMathlibExt.taylorCoeff_comp_eq_sum_partitions, MetaMathlibExt.tsum_weaklyDecreasing_prod_inv_odd_sq_eq, MetaMathlibExt.starValue_replicate_two_eq, MetaMathlibExt.tsum_strictDecreasing_prod_inv_odd_sq_eq
statement: formalized
---

# Faà di Bruno's formula and nested sums of reciprocal squares

4 results, 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/fa-di-bruno-s-formula-and-nested-sums-of-recipro/index.html).

## Faà di Bruno's formula for Taylor coefficients

Let $f, g : \mathbb{R} \to \mathbb{R}$,
let $a \in \mathbb{R}$ and let $n$ be a natural number. Suppose that $g$ is $n$ times continuously
differentiable on a neighbourhood of $a$ and that $f$ is $n$ times continuously differentiable on a
neighbourhood of $g(a)$. For a partition $\pi$ of $n$, let $m_i(\pi)$ be the number of parts of
$\pi$ equal to $i$, and let $\ell(\pi) = m_1(\pi) + \cdots + m_n(\pi)$ be its number of parts. Then

$$\frac{(f \circ g)^{(n)}(a)}{n!} = \sum_{\pi} \frac{\ell(\pi)!}{\prod_{i=1}^{n} m_i(\pi)!} \cdot
\frac{f^{(\ell(\pi))}(g(a))}{\ell(\pi)!} \cdot
\prod_{i=1}^{n} \Bigl(\frac{g^{(i)}(a)}{i!}\Bigr)^{m_i(\pi)},$$

where the sum runs over all partitions $\pi$ of $n$.

## Sources

- Serge Iovleff, *About Some Nested Sums of Reciprocal Squared Numbers*, INTEGERS 26 (2026), Article A114, Corollary 1 (quoted as Corollary 4 from the paper's reference [8]).

Stated but not proved: `MetaMathlibExt.taylorCoeff_comp_eq_sum_partitions` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/TaylorCoefficientCompositionWanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Calculus/TaylorCoefficientCompositionWanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/fa-di-bruno-s-formula-and-nested-sums-of-recipro/index.html#taylor-coeff-comp-eq-sum-partitions).

## Nested sums of reciprocal odd squares

For every natural number $k$,

$$\sum_{i_1 \ge i_2 \ge \cdots \ge i_k \ge 1} \prod_{j=1}^{k} \frac{1}{(2 i_j - 1)^2} =
\frac{(\pi/2)^{2k} E^*_{2k}}{(2k)!},$$

where the sum runs over all weakly decreasing $k$-tuples $(i_1, \ldots, i_k)$ of positive integers
and $E^*_{2k} = \sec^{(2k)}(0)$ is the $2k$-th derivative at $0$ of $\sec x = 1/\cos x$ (the Euler
zig number, OEIS A000364). For $k = 0$ the sum has the single empty term and both sides equal $1$.

The source also claims that the sum equals $(\pi/4)\,\beta(2k+1)$, where $\beta$ is Dirichlet's beta
function; this is false as printed and is not stated here: at $k = 0$ the sum is $1$ but
$(\pi/4)\,\beta(1) = \pi^2/16$, and at $k = 1$ it is $\pi^2/8$ but $(\pi/4)\,\beta(3) = \pi^4/128$
(the correct factor is $4/\pi$).

## Sources

- Serge Iovleff, *About Some Nested Sums of Reciprocal Squared Numbers*, INTEGERS 26 (2026), Article A114, Theorem 1.

Stated but not proved: `MetaMathlibExt.tsum_weaklyDecreasing_prod_inv_odd_sq_eq` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/TaylorCoefficientCompositionWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Calculus/TaylorCoefficientCompositionWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/fa-di-bruno-s-formula-and-nested-sums-of-recipro/index.html#tsum-weakly-decreasing-prod-inv-odd-sq-e).

## Nested sums of reciprocal squares

For every natural number $k$, the multiple zeta-star
value

$$\zeta^\star(\{2\}^k) =
\sum_{n_1 \ge n_2 \ge \cdots \ge n_k \ge 1} \frac{1}{n_1^2 n_2^2 \cdots n_k^2},$$

which is $1$ for $k = 0$, satisfies

$$\zeta^\star(\{2\}^k) = \frac{2\pi^{2k} |(2^{2k-1} - 1) B_{2k}|}{(2k)!} =
2\,(1 - 2^{1-2k})\,\zeta(2k),$$

where $B_{2k}$ is the $2k$-th Bernoulli number and $\zeta$ is the Riemann zeta function. The
right-hand side is $2\eta(2k)$ for Dirichlet's eta function $\eta(s) = (1 - 2^{1-s})\,\zeta(s)$;
at $k = 0$ all three expressions equal $1$, since $\zeta(0) = -1/2$.

## Sources

- Serge Iovleff, *About Some Nested Sums of Reciprocal Squared Numbers*, INTEGERS 26 (2026), Article A114, Theorem 2.

Stated but not proved: `MetaMathlibExt.starValue_replicate_two_eq` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/TaylorCoefficientCompositionWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Calculus/TaylorCoefficientCompositionWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/fa-di-bruno-s-formula-and-nested-sums-of-recipro/index.html#star-value-replicate-two-eq).

## Strictly nested sums of reciprocal odd squares

For every natural number $k$,

$$\sum_{i_1 > i_2 > \cdots > i_k \ge 1} \prod_{j=1}^{k} \frac{1}{(2 i_j - 1)^2} =
\frac{(\pi/2)^{2k}}{(2k)!},$$

where the sum runs over all strictly decreasing $k$-tuples $(i_1, \ldots, i_k)$ of positive
integers. For $k = 0$ the sum has the single empty term and both sides equal $1$.

The source states the identity for $k > 0$; the case $k = 0$ is included here.

## Sources

- Serge Iovleff, *About Some Nested Sums of Reciprocal Squared Numbers*, INTEGERS 26 (2026), Article A114, Corollary 2.

Stated but not proved: `MetaMathlibExt.tsum_strictDecreasing_prod_inv_odd_sq_eq` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/TaylorCoefficientCompositionWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Calculus/TaylorCoefficientCompositionWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/fa-di-bruno-s-formula-and-nested-sums-of-recipro/index.html#tsum-strict-decreasing-prod-inv-odd-sq-e).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Faà di Bruno's formula and nested sums of reciprocal squares](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/fa-di-bruno-s-formula-and-nested-sums-of-recipro/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/fa-di-bruno-s-formula-and-nested-sums-of-recipro)
