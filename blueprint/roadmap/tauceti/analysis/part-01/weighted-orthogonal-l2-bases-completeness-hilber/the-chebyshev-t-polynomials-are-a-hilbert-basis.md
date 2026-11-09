---
declaration: def
origin: cited
lean: TauCeti.chebyshevTHilbertBasis
statement: formalized
---

# The Chebyshev `T` polynomials are a Hilbert basis of `L²(measureT)`

Orthonormality is
`orthonormal_normalizedChebyshevTLp`; completeness is
`orthogonal_span_normalizedChebyshevTLp_eq_bot`.

```lean
TauCeti.chebyshevTHilbertBasis.{u_1} (𝕜 : Type u_1) [RCLike 𝕜] :
  HilbertBasis ℕ 𝕜 ↥(MeasureTheory.Lp 𝕜 2 Polynomial.Chebyshev.measureT)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Moment determinacy, exponential-moment form (the roadmap's B1 hypothesis)](moment-determinacy-exponential-moment-form-the-r.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.chebyshevTHilbertBasis`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/HilbertBasis.html#TauCeti.chebyshevTHilbertBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.chebyshevTHilbertBasis`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/HilbertBasis.html#TauCeti.chebyshevTHilbertBasis)
- [Source of `TauCeti.chebyshevTHilbertBasis` in TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/HilbertBasis.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/HilbertBasis.lean#L85)
- [Tau Ceti roadmap status: Weighted orthogonal L² bases — completeness, Hilbert-basis structure, and product bases of orthogonal systems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/OrthogonalL2Bases/STATUS.md)
