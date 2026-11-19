---
declaration: def
origin: cited
lean: Subgroup.strictLevel
statement: formalized
---

# Subgroup.strictLevel

The **strict level** of `Γ ≤ SL(2, ℤ)`: the least `N > 0` such that `σ * T ^ N * σ⁻¹ ∈ Γ`
for every `σ ∈ SL(2, ℤ)`, or `0` if there is no such `N` (`strictLevel_eq_sInf`). It is defined
as the order of the image of `T` modulo the normal core of `Γ`.

```lean
Subgroup.strictLevel (Γ : Subgroup (Matrix.SpecialLinearGroup (Fin 2) ℤ)) : ℕ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Subgroup.strictLevel`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/StrictLevel.html#Subgroup.strictLevel).

## Sources

- [Tau Ceti documentation: `Subgroup.strictLevel`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/StrictLevel.html#Subgroup.strictLevel)
- [Source of `Subgroup.strictLevel` in TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/StrictLevel.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/StrictLevel.lean#L62)
- [Tau Ceti roadmap status: Noncongruence subgroups of the modular group and their modular forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NoncongruenceModularForms/STATUS.md)
