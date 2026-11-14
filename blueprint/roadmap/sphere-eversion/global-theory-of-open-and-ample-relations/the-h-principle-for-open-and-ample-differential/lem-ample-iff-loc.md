---
declaration: lemma
origin: cited
lean: RelMfld.Ample.localize
statement: formalized
proof: formalized
---

# ample_iff_loc

Given manifolds $W$, $X$, $Y$ and $Z$ and smooth open embeddings $g : Z → Y$ and $h : W → X$, the relation induced (in the sense of [Definition transfer_map](../first-order-differential-relations/def-transfer-map.md)) in $J^1(W, Z)$ by an ample relation in $J^1(X, Y)$ is ample.

## Depends on

- [ample_relation](def-ample-relation.md)
- [transfer_map](../first-order-differential-relations/def-transfer-map.md)

## Proof

By definition, the relation induced by $\mathcal{R}$ is $ψ_{g, h}⁻¹\mathcal{R}$ where $ψ_{g, h}(w, z, φ) = (h(w), g(z), T_zg ∘ φ ∘ (T_wh)⁻¹)$. Fix $σ =(w, z, φ) ∈ ψ_{g, h}⁻¹\mathcal{R}$ and a dual pair $(λ, v)$ on $T_wW$. We set $G = T_z g$ and $H = T_w h$. Both those maps are linear isomorphisms. We compute the slice corresponding to $(σ, λ, v)$:

$$
\begin{aligned}
ψ_{g, h}⁻¹\mathcal{R}(σ, λ, v)
&= \operatorname{Conn}_{φv}\left\{u ∈ T_wW \;\left|\; (w, z, φ + (u - φv)⊗λ) ∈ ψ_{g, h}⁻¹\mathcal{R} \right.\right\}\\
&= \operatorname{Conn}_{φv}\left\{u ∈ T_wW \;\left|\; (h(w), g(z), G ∘ (φ + (u - φv)⊗λ)∘ H⁻¹) ∈ \mathcal{R} \right.\right\}\\
&= G⁻¹\mathcal{R}(ψ_{g, h}σ, λ ∘ H⁻¹, Hv).
\end{aligned}
$$

Hence the slice $ψ_{g, h}⁻¹\mathcal{R}(σ, λ, v)$ is the image of a slice of $\mathcal{R}$ under a linear isomorphism, hence ample.

## Lean

Formalized as [`RelMfld.Ample.localize`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/RelMfld.Ample.localize).

## Sources

- [Sphere eversion blueprint: global_convex_integration.tex, line 578](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/global_convex_integration.tex#L578)
