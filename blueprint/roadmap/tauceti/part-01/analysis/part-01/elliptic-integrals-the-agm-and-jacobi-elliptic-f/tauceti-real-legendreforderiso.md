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
- [Source of `TauCeti.Real.legendreFOrderIso` in TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Legendre.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Legendre.lean#L332)
- [Tau Ceti roadmap status: Elliptic integrals, the AGM, and Jacobi elliptic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EllipticIntegrals/STATUS.md)
