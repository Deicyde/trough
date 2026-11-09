---
declaration: def
origin: cited
lean: FirstOrder.Language.BoundedFormulaInf.reindex
statement: formalized
---

# Transport a formula along a coding of its carrier

each `ι`-indexed conjunction or
disjunction becomes the corresponding coded connective at carrier `κ`.

```lean
FirstOrder.Language.BoundedFormulaInf.reindex.{u, v, u', uι, uκ} {L : FirstOrder.Language}
  {ι : Type uι} {κ : Type uκ} {α : Type u'} (c : TauCeti.IndexCoding ι κ) {n : ℕ} :
  L.BoundedFormulaInf ι α n → L.BoundedFormulaInf κ α n
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](firstorder-language-boundedformulainf.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.BoundedFormulaInf.reindex`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Infinitary/Reindex.html#FirstOrder.Language.BoundedFormulaInf.reindex).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.BoundedFormulaInf.reindex`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Infinitary/Reindex.html#FirstOrder.Language.BoundedFormulaInf.reindex)
- [Source of `FirstOrder.Language.BoundedFormulaInf.reindex` in TauCeti/ModelTheory/Infinitary/Reindex.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/ModelTheory/Infinitary/Reindex.lean#L64)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/InfinitaryLogic/STATUS.md)
