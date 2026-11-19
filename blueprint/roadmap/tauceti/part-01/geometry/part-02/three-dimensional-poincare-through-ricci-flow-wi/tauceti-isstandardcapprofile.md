---
declaration: structure
origin: cited
lean: TauCeti.IsStandardCapProfile
statement: formalized
---

# TauCeti.IsStandardCapProfile

A *standard cap profile*: a function `f` for which `dr² + f(r)² g_(S²)` is the standard cap
metric on `ℝ³`. It is smooth and odd on `ℝ` (the odd smooth extension across the tip), concave on
`[0, ∞)`, equal to `2 sin (r / 2)` on some interval `[0, r₀)` (a round tip of sectional curvature
`1 / 4`), and equal to `√2` beyond some radius (a round cylinder of scalar curvature one).

```lean
TauCeti.IsStandardCapProfile (f : ℝ → ℝ) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsStandardCapProfile`](https://taucetiproject.org/docs/TauCeti/Geometry/RicciFlow/StandardCap/Profile.html#TauCeti.IsStandardCapProfile).

## Sources

- [Tau Ceti documentation: `TauCeti.IsStandardCapProfile`](https://taucetiproject.org/docs/TauCeti/Geometry/RicciFlow/StandardCap/Profile.html#TauCeti.IsStandardCapProfile)
- [Source of `TauCeti.IsStandardCapProfile` in TauCeti/Geometry/RicciFlow/StandardCap/Profile.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/RicciFlow/StandardCap/Profile.lean#L83)
- [Tau Ceti roadmap status: Three-dimensional Poincaré through Ricci flow with surgery](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Poincare3D/STATUS.md)
