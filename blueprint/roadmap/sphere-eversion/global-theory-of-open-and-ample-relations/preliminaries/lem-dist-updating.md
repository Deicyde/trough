---
declaration: lemma
origin: cited
lean: OpenSmoothEmbedding.dist_update
statement: formalized
proof: formalized
---

# dist_updating

Let $φ : X → M$ and $ψ : Y → N$ be smooth open embeddings. Let $K_X$ and $K_P$ be compact sets in $X$ and $P$. Let $f : P × M → N$ be a continuous family of maps such that, for each $p$, $f_p(φ(X)) ⊂ ψ(Y)$. For every continuous function $ε : M → ℝ_{> 0}$, there is some positive number $η$ such that, for every map $g : P × X → Y$ and every $(p, p', x)$ in $K_P × K_P × K_X$, $d(g_{p'}(x), ψ⁻¹∘f_p∘φ(x)) < η$ implies $d(f'_{p'}(φ(x)), f_p(φ(x))) < ε(φ(x))$ where $f'$ is obtained by updating $f$ using $g$.

## Depends on

- [update](def-update.md)

## Proof

Let $ε$ be a positive continuous function on $M$. Since $K_X$ is compact, we get a positive number $ε₀$ such that $ε(m) ≥ ε₀$ for each $m$ in $K_X$. We denote by $K₁$ the closed $1$-thickening of the image of $K_P × K_X$ under $(p, x) ↦ ψ⁻¹∘f_p∘φ(x)$. This is a compact set so $ψ$ is uniformly continuous on $K₁$ and we get a positive $τ$ such that for all $x$ and $y$ in $K₁$, $d(x, y) < τ ⇒ d(ψ(x), ψ(y)) < ε₀$.

We now prove that $η = \min(τ, 1)$ is suitable. Fix $(p, p', x)$ in $K_P × K_P × K_X$ such that $d(g_{p'}(x), ψ⁻¹∘f_p∘φ(x)) < η$. In particular $d(g_{p'}(x), ψ⁻¹∘f_p∘φ(x)) < 1$ hence $g_{p'}(x)$ is in $K₁$. Since $ψ⁻¹∘f_p∘φ(x)$ is also in $K₁$ and $d(g_{p'}(x), ψ⁻¹∘f∘φ(x)) < τ$, we get $d(ψ∘ g_{p'}(x), ψ ∘ ψ⁻¹∘f_p∘φ(x)) < ε₀$. This precisely means that $d(f'_{p'}(φ(x)), f_p(φ(x)) < ε₀$. Since $(p, p', x)$ is in $K_P × K_P × K_X$, this is less than $ε(m)$.

## Lean

Formalized as [`OpenSmoothEmbedding.dist_update`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/OpenSmoothEmbedding.dist_update).

## Sources

- [Sphere eversion blueprint: global_convex_integration.tex, line 52](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/global_convex_integration.tex#L52)
