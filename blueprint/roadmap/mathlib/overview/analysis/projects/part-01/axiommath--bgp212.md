---
declaration: theorem
origin: cited
lean: Gap212.nthPrimeGapLE_212_of_dhl, Gap212.primeGapLE_212_of_dhl, Gap212.dhl45_of_inputsFamily, Gap212.nthPrimeGapLE_212_of_inputsFamily, Gap212.primeGapLE_212_of_inputsFamily
statement: formalized
proof: formalized
---

# Bounded gaps between primes (H₁ ≤ 212)

[AxiomMath/BGP212](https://github.com/AxiomMath/BGP212) at commit [6641780b](https://github.com/AxiomMath/BGP212/tree/6641780bb6bab050fd400a348ba759d233e34fad), 2026-10-01.

> This is a Lean formalization of the bound `H₁ ≤ 212` on gaps between consecutive primes, conditional on the numerical certificate `Gap212.Gap212Certificate` and on cited analytic estimates.

*Quoted from [README.md](https://github.com/AxiomMath/BGP212/blob/6641780bb6bab050fd400a348ba759d233e34fad/README.md), Apache-2.0.*

## Depends on

- [PrimeGapsLib](../../../../../pnt-plus/projects/axiommath--primegapslib.md)

## Proof depends on

- [Regularization by convolution](../../measures-and-integral-calculus/part-02/regularization-by-convolution.md)
- [Euler's totient function ($\varphi$)](../../../general-algebra/divisibility-in-integral-domains/eulers-totient-function-varphi.md)
- [Arithmetic functions](../../../general-algebra/number-theory/arithmetic-functions.md)
- [Uniformly continuous function](../../../topology/uniform-notions/uniformly-continuous-function.md)
- [Continuity of the sum of a series of functions](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/continuity-of-the-sum-of-a-series-of-functions.md)
- [Logarithm](../../special-functions/logarithm.md)
- [Real number](../../../general-algebra/numbers/real-number.md)
- [Absolutely convergent series in Banach spaces](../../normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)

## Main results

Its Lean names are the theorems of its top-level module named Main, MainTheorem(s) or Statement(s):

- [`Gap212.nthPrimeGapLE_212_of_dhl`](https://github.com/AxiomMath/BGP212/blob/6641780bb6bab050fd400a348ba759d233e34fad/Gap212/Main.lean#L92) (theorem)
- [`Gap212.primeGapLE_212_of_dhl`](https://github.com/AxiomMath/BGP212/blob/6641780bb6bab050fd400a348ba759d233e34fad/Gap212/Main.lean#L97) (theorem)
- [`Gap212.dhl45_of_inputsFamily`](https://github.com/AxiomMath/BGP212/blob/6641780bb6bab050fd400a348ba759d233e34fad/Gap212/Main.lean#L156) (theorem)
- [`Gap212.nthPrimeGapLE_212_of_inputsFamily`](https://github.com/AxiomMath/BGP212/blob/6641780bb6bab050fd400a348ba759d233e34fad/Gap212/Main.lean#L162) (theorem)
- [`Gap212.primeGapLE_212_of_inputsFamily`](https://github.com/AxiomMath/BGP212/blob/6641780bb6bab050fd400a348ba759d233e34fad/Gap212/Main.lean#L168) (theorem)

No file its headlines import, directly or not (11 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.33.0-rc1, Mathlib at [288f16d9](https://github.com/leanprover-community/mathlib4/tree/288f16d9a07189233a9bc5e1c143c38d1f3f4d37).
- 254 .lean files; its Lean libraries `Gap212`, `Gap212Challenge`, `Gap212Solution` hold 254, declaring 4,061 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/AxiomMath/BGP212/blob/6641780bb6bab050fd400a348ba759d233e34fad/LICENSE)).

## Builds on

- Mathlib, at [288f16d9](https://github.com/leanprover-community/mathlib4/tree/288f16d9a07189233a9bc5e1c143c38d1f3f4d37).
- [PrimeGapsLib](../../../../../pnt-plus/projects/axiommath--primegapslib.md) at `1faa7b14`.

## Placement

Of its imports of Mathlib modules in an overview area, 74 of 151 are in Analysis, 1.8 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (74 of 151 imports, 1.8×), General algebra (59 of 151 imports, 1.1×). *Proof depends on* names 8 of the 37 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [AxiomMath/BGP212 at 6641780b](https://github.com/AxiomMath/BGP212/tree/6641780bb6bab050fd400a348ba759d233e34fad)
