---
declaration: theorem
origin: cited
lean: TauCeti.coeff_rayTorusWeightSeries
statement: formalized
proof: formalized
---

# Independent-component expansion

of the ray series: its `n`-th coefficient is the sum,
over all configurations `l` of total class `n • A₀` (the elements of
`s.weightedFinsuppAntidiag m n`), of the products of the local weights
`w_(σ c, i c)(l c)`.

```lean
TauCeti.coeff_rayTorusWeightSeries.{u_1} {ι : Type u_1} (s : Finset ι) (m : ι → ℕ+) (σ : ι → Bool)
  (i : ι → Fin 4) (n : ℕ) :
  (PowerSeries.coeff n) (TauCeti.rayTorusWeightSeries s m σ i) =
    ∑ l ∈ s.weightedFinsuppAntidiag m n, ∏ c ∈ s, TauCeti.torusWeight (σ c) (i c) (l c)
```

## Depends on

- [TauCeti.torusWeightSeries](tauceti-torusweightseries.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.coeff_rayTorusWeightSeries`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/TorusWeight.html#TauCeti.coeff_rayTorusWeightSeries).

## Sources

- [Tau Ceti documentation: `TauCeti.coeff_rayTorusWeightSeries`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/TorusWeight.html#TauCeti.coeff_rayTorusWeightSeries)
- [Source of `TauCeti.coeff_rayTorusWeightSeries` in TauCeti/Geometry/Symplectic/JHolomorphic/TorusWeight.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/JHolomorphic/TorusWeight.lean#L349)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TaubesGromov/STATUS.md)
