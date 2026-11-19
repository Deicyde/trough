---
declaration: module
origin: cited
lean: FastExtract, SampCert, VMC
statement: formalized
proof: formalized
---

# SampCert

[leanprover/SampCert](https://github.com/leanprover/SampCert) at commit [a2c53bb5](https://github.com/leanprover/SampCert/tree/a2c53bb5ff790e729e252958060699b7eff898b9), 2026-09-25.

> A verified implementation using [Lean](https://github.com/leanprover/lean4) and [Mathlib](https://github.com/leanprover-community/mathlib4) of randomized algorithms including [the discrete Gaussian sampler for differential privacy](https://arxiv.org/abs/2004.00010), key results in [zero concentrated differential privacy](https://arxiv.org/abs/1605.02065), and [some verified (unbounded) private queries](https://arxiv.org/pdf/1909.01917).

*Quoted from [README.md](https://github.com/leanprover/SampCert/blob/a2c53bb5ff790e729e252958060699b7eff898b9/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Jensen's inequality (integral version)](../../analysis/convexity/jensens-inequality-integral-version.md)
- [Discrete law](../random-variables-and-their-laws/discrete-law.md)
- [Derivative of a composition of functions (Single Variable Real Analysis)](../../../undergraduate/single-variable-real-analysis/differentiability/derivative-of-a-composition-of-functions.md)
- [Extended real number](../../general-algebra/numbers/extended-real-number.md)
- [Infinite sum](../../topology/topological-algebra/infinite-sum.md)
- [Hyperbolic trigonometric functions](../../analysis/special-functions/hyperbolic-trigonometric-functions.md)
- [Integer](../../general-algebra/numbers/integer.md)
- [Real number](../../general-algebra/numbers/real-number.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`FastExtract`](https://github.com/leanprover/SampCert/blob/a2c53bb5ff790e729e252958060699b7eff898b9/FastExtract.lean), [`SampCert`](https://github.com/leanprover/SampCert/blob/a2c53bb5ff790e729e252958060699b7eff898b9/SampCert.lean), [`VMC`](https://github.com/leanprover/SampCert/blob/a2c53bb5ff790e729e252958060699b7eff898b9/VMC.lean): the root of a Lean library its lakefile builds, not a theorem. No file they import, directly or not (104 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.34.1, Mathlib at [d13f23b7](https://github.com/leanprover-community/mathlib4/tree/d13f23b723b8a846827a245b89c10fc7d3f11612).
- 107 .lean files; its Lean libraries `SampCert`, `FastExtract`, `VMC` hold 105, declaring 792 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/leanprover/SampCert/blob/a2c53bb5ff790e729e252958060699b7eff898b9/LICENSE)).

## Builds on

- Mathlib, at [d13f23b7](https://github.com/leanprover-community/mathlib4/tree/d13f23b723b8a846827a245b89c10fc7d3f11612).

## Placement

Of its imports of Mathlib modules in an overview area, 11 of 55 are in Probability Theory, 10.5 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Probability Theory (11 of 55 imports, 10.5×), Topology (6 of 55 imports, 1.5×), Data structures (8 of 55 imports, 1.0×). *Proof depends on* names 8 of the 29 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [leanprover/SampCert at a2c53bb5](https://github.com/leanprover/SampCert/tree/a2c53bb5ff790e729e252958060699b7eff898b9)
