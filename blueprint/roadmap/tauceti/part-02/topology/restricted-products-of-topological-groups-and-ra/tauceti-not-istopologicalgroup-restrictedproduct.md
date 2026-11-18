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
- [Source of `TauCeti.not_isTopologicalGroup_restrictedProduct_rat_bot` in TauCeti/Topology/Algebra/RestrictedProduct/NotContinuousMul.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/RestrictedProduct/NotContinuousMul.lean#L223)
- [Tau Ceti roadmap status: Restricted products of topological groups and rational diagonals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/RestrictedProducts/STATUS.md)
