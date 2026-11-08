---
declaration: theorem
origin: cited
lean: TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_frontier, TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_of_halfStripExterior, TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_of_halfStrip, TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_ends
statement: formalized
proof: formalized
---

# The Schwarz--Christoffel theorem for a bounded polygonal Jordan domain

Let `U` be a
bounded, connected open set whose frontier is a Jordan curve.  Suppose that `U` coincides
near each frontier point other than the distinct vertices `v i` with an open half-plane, and near
the vertex `v i` with the open sector of opening `(e i + 1) * π` at `v i`, where `e i ∈ (-1, 1)`.
Then there are distinct real prevertices `a i` and constants `A ≠ 0` and `B` such that
`z ↦ A * F z + B` maps the upper half-plane bijectively onto `U`, where `F` is the normalized
Schwarz--Christoffel primitive for the prevertices `a` and the turning exponents `e`, and such that
the Schwarz--Christoffel vertex at `a i`, the limit of `F` at `a i`, is sent to `v i`.

```lean
TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_frontier.{u_1}
  {ι : Type u_1} [Fintype ι] (e : ι → ℝ) (he : ∀ (i : ι), e i ∈ Set.Ioo (-1) 1)
  (z₀ : UpperHalfPlane) {U : Set ℂ} (hUo : IsOpen U) (hUc : IsConnected U)
  (hUb : Bornology.IsBounded U) (hUJ : TauCeti.IsJordanCurve (frontier U)) {v : ι → ℂ}
  (hv : Function.Injective v)
  (hside :
    ∀ w ∈ frontier U,
      (∀ (i : ι), w ≠ v i) →
        ∃ ρ > 0, ∃ q b, b ≠ 0 ∧ ∀ z ∈ Metric.ball w ρ, z ∈ U ↔ 0 < ((z - q) / b).im)
  (hcorner :
    ∀ (i : ι),
      ∃ ρ > 0,
        ∃ b,
          b ≠ 0 ∧
            ∀ z ∈ Metric.ball (v i) ρ,
              z ≠ v i → (z ∈ U ↔ |((z - v i) / b).arg| < (e i + 1) * Real.pi / 2)) :
  ∃ a,
    Function.Injective a ∧
      ∃ A,
        A ≠ 0 ∧
          ∃ B,
            Set.BijOn (fun z => A * TauCeti.schwarzChristoffelPrimitive a e z₀ z + B)
                UpperHalfPlane.upperHalfPlaneSet U ∧
              ∀ (i : ι), A * TauCeti.schwarzChristoffelVertex a e z₀ i + B = v i
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Carathéodory's continuity theorem, as a characterization](caratheodorys-continuity-theorem-as-a-characteri.md)
- [Carathéodory's theorem for the inside of a Jordan curve](caratheodorys-theorem-for-the-inside-of-a-jordan.md)
- [Cauchy estimate](../../../part-02/complex/part-01/cauchy-estimate.md)
- [The converse of Cauchy's theorem](../../../../number-theory/part-01/bounded-laplace-and-ordered-dirichlet-boundary-c/the-converse-of-cauchys-theorem.md)
- [Generalized winding number (HW Def 2.1)](../../contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)
- [The homology Cauchy theorem (roadmap `homologyCauchyTheorem`, Layer 3)](../../contour-integration-and-the-hungerbuhler-wasem-g/the-homology-cauchy-theorem-roadmap-homologycauc.md)
- [Hurwitz's theorem](hurwitzs-theorem.md)
- [Janiszewski's theorem](../part-02/janiszewskis-theorem.md)
- [Montel's selection theorem](../../../part-02/complex/part-02/montels-selection-theorem.md)
- [The Riemann mapping theorem](the-riemann-mapping-theorem.md)
- [Rouché's theorem for a disc, classical form](../part-02/rouches-theorem-for-a-disc-classical-form.md)
- [Schwarz reflection principle (real axis)](schwarz-reflection-principle-real-axis.md)
- [The Schwarz--Christoffel formula](../part-02/the-schwarz-christoffel-formula.md)
- [Strict Schwarz lemma](../part-02/strict-schwarz-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_frontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/JordanPolygon.html#TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_frontier).

## Other forms

**The Schwarz--Christoffel theorem for a polygonal Jordan domain whose end is the exterior of a half-strip.** Formalized in Tau Ceti as [`TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_of_halfStripExterior`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/JordanPolygon.html#TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_of_halfStripExterior).

```lean
TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_of_halfStripExterior.{u_1}
  {ι : Type u_1} [Fintype ι] (e : ι → ℝ) (he : ∀ (i : ι), e i ∈ Set.Ioo (-1) 1)
  (z₀ : UpperHalfPlane) {U : Set ℂ} (hUo : IsOpen U) (hUc : IsConnected U)
  (hUJ : TauCeti.IsJordanCurve (insert OnePoint.infty (OnePoint.some '' frontier U))) {v : ι → ℂ}
  (hv : Function.Injective v)
  (hside :
    ∀ w ∈ frontier U,
      (∀ (i : ι), w ≠ v i) →
        ∃ ρ > 0, ∃ q b, b ≠ 0 ∧ ∀ z ∈ Metric.ball w ρ, z ∈ U ↔ 0 < ((z - q) / b).im)
  (hcorner :
    ∀ (i : ι),
      ∃ ρ > 0,
        ∃ b,
          b ≠ 0 ∧
            ∀ z ∈ Metric.ball (v i) ρ,
              z ≠ v i → (z ∈ U ↔ |((z - v i) / b).arg| < (e i + 1) * Real.pi / 2))
  (hinfty :
    ∃ ρ c b,
      b ≠ 0 ∧
        ∀ (z : ℂ),
          ρ < ‖z - c‖ → (z ∈ U ↔ ((z - c) / b).re < 0 ∨ ((z - c) / b).im ∉ Set.Icc 0 Real.pi)) :
  ∃ a,
    Function.Injective a ∧
      ∃ A,
        A ≠ 0 ∧
          ∃ B,
            Set.BijOn (fun z => A * TauCeti.schwarzChristoffelPrimitive a e z₀ z + B)
                UpperHalfPlane.upperHalfPlaneSet U ∧
              ∀ (i : ι), A * TauCeti.schwarzChristoffelVertex a e z₀ i + B = v i
