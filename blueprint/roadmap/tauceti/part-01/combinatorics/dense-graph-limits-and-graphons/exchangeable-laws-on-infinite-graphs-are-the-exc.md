---
declaration: def
origin: cited
lean: TauCeti.DenseGraphLimits.InfiniteExchangeableGraphLaw.relationalLawEquiv
statement: formalized
---

# Exchangeable laws on infinite graphs are the exchangeable relational laws of the language of graphs on `ℕ` concentrated on simple graphs, that is, on symmetric irreflexive configurations

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
- [Source of `TauCeti.DenseGraphLimits.InfiniteExchangeableGraphLaw.relationalLawEquiv` in TauCeti/Combinatorics/DenseGraphLimits/ExchangeableGraphLaw/Relational/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/DenseGraphLimits/ExchangeableGraphLaw/Relational/Basic.lean#L141)
- [Tau Ceti roadmap status: Dense graph limits and graphons](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/DenseGraphLimits/STATUS.md)
