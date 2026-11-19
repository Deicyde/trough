---
declaration: theorem
origin: cited
lean: ProbabilityTheory.fDiv_map_le
statement: formalized
proof: formalized
---

# fDiv_map_le

Let $\mu, \nu \in \mathcal M (\mathcal X)$ be two finite measures and let $g : \mathcal X \to \mathcal Y$ be a measurable function. Then $D_f(g_* \mu, g_* \nu) \le D_f(\mu, \nu)$.

## Depends on

- [f-divergence](../part-01/def-fdiv.md)

## Proof depends on

- [DPI_of_DPI_ac](lem-dpi-of-dpi-ac.md)
- [rnDeriv_map_eq_condexp](../../../radon-nikodym-derivatives-and-disintegration/composition/lem-rnderiv-map-eq-condexp.md)
- [condexp_jensen](../../../convex-functions-of-radon-nikodym-derivatives/thm-condexp-jensen.md)

## Proof

By Lemma [DPI_of_DPI_ac](lem-dpi-of-dpi-ac.md), it is sufficient to prove the inequality with the additional hypothesis $\mu \ll \nu$ (hence also $g_* \mu \ll g_*\nu$). In that case,

$$
\begin{aligned}
D_f(g_* \mu, g_* \nu)
&= \int_y f \left( \frac{d g_* \mu}{d g_* \nu}(y) \right) \partial(g_* \nu)
\\
&= \int_{x} f \left( \frac{d g_* \mu}{d g_* \nu}(g(x)) \right) \partial\nu
\: .
\end{aligned}
$$

By Lemma [rnDeriv_map_eq_condexp](../../../radon-nikodym-derivatives-and-disintegration/composition/lem-rnderiv-map-eq-condexp.md), $\nu$-almost everywhere,

$$
\begin{aligned}
\frac{d g_* \mu}{d g_* \nu}(g(x))
&= \nu\left[\frac{d \mu}{d \nu} \mid g^* \mathcal Y \right](x)
\: .
\end{aligned}
$$

Using that expression, then Jensen's inequality for the conditional expectation(Theorem [condexp_jensen](../../../convex-functions-of-radon-nikodym-derivatives/thm-condexp-jensen.md)), we get

$$
\begin{aligned}
D_f(g_* \mu, g_* \nu)
&= \int_{x} f \left( \nu\left[\frac{d \mu}{d \nu} \mid g^* \mathcal Y \right](x) \right) \partial\nu
\\
&\le \int_{x} \nu\left[ f \left( \frac{d \mu}{d \nu} \right) \mid g^* \mathcal Y \right](x) \partial\nu
\: .
\end{aligned}
$$

The integral of a conditional expectation is equal to the integral of the function, hence

$$
\begin{aligned}
D_f(\kappa \circ \mu, \kappa \circ \nu)
&\le \int_{x} f \left( \frac{d \mu}{d \nu}(x) \right) \partial\nu
\: .
\end{aligned}
$$

This is equal to $D_f(\mu, \nu)$.

## Lean

Formalized as [`ProbabilityTheory.fDiv_map_le`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_map_le).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 886](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L886)
