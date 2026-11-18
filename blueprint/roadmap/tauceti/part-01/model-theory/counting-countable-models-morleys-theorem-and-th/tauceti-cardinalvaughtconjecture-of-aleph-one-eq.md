---
declaration: theorem
origin: cited
lean: TauCeti.cardinalVaughtConjecture_of_aleph_one_eq_continuum
statement: formalized
proof: formalized
---

# TauCeti.cardinalVaughtConjecture_of_aleph_one_eq_continuum

CH implies the cardinal Vaught conjecture, without settling the perfect-set conjecture.

```lean
TauCeti.cardinalVaughtConjecture_of_aleph_one_eq_continuum
  (hCH : Cardinal.aleph 1 = Cardinal.continuum) : TauCeti.CardinalVaughtConjecture
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)
- [TauCeti.countableModelCount](tauceti-countablemodelcount.md)

## Proof depends on

- [Morley's theorem (cardinal form)](../counting/morleys-theorem-cardinal-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.cardinalVaughtConjecture_of_aleph_one_eq_continuum`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Vaught.html#TauCeti.cardinalVaughtConjecture_of_aleph_one_eq_continuum).

## Sources

- [Tau Ceti documentation: `TauCeti.cardinalVaughtConjecture_of_aleph_one_eq_continuum`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Vaught.html#TauCeti.cardinalVaughtConjecture_of_aleph_one_eq_continuum)
- [Source of `TauCeti.cardinalVaughtConjecture_of_aleph_one_eq_continuum` in TauCeti/ModelTheory/Counting/Vaught.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/Counting/Vaught.lean#L360)
- [Tau Ceti roadmap status: Counting countable models: Morley's theorem and the Vaught toolkit](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CountableModelCounting/STATUS.md)
