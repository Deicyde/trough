---
declaration: definition
origin: cited
lean: OpenSmoothEmbedding.update
statement: formalized
---

# update

Given smooth open embeddings $φ : X → M$ and $ψ : Y → N$, the update of a map $f : M → N$, using a map $g : X → Y$ is the map from $M$ to $N$ sending $m$ to $ψ ∘ g ∘ φ⁻¹(m)$ if $m ∈ φ(X)$ and $f(m)$ otherwise.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`OpenSmoothEmbedding.update`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/OpenSmoothEmbedding.update).

## Sources

- [Sphere eversion blueprint: global_convex_integration.tex, line 22](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/global_convex_integration.tex#L22)
