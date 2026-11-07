---
declaration: theorem
origin: cited
lean: TauCeti.hasSum_chebyshevT_expansion
statement: formalized
proof: formalized
---

# The Chebyshev expansion

Every `f ∈ L²(measureT)` is the sum of its normalized
Chebyshev-polynomial series.

```lean
TauCeti.hasSum_chebyshevT_expansion.{u_1} {𝕜 : Type u_1} [RCLike 𝕜]
  (f : ↥(MeasureTheory.Lp 𝕜 2 Polynomial.Chebyshev.measureT)) :
  HasSum
    (fun n =>
      (∫ (x : ℝ),
          (algebraMap ℝ 𝕜) (TauCeti.normalizedChebyshevT n x) *
            ↑↑f x ∂Polynomial.Chebyshev.measureT) •
        TauCeti.normalizedChebyshevTLp 𝕜 n)
    f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Chebyshev `T` polynomials are a Hilbert basis of `L²(measureT)`](the-chebyshev-t-polynomials-are-a-hilbert-basis.md)
- [Moment determinacy, exponential-moment form (the roadmap's B1 hypothesis)](moment-determinacy-exponential-moment-form-the-r.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hasSum_chebyshevT_expansion`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/Parseval.html#TauCeti.hasSum_chebyshevT_expansion).

## Sources

- [Tau Ceti documentation: `TauCeti.hasSum_chebyshevT_expansion`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/Parseval.html#TauCeti.hasSum_chebyshevT_expansion)
- [Source of `TauCeti.hasSum_chebyshevT_expansion` in TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/Parseval.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/Parseval.lean#L74)
- [Tau Ceti roadmap status: Weighted orthogonal L² bases — completeness, Hilbert-basis structure, and product bases of orthogonal systems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/OrthogonalL2Bases/STATUS.md)
