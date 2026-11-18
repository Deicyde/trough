---
declaration: theorem
origin: cited
lean: TauCeti.not_hasVaughtDichotomy_iff
statement: formalized
proof: formalized
---

# TauCeti.not_hasVaughtDichotomy_iff

A counterexample to the perfect-set dichotomy has exactly `ℵ₁` countable models and no
perfect set of pairwise non-isomorphic countable models. No CH hypothesis is needed.

```lean
TauCeti.not_hasVaughtDichotomy_iff.{u, v, uι} {L : FirstOrder.Language} [L.IsRelational]
  {ι : Type uι} [∀ (n : ℕ), Countable (L.Relations n)] [Countable ι] {φ : L.SentenceInf ι} :
  ¬TauCeti.HasVaughtDichotomy φ ↔
    TauCeti.countableModelCount φ = Cardinal.aleph 1 ∧ ¬TauCeti.HasPerfectlyManyCountableModels φ
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)
- [TauCeti.countableModelCount](tauceti-countablemodelcount.md)

## Proof depends on

- [Morley's theorem (cardinal form)](../counting/morleys-theorem-cardinal-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.not_hasVaughtDichotomy_iff`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Vaught.html#TauCeti.not_hasVaughtDichotomy_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.not_hasVaughtDichotomy_iff`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Vaught.html#TauCeti.not_hasVaughtDichotomy_iff)
- [Source of `TauCeti.not_hasVaughtDichotomy_iff` in TauCeti/ModelTheory/Counting/Vaught.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/Counting/Vaught.lean#L101)
- [Tau Ceti roadmap status: Counting countable models: Morley's theorem and the Vaught toolkit](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CountableModelCounting/STATUS.md)
