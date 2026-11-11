---
declaration: theorem
origin: cited
lean: TauCeti.maximalTameExtension_eq_fixedField_inf_separableClosure
statement: formalized
proof: formalized
---

# The maximal tamely ramified extension is cut out by wild inertia

`K^{t}` is the separable
part of the field fixed by `P_K`. The intersection with the separable closure cannot be dropped:
in positive characteristic every fixed field contains the purely inseparable closure of `K`, while
`K^{t}` is separable over `K`.

```lean
TauCeti.maximalTameExtension_eq_fixedField_inf_separableClosure.{u_1} (K : Type u_1) [Field K]
  [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] :
  TauCeti.maximalTameExtension K (AlgebraicClosure K) =
    IntermediateField.fixedField (TauCeti.wildInertiaSubgroup K) ⊓
      separableClosure K (AlgebraicClosure K)
```

## Depends on

- [The wild inertia subgroup](the-wild-inertia-subgroup.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.maximalTameExtension_eq_fixedField_inf_separableClosure`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/WildInertia.html#TauCeti.maximalTameExtension_eq_fixedField_inf_separableClosure).

## Sources

- [Tau Ceti documentation: `TauCeti.maximalTameExtension_eq_fixedField_inf_separableClosure`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/WildInertia.html#TauCeti.maximalTameExtension_eq_fixedField_inf_separableClosure)
- [Source of `TauCeti.maximalTameExtension_eq_fixedField_inf_separableClosure` in TauCeti/NumberTheory/LocalField/WildInertia.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/WildInertia.lean#L301)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/LocalFieldsRamification/STATUS.md)
