---
declaration: theorem
origin: cited
lean: TauCeti.exists_sentenceω_realize_iff_nonempty_orderIso
statement: formalized
proof: formalized
---

# TauCeti.exists_sentenceω_realize_iff_nonempty_orderIso

Every countable order `M` has an `Lω₁ω` sentence in the language of orders that holds in a
countable order, in any universe, exactly when that order is isomorphic to `M`. For a countable
well-order `M`, such as `o.ToType` for an ordinal `o < ω₁`, its countable models are exactly the
well-orders of the order type of `M`.

```lean
TauCeti.exists_sentenceω_realize_iff_nonempty_orderIso.{w, w'} (M : Type w) [LE M] [Countable M] :
  ∃ σ,
    ∀ (N : Type w') [inst : FirstOrder.Language.order.Structure N] [inst_1 : LE N]
      [FirstOrder.Language.order.OrderedStructure N] [Countable N],
      FirstOrder.Language.SentenceInf.Realize σ N ↔ Nonempty (M ≃o N)
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](firstorder-language-boundedformulainf.md)

## Proof depends on

- [Scott's isomorphism theorem](scotts-isomorphism-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_sentenceω_realize_iff_nonempty_orderIso`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Scott/WellOrder.html#TauCeti.exists_sentence%CF%89_realize_iff_nonempty_orderIso).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_sentenceω_realize_iff_nonempty_orderIso`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Scott/WellOrder.html#TauCeti.exists_sentence%CF%89_realize_iff_nonempty_orderIso)
- [Source of `TauCeti.exists_sentenceω_realize_iff_nonempty_orderIso` in TauCeti/ModelTheory/Scott/WellOrder.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/Scott/WellOrder.lean#L47)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/InfinitaryLogic/STATUS.md)
