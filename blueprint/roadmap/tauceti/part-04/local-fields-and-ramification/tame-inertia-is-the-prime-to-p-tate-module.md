---
declaration: def
origin: cited
lean: TauCeti.quotientWildInertiaSubgroupEquiv
statement: formalized
---

# Tame inertia is the prime-to-`p` Tate module

the tame character induces an isomorphism
of topological groups `I_K / P_K ≃ₜ* ℤ̂^{(p')}(1)` from the tame inertia group, the quotient of
the inertia subgroup by the wild inertia subgroup.

```lean
TauCeti.quotientWildInertiaSubgroupEquiv.{u_1} (K : Type u_1) [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] :
  ↥(TauCeti.inertiaSubgroup K) ⧸
      (TauCeti.wildInertiaSubgroup K).subgroupOf (TauCeti.inertiaSubgroup K) ≃ₜ*
    TauCeti.PrimeToPTateModule
      (ringChar (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer)) (AlgebraicClosure K)
```

## Depends on

- [TauCeti.wildInertiaSubgroup](tauceti-wildinertiasubgroup.md)

## Proof depends on

- [TauCeti.algebraicExtensionNormedField](tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.quotientWildInertiaSubgroupEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Tame/Character.html#TauCeti.quotientWildInertiaSubgroupEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.quotientWildInertiaSubgroupEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Tame/Character.html#TauCeti.quotientWildInertiaSubgroupEquiv)
- [Source of `TauCeti.quotientWildInertiaSubgroupEquiv` in TauCeti/NumberTheory/LocalField/Tame/Character.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/Tame/Character.lean#L518)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalFieldsRamification/STATUS.md)
