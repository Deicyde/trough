---
declaration: module
origin: cited
lean: FABL
statement: formalized
proof: formalized
---

# FABL: Formal Analysis of Boolean Functions in Lean

[Polarnova/FABL](https://github.com/Polarnova/FABL) at commit [164f8303](https://github.com/Polarnova/FABL/tree/164f830312946ccac6e7fdc7bb9493f0149e820d), 2026-08-30.

> FABL is a Lean 4 and Mathlib formalization of Ryan O'Donnell's [*Analysis of Boolean Functions*](https://arxiv.org/abs/2105.10386), following the May 2021 edition. It develops the book's results as a reusable theorem library while preserving the domains, normalizations, and hypotheses of the original statements.

*Quoted from [README.md](https://github.com/Polarnova/FABL/blob/164f830312946ccac6e7fdc7bb9493f0149e820d/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Fourier Series](../../mathlib/hundred-theorems/part-03/fourier-series.md)
- [Lévy continuity theorem](../../mathlib/thousand-plus/probability-and-statistics/levy-continuity-theorem.md)
- [Binomial law](../../mathlib/overview/probability-theory/random-variables-and-their-laws/binomial-law.md)
- [Discrete law](../../mathlib/overview/probability-theory/random-variables-and-their-laws/discrete-law.md)
- [Conditional probability](../../mathlib/overview/probability-theory/definitions-in-probability-theory/conditional-probability.md)
- [Variance of a real-valued random variable](../../mathlib/overview/probability-theory/random-variables-and-their-laws/variance-of-a-real-valued-random-variable.md)
- [Formula for the Number of Combinations](../../mathlib/hundred-theorems/part-03/formula-for-the-number-of-combinations.md)
- [Inverse trigonometric functions](../../mathlib/overview/analysis/special-functions/inverse-trigonometric-functions.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`FABL`](https://github.com/Polarnova/FABL/blob/164f830312946ccac6e7fdc7bb9493f0149e820d/FABL.lean): the root of a Lean library its lakefile builds, not a theorem. No file it imports, directly or not (293 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.32.0, Mathlib at [81a5d257](https://github.com/leanprover-community/mathlib4/tree/81a5d257c8e410db227a6665ed08f64fea08e997).
- 360 .lean files; its Lean libraries `FABL` hold 293, declaring 9,120 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/Polarnova/FABL/blob/164f830312946ccac6e7fdc7bb9493f0149e820d/LICENSE)).

## Builds on

- Mathlib, at [81a5d257](https://github.com/leanprover-community/mathlib4/tree/81a5d257c8e410db227a6665ed08f64fea08e997).
- [cslib](../README.md) at `197a7be6`.
- `ProbabilityApproximation` (https://github.com/Polarnova/ProbabilityApproximation.git) at `c89fba90`.

## Placement

Its Lake manifest requires `cslib`.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (61 of 126 imports, 1.8×), General algebra (24 of 126 imports, 0.5×). *Proof depends on* names 8 of the 68 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [Polarnova/FABL at 164f8303](https://github.com/Polarnova/FABL/tree/164f830312946ccac6e7fdc7bb9493f0149e820d)
