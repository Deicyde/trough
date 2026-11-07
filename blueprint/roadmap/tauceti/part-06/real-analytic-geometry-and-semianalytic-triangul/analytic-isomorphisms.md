---
declaration: theorem
origin: cited
lean: Equiv.isSemianalytic_image_iff
statement: formalized
proof: formalized
---

# Analytic isomorphisms

For a bijection `e` that is analytic with analytic inverse, the
image `e '' s` is semianalytic if and only if `s` is semianalytic.

```lean
Equiv.isSemianalytic_image_iff.{u_1, u_2} {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] {s : Set E} (e : E ≃ F)
  (he : AnalyticOnNhd ℝ (⇑e) Set.univ) (he' : AnalyticOnNhd ℝ (⇑e.symm) Set.univ) :
  TauCeti.IsSemianalytic (⇑e '' s) ↔ TauCeti.IsSemianalytic s
```

## Depends on

- [TauCeti.IsSemianalytic](tauceti-issemianalytic.md)

## Proof depends on

- [Analytic preimages](analytic-preimages.md)

## Lean

Formalized in Tau Ceti as [`Equiv.isSemianalytic_image_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.html#Equiv.isSemianalytic_image_iff).

## Sources

- [Tau Ceti documentation: `Equiv.isSemianalytic_image_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.html#Equiv.isSemianalytic_image_iff)
- [Source of `Equiv.isSemianalytic_image_iff` in TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.lean#L561)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
