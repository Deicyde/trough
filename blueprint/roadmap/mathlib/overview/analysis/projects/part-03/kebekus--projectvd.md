---
declaration: module
origin: cited
lean: VD
statement: formalized
proof: formalized
---

# Project VD

[kebekus/ProjectVD](https://github.com/kebekus/ProjectVD) at commit [95de4d7f](https://github.com/kebekus/ProjectVD/tree/95de4d7f3678ee35f38d15c910b88fa2b89d15fd), 2026-11-16.

> This project aims to formalize [value distribution theory](https://en.wikipedia.org/wiki/Value_distribution_theory_of_holomorphic_functions) for meromorphic functions in the complex plane, roughly following Serge Lang's [Introduction to Complex Hyperbolic Spaces](https://link.springer.com/book/10.1007/978-1-4757-1945-1). The project uses the [Lean](https://lean-lang.org/) theorem prover and builds on [mathlib](https://leanprover-community.github.io/), the Lean mathematical library.

*Quoted from [README.md](https://github.com/kebekus/ProjectVD/blob/95de4d7f3678ee35f38d15c910b88fa2b89d15fd/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [First Main Theorem of Value Distribution Theory](../../complex-analysis/first-main-theorem-of-value-distribution-theory.md)
- [$\C$ is algebraically closed](../../../general-algebra/field-theory/c-is-algebraically-closed.md)
- [Principle of analytic continuation](../../complex-analysis/principle-of-analytic-continuation.md)
- [The Factor and Remainder Theorems](../../../../hundred-theorems/part-04/the-factor-and-remainder-theorems.md)
- [Bornology](../../topological-vector-spaces/bornology.md)
- [Algebraic elements](../../../../undergraduate/ring-theory/field-theory/algebraic-elements.md)
- [Real number](../../../general-algebra/numbers/real-number.md)
- [Logarithm](../../special-functions/logarithm.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`VD`](https://github.com/kebekus/ProjectVD/blob/95de4d7f3678ee35f38d15c910b88fa2b89d15fd/VD.lean): the root of a Lean library its lakefile builds, not a theorem. No file it imports, directly or not (39 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.36.0-rc2, Mathlib at [4b39df7a](https://github.com/leanprover-community/mathlib4/tree/4b39df7a6e9d22530ad9b787919829826eb55824).
- 39 .lean files; its Lean libraries `VD` hold 39, declaring 280 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/kebekus/ProjectVD/blob/95de4d7f3678ee35f38d15c910b88fa2b89d15fd/LICENSE)).

## Builds on

- Mathlib, at [4b39df7a](https://github.com/leanprover-community/mathlib4/tree/4b39df7a6e9d22530ad9b787919829826eb55824).

## Placement

Of its imports of Mathlib modules in an overview area, 50 of 67 are in Analysis, 2.7 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (50 of 67 imports, 2.7×), Topology (7 of 67 imports, 1.4×), General algebra (10 of 67 imports, 0.4×). *Proof depends on* names 8 of the 34 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [kebekus/ProjectVD at 95de4d7f](https://github.com/kebekus/ProjectVD/tree/95de4d7f3678ee35f38d15c910b88fa2b89d15fd)
