---
declaration: theorem
origin: cited
lean: TauCeti.Toric.Fan.algebraicAnalyticEquiv_smul
statement: formalized
proof: formalized
---

# TauCeti.Toric.Fan.algebraicAnalyticEquiv_smul

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

## Proof depends on

- [Gordan's lemma](../../part-02/other-results/gordans-lemma.md)
- [Tucker's theorem](../../part-02/convex/tuckers-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Toric.Fan.algebraicAnalyticEquiv_smul`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/Comparison/TorusAction.html#TauCeti.Toric.Fan.algebraicAnalyticEquiv_smul).

## Sources

- [Tau Ceti documentation: `TauCeti.Toric.Fan.algebraicAnalyticEquiv_smul`](https://taucetiproject.org/docs/TauCeti/Geometry/Toric/Analytic/Fan/Comparison/TorusAction.html#TauCeti.Toric.Fan.algebraicAnalyticEquiv_smul)
- [Source of `TauCeti.Toric.Fan.algebraicAnalyticEquiv_smul` in TauCeti/Geometry/Toric/Analytic/Fan/Comparison/TorusAction.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Toric/Analytic/Fan/Comparison/TorusAction.lean#L381)
- [Tau Ceti roadmap status: Analytic toric geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AnalyticToricGeometry/STATUS.md)
