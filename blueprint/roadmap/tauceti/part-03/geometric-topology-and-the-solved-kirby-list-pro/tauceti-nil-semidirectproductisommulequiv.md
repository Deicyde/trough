---
declaration: def
origin: cited
lean: TauCeti.Nil.semidirectProductIsomMulEquiv
statement: formalized
---

# TauCeti.Nil.semidirectProductIsomMulEquiv

The full Riemannian isometry group of Nil is `Nil ⋊ O(2)`, with its canonical
translation and orthogonal actions. This is an isomorphism of groups.

```lean
TauCeti.Nil.semidirectProductIsomMulEquiv :
  TauCeti.Nil ⋊[TauCeti.Nil.orthogonalMulAut] ↥(Matrix.orthogonalGroup (Fin 2) ℝ) ≃*
    TauCeti.Isom (modelWithCornersSelf ℝ (ℝ × ℝ × ℝ)) TauCeti.Nil
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.Manifold.riemannianExp](../geodesics-the-exponential-map-and-the-hopf-rinow/tauceti-manifold-riemannianexp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Nil.semidirectProductIsomMulEquiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Nil/Stabilizer.html#TauCeti.Nil.semidirectProductIsomMulEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.Nil.semidirectProductIsomMulEquiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Nil/Stabilizer.html#TauCeti.Nil.semidirectProductIsomMulEquiv)
- [Source of `TauCeti.Nil.semidirectProductIsomMulEquiv` in TauCeti/Geometry/Manifold/Riemannian/Nil/Stabilizer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Riemannian/Nil/Stabilizer.lean#L256)
- [Tau Ceti roadmap status: Geometric topology and the solved Kirby-list problems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricTopology/STATUS.md)
