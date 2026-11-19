---
declaration: lemma
origin: cited
lean: ProbabilityTheory.fDiv_map_eq_fDiv_trim_of_ac
statement: formalized
proof: formalized
---

# fDiv_map_eq_fDiv_trim_of_ac

Let $\mu, \nu \in \mathcal M(\mathcal X)$ be finite measures with $\mu \ll \nu$ and let $g : \mathcal X \to \mathcal Y$ be a measurable function. Denote by $g^* \mathcal Y$ the comap of the $\sigma$-algebra on $\mathcal Y$ by $g$. Then $D_f(g_* \mu, g_* \nu) = D_f(\mu_{| g^* \mathcal Y}, \nu_{| g^* \mathcal Y})$ .

## Depends on

- [f-divergence](../part-01/def-fdiv.md)

## Proof

Using Lemma [rnDeriv_map_eq_rnDeriv_trim](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/rn_deriv.tex#L455),

$$
\begin{aligned}
D_f(g_* \mu, g_* \nu)
&= \int_y f \left( \frac{d g_*\mu}{d g_*\nu}(y)\right) \partial(g_*\nu)
\\
&= \int_x f \left( \frac{d g_*\mu}{d g_*\nu}(g(x))\right) \partial\nu
\\
&= \int_x f \left(\frac{d \mu_{| g^* \mathcal Y}}{d \nu_{| g^* \mathcal Y}}(x) \right) \partial\nu
\\
&= \int_x f \left(\frac{d \mu_{| g^* \mathcal Y}}{d \nu_{| g^* \mathcal Y}}(x) \right) \partial\nu_{| g^* \mathcal Y}
\\
&= D_f(\mu_{| g^* \mathcal Y}, \nu_{| g^* \mathcal Y})
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.fDiv_map_eq_fDiv_trim_of_ac`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_map_eq_fDiv_trim_of_ac).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 1204](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L1204)
