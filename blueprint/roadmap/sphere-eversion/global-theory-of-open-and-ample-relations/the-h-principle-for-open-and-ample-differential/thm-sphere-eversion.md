---
declaration: theorem
origin: cited
lean: sphere_eversion
statement: formalized
proof: formalized
---

# Smale 1958

There is a homotopy of immersions of $𝕊^2$ into $ℝ^3$ from the inclusion map to the antipodal map $a : q ↦ -q$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Gromov](thm-open-ample.md)
- [open_ample_immersion](lem-open-ample-immersion.md)

## Proof

We denote by $ι$ the inclusion of $𝕊^2$ into $ℝ^3$. We set $j_t = (1-t)ι + ta$. This is a homotopy from $ι$ to $a$ (but not an immersion for $t=1/2$). Using the canonical trivialization of the tangent bundle of $ℝ^3$, we can set, for $(q, v) ∈ T𝕊^2$, $G_t(q, v) = \mathrm{Rot}_{Oq}^{πt}(v)$, the rotation around axis $Oq$ with angle $πt$. The family $σ : t ↦ (j_t, G_t)$ is a homotopy of formal immersions relating $j^1ι$ to $j^1a$. It is homotopic by reparametrization to a homotopy of formal immersions relating $j^1ι$ to $j^1a$ which are holonomic for $t$ near the $0$ and $1$.

The above theorem ensures this family is homotopic, relative to $t = 0$ and $t = 1$, to a family of holonomic formal immersions, ie a family $t ↦ j^1f_t$ with $f_0 = ι$, $f_1 = a$, and each $f_t$ is an immersion.

## Lean

Formalized as [`sphere_eversion`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/sphere_eversion).

## Sources

- [Sphere eversion blueprint: global_convex_integration.tex, line 737](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/global_convex_integration.tex#L737)
