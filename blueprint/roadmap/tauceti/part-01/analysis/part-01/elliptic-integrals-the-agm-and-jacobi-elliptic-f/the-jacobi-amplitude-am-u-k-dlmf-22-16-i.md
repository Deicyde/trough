---
declaration: def
origin: cited
lean: TauCeti.Real.jacobiAm
statement: formalized
---

# The Jacobi amplitude `am(u, k)` (DLMF §22.16(i))

for `k ^ 2 < 1`, the inverse of the
integral of the first kind `φ ↦ F(φ, k)`, so that `F(am(u, k), k) = u`. For `k ^ 2 ≥ 1` it is the
junk value `id`.

```lean
TauCeti.Real.jacobiAm (k : ℝ) : ℝ → ℝ
```

## Depends on

- [TauCeti.Real.legendreFOrderIso](tauceti-real-legendreforderiso.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Real.jacobiAm`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/JacobiElliptic/Basic.html#TauCeti.Real.jacobiAm).

## Sources

- [Tau Ceti documentation: `TauCeti.Real.jacobiAm`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/JacobiElliptic/Basic.html#TauCeti.Real.jacobiAm)
- [Source of `TauCeti.Real.jacobiAm` in TauCeti/Analysis/SpecialFunctions/JacobiElliptic/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/JacobiElliptic/Basic.lean#L62)
- [Tau Ceti roadmap status: Elliptic integrals, the AGM, and Jacobi elliptic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EllipticIntegrals/STATUS.md)
