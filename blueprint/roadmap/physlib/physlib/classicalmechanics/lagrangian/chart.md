---
declaration: module
origin: cited
lean: ClassicalMechanics.LagrangianSystem.chartLagrangian, ClassicalMechanics.LagrangianSystem.contDiffAt_chartLagrangian, ClassicalMechanics.LagrangianSystem.exists_contDiff_chartLagrangian_eq, ClassicalMechanics.LagrangianSystem.action_integrand_eq_chartLagrangian, ClassicalMechanics.LagrangianSystem.action_integrand_eq_of_eventuallyEq, ClassicalMechanics.LagrangianSystem.continuousAt_action_integrand
statement: formalized
proof: formalized
---

# Lagrangian systems in charts

The module `Physlib.ClassicalMechanics.Lagrangian.Chart`, [Physlib/ClassicalMechanics/Lagrangian/Chart.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/Lagrangian/Chart.lean): 6 declarations, 6 with a docstring.

> The Lagrangian in a chart, and the action integrand of a curve read in a chart.

## i. Overview

> In a chart `(q, q̇)` are coordinates on the tangent bundle, so the Lagrangian is a function
> `L (t, q, q̇)`. For a chart-read curve `c` the action integrand at `τ` is `L (τ, c τ, ċ τ)`.

## ii. Key results

> - `LagrangianSystem.chartLagrangian`: `L (t, q, q̇)` in a chart
> - `LagrangianSystem.contDiffAt_chartLagrangian`: it is smooth over the chart target
> - `LagrangianSystem.exists_contDiff_chartLagrangian_eq`: it agrees with a smooth `L` near a
>   compact set
> - `LagrangianSystem.action_integrand_eq_chartLagrangian`: the action integrand in a chart is `L`
> - `LagrangianSystem.action_integrand_eq_of_eventuallyEq`: the same for a curve chart-read near a
>   time
> - `LagrangianSystem.continuousAt_action_integrand`: the action integrand is continuous

## iv. References

> * I. Terek, Introductory Variational Calculus on Manifolds. [ref: terek\_variational\_manifolds]

## A. The Lagrangian in a chart

**`ClassicalMechanics.LagrangianSystem.chartLagrangian`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/Lagrangian/Chart.lean#L63).

> The Lagrangian in the chart `φ = extChartAt I x`, with time coordinate based at `t₀`:
> `L (t, q, q̇) = S (t +ᵥ t₀, d(φ.symm) (q, q̇))`, with generalised coordinates `q` and velocities
> `q̇`. It is meaningful only for `q` in the target of `φ`.

```lean
noncomputable def chartLagrangian (S : LagrangianSystem I M) (x : M) (t₀ : Time) :
    ℝ × E × E → ℝ
```

**`ClassicalMechanics.LagrangianSystem.contDiffAt_chartLagrangian`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/Lagrangian/Chart.lean#L69).

> The chart Lagrangian is smooth over the target of the chart.

```lean
lemma contDiffAt_chartLagrangian [I.Boundaryless] (S : LagrangianSystem I M)
    (x : M) (t₀ : Time) {p : ℝ × E × E} (hp : p.2.1 ∈ (extChartAt I x).target) :
    ContDiffAt ℝ ∞ (S.chartLagrangian x t₀) p
```

**`ClassicalMechanics.LagrangianSystem.exists_contDiff_chartLagrangian_eq`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/Lagrangian/Chart.lean#L90).

> A chart Lagrangian agrees with a globally smooth one near a compact set of positions.

```lean
lemma exists_contDiff_chartLagrangian_eq [I.Boundaryless] [FiniteDimensional ℝ E]
    (S : LagrangianSystem I M) (x : M) (t₀ : Time) {K : Set E} (hK : IsCompact K)
    (hKx : K ⊆ (extChartAt I x).target) :
    ∃ (L : ℝ × E × E → ℝ) (N : Set E), IsOpen N ∧ K ⊆ N ∧ N ⊆ (extChartAt I x).target ∧
      ContDiff ℝ ∞ L ∧ ∀ p : ℝ × E × E, p.2.1 ∈ N → L p = S.chartLagrangian x t₀ p
```

