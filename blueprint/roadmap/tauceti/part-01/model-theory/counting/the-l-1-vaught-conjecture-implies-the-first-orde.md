---
declaration: theorem
origin: cited
lean: TauCeti.VaughtConjecture.firstOrder
statement: formalized
proof: formalized
---

# The `L_{ω₁ω}` Vaught conjecture implies the first-order Vaught conjecture

Completeness of
the first-order theory is not needed for this implication; the underlying per-theory reduction is
`TauCeti.VaughtConjecture.countable_or_hasPerfectAntichainOn_modelsOfTheory`.

```lean
TauCeti.VaughtConjecture.firstOrder (h : TauCeti.VaughtConjecture) :
  TauCeti.FirstOrderVaughtConjecture
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)
- [TauCeti.countableModelCount](../counting-countable-models-morleys-theorem-and-th/tauceti-countablemodelcount.md)

## Proof depends on

- [Vaught's witnessed dichotomy along a language equivalence](../counting-countable-models-morleys-theorem-and-th/vaughts-witnessed-dichotomy-along-a-language-equ.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.VaughtConjecture.firstOrder`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/FirstOrder.html#TauCeti.VaughtConjecture.firstOrder), assuming [`TauCeti.VaughtConjecture`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Vaught.html#TauCeti.VaughtConjecture), a proposition Tau Ceti defines.

## Sources

- [Tau Ceti documentation: `TauCeti.VaughtConjecture.firstOrder`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/FirstOrder.html#TauCeti.VaughtConjecture.firstOrder)
- [Source of `TauCeti.VaughtConjecture.firstOrder` in TauCeti/ModelTheory/Counting/FirstOrder.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/Counting/FirstOrder.lean#L251)
