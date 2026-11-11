---
declaration: def
origin: cited
lean: TauCeti.Real.legendreFOrderIso
statement: formalized
---

# TauCeti.Real.legendreFOrderIso

For `k ^ 2 < 1`, the integral of the first kind `φ ↦ F(φ, k)` as an order isomorphism of `ℝ`.
Its inverse is the Jacobi amplitude `u ↦ am(u, k)`.

```lean
TauCeti.Real.legendreFOrderIso {k : ℝ} (hk : k ^ 2 < 1) : ℝ ≃o ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Real.legendreFOrderIso`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Legendre.html#TauCeti.Real.legendreFOrderIso).

## Sources

- [Tau Ceti documentation: `TauCeti.Real.legendreFOrderIso`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Legendre.html#TauCeti.Real.legendreFOrderIso)
- [Source of `TauCeti.Real.legendreFOrderIso` in TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Legendre.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Legendre.lean#L334)
- [Tau Ceti roadmap status: Elliptic integrals, the AGM, and Jacobi elliptic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EllipticIntegrals/STATUS.md)
