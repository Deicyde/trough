---
declaration: structure
origin: cited
lean: TauCeti.FiniteSlopeData
statement: formalized
---

# TauCeti.FiniteSlopeData

The unit-slope presentation of a nonempty convex polygon with finite domain
`[start, start + length]`. The edge from `start + i` to `start + i + 1` has slope `slope i`.
Length zero represents a singleton polygon and carries no slopes.

```lean
TauCeti.FiniteSlopeData.{u_3} (Γ : Type u_3) [Preorder Γ] : Type u_3
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteSlopeData`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Sequence/SlopeData/Basic.html#TauCeti.FiniteSlopeData).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteSlopeData`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Sequence/SlopeData/Basic.html#TauCeti.FiniteSlopeData)
- [Source of `TauCeti.FiniteSlopeData` in TauCeti/Analysis/Convex/Sequence/SlopeData/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Convex/Sequence/SlopeData/Basic.lean#L66)
- [Tau Ceti roadmap status: Newton polygons of polynomials and power series](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NewtonPolygons/STATUS.md)
