---
declaration: module
origin: cited
lean: BlockBand
statement: formalized
---

# BandMatrixQUE

*Quantum Unique Ergodicity and the Critical Crossover for Band Matrices*

[AxiomMath/BandMatrixQUE](https://github.com/AxiomMath/BandMatrixQUE) at commit [ad595200](https://github.com/AxiomMath/BandMatrixQUE/tree/ad59520033d1ed202d582b256232d5ead86fa735), 2026-11-13.

> This is a Lean formalization of Theorems 1.1, 1.3 and 1.4 of [Quantum unique ergodicity and the critical crossover for 1-d Gaussian band matrices](https://arxiv.org/abs/2611.15085) by Promit Ghosal and Guillaume Remy.

*Quoted from [README.md](https://github.com/AxiomMath/BandMatrixQUE/blob/ad59520033d1ed202d582b256232d5ead86fa735/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Cauchy integral formula](../../analysis/complex-analysis/cauchy-integral-formula.md)
- [Gram-Schmidt orthogonalisation](../../../undergraduate/bilinear-and-quadratic-forms-over-a-vector-space/orthogonality/gram-schmidt-orthogonalisation.md)
- [Rank of a linear map](../../../undergraduate/linear-algebra/finite-dimensional-vector-spaces/rank-of-a-linear-map.md)
- [Stieltjes measure](../../analysis/measures-and-integral-calculus/part-01/stieltjes-measure.md)
- [Parseval formula for Fourier series](../../analysis/fourier-analysis/parseval-formula-for-fourier-series.md)
- [Stopping time](../stochastic-processes/stopping-time.md)
- [Fatou's lemma](../../analysis/measures-and-integral-calculus/part-01/fatous-lemma.md)
- [Martingale](../stochastic-processes/martingale.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`BlockBand`](https://github.com/AxiomMath/BandMatrixQUE/blob/ad59520033d1ed202d582b256232d5ead86fa735/BlockBand.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files it imports, directly or not, `BlockBand/SourceProcess/PhysApprox/B3FddMod.lean`, `BlockBand/SourceProcess/PhysApprox/B3ModulMain.lean`, `BlockBand/SourceProcess/Stochastic/SemimartingaleIto/LocData.lean` hold `sorry` or `admit`.

## Project

- Lean v4.35.0-rc3, Mathlib at [3b531c35](https://github.com/leanprover-community/mathlib4/tree/3b531c35df33d6bbe64b4e87dec056211d3a5676).
- 5,387 .lean files; its Lean libraries `BlockBand`, `BlockBandChallenge`, `BlockBandSolution` hold 5,000 (the first read), declaring 56,396 names, with `sorry` in 3 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/AxiomMath/BandMatrixQUE/blob/ad59520033d1ed202d582b256232d5ead86fa735/LICENSE)).

## Builds on

- Mathlib, at [3b531c35](https://github.com/leanprover-community/mathlib4/tree/3b531c35df33d6bbe64b4e87dec056211d3a5676).

## Placement

Of its imports of Mathlib modules in an overview area, 268 of 2254 are in Probability Theory, 6.3 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Probability Theory (268 of 2254 imports, 6.3×), Analysis (1379 of 2254 imports, 2.3×). *Proof depends on* names 8 of the 152 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [AxiomMath/BandMatrixQUE at ad595200](https://github.com/AxiomMath/BandMatrixQUE/tree/ad59520033d1ed202d582b256232d5ead86fa735)
