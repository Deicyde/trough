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
- [Source of `FirstOrder.Language.ConsistencyProperty.model_existence` in TauCeti/ModelTheory/ModelExistence/ModelExistence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/ModelExistence/ModelExistence.lean#L81)
- [Tau Ceti roadmap status: Infinitary model existence, omitting types and interpolation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/InfinitaryModelExistence/STATUS.md)
