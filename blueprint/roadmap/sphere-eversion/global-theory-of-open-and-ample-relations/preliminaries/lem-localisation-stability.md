---
declaration: lemma
origin: cited
lean: localisation_stability
statement: formalized
proof: formalized
---

# localisation_stability

Let $f : M → N$ be a continuous map between manifolds, and let $(φ, ψ, i)$ be some localisation data for $f$. There exists a continuous positive function $ε : M → ℝ_{>0}$ such that:

$$
∀ g : M → N, \big[∀ m,\; d(f(m), g(m)) < ε(m)\big] ⇒ ∀ i,\; g(φ_i(E)) ⊂ ψ_{j(i)}(F).
$$

## Depends on

- [localisation_data](def-localisation-data.md)

## Proof depends on

- [stability_cover](lem-stability-cover.md)

## Proof

The preceding lemma applied to the family of open sets $ψ_j(F)$ and the family of compact sets $ψ_j(\overline{B_F})$ give a positive continuous function $δ : N → ℝ$ such that $ε = δ ∘ f$ is suitable. Indeed, assume $g : M → N$ satisfies $d(g, f) < ε$ and fix some $i$ and some $m ∈ φ_i(E)$. We know $f(m) ∈ ψ_{j(i)}(\overline{B_F})$ and our assumption on $g$ gives $d(g(m), f(m)) < δ(f(m))$. So the property of $δ$ ensures $g(m) ∈ ψ_{j(i)}(F)$.

## Lean

Formalized as [`localisation_stability`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/localisation_stability).

## Sources

- [Sphere eversion blueprint: global_convex_integration.tex, line 237](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/global_convex_integration.tex#L237)
