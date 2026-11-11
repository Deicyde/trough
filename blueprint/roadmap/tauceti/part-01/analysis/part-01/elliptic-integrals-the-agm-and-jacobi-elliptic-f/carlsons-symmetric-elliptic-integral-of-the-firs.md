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
- [Source of `Complex.carlsonRF` in TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Carlson/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Carlson/Basic.lean#L86)
- [Tau Ceti roadmap status: Elliptic integrals, the AGM, and Jacobi elliptic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EllipticIntegrals/STATUS.md)
