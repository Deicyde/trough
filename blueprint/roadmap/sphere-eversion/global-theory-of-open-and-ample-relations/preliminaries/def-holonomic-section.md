---
declaration: definition
origin: cited
lean: OneJetSec.IsHolonomicAt, OneJetSec.isHolonomicAt_iff
statement: formalized
---

# holonomic_section

A section $\mathcal{F}$ of $J^1(M, N) → M$ is called holonomic if it is the $1$–jet of its base map. Equivalently, $\mathcal{F}$ is holonomic if there exists $f \!: M → N$ such that $\mathcal{F} = j^1f$, since such a map is necessarily $\operatorname{bs} \mathcal{F}$.

## Depends on

- [one_jet_space](def-one-jet-space.md)

## Lean

Formalized as [`OneJetSec.IsHolonomicAt`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/OneJetSec.IsHolonomicAt), [`OneJetSec.isHolonomicAt_iff`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/OneJetSec.isHolonomicAt_iff).

## Sources

- [Sphere eversion blueprint: global_convex_integration.tex, line 367](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/global_convex_integration.tex#L367)
