---
declaration: theorem
origin: cited
lean: TauCeti.ModularForm.cuspTranslationOrbitWidth_mk_inf
statement: formalized
proof: formalized
---

# Widths of an intersection

at every coset, the width of the cusp translation orbit for
`𝒢₁ ⊓ 𝒢₂` is the least common multiple of the widths for `𝒢₁` and for `𝒢₂`.

```lean
TauCeti.ModularForm.cuspTranslationOrbitWidth_mk_inf (𝒢₁ 𝒢₂ : Subgroup (GL (Fin 2) ℝ))
  (x : ↥(Matrix.SpecialLinearGroup.mapGL ℝ).range) :
  TauCeti.ModularForm.cuspTranslationOrbitWidth ⟦↑x⟧ =
    (TauCeti.ModularForm.cuspTranslationOrbitWidth ⟦↑x⟧).lcm
      (TauCeti.ModularForm.cuspTranslationOrbitWidth ⟦↑x⟧)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularForm.cuspTranslationOrbitWidth_mk_inf`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/Norm/Cusps.html#TauCeti.ModularForm.cuspTranslationOrbitWidth_mk_inf).

## Sources

- [Tau Ceti documentation: `TauCeti.ModularForm.cuspTranslationOrbitWidth_mk_inf`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/Norm/Cusps.html#TauCeti.ModularForm.cuspTranslationOrbitWidth_mk_inf)
- [Source of `TauCeti.ModularForm.cuspTranslationOrbitWidth_mk_inf` in TauCeti/NumberTheory/ModularForms/Norm/Cusps.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/Norm/Cusps.lean#L239)
- [Tau Ceti roadmap status: Noncongruence subgroups of the modular group and their modular forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NoncongruenceModularForms/STATUS.md)
