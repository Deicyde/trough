---
declaration: def
origin: cited
lean: FirstOrder.Language.BoundedFormulaInf.freeVarSupport
statement: formalized
---

# FirstOrder.Language.BoundedFormulaInf.freeVarSupport

The **free-variable support** of an infinitary formula: the set of free variables that occur
in one of its atoms. Infinitary connectives take the union over all their branches, so the support
may be infinite.

```lean
FirstOrder.Language.BoundedFormulaInf.freeVarSupport.{u, v, u', uι} {L : FirstOrder.Language}
  {α : Type u'} {ι : Type uι} {n : ℕ} : L.BoundedFormulaInf ι α n → Set α
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](firstorder-language-boundedformulainf.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.BoundedFormulaInf.freeVarSupport`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Infinitary/FreeVarSupport.html#FirstOrder.Language.BoundedFormulaInf.freeVarSupport).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.BoundedFormulaInf.freeVarSupport`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Infinitary/FreeVarSupport.html#FirstOrder.Language.BoundedFormulaInf.freeVarSupport)
- [Source of `FirstOrder.Language.BoundedFormulaInf.freeVarSupport` in TauCeti/ModelTheory/Infinitary/FreeVarSupport.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/ModelTheory/Infinitary/FreeVarSupport.lean#L71)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/InfinitaryLogic/STATUS.md)
