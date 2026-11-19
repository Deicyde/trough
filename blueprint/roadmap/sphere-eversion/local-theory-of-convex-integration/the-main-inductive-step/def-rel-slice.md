---
declaration: definition
origin: cited
lean: RelMfld.slice
statement: formalized
---

# rel_slice

For every $σ = (x, y, φ)$, the slice of $\mathcal{R}$ at $σ$ with respect to $(π, v)$ is:

$$
\mathcal{R}(σ, π, v) = \{w ∈ F \;|\; (x, y, φ + (w - φ(v)) ⊗ π) ∈ \mathcal{R}\}.
$$

## Depends on

- [rel_loc](def-rel-loc.md)

## Lean

Formalized as [`RelMfld.slice`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/RelMfld.slice).

## Sources

- [Sphere eversion blueprint: local_convex_integration.tex, line 148](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/local_convex_integration.tex#L148)
