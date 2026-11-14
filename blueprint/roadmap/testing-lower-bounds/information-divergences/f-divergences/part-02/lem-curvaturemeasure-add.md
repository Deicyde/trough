---
declaration: lemma
origin: cited
lean: ProbabilityTheory.DivFunction.curvatureMeasure_add
statement: formalized
proof: formalized
---

# curvatureMeasure_add

Let $f,g$ be two convex functions whose effective domains have the same endpoints $a \le b$, and such that the right derivatives $f'_+$ and $g'_+$ either both tend to $-\infty$ at $a$ or both have a finite limit at $a$. Then the curvature measure of $f+g$ is $\gamma_{f+g} = \gamma_f + \gamma_g$ . In particular, this holds for $f,g: \mathbb{R} \to \mathbb{R}$ two convex functions.

## Depends on

- [Curvature measure](def-curvaturemeasure.md)

## Proof

The right derivative of $f+g$ is $f'_+ + g'_+$, seen as functions with values in $[-\infty, +\infty]$ ($-\infty$ below the domain, $+\infty$ above it). By the assumptions, $f'_+$ and $g'_+$ are equal to $-\infty$ at the same points and equal to $+\infty$ at the same points. On the region where both are finite, $\gamma_{f+g}((x,y]) = \gamma_f((x,y]) + \gamma_g((x,y])$. The region where $f'_+$ and $g'_+$ are $-\infty$, and the region above the first point where they are $+\infty$, are null for the three measures. At $a$ and $b$, the three measures have the same atoms (equal to $0$ or $+\infty$).

The assumption at $a$ is needed: if $f'_+(x) \to -\infty$ as $x \downarrow a$ but $g'_+$ has a finite limit at $a$, then $\gamma_g$ has an infinite atom at $a$ but $\gamma_{f+g}$ does not.

## Lean

Formalized as [`ProbabilityTheory.DivFunction.curvatureMeasure_add`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.DivFunction.curvatureMeasure_add).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 582](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L582)
