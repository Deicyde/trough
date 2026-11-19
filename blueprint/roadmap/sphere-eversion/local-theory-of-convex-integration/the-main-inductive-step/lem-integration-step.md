---
declaration: lemma
origin: cited
lean: StepLandscape.improveStep_rel_t_eq_0, StepLandscape.improveStep_rel_C, StepLandscape.improveStep_rel_compl_K₁, StepLandscape.improveStep_c0_close, StepLandscape.improveStep_part_hol
statement: formalized
proof: formalized
---

# integration_step

Let $\mathcal{F}$ be a formal solution of $\mathcal{R}$. Let $K_1 ⊂ E$ be a compact subset, and let $K_0$ be a compact subset of the interior of $K_1$. Let $C$ be a closed subset of $E$. Let $E'$ be a linear subspace of $E$ contained in $\ker π$. Let $ε$ be a positive real number.

Assume $\mathcal{R}$ is open. Assume that $\mathcal{F}$ is $E'$–holonomic near $K_0$, $(π, v)$–short, and holonomic near $C$. Then there is a homotopy $\mathcal{F}_t$ such that:

1. $\mathcal{F}_0 = \mathcal{F}$ ;
2. $\mathcal{F}_t$ is a formal solution of $\mathcal{R}$ for all $t$ ;
3. $\mathcal{F}_t(x) = \mathcal{F}(x)$ for all $t$ when $x$ is near $C$ or outside $K_1$ ;
4. $d(\operatorname{bs}\mathcal{F}_t(x), \operatorname{bs} \mathcal{F}(x)) ≤ ε$ for all $t$ and all $x$ ;
5. $\mathcal{F}_1$ is $E' ⊕ ℝv$–holonomic near $K_0$.

## Depends on

- [short_formal_sol](def-short-formal-sol.md)
- [hol_partial](def-hol-partial.md)
- [htpy_jet_sec_loc](def-htpy-jet-sec-loc.md)

## Proof depends on

- [∃\_loops](../../loops/introduction/prop-loops.md)
- [Theillière 2018](../key-construction/cp-v.md)
- [update_lin_map](lem-update-lin-map.md)

## Proof

We denote the components of $\mathcal{F}$ by $f$ and $φ$. Since $\mathcal{F}$ is short, [Proposition ∃\_loops](../../loops/introduction/prop-loops.md) applied to $g \!: x ↦ Df(x)v$, $β \!: x ↦ φ(x)v$, $Ω_x = \mathcal{R}(\mathcal{F}(x), π, v)$, and $K = C ∩ K_1$ gives us a smooth family of loops $γ \!: E × [0, 1] × 𝕊^1 → F$ such that, for all $x$:

- $∀ t\, s,\; γ^t_x(s) ∈ \mathcal{R}(\mathcal{F}(x), π, v)$
- $∀ s,\; γ^0_x(s) = φ(x)v$
- $\bar γ^1_x = Df(x)v$
- if $x$ is near $C$, $∀t\, s,\; γ^t_x(s) = φ(x)v$

Let $ρ: E → ℝ$ be a smooth cut-off function which equals one on a neighborhood of $K_0$ and whose support is contained in $K_1$.

Let $N$ be a positive real number. Let $\bar f$ be the corrugated map constructed from $f$, $γ^1$ and $N$. [Theillière 2018](../key-construction/cp-v.md) ensures that, for all $x$,

$$
D\bar f(x) = Df(x) + \left[γ^1_x(Nπ(x)) - Df(x)v\right] ⊗ π +
R_x
$$

for some remainder term $R$ which is $ε$-small and vanishes whenever $γ_x$ is constant, hence vanishes near $C$.

We set $\mathcal{F}_t(x) = \big(f_t(x), φ_t(x)\big)$ where:

$$
f_t(x) = f(x) + \frac{tρ(x)}N \int_0^{Nπ(x)}
\left[γ^t_x(s) - Df(x)v\right]\, ds
$$

and

