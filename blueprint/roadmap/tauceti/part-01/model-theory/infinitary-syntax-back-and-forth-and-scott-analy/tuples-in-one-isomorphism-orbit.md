---
declaration: theorem
origin: cited
lean: TauCeti.bfEquiv_all_iff_exists_equiv_comp_eq
statement: formalized
proof: formalized
---

# Tuples in one isomorphism orbit

Tuples of countable relational structures are
back-and-forth equivalent at every level exactly when an isomorphism carries one to the
other.

```lean
TauCeti.bfEquiv_all_iff_exists_equiv_comp_eq.{u, v, w, w'} {L : FirstOrder.Language}
  [L.IsRelational] {M : Type w} {N : Type w'} [L.Structure M] [L.Structure N] [Countable M]
  [Countable N] {n : ℕ} {a : Fin n → M} {b : Fin n → N} :
  (∀ (α : Ordinal.{max w w'}), TauCeti.BFEquiv α n a b) ↔ ∃ e, ⇑e ∘ a = b
```

## Depends on

- [TauCeti.BFEquiv](tauceti-bfequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.bfEquiv_all_iff_exists_equiv_comp_eq`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/AllLevels.html#TauCeti.bfEquiv_all_iff_exists_equiv_comp_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.bfEquiv_all_iff_exists_equiv_comp_eq`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/AllLevels.html#TauCeti.bfEquiv_all_iff_exists_equiv_comp_eq)
- [Source of `TauCeti.bfEquiv_all_iff_exists_equiv_comp_eq` in TauCeti/ModelTheory/BackAndForth/AllLevels.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/BackAndForth/AllLevels.lean#L123)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/InfinitaryLogic/STATUS.md)
