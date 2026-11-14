---
declaration: lemma
origin: cited
lean: OpenSmoothEmbedding.contMDiff_update
statement: formalized
proof: formalized
---

# smooth_updating

Let $φ : P × X → M$ and $ψ : P × Y → N$ be families of smooth open embeddings. Let $K$ be a set in $X$ whose image in $M$ is closed. Let $f : P × M → N$ and $g : P × X → Y$ be smooth families of maps. If for each $p$ and for every $x$ not in $K$, $f_p(φ(x)) = ψ(g_p(x))$ then the family of maps $f_p$ updated using $g_p$ is smooth from $P × M$ to $N$.

## Depends on

- [update](def-update.md)

## Proof

Note that $P × M = (P × φ(X)) ∪ (P × φ(K)^c)$. Both those sets are open and the updated maps coincide with $(p, m) ↦ ψ ∘ g_p ∘ φ⁻¹(m)$ on the first one and $f$ on the second one.

## Lean

Formalized as [`OpenSmoothEmbedding.contMDiff_update`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/OpenSmoothEmbedding.contMDiff_update).

## Sources

- [Sphere eversion blueprint: global_convex_integration.tex, line 32](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/global_convex_integration.tex#L32)
