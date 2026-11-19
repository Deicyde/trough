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
- [Moment determinacy, exponential-moment form](moment-determinacy-exponential-moment-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hasSum_chebyshevT_expansion`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/Parseval.html#TauCeti.hasSum_chebyshevT_expansion).

## Sources

- [Tau Ceti documentation: `TauCeti.hasSum_chebyshevT_expansion`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/Parseval.html#TauCeti.hasSum_chebyshevT_expansion)
- [Source of `TauCeti.hasSum_chebyshevT_expansion` in TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/Parseval.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/Parseval.lean#L74)
- [Tau Ceti roadmap status: Weighted orthogonal L² bases — completeness, Hilbert-basis structure, and product bases of orthogonal systems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/OrthogonalL2Bases/STATUS.md)
