---
declaration: theorem
origin: cited
lean: ProbabilityTheory.fDiv_comp_right_le''
statement: formalized
proof: formalized
---

# Data-processing

Let $\mu, \nu$ be two finite measures on $\mathcal X$ and let $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ be a Markov kernel. Then $D_f(\kappa \circ \mu, \kappa \circ \nu) \le D_f(\mu, \nu)$.

## Depends on

- [f-divergence](../part-01/def-fdiv.md)

## Proof depends on

- [Composition-product with a kernel](thm-fdiv-compprod-left-1.md)
- [fDiv_map_le](thm-fdiv-map-le.md)

## Proof

Let $\pi_Y : \mathcal X \times \mathcal Y \to \mathcal Y$ be the projection $\pi_Y((x,y)) = y$. Then $\kappa \circ \mu = \pi_{Y*}(\mu \otimes \kappa)$ and similarly for $\nu$. We can use the DPI for that function (Theorem [fDiv_map_le](thm-fdiv-map-le.md)), then Lemma [Composition-product with a kernel](thm-fdiv-compprod-left-1.md),

$$
\begin{aligned}
D_f(\kappa \circ \mu, \kappa \circ \nu)
&= D_f(\pi_{Y*}(\mu \otimes \kappa), \pi_{Y*}(\nu \otimes \kappa))
\\
&\le D_f(\mu \otimes \kappa, \nu \otimes \kappa)
\\
&= D_f(\mu, \nu)
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.fDiv_comp_right_le''`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_comp_right_le'').

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 929](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L929)
