---
declaration: theorem
origin: cited
lean: DOZZ.dozz_main, DOZZ.dozz_unitVolume, DOZZ.dozz_existence, DOZZ.equatorGFF_GMC_unique_ae, DOZZ.equatorGFF_circle_average_GMC_exists, DOZZ.structureConstant_infinity_limit, DOZZ.reflection_Rtheor_off_poles, DOZZ.reflection_Rtheor_punctured
statement: formalized
proof: formalized
---

# The DOZZ formula, formalized in Lean 4

[scottnarmstrong/DOZZ](https://github.com/scottnarmstrong/DOZZ) at commit [5d770d1a](https://github.com/scottnarmstrong/DOZZ/tree/5d770d1a6d69fac6dbb63060e8a89861bf3ee330), 2026-10-10.

## Depends on

- [Sigma-algebra](../../measures-and-integral-calculus/part-01/sigma-algebra.md)
- [Positive measure](../../measures-and-integral-calculus/part-01/positive-measure.md)
- [Limit of a map with respect to filters](../../../topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)

## Proof depends on

- [Strong law of large numbers](../../../probability-theory/convergence-of-a-sequence-of-random-variables/strong-law-of-large-numbers.md)
- [Gaussian processes](../../../probability-theory/stochastic-processes/gaussian-processes.md)
- [Extension by continuity](../../../topology/general-topology/part-01/extension-by-continuity.md)
- [Convergence in probability](../../../probability-theory/convergence-of-a-sequence-of-random-variables/convergence-in-probability.md)
- [Log](../../../../undergraduate/single-variable-complex-analysis/complex-valued-series/power-series-expansion-of-elementary-functions/log.md)
- [Uniform integrability](../../measures-and-integral-calculus/part-01/uniform-integrability.md)
- [Uniform convergence](../../../topology/uniform-notions/uniform-convergence.md)
- [Exponential law](../../../probability-theory/random-variables-and-their-laws/exponential-law.md)

## Main results

Its Lean names are 8 of the 11 theorems its README names in code:

- [`DOZZ.dozz_main`](https://github.com/scottnarmstrong/DOZZ/blob/5d770d1a6d69fac6dbb63060e8a89861bf3ee330/DOZZ/Statements/Roots/DozzMain.lean#L20) (theorem)
- [`DOZZ.dozz_unitVolume`](https://github.com/scottnarmstrong/DOZZ/blob/5d770d1a6d69fac6dbb63060e8a89861bf3ee330/DOZZ/Statements/Roots/DozzUnitVolume.lean#L21) (theorem)
- [`DOZZ.dozz_existence`](https://github.com/scottnarmstrong/DOZZ/blob/5d770d1a6d69fac6dbb63060e8a89861bf3ee330/DOZZ/Statements/Roots/DozzExistence.lean#L21) (theorem)
- [`DOZZ.equatorGFF_GMC_unique_ae`](https://github.com/scottnarmstrong/DOZZ/blob/5d770d1a6d69fac6dbb63060e8a89861bf3ee330/DOZZ/Statements/GMC/EquatorGFFGMCUniqueAe.lean#L22) (theorem)
- [`DOZZ.equatorGFF_circle_average_GMC_exists`](https://github.com/scottnarmstrong/DOZZ/blob/5d770d1a6d69fac6dbb63060e8a89861bf3ee330/DOZZ/Statements/GMC/EquatorGFFCircleAverageGMCExists.lean#L22) (theorem)
- [`DOZZ.structureConstant_infinity_limit`](https://github.com/scottnarmstrong/DOZZ/blob/5d770d1a6d69fac6dbb63060e8a89861bf3ee330/DOZZ/Statements/FourPoint/StructureConstantInfinityLimit.lean#L23) (theorem)
- [`DOZZ.reflection_Rtheor_off_poles`](https://github.com/scottnarmstrong/DOZZ/blob/5d770d1a6d69fac6dbb63060e8a89861bf3ee330/DOZZ/Statements/Brownian/ReflectionRtheorOffPoles.lean#L23) (theorem)
- [`DOZZ.reflection_Rtheor_punctured`](https://github.com/scottnarmstrong/DOZZ/blob/5d770d1a6d69fac6dbb63060e8a89861bf3ee330/DOZZ/Statements/Brownian/ReflectionRtheorPunctured.lean#L23) (theorem)

No file its headlines import, directly or not (1960 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0-rc2, Mathlib at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- 2,224 .lean files; its Lean libraries `DOZZ`, `GaussianFields`, `DOZZChallenge`, `DOZZSolution`, `ReflectionChallenge`, `ReflectionSolution` hold 2,224, declaring 10,477 names, with `sorry` in 2 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/scottnarmstrong/DOZZ/blob/5d770d1a6d69fac6dbb63060e8a89861bf3ee330/LICENSE)).

## Builds on

- Mathlib, at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).

## Placement

2 of the 3 Mathlib concepts its headline statements name are in Analysis.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Probability Theory (122 of 1092 imports, 5.9×), Analysis (788 of 1092 imports, 2.7×), Topology (129 of 1092 imports, 1.6×). *Proof depends on* names 8 of the 98 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [scottnarmstrong/DOZZ at 5d770d1a](https://github.com/scottnarmstrong/DOZZ/tree/5d770d1a6d69fac6dbb63060e8a89861bf3ee330)
