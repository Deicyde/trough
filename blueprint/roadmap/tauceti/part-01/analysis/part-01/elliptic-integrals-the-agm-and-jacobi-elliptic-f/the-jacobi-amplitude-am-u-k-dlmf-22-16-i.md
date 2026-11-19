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
- [Source of `TauCeti.Real.jacobiAm` in TauCeti/Analysis/SpecialFunctions/JacobiElliptic/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/JacobiElliptic/Basic.lean#L62)
- [Tau Ceti roadmap status: Elliptic integrals, the AGM, and Jacobi elliptic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EllipticIntegrals/STATUS.md)
