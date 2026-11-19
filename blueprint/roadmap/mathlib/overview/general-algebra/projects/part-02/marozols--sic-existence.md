---
declaration: module
origin: cited
lean: SICs
statement: formalized
proof: formalized
---

# SIC existence in Lean

[marozols/SIC-existence](https://github.com/marozols/SIC-existence) at commit [91e3a438](https://github.com/marozols/SIC-existence/tree/91e3a438beb8dd4f580fd56195479981f0db49bd), 2026-10-09.

> A [symmetric informationally complete measurement (SIC)](https://en.wikipedia.org/wiki/SIC-POVM) is a highly symmetric quantum measurement built from $d^2$ states in dimension $d$, with every distinct pair having the same overlap. This is equivalent to $d^2$ equiangular lines in $\mathbb C^d$. Zauner's conjecture asks whether SICs exist in every finite dimension.

*Quoted from [README.md](https://github.com/marozols/SIC-existence/blob/91e3a438beb8dd4f580fd56195479981f0db49bd/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Dirichlet's unit theorem](../../../../thousand-plus/number-theory/part-01/dirichlets-unit-theorem.md)
- [Galois correspondence](../../field-theory/galois-correspondence.md)
- [Periodic points](../../../dynamics/general-theory/periodic-points.md)
- [Dirichlet unit theorem](../../algebraic-number-theory/dirichlet-unit-theorem.md)
- [Cayley-Hamilton theorem](../../../linear-algebra/endomorphism-polynomials/cayley-hamilton-theorem.md)
- [Sin (extension of trigonometric functions to the complex plane)](../../../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/sin.md)
- [Dirichlet class number formula](../../algebraic-number-theory/dirichlet-class-number-formula.md)
- [Principal ideal domain](../../divisibility-in-integral-domains/principal-ideal-domain.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`SICs`](https://github.com/marozols/SIC-existence/blob/91e3a438beb8dd4f580fd56195479981f0db49bd/SICs.lean): the root of a Lean library its lakefile builds, not a theorem. No file it imports, directly or not (450 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.34.1, Mathlib at [d13f23b7](https://github.com/leanprover-community/mathlib4/tree/d13f23b723b8a846827a245b89c10fc7d3f11612).
- 450 .lean files; its Lean libraries `SICs` hold 450, declaring 4,706 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/marozols/SIC-existence/blob/91e3a438beb8dd4f580fd56195479981f0db49bd/LICENSE)).

## Builds on

- Mathlib, at [d13f23b7](https://github.com/leanprover-community/mathlib4/tree/d13f23b723b8a846827a245b89c10fc7d3f11612).

## Placement

Of its imports of Mathlib modules in an overview area, 223 of 412 are in General algebra, 1.5 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: General algebra (223 of 412 imports, 1.5×), Analysis (116 of 412 imports, 1.0×). *Proof depends on* lists 8 of the 109 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [marozols/SIC-existence at 91e3a438](https://github.com/marozols/SIC-existence/tree/91e3a438beb8dd4f580fd56195479981f0db49bd)
