---
declaration: theorem
origin: cited
lean: TauCeti.LocalFieldsRamification.map_restrictNormalHom_upperRamificationGroup
statement: formalized
proof: formalized
---

# Herbrand's theorem in the upper numbering

For a tower `M/L/K` of Galois extensions, the
image of the upper ramification group `G^v` of `M/K` under restriction to `L` is the upper
ramification group of `L/K` at the same index: `(G/H)^v = G^v H / H` for `H = Gal(M/L)`.

```lean
TauCeti.LocalFieldsRamification.map_restrictNormalHom_upperRamificationGroup.{u_1, u_2, u_3}
  (K : Type u_1) (L : Type u_2) (M : Type u_3) [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] [Field L] [ValuativeRel L] [TopologicalSpace L]
  [IsNonarchimedeanLocalField L] [Field M] [ValuativeRel M] [TopologicalSpace M]
  [IsNonarchimedeanLocalField M] [Algebra K L] [ValuativeExtension K L] [Module.Finite K L]
  [Algebra L M] [ValuativeExtension L M] [Module.Finite L M] [Algebra K M] [ValuativeExtension K M]
  [IsScalarTower K L M] [IsGalois K L] [IsGalois K M]
  (v : ↑TauCeti.LocalFieldsRamification.RamificationIndexDomain) :
  Subgroup.map (AlgEquiv.restrictNormalHom L)
      (TauCeti.LocalFieldsRamification.upperRamificationGroup K M v) =
    TauCeti.LocalFieldsRamification.upperRamificationGroup K L v
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.algebraicExtensionNormedField](tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LocalFieldsRamification.map_restrictNormalHom_upperRamificationGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/UpperQuotient.html#TauCeti.LocalFieldsRamification.map_restrictNormalHom_upperRamificationGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.LocalFieldsRamification.map_restrictNormalHom_upperRamificationGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/UpperQuotient.html#TauCeti.LocalFieldsRamification.map_restrictNormalHom_upperRamificationGroup)
- [Source of `TauCeti.LocalFieldsRamification.map_restrictNormalHom_upperRamificationGroup` in TauCeti/NumberTheory/LocalField/Herbrand/UpperQuotient.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/Herbrand/UpperQuotient.lean#L94)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalFieldsRamification/STATUS.md)
