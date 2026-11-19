---
declaration: theorem
origin: cited
lean: HypoellipticAleksandrov.KineticAleksandrov.kinetic_aleksandrov_timeVelocity, HypoellipticAleksandrov.KineticAleksandrov.kinetic_aleksandrov_timeVelocity_localised, HypoellipticAleksandrov.KineticAleksandrov.kinetic_aleksandrov_autonomous, HypoellipticAleksandrov.KineticAleksandrov.kinetic_aleksandrov_autonomous_localised, HypoellipticAleksandrov.KineticAleksandrov.existsUnique_bellmanAdjointExponent, HypoellipticAleksandrov.KineticAleksandrov.kinetic_aleksandrov_autonomous_counterexample, HypoellipticAleksandrov.KineticAleksandrov.kinetic_holder_of_aleksandrov, HypoellipticAleksandrov.KineticAleksandrov.Holder.kinetic_crawling_ink_spots
statement: formalized
proof: formalized
---

# hypoelliptic-aleksandrov

*Kinetic Aleksandrov estimates, formalised in Lean 4*

[amelieloher/hypoelliptic-aleksandrov](https://github.com/amelieloher/hypoelliptic-aleksandrov) at commit [d7e01258](https://github.com/amelieloher/hypoelliptic-aleksandrov/tree/d7e0125892d7bbd013c86c9c5d6a04e39e0168a6), 2026-10-09.

## Depends on

- [Measurable function](../../measures-and-integral-calculus/part-01/measurable-function.md)
- [Closure](../../../topology/general-topology/part-01/closure.md)
- [$C^k$ function](../../differentiability/c-k-function.md)
- [Limit of a map with respect to filters](../../../topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)
- [Compactness in terms of filters](../../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Positive measure](../../measures-and-integral-calculus/part-01/positive-measure.md)
- [Set](../../../data-structures/sets/set.md)
- [hoermander-rothschild-stein](amelieloher--hoermander-rothschild-stein.md)

## Proof depends on

- [Tietze extension theorem](../../../../thousand-plus/geometry-and-topology/54-general-topology/tietze-extension-theorem.md)
- [Inner product space $L^2$](../../../../undergraduate/topology/hilbert-spaces/inner-product-space-l-2-2.md)
- [Convexity inequalities](../../convexity/convexity-inequalities.md)
- [Leibniz formula (Analysis)](../../differentiability/leibniz-formula.md)
- [Differentiability of the limit of a sequence of functions](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/differentiability-of-the-limit-of-a-sequence-of.md)
- [Approximation by convolution](../../measures-and-integral-calculus/part-02/approximation-by-convolution.md)
- [Fatou's lemma](../../measures-and-integral-calculus/part-01/fatous-lemma.md)
- [Power functions](../../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/power-functions.md)

## Main results

Its Lean names are 8 of the 19 theorems its README names in code:

- [`HypoellipticAleksandrov.KineticAleksandrov.kinetic_aleksandrov_timeVelocity`](https://github.com/amelieloher/hypoelliptic-aleksandrov/blob/d7e0125892d7bbd013c86c9c5d6a04e39e0168a6/HypoellipticAleksandrov/Statements/KineticAleksandrovTimeVelocity.lean#L31) (theorem)
- [`HypoellipticAleksandrov.KineticAleksandrov.kinetic_aleksandrov_timeVelocity_localised`](https://github.com/amelieloher/hypoelliptic-aleksandrov/blob/d7e0125892d7bbd013c86c9c5d6a04e39e0168a6/HypoellipticAleksandrov/Statements/KineticAleksandrovTimeVelocityLocalised.lean#L31) (theorem)
- [`HypoellipticAleksandrov.KineticAleksandrov.kinetic_aleksandrov_autonomous`](https://github.com/amelieloher/hypoelliptic-aleksandrov/blob/d7e0125892d7bbd013c86c9c5d6a04e39e0168a6/HypoellipticAleksandrov/Statements/KineticAleksandrovAutonomous.lean#L28) (theorem)
- [`HypoellipticAleksandrov.KineticAleksandrov.kinetic_aleksandrov_autonomous_localised`](https://github.com/amelieloher/hypoelliptic-aleksandrov/blob/d7e0125892d7bbd013c86c9c5d6a04e39e0168a6/HypoellipticAleksandrov/Statements/KineticAleksandrovAutonomousLocalised.lean#L27) (theorem)
- [`HypoellipticAleksandrov.KineticAleksandrov.existsUnique_bellmanAdjointExponent`](https://github.com/amelieloher/hypoelliptic-aleksandrov/blob/d7e0125892d7bbd013c86c9c5d6a04e39e0168a6/HypoellipticAleksandrov/Statements/BellmanExponentWellDefined.lean#L21) (theorem)
- [`HypoellipticAleksandrov.KineticAleksandrov.kinetic_aleksandrov_autonomous_counterexample`](https://github.com/amelieloher/hypoelliptic-aleksandrov/blob/d7e0125892d7bbd013c86c9c5d6a04e39e0168a6/HypoellipticAleksandrov/Statements/KineticAleksandrovCounterexample.lean#L23) (theorem)
- [`HypoellipticAleksandrov.KineticAleksandrov.kinetic_holder_of_aleksandrov`](https://github.com/amelieloher/hypoelliptic-aleksandrov/blob/d7e0125892d7bbd013c86c9c5d6a04e39e0168a6/HypoellipticAleksandrov/Statements/KineticHolder.lean#L24) (theorem)
- [`HypoellipticAleksandrov.KineticAleksandrov.Holder.kinetic_crawling_ink_spots`](https://github.com/amelieloher/hypoelliptic-aleksandrov/blob/d7e0125892d7bbd013c86c9c5d6a04e39e0168a6/HypoellipticAleksandrov/Statements/KineticInkSpots.lean#L21) (theorem)

No file its headlines import, directly or not (2357 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0-rc2, Mathlib at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- 2,541 .lean files; its Lean libraries `PDEFoundation`, `HypoellipticAleksandrov`, `FullCoefficientChallenge`, `FullCoefficientSolution`, `KineticAleksandrovChallenge`, `KineticAleksandrovSolution` hold 2,541, declaring 11,658 names, with `sorry` in 2 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/amelieloher/hypoelliptic-aleksandrov/blob/d7e0125892d7bbd013c86c9c5d6a04e39e0168a6/LICENSE)).

## Builds on

- Mathlib, at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- [hormander](amelieloher--hoermander-rothschild-stein.md) at `d1462014`.

## Placement

Of its imports of Mathlib modules in an overview area, 1380 of 1776 are in Analysis, 2.9 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (1380 of 1776 imports, 2.9×), Topology (224 of 1776 imports, 1.7×). *Proof depends on* names 8 of the 100 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [amelieloher/hypoelliptic-aleksandrov at d7e01258](https://github.com/amelieloher/hypoelliptic-aleksandrov/tree/d7e0125892d7bbd013c86c9c5d6a04e39e0168a6)
