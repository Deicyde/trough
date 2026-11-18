---
declaration: theorem
origin: cited
lean: Cochrane.AssetsRulesBalanceSheets.PresentValue.flow_tvc_iff_pv, Cochrane.AssetsRulesBalanceSheets.PresentValue.real_flow_tvc_iff, Cochrane.AssetsRulesBalanceSheets.PresentValue.tendsto_partialSums_of_tvc, Cochrane.AssetsRulesBalanceSheets.PresentValue.eq_zero_of_tvc, Cochrane.AssetsRulesBalanceSheets.RealDebt.indexedFlow_price_free, Cochrane.AssetsRulesBalanceSheets.RealDebt.indexed_pv_news_zero, Cochrane.AssetsRulesBalanceSheets.RealDebt.nominalOutstanding_price_unique, Cochrane.AssetsRulesBalanceSheets.RealDebt.foreign_default_required
statement: formalized
proof: formalized
---

# Monetary Economics in Lean

[LeanEconomics/MonetaryEconomics](https://github.com/LeanEconomics/MonetaryEconomics) at commit [98285751](https://github.com/LeanEconomics/MonetaryEconomics/tree/982857516ec165beb174770444991f9123f7a252), 2026-11-12.

> Checked monetary economics, following three textbooks: Jordi Galí, *Monetary Policy, Inflation, and the Business Cycle: An Introduction to the New Keynesian Framework and Its Applications* (2nd ed., 2015); Michael Woodford, *Interest and Prices: Foundations of a Theory of Monetary Policy* (2003); and John H. Cochrane, *The Fiscal Theory of the Price Level* (Princeton University Press).

*Quoted from [README.md](https://github.com/LeanEconomics/MonetaryEconomics/blob/982857516ec165beb174770444991f9123f7a252/README.md), Apache-2.0.*

## Depends on

- [Limit of a map with respect to filters](../../topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)

## Proof depends on

- [Divergence of the Harmonic Series](../../../hundred-theorems/part-02/divergence-of-the-harmonic-series.md)
- [The Non-Denumerability of the Continuum](../../../hundred-theorems/part-01/the-non-denumerability-of-the-continuum.md)
- [Independent sigma-algebras](../definitions-in-probability-theory/independent-sigma-algebras.md)
- [Product of sigma-algebras](../../../undergraduate/measures-and-integral-calculus/measure-theory/product-of-sigma-algebras.md)
- [Infinite sum](../../topology/topological-algebra/infinite-sum.md)
- [Almost sure convergence](../convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Intermediate value theorem](../../topology/topological-algebra/intermediate-value-theorem.md)
- [Vector-valued integrable function (Bochner integral)](../../analysis/measures-and-integral-calculus/part-01/vector-valued-integrable-function-bochner-integr.md)

## Main results

Its Lean names are 8 of the 164 theorems its README names in code:

- [`Cochrane.AssetsRulesBalanceSheets.PresentValue.flow_tvc_iff_pv`](https://github.com/LeanEconomics/MonetaryEconomics/blob/982857516ec165beb174770444991f9123f7a252/Cochrane/AssetsRulesBalanceSheets/AssetsRulesBalanceSheets/PresentValue.lean#L121) (theorem)
- [`Cochrane.AssetsRulesBalanceSheets.PresentValue.real_flow_tvc_iff`](https://github.com/LeanEconomics/MonetaryEconomics/blob/982857516ec165beb174770444991f9123f7a252/Cochrane/AssetsRulesBalanceSheets/AssetsRulesBalanceSheets/PresentValue.lean#L165) (theorem)
- [`Cochrane.AssetsRulesBalanceSheets.PresentValue.tendsto_partialSums_of_tvc`](https://github.com/LeanEconomics/MonetaryEconomics/blob/982857516ec165beb174770444991f9123f7a252/Cochrane/AssetsRulesBalanceSheets/AssetsRulesBalanceSheets/PresentValue.lean#L93) (theorem)
- [`Cochrane.AssetsRulesBalanceSheets.PresentValue.eq_zero_of_tvc`](https://github.com/LeanEconomics/MonetaryEconomics/blob/982857516ec165beb174770444991f9123f7a252/Cochrane/AssetsRulesBalanceSheets/AssetsRulesBalanceSheets/PresentValue.lean#L137) (theorem)
- [`Cochrane.AssetsRulesBalanceSheets.RealDebt.indexedFlow_price_free`](https://github.com/LeanEconomics/MonetaryEconomics/blob/982857516ec165beb174770444991f9123f7a252/Cochrane/AssetsRulesBalanceSheets/AssetsRulesBalanceSheets/RealDebt.lean#L94) (theorem)
- [`Cochrane.AssetsRulesBalanceSheets.RealDebt.indexed_pv_news_zero`](https://github.com/LeanEconomics/MonetaryEconomics/blob/982857516ec165beb174770444991f9123f7a252/Cochrane/AssetsRulesBalanceSheets/AssetsRulesBalanceSheets/RealDebt.lean#L134) (theorem)
- [`Cochrane.AssetsRulesBalanceSheets.RealDebt.nominalOutstanding_price_unique`](https://github.com/LeanEconomics/MonetaryEconomics/blob/982857516ec165beb174770444991f9123f7a252/Cochrane/AssetsRulesBalanceSheets/AssetsRulesBalanceSheets/RealDebt.lean#L191) (theorem)
- [`Cochrane.AssetsRulesBalanceSheets.RealDebt.foreign_default_required`](https://github.com/LeanEconomics/MonetaryEconomics/blob/982857516ec165beb174770444991f9123f7a252/Cochrane/AssetsRulesBalanceSheets/AssetsRulesBalanceSheets/RealDebt.lean#L264) (theorem)

No file its headlines import, directly or not (5 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.34.0, Mathlib at [5ed29652](https://github.com/leanprover-community/mathlib4/tree/5ed2965256430c3649e86755f9576b54eca72435).
- 1,404 .lean files; its Lean libraries `AssetsRulesBalanceSheets` hold 45, declaring 1,190 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/LeanEconomics/MonetaryEconomics/blob/982857516ec165beb174770444991f9123f7a252/LICENSE)).

## Builds on

- Mathlib, at [5ed29652](https://github.com/leanprover-community/mathlib4/tree/5ed2965256430c3649e86755f9576b54eca72435).

## Placement

Of its imports of Mathlib modules in an overview area, 9 of 49 are in Probability Theory, 9.7 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Probability Theory (9 of 49 imports, 9.7×), Analysis (26 of 49 imports, 2.0×), Topology (5 of 49 imports, 1.4×). *Proof depends on* names 8 of the 27 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [LeanEconomics/MonetaryEconomics at 98285751](https://github.com/LeanEconomics/MonetaryEconomics/tree/982857516ec165beb174770444991f9123f7a252)
