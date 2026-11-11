---
declaration: theorem
origin: cited
lean: TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart, TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq, TauCeti.exists_equivariant_diffeomorph_compContinuousLinearMap_fderiv_eq, TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart_of_isInteriorPoint, TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart_of_symplecticForm, TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart_of_symplecticForm_of_isInteriorPoint, TauCeti.exists_diffeomorph_centered_forall_mem_eq_compContinuousLinearMap_fderiv
statement: formalized
proof: formalized
---

# Darboux's theorem

Around every point `x₀` of a finite-dimensional boundaryless symplectic
manifold `(M, form)`, there are a smooth partial diffeomorphism `chart` into `E` with
`x₀ ∈ chart.source` and `chart x₀ = 0` and a constant symplectic form `form₀` on `E` whose pullback
by `mvfderiv I chart` equals `form` on `chart.source`.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Linear Darboux theorem](linear-darboux-theorem.md)
- [Moser's lemma, local form](mosers-lemma-local-form.md)
- [The Poincaré lemma](../../../analysis/part-02/calculus/part-02/the-poincare-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/Darboux.html#TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart).

## Other forms

**Darboux's theorem.** Formalized in Tau Ceti as [`TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Darboux/Basic.html#TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq).

```lean
TauCeti.exists_diffeomorph_eventually_compContinuousLinearMap_fderiv_eq.{u_1} {V : Type u_1}
  [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V] {ω : V → V [⋀^Fin 2]→L[ℝ] ℝ}
  {W : Set V} {x₀ : V} {r : ℕ∞} (hr : 1 ≤ r) (hW : IsOpen W) (hx₀ : x₀ ∈ W)
  (hω : ContDiffOn ℝ (↑r) ω W) (hdω : ∀ x ∈ W, extDeriv ω x = 0)
  (hnd : ∀ (v : V), (∀ (w : V), (ω x₀) ![v, w] = 0) → v = 0) :
  ∃ ψ, ψ x₀ = x₀ ∧ ∀ᶠ (x : V) in nhds x₀, (ω (ψ x)).compContinuousLinearMap (fderiv ℝ (⇑ψ) x) = ω x₀
```

**Darboux's theorem, equivariant form.** Formalized in Tau Ceti as [`TauCeti.exists_equivariant_diffeomorph_compContinuousLinearMap_fderiv_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Darboux/Basic.html#TauCeti.exists_equivariant_diffeomorph_compContinuousLinearMap_fderiv_eq).

```lean
TauCeti.exists_equivariant_diffeomorph_compContinuousLinearMap_fderiv_eq.{u_1, u_2} {V : Type u_1}
  [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V] {G : Type u_2} [Group G]
  {ρ : ContRepresentation ℝ G V} (hρ : Bornology.IsBounded (Set.range ⇑ρ))
  {ω : V → V [⋀^Fin 2]→L[ℝ] ℝ} {W : Set V} {x₀ : V} (hρx₀ : ∀ (g : G), (ρ g) x₀ = x₀) {r : ℕ∞}
  (hr : 1 ≤ r) (hW : IsOpen W) (hx₀ : x₀ ∈ W) (hω : ContDiffOn ℝ (↑r) ω W)
  (hdω : ∀ x ∈ W, extDeriv ω x = 0) (hnd : ∀ (v : V), (∀ (w : V), (ω x₀) ![v, w] = 0) → v = 0)
  (hωρ : ∀ (g : G), ∀ y ∈ W, (ω ((ρ g) y)).compContinuousLinearMap (ρ g) = ω y) :
  ∃ ψ U,
    IsOpen U ∧
      x₀ ∈ U ∧
        U ⊆ W ∧
          (∀ (g : G), Set.MapsTo (⇑(ρ g)) U U) ∧
            ψ x₀ = x₀ ∧
              (∀ (g : G), ∀ x ∈ U, ψ ((ρ g) x) = (ρ g) (ψ x)) ∧
                ∀ x ∈ U, (ω (ψ x)).compContinuousLinearMap (fderiv ℝ (⇑ψ) x) = ω x₀
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

**Darboux's theorem, centred inverse form.** Formalized in Tau Ceti as [`TauCeti.exists_diffeomorph_centered_forall_mem_eq_compContinuousLinearMap_fderiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Darboux/Basic.html#TauCeti.exists_diffeomorph_centered_forall_mem_eq_compContinuousLinearMap_fderiv).

```lean
TauCeti.exists_diffeomorph_centered_forall_mem_eq_compContinuousLinearMap_fderiv.{u_1}
  {V : Type u_1} [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V]
  {ω : V → V [⋀^Fin 2]→L[ℝ] ℝ} {W : Set V} {x₀ : V} {r : ℕ∞} (hr : 1 ≤ r) (hW : IsOpen W)
  (hx₀ : x₀ ∈ W) (hω : ContDiffOn ℝ (↑r) ω W) (hdω : ∀ x ∈ W, extDeriv ω x = 0)
  (hnd : ∀ (v : V), (∀ (w : V), (ω x₀) ![v, w] = 0) → v = 0) :
  ∃ Φ V₀,
    Φ x₀ = 0 ∧
      IsOpen V₀ ∧
        x₀ ∈ V₀ ∧ V₀ ⊆ W ∧ ∀ y ∈ V₀, ω y = (ω x₀).compContinuousLinearMap (fderiv ℝ (⇑Φ) y)
```

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/Darboux.html#TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart)
- [Source of `TauCeti.SmoothTwoForm.IsSymplectic.exists_darbouxChart` in TauCeti/Geometry/Symplectic/Manifold/Darboux.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Manifold/Darboux.lean#L303)
