---
declaration: module
origin: cited
lean: CollatzPosDens
statement: formalized
---

# CollatzPositiveDensity

*Explicit Positive-Density Collatz Convergence in Logarithmic Time*

[AxiomMath/CollatzPositiveDensity](https://github.com/AxiomMath/CollatzPositiveDensity) at commit [c2e1f71e](https://github.com/AxiomMath/CollatzPositiveDensity/tree/c2e1f71e5ac8f54292d633cda70d23853c4e2c42), 2026-10-23.

> This is a Lean formalization of an explicit positive-density theorem for Collatz convergence in logarithmic time, refining [Lech Mazur's Theorem 1.1](https://x.com/LechMazur/status/2096464472973975782).

*Quoted from [README.md](https://github.com/AxiomMath/CollatzPositiveDensity/blob/c2e1f71e5ac8f54292d633cda70d23853c4e2c42/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [$\Z/n\Z$ and its invertible elements](../../../undergraduate/ring-theory/divisibility-in-integral-domains/z-n-z-and-its-invertible-elements.md)
- [Congruence in $\Z$](../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in-z.md)
- [Cos (extension of trigonometric functions to the complex plane)](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Infinite sum](../topological-algebra/infinite-sum.md)
- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Exponential](../../analysis/special-functions/exponential.md)
- [Real number](../../general-algebra/numbers/real-number.md)
- [Logarithm](../../analysis/special-functions/logarithm.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`CollatzPosDens`](https://github.com/AxiomMath/CollatzPositiveDensity/blob/c2e1f71e5ac8f54292d633cda70d23853c4e2c42/CollatzPosDens.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files it imports, directly or not, `Challenge/Basic.lean` holds `sorry` or `admit`.

## Project

- Lean v4.35.0-rc2, Mathlib at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- 1,050 .lean files; its Lean libraries `CollatzPosDens`, `Challenge`, `Solution` hold 1,050, declaring 6,016 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/AxiomMath/CollatzPositiveDensity/blob/c2e1f71e5ac8f54292d633cda70d23853c4e2c42/LICENSE)).

## Builds on

- Mathlib, at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).

## Placement

Of its imports of Mathlib modules in an overview area, 74 of 569 are in Topology, 1.7 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Topology (74 of 569 imports, 1.7×), General algebra (243 of 569 imports, 1.2×), Data structures (93 of 569 imports, 1.1×). *Proof depends on* lists 8 of the 29 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [AxiomMath/CollatzPositiveDensity at c2e1f71e](https://github.com/AxiomMath/CollatzPositiveDensity/tree/c2e1f71e5ac8f54292d633cda70d23853c4e2c42)
