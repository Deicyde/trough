---
declaration: definition
origin: cited
lean: SurroundingFamily
statement: formalized
---

# family_surrounds

A continuous family of loops $γ \!: E × [0, 1] × 𝕊^1 → F, (x, t, s) ↦ γ^t_x(s)$ surrounds a map $g \!: E → F$ with base $β \!: E → F$ on $U ⊂ E$ in $Ω ⊂ E × F$ if, for every $x$ in $U$, every $t ∈ [0, 1]$ and every $s ∈ 𝕊^1$,

- $γ^t_x$ is based at $β(x)$
- $γ^0_x(s) = β(x)$
- $γ^1_x$ surrounds $g(x)$
- $(x,γ^t_x(s)) ∈ Ω$.

The space of such families will be denoted by $\operatorname{\mathcal{L}}(g, β, U, Ω)$.

## Depends on

- [surrounds](def-surrounds.md)

## Lean

Formalized as [`SurroundingFamily`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/SurroundingFamily).

## Sources

- [Sphere eversion blueprint: loops.tex, line 409](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/loops.tex#L409)
