---
declaration: section
origin: cited
lean: MeasureTheory.Martingale.condExp_sub_sq_eq, MeasureTheory.Martingale.integral_sub_mul_eq_zero, MeasureTheory.Martingale.integral_sub_sq_eq
statement: formalized
proof: formalized
---

# Square-integrable martingales

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/square-integrable-martingales/index.html).

## Conditional variance theorem for martingales

Let $(\Omega, \mu)$ be a probability space
with a filtration $(\mathcal{F}_n)_{n \in \mathbb{N}}$, and let $(X_n)_{n \in \mathbb{N}}$ be a
real-valued martingale with respect to $(\mathcal{F}_n)$ and $\mu$ such that $X_n$ is
square-integrable for every $n$. Then for all $m \le n$, almost surely

$$
\mathbb{E}[(X_n - X_m)^2 \mid \mathcal{F}_m] = \mathbb{E}[X_n^2 \mid \mathcal{F}_m] - X_m^2.
$$

This expresses the conditional variance of the increment $X_n - X_m$ in terms of the conditional
second moment of $X_n$.

## Sources

- Lecture 28, conditional variance theorem.

Formalized by `MeasureTheory.Martingale.condExp_sub_sq_eq`, a theorem declared in [MathlibExt/Probability/MartingaleConditionalVariance.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MartingaleConditionalVariance.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/square-integrable-martingales/index.html#cond-exp-sub-sq-eq).

## Orthogonality of martingale increments

Let $(\Omega, \mu)$ be a probability space with a
filtration $(\mathcal{F}_n)_{n \in \mathbb{N}}$, and let $(X_n)_{n \in \mathbb{N}}$ be a real-valued
martingale with respect to $(\mathcal{F}_n)$ and $\mu$ such that $\mathbb{E}[X_k^2] < \infty$ for
every $k$. Let $m \le n$ and let $Y$ be an $\mathcal{F}_m$-measurable real random variable with
$\mathbb{E}[Y^2] < \infty$. Then $\mathbb{E}[(X_n - X_m) Y] = 0$. In other words, the increment
$X_n - X_m$ is orthogonal in $L^2$ to every square-integrable $\mathcal{F}_m$-measurable random
variable.

## Sources

- Lecture 28, orthogonality of martingale increments.

Formalized by `MeasureTheory.Martingale.integral_sub_mul_eq_zero`, a theorem declared in [MathlibExt/Probability/MartingaleOrthogonality.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MartingaleOrthogonality.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/square-integrable-martingales/index.html#integral-sub-mul-eq-zero).

## Pythagorean identity for martingale increments

Let $(\Omega, \mu)$ be a probability
space with a filtration $(\mathcal{F}_n)_{n \in \mathbb{N}}$, and let $(X_n)_{n \in \mathbb{N}}$ be
a real-valued martingale with respect to $(\mathcal{F}_n)$ and $\mu$ such that
$\mathbb{E}[X_k^2] < \infty$ for every $k$. Then for all $m \le n$,

$$
\mathbb{E}[(X_n - X_m)^2] = \mathbb{E}[X_n^2] - \mathbb{E}[X_m^2].
$$

This is the orthogonality of martingale increments applied to the $\mathcal{F}_m$-measurable
random variable $X_m$, expanded.

Formalized by `MeasureTheory.Martingale.integral_sub_sq_eq`, a theorem declared in [MathlibExt/Probability/MartingaleOrthogonality.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MartingaleOrthogonality.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/square-integrable-martingales/index.html#integral-sub-sq-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Square-integrable martingales](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/square-integrable-martingales/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/martingales/square-integrable-martingales)
