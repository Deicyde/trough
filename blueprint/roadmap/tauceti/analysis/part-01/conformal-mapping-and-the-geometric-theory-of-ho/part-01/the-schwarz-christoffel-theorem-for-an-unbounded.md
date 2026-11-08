---
declaration: theorem
origin: cited
lean: TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_insert_infty
statement: formalized
proof: formalized
---

# The Schwarz--Christoffel theorem for an unbounded polygonal Jordan domain

Let `U` be a
connected open set whose frontier, together with the point at infinity, is a Jordan curve
of the Riemann sphere.  Suppose that `U` coincides near each frontier point other than the
distinct vertices `v i` with an open half-plane, near the vertex `v i` with the open sector of
opening `(e i + 1) * π` at `v i`, where `e i ∈ (-1, 1)`, and far from a point `c` with the open
sector `{|arg ((z - c) / b)| < β * π / 2}` of opening `β * π`, where `0 < β < 2`: so `U` has a
further vertex at infinity.  Then there are distinct real prevertices `a i` and constants `A ≠ 0`
and `B` such that `z ↦ A * F z + B` maps the upper half-plane bijectively onto `U`, where `F` is
the normalized Schwarz--Christoffel primitive for the prevertices `a` and the turning exponents
`e`, and such that the Schwarz--Christoffel vertex at `a i`, the limit of `F` at `a i`, is sent to
`v i`.  The prevertex of the vertex at infinity is the point at infinity of the half-plane.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Carathéodory's theorem for the inside of a Jordan curve](../../../part-02/complex/part-01/caratheodorys-theorem-for-the-inside-of-a-jordan.md)
- [Rouché's theorem for a disc, classical form](../part-02/rouches-theorem-for-a-disc-classical-form.md)
- [The Schwarz--Christoffel theorem for a bounded polygonal Jordan domain](the-schwarz-christoffel-theorem-for-a-bounded-po.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_insert_infty`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/JordanPolygon.html#TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_insert_infty).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_insert_infty`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/JordanPolygon.html#TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_insert_infty)
- [Source of `TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_insert_infty` in TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/JordanPolygon.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/JordanPolygon.lean#L154)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ConformalMapping/STATUS.md)
