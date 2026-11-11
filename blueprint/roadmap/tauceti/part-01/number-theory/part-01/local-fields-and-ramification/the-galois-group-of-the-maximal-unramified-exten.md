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

## Proof depends on

- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.maximalUnramifiedGaloisGroupEquivZHat`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Unramified/ZHat.html#TauCeti.maximalUnramifiedGaloisGroupEquivZHat).

## Sources

- [Tau Ceti documentation: `TauCeti.maximalUnramifiedGaloisGroupEquivZHat`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Unramified/ZHat.html#TauCeti.maximalUnramifiedGaloisGroupEquivZHat)
- [Source of `TauCeti.maximalUnramifiedGaloisGroupEquivZHat` in TauCeti/NumberTheory/LocalField/Unramified/ZHat.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/Unramified/ZHat.lean#L195)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/LocalFieldsRamification/STATUS.md)
