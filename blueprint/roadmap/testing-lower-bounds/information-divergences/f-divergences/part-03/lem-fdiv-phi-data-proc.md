---
declaration: lemma
origin: cited
lean: ProbabilityTheory.fDiv_statInfoFun_comp_right_le
statement: formalized
proof: formalized
---

# fDiv_phi_data_proc

Let $a,b \in [0, +\infty)$. Let $\mu, \nu$ be two finite measures on $\mathcal X$ and let $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ be a Markov kernel. Then $D_{\phi_{a,b}}(\kappa \circ \mu, \kappa \circ \nu) \le D_{\phi_{a,b}}(\mu, \nu)$.

## Depends on

- [f-divergence](../part-01/def-fdiv.md)
- [statInfoFun](../part-02/def-statinfofun.md)

## Proof depends on

- [Data-processing inequality](../../statistical-divergences/part-01/thm-data-proc-statinfo.md)
- [fDiv_statInfoFun_eq_statInfo](cor-fdiv-statinfofun-eq-statinfo.md)

## Proof

By Corollary [fDiv_statInfoFun_eq_statInfo](cor-fdiv-statinfofun-eq-statinfo.md),

$$
\begin{aligned}
D_{\phi_{a,b}}(\mu, \nu) = \mathcal I_{(a,b)}(\mu, \nu) + \frac{1}{2} \left\vert a \mu(\mathcal X) - b \nu(\mathcal X) \right\vert + \text{sign}(b-a)\frac{1}{2}(a \mu(\mathcal X) - b \nu(\mathcal X))
\: .
\end{aligned}
$$

The statistical information satisfies the data-processing inequality (Theorem [Data-processing inequality](../../statistical-divergences/part-01/thm-data-proc-statinfo.md)) and the other terms are invariant by composition with a Markov kernel, hence $D_{\phi_{a,b}}$ also satisfies the data-processing inequality.

## Lean

Formalized as [`ProbabilityTheory.fDiv_statInfoFun_comp_right_le`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_statInfoFun_comp_right_le).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 1128](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L1128)
