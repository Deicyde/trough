---
declaration: def
origin: cited
lean: TauCeti.BFEquiv
statement: formalized
---

# TauCeti.BFEquiv

Ordinal back-and-forth equivalence of tuples. At successors the previous level is retained,
in addition to the forth and back requirements. The language is relational.

```lean
TauCeti.BFEquiv.{u, v, w, w', o} {L : FirstOrder.Language} [L.IsRelational] {M : Type w}
  {N : Type w'} [L.Structure M] [L.Structure N] (α : Ordinal.{o}) (n : ℕ) (a : Fin n → M)
  (b : Fin n → N) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.BFEquiv`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/Equivalence.html#TauCeti.BFEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.BFEquiv`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/Equivalence.html#TauCeti.BFEquiv)
- [Source of `TauCeti.BFEquiv` in TauCeti/ModelTheory/BackAndForth/Equivalence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/ModelTheory/BackAndForth/Equivalence.lean#L47)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/InfinitaryLogic/STATUS.md)
