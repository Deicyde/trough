---
declaration: definition
origin: cited
lean: Loop, Loop.average, Loop.support
statement: formalized
---

# loop

A loop is a map defined on the circle $𝕊^1 = ℝ/ℤ$ with values in a finite-dimensional vector space. It can also freely be seen as $1$-periodic maps defined on $ℝ$.

The average of a loop $γ$ is $\bar γ := \int_{𝕊^1} γ(s)\, ds$.

The *support* of a family $γ$ of loops in $F$ parametrized by $E$ is the closure of the set of $x$ in $E$ such that $γ_x$ is not a constant loop.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Loop`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/Loop), [`Loop.average`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/Loop.average), [`Loop.support`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/Loop.support).

## Sources

- [Sphere eversion blueprint: loops.tex, line 13](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/loops.tex#L13)
