---
declaration: theorem
origin: cited
lean: Subgroup.strictLevel_inf
statement: formalized
proof: formalized
---

# The intersection law

the strict level of `Γ₁ ⊓ Γ₂` is the least common multiple of the
strict levels of `Γ₁` and `Γ₂`.

```lean
Subgroup.strictLevel_inf {Γ₁ Γ₂ : Subgroup (Matrix.SpecialLinearGroup (Fin 2) ℤ)} :
  (Γ₁ ⊓ Γ₂).strictLevel = Γ₁.strictLevel.lcm Γ₂.strictLevel
```

## Depends on

- [Subgroup.strictLevel](subgroup-strictlevel.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.strictLevel_inf`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/StrictLevel.html#Subgroup.strictLevel_inf).

## Sources

- [Tau Ceti documentation: `Subgroup.strictLevel_inf`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/StrictLevel.html#Subgroup.strictLevel_inf)
- [Source of `Subgroup.strictLevel_inf` in TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/StrictLevel.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/StrictLevel.lean#L122)
- [Tau Ceti roadmap status: Noncongruence subgroups of the modular group and their modular forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NoncongruenceModularForms/STATUS.md)
