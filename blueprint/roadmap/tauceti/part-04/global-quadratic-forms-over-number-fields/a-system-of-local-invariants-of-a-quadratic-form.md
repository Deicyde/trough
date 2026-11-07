---
declaration: structure
origin: cited
lean: TauCeti.NumberField.QuadraticForm.GlobalFormInvariants
statement: formalized
---

# A system of local invariants of a quadratic form over a number field `K`

a rank `n`, a
global plain discriminant `d ∈ Kˣ/(Kˣ)²`, a Hasse sign `s_v ∈ {±1}` at every finite place `v`,
and a positive index `p_w` at every real place `w`. No condition relates the data; the systems
arising from regular forms of positive rank are those satisfying `IsAdmissible`.

```lean
TauCeti.NumberField.QuadraticForm.GlobalFormInvariants.{u_1} (K : Type u_1) [Field K]
  [NumberField K] : Type u_1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.QuadraticForm.GlobalFormInvariants`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/Invariants.html#TauCeti.NumberField.QuadraticForm.GlobalFormInvariants).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.QuadraticForm.GlobalFormInvariants`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/Invariants.html#TauCeti.NumberField.QuadraticForm.GlobalFormInvariants)
- [Source of `TauCeti.NumberField.QuadraticForm.GlobalFormInvariants` in TauCeti/NumberTheory/QuadraticForm/Global/Invariants.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/QuadraticForm/Global/Invariants.lean#L85)
- [Tau Ceti roadmap status: Global quadratic forms over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GlobalQuadraticForms/STATUS.md)
