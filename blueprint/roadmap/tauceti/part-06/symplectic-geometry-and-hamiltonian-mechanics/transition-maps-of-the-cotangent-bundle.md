---
declaration: theorem
origin: cited
lean: TauCeti.CotangentBundle.extChartAt_extChartAt_symm
statement: formalized
proof: formalized
---

# Transition maps of the cotangent bundle

Changing from the preferred chart at `z₀` to the
preferred chart at `z₁` sends `(q, p)` to `(φ q, p ∘ (dφ_q)⁻¹)`, where `φ` is the change of base
charts; `(dφ_q)⁻¹` is the derivative of the inverse change of charts at `φ q`.

```lean
TauCeti.CotangentBundle.extChartAt_extChartAt_symm.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1}
  {E : Type u_2} {H : Type u_3} [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [TopologicalSpace H] {I : ModelWithCorners 𝕜 E H} {M : Type u_4} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I 1 M] (z₀ z₁ : TauCeti.CotangentBundle I M) {q : E}
  (p : E →L[𝕜] 𝕜) (hq : q ∈ (extChartAt I z₀.proj).target)
  (hq₁ : ↑(extChartAt I z₀.proj).symm q ∈ (extChartAt I z₁.proj).source) :
  ↑(extChartAt (I.prod (modelWithCornersSelf 𝕜 (E →L[𝕜] 𝕜))) z₁)
      (↑(extChartAt (I.prod (modelWithCornersSelf 𝕜 (E →L[𝕜] 𝕜))) z₀).symm (q, p)) =
    ((↑(extChartAt I z₁.proj) ∘ ↑(extChartAt I z₀.proj).symm) q,
      p ∘SL
        fderivWithin 𝕜 (↑(extChartAt I z₀.proj) ∘ ↑(extChartAt I z₁.proj).symm) (Set.range ↑I)
          ((↑(extChartAt I z₁.proj) ∘ ↑(extChartAt I z₀.proj).symm) q))
```

## Depends on

- [TauCeti.CotangentBundle](tauceti-cotangentbundle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CotangentBundle.extChartAt_extChartAt_symm`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/Cotangent/Basic.html#TauCeti.CotangentBundle.extChartAt_extChartAt_symm).

## Sources

- [Tau Ceti documentation: `TauCeti.CotangentBundle.extChartAt_extChartAt_symm`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/Cotangent/Basic.html#TauCeti.CotangentBundle.extChartAt_extChartAt_symm)
- [Source of `TauCeti.CotangentBundle.extChartAt_extChartAt_symm` in TauCeti/Geometry/Manifold/VectorBundle/Cotangent/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/VectorBundle/Cotangent/Basic.lean#L123)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