```

**The Schwarz--Christoffel theorem for a polygonal Jordan domain with a half-strip end.** Formalized in Tau Ceti as [`TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_of_halfStrip`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/JordanPolygon.html#TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_of_halfStrip).

```lean
TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_of_halfStrip.{u_1}
  {ι : Type u_1} [Fintype ι] (e : ι → ℝ) (he : ∀ (i : ι), e i ∈ Set.Ioo (-1) 1)
  (z₀ : UpperHalfPlane) {U : Set ℂ} (hUo : IsOpen U) (hUc : IsConnected U)
  (hUJ : TauCeti.IsJordanCurve (insert OnePoint.infty (OnePoint.some '' frontier U))) {v : ι → ℂ}
  (hv : Function.Injective v)
  (hside :
    ∀ w ∈ frontier U,
      (∀ (i : ι), w ≠ v i) →
        ∃ ρ > 0, ∃ q b, b ≠ 0 ∧ ∀ z ∈ Metric.ball w ρ, z ∈ U ↔ 0 < ((z - q) / b).im)
  (hcorner :
    ∀ (i : ι),
      ∃ ρ > 0,
        ∃ b,
          b ≠ 0 ∧
            ∀ z ∈ Metric.ball (v i) ρ,
              z ≠ v i → (z ∈ U ↔ |((z - v i) / b).arg| < (e i + 1) * Real.pi / 2))
  (hinfty :
    ∃ ρ c b,
      b ≠ 0 ∧
        ∀ (z : ℂ),
          ρ < ‖z - c‖ → (z ∈ U ↔ 0 < ((z - c) / b).re ∧ ((z - c) / b).im ∈ Set.Ioo 0 Real.pi)) :
  ∃ a,
    Function.Injective a ∧
      ∃ A,
        A ≠ 0 ∧
          ∃ B,
            Set.BijOn (fun z => A * TauCeti.schwarzChristoffelPrimitive a e z₀ z + B)
                UpperHalfPlane.upperHalfPlaneSet U ∧
              ∀ (i : ι), A * TauCeti.schwarzChristoffelVertex a e z₀ i + B = v i
