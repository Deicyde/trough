---
declaration: lemma
origin: cited
lean: ProbabilityTheory.one_sub_exp_le_add_measure_mul_exp_max_renyiDiv
statement: formalized
proof: formalized
---

# renyi_change_measure_add

Let $\mu, \nu, \xi$ be three probability measures on $\mathcal X$ and let $E$ be an event on $\mathcal X$. Let $\alpha, \beta \ge 0$. Then

$$
\begin{aligned}
\mu(E) e^{R_{1+\alpha}(\xi, \mu) + \beta} + \nu(E^c) e^{R_{1+\alpha}(\xi, \nu) + \beta} \ge 1 - 2 e^{-\alpha \beta} \: .
\end{aligned}
$$

## Depends on

- [Rényi divergence](../../information-divergences/renyi-divergences/def-renyi.md)

## Proof depends on

- [3 points change of measure](lem-llr-change-measure-add.md)
- [Change of measure - c.g.f.](lem-renyi-chernoff-bound.md)

## Proof

Use Lemma [3 points change of measure](lem-llr-change-measure-add.md) with the choices $R_{1+\alpha}(\xi, \mu) + \beta$ and $R_{1+\alpha}(\xi, \nu) + \beta$ for $\beta_1$ and $\beta_2$. Then apply Lemma [Change of measure - c.g.f.](lem-renyi-chernoff-bound.md).

## Lean

Formalized as [`ProbabilityTheory.one_sub_exp_le_add_measure_mul_exp_max_renyiDiv`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.one_sub_exp_le_add_measure_mul_exp_max_renyiDiv).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/testing.tex, line 627](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/testing.tex#L627)
