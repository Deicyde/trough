---
declaration: definition
origin: cited
lean: LocalisationData
statement: formalized
---

# localisation_data

Let $f : M → N$ be a continuous map between manifolds. A localisation data for $f$ is a tuple $(E, F, N, ι, φ, ψ, j)$ where $E$ and $F$ are normed vector spaces, $N$ is a natural number, $ι$ is a set, $φ : \mathcal{I}_{N} × E → M$ and $ψ : ι × F → N$ are families of smooth open embeddings, and $j : \mathcal{I}_{N} → ι$ such that:

- $⋃_i φ_i(B_E) = M$ where $B_E$ is the open unit ball in $E$,
- $⋃_i ψ_i(B_F) = N$ where $B_F$ is the open unit ball in $F$,
- $∀ i, f(φ_i(E)) ⊂ ψ_{j(i)}(B_F)$ where $B_F$ is the open unit ball in $F$,
- $i \mapsto ψ_i(F)$ is locally finite.

Such a tuple will be denoted by $(φ, ψ, j)$ for brevity.

## Depends on

- [index_type](../../from-local-to-global/def-index-type.md)

## Lean

Formalized as [`LocalisationData`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/LocalisationData).

## Sources

- [Sphere eversion blueprint: global_convex_integration.tex, line 163](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/global_convex_integration.tex#L163)
