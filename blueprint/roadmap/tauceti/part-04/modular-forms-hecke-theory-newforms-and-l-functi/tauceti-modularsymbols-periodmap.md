---
declaration: def
origin: cited
lean: TauCeti.ModularSymbols.periodMap
statement: formalized
---

# TauCeti.ModularSymbols.periodMap

The **period map** `S_k(Γ) →ₗ[ℂ] (𝕄_w(Γ; R) →ₗ[R] ℂ)` for `k = w + 2`: a cusp form `f` on
`Γ` is sent to the `R`-linear functional on the modular symbols induced by its raw period
pairing, so that `{α, β} ⊗ P ↦ ∫_β^α f(z) P(z, 1) dz`. For `R = ℤ` this is
the pairing of cusp forms with the integral modular symbols.

```lean
TauCeti.ModularSymbols.periodMap.{u_1} (R : Type u_1) [CommRing R] [Algebra R ℂ]
  (Γ : Subgroup (Matrix.SpecialLinearGroup (Fin 2) ℤ)) [Γ.FiniteIndex] {k : ℤ} {w : ℕ}
  (hk : k = ↑w + 2) :
  CuspForm (Subgroup.map (Matrix.SpecialLinearGroup.mapGL ℝ) Γ) k →ₗ[ℂ]
    TauCeti.ModularSymbols R Γ w →ₗ[R] ℂ
```

## Depends on

- [TauCeti.ModularSymbols](tauceti-modularsymbols.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularSymbols.periodMap`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ModularSymbols/Period/Map.html#TauCeti.ModularSymbols.periodMap).

## Sources

- [Tau Ceti documentation: `TauCeti.ModularSymbols.periodMap`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ModularSymbols/Period/Map.html#TauCeti.ModularSymbols.periodMap)
- [Source of `TauCeti.ModularSymbols.periodMap` in TauCeti/NumberTheory/ModularForms/ModularSymbols/Period/Map.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/ModularSymbols/Period/Map.lean#L90)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularForms/STATUS.md)
