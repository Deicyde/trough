---
declaration: theorem
origin: cited
lean: CongruenceSubgroup.strictLevel_dvd_of_Gamma_le
statement: formalized
proof: formalized
---

# CongruenceSubgroup.strictLevel_dvd_of_Gamma_le

A subgroup containing `Γ(N)` has strict level dividing `N`.

```lean
CongruenceSubgroup.strictLevel_dvd_of_Gamma_le {Γ : Subgroup (Matrix.SpecialLinearGroup (Fin 2) ℤ)}
  {N : ℕ} (h : CongruenceSubgroup.Gamma N ≤ Γ) : Γ.strictLevel ∣ N
```

## Depends on

- [Subgroup.strictLevel](subgroup-strictlevel.md)

## Lean

Formalized in Tau Ceti as [`CongruenceSubgroup.strictLevel_dvd_of_Gamma_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/StrictLevel.html#CongruenceSubgroup.strictLevel_dvd_of_Gamma_le).

## Sources

- [Tau Ceti documentation: `CongruenceSubgroup.strictLevel_dvd_of_Gamma_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/StrictLevel.html#CongruenceSubgroup.strictLevel_dvd_of_Gamma_le)
- [Source of `CongruenceSubgroup.strictLevel_dvd_of_Gamma_le` in TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/StrictLevel.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/StrictLevel.lean#L176)
- [Tau Ceti roadmap status: Noncongruence subgroups of the modular group and their modular forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NoncongruenceModularForms/STATUS.md)
