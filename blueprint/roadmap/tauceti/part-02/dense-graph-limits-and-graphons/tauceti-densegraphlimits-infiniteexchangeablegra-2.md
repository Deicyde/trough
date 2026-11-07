---
declaration: def
origin: cited
lean: TauCeti.DenseGraphLimits.InfiniteExchangeableGraphLaw.relationalLawEquiv
statement: formalized
---

# TauCeti.DenseGraphLimits.InfiniteExchangeableGraphLaw.relationalLawEquiv

**Exchangeable laws on infinite graphs are the exchangeable relational laws of the language of
graphs on `ℕ` concentrated on simple graphs**, that is, on symmetric irreflexive configurations.
The inverse pulls the law back along the encoding.

```lean
TauCeti.DenseGraphLimits.InfiniteExchangeableGraphLaw.relationalLawEquiv :
  TauCeti.DenseGraphLimits.InfiniteExchangeableGraphLaw ≃
    { μ //
      ∀ᵐ (c : TauCeti.RelationalConfiguration FirstOrder.Language.graph ℕ) ∂μ.law, c.IsSimpleGraph }
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.DenseGraphLimits.InfiniteExchangeableGraphLaw.relationalLawEquiv`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/ExchangeableGraphLaw/Relational/Basic.html#TauCeti.DenseGraphLimits.InfiniteExchangeableGraphLaw.relationalLawEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.DenseGraphLimits.InfiniteExchangeableGraphLaw.relationalLawEquiv`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/ExchangeableGraphLaw/Relational/Basic.html#TauCeti.DenseGraphLimits.InfiniteExchangeableGraphLaw.relationalLawEquiv)
- [Source of `TauCeti.DenseGraphLimits.InfiniteExchangeableGraphLaw.relationalLawEquiv` in TauCeti/Combinatorics/DenseGraphLimits/ExchangeableGraphLaw/Relational/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/DenseGraphLimits/ExchangeableGraphLaw/Relational/Basic.lean#L141)
- [Tau Ceti roadmap status: Dense graph limits and graphons](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/DenseGraphLimits/STATUS.md)
