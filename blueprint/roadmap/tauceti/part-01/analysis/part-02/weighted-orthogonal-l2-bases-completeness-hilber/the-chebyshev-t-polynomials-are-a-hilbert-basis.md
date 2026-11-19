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

- [Moment determinacy, exponential-moment form](moment-determinacy-exponential-moment-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.chebyshevTHilbertBasis`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/HilbertBasis.html#TauCeti.chebyshevTHilbertBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.chebyshevTHilbertBasis`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/HilbertBasis.html#TauCeti.chebyshevTHilbertBasis)
- [Source of `TauCeti.chebyshevTHilbertBasis` in TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/HilbertBasis.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/HilbertBasis.lean#L85)
- [Tau Ceti roadmap status: Weighted orthogonal L² bases — completeness, Hilbert-basis structure, and product bases of orthogonal systems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/OrthogonalL2Bases/STATUS.md)
