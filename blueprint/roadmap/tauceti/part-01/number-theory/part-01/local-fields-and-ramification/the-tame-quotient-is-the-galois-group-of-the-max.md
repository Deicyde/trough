---
declaration: def
origin: cited
lean: TauCeti.tameQuotientEquivMaximalTameExtension
statement: formalized
---

# The tame quotient is the Galois group of the maximal tamely ramified extension

restriction to `K^{t}` induces an isomorphism of topological groups `G_K / P_K ≃ₜ* Gal(K^{t}/K)`.

```lean
TauCeti.tameQuotientEquivMaximalTameExtension.{u} (K : Type u) [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] :
  TauCeti.tameQuotient K ≃ₜ* Gal(↥(TauCeti.maximalTameExtension K (AlgebraicClosure K))/K)
```

## Depends on

- [The wild inertia subgroup](the-wild-inertia-subgroup.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tameQuotientEquivMaximalTameExtension`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Tame/Quotient.html#TauCeti.tameQuotientEquivMaximalTameExtension).

## Sources

- [Tau Ceti documentation: `TauCeti.tameQuotientEquivMaximalTameExtension`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Tame/Quotient.html#TauCeti.tameQuotientEquivMaximalTameExtension)
- [Source of `TauCeti.tameQuotientEquivMaximalTameExtension` in TauCeti/NumberTheory/LocalField/Tame/Quotient.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/Tame/Quotient.lean#L348)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/LocalFieldsRamification/STATUS.md)
