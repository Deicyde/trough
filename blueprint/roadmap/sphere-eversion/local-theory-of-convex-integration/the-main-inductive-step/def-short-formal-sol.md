---
declaration: definition
origin: cited
lean: RelLoc.FormalSol.IsShortAt
statement: formalized
---

# short_formal_sol

A formal solution $\mathcal{F}$ of $\mathcal{R}$ is $(π, v)$–short if, for every $x$, $Df(x)v$ belongs to the interior of the convex hull of $\operatorname{Conn}_{φ(v)}\mathcal{R}((x, f(x), φ(x)), π, v)$.

## Depends on

- [formal_sol_loc](def-formal-sol-loc.md)
- [dual_pair](../key-construction/def-dual-pair.md)

## Lean

Formalized as [`RelLoc.FormalSol.IsShortAt`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/RelLoc.FormalSol.IsShortAt).

## Sources

- [Sphere eversion blueprint: local_convex_integration.tex, line 178](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/local_convex_integration.tex#L178)
