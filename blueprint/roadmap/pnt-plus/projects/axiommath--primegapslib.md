---
declaration: module
origin: cited
lean: ChallengeFast, PrimeGaps, PrimeGapsCert
statement: formalized
---

# PrimeGapsLib

[AxiomMath/PrimeGapsLib](https://github.com/AxiomMath/PrimeGapsLib) at commit [1faa7b14](https://github.com/AxiomMath/PrimeGapsLib/tree/1faa7b14e82ddebc2772dfb9153922f01b106477), 2026-08-18.

> Public Lean library for formalizations related to prime gaps, maintained by Axiom Math.

*Quoted from [README.md](https://github.com/AxiomMath/PrimeGapsLib/blob/1faa7b14e82ddebc2772dfb9153922f01b106477/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Convergence of $p$-series for $p>1$](../../mathlib/undergraduate/single-variable-real-analysis/numerical-series/convergence-of-p-series-for-p-1.md)
- [Euler's totient function ($\varphi$)](../../mathlib/overview/general-algebra/divisibility-in-integral-domains/eulers-totient-function-varphi.md)
- [Arithmetic functions](../../mathlib/overview/general-algebra/number-theory/arithmetic-functions.md)
- [Finitely supported function](../../mathlib/overview/data-structures/maps/finitely-supported-function.md)
- [Integration by parts](../../mathlib/undergraduate/single-variable-real-analysis/integration/integration-by-parts.md)
- [Congruence in $\Z$](../../mathlib/undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in-z.md)
- [Convolution](../../mathlib/overview/analysis/measures-and-integral-calculus/part-02/convolution.md)
- [Absolutely convergent series in Banach spaces](../../mathlib/overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`ChallengeFast`](https://github.com/AxiomMath/PrimeGapsLib/blob/1faa7b14e82ddebc2772dfb9153922f01b106477/ChallengeFast.lean), [`PrimeGaps`](https://github.com/AxiomMath/PrimeGapsLib/blob/1faa7b14e82ddebc2772dfb9153922f01b106477/PrimeGaps.lean), [`PrimeGapsCert`](https://github.com/AxiomMath/PrimeGapsLib/blob/1faa7b14e82ddebc2772dfb9153922f01b106477/PrimeGapsCert.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `Challenge/Basic.lean`, `ChallengeFast/Basic.lean` hold `sorry` or `admit`.

## Project

- Lean v4.33.0-rc1, Mathlib at [288f16d9](https://github.com/leanprover-community/mathlib4/tree/288f16d9a07189233a9bc5e1c143c38d1f3f4d37).
- 420 .lean files; its Lean libraries `PrimeGapsCert`, `PrimeGapsTheory`, `PrimeGaps`, `Challenge`, `Solution`, `ChallengeFast` and 1 more hold 420, declaring 3,249 names, with `sorry` in 2 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/AxiomMath/PrimeGapsLib/blob/1faa7b14e82ddebc2772dfb9153922f01b106477/LICENSE)).

## Builds on

- Mathlib, at [288f16d9](https://github.com/leanprover-community/mathlib4/tree/288f16d9a07189233a9bc5e1c143c38d1f3f4d37).
- [PrimeNumberTheoremAnd](../README.md) at `2667e414`, a repository with the Lake package name and library root of AlexKontorovich/PrimeNumberTheoremAnd.

## Placement

Its Lake manifest requires `PrimeNumberTheoremAnd`, a repository with the Lake package name and library root of AlexKontorovich/PrimeNumberTheoremAnd, whose modules 2 files of the project import.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: General algebra (105 of 197 imports, 1.5×), Analysis (51 of 197 imports, 1.0×). *Proof depends on* lists 8 of the 63 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [AxiomMath/PrimeGapsLib at 1faa7b14](https://github.com/AxiomMath/PrimeGapsLib/tree/1faa7b14e82ddebc2772dfb9153922f01b106477)
