---
declaration: module
origin: cited
lean: RiemannJensen
statement: formalized
---

# Riemann and Dedekind Jensen Polynomials

[AxiomMath/RiemannJensen](https://github.com/AxiomMath/RiemannJensen) at commit [c1e023fa](https://github.com/AxiomMath/RiemannJensen/tree/c1e023fa3ae7161219dde3dcb73f0c28ff972be2), 2026-10-23.

> This is a Lean formalization of the theorem that almost all zeros of the Jensen polynomials of the Riemann and Dedekind xi functions are distinct negative reals.

*Quoted from [README.md](https://github.com/AxiomMath/RiemannJensen/blob/c1e023fa3ae7161219dde3dcb73f0c28ff972be2/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Stirling’s Formula](../../../../hundred-theorems/part-04/stirlings-formula.md)
- [Geometric series](../../../../undergraduate/single-variable-real-analysis/numerical-series/geometric-series.md)
- [Integration by parts](../../../../undergraduate/single-variable-real-analysis/integration/integration-by-parts.md)
- [Higher-order derivatives of functions](../../../../undergraduate/single-variable-real-analysis/differentiability/higher-order-derivatives-of-functions.md)
- [Quotient space (Basic definitions)](../../../../undergraduate/group-theory/basic-definitions/quotient-space.md)
- [Complex exponential](../../../../undergraduate/single-variable-complex-analysis/complex-valued-series/complex-exponential.md)
- [Fractional ideal](../../../general-algebra/ideals-and-quotients/fractional-ideal.md)
- [Intermediate value theorem](../../../topology/topological-algebra/intermediate-value-theorem.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`RiemannJensen`](https://github.com/AxiomMath/RiemannJensen/blob/c1e023fa3ae7161219dde3dcb73f0c28ff972be2/RiemannJensen.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files it imports, directly or not, `Challenge/Basic.lean` holds `sorry` or `admit`.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 152 .lean files; its Lean libraries `RiemannJensen`, `Challenge`, `Solution` hold 152, declaring 2,243 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/AxiomMath/RiemannJensen/blob/c1e023fa3ae7161219dde3dcb73f0c28ff972be2/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).

## Placement

Of its imports of Mathlib modules in an overview area, 91 of 130 are in Analysis, 2.6 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (91 of 130 imports, 2.6×), General algebra (32 of 130 imports, 0.7×). *Proof depends on* lists 8 of the 64 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [AxiomMath/RiemannJensen at c1e023fa](https://github.com/AxiomMath/RiemannJensen/tree/c1e023fa3ae7161219dde3dcb73f0c28ff972be2)
