---
declaration: theorem
origin: cited
lean: ProbabilityTheory.le_fDiv_compProd
statement: formalized
proof: formalized
---

# fDiv_le_compProd_1

Let $\mu, \nu$ be two finite measures on $\mathcal X$ and let $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ be two Markov kernels, with either $\mathcal X$ countable or $\mathcal{Y}$ countably generated. Then $D_f(\mu, \nu) \le D_f(\mu \otimes \kappa, \nu \otimes \eta)$.

## Depends on

- [f-divergence](../part-01/def-fdiv.md)

## Proof depends on

- [rnDeriv_compProd](../../../radon-nikodym-derivatives-and-disintegration/composition-product/lem-rnderiv-compprod.md)
- [rnDeriv_value](../../../radon-nikodym-derivatives-and-disintegration/kernel-radon-nikodym-derivative/cor-rnderiv-value.md)

## Proof

TODO: the following proof assumes $\mu \ll \nu$ and $\kappa(x) \ll \eta(x)$ for $\nu$-almost all $x$. Describe the general case.

Using Lemma [rnDeriv_compProd](../../../radon-nikodym-derivatives-and-disintegration/composition-product/lem-rnderiv-compprod.md) and [rnDeriv_value](../../../radon-nikodym-derivatives-and-disintegration/kernel-radon-nikodym-derivative/cor-rnderiv-value.md),

$$
\begin{aligned}
D(\mu \otimes \kappa, \nu \otimes \eta)
&= \int_x \int_y f \left( \frac{\partial \mu}{\partial\nu}(x) \frac{\partial \kappa(x)}{\partial\eta(x)}(y) \right) \partial \eta(x) \partial \nu
\: .
\end{aligned}
$$

Since $f$ is convex, by Jensen's inequality,

$$
\begin{aligned}
\int_y f \left( \frac{\partial \mu}{\partial\nu}(x) \frac{\partial \kappa(x)}{\partial\eta(x)}(y) \right) \partial \eta(x)
&\ge f \left( \int_y \frac{\partial \mu}{\partial\nu}(x) \frac{\partial \kappa(x)}{\partial\eta(x)}(y) \partial \eta(x) \right)
\\
&= f \left( \frac{\partial \mu}{\partial\nu}(x) \int_y \frac{\partial \kappa(x)}{\partial\eta(x)}(y) \partial \eta(x) \right)
\: .
\end{aligned}
$$

Since $\kappa(x) \ll \eta(x)$ for $\nu$-almost all $x$, $\int_y \frac{\partial \kappa(x)}{\partial\eta(x)}(y) \partial \eta(x) = \int_y 1 \partial \kappa(x) = 1$ a.e.. We have obtained

$$
\begin{aligned}
D_f(\mu \otimes \kappa, \nu \otimes \eta)
\ge \int_x f \left( \frac{\partial \mu}{\partial\nu}(x)\right) \partial \nu
= D_f(\mu, \nu)
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.le_fDiv_compProd`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.le_fDiv_compProd).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 976](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L976)
