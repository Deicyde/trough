---
declaration: theorem
origin: cited
lean: TauCeti.not_isTopologicalGroup_restrictedProduct_rat_bot
statement: formalized
proof: formalized
---

# TauCeti.not_isTopologicalGroup_restrictedProduct_rat_bot

The restricted product `Πʳ n : ℕ, [Multiplicative ℚ, ⊥]` is not a topological group: the
hypothesis `Fact (∀ i, IsOpen (A i))` of Mathlib's `RestrictedProduct.isTopologicalGroup` cannot be
dropped.

```lean
TauCeti.not_isTopologicalGroup_restrictedProduct_rat_bot :
  ¬IsTopologicalGroup (RestrictedProduct (fun x => Multiplicative ℚ) (fun x => ↑⊥) Filter.cofinite)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.not_isTopologicalGroup_restrictedProduct_rat_bot`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/NotContinuousMul.html#TauCeti.not_isTopologicalGroup_restrictedProduct_rat_bot).

## Sources

- [Tau Ceti documentation: `TauCeti.not_isTopologicalGroup_restrictedProduct_rat_bot`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/NotContinuousMul.html#TauCeti.not_isTopologicalGroup_restrictedProduct_rat_bot)
- [Source of `TauCeti.not_isTopologicalGroup_restrictedProduct_rat_bot` in TauCeti/Topology/Algebra/RestrictedProduct/NotContinuousMul.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/RestrictedProduct/NotContinuousMul.lean#L223)
- [Tau Ceti roadmap status: Restricted products of topological groups and rational diagonals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/RestrictedProducts/STATUS.md)
