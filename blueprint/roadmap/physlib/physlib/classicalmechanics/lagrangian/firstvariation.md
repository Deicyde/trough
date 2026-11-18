---
declaration: module
origin: cited
lean: ClassicalMechanics.LagrangianSystem.fderiv_action_integrand_apply, ClassicalMechanics.LagrangianSystem.contDiff_action_integrand, ClassicalMechanics.LagrangianSystem.hasDerivAt_integral_variation, ClassicalMechanics.LagrangianSystem.action_variation_eq_integral, ClassicalMechanics.LagrangianSystem.hasDerivAt_action_variation
statement: formalized
proof: formalized
---

# First variation of the action

The module `Physlib.ClassicalMechanics.Lagrangian.FirstVariation`, [Physlib/ClassicalMechanics/Lagrangian/FirstVariation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/FirstVariation.lean): 5 declarations, 5 with a docstring.

> The first variation of `∫ L (τ, H, ∂τ H) dτ`.

## i. Overview

> `H (s, τ)` is a smooth family of curves around `H (0, ·)`.
> Along a smooth family fixing the endpoints, the derivative of the action is the integral of the
> Euler-Lagrange covector `∂L/∂q - dₜ(∂L/∂q̇)` against the variation field.

## ii. Key results

> - `LagrangianSystem.contDiff_action_integrand`: smoothness of the action integrand
> - `LagrangianSystem.fderiv_action_integrand_apply`: first variation of the integrand, the
>   Euler-Lagrange term plus a total `τ`-derivative
> - `LagrangianSystem.hasDerivAt_integral_variation`: first variation of the action
> - `LagrangianSystem.action_variation_eq_integral`: the action along a variation in coordinates
> - `LagrangianSystem.hasDerivAt_action_variation`: first variation of the action along a variation

## iv. References

> * I. Terek, Introductory Variational Calculus on Manifolds. [ref: terek\_variational\_manifolds]
> * L. D. Landau and E. M. Lifshitz, Mechanics. [ref: landau\_mechanics]

## A. First variation

**`ClassicalMechanics.LagrangianSystem.fderiv_action_integrand_apply`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/FirstVariation.lean#L60).

> The `s`-derivative of the integrand of the action splits into the Euler-Lagrange term and
> a total `τ`-derivative.

```lean
lemma fderiv_action_integrand_apply (S : LagrangianSystem 𝓘(ℝ, E) ⟨E⟩) (t₀ : Time)
    (hH : ContDiff ℝ ∞ H) (τ : ℝ) :
    fderiv ℝ (fun p : ℝ × ℝ ↦ S.coord t₀ (p.2, H p, fderiv ℝ H p (0, 1))) (0, τ) (1, 0) =
      eulerLagrange S t₀ (fun σ ↦ H (0, σ)) τ (fderiv ℝ H (0, τ) (1, 0)) +
        (deriv (canonicalMomentum S t₀ fun σ ↦ H (0, σ)) τ
            (fderiv ℝ H (0, τ) (1, 0)) +
          canonicalMomentum S t₀ (fun σ ↦ H (0, σ)) τ
            (deriv (fun σ ↦ fderiv ℝ H (0, σ) (1, 0)) τ))
```

**`ClassicalMechanics.LagrangianSystem.contDiff_action_integrand`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/FirstVariation.lean#L83).

> The integrand `L(τ, H, ∂τ H)` of the action is smooth.

```lean
lemma contDiff_action_integrand (S : LagrangianSystem 𝓘(ℝ, E) ⟨E⟩) (t₀ : Time)
    (hH : ContDiff ℝ ∞ H) :
    ContDiff ℝ ∞ fun p : ℝ × ℝ ↦ S.coord t₀ (p.2, H p, fderiv ℝ H p (0, 1))
```

**`ClassicalMechanics.LagrangianSystem.hasDerivAt_integral_variation`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/FirstVariation.lean#L90).

