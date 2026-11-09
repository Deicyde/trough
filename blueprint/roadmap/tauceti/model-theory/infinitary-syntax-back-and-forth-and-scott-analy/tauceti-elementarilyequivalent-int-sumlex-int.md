---
declaration: theorem
origin: cited
lean: TauCeti.elementarilyEquivalent_int_sumLex_int
statement: formalized
proof: formalized
---

# TauCeti.elementarilyEquivalent_int_sumLex_int

`ℤ` and `ℤ ⊕ₗ ℤ` satisfy the same first-order sentences in the language of orders.

```lean
TauCeti.elementarilyEquivalent_int_sumLex_int :
  FirstOrder.Language.order.ElementarilyEquivalent ℤ (ℤ ⊕ₗ ℤ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Back-and-forth equivalence at level `α` gives agreement up to quantifier rank `α`](back-and-forth-equivalence-at-level-gives-agreem.md)
- [FirstOrder.Language.BoundedFormulaInf](firstorder-language-boundedformulainf.md)
- [TauCeti.BFEquiv](tauceti-bfequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.elementarilyEquivalent_int_sumLex_int`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/DiscreteOrder.html#TauCeti.elementarilyEquivalent_int_sumLex_int).

## Sources

- [Tau Ceti documentation: `TauCeti.elementarilyEquivalent_int_sumLex_int`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/DiscreteOrder.html#TauCeti.elementarilyEquivalent_int_sumLex_int)
- [Source of `TauCeti.elementarilyEquivalent_int_sumLex_int` in TauCeti/ModelTheory/BackAndForth/DiscreteOrder.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/ModelTheory/BackAndForth/DiscreteOrder.lean#L299)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/InfinitaryLogic/STATUS.md)
