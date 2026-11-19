---
declaration: structure
origin: cited
lean: TauCeti.InfiniteSlopeData
statement: formalized
---

# TauCeti.InfiniteSlopeData

The unit-slope presentation of a convex polygon whose finite domain is the half-line
`[start, ∞)`. The edge from `start + i` to `start + i + 1` has slope `slope i`. A terminal
ray is an eventually constant slope sequence; no slope is infinite.

```lean
TauCeti.InfiniteSlopeData.{u_3} (Γ : Type u_3) [Preorder Γ] : Type u_3
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.InfiniteSlopeData`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Sequence/SlopeData/Basic.html#TauCeti.InfiniteSlopeData).

## Sources

- [Tau Ceti documentation: `TauCeti.InfiniteSlopeData`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Sequence/SlopeData/Basic.html#TauCeti.InfiniteSlopeData)
- [Source of `TauCeti.InfiniteSlopeData` in TauCeti/Analysis/Convex/Sequence/SlopeData/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Convex/Sequence/SlopeData/Basic.lean#L220)
- [Tau Ceti roadmap status: Newton polygons of polynomials and power series](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NewtonPolygons/STATUS.md)