## B. The action integrand

**`ClassicalMechanics.LagrangianSystem.action_integrand_eq_chartLagrangian`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/Lagrangian/Chart.lean#L110).

> Near a chart-read curve the action integrand is the chart Lagrangian.

```lean
lemma action_integrand_eq_chartLagrangian [I.Boundaryless]
    (S : LagrangianSystem I M) (x : M) (t₀ : Time) {γ' : Time → M} {c : Time → E} {τ : ℝ}
    (hev : γ' =ᶠ[𝓝 (τ +ᵥ t₀)] (extChartAt I x).symm ∘ c)
    (hc : ContMDiffAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) ∞ c (τ +ᵥ t₀))
    (hcx : c (τ +ᵥ t₀) ∈ (extChartAt I x).target) :
    S (τ +ᵥ t₀, tangentMap 𝓘(ℝ, ℝ) I γ' ⟨τ +ᵥ t₀, (1 : ℝ)⟩) =
      S.chartLagrangian x t₀ (τ, c (τ +ᵥ t₀), deriv (fun σ : ℝ ↦ c (σ +ᵥ t₀)) τ)
```

**`ClassicalMechanics.LagrangianSystem.action_integrand_eq_of_eventuallyEq`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/Lagrangian/Chart.lean#L134).

> If `γ'` is the chart-read curve `t ↦ (extChartAt I x).symm (c (t -ᵥ t₀))` near `τ +ᵥ t₀` and
> `L` agrees with the chart Lagrangian over positions in `N ∋ c τ`, the action integrand at `τ` is
> `L (τ, c τ, deriv c τ)`. Here `c` is a function of the time relative to `t₀`.

```lean
lemma action_integrand_eq_of_eventuallyEq [I.Boundaryless]
    (S : LagrangianSystem I M) (x : M) (t₀ : Time) {γ' : Time → M} {c : ℝ → E} {τ : ℝ}
    {L : ℝ × E × E → ℝ} {N : Set E}
    (hN : N ⊆ (extChartAt I x).target)
    (hLN : ∀ p : ℝ × E × E, p.2.1 ∈ N → L p = S.chartLagrangian x t₀ p) (hc : ContDiffAt ℝ ∞ c τ)
    (hcN : c τ ∈ N)
    (hev : γ' =ᶠ[𝓝 (τ +ᵥ t₀)] (extChartAt I x).symm ∘ fun t ↦ c (t -ᵥ t₀)) :
    S (τ +ᵥ t₀, tangentMap 𝓘(ℝ, ℝ) I γ' ⟨τ +ᵥ t₀, (1 : ℝ)⟩) = L (τ, c τ, deriv c τ)
```

**`ClassicalMechanics.LagrangianSystem.continuousAt_action_integrand`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/Lagrangian/Chart.lean#L152).

> The action integrand of a smooth curve is continuous.

```lean
lemma continuousAt_action_integrand [I.Boundaryless]
    (S : LagrangianSystem I M) (t₀ : Time) {γ' : Time → M} (hγ' : ContMDiff 𝓘(ℝ, ℝ) I ∞ γ')
    (τ : ℝ) : ContinuousAt (fun τ : ℝ ↦
      S (τ +ᵥ t₀, tangentMap 𝓘(ℝ, ℝ) I γ' ⟨τ +ᵥ t₀, (1 : ℝ)⟩)) τ
```

## Depends on

- [Lagrangian systems](basic.md)

## Proof depends on

- [Cutoff functions](../../mathematics/formathlib/part-01/cutoff.md)

## Sources

- [Physlib/ClassicalMechanics/Lagrangian/Chart.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ClassicalMechanics/Lagrangian/Chart.lean)
