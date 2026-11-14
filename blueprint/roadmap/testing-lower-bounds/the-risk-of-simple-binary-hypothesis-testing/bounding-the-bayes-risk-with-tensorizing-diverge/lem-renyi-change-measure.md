---
declaration: lemma
origin: cited
lean: ProbabilityTheory.measure_sub_le_measure_mul_exp_renyiDiv
statement: formalized
proof: formalized
---

# renyi_change_measure

Let $\mu, \nu$ be two finite measures on $\mathcal X$ and let $E$ be an event on $\mathcal X$. Let $\alpha,\beta > 0$. Then

$$
\begin{aligned}
\nu(E) e^{R_{1+\alpha}(\mu, \nu) + \beta} \ge \mu(E) - e^{-\alpha \beta} \: .
\end{aligned}
$$

## Depends on

- [Rényi divergence](../../information-divergences/renyi-divergences/def-renyi.md)

## Proof depends on

- [Change of measure lemma](lem-llr-change-measure.md)
- [Change of measure - c.g.f.](lem-renyi-chernoff-bound.md)

## Proof

Use Lemma [Change of measure lemma](lem-llr-change-measure.md) with the choice $R_{1+\alpha}(\mu, \nu) + \beta$ for $\beta$. Then apply Lemma [Change of measure - c.g.f.](lem-renyi-chernoff-bound.md).

## Lean

Formalized as [`ProbabilityTheory.measure_sub_le_measure_mul_exp_renyiDiv`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.measure_sub_le_measure_mul_exp_renyiDiv).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/testing.tex, line 570](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/testing.tex#L570)
