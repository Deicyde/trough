---
declaration: theorem
origin: cited
lean: SubdiffusiveProcess.process_convergence, SubdiffusiveProcess.process_convergence_precise, SubdiffusiveProcess.quantitative_homogenization, SubdiffusiveProcess.anomalous_holder_regularity, SubdiffusiveProcess.Model.nonempty_gmcModel_of_zeroLevelLaw
statement: formalized
---

# subdiffusive-process

*Anomalous scaling limit of a Brownian particle in a log-correlated potential*

[nitromannitol/subdiffusive-process](https://github.com/nitromannitol/subdiffusive-process) at commit [4c6b8fa6](https://github.com/nitromannitol/subdiffusive-process/tree/4c6b8fa60357a07fd5713e5104a6cc70f8e432dc), 2026-10-08.

## Depends on

- [Borel sigma-algebra](../../analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Continuous function](../../topology/general-topology/part-01/continuous-function.md)
- [Limit of a map with respect to filters](../../topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)
- [Measurable function](../../analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Sigma-algebra](../../analysis/measures-and-integral-calculus/part-01/sigma-algebra.md)
- [Positive measure](../../analysis/measures-and-integral-calculus/part-01/positive-measure.md)
- [Ball](../../topology/metric-spaces/ball.md)
- [Gaussian measures](../random-variables-and-their-laws/gaussian-measures.md)
- [Exponential](../../analysis/special-functions/exponential.md)
- [Logarithm](../../analysis/special-functions/logarithm.md)
- [Compactness in terms of filters](../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Events](../../../undergraduate/probability-theory/definitions-of-a-probability-space/events.md)
- [Probability measure](../definitions-in-probability-theory/probability-measure.md)
- [Set](../../data-structures/sets/set.md)

## Proof depends on

- [Independent events](../definitions-in-probability-theory/independent-events.md)
- [Kolmogorov's $0$-$1$ law](../random-variables-and-their-laws/kolmogorovs-0-1-law.md)
- [Exponential law](../random-variables-and-their-laws/exponential-law.md)
- [Independent sigma-algebras](../definitions-in-probability-theory/independent-sigma-algebras.md)
- [Markov inequality](../convergence-of-a-sequence-of-random-variables/markov-inequality.md)
- [Borel-Cantelli lemma (easy direction)](../../../undergraduate/probability-theory/definitions-of-a-probability-space/borel-cantelli-lemma-easy-direction.md)
- [Hausdorff measure](../../analysis/measures-and-integral-calculus/part-01/hausdorff-measure.md)
- [Approximation by step functions](../../../undergraduate/measures-and-integral-calculus/measure-theory/approximation-by-step-functions.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`SubdiffusiveProcess.process_convergence`](https://github.com/nitromannitol/subdiffusive-process/blob/4c6b8fa60357a07fd5713e5104a6cc70f8e432dc/SubdiffusiveProcess/MainTheorems.lean#L31) (theorem)
- [`SubdiffusiveProcess.process_convergence_precise`](https://github.com/nitromannitol/subdiffusive-process/blob/4c6b8fa60357a07fd5713e5104a6cc70f8e432dc/SubdiffusiveProcess/MainTheorems.lean#L133) (theorem)
- [`SubdiffusiveProcess.quantitative_homogenization`](https://github.com/nitromannitol/subdiffusive-process/blob/4c6b8fa60357a07fd5713e5104a6cc70f8e432dc/SubdiffusiveProcess/MainTheorems.lean#L263) (theorem)
- [`SubdiffusiveProcess.anomalous_holder_regularity`](https://github.com/nitromannitol/subdiffusive-process/blob/4c6b8fa60357a07fd5713e5104a6cc70f8e432dc/SubdiffusiveProcess/MainTheorems.lean#L404) (theorem)
- [`SubdiffusiveProcess.Model.nonempty_gmcModel_of_zeroLevelLaw`](https://github.com/nitromannitol/subdiffusive-process/blob/4c6b8fa60357a07fd5713e5104a6cc70f8e432dc/SubdiffusiveProcess/Model/ZeroLevel.lean#L186) (theorem)

## Project

- Lean v4.35.0-rc2, Mathlib at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- 5,895 .lean files; its Lean libraries `SubdiffusiveProcess`, `SubdiffusiveProcessAudit` hold 5,000 (the first read), declaring 37,241 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/nitromannitol/subdiffusive-process/blob/4c6b8fa60357a07fd5713e5104a6cc70f8e432dc/LICENSE)).

## Builds on

- Mathlib, at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- `CoarseGraining` (https://github.com/scottnarmstrong/CoarseGraining) at `310d1a6b`.
- `MarkovProcess` (https://github.com/scottnarmstrong/MarkovProcess) at `666cda02`.

## Placement

Of its imports of Mathlib modules in an overview area, 274 of 2185 are in Probability Theory, 6.6 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Probability Theory (274 of 2185 imports, 6.6×), Topology (443 of 2185 imports, 2.7×), Analysis (1193 of 2185 imports, 2.0×). *Proof depends on* lists 8 of the 143 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [nitromannitol/subdiffusive-process at 4c6b8fa6](https://github.com/nitromannitol/subdiffusive-process/tree/4c6b8fa60357a07fd5713e5104a6cc70f8e432dc)
