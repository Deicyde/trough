---
declaration: abbrev
origin: cited
lean: AbstractMeasure.unitsPseudomeasures
statement: formalized
---

# AbstractMeasure.unitsPseudomeasures

The pseudo-measures on `ℤ_pˣ`: the elements `z` of the total quotient ring of
`D(ℤ_pˣ, ℤ_p)` such that `(δ_a - 1) z` is a measure for every unit `a`.

```lean
AbstractMeasure.unitsPseudomeasures (p : ℕ) [Fact (Nat.Prime p)] :
  Submodule (AbstractMeasure ℤ_[p]ˣ ℤ_[p] ℤ_[p]) (FractionRing (AbstractMeasure ℤ_[p]ˣ ℤ_[p] ℤ_[p]))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AbstractMeasure.unitsPseudomeasures`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/Units/Pseudomeasure.html#AbstractMeasure.unitsPseudomeasures).

## Sources

- [Tau Ceti documentation: `AbstractMeasure.unitsPseudomeasures`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/Units/Pseudomeasure.html#AbstractMeasure.unitsPseudomeasures)
- [Source of `AbstractMeasure.unitsPseudomeasures` in TauCeti/NumberTheory/Padics/Measure/Units/Pseudomeasure.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Padics/Measure/Units/Pseudomeasure.lean#L75)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
