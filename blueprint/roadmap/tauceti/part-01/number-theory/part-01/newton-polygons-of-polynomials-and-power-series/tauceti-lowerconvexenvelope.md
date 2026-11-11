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
- [Source of `TauCeti.lowerConvexEnvelope` in TauCeti/Analysis/Convex/Sequence/Envelope.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Convex/Sequence/Envelope.lean#L164)
- [Tau Ceti roadmap status: Newton polygons of polynomials and power series](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NewtonPolygons/STATUS.md)
