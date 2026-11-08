---
declaration: theorem
origin: cited
lean: TauCeti.compContinuousLinearMap_fderiv_eq_of_curryLeft_eq_neg
statement: formalized
proof: formalized
---

# Moser's identity

Let `ω₀`, `ω₁` be forms that are closed along the orbit `t ↦ ψₜ x`,
`t ∈ [0, 1]`, with `ω₁ - ω₀ = dα` there. If `ψₜ` moves along a time-dependent field `Xₜ` with
`ι_{Xₜ} ((1 - t) • ω₀ + t • ω₁) = -α` near the orbit, and the derivative of `ψₜ` at `x` solves the
variational equation, then `ψ₁^* ω₁ = ψ₀^* ω₀` at `x`.

```lean
TauCeti.compContinuousLinearMap_fderiv_eq_of_curryLeft_eq_neg.{u_2, u_3} {E : Type u_2}
  {F : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  {k : ℕ} {ω₀ ω₁ : E → E [⋀^Fin (k + 1)]→L[ℝ] F} {α : E → E [⋀^Fin k]→L[ℝ] F} {ψ X : ℝ → E → E}
  {x : E} (hω₀ : ∀ t ∈ Set.Icc 0 1, DifferentiableAt ℝ ω₀ (ψ t x))
  (hω₁ : ∀ t ∈ Set.Icc 0 1, DifferentiableAt ℝ ω₁ (ψ t x))
  (hdω₀ : ∀ t ∈ Set.Icc 0 1, extDeriv ω₀ (ψ t x) = 0)
  (hdω₁ : ∀ t ∈ Set.Icc 0 1, extDeriv ω₁ (ψ t x) = 0)
  (hα : ∀ t ∈ Set.Icc 0 1, extDeriv α (ψ t x) = ω₁ (ψ t x) - ω₀ (ψ t x))
  (hX :
    ∀ t ∈ Set.Icc 0 1, (fun y => ((1 - t) • ω₀ y + t • ω₁ y).curryLeft (X t y)) =ᶠ[nhds (ψ t x)] -α)
  (hXd : ∀ t ∈ Set.Icc 0 1, DifferentiableAt ℝ (X t) (ψ t x))
  (hψ : ∀ t ∈ Set.Icc 0 1, HasDerivAt (fun s => ψ s x) (X t (ψ t x)) t)
  (hDψ :
    ∀ t ∈ Set.Icc 0 1,
      HasDerivAt (fun s => fderiv ℝ (ψ s) x) (fderiv ℝ (X t) (ψ t x) ∘SL fderiv ℝ (ψ t) x) t) :
  (ω₁ (ψ 1 x)).compContinuousLinearMap (fderiv ℝ (ψ 1) x) =
    (ω₀ (ψ 0 x)).compContinuousLinearMap (fderiv ℝ (ψ 0) x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartan's formula `L_V ω = ι_V dω + d (ι_V ω)`, where the interior product `ι_V` inserts `V` into the first slot](cartans-formula-l-v-v-d-d-v-where-the-interior-p.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.compContinuousLinearMap_fderiv_eq_of_curryLeft_eq_neg`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Moser.html#TauCeti.compContinuousLinearMap_fderiv_eq_of_curryLeft_eq_neg).

## Sources

- [Tau Ceti documentation: `TauCeti.compContinuousLinearMap_fderiv_eq_of_curryLeft_eq_neg`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Moser.html#TauCeti.compContinuousLinearMap_fderiv_eq_of_curryLeft_eq_neg)
- [Source of `TauCeti.compContinuousLinearMap_fderiv_eq_of_curryLeft_eq_neg` in TauCeti/Analysis/Calculus/Moser.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/Moser.lean#L148)
