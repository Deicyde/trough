---
declaration: def
origin: cited
lean: TauCeti.lowerConvexEnvelope
statement: formalized
---

# TauCeti.lowerConvexEnvelope

The lower convex envelope of a height sequence, as a total function. For an admissible
sequence it is the pointwise supremum of all convex minorants. For an inadmissible
sequence it is the all-infinite fallback, which is not an envelope of that sequence.

```lean
TauCeti.lowerConvexEnvelope (a : ℕ → WithTop ℝ) : ℕ → WithTop ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.lowerConvexEnvelope`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Sequence/Envelope.html#TauCeti.lowerConvexEnvelope).

## Sources

- [Tau Ceti documentation: `TauCeti.lowerConvexEnvelope`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Sequence/Envelope.html#TauCeti.lowerConvexEnvelope)
- [Source of `TauCeti.lowerConvexEnvelope` in TauCeti/Analysis/Convex/Sequence/Envelope.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Convex/Sequence/Envelope.lean#L165)
- [Tau Ceti roadmap status: Newton polygons of polynomials and power series](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NewtonPolygons/STATUS.md)
