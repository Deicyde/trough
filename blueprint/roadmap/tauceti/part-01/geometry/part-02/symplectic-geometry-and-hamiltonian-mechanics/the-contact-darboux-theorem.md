---
declaration: theorem
origin: cited
lean: TauCeti.SmoothForm.IsContactForm.exists_darbouxChart, TauCeti.IsContactFormAt.exists_darbouxChart, TauCeti.IsContactFormAt.exists_darbouxChart_of_isInteriorPoint, TauCeti.exists_diffeomorph_eventually_innerProductContactForm_apply_fderiv_eq_mul, TauCeti.SmoothForm.IsContactForm.exists_darbouxChart_of_isInteriorPoint, TauCeti.IsContactFormAt.exists_darbouxChart_of_finrank_eq_of_isInteriorPoint, TauCeti.SmoothForm.IsContactForm.exists_darbouxChart_of_finrank_eq_of_isInteriorPoint, TauCeti.IsContactDistribution.exists_darbouxChart, TauCeti.IsContactDistribution.exists_darbouxChart_of_isInteriorPoint, TauCeti.IsContactDistribution.exists_darbouxChart_of_finrank_eq_of_isInteriorPoint, TauCeti.IsContactDistribution.exists_darbouxChart_of_finrank_eq, TauCeti.IsContactFormAt.exists_darbouxChart_of_finrank_eq, TauCeti.SmoothForm.IsContactForm.exists_darbouxChart_of_finrank_eq
statement: formalized
proof: formalized
---

# The contact Darboux theorem

Around every point `x₀` of a boundaryless manifold with a
smooth contact form `α`, there are `n` with `dim E = 2n + 1`, a smooth partial diffeomorphism
`chart` from `M` to `ℝⁿ × ℝⁿ × ℝ` with `x₀ ∈ chart.source` and `chart x₀ = 0`, and a function `g`,
positive on `chart.source`, such that `chart` pulls the standard contact form `dz - Σᵢ pᵢ dqᵢ` back
to `g α` on `chart.source`.

```lean
TauCeti.SmoothForm.IsContactForm.exists_darbouxChart.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [BoundarylessManifold I M] {α : TauCeti.SmoothForm I M ℝ 1}
  (hα : α.IsContactForm) (x₀ : M) :
  ∃ n chart g,
    Module.finrank ℝ E = 2 * n + 1 ∧
      x₀ ∈ chart.source ∧
        ↑chart.toPartialEquiv x₀ = 0 ∧
          ∀ x ∈ chart.source,
            0 < g x ∧
              ∀ (v : TangentSpace I x),
                (↑(TauCeti.innerProductContactForm (EuclideanSpace ℝ (Fin n)))
                      (↑chart.toPartialEquiv x))
                    ![(d% ↑chart.toPartialEquiv x) v] =
                  g x * (↑α x) ![v]
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartan's formula for the Levi form](../manifold/part-01/cartans-formula-for-the-levi-form.md)
- [The contact Moser lemma, local form](../contact/the-contact-moser-lemma-local-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothForm.IsContactForm.exists_darbouxChart`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux/Manifold.html#TauCeti.SmoothForm.IsContactForm.exists_darbouxChart).

## Other forms

