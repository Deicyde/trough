---
declaration: theorem
origin: cited
lean: TauCeti.pathIntegral_mextDeriv
statement: formalized
proof: formalized
---

# TauCeti.pathIntegral\_mextDeriv

**The fundamental theorem of calculus for line integrals**, for a `C¹` form `ψ` of degree
zero: the line integral of `dψ` along a `C¹` curve is the difference of the values of `ψ` at the
endpoints.

```lean
TauCeti.pathIntegral_mextDeriv.{u_1, u_2, u_3, u_4} {E : Type u_1} {H : Type u_2} {M : Type u_3}
  {F : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [NormedAddCommGroup F]
  [NormedSpace ℝ F] [CompleteSpace F] [IsManifold I 1 M] {ψ : TauCeti.RoughForm I M F 0}
  (hψ : TauCeti.IsSmoothForm I 1 ψ) {γ : ℝ → M} (hγ : ContMDiff (modelWithCornersSelf ℝ ℝ) I 1 γ)
  (a b : ℝ) : TauCeti.pathIntegral (TauCeti.mextDeriv ψ) γ a b = (ψ (γ b)) 0 - (ψ (γ a)) 0
```

## Depends on

- [TauCeti.pathIntegral](tauceti-pathintegral.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.pathIntegral_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Path.html#TauCeti.pathIntegral_mextDeriv).

## Sources

- [Tau Ceti documentation: `TauCeti.pathIntegral_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Path.html#TauCeti.pathIntegral_mextDeriv)
- [Source of `TauCeti.pathIntegral_mextDeriv` in TauCeti/Geometry/Manifold/DifferentialForm/Integration/Path.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Path.lean#L370)
- [Tau Ceti roadmap status: Differential geometry — forms, de Rham cohomology, flows, and degree](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
