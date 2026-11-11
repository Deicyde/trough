---
declaration: theorem
origin: cited
lean: TauCeti.DenseGraphLimits.InfiniteExchangeableGraphLaw.existsUnique_bind_infiniteSampleLawOnSpace
statement: formalized
proof: formalized
---

# Every exchangeable law on infinite graphs is a graphon mixture, for exactly one mixing measure

The integral form of the Diaconis–Janson correspondence: the law is the bind of a
unique probability measure on graphon space against the joint sampling laws.

```lean
TauCeti.DenseGraphLimits.InfiniteExchangeableGraphLaw.existsUnique_bind_infiniteSampleLawOnSpace
  (L : TauCeti.DenseGraphLimits.InfiniteExchangeableGraphLaw) :
  ∃! P, (↑P).bind TauCeti.DenseGraphLimits.infiniteSampleLawOnSpace = L.law
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A measurable function on a product factors through Boolean coordinates](a-measurable-function-on-a-product-factors-throu.md)
- [Frieze--Kannan weak regularity](frieze-kannan-weak-regularity.md)
- [Hoeffding's lemma, oscillation form](../../probability/moments/hoeffdings-lemma-oscillation-form.md)
- [TauCeti.DenseGraphLimits.cutDist](tauceti-densegraphlimits-cutdist.md)
- [TauCeti.DenseGraphLimits.cutDist_triangle](tauceti-densegraphlimits-cutdist-triangle.md)
- [TauCeti.Probability.empiricalFiniteMeasure](../../probability/random-matrices/tauceti-probability-empiricalfinitemeasure.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DenseGraphLimits.InfiniteExchangeableGraphLaw.existsUnique_bind_infiniteSampleLawOnSpace`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/ExchangeableGraphLaw/Infinite/Mixture.html#TauCeti.DenseGraphLimits.InfiniteExchangeableGraphLaw.existsUnique_bind_infiniteSampleLawOnSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.DenseGraphLimits.InfiniteExchangeableGraphLaw.existsUnique_bind_infiniteSampleLawOnSpace`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/ExchangeableGraphLaw/Infinite/Mixture.html#TauCeti.DenseGraphLimits.InfiniteExchangeableGraphLaw.existsUnique_bind_infiniteSampleLawOnSpace)
- [Source of `TauCeti.DenseGraphLimits.InfiniteExchangeableGraphLaw.existsUnique_bind_infiniteSampleLawOnSpace` in TauCeti/Combinatorics/DenseGraphLimits/ExchangeableGraphLaw/Infinite/Mixture.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/DenseGraphLimits/ExchangeableGraphLaw/Infinite/Mixture.lean#L87)
- [Tau Ceti roadmap status: Dense graph limits and graphons](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/DenseGraphLimits/STATUS.md)
