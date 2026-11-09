---
declaration: theorem
origin: cited
lean: TauCeti.CotangentBundle.inChartAt_symplecticForm_apply
statement: formalized
proof: formalized
---

# Chart formula for the canonical symplectic form

In every preferred chart of the cotangent
bundle, the canonical symplectic form is the linear form
`TauCeti.strongDualCotangentSymplecticForm`, `ω((δq, δp), (δq', δp')) = δp'(δq) - δp(δq')`.

```lean
TauCeti.CotangentBundle.inChartAt_symplecticForm_apply.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  (z₀ : TauCeti.CotangentBundle I M) {w : E × (E →L[ℝ] ℝ)}
  (hw : w ∈ (extChartAt (I.prod (modelWithCornersSelf ℝ (E →L[ℝ] ℝ))) z₀).target)
  (v : Fin 2 → E × (E →L[ℝ] ℝ)) :
  (TauCeti.RoughForm.inChartAt (↑(TauCeti.CotangentBundle.symplecticForm I M)) z₀ w) v =
    (fun v w => (TauCeti.strongDualCotangentSymplecticForm.toBilinForm v) w) (v 0) (v 1)
```

## Depends on

- [TauCeti.CotangentBundle](tauceti-cotangentbundle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CotangentBundle.inChartAt_symplecticForm_apply`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Liouville.html#TauCeti.CotangentBundle.inChartAt_symplecticForm_apply).

## Sources

- [Tau Ceti documentation: `TauCeti.CotangentBundle.inChartAt_symplecticForm_apply`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Liouville.html#TauCeti.CotangentBundle.inChartAt_symplecticForm_apply)
- [Source of `TauCeti.CotangentBundle.inChartAt_symplecticForm_apply` in TauCeti/Geometry/Symplectic/Cotangent/Bundle/Liouville.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Cotangent/Bundle/Liouville.lean#L293)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
