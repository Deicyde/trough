---
declaration: lemma
origin: cited
lean: ProbabilityTheory.measure_sub_le_measure_mul_exp'
statement: formalized
proof: formalized
---

# Change of measure lemma

Let $\mu, \nu$ be two measures on $\mathcal X$ with $\mu \ll \nu$ and let $E$ be an event on $\mathcal X$. Let $\beta \in \mathbb{R}$. Then

$$
\begin{aligned}
\nu(E) e^{\beta} \ge \mu(E) - \mu\left\{ \log\frac{d \mu}{d \nu} > \beta \right\} \: .
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

$$
\begin{aligned}
\nu(E)
\ge \mu\left[\mathbb{I}(E) e^{- \log\frac{d \mu}{d \nu} }\right]
&\ge \mu\left[\mathbb{I}\left(E \cap \left\{\log\frac{d \mu}{d \nu} \le \beta\right\}\right) e^{- \log\frac{d \mu}{d \nu} }\right]
\\
&\ge e^{- \beta}\mu\left(E \cap \left\{\log\frac{d \mu}{d \nu} \le \beta\right\}\right)
\\
&\ge e^{- \beta}\left( \mu(E) - \mu\left\{ \log\frac{d \mu}{d \nu} > \beta \right\} \right)
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.measure_sub_le_measure_mul_exp'`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.measure_sub_le_measure_mul_exp').

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/testing.tex, line 345](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/testing.tex#L345)
