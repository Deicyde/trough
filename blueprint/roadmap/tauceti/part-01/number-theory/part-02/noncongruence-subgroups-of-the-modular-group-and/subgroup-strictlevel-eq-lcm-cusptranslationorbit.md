---
declaration: theorem
origin: cited
lean: Subgroup.strictLevel_eq_lcm_cuspTranslationOrbitWidth
statement: formalized
proof: formalized
---

# Subgroup.strictLevel_eq_lcm_cuspTranslationOrbitWidth

For `Γ` of finite index, the strict level is the least common multiple of the widths of its
finitely many cusp translation orbits.

```lean
Subgroup.strictLevel_eq_lcm_cuspTranslationOrbitWidth
  {Γ : Subgroup (Matrix.SpecialLinearGroup (Fin 2) ℤ)} [Γ.FiniteIndex] :
  Γ.strictLevel = Finset.univ.lcm TauCeti.ModularForm.cuspTranslationOrbitWidth
```

## Depends on

- [Subgroup.strictLevel](subgroup-strictlevel.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.strictLevel_eq_lcm_cuspTranslationOrbitWidth`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/StrictLevel.html#Subgroup.strictLevel_eq_lcm_cuspTranslationOrbitWidth).

## Sources

- [Tau Ceti documentation: `Subgroup.strictLevel_eq_lcm_cuspTranslationOrbitWidth`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/StrictLevel.html#Subgroup.strictLevel_eq_lcm_cuspTranslationOrbitWidth)
- [Source of `Subgroup.strictLevel_eq_lcm_cuspTranslationOrbitWidth` in TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/StrictLevel.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/StrictLevel.lean#L152)
- [Tau Ceti roadmap status: Noncongruence subgroups of the modular group and their modular forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NoncongruenceModularForms/STATUS.md)
