---
declaration: lemma
origin: cited
lean: ProbabilityTheory.one_sub_le_add_measure_mul_exp
statement: formalized
proof: formalized
---

# 3 points change of measure

Let $\mu, \nu, \xi \in \mathcal P(\mathcal X)$ and let $E$ be an event on $\mathcal X$. Let $\beta_1, \beta_2 \in \mathbb{R}$. Then

$$
\begin{aligned}
\mu(E) e^{\beta_1} + \nu(E^c) e^{\beta_2} \ge 1 - \xi\left\{ \log\frac{d \xi}{d \mu} > \beta_1 \right\} - \xi\left\{ \log\frac{d \xi}{d \nu} > \beta_2 \right\} \: .
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Change of measure lemma](lem-llr-change-measure.md)

## Proof

Two applications of Lemma [Change of measure lemma](lem-llr-change-measure.md), then sum them and use $\xi(E)+\xi(E^c) = 1$.

## Lean

Formalized as [`ProbabilityTheory.one_sub_le_add_measure_mul_exp`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.one_sub_le_add_measure_mul_exp).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/testing.tex, line 447](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/testing.tex#L447)
