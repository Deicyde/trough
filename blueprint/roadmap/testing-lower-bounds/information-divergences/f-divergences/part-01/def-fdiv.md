---
declaration: definition
origin: cited
lean: ProbabilityTheory.fDiv
statement: formalized
---

# f-divergence

Let $f : \mathbb{R} \to \mathbb{R}$ and let $\mu, \nu$ be two measures on a measurable space $\mathcal X$. The f-divergence between $\mu$ and $\nu$ is

$$
\begin{aligned}
D_f(\mu, \nu) = \nu\left[x \mapsto f\left(\frac{d \mu}{d \nu}(x)\right)\right] + f'(\infty) \mu_{\perp \nu}(\mathcal X)
\end{aligned}
$$

if $x \mapsto f\left(\frac{d \mu}{d \nu}(x)\right)$ is $\nu$-integrable and $+\infty$ otherwise.

## Depends on

- [derivAtTop](../../../convex-functions-of-radon-nikodym-derivatives/def-derivattop.md)

## Lean

Formalized as [`ProbabilityTheory.fDiv`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 10](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L10)
