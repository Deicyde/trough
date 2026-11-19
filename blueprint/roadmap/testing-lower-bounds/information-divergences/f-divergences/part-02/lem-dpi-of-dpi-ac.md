---
declaration: lemma
origin: cited
lean: ProbabilityTheory.fDiv_comp_le_of_comp_le_of_ac
statement: formalized
proof: formalized
---

# DPI_of_DPI_ac

Let $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ be a Markov kernel and $\nu \in \mathcal M(\mathcal X)$ be a finite measure. Suppose that for all finite measures $\mu \in \mathcal M(\mathcal X)$ with $\mu \ll \nu$, $D_f(\kappa \circ \mu, \kappa \circ \nu) \le D_f(\mu, \nu)$. Then the same is true without the absolute continuity hypothesis.

## Depends on

- [f-divergence](../part-01/def-fdiv.md)

## Proof depends on

- [fDiv_add_measure_le](../part-01/lem-fdiv-add-measure-le.md)

## Proof

We use $\kappa \circ \mu = \kappa \circ (\frac{d\mu}{d\nu}\cdot \nu) + \kappa \circ \mu_{\perp \nu}$ . By Lemma [fDiv_add_measure_le](../part-01/lem-fdiv-add-measure-le.md),

$$
\begin{aligned}
D_f(\kappa \circ \mu, \kappa \circ \nu)
\le D_f\left(\kappa \circ (\frac{d\mu}{d\nu}\cdot \nu), \kappa \circ \nu\right)
+ (\kappa \circ \mu_{\perp \nu})(\mathcal Y) f'(\infty)
\: .
\end{aligned}
$$

Since $\kappa$ is a Markov kernel, $(\kappa \circ \mu_{\perp \nu})(\mathcal Y) = \mu_{\perp \nu}(\mathcal Y)$.

By hypothesis, since $\frac{d\mu}{d\nu}\cdot \nu \ll \nu$, $D_f\left(\kappa \circ (\frac{d\mu}{d\nu}\cdot \nu), \kappa \circ \nu\right) \le D_f\left(\frac{d\mu}{d\nu}\cdot \nu, \nu\right)$. We get

$$
\begin{aligned}
D_f(\kappa \circ \mu, \kappa \circ \nu)
&\le D_f\left(\frac{d\mu}{d\nu}\cdot \nu,\nu\right)
+ \mu_{\perp \nu}(\mathcal Y) f'(\infty)
\\
&= D_f(\mu, \nu)
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.fDiv_comp_le_of_comp_le_of_ac`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_comp_le_of_comp_le_of_ac).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 796](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L796)
