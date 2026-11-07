---
declaration: def
origin: cited
lean: TauCeti.maximalUnramifiedGaloisGroupEquivZHat
statement: formalized
---

# The Galois group of the maximal unramified extension is the profinite integers

This
continuous multiplicative equivalence sends arithmetic Frobenius to `zHat.gen`.

```lean
TauCeti.maximalUnramifiedGaloisGroupEquivZHat.{u, v} (K : Type u) [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] (Ω : Type v) [Field Ω] [Algebra K Ω]
  [IsSepClosed Ω] :
  Gal(↥(TauCeti.maximalUnramifiedExtension K Ω)/K) ≃ₜ* ↑TauCeti.zHat.toProfinite.toTop
```

## Depends on

- [TauCeti.algebraicExtensionNormedField](tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.maximalUnramifiedGaloisGroupEquivZHat`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Unramified/ZHat.html#TauCeti.maximalUnramifiedGaloisGroupEquivZHat).

## Sources

- [Tau Ceti documentation: `TauCeti.maximalUnramifiedGaloisGroupEquivZHat`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Unramified/ZHat.html#TauCeti.maximalUnramifiedGaloisGroupEquivZHat)
- [Source of `TauCeti.maximalUnramifiedGaloisGroupEquivZHat` in TauCeti/NumberTheory/LocalField/Unramified/ZHat.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/Unramified/ZHat.lean#L195)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalFieldsRamification/STATUS.md)
