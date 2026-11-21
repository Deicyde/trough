---
declaration: theorem
origin: cited
lean: Miao.Applications.od_option_exists_unique, Miao.Applications.od_option_threshold, Miao.Applications.od_option_threshold_gt_iff, Miao.Applications.od_option_threshold_dirac, Miao.Applications.od_wait_mean, Miao.Applications.od_wait_mean_misprint, Miao.Applications.od_option_riskier, Miao.Applications.od_mccall_reservation
statement: formalized
proof: formalized
---

# Dynamic Programming in Lean

[LeanEconomics/DynamicProgramming](https://github.com/LeanEconomics/DynamicProgramming) at commit [78fa683c](https://github.com/LeanEconomics/DynamicProgramming/tree/78fa683cf72424e2f14d9a5d5dd5d43c9e5044e2), 2026-11-11.

> Checked dynamic programming, following Sargent and Stachurski, *Dynamic Programming*, Volume 1: *Finite States* and Volume 2: *General States*; Stokey and Lucas with Prescott, *Recursive Methods in Economic Dynamics*; and Miao, *Economic Dynamics in Discrete Time*. Each folder is an independent Lean/Mathlib project for one chapter, with precise statements, a source map to the book's results and pages, and reproducible proof checks. Volume 1 projects live under `FiniteStates/`, Volume 2 under `GeneralStates/`, Stokey–Lucas–Prescott under `RecursiveMethods/`, Miao under `EconomicDynamics/`.

*Quoted from [README.md](https://github.com/LeanEconomics/DynamicProgramming/blob/78fa683cf72424e2f14d9a5d5dd5d43c9e5044e2/README.md), Apache-2.0.*

## Depends on

- [Infinite sum](../../topology/topological-algebra/infinite-sum.md)
- [Probability measure](../definitions-in-probability-theory/probability-measure.md)
- [Positive measure](../../analysis/measures-and-integral-calculus/part-01/positive-measure.md)

## Proof depends on

- [Geometric law](../random-variables-and-their-laws/geometric-law.md)
- [Bolzano-Weierstrass theorem (Topology of R)](../../../undergraduate/single-variable-real-analysis/topology-of-r/bolzano-weierstrass-theorem.md)
- [Uniformly continuous function](../../topology/uniform-notions/uniformly-continuous-function.md)
- [Extended real number](../../general-algebra/numbers/extended-real-number.md)
- [Convergence in distribution](../convergence-of-a-sequence-of-random-variables/convergence-in-distribution.md)
- [Product of sigma-algebras](../../../undergraduate/measures-and-integral-calculus/measure-theory/product-of-sigma-algebras.md)
- [Metric space](../../topology/metric-spaces/metric-space.md)
- [Uniform convergence](../../topology/uniform-notions/uniform-convergence.md)

## Main results

Its Lean names are 8 of the 55 theorems its README names in code:

- [`Miao.Applications.od_option_exists_unique`](https://github.com/LeanEconomics/DynamicProgramming/blob/78fa683cf72424e2f14d9a5d5dd5d43c9e5044e2/EconomicDynamics/Applications/Applications/ODOption.lean#L117) (theorem)
- [`Miao.Applications.od_option_threshold`](https://github.com/LeanEconomics/DynamicProgramming/blob/78fa683cf72424e2f14d9a5d5dd5d43c9e5044e2/EconomicDynamics/Applications/Applications/ODOption.lean#L141) (theorem)
- [`Miao.Applications.od_option_threshold_gt_iff`](https://github.com/LeanEconomics/DynamicProgramming/blob/78fa683cf72424e2f14d9a5d5dd5d43c9e5044e2/EconomicDynamics/Applications/Applications/ODOption.lean#L303) (theorem)
- [`Miao.Applications.od_option_threshold_dirac`](https://github.com/LeanEconomics/DynamicProgramming/blob/78fa683cf72424e2f14d9a5d5dd5d43c9e5044e2/EconomicDynamics/Applications/Applications/ODOption.lean#L340) (theorem)
- [`Miao.Applications.od_wait_mean`](https://github.com/LeanEconomics/DynamicProgramming/blob/78fa683cf72424e2f14d9a5d5dd5d43c9e5044e2/EconomicDynamics/Applications/Applications/ODWaiting.lean#L98) (theorem)
- [`Miao.Applications.od_wait_mean_misprint`](https://github.com/LeanEconomics/DynamicProgramming/blob/78fa683cf72424e2f14d9a5d5dd5d43c9e5044e2/EconomicDynamics/Applications/Applications/ODWaiting.lean#L125) (theorem)
- [`Miao.Applications.od_option_riskier`](https://github.com/LeanEconomics/DynamicProgramming/blob/78fa683cf72424e2f14d9a5d5dd5d43c9e5044e2/EconomicDynamics/Applications/Applications/ODRisk.lean#L68) (theorem)
- [`Miao.Applications.od_mccall_reservation`](https://github.com/LeanEconomics/DynamicProgramming/blob/78fa683cf72424e2f14d9a5d5dd5d43c9e5044e2/EconomicDynamics/Applications/Applications/ODMcCall.lean#L273) (theorem)

No file its headlines import, directly or not (14 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.34.0, Mathlib at [5ed29652](https://github.com/leanprover-community/mathlib4/tree/5ed2965256430c3649e86755f9576b54eca72435).
- 3,702 .lean files; its Lean libraries `Applications` hold 102, declaring 1,732 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/LeanEconomics/DynamicProgramming/blob/78fa683cf72424e2f14d9a5d5dd5d43c9e5044e2/LICENSE)).

## Builds on

- Mathlib, at [5ed29652](https://github.com/leanprover-community/mathlib4/tree/5ed2965256430c3649e86755f9576b54eca72435).

## Placement

Of its imports of Mathlib modules in an overview area, 23 of 164 are in Probability Theory, 7.4 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Probability Theory (23 of 164 imports, 7.4×), Analysis (101 of 164 imports, 2.3×), Topology (27 of 164 imports, 2.2×). *Proof depends on* lists 8 of the 46 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [LeanEconomics/DynamicProgramming at 78fa683c](https://github.com/LeanEconomics/DynamicProgramming/tree/78fa683cf72424e2f14d9a5d5dd5d43c9e5044e2)