> First variation of `∫ L(τ, H, ∂τ H) dτ` along a variation fixing the endpoints.

```lean
lemma hasDerivAt_integral_variation (S : LagrangianSystem 𝓘(ℝ, E) ⟨E⟩) (t₀ : Time)
    (hH : ContDiff ℝ ∞ H)
    (T : ℝ) (h0 : ∀ s, H (s, 0) = H (0, 0)) (hT : ∀ s, H (s, T) = H (0, T)) :
    HasDerivAt
      (fun s ↦ ∫ τ in (0 : ℝ)..T, S.coord t₀ (τ, H (s, τ), fderiv ℝ H (s, τ) (0, 1)))
      (∫ τ in (0 : ℝ)..T,
        eulerLagrange S t₀ (fun σ ↦ H (0, σ)) τ (fderiv ℝ H (0, τ) (1, 0))) 0
```

## B. The action along a variation

**`ClassicalMechanics.LagrangianSystem.action_variation_eq_integral`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/FirstVariation.lean#L132).

> The action of `t ↦ h (s, t)` is the integral over `[0, t₁ -ᵥ t₀]` of
> `S.coord t₀ (τ, q τ, q' τ)`, where `q τ = h (s, τ +ᵥ t₀)` and `q' = deriv q`.

```lean
lemma action_variation_eq_integral (S : LagrangianSystem 𝓘(ℝ, E) ⟨E⟩) {γ : Time → E}
    {t₀ t₁ : Time} (h : Variation (M := ⟨E⟩) 𝓘(ℝ, E) γ t₀ t₁) (ht : 0 ≤ t₁ -ᵥ t₀) (s : ℝ) :
    S.action (fun t ↦ h.toFun (s, t)) t₀ t₁ =
      ∫ τ in (0 : ℝ)..(t₁ -ᵥ t₀), S.coord t₀ (τ, h.toFun (s, τ +ᵥ t₀),
        fderiv ℝ (fun p : ℝ × ℝ ↦ h.toFun (p.1, p.2 +ᵥ t₀)) (s, τ) (0, 1))
```

**`ClassicalMechanics.LagrangianSystem.hasDerivAt_action_variation`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/FirstVariation.lean#L146).

> The `s`-derivative at `0` of the action of `t ↦ h (s, t)` is the integral over
> `[0, t₁ -ᵥ t₀]` of `eulerLagrange S t₀ q τ` applied to the derivative of `s ↦ h (s, τ +ᵥ t₀)` at
> `0`, where `q σ = h (0, σ +ᵥ t₀)`.

```lean
lemma hasDerivAt_action_variation (S : LagrangianSystem 𝓘(ℝ, E) ⟨E⟩) {γ : Time → E}
    {t₀ t₁ : Time} (h : Variation (M := ⟨E⟩) 𝓘(ℝ, E) γ t₀ t₁) (ht : 0 ≤ t₁ -ᵥ t₀) :
    HasDerivAt (fun s ↦ S.action (fun t ↦ h.toFun (s, t)) t₀ t₁)
      (∫ τ in (0 : ℝ)..(t₁ -ᵥ t₀),
        eulerLagrange S t₀ (fun σ ↦ h.toFun (0, σ +ᵥ t₀)) τ
          (fderiv ℝ (fun p : ℝ × ℝ ↦ h.toFun (p.1, p.2 +ᵥ t₀)) (0, τ) (1, 0))) 0
```

## Depends on

- [Variations of curves](../configurationspace/variation.md)
- [A. Euler–Lagrange equations](../eulerlagrange.md)

## Proof depends on

- [Parametric Integration](../../mathematics/calculus/parametricintegration.md)
- [Partial derivatives on products](../../mathematics/calculus/partialderivatives.md)

## Sources

- [Physlib/ClassicalMechanics/Lagrangian/FirstVariation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Lagrangian/FirstVariation.lean)
