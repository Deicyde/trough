---
declaration: lemma
origin: cited
lean: RelMfld.SatisfiesHPrinciple.satisfiesHPrincipleWith
statement: formalized
proof: formalized
---

# param_for_free

Let $\mathcal{R}$ be a first order differential relation for maps from $M$ to $N$. If, for every manifold with boundary $P$, $\mathcal{R}^P$ satisfies the $h$-principle then $\mathcal{R}$ satisfies the parametric $h$-principle. Likewise, the $C^0$-dense and relative $h$-principle for all $\mathcal{R}^P$ imply the parametric $C^0$-dense and relative $h$-principle for $\mathcal{R}$.

## Depends on

- [h-princ](def-h-princ.md)

## Proof depends on

- [param_trick](lem-param-trick.md)

## Proof

By [Lemma param_trick](lem-param-trick.md) we can turn a formal solution of $\mathcal{R}$ into a formal solution of $\mathcal{R}^P$, so we get a homotopy to a holonomic formal solution. We can turn this homotopy back to a homotopy of the original formal solution.

## Lean

Formalized as [`RelMfld.SatisfiesHPrinciple.satisfiesHPrincipleWith`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/RelMfld.SatisfiesHPrinciple.satisfiesHPrincipleWith).

## Sources

- [Sphere eversion blueprint: global_convex_integration.tex, line 520](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/global_convex_integration.tex#L520)
