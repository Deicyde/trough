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
- [Source of `TauCeti.bfEquiv_all_iff_exists_equiv_comp_eq` in TauCeti/ModelTheory/BackAndForth/AllLevels.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/BackAndForth/AllLevels.lean#L123)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/InfinitaryLogic/STATUS.md)