**The contact Darboux theorem for a locally defined one-form on a boundaryless manifold.** Formalized in Tau Ceti as [`TauCeti.IsContactFormAt.exists_darbouxChart`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux/Manifold.html#TauCeti.IsContactFormAt.exists_darbouxChart).

```lean
TauCeti.IsContactFormAt.exists_darbouxChart.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [BoundarylessManifold I M] {α : TauCeti.RoughForm I M ℝ 1} {U : Set M}
  {x₀ : M} (hc : TauCeti.IsContactFormAt α x₀) (hU : IsOpen U) (hx₀U : x₀ ∈ U)
  (hα :
    ContMDiffOn I (I.prod (modelWithCornersSelf ℝ (E [⋀^Fin 1]→L[ℝ] ℝ))) (↑⊤) (fun y => ⟨y, α y⟩)
      U) :
  ∃ n chart g,
    Module.finrank ℝ E = 2 * n + 1 ∧
      x₀ ∈ chart.source ∧
        chart.source ⊆ U ∧
          ↑chart.toPartialEquiv x₀ = 0 ∧
            ∀ x ∈ chart.source,
              0 < g x ∧
                ∀ (v : TangentSpace I x),
                  (↑(TauCeti.innerProductContactForm (EuclideanSpace ℝ (Fin n)))
                        (↑chart.toPartialEquiv x))
                      ![(d% ↑chart.toPartialEquiv x) v] =
                    g x * (α x) ![v]
```

**The contact Darboux theorem for a locally defined one-form.** Formalized in Tau Ceti as [`TauCeti.IsContactFormAt.exists_darbouxChart_of_isInteriorPoint`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux/Manifold.html#TauCeti.IsContactFormAt.exists_darbouxChart_of_isInteriorPoint).

```lean
TauCeti.IsContactFormAt.exists_darbouxChart_of_isInteriorPoint.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] {α : TauCeti.RoughForm I M ℝ 1} {U : Set M} {x₀ : M}
  (hc : TauCeti.IsContactFormAt α x₀) (hU : IsOpen U) (hx₀U : x₀ ∈ U)
  (hα :
    ContMDiffOn I (I.prod (modelWithCornersSelf ℝ (E [⋀^Fin 1]→L[ℝ] ℝ))) (↑⊤) (fun y => ⟨y, α y⟩) U)
  (hx₀ : I.IsInteriorPoint x₀) :
  ∃ n chart g,
    Module.finrank ℝ E = 2 * n + 1 ∧
      x₀ ∈ chart.source ∧
        chart.source ⊆ U ∧
          ↑chart.toPartialEquiv x₀ = 0 ∧
            ∀ x ∈ chart.source,
              0 < g x ∧
                ∀ (v : TangentSpace I x),
                  (↑(TauCeti.innerProductContactForm (EuclideanSpace ℝ (Fin n)))
                        (↑chart.toPartialEquiv x))
                      ![(d% ↑chart.toPartialEquiv x) v] =
                    g x * (α x) ![v]
```

**The contact Darboux theorem, local form.** Formalized in Tau Ceti as [`TauCeti.exists_diffeomorph_eventually_innerProductContactForm_apply_fderiv_eq_mul`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux/Basic.html#TauCeti.exists_diffeomorph_eventually_innerProductContactForm_apply_fderiv_eq_mul).

```lean
TauCeti.exists_diffeomorph_eventually_innerProductContactForm_apply_fderiv_eq_mul.{u_1}
  {V : Type u_1} [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V]
  {α : V → V [⋀^Fin 1]→L[ℝ] ℝ} {W : Set V} {x₀ : V} {r : ℕ∞} (hr : 1 ≤ r) (hW : IsOpen W)
  (hx₀ : x₀ ∈ W) (hα : ContDiffOn ℝ (↑r + 1) α W) (hc : TauCeti.IsContactFormAt α x₀) :
  ∃ n Φ g,
    Φ x₀ = 0 ∧
      ∀ᶠ (x : V) in nhds x₀,
        0 < g x ∧
          ∀ (v : V),
            (↑(TauCeti.innerProductContactForm (EuclideanSpace ℝ (Fin n))) (Φ x))
                ![(fderiv ℝ (⇑Φ) x) v] =
              g x * (α x) ![v]
```

**The contact Darboux theorem at an interior point.** Formalized in Tau Ceti as [`TauCeti.SmoothForm.IsContactForm.exists_darbouxChart_of_isInteriorPoint`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux/Manifold.html#TauCeti.SmoothForm.IsContactForm.exists_darbouxChart_of_isInteriorPoint).

```lean
TauCeti.SmoothForm.IsContactForm.exists_darbouxChart_of_isInteriorPoint.{u_1, u_2, u_3}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] {α : TauCeti.SmoothForm I M ℝ 1} (hα : α.IsContactForm)
  {x₀ : M} (hx₀ : I.IsInteriorPoint x₀) :
  ∃ n chart g,
    Module.finrank ℝ E = 2 * n + 1 ∧
      x₀ ∈ chart.source ∧
        ↑chart.toPartialEquiv x₀ = 0 ∧
          ∀ x ∈ chart.source,
            0 < g x ∧
              ∀ (v : TangentSpace I x),
                (↑(TauCeti.innerProductContactForm (EuclideanSpace ℝ (Fin n)))
                      (↑chart.toPartialEquiv x))
                    ![(d% ↑chart.toPartialEquiv x) v] =
                  g x * (↑α x) ![v]
```

**The contact Darboux theorem at an interior point, in dimension `2 n + 1`.** Formalized in Tau Ceti as [`TauCeti.IsContactFormAt.exists_darbouxChart_of_finrank_eq_of_isInteriorPoint`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux/Manifold.html#TauCeti.IsContactFormAt.exists_darbouxChart_of_finrank_eq_of_isInteriorPoint).

```lean
TauCeti.IsContactFormAt.exists_darbouxChart_of_finrank_eq_of_isInteriorPoint.{u_1, u_2, u_3}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] {α : TauCeti.RoughForm I M ℝ 1} {U : Set M} {x₀ : M}
  (hc : TauCeti.IsContactFormAt α x₀) {n : ℕ} (hn : Module.finrank ℝ E = 2 * n + 1) (hU : IsOpen U)
  (hx₀U : x₀ ∈ U)
  (hα :
    ContMDiffOn I (I.prod (modelWithCornersSelf ℝ (E [⋀^Fin 1]→L[ℝ] ℝ))) (↑⊤) (fun y => ⟨y, α y⟩) U)
  (hx₀ : I.IsInteriorPoint x₀) :
  ∃ chart g,
    x₀ ∈ chart.source ∧
      chart.source ⊆ U ∧
        ↑chart.toPartialEquiv x₀ = 0 ∧
          ∀ x ∈ chart.source,
            0 < g x ∧
              ∀ (v : TangentSpace I x),
                (↑(TauCeti.innerProductContactForm (EuclideanSpace ℝ (Fin n)))
                      (↑chart.toPartialEquiv x))
                    ![(d% ↑chart.toPartialEquiv x) v] =
                  g x * (α x) ![v]
```

**The contact Darboux theorem at an interior point, in dimension `2 n + 1`.** Formalized in Tau Ceti as [`TauCeti.SmoothForm.IsContactForm.exists_darbouxChart_of_finrank_eq_of_isInteriorPoint`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux/Manifold.html#TauCeti.SmoothForm.IsContactForm.exists_darbouxChart_of_finrank_eq_of_isInteriorPoint).

```lean
TauCeti.SmoothForm.IsContactForm.exists_darbouxChart_of_finrank_eq_of_isInteriorPoint.{u_1, u_2,
    u_3}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] {α : TauCeti.SmoothForm I M ℝ 1} (hα : α.IsContactForm)
  {n : ℕ} (hn : Module.finrank ℝ E = 2 * n + 1) {x₀ : M} (hx₀ : I.IsInteriorPoint x₀) :
  ∃ chart g,
    x₀ ∈ chart.source ∧
      ↑chart.toPartialEquiv x₀ = 0 ∧
        ∀ x ∈ chart.source,
          0 < g x ∧
            ∀ (v : TangentSpace I x),
              (↑(TauCeti.innerProductContactForm (EuclideanSpace ℝ (Fin n)))
                    (↑chart.toPartialEquiv x))
                  ![(d% ↑chart.toPartialEquiv x) v] =
                g x * (↑α x) ![v]
```

**The contact Darboux theorem for contact structures.** Formalized in Tau Ceti as [`TauCeti.IsContactDistribution.exists_darbouxChart`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux/Manifold.html#TauCeti.IsContactDistribution.exists_darbouxChart).

```lean
TauCeti.IsContactDistribution.exists_darbouxChart.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [BoundarylessManifold I M] {D : (x : M) → Submodule ℝ (TangentSpace I x)}
  (hD : TauCeti.IsContactDistribution I (↑⊤) D) (x₀ : M) :
  ∃ n chart,
    Module.finrank ℝ E = 2 * n + 1 ∧
      x₀ ∈ chart.source ∧
        ↑chart.toPartialEquiv x₀ = 0 ∧
          ∀ x ∈ chart.source,
            D x =
              Submodule.comap (↑(mfderiv% ↑chart.toPartialEquiv x))
                ((TauCeti.innerProductContactForm (EuclideanSpace ℝ (Fin n))).kerDistribution
                  (↑chart.toPartialEquiv x))
```

**The contact Darboux theorem for contact structures at an interior point.** Formalized in Tau Ceti as [`TauCeti.IsContactDistribution.exists_darbouxChart_of_isInteriorPoint`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux/Manifold.html#TauCeti.IsContactDistribution.exists_darbouxChart_of_isInteriorPoint).

```lean
TauCeti.IsContactDistribution.exists_darbouxChart_of_isInteriorPoint.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] {D : (x : M) → Submodule ℝ (TangentSpace I x)}
  (hD : TauCeti.IsContactDistribution I (↑⊤) D) {x₀ : M} (hx₀ : I.IsInteriorPoint x₀) :
  ∃ n chart,
    Module.finrank ℝ E = 2 * n + 1 ∧
      x₀ ∈ chart.source ∧
        ↑chart.toPartialEquiv x₀ = 0 ∧
          ∀ x ∈ chart.source,
            D x =
              Submodule.comap (↑(mfderiv% ↑chart.toPartialEquiv x))
                ((TauCeti.innerProductContactForm (EuclideanSpace ℝ (Fin n))).kerDistribution
                  (↑chart.toPartialEquiv x))
```

**The contact Darboux theorem for contact structures at an interior point, in dimension `2 n + 1`.** Formalized in Tau Ceti as [`TauCeti.IsContactDistribution.exists_darbouxChart_of_finrank_eq_of_isInteriorPoint`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux/Manifold.html#TauCeti.IsContactDistribution.exists_darbouxChart_of_finrank_eq_of_isInteriorPoint).

```lean
TauCeti.IsContactDistribution.exists_darbouxChart_of_finrank_eq_of_isInteriorPoint.{u_1, u_2, u_3}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] {D : (x : M) → Submodule ℝ (TangentSpace I x)}
  (hD : TauCeti.IsContactDistribution I (↑⊤) D) {n : ℕ} (hn : Module.finrank ℝ E = 2 * n + 1)
  {x₀ : M} (hx₀ : I.IsInteriorPoint x₀) :
  ∃ chart,
    x₀ ∈ chart.source ∧
      ↑chart.toPartialEquiv x₀ = 0 ∧
        ∀ x ∈ chart.source,
          D x =
            Submodule.comap (↑(mfderiv% ↑chart.toPartialEquiv x))
              ((TauCeti.innerProductContactForm (EuclideanSpace ℝ (Fin n))).kerDistribution
                (↑chart.toPartialEquiv x))
```

**The contact Darboux theorem for contact structures in dimension `2 n + 1`.** Formalized in Tau Ceti as [`TauCeti.IsContactDistribution.exists_darbouxChart_of_finrank_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux/Manifold.html#TauCeti.IsContactDistribution.exists_darbouxChart_of_finrank_eq).

```lean
TauCeti.IsContactDistribution.exists_darbouxChart_of_finrank_eq.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [BoundarylessManifold I M] {D : (x : M) → Submodule ℝ (TangentSpace I x)}
  (hD : TauCeti.IsContactDistribution I (↑⊤) D) {n : ℕ} (hn : Module.finrank ℝ E = 2 * n + 1)
  (x₀ : M) :
  ∃ chart,
    x₀ ∈ chart.source ∧
      ↑chart.toPartialEquiv x₀ = 0 ∧
        ∀ x ∈ chart.source,
          D x =
            Submodule.comap (↑(mfderiv% ↑chart.toPartialEquiv x))
              ((TauCeti.innerProductContactForm (EuclideanSpace ℝ (Fin n))).kerDistribution
                (↑chart.toPartialEquiv x))
```

**The contact Darboux theorem in dimension `2 n + 1`.** Formalized in Tau Ceti as [`TauCeti.IsContactFormAt.exists_darbouxChart_of_finrank_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux/Manifold.html#TauCeti.IsContactFormAt.exists_darbouxChart_of_finrank_eq).

```lean
TauCeti.IsContactFormAt.exists_darbouxChart_of_finrank_eq.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [BoundarylessManifold I M] {α : TauCeti.RoughForm I M ℝ 1} {U : Set M}
  {x₀ : M} (hc : TauCeti.IsContactFormAt α x₀) {n : ℕ} (hn : Module.finrank ℝ E = 2 * n + 1)
  (hU : IsOpen U) (hx₀U : x₀ ∈ U)
  (hα :
    ContMDiffOn I (I.prod (modelWithCornersSelf ℝ (E [⋀^Fin 1]→L[ℝ] ℝ))) (↑⊤) (fun y => ⟨y, α y⟩)
      U) :
  ∃ chart g,
    x₀ ∈ chart.source ∧
      chart.source ⊆ U ∧
        ↑chart.toPartialEquiv x₀ = 0 ∧
          ∀ x ∈ chart.source,
            0 < g x ∧
              ∀ (v : TangentSpace I x),
                (↑(TauCeti.innerProductContactForm (EuclideanSpace ℝ (Fin n)))
                      (↑chart.toPartialEquiv x))
                    ![(d% ↑chart.toPartialEquiv x) v] =
                  g x * (α x) ![v]
```

**The contact Darboux theorem in dimension `2 n + 1`.** Formalized in Tau Ceti as [`TauCeti.SmoothForm.IsContactForm.exists_darbouxChart_of_finrank_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux/Manifold.html#TauCeti.SmoothForm.IsContactForm.exists_darbouxChart_of_finrank_eq).

```lean
TauCeti.SmoothForm.IsContactForm.exists_darbouxChart_of_finrank_eq.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [BoundarylessManifold I M] {α : TauCeti.SmoothForm I M ℝ 1}
  (hα : α.IsContactForm) {n : ℕ} (hn : Module.finrank ℝ E = 2 * n + 1) (x₀ : M) :
  ∃ chart g,
    x₀ ∈ chart.source ∧
      ↑chart.toPartialEquiv x₀ = 0 ∧
        ∀ x ∈ chart.source,
          0 < g x ∧
            ∀ (v : TangentSpace I x),
              (↑(TauCeti.innerProductContactForm (EuclideanSpace ℝ (Fin n)))
                    (↑chart.toPartialEquiv x))
                  ![(d% ↑chart.toPartialEquiv x) v] =
                g x * (↑α x) ![v]
```

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothForm.IsContactForm.exists_darbouxChart`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Darboux/Manifold.html#TauCeti.SmoothForm.IsContactForm.exists_darbouxChart)
- [Source of `TauCeti.SmoothForm.IsContactForm.exists_darbouxChart` in TauCeti/Geometry/Contact/Darboux/Manifold.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Contact/Darboux/Manifold.lean#L317)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
