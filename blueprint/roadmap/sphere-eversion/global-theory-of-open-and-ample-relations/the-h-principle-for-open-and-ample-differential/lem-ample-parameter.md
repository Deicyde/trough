---
declaration: lemma
origin: cited
lean: RelMfld.Ample.relativize
statement: formalized
proof: formalized
---

# ample_parameter

If $\mathcal{R}$ is ample then, for any parameter space $P$, $\mathcal{R}^P$ is also ample.

## Depends on

- [ample_relation](def-ample-relation.md)

## Proof

We fix $σ = (x, y, ψ)$ in $\mathcal{R}^P$. For any $λ = (λ_X, λ_P) ∈ T^*_xX × T^*_pP$ and $v = (v_X, v_P) ∈ T_xX × T_pP$ such that $λ(v) = 1$, we need to prove that $\operatorname{Conv}\mathcal{R}^P_{σ, λ, v} = T_yY$. Unfolding the definitions gives:

$$
\mathcal{R}^P_{σ, λ, v} = \operatorname{Conn}_{φ(v)}\left\{w ∈ T_yY \;;\;
\big(x,\; y,\; ψ ∘ ι_{x, p} + (w - ψ(v))⊗λ_X\big) ∈ \mathcal{R}\right\}.
$$

A degenerate but easy case is when $λ_X = 0$. Then the condition on $w$ becomes $ψ ∘ ι_{x, p} ∈ \mathcal{R}$, which is true by definition of $\mathcal{R}^P$, so $\mathcal{R}^P_{σ, λ, v} = T_yY$.

We now assume $λ_X$ is not zero and choose $u ∈ T_xX$ such that $λ_X(u) = 1$. We then have $\mathcal{R}^P_{σ, λ, v} = \mathcal{R}_{Ψσ, λ_X, u} + ψ(v) - ψ∘ι_{x, p}(u)$. Because $\mathcal{R}$ is ample and taking convex hull commutes with translation, we get that $\operatorname{Conv}\mathcal{R}^P_{σ, λ, v} = T_yY$.

## Lean

Formalized as [`RelMfld.Ample.relativize`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/RelMfld.Ample.relativize).

## Sources

- [Sphere eversion blueprint: global_convex_integration.tex, line 643](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/global_convex_integration.tex#L643)
