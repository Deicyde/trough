---
declaration: theorem
origin: cited
lean: TauCeti.BFEquiv.realize_iff_of_qrank_le
statement: formalized
proof: formalized
---

# Back-and-forth equivalence at level `α` gives agreement up to quantifier rank `α`

Tuples
that are back-and-forth equivalent at level `α` satisfy the same infinitary formulas of quantifier
rank at most `α`, at every carrier. The rank and the level are compared after lifting them to a
common universe.

```lean
TauCeti.BFEquiv.realize_iff_of_qrank_le.{u, v, w, w', o, uκ} {L : FirstOrder.Language} {M : Type w}
  {N : Type w'} [L.Structure M] [L.Structure N] [L.IsRelational] {κ : Type uκ} {n : ℕ}
  (φ : L.BoundedFormulaInf κ Empty n) {α : Ordinal.{o}} {a : Fin n → M} {b : Fin n → N} :
  TauCeti.BFEquiv α n a b →
    Ordinal.lift.{o, uκ} φ.qrank ≤ Ordinal.lift.{uκ, o} α →
      ∀ (v : Empty → M) (w : Empty → N), φ.Realize v a ↔ φ.Realize w b
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](firstorder-language-boundedformulainf.md)
- [TauCeti.BFEquiv](tauceti-bfequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BFEquiv.realize_iff_of_qrank_le`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/Karp.html#TauCeti.BFEquiv.realize_iff_of_qrank_le).

## Sources

- [Tau Ceti documentation: `TauCeti.BFEquiv.realize_iff_of_qrank_le`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/Karp.html#TauCeti.BFEquiv.realize_iff_of_qrank_le)
- [Source of `TauCeti.BFEquiv.realize_iff_of_qrank_le` in TauCeti/ModelTheory/BackAndForth/Karp.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/ModelTheory/BackAndForth/Karp.lean#L202)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/InfinitaryLogic/STATUS.md)
