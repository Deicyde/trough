---
declaration: theorem
origin: cited
lean: TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_frontier, TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_of_halfStripExterior, TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_of_halfStrip, TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_insert_infty
statement: formalized
proof: formalized
---

# The Schwarz--Christoffel theorem for a bounded polygonal Jordan domain

Let `U` be a
bounded open set whose frontier is a Jordan curve.  Suppose that `U` coincides
near each frontier point other than the distinct vertices `v i` with an open half-plane, and near
the vertex `v i` with the open sector of opening `(e i + 1) * π` at `v i`, where `e i ∈ (-1, 1)`.
Then there are distinct real prevertices `a i` and constants `A ≠ 0` and `B` such that
`z ↦ A * F z + B` maps the upper half-plane bijectively onto `U`, where `F` is the normalized
Schwarz--Christoffel primitive for the prevertices `a` and the turning exponents `e`, and such that
the Schwarz--Christoffel vertex at `a i`, the limit of `F` at `a i`, is sent to `v i`.

```lean
TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_frontier.{u_1}
  {ι : Type u_1} [Fintype ι] (e : ι → ℝ) (he : ∀ (i : ι), e i ∈ Set.Ioo (-1) 1)
  (z₀ : UpperHalfPlane) {U : Set ℂ} (hUo : IsOpen U) (hUb : Bornology.IsBounded U)
  (hUJ : TauCeti.IsJordanCurve (frontier U)) {v : ι → ℂ} (hv : Function.Injective v)
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

- [Carathéodory's continuity theorem](../../part-02/complex/part-01/caratheodorys-continuity-theorem.md)
- [Carathéodory's theorem for the inside of a Jordan curve](../../part-02/complex/part-01/caratheodorys-theorem-for-the-inside-of-a-jordan.md)
- [Cauchy estimate](../../part-02/complex/part-01/cauchy-estimate.md)
- [The converse of Cauchy's theorem](../../../number-theory/part-01/bounded-laplace-and-ordered-dirichlet-boundary-c/the-converse-of-cauchys-theorem.md)
- [Generalized winding number (HW Def 2.1)](../contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)
- [The homology Cauchy theorem (roadmap `homologyCauchyTheorem`, Layer 3)](../contour-integration-and-the-hungerbuhler-wasem-g/the-homology-cauchy-theorem-roadmap-homologycauc.md)
- [Hurwitz's theorem](../../part-02/complex/part-01/hurwitzs-theorem.md)
- [Janiszewski's theorem](../../part-02/complex/part-02/janiszewskis-theorem.md)
- [The Jordan curve theorem](the-jordan-curve-theorem.md)
- [The Jordan separation theorem](../../part-02/complex/part-02/the-jordan-separation-theorem.md)
- [Montel's selection theorem](../../part-02/complex/part-02/montels-selection-theorem.md)
- [Poincaré defect identity (norm form)](../../part-02/complex/part-03/poincare-defect-identity-norm-form.md)
- [The Riemann mapping theorem](the-riemann-mapping-theorem.md)
- [Rouché's theorem for a disc, classical form](../../part-02/complex/part-03/rouches-theorem-for-a-disc-classical-form.md)
- [The Schwarz--Christoffel formula](the-schwarz-christoffel-formula.md)
- [Strict Schwarz lemma](../../part-02/complex/part-03/strict-schwarz-lemma.md)

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

**The Schwarz--Christoffel theorem for an unbounded polygonal Jordan domain.** Formalized in Tau Ceti as [`TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_insert_infty`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/JordanPolygon.html#TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_insert_infty).

```lean
TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_insert_infty.{u_1}
  {ι : Type u_1} [Fintype ι] (e : ι → ℝ) (he : ∀ (i : ι), e i ∈ Set.Ioo (-1) 1)
  (z₀ : UpperHalfPlane) {β : ℝ} (hβ : β ∈ Set.Ioo 0 2) {U : Set ℂ} (hUo : IsOpen U)
  (hUc : IsConnected U)
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
    ∃ ρ c b, b ≠ 0 ∧ ∀ (z : ℂ), ρ < ‖z - c‖ → (z ∈ U ↔ |((z - c) / b).arg| < β * Real.pi / 2)) :
  ∃ a,
    Function.Injective a ∧
      ∃ A,
        A ≠ 0 ∧
          ∃ B,
            Set.BijOn (fun z => A * TauCeti.schwarzChristoffelPrimitive a e z₀ z + B)
                UpperHalfPlane.upperHalfPlaneSet U ∧
              ∀ (i : ι), A * TauCeti.schwarzChristoffelVertex a e z₀ i + B = v i
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_frontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/JordanPolygon.html#TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_frontier)
- [Source of `TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_frontier` in TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/JordanPolygon.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/JordanPolygon.lean#L109)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ConformalMapping/STATUS.md)
