---
declaration: lemma
origin: cited
lean: ProbabilityTheory.fDiv_add_measure_le
statement: formalized
proof: formalized
---

# fDiv_add_measure_le

Let $\mu_1, \mu_2, \nu$ be three finite measures on $\mathcal X$. Then $D_f(\mu_1 + \mu_2, \nu) \le D_f(\mu_1, \nu) + \mu_2(\mathcal X) f'(\infty)$.

## Depends on

- [f-divergence](def-fdiv.md)

## Proof depends on

- [fDiv_absolutelyContinuous_add_mutuallySingular](lem-fdiv-absolutelycontinuous-add-mutuallysingul.md)
- [Superseded by Lemma fDiv_add_measure_le](lem-fdiv-add-measure-le-of-ac.md)

## Proof

From Lemma [fDiv_absolutelyContinuous_add_mutuallySingular](lem-fdiv-absolutelycontinuous-add-mutuallysingul.md), then Lemma [Superseded by Lemma fDiv_add_measure_le](lem-fdiv-add-measure-le-of-ac.md),

$$
\begin{aligned}
D_f(\mu_1 + \mu_2, \nu)
&= D_f(\frac{d\mu_1}{d \nu}\cdot \nu + \frac{d\mu_2}{d \nu}\cdot \nu, \nu) + (\mu_1)_{\perp\nu}(\mathcal X) f'(\infty) + (\mu_2)_{\perp\nu}(\mathcal X) f'(\infty)
\\
&\le D_f(\frac{d\mu_1}{d \nu}\cdot \nu, \nu) + (\frac{d\mu_2}{d \nu}\cdot \nu)(\mathcal X) f'(\infty) + (\mu_1)_{\perp\nu}(\mathcal X) f'(\infty) + (\mu_2)_{\perp\nu}(\mathcal X) f'(\infty)
\\
&= D_f(\mu_1, \nu) + \mu_2(\mathcal X) f'(\infty)
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.fDiv_add_measure_le`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_add_measure_le).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 256](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L256)
