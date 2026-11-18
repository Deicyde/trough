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
using the local-field structures induced from the base field.

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

## Proof depends on

- [Wild inertia, through radicals](wild-inertia-through-radicals.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mem_wildInertiaSubgroup_iff_forall_restrictNormal_mem_finiteGaloisLowerRamificationGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/WildInertia.html#TauCeti.mem_wildInertiaSubgroup_iff_forall_restrictNormal_mem_finiteGaloisLowerRamificationGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.mem_wildInertiaSubgroup_iff_forall_restrictNormal_mem_finiteGaloisLowerRamificationGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/WildInertia.html#TauCeti.mem_wildInertiaSubgroup_iff_forall_restrictNormal_mem_finiteGaloisLowerRamificationGroup)
- [Source of `TauCeti.mem_wildInertiaSubgroup_iff_forall_restrictNormal_mem_finiteGaloisLowerRamificationGroup` in TauCeti/NumberTheory/LocalField/WildInertia.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LocalField/WildInertia.lean#L412)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/LocalFieldsRamification/STATUS.md)
