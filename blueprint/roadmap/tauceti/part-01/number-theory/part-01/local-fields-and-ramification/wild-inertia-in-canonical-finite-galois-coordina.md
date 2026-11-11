---
declaration: theorem
origin: cited
lean: TauCeti.mem_wildInertiaSubgroup_iff_forall_restrictNormal_mem_finiteGaloisLowerRamificationGroup
statement: formalized
proof: formalized
---

# Wild inertia in canonical finite Galois coordinates

An absolute Galois automorphism
is wild exactly when its restriction to every finite Galois subextension belongs to `G₁`,
using the local-field structures induced from the base field. This is the canonical finite-Galois
criterion prescribed in `TauCetiRoadmap/LocalFieldsRamification`, Layer 4.

```lean
TauCeti.mem_wildInertiaSubgroup_iff_forall_restrictNormal_mem_finiteGaloisLowerRamificationGroup.{u_1}
  {K : Type u_1} [Field K] [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K]
  {σ : Gal(AlgebraicClosure K/K)} :
  σ ∈ TauCeti.wildInertiaSubgroup K ↔
    ∀ (L : FiniteGaloisIntermediateField K (AlgebraicClosure K)),
      σ.restrictNormal ↥L.toIntermediateField ∈
        TauCeti.LocalFieldsRamification.finiteGaloisLowerRamificationGroup K L 1
```

## Depends on

- [TauCeti.algebraicExtensionNormedField](tauceti-algebraicextensionnormedfield.md)
- [The wild inertia subgroup](the-wild-inertia-subgroup.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mem_wildInertiaSubgroup_iff_forall_restrictNormal_mem_finiteGaloisLowerRamificationGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/WildInertia.html#TauCeti.mem_wildInertiaSubgroup_iff_forall_restrictNormal_mem_finiteGaloisLowerRamificationGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.mem_wildInertiaSubgroup_iff_forall_restrictNormal_mem_finiteGaloisLowerRamificationGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/WildInertia.html#TauCeti.mem_wildInertiaSubgroup_iff_forall_restrictNormal_mem_finiteGaloisLowerRamificationGroup)
- [Source of `TauCeti.mem_wildInertiaSubgroup_iff_forall_restrictNormal_mem_finiteGaloisLowerRamificationGroup` in TauCeti/NumberTheory/LocalField/WildInertia.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/WildInertia.lean#L412)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/LocalFieldsRamification/STATUS.md)
