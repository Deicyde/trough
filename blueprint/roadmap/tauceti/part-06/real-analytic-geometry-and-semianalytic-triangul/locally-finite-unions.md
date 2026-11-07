---
declaration: theorem
origin: cited
lean: LocallyFinite.isSemianalytic_iUnion
statement: formalized
proof: formalized
---

# Locally finite unions

The union of a locally finite family of semianalytic sets is
semianalytic.

```lean
LocallyFinite.isSemianalytic_iUnion.{u_1, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {ι : Type u_3} {s : ι → Set E} (hfin : LocallyFinite s)
  (hs : ∀ (i : ι), TauCeti.IsSemianalytic (s i)) : TauCeti.IsSemianalytic (⋃ i, s i)
```

## Depends on

- [TauCeti.IsSemianalytic](tauceti-issemianalytic.md)

## Proof depends on

- [TauCeti.SemianalyticAt](tauceti-semianalyticat.md)

## Lean

Formalized in Tau Ceti as [`LocallyFinite.isSemianalytic_iUnion`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.html#LocallyFinite.isSemianalytic_iUnion).

## Sources

- [Tau Ceti documentation: `LocallyFinite.isSemianalytic_iUnion`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.html#LocallyFinite.isSemianalytic_iUnion)
- [Source of `LocallyFinite.isSemianalytic_iUnion` in TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.lean#L528)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
