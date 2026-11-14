---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.toReal_rnDeriv_map
---

# rnDeriv_map_eq_condexp

Let $\mu, \nu \in \mathcal M(\mathcal X)$ with $\mu \ll \nu$, $g : \mathcal X \to \mathcal Y$ a measurable function and denote by $g^* \mathcal Y$ the comap of the $\sigma$-algebra on $\mathcal Y$ by $g$. Then $\nu$-almost everywhere,

$$
\begin{aligned}
\frac{d g_*\mu}{d g_*\nu}(g(x)) = \nu\left[ \frac{d \mu}{d \nu} \mid g^* \mathcal Y\right](x)
\: .
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We show that the integrals of the two functions agree on all $g^* \mathcal Y$-measurable sets. It suffices to show equality on all sets oc $\mathcal X$ of the form $g^{-1}(t)$ for $t$ a measurable set of $\mathcal Y$. TODO: also show measurability.

$$
\begin{aligned}
\int_{x \in g^{-1}(t)}\frac{d g_*\mu}{d g_*\nu}(g(x)) \partial\nu
&= \int_{y \in t}\frac{d g_*\mu}{d g_*\nu}(y) \partial(g_*\nu)
\\
&= g_*\mu (t)
\: .
\end{aligned}
$$

$$
\begin{aligned}
\int_{x \in g^{-1}(t)}\nu\left[ \frac{d \mu}{d \nu} \mid g^* \mathcal Y\right](x) \partial\nu
&= \int_{x \in g^{-1}(t)}\frac{d \mu}{d \nu}(x) \partial\nu
\\
&= \mu(g^{-1}(t))
\\
&= g_*\mu(t)
\: .
\end{aligned}
$$

## Lean

Formalized as [`MeasureTheory.toReal_rnDeriv_map`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/MeasureTheory.toReal_rnDeriv_map).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/rn_deriv.tex, line 338](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/rn_deriv.tex#L338)
