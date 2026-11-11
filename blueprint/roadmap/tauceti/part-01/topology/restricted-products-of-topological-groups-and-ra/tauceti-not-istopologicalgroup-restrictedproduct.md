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
- [Source of `TauCeti.not_isTopologicalGroup_restrictedProduct_rat_bot` in TauCeti/Topology/Algebra/RestrictedProduct/NotContinuousMul.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/RestrictedProduct/NotContinuousMul.lean#L223)
- [Tau Ceti roadmap status: Restricted products of topological groups and rational diagonals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/RestrictedProducts/STATUS.md)