```

**The Schwarz--Christoffel theorem for polygonal domains with several ends.** Formalized in Tau Ceti as [`TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_ends`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/MultipleEnds/PolygonalDomain.html#TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_ends).

```lean
TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_polygonal_ends.{u_1, u_2, u_3,
    u_4}
  {ι : Type u_1} {κ : Type u_2} [Fintype ι] [Fintype κ] (e : ι → ℝ)
  (he : ∀ (i : ι), e i ∈ Set.Ioo (-1) 1) (e' : κ → ℝ) (z₀ : UpperHalfPlane) {U : Set ℂ}
  (hUo : IsOpen U) (hUs : IsSimplyConnected U) (hUb : ¬Bornology.IsBounded U) {v : ι → ℂ}
  (hv : Function.Injective v)
  (hside :
    ∀ w ∈ frontier U,
      (∀ (i : ι), w ≠ v i) →
        ∃ ρ > 0, ∃ p b, b ≠ 0 ∧ ∀ z ∈ Metric.ball w ρ, z ∈ U ↔ 0 < ((z - p) / b).im)
  (hcorner :
    ∀ (i : ι),
      ∃ ρ > 0,
        ∃ b,
          b ≠ 0 ∧
            ∀ z ∈ Metric.ball (v i) ρ,
              z ≠ v i → (z ∈ U ↔ |((z - v i) / b).arg| < (e i + 1) * Real.pi / 2))
  {σ : Type u_3} {τ : Type u_4} [Finite σ] [Finite τ] {x y : σ → ℂ} {o d : τ → ℂ}
  (hd : ∀ (k : τ), d k ≠ 0)
  (hfr : frontier U = (⋃ i, segment ℝ (x i) (y i)) ∪ ⋃ k, (fun t => o k + ↑t * d k) '' Set.Ici 0)
  {q : ℂ} (hq : q ∉ closure U) {E : κ → Set ℂ} {c b : κ → ℂ} {ρ : κ → ℝ} {R : ℝ}
  (hb : ∀ (k : κ), b k ≠ 0)
  (hE :
    ∀ (k : κ),
      e' k ∈ Set.Ioo (-3) (-1) ∧
          E k = {w | ρ k < ‖w - c k‖ ∧ |((w - c k) / b k).arg| < (-e' k - 1) * Real.pi / 2} ∨
        e' k = -1 ∧
            E k = {w | ρ k < ((w - c k) / b k).re ∧ ((w - c k) / b k).im ∈ Set.Ioo 0 Real.pi} ∨
          e' k = -3 ∧
            E k =
              {w |
                ρ k < ‖w - c k‖ ∧
                  (((w - c k) / b k).re < 0 ∨ ((w - c k) / b k).im ∉ Set.Icc 0 Real.pi)})
  (hEU : ∀ (k : κ), E k ⊆ U) (hUE : ∀ w ∈ U, R < ‖w‖ → ∃ k, w ∈ E k)
  (hEd : Pairwise (Function.onFun Disjoint E)) :
  ∃ a a',
    Function.Injective (Sum.elim a a') ∧
      ∃ A,
        A ≠ 0 ∧
          ∃ B,
            Set.BijOn
                (fun z =>
                  A * TauCeti.schwarzChristoffelPrimitive (Sum.elim a a') (Sum.elim e e') z₀ z + B)
                UpperHalfPlane.upperHalfPlaneSet U ∧
              (∀ (i : ι),
                  A *
                        TauCeti.schwarzChristoffelVertex (Sum.elim a a') (Sum.elim e e') z₀
                          (Sum.inl i) +
                      B =
                    v i) ∧
                ∀ (k : κ),
                  ∀ᶠ (z : ℂ) in nhdsWithin (↑(a' k)) UpperHalfPlane.upperHalfPlaneSet,
                    A * TauCeti.schwarzChristoffelPrimitive (Sum.elim a a') (Sum.elim e e') z₀ z +
                        B ∈
                      E k
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_frontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/JordanPolygon.html#TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_frontier)
- [Source of `TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_frontier` in TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/JordanPolygon.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/JordanPolygon.lean#L108)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ConformalMapping/STATUS.md)
