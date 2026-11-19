---
declaration: definition
origin: cited
lean: ProbabilityTheory.DivFunction.curvatureMeasure
statement: formalized
---

# Curvature measure

Let $f: \mathbb{R} \to \mathbb{R}$ be a convex function. Then its right derivative $f'_+(x) \coloneqq \lim_{y \downarrow x}\frac{f(y) - f(x)}{y - x}$ is a Stieltjes function (a monotone right continuous function) and it defines a measure $\gamma_f$ on $\mathbb{R}$ by $\gamma_f((x,y]) \coloneqq f'_+(y) - f'_+(x)$ . (Liese 2012) calls $\gamma_f$ the curvature measure of $f$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`ProbabilityTheory.DivFunction.curvatureMeasure`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.DivFunction.curvatureMeasure).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 557](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L557)
