---
declaration: def
origin: cited
lean: TauCeti.wildInertiaSubgroup
statement: formalized
---

# The wild inertia subgroup `P_K` of the absolute Galois group of a nonarchimedean local field `K`

the automorphisms of the algebraic closure fixing the maximal tamely ramified extension
`K^{t}`. Through `IntermediateField.fixingSubgroupEquiv` it is `Gal(K^{alg}/K^{t})`.

```lean
TauCeti.wildInertiaSubgroup.{u_1} (K : Type u_1) [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] : Subgroup (Field.absoluteGaloisGroup K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.wildInertiaSubgroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/WildInertia.html#TauCeti.wildInertiaSubgroup).

## Sources

- [Tau Ceti documentation: `TauCeti.wildInertiaSubgroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/WildInertia.html#TauCeti.wildInertiaSubgroup)
- [Source of `TauCeti.wildInertiaSubgroup` in TauCeti/NumberTheory/LocalField/WildInertia.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/WildInertia.lean#L248)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalFieldsRamification/STATUS.md)
