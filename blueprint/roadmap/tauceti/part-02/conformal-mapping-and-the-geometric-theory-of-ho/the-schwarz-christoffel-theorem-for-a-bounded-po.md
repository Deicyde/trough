---
declaration: theorem
origin: cited
lean: TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_frontier
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

- [Rigidity of the pre-Schwarzian derivative](rigidity-of-the-pre-schwarzian-derivative.md)
- [Schwarz reflection principle (real axis)](schwarz-reflection-principle-real-axis.md)
- [TauCeti.Contour.homologyCauchyTheorem](../contour-integration-and-the-hungerbuhler-wasem-g/tauceti-contour-homologycauchytheorem.md)
- [TauCeti.Contour.windingNumber](../contour-integration-and-the-hungerbuhler-wasem-g/tauceti-contour-windingnumber.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_frontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/JordanPolygon.html#TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_frontier).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_frontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/JordanPolygon.html#TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_frontier)
- [Source of `TauCeti.exists_bijOn_const_mul_schwarzChristoffelPrimitive_add_of_isJordanCurve_frontier` in TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/JordanPolygon.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/JordanPolygon.lean#L108)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ConformalMapping/STATUS.md)
