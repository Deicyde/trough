---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.MaxNTimesCoverage.Instance, MetaMathlibExt.Complexity.NPComplete.MaxNTimesCoverage.WellFormed, MetaMathlibExt.Complexity.NPComplete.MaxNTimesCoverage.coveredWeight, MetaMathlibExt.Complexity.NPComplete.MaxNTimesCoverage.Feasible, MetaMathlibExt.Complexity.NPComplete.MaxNTimesCoverage.maxNTimesCoverageDec, MetaMathlibExt.Complexity.NPComplete.MaxNTimesCoverage.maxNTimesCoverage_npComplete
statement: formalized
---

# Maximum n-times coverage

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/maximum-n-times-coverage/index.html).

## Instance of maximum n-times coverage

An instance: `n`, the coverage rows of the overlays, element weights, `k`, `τ`.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaxNTimesCoverage.Instance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/MaxNTimesCoverageWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MaxNTimesCoverageWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/maximum-n-times-coverage/index.html#instance).

## Well-formed maximum n-times coverage instance

Well-formedness: every row has one entry per element.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaxNTimesCoverage.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/MaxNTimesCoverageWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MaxNTimesCoverageWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/maximum-n-times-coverage/index.html#well-formed).

## Weight covered at least n times

The weight of the elements covered at least `n` times by the rows `sub`.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaxNTimesCoverage.coveredWeight`, a definition declared in [WantedExt/Complexity/NPComplete/MaxNTimesCoverageWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MaxNTimesCoverageWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/maximum-n-times-coverage/index.html#covered-weight).

## Feasibility for maximum n-times coverage

At most `k` overlays cover weight at least `τ` at least `n` times.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaxNTimesCoverage.Feasible`, a definition declared in [WantedExt/Complexity/NPComplete/MaxNTimesCoverageWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MaxNTimesCoverageWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/maximum-n-times-coverage/index.html#feasible).

## Maximum n-times coverage decision problem

MAXIMUM n-TIMES COVERAGE as a decision problem over bitstrings.

Formalized by `MetaMathlibExt.Complexity.NPComplete.MaxNTimesCoverage.maxNTimesCoverageDec`, a definition declared in [WantedExt/Complexity/NPComplete/MaxNTimesCoverageWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MaxNTimesCoverageWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/maximum-n-times-coverage/index.html#max-ntimes-coverage-dec).

## MAXIMUM n-TIMES COVERAGE is NP-complete

**MAXIMUM n-TIMES COVERAGE is NP-complete** (Liu, Dimitrakakis, Carter and Gifford 2022).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.MaxNTimesCoverage.maxNTimesCoverage_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/MaxNTimesCoverageWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/MaxNTimesCoverageWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/maximum-n-times-coverage/index.html#max-ntimes-coverage-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Maximum n-times coverage](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/maximum-n-times-coverage/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/set-systems-and-location/maximum-n-times-coverage)
