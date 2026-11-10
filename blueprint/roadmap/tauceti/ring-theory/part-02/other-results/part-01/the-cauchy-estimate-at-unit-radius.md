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

- [TauCeti.Dagger.washnitzerAlgebra](../../../part-01/foundations-of-adic-spaces-part-iv-etale-sites-f/tauceti-dagger-washnitzeralgebra.md)
- [TauCeti.Dagger.washnitzerAlgebra.toTate](../../../part-01/foundations-of-adic-spaces-part-iv-etale-sites-f/tauceti-dagger-washnitzeralgebra-totate.md)

## Proof depends on

- [The Cauchy estimate for partial derivatives](../../../part-01/mv-power-series/the-cauchy-estimate-for-partial-derivatives.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.washnitzerAlgebra.norm_toTate_hasseDeriv_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Derivative.html#TauCeti.Dagger.washnitzerAlgebra.norm_toTate_hasseDeriv_le).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.washnitzerAlgebra.norm_toTate_hasseDeriv_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Derivative.html#TauCeti.Dagger.washnitzerAlgebra.norm_toTate_hasseDeriv_le)
- [Source of `TauCeti.Dagger.washnitzerAlgebra.norm_toTate_hasseDeriv_le` in TauCeti/RingTheory/Dagger/Derivative.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Dagger/Derivative.lean#L247)
