---
declaration: theorem
origin: cited
lean: TauCeti.Dagger.washnitzerAlgebra.norm_toTate_hasseDeriv_le
statement: formalized
proof: formalized
---

# The Cauchy estimate at unit radius

Hasse derivatives do not increase the Gauss norm of an
overconvergent series.

```lean
TauCeti.Dagger.washnitzerAlgebra.norm_toTate_hasseDeriv_le.{u_1, u_2} {σ : Type u_1} {R : Type u_2}
  [NormedCommRing R] [IsUltrametricDist R] (d : σ →₀ ℕ)
  (f : ↥(TauCeti.Dagger.washnitzerAlgebra σ R)) :
  ‖(TauCeti.Dagger.washnitzerAlgebra.toTate σ R)
        ((TauCeti.Dagger.washnitzerAlgebra.hasseDeriv σ R d) f)‖ ≤
    ‖(TauCeti.Dagger.washnitzerAlgebra.toTate σ R) f‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cauchy estimate for partial derivatives](../../../part-01/restricted-power-series-and-tate-algebras/part-01/the-cauchy-estimate-for-partial-derivatives.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.washnitzerAlgebra.norm_toTate_hasseDeriv_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Derivative.html#TauCeti.Dagger.washnitzerAlgebra.norm_toTate_hasseDeriv_le).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.washnitzerAlgebra.norm_toTate_hasseDeriv_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Derivative.html#TauCeti.Dagger.washnitzerAlgebra.norm_toTate_hasseDeriv_le)
- [Source of `TauCeti.Dagger.washnitzerAlgebra.norm_toTate_hasseDeriv_le` in TauCeti/RingTheory/Dagger/Derivative.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Dagger/Derivative.lean#L247)
