---
declaration: theorem
origin: cited
lean: TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq, TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart, TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart_of_isInteriorPoint, TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart_of_symplecticForm, TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart_of_symplecticForm_of_isInteriorPoint
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

## Proof depends on

- [Linear Darboux theorem](../../../geometry/part-02/symplectic/linear-darboux-theorem.md)
- [Moser's lemma, local form](mosers-lemma-local-form.md)
- [The Poincaré lemma](../../part-02/calculus/part-01/the-poincare-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Darboux/Basic.html#TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq).

## Other forms

**Darboux's theorem.** Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/Darboux.html#TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart).

```lean
TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [BoundarylessManifold I M] {form : TauCeti.SmoothTwoForm I M}
  (hform : form.IsSymplectic) (x₀ : M) :
  ∃ chart form₀,
    x₀ ∈ chart.source ∧
      ↑chart.toPartialEquiv x₀ = 0 ∧
        ∀ x ∈ chart.source,
          ∀ (v w : TangentSpace I x),
            TauCeti.SmoothBundleForm.eval₂ form x v w =
              (fun v w => (form₀.toBilinForm v) w) ((d% ↑chart.toPartialEquiv x) v)
                ((d% ↑chart.toPartialEquiv x) w)
```

**Darboux's theorem at an interior point.** Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart_of_isInteriorPoint`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/Darboux.html#TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart_of_isInteriorPoint).

```lean
TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart_of_isInteriorPoint.{u_1, u_2, u_3}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] {form : TauCeti.SmoothTwoForm I M}
  (hform : form.IsSymplectic) {x₀ : M} (hx₀ : I.IsInteriorPoint x₀) :
  ∃ chart form₀,
    x₀ ∈ chart.source ∧
      ↑chart.toPartialEquiv x₀ = 0 ∧
        ∀ x ∈ chart.source,
          ∀ (v w : TangentSpace I x),
            TauCeti.SmoothBundleForm.eval₂ form x v w =
              (fun v w => (form₀.toBilinForm v) w) ((d% ↑chart.toPartialEquiv x) v)
                ((d% ↑chart.toPartialEquiv x) w)
```

**Darboux's theorem for a prescribed model symplectic form.** Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart_of_symplecticForm`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/Darboux.html#TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart_of_symplecticForm).

```lean
TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart_of_symplecticForm.{u_1, u_2, u_3}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] [BoundarylessManifold I M]
  {form : TauCeti.SmoothTwoForm I M} (hform : form.IsSymplectic) (form₀ : TauCeti.SymplecticForm E)
  (x₀ : M) :
  ∃ chart,
    x₀ ∈ chart.source ∧
      ↑chart.toPartialEquiv x₀ = 0 ∧
        ∀ x ∈ chart.source,
          ∀ (v w : TangentSpace I x),
            TauCeti.SmoothBundleForm.eval₂ form x v w =
              (fun v w => (form₀.toBilinForm v) w) ((d% ↑chart.toPartialEquiv x) v)
                ((d% ↑chart.toPartialEquiv x) w)
```

**Darboux's theorem for a prescribed model symplectic form at an interior point.** Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart_of_symplecticForm_of_isInteriorPoint`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/Darboux.html#TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart_of_symplecticForm_of_isInteriorPoint).

```lean
TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart_of_symplecticForm_of_isInteriorPoint.{u_1,
    u_2, u_3}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] {form : TauCeti.SmoothTwoForm I M}
  (hform : form.IsSymplectic) (form₀ : TauCeti.SymplecticForm E) {x₀ : M}
  (hx₀ : I.IsInteriorPoint x₀) :
  ∃ chart,
    x₀ ∈ chart.source ∧
      ↑chart.toPartialEquiv x₀ = 0 ∧
        ∀ x ∈ chart.source,
          ∀ (v w : TangentSpace I x),
            TauCeti.SmoothBundleForm.eval₂ form x v w =
              (fun v w => (form₀.toBilinForm v) w) ((d% ↑chart.toPartialEquiv x) v)
                ((d% ↑chart.toPartialEquiv x) w)
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Darboux/Basic.html#TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq)
- [Source of `TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq` in TauCeti/Geometry/Symplectic/Darboux/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Darboux/Basic.lean#L143)
- [Tau Ceti roadmap status: Analytic Heegaard Floer homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/HeegaardFloer/STATUS.md)
