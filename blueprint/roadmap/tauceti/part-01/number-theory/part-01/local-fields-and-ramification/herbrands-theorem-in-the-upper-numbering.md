---
declaration: theorem
origin: cited
lean: TauCeti.LocalFieldsRamification.map_restrictNormalHom_upperRamificationGroup, TauCeti.LocalFieldsRamification.map_restrictNormalHom_lowerRamificationGroupReal, TauCeti.LocalFieldsRamification.natCard_lowerRamificationGroupReal_herbrand_mul
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

- [Serre's lemma on the lower index of a quotient](serres-lemma-on-the-lower-index-of-a-quotient.md)
- [TauCeti.algebraicExtensionNormedField](tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LocalFieldsRamification.map_restrictNormalHom_upperRamificationGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/UpperQuotient.html#TauCeti.LocalFieldsRamification.map_restrictNormalHom_upperRamificationGroup).

## Other forms

**Herbrand's theorem.** Formalized in Tau Ceti as [`TauCeti.LocalFieldsRamification.map_restrictNormalHom_lowerRamificationGroupReal`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/Quotient.html#TauCeti.LocalFieldsRamification.map_restrictNormalHom_lowerRamificationGroupReal).

```lean
TauCeti.LocalFieldsRamification.map_restrictNormalHom_lowerRamificationGroupReal.{u_1, u_2, u_3}
  {K : Type u_1} {L : Type u_2} {M : Type u_3} [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] [Field L] [ValuativeRel L] [TopologicalSpace L]
  [IsNonarchimedeanLocalField L] [Field M] [ValuativeRel M] [TopologicalSpace M]
  [IsNonarchimedeanLocalField M] [Algebra K L] [ValuativeExtension K L] [Module.Finite K L]
  [Normal K L] [Algebra L M] [ValuativeExtension L M] [Module.Finite L M] [IsGalois L M]
  [Algebra K M] [ValuativeExtension K M] [Module.Finite K M] [IsScalarTower K L M] [Normal K M]
  (u : ↑TauCeti.LocalFieldsRamification.RamificationIndexDomain) :
  Subgroup.map (AlgEquiv.restrictNormalHom L)
      (TauCeti.LocalFieldsRamification.lowerRamificationGroupReal K M ↑u) =
    TauCeti.LocalFieldsRamification.lowerRamificationGroupReal K L
      ↑(TauCeti.LocalFieldsRamification.herbrand L M u)
```

**Herbrand's theorem in counting form.** Formalized in Tau Ceti as [`TauCeti.LocalFieldsRamification.natCard_lowerRamificationGroupReal_herbrand_mul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/Tower.html#TauCeti.LocalFieldsRamification.natCard_lowerRamificationGroupReal_herbrand_mul).

```lean
TauCeti.LocalFieldsRamification.natCard_lowerRamificationGroupReal_herbrand_mul.{u_1, u_2, u_3}
  (K : Type u_1) (L : Type u_2) (M : Type u_3) [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] [Field L] [ValuativeRel L] [TopologicalSpace L]
  [IsNonarchimedeanLocalField L] [Field M] [ValuativeRel M] [TopologicalSpace M]
  [IsNonarchimedeanLocalField M] [Algebra K L] [ValuativeExtension K L] [Module.Finite K L]
  [Algebra L M] [ValuativeExtension L M] [Module.Finite L M] [Algebra K M] [ValuativeExtension K M]
  [IsScalarTower K L M] [Normal K L] [IsGalois L M] [Normal K M]
  (u : ↑TauCeti.LocalFieldsRamification.RamificationIndexDomain) :
  Nat.card
        ↥(TauCeti.LocalFieldsRamification.lowerRamificationGroupReal K L
            ↑(TauCeti.LocalFieldsRamification.herbrand L M u)) *
      Nat.card ↥(TauCeti.LocalFieldsRamification.lowerRamificationGroupReal L M ↑u) =
    Nat.card ↥(TauCeti.LocalFieldsRamification.lowerRamificationGroupReal K M ↑u)
```

## Sources

- [Tau Ceti documentation: `TauCeti.LocalFieldsRamification.map_restrictNormalHom_upperRamificationGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/UpperQuotient.html#TauCeti.LocalFieldsRamification.map_restrictNormalHom_upperRamificationGroup)
- [Source of `TauCeti.LocalFieldsRamification.map_restrictNormalHom_upperRamificationGroup` in TauCeti/NumberTheory/LocalField/Herbrand/UpperQuotient.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/Herbrand/UpperQuotient.lean#L95)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/LocalFieldsRamification/STATUS.md)
