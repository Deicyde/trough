---
declaration: theorem
origin: cited
lean: TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq
statement: formalized
proof: formalized
---

# Darboux's theorem

A closed `C^r` two-form `ω` (`r ≥ 1`) on an open subset of a
finite-dimensional real normed space, nondegenerate at `x₀`, is constant in suitable coordinates
near `x₀`: there is a `C^r` diffeomorphism `ψ` of the space fixing `x₀` such that the pullback
`ψ^* ω` equals the constant form `ω(x₀)` on a neighbourhood of `x₀`.

```lean
TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq.{u_1} {V : Type u_1}
  [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V] {ω : V → V [⋀^Fin 2]→L[ℝ] ℝ}
  {W : Set V} {x₀ : V} {r : ℕ∞} (hr : 1 ≤ r) (hW : IsOpen W) (hx₀ : x₀ ∈ W)
  (hω : ContDiffOn ℝ (↑r) ω W) (hdω : ∀ x ∈ W, extDeriv ω x = 0)
  (hnd : ∀ (v : V), (∀ (w : V), (ω x₀) ![v, w] = 0) → v = 0) :
  ∃ ψ, ψ x₀ = x₀ ∧ ∀ᶠ (x : V) in nhds x₀, (ω (ψ x)).compContinuousLinearMap (fderiv ℝ (⇑ψ) x) = ω x₀
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Darboux/Basic.html#TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Darboux/Basic.html#TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq)
- [Source of `TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq` in TauCeti/Geometry/Symplectic/Darboux/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Darboux/Basic.lean#L143)
- [Tau Ceti roadmap status: Analytic Heegaard Floer homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/HeegaardFloer/STATUS.md)
