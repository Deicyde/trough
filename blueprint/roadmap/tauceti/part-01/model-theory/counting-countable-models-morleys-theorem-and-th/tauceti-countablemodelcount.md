---
declaration: def
origin: cited
lean: TauCeti.countableModelCount
statement: formalized
---

# TauCeti.countableModelCount

The number of countable models of `φ` up to isomorphism, finite models included.

```lean
TauCeti.countableModelCount.{u, v, uι} {L : FirstOrder.Language} [L.IsRelational] {ι : Type uι}
  (φ : L.SentenceInf ι) : Cardinal.{v}
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.countableModelCount`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Classes.html#TauCeti.countableModelCount).

## Sources

- [Tau Ceti documentation: `TauCeti.countableModelCount`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Classes.html#TauCeti.countableModelCount)
- [Source of `TauCeti.countableModelCount` in TauCeti/ModelTheory/Counting/Classes.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/Counting/Classes.lean#L192)
- [Tau Ceti roadmap status: Counting countable models: Morley's theorem and the Vaught toolkit](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CountableModelCounting/STATUS.md)
