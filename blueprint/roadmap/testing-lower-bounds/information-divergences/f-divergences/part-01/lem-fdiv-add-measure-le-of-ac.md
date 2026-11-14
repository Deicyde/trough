---
declaration: lemma
origin: cited
lean: ProbabilityTheory.fDiv_add_measure_le_of_ac
statement: formalized
proof: formalized
---

# Superseded by Lemma fDiv_add_measure_le

Let $\mu_1, \mu_2, \nu$ be three finite measures on $\mathcal X$ with $\mu_1 \ll \nu$ and $\mu_2 \ll \nu$. Then $D_f(\mu_1 + \mu_2, \nu) \le D_f(\mu_1, \nu) + \mu_2(\mathcal X) f'(\infty)$.

## Depends on

- [f-divergence](def-fdiv.md)

## Proof

$$
\begin{aligned}
D_f(\mu_1 + \mu_2, \nu)
&= \int_x f \left( \frac{d \mu_1}{d\nu}(x) + \frac{d\mu_2}{d\nu}(x) \right) \partial \nu
\\
&\le \int_x f \left( \frac{d \mu_1}{d\nu}(x) \right) + \frac{d\mu_2}{d\nu}(x) f'(\infty) \partial \nu
\\
&= D_f(\mu_1, \nu) + \mu_2(\mathcal X) f'(\infty)
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.fDiv_add_measure_le_of_ac`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_add_measure_le_of_ac).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 234](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L234)
