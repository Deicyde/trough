---
declaration: theorem
origin: cited
lean: TauCeti.Toric.Fan.algebraicAnalyticEquiv_smul
statement: formalized
proof: formalized
---

# TauCeti.Toric.Fan.algebraicAnalyticEquiv\_smul

The algebraic–analytic comparison is equivariant for the coordinate-free complex torus.

```lean
TauCeti.Toric.Fan.algebraicAnalyticEquiv_smul {N V : Type} [AddCommGroup N] [AddCommGroup V]
  [_root_.Module ℝ V] {i : N →+ V} {Φ : TauCeti.Toric.Fan i} (hΦ : Φ.IsRegular)
  (t : TauCeti.Toric.ComplexTorus N) (p : Φ.AlgebraicComplexPoint) :
  (TauCeti.Toric.Fan.algebraicAnalyticEquiv hΦ) (t • p) =
    t • (TauCeti.Toric.Fan.algebraicAnalyticEquiv hΦ) p
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Toric.Fan.algebraicAnalyticEquiv_smul`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/Comparison/TorusAction.html#TauCeti.Toric.Fan.algebraicAnalyticEquiv_smul).

## Sources

- [Tau Ceti documentation: `TauCeti.Toric.Fan.algebraicAnalyticEquiv_smul`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/Comparison/TorusAction.html#TauCeti.Toric.Fan.algebraicAnalyticEquiv_smul)
- [Source of `TauCeti.Toric.Fan.algebraicAnalyticEquiv_smul` in TauCeti/Geometry/Toric/Analytic/Fan/Comparison/TorusAction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Toric/Analytic/Fan/Comparison/TorusAction.lean#L381)
- [Tau Ceti roadmap status: Analytic toric geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/AnalyticToricGeometry/STATUS.md)
