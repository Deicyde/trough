---
declaration: theorem
origin: cited
lean: TauCeti.LaurentCover.exact_moduleAugmentation_moduleDiff
statement: formalized
proof: formalized
---

# TauCeti.LaurentCover.exact_moduleAugmentation_moduleDiff

The kernel of the module Laurent differential is exactly the image of the module
augmentation; `M` need not be flat or finite.

```lean
TauCeti.LaurentCover.exact_moduleAugmentation_moduleDiff.{u_1, u_2} {A : Type u_1}
  [NormedCommRing A] [IsUltrametricDist A] (M : Type u_2) [AddCommGroup M] [_root_.Module A M]
  [CompleteSpace A] (f : A) :
  Function.Exact ⇑(TauCeti.LaurentCover.moduleAugmentation M f)
    ⇑(TauCeti.LaurentCover.moduleDiff M f)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LaurentCover.exact_moduleAugmentation_moduleDiff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Rigid/Affinoid/LaurentCover/Module.html#TauCeti.LaurentCover.exact_moduleAugmentation_moduleDiff).

## Sources

- [Tau Ceti documentation: `TauCeti.LaurentCover.exact_moduleAugmentation_moduleDiff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Rigid/Affinoid/LaurentCover/Module.html#TauCeti.LaurentCover.exact_moduleAugmentation_moduleDiff)
- [Source of `TauCeti.LaurentCover.exact_moduleAugmentation_moduleDiff` in TauCeti/AlgebraicGeometry/Rigid/Affinoid/LaurentCover/Module.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Rigid/Affinoid/LaurentCover/Module.lean#L107)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
