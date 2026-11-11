---
declaration: theorem
origin: cited
lean: TauCeti.not_exists_theory_model_iff_nonempty_orderIso
statement: formalized
proof: formalized
---

# Infinite well-orders are not first-order axiomatizable among countable structures

For
an infinite countable well-order `M`, no first-order theory in the language of orders has as its
countable models, in the universe of `M`, exactly the orders isomorphic to `M`. Contrast
`TauCeti.exists_sentenceω_realize_iff_nonempty_orderIso` in `TauCeti.ModelTheory.Scott.WellOrder`,
which gives a single `Lω₁ω` sentence with this property.

```lean
TauCeti.not_exists_theory_model_iff_nonempty_orderIso.{w} (M : Type w) [LinearOrder M]
  [WellFoundedLT M] [Infinite M] [Countable M] :
  ¬∃ T,
      ∀ (N : Type w) [inst : FirstOrder.Language.order.Structure N] [inst_1 : LE N]
        [FirstOrder.Language.order.OrderedStructure N] [Countable N], N ⊨ T ↔ Nonempty (M ≃o N)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.not_exists_theory_model_iff_nonempty_orderIso`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Order.html#TauCeti.not_exists_theory_model_iff_nonempty_orderIso).

## Sources

- [Tau Ceti documentation: `TauCeti.not_exists_theory_model_iff_nonempty_orderIso`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Order.html#TauCeti.not_exists_theory_model_iff_nonempty_orderIso)
- [Source of `TauCeti.not_exists_theory_model_iff_nonempty_orderIso` in TauCeti/ModelTheory/Order.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/Order.lean#L126)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/InfinitaryLogic/STATUS.md)
