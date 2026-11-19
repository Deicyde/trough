---
declaration: theorem
origin: cited
lean: ProbabilityTheory.fDiv_comp_right_le'
statement: formalized
proof: formalized
---

# Data-processing

Let $\mu, \nu$ be two finite measures on $\mathcal X$ and let $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ be a Markov kernel. Then $D_f(\kappa \circ \mu, \kappa \circ \nu) \le D_f(\mu, \nu)$.

## Depends on

- [f-divergence](../part-01/def-fdiv.md)

## Proof depends on

- [fDiv_eq_integral_eGamma](../part-02/thm-fdiv-eq-integral-egamma.md)
- [fDiv_phi_data_proc](lem-fdiv-phi-data-proc.md)

## Proof

By Theorem [fDiv_eq_integral_eGamma](../part-02/thm-fdiv-eq-integral-egamma.md),

$$
\begin{aligned}
D_f(\mu, \nu) = f(1) \nu(\mathcal X) + f'_+(1) (\mu(\mathcal X) - \nu (\mathcal X)) + \int_y D_{\phi_{1,y}}(\mu, \nu) \partial\gamma_f \: .
\end{aligned}
$$

The first two terms are unchanged by composition with a Markov kernel. It thus suffices to prove the data processing inequality for the divergences $D_{\phi_{1, \gamma}}$. This was done in Lemma [fDiv_phi_data_proc](lem-fdiv-phi-data-proc.md).

## Lean

Formalized as [`ProbabilityTheory.fDiv_comp_right_le'`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_comp_right_le').

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 1148](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L1148)
