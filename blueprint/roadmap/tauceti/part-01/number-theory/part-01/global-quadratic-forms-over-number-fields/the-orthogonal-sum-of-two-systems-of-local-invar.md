---
declaration: def
origin: cited
lean: TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.prod
statement: formalized
---

# The orthogonal sum of two systems of local invariants, modelled on the invariants of an orthogonal sum of forms

ranks, discriminants and real positive indices add, and the Hasse sign at
a finite place `v` is `s_v(I) · s_v(J) · (d_v(I), d_v(J))_v`.

```lean
TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.prod.{u} {K : Type u} [Field K]
  [NumberField K] (I J : TauCeti.NumberField.QuadraticForm.GlobalFormInvariants K) :
  TauCeti.NumberField.QuadraticForm.GlobalFormInvariants K
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.prod`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/OrthogonalSum.html#TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.prod).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.prod`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/OrthogonalSum.html#TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.prod)
- [Source of `TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.prod` in TauCeti/NumberTheory/QuadraticForm/Global/OrthogonalSum.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/QuadraticForm/Global/OrthogonalSum.lean#L79)
- [Tau Ceti roadmap status: Global quadratic forms over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GlobalQuadraticForms/STATUS.md)
