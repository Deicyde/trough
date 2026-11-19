---
declaration: module
origin: cited
lean: Zeta5Irr
statement: formalized
---

# ζ(5) is Irrational

[AxiomMath/Zeta5Irrational](https://github.com/AxiomMath/Zeta5Irrational) at commit [ac05f15d](https://github.com/AxiomMath/Zeta5Irrational/tree/ac05f15d9eb58a190361f7461e794f539db041ff), 2026-09-26.

> This is a Lean formalization of Aabir Fauzan's proof that ζ(5) is irrational (https://zenodo.org/records/22826419).

*Quoted from [README.md](https://github.com/AxiomMath/Zeta5Irrational/blob/ac05f15d9eb58a190361f7461e794f539db041ff/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Von Staudt–Clausen theorem](../../mathlib/thousand-plus/number-theory/part-02/von-staudt-clausen-theorem.md)
- [Rational functions](../../mathlib/undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/rational-functions.md)
- [Bernoulli numbers](../../mathlib/overview/general-algebra/number-theory/bernoulli-numbers.md)
- [Polynomial derivative](../../mathlib/undergraduate/ring-theory/polynomial-rings/polynomial-derivative.md)
- [$p$-adic number](../../mathlib/overview/general-algebra/numbers/p-adic-number.md)
- [Complete metric spaces](../../mathlib/undergraduate/topology/topology-and-metric-spaces/complete-metric-spaces.md)
- [Power series](../../mathlib/overview/general-algebra/polynomials-and-power-series/power-series.md)
- [Change of variables formula](../../mathlib/overview/analysis/measures-and-integral-calculus/part-02/change-of-variables-formula.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`Zeta5Irr`](https://github.com/AxiomMath/Zeta5Irrational/blob/ac05f15d9eb58a190361f7461e794f539db041ff/Zeta5Irr.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files it imports, directly or not, `Challenge/Basic.lean` holds `sorry` or `admit`.

## Project

- Lean v4.35.0-rc2, Mathlib at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- 504 .lean files; its Lean libraries `Zeta5Irr`, `Challenge`, `Solution` hold 504, declaring 2,117 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/AxiomMath/Zeta5Irrational/blob/ac05f15d9eb58a190361f7461e794f539db041ff/LICENSE)).

## Builds on

- Mathlib, at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- [PrimeNumberTheoremAnd](../README.md) at `d71f7b41`, a repository with the Lake package name and library root of AlexKontorovich/PrimeNumberTheoremAnd.

## Placement

Its Lake manifest requires `PrimeNumberTheoremAnd`, a repository with the Lake package name and library root of AlexKontorovich/PrimeNumberTheoremAnd, whose modules 1 file of the project import.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: General algebra (998 of 1824 imports, 1.5×), Analysis (364 of 1824 imports, 0.7×). *Proof depends on* names 8 of the 69 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [AxiomMath/Zeta5Irrational at ac05f15d](https://github.com/AxiomMath/Zeta5Irrational/tree/ac05f15d9eb58a190361f7461e794f539db041ff)
