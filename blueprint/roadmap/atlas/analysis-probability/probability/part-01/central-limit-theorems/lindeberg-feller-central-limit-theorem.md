---
declaration: section
origin: cited
lean: ProbabilityTheory.LindebergConditionTriangular, ProbabilityTheory.norm_exp_ofReal_mul_I_sub_one_sub_le, ProbabilityTheory.prod_one_add_sub_exp_sum_le, ProbabilityTheory.lindeberg_charFun_product_tendsto, ProbabilityTheory.lindeberg_feller_clt_triangular
statement: formalized
proof: formalized
---

# Lindeberg–Feller central limit theorem

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/lindeberg-feller-central-limit-theorem/index.html).

## Lindeberg condition for a triangular array

A triangular array of real random variables
$X_{n,k}$ ($n \in \mathbb{N}$, $0 \le k < n$) on a measure space $(\Omega, \mu)$ satisfies the
Lindeberg condition if for every $\varepsilon > 0$ the truncated second moments

$$\sum_{k < n} \int_\Omega X_{n,k}^2 \, \mathbf{1}\{|X_{n,k}| > \varepsilon\} \, d\mu$$

tend to $0$ as $n \to \infty$. This is the key hypothesis of the Lindeberg–Feller central limit
theorem.

Formalized by `ProbabilityTheory.LindebergConditionTriangular`, a definition declared in [MathlibExt/Probability/LindebergFeller.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LindebergFeller.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/lindeberg-feller-central-limit-theorem/index.html#lindeberg-condition-triangular).

## Second-order Taylor bound for the imaginary exponential

For every real $x$ with
$|x| \le 1$, $|e^{ix} - 1 - ix| \le x^2$.

Formalized by `ProbabilityTheory.norm_exp_ofReal_mul_I_sub_one_sub_le`, a theorem declared in [MathlibExt/Probability/LindebergFeller.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LindebergFeller.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/lindeberg-feller-central-limit-theorem/index.html#norm-exp-of-real-mul-i-sub-one-sub-le).

## Comparing a finite product with the exponential of a sum

Let $s$ be a finite index
set and let $u_i \in \mathbb{C}$ for $i \in s$. If $|u_i| \le 1/2$ for every $i \in s$, then

$$
\Bigl|\prod_{i \in s} (1 + u_i) - \exp\Bigl(\sum_{i \in s} u_i\Bigr)\Bigr| \le
\Bigl(\sum_{i \in s} |u_i|^2\Bigr) \exp\Bigl(\sum_{i \in s} |u_i|\Bigr).
$$

This is the estimate that turns the second-order expansion of each characteristic function
into convergence of the product.

Formalized by `ProbabilityTheory.prod_one_add_sub_exp_sum_le`, a theorem declared in [MathlibExt/Probability/LindebergFeller.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LindebergFeller.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/lindeberg-feller-central-limit-theorem/index.html#prod-one-add-sub-exp-sum-le).

## Analytic core of the Lindeberg–Feller theorem

Let $\mu$ be a probability measure on
$\Omega$ and let $X_{n,k}$ ($n \in \mathbb{N}$, $0 \le k < n$) be real random variables on
$\Omega$ such that each $X_{n,k}$ has mean $0$ and each $X_{n,k}^2$ is integrable (expectations
are taken under $\mu$). Suppose that for some $\sigma > 0$ the row variances
$\sum_{k < n} \mathbb{E}[X_{n,k}^2]$ converge to $\sigma^2$ and that the array satisfies the
Lindeberg condition. Then for every real $t$ the product $\prod_{k < n} \varphi_{n,k}(t)$ of the
characteristic functions $\varphi_{n,k}$ of the laws of the $X_{n,k}$ converges to
$e^{-\sigma^2 t^2 / 2}$ as $n \to \infty$.

Formalized by `ProbabilityTheory.lindeberg_charFun_product_tendsto`, a theorem declared in [MathlibExt/Probability/LindebergFeller.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LindebergFeller.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/lindeberg-feller-central-limit-theorem/index.html#lindeberg-char-fun-product-tendsto).

## Lindeberg–Feller central limit theorem

Let $\mu$ be a probability measure on $\Omega$
and let $X_{n,k}$ ($n \in \mathbb{N}$, $0 \le k < n$) be a triangular array of real random
variables on $\Omega$ such that for each $n$ the variables $X_{n,0}, \dots, X_{n,n-1}$ are
independent, each $X_{n,k}$ has mean $0$, and each $X_{n,k}^2$ is integrable (expectations are
taken under $\mu$). Suppose that for some $\sigma > 0$ the row variances
$\sum_{k < n} \mathbb{E}[X_{n,k}^2]$ converge to $\sigma^2$ and that the array satisfies the
Lindeberg condition. Then the row sums $S_n = \sum_{k < n} X_{n,k}$ converge in distribution to
the Gaussian law $N(0, \sigma^2)$: for every bounded continuous $f : \mathbb{R} \to \mathbb{R}$,
$\mathbb{E}[f(S_n)] \to \int_{\mathbb{R}} f \, dN(0, \sigma^2)$ as $n \to \infty$.

Formalized by `ProbabilityTheory.lindeberg_feller_clt_triangular`, a theorem declared in [MathlibExt/Probability/LindebergFeller.lean, line 1017](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LindebergFeller.lean#L1017). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/lindeberg-feller-central-limit-theorem/index.html#lindeberg-feller-clt-triangular).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lindeberg–Feller central limit theorem](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/lindeberg-feller-central-limit-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/central-limit-theorems/lindeberg-feller-central-limit-theorem)
