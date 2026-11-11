---
declaration: theorem
origin: cited
lean: TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_smul_of_extDeriv_eq
statement: formalized
proof: formalized
---

# The contact Moser lemma, local form

Let `α₀`, `α₁` be `C^(r+1)` one-forms (`r ≥ 1`) on an
open subset `W` of a finite-dimensional real normed space, which agree at `x₀ ∈ W` together with
their exterior derivatives, and let `α₁` be a contact form at `x₀`. Then some `C^r` diffeomorphism
`ψ` of the space pulls `α₁` back to a positive multiple `g • α₀` of `α₀` on a neighbourhood of
`x₀`. Moreover `ψ` fixes, near `x₀`, every point at which `α₀` and `α₁` agree; in particular
`ψ x₀ = x₀`.

```lean
TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_smul_of_extDeriv_eq.{u_1}
  {V : Type u_1} [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V]
  {α₀ α₁ : V → V [⋀^Fin 1]→L[ℝ] ℝ} {W : Set V} {x₀ : V} {r : ℕ∞} (hr : 1 ≤ r) (hW : IsOpen W)
  (hx₀ : x₀ ∈ W) (hα₀ : ContDiffOn ℝ (↑r + 1) α₀ W) (hα₁ : ContDiffOn ℝ (↑r + 1) α₁ W)
  (heq : α₁ x₀ = α₀ x₀) (hdeq : extDeriv α₁ x₀ = extDeriv α₀ x₀)
  (hc : TauCeti.IsContactFormAt α₁ x₀) :
  ∃ ψ g,
    (∀ᶠ (x : V) in nhds x₀, α₁ x = α₀ x → ψ x = x) ∧
      ∀ᶠ (x : V) in nhds x₀,
        0 < g x ∧ (α₁ (ψ x)).compContinuousLinearMap (fderiv ℝ (⇑ψ) x) = g x • α₀ x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartan's formula](../../../analysis/part-02/calculus/part-01/cartans-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_smul_of_extDeriv_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux.html#TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_smul_of_extDeriv_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_smul_of_extDeriv_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux.html#TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_smul_of_extDeriv_eq)
- [Source of `TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq_smul_of_extDeriv_eq` in TauCeti/Geometry/Contact/Darboux.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Contact/Darboux.lean#L243)
