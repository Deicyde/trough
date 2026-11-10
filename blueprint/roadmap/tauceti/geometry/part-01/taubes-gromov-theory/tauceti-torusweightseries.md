---
declaration: def
origin: cited
lean: TauCeti.torusWeightSeries
statement: formalized
---

# TauCeti.torusWeightSeries

The local multiplicity series `f_(σ, i) ∈ ℤ⟦X⟧` attached to an embedded square-zero
pseudoholomorphic torus with determinant sign `σ` (`true` for `+`, `false` for `-`) and with
`i` negative signs among its three nontrivially twisted normal operators. The positive series
are `1 / (1 - X)`, `1 + X`, `(1 + X) / (1 + X ^ 2)` and `(1 + X) (1 - X ^ 2) / (1 + X ^ 2)`,
and each negative series is the inverse of the positive series with the same index. The weight
of the torus with multiplicity `m` is the coefficient `coeff m (torusWeightSeries σ i)`.

```lean
TauCeti.torusWeightSeries (σ : Bool) (i : Fin 4) : PowerSeries ℤ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.torusWeightSeries`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/TorusWeight.html#TauCeti.torusWeightSeries).

## Sources

- [Tau Ceti documentation: `TauCeti.torusWeightSeries`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/TorusWeight.html#TauCeti.torusWeightSeries)
- [Source of `TauCeti.torusWeightSeries` in TauCeti/Geometry/Symplectic/JHolomorphic/TorusWeight.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/JHolomorphic/TorusWeight.lean#L99)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TaubesGromov/STATUS.md)
