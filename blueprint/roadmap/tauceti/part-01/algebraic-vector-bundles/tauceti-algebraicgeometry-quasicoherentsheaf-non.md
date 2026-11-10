---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.QuasicoherentSheaf.nonempty_hasLeftDual_iff_isFiniteLocallyFree
statement: formalized
proof: formalized
---

# TauCeti.AlgebraicGeometry.QuasicoherentSheaf.nonempty_hasLeftDual_iff_isFiniteLocallyFree

A quasicoherent sheaf on any scheme has a left dual in `QuasicoherentSheaf X` if and only
if it is finite locally free.

```lean
TauCeti.AlgebraicGeometry.QuasicoherentSheaf.nonempty_hasLeftDual_iff_isFiniteLocallyFree.{u}
  {X : AlgebraicGeometry.Scheme} (E : TauCeti.AlgebraicGeometry.QuasicoherentSheaf X) :
  Nonempty (CategoryTheory.HasLeftDual E) ↔
    AlgebraicGeometry.Scheme.Modules.isFiniteLocallyFree X E.obj
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf](tauceti-algebraicgeometry-finitelocallyfreesheaf-3.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.QuasicoherentSheaf.nonempty_hasLeftDual_iff_isFiniteLocallyFree`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/VectorBundle/Dual/Dualizable.html#TauCeti.AlgebraicGeometry.QuasicoherentSheaf.nonempty_hasLeftDual_iff_isFiniteLocallyFree).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.QuasicoherentSheaf.nonempty_hasLeftDual_iff_isFiniteLocallyFree`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/VectorBundle/Dual/Dualizable.html#TauCeti.AlgebraicGeometry.QuasicoherentSheaf.nonempty_hasLeftDual_iff_isFiniteLocallyFree)
- [Source of `TauCeti.AlgebraicGeometry.QuasicoherentSheaf.nonempty_hasLeftDual_iff_isFiniteLocallyFree` in TauCeti/AlgebraicGeometry/VectorBundle/Dual/Dualizable.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/VectorBundle/Dual/Dualizable.lean#L70)
- [Tau Ceti roadmap status: Algebraic vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicVectorBundles/STATUS.md)
