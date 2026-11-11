---
declaration: theorem
origin: cited
lean: TauCeti.OrientedPDCode.enhancedStateSum_eq_mul_eval₂_jonesPolynomial
statement: formalized
proof: formalized
---

# The enhanced state sum of a nonempty diagram is `(q + q⁻¹)` times its Jones polynomial at `t ^ (1/2) = -q`

The hypothesis `0 < componentCount` says that the diagram is nonempty; it
excludes the empty diagram, whose enhanced state sum is `1`.

```lean
TauCeti.OrientedPDCode.enhancedStateSum_eq_mul_eval₂_jonesPolynomial {n : ℕ}
  (D : TauCeti.OrientedPDCode n) (h : 0 < D.componentCount) :
  D.enhancedStateSum =
    (LaurentPolynomial.T 1 + LaurentPolynomial.T (-1)) *
      (LaurentPolynomial.eval₂ (Int.castRingHom (LaurentPolynomial ℤ))
          (-LaurentPolynomial.genericUnit ℤ))
        D.jonesPolynomial
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.OrientedPDCode.enhancedStateSum_eq_mul_eval₂_jonesPolynomial`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/EnhancedState.html#TauCeti.OrientedPDCode.enhancedStateSum_eq_mul_eval%E2%82%82_jonesPolynomial).

## Sources

- [Tau Ceti documentation: `TauCeti.OrientedPDCode.enhancedStateSum_eq_mul_eval₂_jonesPolynomial`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/EnhancedState.html#TauCeti.OrientedPDCode.enhancedStateSum_eq_mul_eval%E2%82%82_jonesPolynomial)
- [Source of `TauCeti.OrientedPDCode.enhancedStateSum_eq_mul_eval₂_jonesPolynomial` in TauCeti/KnotTheory/Khovanov/EnhancedState.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/KnotTheory/Khovanov/EnhancedState.lean#L266)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/KhovanovHomology/STATUS.md)
