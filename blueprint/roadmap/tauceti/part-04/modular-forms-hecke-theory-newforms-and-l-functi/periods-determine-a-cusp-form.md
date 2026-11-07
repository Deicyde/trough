---
declaration: theorem
origin: cited
lean: TauCeti.ModularSymbols.periodMap_injective
statement: formalized
proof: formalized
---

# Periods determine a cusp form

For a finite-index subgroup of `SL(2, ℤ)` and weight
`k = w + 2 ≥ 2`, the period map into the dual of the modular symbols over `R` is injective.
In particular this applies to the integral modular symbols (`R = ℤ`).

```lean
TauCeti.ModularSymbols.periodMap_injective.{u_1} {R : Type u_1} [CommRing R] [Algebra R ℂ]
  {Γ : Subgroup (Matrix.SpecialLinearGroup (Fin 2) ℤ)} [Γ.FiniteIndex] {k : ℤ} {w : ℕ}
  (hk : k = ↑w + 2) : Function.Injective ⇑(TauCeti.ModularSymbols.periodMap R Γ hk)
```

## Depends on

- [TauCeti.ModularSymbols](tauceti-modularsymbols.md)
- [TauCeti.ModularSymbols.periodMap](tauceti-modularsymbols-periodmap.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularSymbols.periodMap_injective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ModularSymbols/Period/Injective.html#TauCeti.ModularSymbols.periodMap_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.ModularSymbols.periodMap_injective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ModularSymbols/Period/Injective.html#TauCeti.ModularSymbols.periodMap_injective)
- [Source of `TauCeti.ModularSymbols.periodMap_injective` in TauCeti/NumberTheory/ModularForms/ModularSymbols/Period/Injective.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/ModularSymbols/Period/Injective.lean#L145)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularForms/STATUS.md)
