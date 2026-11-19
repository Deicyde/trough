---
declaration: theorem
origin: cited
lean: Subgroup.strictLevel_normalCore
statement: formalized
proof: formalized
---

# Subgroup.strictLevel_normalCore

Passing to the normal core does not change the strict level.

```lean
Subgroup.strictLevel_normalCore {Γ : Subgroup (Matrix.SpecialLinearGroup (Fin 2) ℤ)} :
  Γ.normalCore.strictLevel = Γ.strictLevel
```

## Depends on

- [Subgroup.strictLevel](subgroup-strictlevel.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.strictLevel_normalCore`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/StrictLevel.html#Subgroup.strictLevel_normalCore).

## Sources

- [Tau Ceti documentation: `Subgroup.strictLevel_normalCore`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/StrictLevel.html#Subgroup.strictLevel_normalCore)
- [Source of `Subgroup.strictLevel_normalCore` in TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/StrictLevel.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/StrictLevel.lean#L128)
- [Tau Ceti roadmap status: Noncongruence subgroups of the modular group and their modular forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NoncongruenceModularForms/STATUS.md)
