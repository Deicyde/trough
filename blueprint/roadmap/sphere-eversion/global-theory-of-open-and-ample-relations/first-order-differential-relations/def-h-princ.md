---
declaration: definition
origin: cited
lean: RelMfld.SatisfiesHPrinciple, RelMfld.SatisfiesHPrincipleWith
statement: formalized
---

# h-princ

A first order differential relation $\mathcal{R} ⊂ J^1(M, N)$ satisfies the $h$-principle if every formal solution of $\mathcal{R}$ is homotopic to a holonomic one. It satisfies the parametric $h$-principle if, for every manifold $P$ and every closed set $C$ in $P × M$, every family $\mathcal{F} : P × M → J^1(M, N)$ of formal solutions which are holonomic for $(p, m)$ near $C$ is homotopic to a family of holonomic ones relative to $C$.

## Depends on

- [htpy_formal_sol](def-htpy-formal-sol.md)

## Lean

Formalized as [`RelMfld.SatisfiesHPrinciple`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/RelMfld.SatisfiesHPrinciple), [`RelMfld.SatisfiesHPrincipleWith`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/RelMfld.SatisfiesHPrincipleWith).

## Sources

- [Sphere eversion blueprint: global_convex_integration.tex, line 469](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/global_convex_integration.tex#L469)
