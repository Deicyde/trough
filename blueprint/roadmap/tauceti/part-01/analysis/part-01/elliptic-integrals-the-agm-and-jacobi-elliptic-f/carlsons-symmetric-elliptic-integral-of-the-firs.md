---
declaration: def
origin: cited
lean: Complex.carlsonRF
statement: formalized
---

# Carlson's symmetric elliptic integral of the first kind (DLMF 19.16.1)

`R_F(x, y, z) = ½ ∫₀^∞ (t + x)^(-1/2) (t + y)^(-1/2) (t + z)^(-1/2) dt`, with principal complex
powers of each factor.

The integral converges when `x, y, z ∈ slitPlane ∪ {0}` with at most one of them `0`
(`integrableOn_carlsonRF_integrand`); its behavior outside this domain is not characterized here.
Where the integrand is not integrable, the value is the totalized junk value `0`.

```lean
Complex.carlsonRF (x y z : ℂ) : ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Complex.carlsonRF`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Carlson/Basic.html#Complex.carlsonRF).

## Sources

- [Tau Ceti documentation: `Complex.carlsonRF`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Carlson/Basic.html#Complex.carlsonRF)
- [Source of `Complex.carlsonRF` in TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Carlson/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Carlson/Basic.lean#L86)
- [Tau Ceti roadmap status: Elliptic integrals, the AGM, and Jacobi elliptic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EllipticIntegrals/STATUS.md)
