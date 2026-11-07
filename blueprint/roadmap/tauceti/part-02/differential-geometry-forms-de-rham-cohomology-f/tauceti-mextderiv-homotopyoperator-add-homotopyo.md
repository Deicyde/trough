---
declaration: theorem
origin: cited
lean: TauCeti.mextDeriv_homotopyOperator_add_homotopyOperator_mextDeriv
statement: formalized
proof: formalized
---

# TauCeti.mextDeriv\_homotopyOperator\_add\_homotopyOperator\_mextDeriv

**The cochain-homotopy identity** for the homotopy operator on the cylinder `M × [0, 1]`:
for a `C¹` form `φ` with values in a Banach space on a `C²` manifold, possibly with boundary or
corners, `d (h φ) + h (d φ) = ι₁^* φ - ι₀^* φ`, where `ιₜ x = (x, t)`.

```lean
TauCeti.mextDeriv_homotopyOperator_add_homotopyOperator_mextDeriv.{u_1, u_2, u_3, u_4}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} {F : Type u_4} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M]
  [ChartedSpace H M] [NormedAddCommGroup F] [NormedSpace ℝ F] {k : ℕ} [IsManifold I 2 M]
  [CompleteSpace F]
  {φ :
    TauCeti.RoughForm (I.prod (modelWithCornersEuclideanHalfSpace 1)) (M × ↑(Set.Icc 0 1)) F
      (k + 1)}
  (hφ : TauCeti.IsSmoothForm (I.prod (modelWithCornersEuclideanHalfSpace 1)) 1 φ) (x₀ : M) :
  TauCeti.mextDeriv (TauCeti.homotopyOperator φ) x₀ +
      TauCeti.homotopyOperator (TauCeti.mextDeriv φ) x₀ =
    TauCeti.mpullback I (I.prod (modelWithCornersEuclideanHalfSpace 1)) (fun x => (x, 1)) φ x₀ -
      TauCeti.mpullback I (I.prod (modelWithCornersEuclideanHalfSpace 1)) (fun x => (x, 0)) φ x₀
```

## Depends on

- [TauCeti.homotopyOperator](tauceti-homotopyoperator.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mextDeriv_homotopyOperator_add_homotopyOperator_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/HomotopyOperator.html#TauCeti.mextDeriv_homotopyOperator_add_homotopyOperator_mextDeriv).

## Sources

- [Tau Ceti documentation: `TauCeti.mextDeriv_homotopyOperator_add_homotopyOperator_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/HomotopyOperator.html#TauCeti.mextDeriv_homotopyOperator_add_homotopyOperator_mextDeriv)
- [Source of `TauCeti.mextDeriv_homotopyOperator_add_homotopyOperator_mextDeriv` in TauCeti/Geometry/Manifold/DifferentialForm/HomotopyOperator.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DifferentialForm/HomotopyOperator.lean#L331)
- [Tau Ceti roadmap status: Differential geometry — forms, de Rham cohomology, flows, and degree](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
