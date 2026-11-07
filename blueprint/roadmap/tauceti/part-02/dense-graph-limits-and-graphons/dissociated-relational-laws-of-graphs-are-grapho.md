---
declaration: theorem
origin: cited
lean: TauCeti.DenseGraphLimits.isDissociated_iff_exists_toRelationalLaw_sampleExchangeableLaw
statement: formalized
proof: formalized
---

# Dissociated relational laws of graphs are graphon sampling laws

An exchangeable relational
law of the language of graphs whose marginals are concentrated on simple graphs is dissociated
exactly when it is the relational law of the sampling law of a graphon, which may be taken on any
atomless standard Borel carrier `(Ω, μ)`, such as the unit interval.

```lean
TauCeti.DenseGraphLimits.isDissociated_iff_exists_toRelationalLaw_sampleExchangeableLaw.{u_1}
  {Ω : Type u_1} [MeasurableSpace Ω] (μ : MeasureTheory.Measure Ω)
  [MeasureTheory.IsProbabilityMeasure μ] [StandardBorelSpace Ω] [MeasureTheory.NullSingletonClass μ]
  {ν : TauCeti.Probability.ExchangeableRelationalLaw FirstOrder.Language.graph}
  (hν :
    ∀ (n : ℕ),
      ∀ᵐ (c : TauCeti.RelationalConfiguration FirstOrder.Language.graph (Fin n)) ∂ν.law n,
        c.IsSimpleGraph) :
  ν.IsDissociated ↔ ∃ W, ν = (TauCeti.DenseGraphLimits.sampleExchangeableLaw W).toRelationalLaw
```

## Depends on

- [TauCeti.Probability.ExchangeableRelationalLaw](tauceti-probability-exchangeablerelationallaw.md)

## Proof depends on

- [Frieze--Kannan weak regularity](frieze-kannan-weak-regularity.md)
- [TauCeti.DenseGraphLimits.cutDist](tauceti-densegraphlimits-cutdist.md)
- [TauCeti.DenseGraphLimits.cutDist\_triangle](tauceti-densegraphlimits-cutdist-triangle.md)
- [TauCeti.DenseGraphLimits.Graphon.unitIntervalRepr](tauceti-densegraphlimits-graphon-unitintervalrep.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DenseGraphLimits.isDissociated_iff_exists_toRelationalLaw_sampleExchangeableLaw`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/ExchangeableGraphLaw/Relational/Dissociated.html#TauCeti.DenseGraphLimits.isDissociated_iff_exists_toRelationalLaw_sampleExchangeableLaw).

## Sources

- [Tau Ceti documentation: `TauCeti.DenseGraphLimits.isDissociated_iff_exists_toRelationalLaw_sampleExchangeableLaw`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/ExchangeableGraphLaw/Relational/Dissociated.html#TauCeti.DenseGraphLimits.isDissociated_iff_exists_toRelationalLaw_sampleExchangeableLaw)
- [Source of `TauCeti.DenseGraphLimits.isDissociated_iff_exists_toRelationalLaw_sampleExchangeableLaw` in TauCeti/Combinatorics/DenseGraphLimits/ExchangeableGraphLaw/Relational/Dissociated.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/DenseGraphLimits/ExchangeableGraphLaw/Relational/Dissociated.lean#L96)
- [Tau Ceti roadmap status: Dense graph limits and graphons](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/DenseGraphLimits/STATUS.md)
