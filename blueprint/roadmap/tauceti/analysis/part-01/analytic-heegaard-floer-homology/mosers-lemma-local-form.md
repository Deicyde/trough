---
declaration: theorem
origin: cited
lean: TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_of_extDeriv_eq
statement: formalized
proof: formalized
---

# Moser's lemma, local form

Let `ω₀`, `ω₁` be closed `C^r` two-forms (`r ≥ 1`) on an open
subset `W` of a finite-dimensional real normed space, with `ω₁ - ω₀ = dα` on `W` for a `C^r`
one-form `α` vanishing at `x₀ ∈ W`. If `ω₀` and `ω₁` agree at `x₀` and are nondegenerate there,
then some `C^r` diffeomorphism `ψ` of the space pulls `ω₁` back to `ω₀` on a neighbourhood of `x₀`.
Moreover `ψ` fixes, near `x₀`, every point at which `α` vanishes; in particular `ψ x₀ = x₀`.

```lean
TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_of_extDeriv_eq.{u_1}
  {V : Type u_1} [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V]
  {ω₀ ω₁ : V → V [⋀^Fin 2]→L[ℝ] ℝ} {α : V → V [⋀^Fin 1]→L[ℝ] ℝ} {W : Set V} {x₀ : V} {r : ℕ∞}
  (hr : 1 ≤ r) (hW : IsOpen W) (hx₀ : x₀ ∈ W) (hω₀ : ContDiffOn ℝ (↑r) ω₀ W)
  (hω₁ : ContDiffOn ℝ (↑r) ω₁ W) (hα : ContDiffOn ℝ (↑r) α W) (hdω₀ : ∀ x ∈ W, extDeriv ω₀ x = 0)
  (hdω₁ : ∀ x ∈ W, extDeriv ω₁ x = 0) (hdα : ∀ x ∈ W, extDeriv α x = ω₁ x - ω₀ x) (hα₀ : α x₀ = 0)
  (heq : ω₁ x₀ = ω₀ x₀) (hnd : ∀ (v : V), (∀ (w : V), (ω₀ x₀) ![v, w] = 0) → v = 0) :
  ∃ ψ,
    (∀ᶠ (x : V) in nhds x₀, α x = 0 → ψ x = x) ∧
      ∀ᶠ (x : V) in nhds x₀, (ω₁ (ψ x)).compContinuousLinearMap (fderiv ℝ (⇑ψ) x) = ω₀ x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Moser's identity](../calculus/part-01/mosers-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_of_extDeriv_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Darboux/Basic.html#TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_of_extDeriv_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_of_extDeriv_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Darboux/Basic.html#TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_of_extDeriv_eq)
- [Source of `TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_of_extDeriv_eq` in TauCeti/Geometry/Symplectic/Darboux/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Darboux/Basic.lean#L63)
