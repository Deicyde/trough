---
declaration: def
origin: cited
lean: TauCeti.chebyshevTEnvelopeHilbertBasis
statement: formalized
---

# The Chebyshev envelope functions are a Hilbert basis of `L²((-1, 1]; dx)`

It is the
weight-in-the-function normalization, assembled from the same bridge as the weight-in-the-measure
basis `TauCeti.chebyshevTHilbertBasis`: orthonormality from the Chebyshev orthogonality relation,
completeness from moment determinacy applied to the exact-degree family `Tₙ`.

```lean
TauCeti.chebyshevTEnvelopeHilbertBasis.{u_1} (𝕜 : Type u_1) [RCLike 𝕜] :
  HilbertBasis ℕ 𝕜 ↥(MeasureTheory.Lp 𝕜 2 (MeasureTheory.volume.restrict (Set.Ioc (-1) 1)))
```

## Depends on

- [The weight ↔ measure isometry](the-weight-measure-isometry.md)
- [The weighted-measure basis](the-weighted-measure-basis.md)

## Proof depends on

- [Moment determinacy, exponential-moment form (the roadmap's B1 hypothesis)](moment-determinacy-exponential-moment-form-the-r.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.chebyshevTEnvelopeHilbertBasis`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/Envelope.html#TauCeti.chebyshevTEnvelopeHilbertBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.chebyshevTEnvelopeHilbertBasis`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/Envelope.html#TauCeti.chebyshevTEnvelopeHilbertBasis)
- [Source of `TauCeti.chebyshevTEnvelopeHilbertBasis` in TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/Envelope.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/Envelope.lean#L156)
- [Tau Ceti roadmap status: Weighted orthogonal L² bases — completeness, Hilbert-basis structure, and product bases of orthogonal systems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/OrthogonalL2Bases/STATUS.md)
