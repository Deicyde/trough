---
declaration: theorem
origin: cited
lean: TauCeti.realize_scottFormula_iff_bfEquiv
statement: formalized
proof: formalized
---

# TauCeti.realize_scottFormula_iff_bfEquiv

A tuple in any structure satisfies the canonical Scott formula exactly when it is
back-and-forth equivalent to the original tuple at that countable ordinal.

```lean
TauCeti.realize_scottFormula_iff_bfEquiv.{u, v, w, w', o} {L : FirstOrder.Language}
  [Countable ((k : ℕ) × L.Relations k)] {M : Type w} [L.Structure M] [Countable M] {n : ℕ}
  [L.IsRelational] {N : Type w'} [L.Structure N] (a : Fin n → M) (b : Fin n → N) {α : Ordinal.{o}}
  (hα : α < Ordinal.omega 1) :
  FirstOrder.Language.BoundedFormulaInf.Realize (TauCeti.scottFormula a α) Empty.elim b ↔
    TauCeti.BFEquiv α n a b
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](firstorder-language-boundedformulainf.md)
- [TauCeti.BFEquiv](tauceti-bfequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.realize_scottFormula_iff_bfEquiv`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Scott/Formula.html#TauCeti.realize_scottFormula_iff_bfEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.realize_scottFormula_iff_bfEquiv`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Scott/Formula.html#TauCeti.realize_scottFormula_iff_bfEquiv)
- [Source of `TauCeti.realize_scottFormula_iff_bfEquiv` in TauCeti/ModelTheory/Scott/Formula.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/Scott/Formula.lean#L93)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/InfinitaryLogic/STATUS.md)
