---
declaration: theorem
origin: cited
lean: AbstractMeasure.unitCharacterEval_ext
statement: formalized
proof: formalized
---

# AbstractMeasure.unitCharacterEval_ext

Pseudo-measures on `ℤ_pˣ` are determined by their evaluations at the nontrivial continuous
characters.

```lean
AbstractMeasure.unitCharacterEval_ext {p : ℕ} [Fact (Nat.Prime p)]
  {z η : ↥(AbstractMeasure.unitsPseudomeasures p)}
  (h :
    ∀ (κ : ℤ_[p]ˣ →ₜ* ℤ_[p]) (hκ : κ ≠ 1),
      (κ.unitCharacterEval hκ) z = (κ.unitCharacterEval hκ) η) :
  z = η
```

## Depends on

- [AbstractMeasure.unitsPseudomeasures](abstractmeasure-unitspseudomeasures.md)
- [ContinuousMonoidHom.unitCharacterEval](continuousmonoidhom-unitcharactereval.md)

## Lean

Formalized in Tau Ceti as [`AbstractMeasure.unitCharacterEval_ext`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/Units/Pseudomeasure.html#AbstractMeasure.unitCharacterEval_ext).

## Sources

- [Tau Ceti documentation: `AbstractMeasure.unitCharacterEval_ext`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/Units/Pseudomeasure.html#AbstractMeasure.unitCharacterEval_ext)
- [Source of `AbstractMeasure.unitCharacterEval_ext` in TauCeti/NumberTheory/Padics/Measure/Units/Pseudomeasure.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Padics/Measure/Units/Pseudomeasure.lean#L250)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
