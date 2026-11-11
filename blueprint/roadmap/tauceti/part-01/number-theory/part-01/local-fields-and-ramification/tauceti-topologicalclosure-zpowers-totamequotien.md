---
declaration: theorem
origin: cited
lean: TauCeti.topologicalClosure_zpowers_toTameQuotient_eq_iff
statement: formalized
proof: formalized
---

# TauCeti.topologicalClosure_zpowers_toTameQuotient_eq_iff

An inertia element generates tame inertia exactly when its tame character generates the
prime-to-residue-characteristic Tate module. Thus either description of a tame inertia
generator can be used in the marked Iwasawa presentation.

```lean
TauCeti.topologicalClosure_zpowers_toTameQuotient_eq_iff.{u} {K : Type u} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] {τ : ↥(TauCeti.inertiaSubgroup K)} :
  (Subgroup.zpowers ((TauCeti.toTameQuotient K) ↑τ)).topologicalClosure = TauCeti.tameInertia K ↔
    (Subgroup.zpowers ((TauCeti.inertiaTameCharacter K) τ)).topologicalClosure = ⊤
```

## Depends on

- [The wild inertia subgroup](the-wild-inertia-subgroup.md)

## Proof depends on

- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [Euler's theorem on an `n`-th root of unity](../../../group-theory/other-results/eulers-theorem-on-an-n-th-root-of-unity.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Tame inertia is the prime-to-`p` Tate module](tame-inertia-is-the-prime-to-p-tate-module.md)
- [TauCeti.algebraicExtensionNormedField](tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.topologicalClosure_zpowers_toTameQuotient_eq_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Tame/Quotient.html#TauCeti.topologicalClosure_zpowers_toTameQuotient_eq_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.topologicalClosure_zpowers_toTameQuotient_eq_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Tame/Quotient.html#TauCeti.topologicalClosure_zpowers_toTameQuotient_eq_iff)
- [Source of `TauCeti.topologicalClosure_zpowers_toTameQuotient_eq_iff` in TauCeti/NumberTheory/LocalField/Tame/Quotient.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/Tame/Quotient.lean#L670)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/LocalFieldsRamification/STATUS.md)
