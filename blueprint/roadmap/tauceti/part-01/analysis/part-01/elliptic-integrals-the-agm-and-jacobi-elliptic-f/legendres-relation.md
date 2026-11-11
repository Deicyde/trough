---
declaration: theorem
origin: cited
lean: TauCeti.Real.legendre_relation
statement: formalized
proof: formalized
---

# Legendre's relation

**Legendre's relation** between the complete first and second elliptic integrals at
complementary moduli (DLMF 19.7.1).

```lean
TauCeti.Real.legendre_relation {k : ℝ} (hk₀ : 0 < k) (hk₁ : k < 1) :
  TauCeti.Real.legendreEc k * TauCeti.Real.legendreK √(1 - k ^ 2) +
        TauCeti.Real.legendreEc √(1 - k ^ 2) * TauCeti.Real.legendreK k -
      TauCeti.Real.legendreK k * TauCeti.Real.legendreK √(1 - k ^ 2) =
    Real.pi / 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Real.legendre_relation`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Relation.html#TauCeti.Real.legendre_relation).

## Sources

- [Tau Ceti documentation: `TauCeti.Real.legendre_relation`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Relation.html#TauCeti.Real.legendre_relation)
- [Source of `TauCeti.Real.legendre_relation` in TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Relation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Relation.lean#L86)
- [Tau Ceti roadmap status: Elliptic integrals, the AGM, and Jacobi elliptic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EllipticIntegrals/STATUS.md)
