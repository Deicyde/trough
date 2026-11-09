---
declaration: abbrev
origin: cited
lean: TauCeti.ModularSymbols
statement: formalized
---

# TauCeti.ModularSymbols

The **module of modular symbols** `𝕄_w(Γ; R) = (Div⁰(ℙ¹(ℚ)) ⊗_R Sym^w(R²))_Γ` of weight
`w + 2` for a subgroup `Γ ≤ SL(2, ℤ)`, with coefficients in `R`: the `Γ`-coinvariants of the
degree-zero divisors on the cusps tensored with the binary forms of degree `w`.

This is an abbreviation for the coinvariants, so that their universal property
(`Representation.Coinvariants.lift`, `Representation.Coinvariants.hom_ext`) applies directly.

```lean
TauCeti.ModularSymbols.{u_1} (R : Type u_1) [CommRing R]
  (Γ : Subgroup (Matrix.SpecialLinearGroup (Fin 2) ℤ)) (w : ℕ) : Type u_1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularSymbols`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ModularSymbols/Basic.html#TauCeti.ModularSymbols).

## Sources

- [Tau Ceti documentation: `TauCeti.ModularSymbols`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ModularSymbols/Basic.html#TauCeti.ModularSymbols)
- [Source of `TauCeti.ModularSymbols` in TauCeti/NumberTheory/ModularForms/ModularSymbols/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/ModularSymbols/Basic.lean#L315)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularForms/STATUS.md)
