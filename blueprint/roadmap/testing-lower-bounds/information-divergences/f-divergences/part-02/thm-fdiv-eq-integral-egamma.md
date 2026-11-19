---
declaration: theorem
origin: cited
lean: ProbabilityTheory.fDiv_eq_lintegral_fDiv_statInfoFun
statement: formalized
proof: formalized
---

# fDiv_eq_integral_eGamma

For two finite measures $\mu, \nu \in \mathcal M(\mathcal X)$,

$$
\begin{aligned}
D_f(\mu, \nu) = f(1) \nu(\mathcal X) + f'_+(1)(\mu(\mathcal X) - \nu(\mathcal X)) + \int_y D_{\phi_{1,y}}(\mu, \nu) \partial\gamma_f \: .
\end{aligned}
$$

## Depends on

- [f-divergence](../part-01/def-fdiv.md)
- [Curvature measure](def-curvaturemeasure.md)
- [eGamma](../../statistical-divergences/part-01/def-egamma.md)

## Proof

We prove the result for $f(1) = 0$ and $f'_+(1) = 0$ for simplicity of exposition.

From Corollary [convex_taylor_statInfoFun](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L664) we get that $f(x) = \int_y \phi_{1,y}(x) \partial\gamma_f$ . From this and the theorem of Fubini,

$$
\begin{aligned}
\int_x f\left( \frac{d \mu}{d \nu}(x) \right) \partial\nu
= \int_{x} \int_{y} \phi_{1,y} \left(\frac{d \mu}{d \nu}(x) \right) \partial\gamma_f \partial\nu
= \int_{y} \int_{x} \phi_{1,y} \left(\frac{d \mu}{d \nu}(x) \right) \partial\nu \partial\gamma_f
\: .
\end{aligned}
$$

For the mutually singular part of the divergence $D_f$,

$$
\begin{aligned}
f'(\infty)
= f'_+(\infty) - f'_+(1)
= \gamma_f((1,+\infty))
= \int_{y > 1} 1 \partial \gamma_f
= \int_{y > 1} \phi_{1,y}'(\infty) \partial \gamma_f
\: .
\end{aligned}
$$

The last integral is equal to $\int_{y \in \mathbb{R}} \phi_{1,y}'(\infty) \partial \gamma_f$ since $\phi_{1,y}'(\infty) = 0$ for $y \le 1$. Finally,

$$
\begin{aligned}
D_f(\mu, \nu)
&= \int_x f\left( \frac{d \mu}{d \nu}(x) \right) \partial\nu + f'(\infty) \mu_{\perp \nu}(\mathcal X)
\\
&= \int_{y} \left(\int_{x} \phi_{1,y} \left(\frac{d \mu}{d \nu}(x) \right) \partial\nu + \phi_{1,y}'(\infty) \mu(\mathcal X) \right) \partial\gamma_f
\\
&= \int_y D_{\phi_{1,y}}(\mu, \nu) \partial \gamma_f
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.fDiv_eq_lintegral_fDiv_statInfoFun`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_eq_lintegral_fDiv_statInfoFun).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 708](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L708)
