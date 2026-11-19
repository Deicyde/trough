---
declaration: lemma
origin: cited
lean: ProbabilityTheory.fDiv_tvDivFun, ProbabilityTheory.tv_eq_fDiv_tvDivFun
statement: formalized
proof: formalized
---

# tv_eq_fDiv

On probability measures, the total variation distance $\operatorname{TV}$ is an $f$-divergence for the function $x \mapsto \frac{1}{2}\vert x - 1 \vert$.

## Depends on

- [TV](../../statistical-divergences/part-01/def-tv.md)
- [f-divergence](../part-01/def-fdiv.md)

## Proof

This is a reformulation of Lemma [tv_eq_integral_abs](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/stat_div.tex#L611).

## Lean

Formalized as [`ProbabilityTheory.fDiv_tvDivFun`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_tvDivFun), [`ProbabilityTheory.tv_eq_fDiv_tvDivFun`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.tv_eq_fDiv_tvDivFun).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 1731](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L1731)
