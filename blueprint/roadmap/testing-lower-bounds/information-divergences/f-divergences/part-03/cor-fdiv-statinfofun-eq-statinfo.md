---
declaration: corollary
origin: cited
lean: ProbabilityTheory.fDiv_statInfoFun_eq_StatInfo_of_nonneg
statement: formalized
proof: formalized
---

# fDiv_statInfoFun_eq_statInfo

Let $a,b \in [0, +\infty)$ and let $\mu, \nu$ be two measures on $\mathcal X$.

$$
\begin{aligned}
D_{\phi_{a,b}}(\mu, \nu) = \mathcal I_{(a,b)}(\mu, \nu) + \frac{1}{2} \left\vert a \mu(\mathcal X) - b \nu(\mathcal X) \right\vert + \text{sign}(b-a)\frac{1}{2}(a \mu(\mathcal X) - b \nu(\mathcal X))
\: .
\end{aligned}
$$

## Depends on

- [f-divergence](../part-01/def-fdiv.md)
- [statInfoFun](../part-02/def-statinfofun.md)
- [statInfo](../../statistical-divergences/part-01/def-statinfo.md)

## Proof depends on

- [fDiv_statInfoFun_eq](../part-02/lem-fdiv-statinfofun-eq.md)
- [statInfo_eq_integral_abs](../../statistical-divergences/part-01/cor-statinfo-eq-integral-abs.md)

## Proof

Combine Lemma [fDiv_statInfoFun_eq](../part-02/lem-fdiv-statinfofun-eq.md) and Corollary [statInfo_eq_integral_abs](../../statistical-divergences/part-01/cor-statinfo-eq-integral-abs.md).

## Lean

Formalized as [`ProbabilityTheory.fDiv_statInfoFun_eq_StatInfo_of_nonneg`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_statInfoFun_eq_StatInfo_of_nonneg).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 1110](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L1110)
