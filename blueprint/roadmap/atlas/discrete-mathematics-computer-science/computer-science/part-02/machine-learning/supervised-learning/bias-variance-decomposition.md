---
declaration: section
origin: cited
lean: Cslib.MachineLearning.BiasVariance.integral_sq_sub_of_indepFun, Cslib.MachineLearning.BiasVariance.integral_sq_noise_sub
statement: formalized
proof: formalized
---

# Bias–variance decomposition

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bias-variance-decomposition/index.html).

## Expected squared error of independent random variables

Let $(\Omega, \mu)$ be a
probability space, with expectation $\mathbb{E}$ and variance $\operatorname{Var}$ taken with
respect to $\mu$. If $Y$ and $\hat Y$ are independent square-integrable real random variables on
$\Omega$, then $\mathbb{E}[(Y - \hat Y)^2] = \operatorname{Var}(Y) + \operatorname{Var}(\hat Y) +
(\mathbb{E}[Y] - \mathbb{E}[\hat Y])^2$.

Formalized by `Cslib.MachineLearning.BiasVariance.integral_sq_sub_of_indepFun`, a theorem declared in [CSLibExt/MachineLearning/Regression/BiasVariance.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Regression/BiasVariance.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bias-variance-decomposition/index.html#integral-sq-sub-of-indep-fun).

## The bias-variance decomposition

Let $(\Omega, \mu)$ be a probability space, with
expectation $\mathbb{E}$ and variance $\operatorname{Var}$ taken with respect to $\mu$. Let $f$ be
a real number, and let $\varepsilon$ (the noise) and $\hat Y$ (the predictor) be square-integrable
real random variables on $\Omega$ such that $\mathbb{E}[\varepsilon] = 0$ and $\varepsilon$ is
independent of $\hat Y$. Then the expected squared error of $\hat Y$ for the response
$\varepsilon + f$ is the noise variance plus the squared bias plus the variance of the predictor:
$\mathbb{E}[(\varepsilon + f - \hat Y)^2] = \operatorname{Var}(\varepsilon) +
(f - \mathbb{E}[\hat Y])^2 + \operatorname{Var}(\hat Y)$.

Formalized by `Cslib.MachineLearning.BiasVariance.integral_sq_noise_sub`, a theorem declared in [CSLibExt/MachineLearning/Regression/BiasVariance.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Regression/BiasVariance.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bias-variance-decomposition/index.html#integral-sq-noise-sub).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bias–variance decomposition](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bias-variance-decomposition/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/machine-learning/supervised-learning/bias-variance-decomposition)
