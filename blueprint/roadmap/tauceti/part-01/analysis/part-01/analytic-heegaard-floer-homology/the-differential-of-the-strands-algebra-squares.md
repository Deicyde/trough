---
declaration: theorem
origin: cited
lean: TauCeti.StrandsAlgebra.differential_differential
statement: formalized
proof: formalized
---

# The differential of the strands algebra squares to zero over a ring of characteristic two

```lean
TauCeti.StrandsAlgebra.differential_differential.{u_1, u_2} {R : Type u_1} {α : Type u_2}
  [CommSemiring R] [LinearOrder α] [Fintype α] [CharP R 2] (x : TauCeti.StrandsAlgebra R α) :
  (TauCeti.StrandsAlgebra.differential R α) ((TauCeti.StrandsAlgebra.differential R α) x) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.StrandsAlgebra.differential_differential`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/Bordered/StrandsAlgebra/Differential.html#TauCeti.StrandsAlgebra.differential_differential).

## Sources

- [Tau Ceti documentation: `TauCeti.StrandsAlgebra.differential_differential`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/Bordered/StrandsAlgebra/Differential.html#TauCeti.StrandsAlgebra.differential_differential)
- [Source of `TauCeti.StrandsAlgebra.differential_differential` in TauCeti/LowDimTopology/Bordered/StrandsAlgebra/Differential.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LowDimTopology/Bordered/StrandsAlgebra/Differential.lean#L551)
- [Tau Ceti roadmap status: Analytic Heegaard Floer homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HeegaardFloer/STATUS.md)
