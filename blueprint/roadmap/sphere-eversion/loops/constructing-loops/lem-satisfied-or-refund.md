---
declaration: lemma
origin: cited
lean: satisfied_or_refund
statement: formalized
proof: formalized
---

# satisfied_or_refund

For every set $U ⊂ E$, $\operatorname{\mathcal{L}}(g, β, U, Ω)$ is “path connected”: for every $γ_0$ and $γ_1$ in $\operatorname{\mathcal{L}}(g, β, U, Ω)$, there is a continuous map $δ \!: [0, 1] × E × [0, 1] × 𝕊^1 → F, (τ, x, t, s) ↦ δ^t_{τ, x}(s)$ which interpolates between $γ_0$ and $γ_1$ in $\operatorname{\mathcal{L}}(g, β, U, Ω)$.

## Depends on

- [family_surrounds](def-family-surrounds.md)

## Proof

Let $ρ$ be the piecewise affine map from $ℝ$ to $ℝ$ such that $ρ(τ) = 1$ if $τ ≤ 1/2$, $ρ$ is affine on $[1/2, 1]$, $ρ(τ) = 0$ if $τ ≥ 1$. We set

$$
δ_{τ, x}^t(s) =
\begin{cases}
γ_{0,x}^{ρ(τ)t}\left(\frac1{1 - τ} s\right) & \text{if $s ≤ 1 - τ$ and $τ < 1$}\\
γ_{1,x}^{ρ(1-τ)t}\left(\frac1τ \big(s - (1- τ)\big)\right) &
\text{if $s ≥ 1 - τ$ and $τ > 0$}\\
\end{cases}
$$

It is clear that if $s = 1 - τ$ then both branches agree and are equal to $β(x)$. Therefore it is easy to see that $δ$ is continuous at $(τ, x, t, s)$ except when $(τ,s)=(1,0)$ or $(τ,s)=(0,1)$.

To show the continuity for $(τ,s)=(1,0)$, let $K$ be a compact neighborhood of $x$ in $E$. Then $γ_0$ is uniformly continuous on the compact set $K × [0, 1] × 𝕊^1$, which means that $γ_{0,x'}^t$ tends uniformly to the constant function $s ↦ β(x)$ as $(x', t)$ tends to $(x, 0)$. This means that $γ_{0,x'}^{ρ(τ)t'}$ tends uniformly to the constant function $s ↦ β(x)$ as $(τ, x', t')$ tends to $(1, x, t)$. This means that $δ$ is continuous at $(τ,s)=(1,0)$ (it is clear that the other branch also tends to $β(x)$). The continuity at $(τ,s)=(0,1)$ is entirely analogous.

The beautiful observation motivating the above formula is why each $δ_{τ, x}^1$ surrounds $g(x)$. The key is that the image of $δ_{τ, x}^1$ contains the image of $γ_{0,x}^1$ when $τ ≤ 1/2$, and contains the image of $γ_{1,x}^1$ when $τ ≥ 1/2$. Hence $δ_{τ, x}^1$ always surrounds $g(x)$.

## Lean

Formalized as [`satisfied_or_refund`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/satisfied_or_refund).

## Sources

- [Sphere eversion blueprint: loops.tex, line 467](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/loops.tex#L467)
