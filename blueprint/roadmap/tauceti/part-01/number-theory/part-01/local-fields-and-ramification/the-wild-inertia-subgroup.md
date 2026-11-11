---
declaration: def
origin: cited
lean: TauCeti.wildInertiaSubgroup
statement: formalized
---

# The wild inertia subgroup

**The wild inertia subgroup** `P_K` of the absolute Galois group of a nonarchimedean local
field `K`: the automorphisms of the algebraic closure fixing the maximal tamely ramified extension
`K^{t}`. Through `IntermediateField.fixingSubgroupEquiv` it is `Gal(K^{alg}/K^{t})`.

```lean
TauCeti.wildInertiaSubgroup.{u_1} (K : Type u_1) [Field K] [ValuativeRel K] :
  Subgroup (Field.absoluteGaloisGroup K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.wildInertiaSubgroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/WildInertia.html#TauCeti.wildInertiaSubgroup).

## Sources

- [Tau Ceti documentation: `TauCeti.wildInertiaSubgroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/WildInertia.html#TauCeti.wildInertiaSubgroup)
- [Source of `TauCeti.wildInertiaSubgroup` in TauCeti/NumberTheory/LocalField/WildInertia.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/WildInertia.lean#L156)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/LocalFieldsRamification/STATUS.md)
