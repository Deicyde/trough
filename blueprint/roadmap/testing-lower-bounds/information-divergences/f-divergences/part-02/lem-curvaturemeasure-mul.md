---
declaration: lemma
origin: cited
lean: ProbabilityTheory.DivFunction.curvatureMeasure_smul
statement: formalized
proof: formalized
---

# curvatureMeasure_mul

For $a > 0$ and $f$ a convex function, the curvature measure of $af$ is $\gamma_{af} = a \gamma_f$ .

## Depends on

- [Curvature measure](def-curvaturemeasure.md)

## Proof

The right derivative of $af$ is $a f'_+$ (with values in $[-\infty, +\infty]$), hence $\gamma_{af}((x,y]) = a f'_+(y) - a f'_+(x) = a \gamma_f((x,y])$. The equality of the measures is obtained at the level of the outer measures, which are built from these interval lengths.

For $f: \mathbb{R} \to \mathbb{R}$, the case $a = 0$ is trivial. It fails in the Lean formalization, where the right derivative is $-\infty$ to the left of the domain of $f$: $0 \cdot f$ is the zero function on $[0, +\infty)$, whose right derivative jumps from $-\infty$ to $0$ at $0$, so that $\gamma_{0 \cdot f}$ has an infinite atom at $0$.

## Lean

Formalized as [`ProbabilityTheory.DivFunction.curvatureMeasure_smul`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.DivFunction.curvatureMeasure_smul).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 566](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L566)
