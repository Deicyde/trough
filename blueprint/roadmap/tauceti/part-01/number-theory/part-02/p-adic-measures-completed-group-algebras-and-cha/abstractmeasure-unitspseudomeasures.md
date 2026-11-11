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
- [Source of `AbstractMeasure.unitsPseudomeasures` in TauCeti/NumberTheory/Padics/Measure/Units/Pseudomeasure.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Padics/Measure/Units/Pseudomeasure.lean#L75)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
