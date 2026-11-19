---
declaration: theorem
origin: cited
lean: TauCeti.Compactification.isIso_denseReplacementBaseChange_iff
statement: formalized
proof: formalized
---

# TauCeti.Compactification.isIso_denseReplacementBaseChange_iff

The dense-replacement comparison is invertible exactly when the base change of the
original dense replacement still has schematically dense interior.

```lean
TauCeti.Compactification.isIso_denseReplacementBaseChange_iff.{u} {X S T : AlgebraicGeometry.Scheme}
  {f : X ⟶ S} (C : TauCeti.Compactification f) (g : T ⟶ S) :
  CategoryTheory.IsIso (C.denseReplacementBaseChange g) ↔
    AlgebraicGeometry.IsSchemeTheoreticallyDominant (C.denseReplacement.obj.baseChange g).j
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Compactification.isIso_denseReplacementBaseChange_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Compactification/DenseReplacement/Basic.html#TauCeti.Compactification.isIso_denseReplacementBaseChange_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Compactification.isIso_denseReplacementBaseChange_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Compactification/DenseReplacement/Basic.html#TauCeti.Compactification.isIso_denseReplacementBaseChange_iff)
- [Source of `TauCeti.Compactification.isIso_denseReplacementBaseChange_iff` in TauCeti/AlgebraicGeometry/Compactification/DenseReplacement/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Compactification/DenseReplacement/Basic.lean#L215)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
