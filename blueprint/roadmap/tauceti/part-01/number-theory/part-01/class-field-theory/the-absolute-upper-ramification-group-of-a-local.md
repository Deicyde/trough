---
declaration: def
origin: cited
lean: TauCeti.localAbsoluteUpperRamificationGroup
statement: formalized
---

# The absolute upper ramification group of a local field

For real `v ≥ -1`, an absolute
Galois automorphism belongs to `G_K^v` precisely when its restriction to every finite Galois
intermediate field belongs to its upper ramification group, using the canonical extended valuation
(Serre, *Local Fields*, IV §3, Proposition 14).

```lean
TauCeti.localAbsoluteUpperRamificationGroup.{u_1} (K : Type u_1) [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K]
  (v : ↑TauCeti.LocalFieldsRamification.RamificationIndexDomain) :
  Subgroup (Field.absoluteGaloisGroup K)
```

## Depends on

- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.localAbsoluteUpperRamificationGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/AbsoluteFiltration.html#TauCeti.localAbsoluteUpperRamificationGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.localAbsoluteUpperRamificationGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/AbsoluteFiltration.html#TauCeti.localAbsoluteUpperRamificationGroup)
- [Source of `TauCeti.localAbsoluteUpperRamificationGroup` in TauCeti/NumberTheory/LocalField/Herbrand/AbsoluteFiltration.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LocalField/Herbrand/AbsoluteFiltration.lean#L109)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClassFieldTheory/STATUS.md)
