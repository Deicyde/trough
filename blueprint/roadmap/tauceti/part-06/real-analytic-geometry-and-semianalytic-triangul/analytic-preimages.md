---
declaration: theorem
origin: cited
lean: TauCeti.IsSemianalytic.preimage
statement: formalized
proof: formalized
---

# Analytic preimages

The preimage of a semianalytic set under a real analytic map is
semianalytic.

```lean
TauCeti.IsSemianalytic.preimage.{u_1, u_2} {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] {s : Set F}
  (hs : TauCeti.IsSemianalytic s) {g : E → F} (hg : AnalyticOnNhd ℝ g Set.univ) :
  TauCeti.IsSemianalytic (g ⁻¹' s)
```

## Depends on

- [TauCeti.IsSemianalytic](tauceti-issemianalytic.md)

## Proof depends on

- [TauCeti.SemianalyticAt](tauceti-semianalyticat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsSemianalytic.preimage`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.html#TauCeti.IsSemianalytic.preimage).

## Sources

- [Tau Ceti documentation: `TauCeti.IsSemianalytic.preimage`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.html#TauCeti.IsSemianalytic.preimage)
- [Source of `TauCeti.IsSemianalytic.preimage` in TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.lean#L515)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
