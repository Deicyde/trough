---
declaration: theorem
origin: cited
lean: TauCeti.cardinalVaughtConjecture_iff_vaughtConjecture
statement: formalized
proof: formalized
---

# TauCeti.cardinalVaughtConjecture_iff_vaughtConjecture

Under `ℵ₁ < 𝔠`, the cardinal and perfect-set Vaught conjectures are equivalent.

```lean
TauCeti.cardinalVaughtConjecture_iff_vaughtConjecture (hc : Cardinal.aleph 1 < Cardinal.continuum) :
  TauCeti.CardinalVaughtConjecture ↔ TauCeti.VaughtConjecture
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)
- [TauCeti.countableModelCount](tauceti-countablemodelcount.md)

## Proof depends on

- [Morley's theorem (cardinal form)](../counting/morleys-theorem-cardinal-form.md)
- [Setoid.HasCantorAntichainOn](../../set-theory/borel-equivalence-relations-the-g0-dichotomy-and/setoid-hascantorantichainon.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.cardinalVaughtConjecture_iff_vaughtConjecture`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Vaught.html#TauCeti.cardinalVaughtConjecture_iff_vaughtConjecture).

## Sources

- [Tau Ceti documentation: `TauCeti.cardinalVaughtConjecture_iff_vaughtConjecture`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Vaught.html#TauCeti.cardinalVaughtConjecture_iff_vaughtConjecture)
- [Source of `TauCeti.cardinalVaughtConjecture_iff_vaughtConjecture` in TauCeti/ModelTheory/Counting/Vaught.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/Counting/Vaught.lean#L366)
- [Tau Ceti roadmap status: Counting countable models: Morley's theorem and the Vaught toolkit](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CountableModelCounting/STATUS.md)
