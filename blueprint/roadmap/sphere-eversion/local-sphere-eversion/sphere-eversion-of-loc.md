---
declaration: theorem
origin: cited
lean: sphere_eversion_of_loc
statement: formalized
proof: formalized
---

# Smale 1958

There is a homotopy of immersion of $𝕊^2$ into $ℝ^3$ from the inclusion map to the antipodal map $a \!: q ↦ -q$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [loc_immersion_rel_open](lem-loc-immersion-rel-open.md)
- [loc_immersion_rel_ample](lem-loc-immersion-rel-ample.md)
- [h_principle_open_ample_loc](../local-theory-of-convex-integration/ample-differential-relations/lem-h-principle-open-ample-loc.md)
- [param_trick](../global-theory-of-open-and-ample-relations/first-order-differential-relations/lem-param-trick.md)

## Proof

We denote by $ι$ the inclusion of $𝕊^2$ into $ℝ^3$. We set $j_t = (1-t)ι + ta$. This is a homotopy from $ι$ to $a$ (but not an immersion for $t=1/2$). Using the canonical trivialization of the tangent bundle of $ℝ^3$, we can set, for $(q, v) ∈ T𝕊^2$, $G_t(q, v) = \mathrm{Rot}_{Oq}^{πt}(v)$, the rotation around axis $Oq$ with angle $πt$. The family $σ : t ↦ (j_t, G_t)$ is a homotopy of formal immersions relating $j^1ι$ to $j^1a$. Those formal solutions are holonomic when $t$ is zero or one, so we can reparametrize the family to make such it is holonomic when $t$ is close to zero or one. Then we can extend it to a homotopy of formal solutions of $\mathcal{R}$ using a suitable cut-off ensuring smoothness near the origin. The relation $\mathcal{R}$ is ample according to [Lemma loc_immersion_rel_ample](lem-loc-immersion-rel-ample.md) and then [Lemma param_trick](../global-theory-of-open-and-ample-relations/first-order-differential-relations/lem-param-trick.md) ensures its 1-parameter version $\mathcal{R}^ℝ$ is also ample. The relation $\mathcal{R}$ is open according to [Lemma loc_immersion_rel_open](lem-loc-immersion-rel-open.md) hence $\mathcal{R}^ℝ$ is also ample. So we can use [Lemma h_principle_open_ample_loc](../local-theory-of-convex-integration/ample-differential-relations/lem-h-principle-open-ample-loc.md) to deform our family of formal solutions into a holonomic one.

## Lean

Formalized as [`sphere_eversion_of_loc`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/sphere_eversion_of_loc).

## Sources

- [Sphere eversion blueprint: appendix.tex, line 100](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/appendix.tex#L100)
