---
declaration: def
origin: cited
lean: TauCeti.padicIntUnitsEquivZModUnitsProd
statement: formalized
---

# The decomposition `ℤ_pˣ ≃ₜ* (ℤ/qℤ)ˣ × ℤ_p`

A unit `x` goes to its residue `x mod q`
together with `log (x / ω(x mod q)) / q`, where `ω` is `TauCeti.padicUnitsSection p`; the inverse
is `(δ, s) ↦ ω(δ) exp(q s)`.

```lean
TauCeti.padicIntUnitsEquivZModUnitsProd (p : ℕ) [hp : Fact (Nat.Prime p)] :
  ℤ_[p]ˣ ≃ₜ* (ZMod (p ^ TauCeti.padicUnitsDepth p))ˣ × Multiplicative ℤ_[p]
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.padicIntUnitsEquivZModUnitsProd`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/UnitsDecomposition/Logarithm.html#TauCeti.padicIntUnitsEquivZModUnitsProd).

## Sources

- [Tau Ceti documentation: `TauCeti.padicIntUnitsEquivZModUnitsProd`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/UnitsDecomposition/Logarithm.html#TauCeti.padicIntUnitsEquivZModUnitsProd)
- [Source of `TauCeti.padicIntUnitsEquivZModUnitsProd` in TauCeti/NumberTheory/Padics/UnitsDecomposition/Logarithm.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Padics/UnitsDecomposition/Logarithm.lean#L421)
- [Tau Ceti roadmap status: P-adic functional analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PadicFunctionalAnalysis/STATUS.md)
