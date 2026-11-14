---
declaration: theorem
origin: cited
lean: BlockBand.Critical.BoundaryMean.exactBoundaryMean_of_inputs, BlockBand.Critical.Herglotz.herglotzTail, BlockBand.Critical.MatrixClosing.middle_error_arith, BlockBand.Critical.MatrixClosing.mem_bulkInterval_half, BlockBand.Critical.MatrixClosing.bulkInterval_mono_half, BlockBand.Critical.MatrixClosing.strictMiddle_of_exactBoundaryMean, BlockBand.Critical.MatrixClosing.middleKernel_radial, BlockBand.Critical.MatrixClosing.middleShiftBoundaryMean_of_exactBoundaryMean
statement: formalized
---

# Quantum Unique Ergodicity and the Critical Crossover for Band Matrices

[AxiomMath/BandMatrixQUE](https://github.com/AxiomMath/BandMatrixQUE) at commit [ad595200](https://github.com/AxiomMath/BandMatrixQUE/tree/ad59520033d1ed202d582b256232d5ead86fa735), 2026-11-13.

> This is a Lean formalization of Theorems 1.1, 1.3 and 1.4 of [Quantum unique ergodicity and the critical crossover for 1-d Gaussian band matrices](https://arxiv.org/abs/2611.15085) by Promit Ghosal and Guillaume Remy.

*Quoted from [README.md](https://github.com/AxiomMath/BandMatrixQUE/blob/ad59520033d1ed202d582b256232d5ead86fa735/README.md), Apache-2.0.*

## Depends on

- [Limit of a map with respect to filters](../../topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)
- [Ring-valued matrix](../../linear-algebra/matrices/ring-valued-matrix.md)

## Proof depends on

- [Stopping time](../stochastic-processes/stopping-time.md)
- [Martingale](../stochastic-processes/martingale.md)
- [Pointwise convergence](../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Invertible elements](../../../undergraduate/ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Dual of a normed space](../../analysis/normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Moment of a random variable](../random-variables-and-their-laws/moment-of-a-random-variable.md)
- [Chain rule](../../../undergraduate/multivariable-calculus/differential-calculus/chain-rule.md)
- [Convergence in distribution](../convergence-of-a-sequence-of-random-variables/convergence-in-distribution.md)

## Main results

Its Lean names are 8 of the 214 theorems of its module named Main, MainTheorem(s) or Statement(s):

- [`BlockBand.Critical.BoundaryMean.exactBoundaryMean_of_inputs`](https://github.com/AxiomMath/BandMatrixQUE/blob/ad59520033d1ed202d582b256232d5ead86fa735/BlockBand/Critical/BoundaryMean/Main.lean#L34) (theorem)
- [`BlockBand.Critical.Herglotz.herglotzTail`](https://github.com/AxiomMath/BandMatrixQUE/blob/ad59520033d1ed202d582b256232d5ead86fa735/BlockBand/Critical/Herglotz/Main.lean#L38) (theorem)
- [`BlockBand.Critical.MatrixClosing.middle_error_arith`](https://github.com/AxiomMath/BandMatrixQUE/blob/ad59520033d1ed202d582b256232d5ead86fa735/BlockBand/Critical/MatrixClosing/MiddleShift/Main.lean#L30) (theorem)
- [`BlockBand.Critical.MatrixClosing.mem_bulkInterval_half`](https://github.com/AxiomMath/BandMatrixQUE/blob/ad59520033d1ed202d582b256232d5ead86fa735/BlockBand/Critical/MatrixClosing/MiddleShift/Main.lean#L100) (theorem)
- [`BlockBand.Critical.MatrixClosing.bulkInterval_mono_half`](https://github.com/AxiomMath/BandMatrixQUE/blob/ad59520033d1ed202d582b256232d5ead86fa735/BlockBand/Critical/MatrixClosing/MiddleShift/Main.lean#L106) (theorem)
- [`BlockBand.Critical.MatrixClosing.strictMiddle_of_exactBoundaryMean`](https://github.com/AxiomMath/BandMatrixQUE/blob/ad59520033d1ed202d582b256232d5ead86fa735/BlockBand/Critical/MatrixClosing/MiddleShift/Main.lean#L112) (theorem)
- [`BlockBand.Critical.MatrixClosing.middleKernel_radial`](https://github.com/AxiomMath/BandMatrixQUE/blob/ad59520033d1ed202d582b256232d5ead86fa735/BlockBand/Critical/MatrixClosing/MiddleShift/Main.lean#L287) (theorem)
- [`BlockBand.Critical.MatrixClosing.middleShiftBoundaryMean_of_exactBoundaryMean`](https://github.com/AxiomMath/BandMatrixQUE/blob/ad59520033d1ed202d582b256232d5ead86fa735/BlockBand/Critical/MatrixClosing/MiddleShift/Main.lean#L299) (theorem)

## Project

- Lean v4.35.0-rc3, Mathlib at [3b531c35](https://github.com/leanprover-community/mathlib4/tree/3b531c35df33d6bbe64b4e87dec056211d3a5676).
- 5,387 .lean files; its Lean libraries `BlockBand`, `BlockBandChallenge`, `BlockBandSolution` hold 5,000 (the first read), declaring 56,396 names, with `sorry` in 3 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/AxiomMath/BandMatrixQUE/blob/ad59520033d1ed202d582b256232d5ead86fa735/LICENSE)).

## Builds on

- Mathlib, at [3b531c35](https://github.com/leanprover-community/mathlib4/tree/3b531c35df33d6bbe64b4e87dec056211d3a5676).

## Placement

Of its imports of Mathlib modules in an overview area, 268 of 2254 are in Probability Theory, 4.7 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Probability Theory (268 of 2254 imports, 4.7×), Analysis (1379 of 2254 imports, 1.8×). *Proof depends on* names 8 of the 152 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [AxiomMath/BandMatrixQUE at ad595200](https://github.com/AxiomMath/BandMatrixQUE/tree/ad59520033d1ed202d582b256232d5ead86fa735)
