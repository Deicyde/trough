---
declaration: theorem
origin: cited
lean: RelMfld.Ample.satisfiesHPrincipleWith
statement: formalized
proof: formalized
---

# Gromov

For any manifolds $X$ and $Y$, any relation $\mathcal{R} ⊂ J^1(X, Y)$ that is open and ample satisfies the full $h$-principle (relative, parametric and $C^0$-dense).

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [param_for_free](../first-order-differential-relations/lem-param-for-free.md)
- [ample_parameter](lem-ample-parameter.md)
- [transfer](../first-order-differential-relations/lem-transfer.md)
- [ex_localisation](../preliminaries/lem-ex-localisation.md)
- [localisation_stability](../preliminaries/lem-localisation-stability.md)
- [smooth_updating](../preliminaries/lem-smooth-updating.md)
- [dist_updating](../preliminaries/lem-dist-updating.md)
- [inductive_htpy_construction](../../from-local-to-global/lem-inductive-htpy-construction.md)
- [ample_iff_loc](lem-ample-iff-loc.md)
- [h_principle_open_ample_loc](../../local-theory-of-convex-integration/ample-differential-relations/lem-h-principle-open-ample-loc.md)

## Proof

*Proof of Theorem Gromov.* Lemmas [param_for_free](../first-order-differential-relations/lem-param-for-free.md) and [ample_parameter](lem-ample-parameter.md) prove we can assume there are no parameters. So we start with a single formal solution $F₀$ of $\mathcal{R}$, which is holonomic near some closed subset $A ⊂ X$. We also fix a positive continuous function $δ$ on $X$ and we want to build a homotopy of formal solutions starting at $F₀$ relative to $A$ with base map staying at distance at most $δ$ from the base map of $F₀$ and ending at a holonomic solution.

We apply [Lemma ex_localisation](../preliminaries/lem-ex-localisation.md) to get some localisation data $(φ \!: \mathcal{I}_{N} × E → \operatorname{\mathcal{P}}{X}, ψ \!: ι × E' → \operatorname{\mathcal{P}}{Y}, j)$ for $\operatorname{bs} F₀ : X → Y$. [Lemma localisation_stability](../preliminaries/lem-localisation-stability.md) then provides a continuous function $ε : X → ℝ_{> 0}$ such that every function $g$ with $d(\operatorname{bs} F₀, g) < ε$ sends each $φ_i(E)$ into $ψ_{j(i)}(E')$. We denote by $τ$ the positive continuous function $\min(δ, ε)$.

We then use the inductive construction of homotopies provided by [Lemma inductive_htpy_construction](../../from-local-to-global/lem-inductive-htpy-construction.md) starting with $F₀$ and using the following local predicates. On maps $F$ from $X$ to $J¹(X, Y)$ we use the background predicate $P₀$ asserting that $F$ is a smooth section of $J¹(X, Y) → X$ that takes values in $R$, coincides with $F₀$ near $A$ and satisfies $d(\operatorname{bs} F, \operatorname{bs} F₀) < τ$. The background predicate for maps from $ℝ × X$ to $J¹(X, Y)$ is simply smoothness and the target local predicate $P₁$ on maps from $X$ to $J¹(X, Y)$ is being holonomic. We use the family of sets $U \!: i ↦ φ_i(E)$ and $K \!: i ↦ φ_i(\bar{B}_E)$.

In order to check the induction assumption from [Lemma inductive_htpy_construction](../../from-local-to-global/lem-inductive-htpy-construction.md), we fix some $i$ in $\mathcal{I}_{N}$, and some formal solution $F$ which coincides with $F₀$ near $A$ and such that $d(\operatorname{bs} F₀, \operatorname{bs} F) < τ$. We assume that $F$ is holonomic near $\bigcup_{j < i} K_j$. We need to build a smooth homotopy of formal solutions starting at $F$ which coincide with $F₀$ near $A$, coincide with $F$ outside $U_i$, have base map at distance less than $τ$ from $\operatorname{bs} F₀$ and end at a formal solution which is holonomic near $\bigcup_{j ≤ i} K_j$. In addition this homotopy must be time-independent for time near $(-∞, 0]$ and $[1, +∞)$.

Of course this homotopy comes from the local $h$-principle we proved in [Lemma h_principle_open_ample_loc](../../local-theory-of-convex-integration/ample-differential-relations/lem-h-principle-open-ample-loc.md). The first key observation allowing to apply that lemma is that $d(\operatorname{bs} F, \operatorname{bs} F₀) < τ ≤ ε$ hence $\operatorname{bs} F$ sends sends $φ_i(E)$ into $ψ_{j(i)}(E')$.

[Definition transfer_map](../first-order-differential-relations/def-transfer-map.md) then turns $F$ into a section $\mathcal{F}$ of $J¹(E, E')$. According to [Lemma transfer](../first-order-differential-relations/lem-transfer.md), $\mathcal{F}$ is a formal solution of the relation $\mathcal{R}_i$ induced by $\mathcal{R}$ in $J¹(E, E')$ via $φ_i$ and $ψ_{j(i)}$, $\mathcal{F}$ is relative to $φ_i⁻¹(A)$ and $\mathcal{F}$ is holonomic near $φ_i⁻¹(A ∪ \bigcup_{j < i} φ_j(\bar B_E))$.

The homotopy $H$ will be constructed by updating $F$ using some homotopy $\mathcal{H}$ of sections of $J¹(E, E')$ with support in the closed ball $2B_E$ and time independent for $t$ near $(-∞, 0] ∪ [1, +∞)$ (here by support we mean the closure of the set of points where $\mathcal{H}_t$ differs from $\mathcal{F}$). In order to ensure $d(\operatorname{bs} F₀, \operatorname{bs} H_t) < τ$ for all $t$, it suffices to ensure that, for each $x ∈ φ_i(2\bar{B}_E)$ and $t ∈ [0, 1]$, $d(\operatorname{bs} H_t(x), \operatorname{bs} F(x)) < τ(x) - d(\operatorname{bs} F(x), \operatorname{bs} F₀(x))$. The latter will hold as soon as, for all $e$ and $t$, $‖\operatorname{bs} \mathcal{H}_t(e) - \operatorname{bs} \mathcal{F}(e)‖ < η$ for some positive $η$ given by [Lemma dist_updating](../preliminaries/lem-dist-updating.md) (applied to $P = ℝ$, $M$ and $N$).

## Lean

Formalized as [`RelMfld.Ample.satisfiesHPrincipleWith`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/RelMfld.Ample.satisfiesHPrincipleWith).

## Sources

- [Sphere eversion blueprint: global_convex_integration.tex, line 631](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/global_convex_integration.tex#L631)
