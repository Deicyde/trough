---
declaration: theorem
origin: cited
lean: Balaban.logPartition_multiscale, Balaban.lowTemperature_correlations
statement: formalized
---

# balaban-lean

*Balaban's low-temperature renormalization group for O(N) spin models, in Lean 4*

[scottnarmstrong/balaban-lean](https://github.com/scottnarmstrong/balaban-lean) at commit [493e9eb9](https://github.com/scottnarmstrong/balaban-lean/tree/493e9eb97292ebf6070c1c217a09bcf1adc23857), 2026-10-22.

> This repository is a formalization in progress, in [Lean 4](https://lean-lang.org/) with [Mathlib](https://github.com/leanprover-community/mathlib4), of Tadeusz Balaban's renormalization-group analysis of the classical O(N) spin model at low temperature. The papers it follows were published in 1995–1999, the last two with Michael O'Carroll; [docs/PAPERS.md](https://github.com/scottnarmstrong/balaban-lean/blob/493e9eb97292ebf6070c1c217a09bcf1adc23857/docs/PAPERS.md) lists them.

*Quoted from [README.md](https://github.com/scottnarmstrong/balaban-lean/blob/493e9eb97292ebf6070c1c217a09bcf1adc23857/README.md), Apache-2.0.*

## Depends on

- [Finite set](../../../data-structures/sets/finite-set.md)
- [Exponential](../../special-functions/exponential.md)
- [Limit of a map with respect to filters](../../../topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)

## Proof depends on

- [Reflection](../../hilbert-spaces/reflection.md)
- [Product of finitely many measures](../../measures-and-integral-calculus/part-02/product-of-finitely-many-measures.md)
- [Analytic function](../../differentiability/analytic-function.md)
- [The Number of Subsets of a Set](../../../../hundred-theorems/part-02/the-number-of-subsets-of-a-set.md)
- [Existence of an eigenvalue](../../../linear-algebra/structure-theory-of-endomorphisms/existence-of-an-eigenvalue.md)
- [Conditional probability](../../../probability-theory/definitions-in-probability-theory/conditional-probability.md)
- [The Triangle Inequality](../../../../hundred-theorems/part-04/the-triangle-inequality.md)
- [Cauchy filter](../../../topology/uniform-notions/cauchy-filter.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`Balaban.logPartition_multiscale`](https://github.com/scottnarmstrong/balaban-lean/blob/493e9eb97292ebf6070c1c217a09bcf1adc23857/Balaban/Frozen/Roots/LogPartitionMultiscale.lean#L42) (theorem, its text holds `sorry`)
- [`Balaban.lowTemperature_correlations`](https://github.com/scottnarmstrong/balaban-lean/blob/493e9eb97292ebf6070c1c217a09bcf1adc23857/Balaban/Frozen/Roots/LowTemperatureCorrelations.lean#L36) (theorem, its text holds `sorry`)

Of the files its headlines import, directly or not, `Balaban/Frozen/Roots/LogPartitionMultiscale.lean`, `Balaban/Frozen/Roots/LowTemperatureCorrelations.lean` hold `sorry` or `admit`.

## Project

- Lean v4.35.0-rc2, Mathlib at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- 3,714 .lean files; its Lean libraries `Balaban` hold 3,714, declaring 39,933 names, with `sorry` in 2 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/scottnarmstrong/balaban-lean/blob/493e9eb97292ebf6070c1c217a09bcf1adc23857/LICENSE)).

## Builds on

- Mathlib, at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).

## Placement

Of its imports of Mathlib modules in an overview area, 458 of 662 are in Analysis, 2.5 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (458 of 662 imports, 2.5×), General algebra (67 of 662 imports, 0.3×). *Proof depends on* lists 8 of the 93 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [scottnarmstrong/balaban-lean at 493e9eb9](https://github.com/scottnarmstrong/balaban-lean/tree/493e9eb97292ebf6070c1c217a09bcf1adc23857)
