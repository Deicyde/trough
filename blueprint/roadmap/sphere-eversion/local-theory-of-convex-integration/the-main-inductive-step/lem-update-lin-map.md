---
declaration: lemma
origin: cited
lean: DualPair.update_ker_pi, DualPair.update_v, mem_slice
statement: formalized
proof: formalized
---

# update_lin_map

The linear map $φ + (w - φ(v)) ⊗ π)$ coincides with $φ$ on $\ker π$ and sends $v$ to $w$. If $\sigma$ belongs to $\mathcal{R}$ then $φ(v)$ belongs to $\{w ∈ F, (x, y, φ + (w - φ(v)) ⊗ π) ∈ \mathcal{R}\}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

These are direct checks.

## Lean

Formalized as [`DualPair.update_ker_pi`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/DualPair.update_ker_pi), [`DualPair.update_v`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/DualPair.update_v), [`mem_slice`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/mem_slice).

## Sources

- [Sphere eversion blueprint: local_convex_integration.tex, line 160](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/local_convex_integration.tex#L160)
