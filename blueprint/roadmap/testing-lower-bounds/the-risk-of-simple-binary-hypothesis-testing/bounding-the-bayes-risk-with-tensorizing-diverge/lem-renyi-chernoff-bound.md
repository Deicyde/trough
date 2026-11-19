---
declaration: lemma
origin: cited
lean: ProbabilityTheory.measure_llr_gt_renyiDiv_le_exp
statement: formalized
proof: formalized
---

# Change of measure - c.g.f.

For $\mu, \nu$ finite measures and $\alpha, \beta > 0$,

$$
\begin{aligned}
\mu\left\{ \log\frac{d \mu}{d \nu} > R_{1+\alpha}(\mu, \nu) + \beta \right\}
\le e^{- \alpha \beta}
\: .
\end{aligned}
$$

## Depends on

- [Rényi divergence](../../information-divergences/renyi-divergences/def-renyi.md)

## Proof

This is a Chernoff bound, using that the cumulant generating function of $\log\frac{d\mu}{d\nu}$ under $\mu$ has value $\alpha R_{1+\alpha}(\mu, \nu)$ at $\alpha$ by Lemma [renyi_cgf_2](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/renyi_divergence.tex#L116).

$$
\begin{aligned}
\mu\left\{ \log\frac{d \mu}{d \nu} > R_{1+\alpha}(\mu, \nu) + \beta \right\}
&= \mu\left\{ \exp\left(\alpha\log\frac{d \mu}{d \nu}\right) > \exp\left(\alpha R_{1+\alpha}(\mu, \nu) + \alpha \beta\right) \right\}
\\
&\le e^{-\alpha R_{1+\alpha}(\mu, \nu) - \alpha \beta} \mu\left[\left(\frac{d \mu}{d \nu}\right)^\alpha \right]
\end{aligned}
$$

Then $\mu\left[\left(\frac{d \mu}{d \nu}\right)^\alpha \right] = \nu\left[\left(\frac{d \mu}{d \nu}\right)^{1+\alpha} \right] = e^{\alpha R_{1+\alpha}(\mu, \nu)}$.

## Lean

Formalized as [`ProbabilityTheory.measure_llr_gt_renyiDiv_le_exp`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.measure_llr_gt_renyiDiv_le_exp).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/testing.tex, line 544](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/testing.tex#L544)
