---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.GaussMarkov.gaussMarkov_covariance_minimality
statement: formalized
proof: formalized
---

# Linear models and multivariate analysis: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/index.html).

Multivariate normal theory and linear models: Gaussian maximum likelihood, Cochran's theorem on quadratic forms, t and F sampling laws, Gauss–Markov and generalized least squares, principal component analysis, and Gaussian graphical models.

## Gauss–Markov covariance minimality

Let $X$ be a real $m \times n$ matrix such that
$X^\top X$ is invertible, and let $B = (X^\top X)^{-1} X^\top$. Then $BX = I_n$, and for every
real $n \times m$ matrix $A$ with $AX = I_n$ the matrix $AA^\top - BB^\top$ is positive
semidefinite.

In the linear model $y = X\beta + \varepsilon$ whose noise has identity covariance, $By$ is the
least-squares estimator of $\beta$, the estimators $Ay$ with $AX = I_n$ are exactly the linear
unbiased ones, and $AA^\top$ is the covariance of $Ay$.

## Sources

- C. F. Gauss, *Theoria combinationis observationum erroribus minimis obnoxiae* (1823); A. C. Aitken, “On Least Squares and Linear Combination of Observations,” *Proceedings of the Royal Society of Edinburgh* 55 (1936), 42–48, DOI `10.1017/S0370164600014346`.

Formalized by `MathlibExt.Probability.Statistics.GaussMarkov.gaussMarkov_covariance_minimality`, a theorem declared in [MathlibExt/Probability/Statistics/GaussMarkov.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/GaussMarkov.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/index.html#gauss-markov-covariance-minimality).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linear models and multivariate analysis](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/linear-models-multivariate)
