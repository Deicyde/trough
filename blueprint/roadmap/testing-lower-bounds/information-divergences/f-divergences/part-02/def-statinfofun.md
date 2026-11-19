---
declaration: definition
origin: cited
lean: ProbabilityTheory.statInfoFun
statement: formalized
---

# statInfoFun

For $a,b \in (0, +\infty)$ let $\phi_{a,b} : \mathbb{R} \to \mathbb{R}$ be the function defined by

$$
\begin{aligned}
\phi_{a,b}(x) &= \max\left\{0, a x - b \right\} & \text{ for } a \le b \: ,
\\
\phi_{a,b}(x) &= \max\left\{0, b - a x \right\} & \text{ for } a > b \: .
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`ProbabilityTheory.statInfoFun`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.statInfoFun).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 650](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L650)
