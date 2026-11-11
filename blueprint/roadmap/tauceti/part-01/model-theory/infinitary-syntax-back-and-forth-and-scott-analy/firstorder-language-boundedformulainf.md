---
declaration: inductive
origin: cited
lean: FirstOrder.Language.BoundedFormulaInf
statement: formalized
---

# FirstOrder.Language.BoundedFormulaInf

An infinitary bounded formula of `L_{∞ω}`, with infinitary conjunctions and disjunctions
branching over the fixed carrier `ι`, free variables indexed by `α`, and `n` additional bound
variables available.

```lean
FirstOrder.Language.BoundedFormulaInf.{u, v, u', uι} (L : FirstOrder.Language) (ι : Type uι)
  (α : Type u') : ℕ → Type (max u v u' uι)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.BoundedFormulaInf`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Infinitary/Syntax.html#FirstOrder.Language.BoundedFormulaInf).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.BoundedFormulaInf`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Infinitary/Syntax.html#FirstOrder.Language.BoundedFormulaInf)
- [Source of `FirstOrder.Language.BoundedFormulaInf` in TauCeti/ModelTheory/Infinitary/Syntax.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/Infinitary/Syntax.lean#L72)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/InfinitaryLogic/STATUS.md)
