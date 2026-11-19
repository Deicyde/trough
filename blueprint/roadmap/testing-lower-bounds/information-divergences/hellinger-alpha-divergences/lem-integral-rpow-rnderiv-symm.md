---
declaration: lemma
origin: cited
lean: ProbabilityTheory.integral_rpow_rnDeriv_symm
statement: formalized
proof: formalized
---

# integral_rpow_rnDeriv_symm

For $\alpha \in (0,1)\cup(1, \infty)$, $\mu, \nu$ two sigma-finite measures,

$$
\begin{aligned}
\int_x \left(\frac{d \mu}{d \nu}(x)\right)^\alpha \partial \nu
= \int_x \left(\frac{d \nu}{d \mu}(x)\right)^{1 - \alpha} \partial \mu
\: .
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

$$
\begin{aligned}
\int_x \left(\frac{d \mu}{d \nu}(x)\right)^\alpha \partial \nu
&= \int_x \left(\frac{d \mu}{d (\mu + \nu)}(x) \left(\frac{d \nu}{d (\mu + \nu)}(x)\right)^{-1} \right)^\alpha \partial \nu \\
&= \int_x \left(\frac{d \mu}{d (\mu + \nu)}(x) \left(\frac{d \nu}{d (\mu + \nu)}(x)\right)^{-1} \right)^\alpha \frac{d \nu}{d (\mu + \nu)}(x) \partial (\mu + \nu) \\
&= \int_x \left(\frac{d \mu}{d (\mu + \nu)}(x) \left(\frac{d \nu}{d (\mu + \nu)}(x)\right)^{-1} \right)^{\alpha - 1} \frac{d \mu}{d (\mu + \nu)}(x) \partial (\mu + \nu) \\
&= \int_x \left(\frac{d \mu}{d (\mu + \nu)}(x) \left(\frac{d \nu}{d (\mu + \nu)}(x)\right)^{-1} \right)^{\alpha - 1} \partial \mu \\
&= \int_x \left(\frac{d \nu}{d \mu}(x)\right)^{1 - \alpha} \partial \mu
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.integral_rpow_rnDeriv_symm`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.integral_rpow_rnDeriv_symm).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/hellinger_alpha.tex, line 52](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/hellinger_alpha.tex#L52)
