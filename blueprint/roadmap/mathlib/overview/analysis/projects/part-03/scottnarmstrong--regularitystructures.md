---
declaration: theorem
origin: cited
lean: GlobalPhi43.Statements.globalDynamics, GlobalPhi43.Statements.regularisedBound, GlobalPhi43.Statements.exponentCompatibility, RegularityStructures.exists_annBump
statement: formalized
proof: formalized
---

# RegularityStructures

*Regularity structures and the dynamical Φ⁴₃ model, formalized in Lean 4*

[scottnarmstrong/RegularityStructures](https://github.com/scottnarmstrong/RegularityStructures) at commit [280380b2](https://github.com/scottnarmstrong/RegularityStructures/tree/280380b2cd1323a557c76c2b7483bd234ff4b651), 2026-10-27.

## Depends on

- [Sigma-algebra](../../measures-and-integral-calculus/part-01/sigma-algebra.md)
- [Probability measure](../../../probability-theory/definitions-in-probability-theory/probability-measure.md)
- [Positive measure](../../measures-and-integral-calculus/part-01/positive-measure.md)
- [Set](../../../data-structures/sets/set.md)
- [Measurable function](../../measures-and-integral-calculus/part-01/measurable-function.md)
- [$C^k$ function](../../differentiability/c-k-function.md)

## Proof depends on

- [Differentiability of the limit of a sequence of functions](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/differentiability-of-the-limit-of-a-sequence-of.md)
- [Taylor's theorem with integral form for remainder (Differential calculus)](../../../../undergraduate/multivariable-calculus/differential-calculus/taylors-theorem-with-integral-form-for-remainder.md)
- [Approximation by step functions](../../../../undergraduate/measures-and-integral-calculus/measure-theory/approximation-by-step-functions.md)
- [General linear group (Fundamentals)](../../../linear-algebra/fundamentals/general-linear-group.md)
- [Stone-Weierstrass theorem](../../../topology/general-topology/part-02/stone-weierstrass-theorem.md)
- [Convolution of two functions of $\mathcal{S}(\R^d)$](../../../../undergraduate/distribution-calculus/spaces-s-r-d/convolution-of-two-functions-of-s-r-d.md)
- [Convolution](../../measures-and-integral-calculus/part-02/convolution.md)
- [Fubini's theorem](../../measures-and-integral-calculus/part-02/fubinis-theorem.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`GlobalPhi43.Statements.globalDynamics`](https://github.com/scottnarmstrong/RegularityStructures/blob/280380b2cd1323a557c76c2b7483bd234ff4b651/GlobalPhi43Statements/GlobalDynamics.lean#L38) (theorem)
- [`GlobalPhi43.Statements.regularisedBound`](https://github.com/scottnarmstrong/RegularityStructures/blob/280380b2cd1323a557c76c2b7483bd234ff4b651/GlobalPhi43Statements/RegularisedBound.lean#L38) (theorem)
- [`GlobalPhi43.Statements.exponentCompatibility`](https://github.com/scottnarmstrong/RegularityStructures/blob/280380b2cd1323a557c76c2b7483bd234ff4b651/GlobalPhi43Statements/ExponentCompatibility.lean#L37) (theorem)
- [`RegularityStructures.exists_annBump`](https://github.com/scottnarmstrong/RegularityStructures/blob/280380b2cd1323a557c76c2b7483bd234ff4b651/RegularityStructures/Analysis/Heat/Annihilating/Shell.lean#L28) (theorem)

No file its headlines import, directly or not (2768 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0-rc2, Mathlib at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- 3,071 .lean files; its Lean libraries `RegularityStructures`, `Phi43Statements`, `Phi43`, `GlobalPhi43Statements`, `GlobalPhi43`, `TheoremAChallenge` and 13 more hold 3,071, declaring 10,965 names, with `sorry` in 6 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/scottnarmstrong/RegularityStructures/blob/280380b2cd1323a557c76c2b7483bd234ff4b651/LICENSE)).

## Builds on

- Mathlib, at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).

## Placement

4 of the 6 Mathlib concepts its headline statements name are in Analysis.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (840 of 1269 imports, 2.4×), Topology (169 of 1269 imports, 1.8×). *Proof depends on* lists 8 of the 96 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [scottnarmstrong/RegularityStructures at 280380b2](https://github.com/scottnarmstrong/RegularityStructures/tree/280380b2cd1323a557c76c2b7483bd234ff4b651)
