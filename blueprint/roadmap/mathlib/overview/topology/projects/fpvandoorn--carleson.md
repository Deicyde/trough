---
declaration: theorem
origin: cited
lean: classical_carleson
statement: formalized
---

# Formalization of a generalized Carleson's theorem

[fpvandoorn/carleson](https://github.com/fpvandoorn/carleson) at commit [d4446d3c](https://github.com/fpvandoorn/carleson/tree/d4446d3cab5d096d936a94e998d24c413b2b017d), 2026-11-13.

> A formalized proof of a generalized Carleson's theorem in the [Lean interactive theorem prover](https://lean-lang.org/).

*Quoted from [README.md](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/README.md), Apache-2.0.*

## Depends on

- [Continuous function](../general-topology/part-01/continuous-function.md)
- [Limit of a map with respect to filters](../general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)

## Proof depends on

- [Integral of positive measurable functions](../../analysis/measures-and-integral-calculus/part-01/integral-of-positive-measurable-functions.md)
- [Convolution](../../analysis/measures-and-integral-calculus/part-02/convolution.md)
- [Regularization by convolution](../../analysis/measures-and-integral-calculus/part-02/regularization-by-convolution.md)
- [Hölder's inequality](../../../undergraduate/measures-and-integral-calculus/integration/holders-inequality.md)
- [Example, the Hilbert basis of trigonometric polynomials](../../../undergraduate/topology/hilbert-spaces/example-the-hilbert-basis-of-trigonometric-polyn.md)
- [Bornology](../../analysis/topological-vector-spaces/bornology.md)
- [Lebesgue measure (Measure theory)](../../../undergraduate/measures-and-integral-calculus/measure-theory/lebesgue-measure.md)
- [Almost sure convergence](../../probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)

## Main results

Its Lean names are the the Lean names of its blueprint's nodes that no other node uses, marked \leanok:

- [`classical_carleson`](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/Carleson/Classical/ClassicalCarleson.lean#L131) (theorem)

## Project

- Lean v4.36.0-rc1, Mathlib at [d8881435](https://github.com/leanprover-community/mathlib4/tree/d88814353fcbcc0461c55b2a4585d3f44d903df1).
- 129 .lean files; its Lean libraries `Carleson`, `Challenge`, `Solution` hold 127, declaring 2,883 names, with `sorry` in 2 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/LICENSE)).

## Builds on

- Mathlib, at [d8881435](https://github.com/leanprover-community/mathlib4/tree/d88814353fcbcc0461c55b2a4585d3f44d903df1).

## Placement

2 of the 2 Mathlib concepts its headline statements name are in Topology.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (59 of 78 imports, 2.4×), Topology (10 of 78 imports, 2.0×). *Proof depends on* names 8 of the 57 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [fpvandoorn/carleson at d4446d3c](https://github.com/fpvandoorn/carleson/tree/d4446d3cab5d096d936a94e998d24c413b2b017d)
