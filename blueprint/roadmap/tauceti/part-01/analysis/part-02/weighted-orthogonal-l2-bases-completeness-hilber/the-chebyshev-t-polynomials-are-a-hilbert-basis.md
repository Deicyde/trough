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
- [Source of `TauCeti.chebyshevTHilbertBasis` in TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/HilbertBasis.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/HilbertBasis.lean#L85)
- [Tau Ceti roadmap status: Weighted orthogonal L² bases — completeness, Hilbert-basis structure, and product bases of orthogonal systems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/OrthogonalL2Bases/STATUS.md)
