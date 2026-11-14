---
declaration: proposition
origin: cited
lean: fderiv_corrugated_map, corrugation.c0_small_on, remainder_c0_small_on, corrugation.support
statement: formalized
proof: formalized
---

# Theillière 2018

Let $f$ be a $\mathcal{C}^1$ function from $E$ to $F$. Let $(π, v)$ be a dual pair on $E$. Let $γ \!: E × 𝕊^1 → F$ be a $\mathcal{C}^1$ family of loops such that $\overline{γ_x} = Df(x)v$ for all $x$.

For any compact set $K ⊂ E$ and any positive $ε$, the function $f'$ obtained by corrugation of $f$ in direction $(π, v)$ using $γ$ with large enough oscillation number $N$ satisfies:

1. $∀ x ∈ K, ‖f'(x) - f(x)‖ ≤ ε$
2. $∀ x ∈ K, ‖(Df'(x) - Df(x))_{|\ker π}‖ ≤ ε$.
3. $∀ x ∈ K, ‖Df'(x)v - γ(x, Nπ(x))‖ ≤ ε$

In addition, all the differences estimated above vanish if $x$ is outside the support of $γ$.

## Depends on

- [Theillière 2018](def-corrugation.md)

## Proof

We set $Γ_x(t) = ∫_0^t \left(γ_x(s) - \overline{γ}_x\right)ds$, so that $f'(x) = f(x) + Γ_x(Nπ(x))/N$. Because each $Γ_x$ is $1$-periodic, and everything has compact support in $E$, all derivatives of $Γ$ are uniformly bounded. Item Theillière 2018 in the statement is then obvious. Item Theillière 2018 also follows since $∂_if'(x) = ∂_if(x) + ∂_iΓ(x, Nπ(x))/N$. In order to prove Item Theillière 2018, we compute:

$$
\begin{aligned}
Df'(x)v &= Df(x)v + \frac1N ∂_jΓ(x, Nπ(x)) + \frac NN ∂_tΓ(x, Nπ(x))\\
&= Df(x)v + O\left(\frac1N\right) + γ(x, Nπ(x)) - Df(x)v\\
&= γ(x, Nπ(x)) + O\left(\frac1N\right).
\end{aligned}
$$

Outside the support of $γ$, $Γ_x$ and its derivative with respect to $x$ vanish identically (for the derivative computation, it is important that the support of $γ$ is the *closure* of the set of $x$ where $γ_x$ is not constant).

## Lean

Formalized as [`fderiv_corrugated_map`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/fderiv_corrugated_map), [`corrugation.c0_small_on`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/corrugation.c0_small_on), [`remainder_c0_small_on`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/remainder_c0_small_on), [`corrugation.support`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/corrugation.support).

## Sources

- [Sphere eversion blueprint: local_convex_integration.tex, line 55](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/local_convex_integration.tex#L55)
