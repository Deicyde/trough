---
declaration: theorem
origin: cited
lean: TauCeti.exists_language_zero_countableModelCount
statement: formalized
proof: formalized
---

# Presentation in universe `0`

A sentence of a relational language with countably many
relation symbols has a counterpart over a relational language in `Language.{0, 0}` with countably
many relation symbols, with the same number of countable models (after lifting) and perfectly many
countable models exactly when the original has. The counterpart is the translation into the small
presentation of the language.

```lean
TauCeti.exists_language_zero_countableModelCount.{u, v, uι} {L : FirstOrder.Language}
  [L.IsRelational] [Countable ((n : ℕ) × L.Relations n)] {ι : Type uι} (φ : L.SentenceInf ι) :
  ∃ L₀,
    ∃ (x : L₀.IsRelational) (_ : Countable ((n : ℕ) × L₀.Relations n)),
      ∃ φ₀,
        Cardinal.lift.{0, v} (TauCeti.countableModelCount φ) =
            Cardinal.lift.{v, 0} (TauCeti.countableModelCount φ₀) ∧
          (TauCeti.HasPerfectlyManyCountableModels φ₀ ↔ TauCeti.HasPerfectlyManyCountableModels φ)
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)
- [TauCeti.countableModelCount](tauceti-countablemodelcount.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_language_zero_countableModelCount`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/LanguageEquiv.html#TauCeti.exists_language_zero_countableModelCount).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_language_zero_countableModelCount`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/LanguageEquiv.html#TauCeti.exists_language_zero_countableModelCount)
- [Source of `TauCeti.exists_language_zero_countableModelCount` in TauCeti/ModelTheory/Counting/LanguageEquiv.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/Counting/LanguageEquiv.lean#L140)
- [Tau Ceti roadmap status: Counting countable models: Morley's theorem and the Vaught toolkit](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CountableModelCounting/STATUS.md)