$$
φ_t(x) = φ(x) + \left[γ^{tρ(x)}_x(Nπ(x)) - φ(x)v\right] ⊗ π +
\frac{tρ(x)}N B_x.
$$

We now prove that $\mathcal{F}_t$ has the announced properties, starting with he obvious ones. The fact that $\mathcal{F}_0 = \mathcal{F}$ is obvious since $γ^0_x(s) = φ(x)v$ for all $s$.

When $x$ is near $C$, $Df(x) = φ(x)$ since $\mathcal{F}$ is holonomic near $C$. In addition, $γ^t_x(s) = φ(x)v$ for all $s$ and $t$, hence $B_x$ vanishes. Hence $\mathcal{F}_t(x) = \mathcal{F}(x)$ for all $t$ when $x$ is near $C$.

Outside of $K_1$, $ρ$ vanishes. Hence $f_t(x) = f(x)$ for all $t$, and $γ^{tρ(x)}_x(s) = φ(x)v$ for all $s$ and $t$, and $φ_t(x) = φ(x)$.

The distance between $f(x)$ and $f_t(x)$ is zero outside of $K_1$ and $ε$-small everywhere.

We now turn to the interesting parts. The first one is that each $\mathcal{F}_t$ is a formal solution of $\mathcal{R}$. We already now that $\mathcal{F}_t$ coincides with $\mathcal{F}$, which is a formal solution, outside of the compact set $K_1$. We set

$$
\mathcal{F}'_t(x) = \left(f(x),
φ(x) + \left[γ^{tρ(x)}_x(Nπ(x)) - φ(x)v\right] ⊗ π\right).
$$

Since $\mathcal{R}$ is open, and $K_1 × [0, 1]$ is compact and $\mathcal{F}_t$ is within $O\left(1/N\right)$ of $\mathcal{F}'_t$, it suffices to prove that $\mathcal{F}'_t$ is a formal solution for all $t$. This is guaranteed by the definition of the slice $\mathcal{R}(\mathcal{F}(x), π, v)$ to which $γ^{tρ(x)}_x(Nπ(x))$ belongs.

Finally, let's prove that $\mathcal{F}_1$ is $E' ⊕ ℝv$–holonomic near $K_0$. Since $ρ = 1$ near $K_0$, we have, for $x$ near $K_0$,

$$
Df_1(x) = Df(x) + \left[γ^1_x(Nπ(x)) - Df(x)v\right] ⊗ π +
\frac1N B_x,
$$

and

$$
φ_1(x) = φ(x) + \left[γ^1_x(Nπ(x)) - φ(x)v\right] ⊗ π +
\frac{1}N B_x.
$$

Let $p$ be the projection of $E$ onto $\ker π$ along $v$, so that $\operatorname{Id}_E = p + v ⊗ π$. We can rewrite the above formulas as

$$
Df_1(x) = Df(x) ∘ p + γ^1_x(Nπ(x)) ⊗ π + \frac1N B_x,
$$

and

$$
φ_1(x) = φ(x) ∘ p + γ^1_x(Nπ(x)) ⊗ π + \frac{1}N B_x.
$$

So we see the difference is $Df(x) ∘ p - φ(x) ∘ p$ which vanishes on $E'$ since $\mathcal{F}$ is $E'$–holonomic near $K_0$, and vanishes on $v$ since $p(v) = 0$.

## Lean

Formalized as [`StepLandscape.improveStep_rel_t_eq_0`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/StepLandscape.improveStep_rel_t_eq_0), [`StepLandscape.improveStep_rel_C`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/StepLandscape.improveStep_rel_C), [`StepLandscape.improveStep_rel_compl_K₁`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/StepLandscape.improveStep_rel_compl_K₁), [`StepLandscape.improveStep_c0_close`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/StepLandscape.improveStep_c0_close), [`StepLandscape.improveStep_part_hol`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/StepLandscape.improveStep_part_hol).

## Sources

- [Sphere eversion blueprint: local_convex_integration.tex, line 188](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/local_convex_integration.tex#L188)
