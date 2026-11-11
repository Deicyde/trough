---
declaration: def
origin: cited
lean: TauCeti.Khovanov.fiberwiseSplit
statement: formalized
---

# TauCeti.Khovanov.fiberwiseSplit

The split map along `f`, adjoint to multiplication along its fibres. It maps the tensor
on `τ` to the tensor on `σ`; a two-element fibre splits that circle.

```lean
TauCeti.Khovanov.fiberwiseSplit.{u_1, u_3, u_4} {R : Type u_1} [CommSemiring R] {σ : Type u_3}
  {τ : Type u_4} [Fintype σ] [Fintype τ] [DecidableEq τ] (f : σ → τ) :
  TauCeti.Khovanov.CircleTensor R τ →ₗ[R] TauCeti.Khovanov.CircleTensor R σ
```

## Depends on

- [TauCeti.Khovanov.CircleTensor](tauceti-khovanov-circletensor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Khovanov.fiberwiseSplit`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Split.html#TauCeti.Khovanov.fiberwiseSplit).

## Sources

- [Tau Ceti documentation: `TauCeti.Khovanov.fiberwiseSplit`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Split.html#TauCeti.Khovanov.fiberwiseSplit)
- [Source of `TauCeti.Khovanov.fiberwiseSplit` in TauCeti/KnotTheory/Khovanov/Split.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/KnotTheory/Khovanov/Split.lean#L111)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/KhovanovHomology/STATUS.md)
