---
declaration: theorem
origin: cited
lean: FirstOrder.Language.ConsistencyProperty.model_existence
statement: formalized
proof: formalized
---

# Model existence

Every countable member of a consistency property over a language with
countably many function and relation symbols has a countable nonempty model in any universe.
Every element of the model is the interpretation of a Henkin constant.

```lean
FirstOrder.Language.ConsistencyProperty.model_existence.{u, v, w} {L : FirstOrder.Language}
  [Countable ((n : ℕ) × L.Functions n)] [Countable ((n : ℕ) × L.Relations n)]
  (C : L.ConsistencyProperty) {s : (L.withConstants ℕ).Theoryω} (hs : s ∈ C.sets)
  (hsc : Set.Countable s) :
  ∃ M x, Countable M ∧ Nonempty M ∧ s.Model M ∧ Function.Surjective fun c => ↑(L.con c)
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.ConsistencyProperty.model_existence`](https://taucetiproject.org/docs/TauCeti/ModelTheory/ModelExistence/ModelExistence.html#FirstOrder.Language.ConsistencyProperty.model_existence).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.ConsistencyProperty.model_existence`](https://taucetiproject.org/docs/TauCeti/ModelTheory/ModelExistence/ModelExistence.html#FirstOrder.Language.ConsistencyProperty.model_existence)
- [Source of `FirstOrder.Language.ConsistencyProperty.model_existence` in TauCeti/ModelTheory/ModelExistence/ModelExistence.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/ModelExistence/ModelExistence.lean#L81)
- [Tau Ceti roadmap status: Infinitary model existence, omitting types and interpolation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/InfinitaryModelExistence/STATUS.md)
