---
declaration: module
origin: cited
lean: GinibrePoincare
statement: formalized
---

# Ginibre Poincaré formalization

[djalilchafai/ginibre-poincare](https://github.com/djalilchafai/ginibre-poincare) at commit [a1b2ba84](https://github.com/djalilchafai/ginibre-poincare/tree/a1b2ba84e7dad8ba11b5c49a18b986a762a00a41), 2026-10-24.

> The 2026-10-09 readability revision adds mathematical reading routes, proof outlines and named result interfaces for deficits, matrix bounds, CIR localization and maximal-domain Bochner data. Its full build and public/private axiom audits pass; [verification evidence](https://github.com/djalilchafai/ginibre-poincare/blob/a1b2ba84e7dad8ba11b5c49a18b986a762a00a41/verification/readability-final-check.txt) and the [independent semantic diff review](https://github.com/djalilchafai/ginibre-poincare/blob/a1b2ba84e7dad8ba11b5c49a18b986a762a00a41/verification/readability-semantic-review.md) record the scope. The mathematical correspondence findings remain the dated 2026-10-08 reviews.

*Quoted from [README.md](https://github.com/djalilchafai/ginibre-poincare/blob/a1b2ba84e7dad8ba11b5c49a18b986a762a00a41/README.md), MIT, Copyright (c) 2026 Djalil Chafai.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Hitting time](../stochastic-processes/hitting-time.md)
- [Martingale](../stochastic-processes/martingale.md)
- [Independence of random variables](../random-variables-and-their-laws/independence-of-random-variables.md)
- [Leibniz formula (Analysis)](../../analysis/differentiability/leibniz-formula.md)
- [Taylor's theorem with integral form for remainder (Differential calculus)](../../../undergraduate/multivariable-calculus/differential-calculus/taylors-theorem-with-integral-form-for-remainder.md)
- [Uniform integrability](../../analysis/measures-and-integral-calculus/part-01/uniform-integrability.md)
- [Stopping time](../stochastic-processes/stopping-time.md)
- [Convergence in probability](../convergence-of-a-sequence-of-random-variables/convergence-in-probability.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`GinibrePoincare`](https://github.com/djalilchafai/ginibre-poincare/blob/a1b2ba84e7dad8ba11b5c49a18b986a762a00a41/GinibrePoincare.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files it imports, directly or not, `Challenge.lean` holds `sorry` or `admit`.

## Project

- Lean v4.35.0-rc2, Mathlib at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- 1,727 .lean files; its Lean libraries `GinibrePoincare`, `Challenge`, `Solution` hold 1,722, declaring 8,372 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: MIT ([LICENSE](https://github.com/djalilchafai/ginibre-poincare/blob/a1b2ba84e7dad8ba11b5c49a18b986a762a00a41/LICENSE)).

## Builds on

- Mathlib, at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).

## Placement

Of its imports of Mathlib modules in an overview area, 103 of 834 are in Probability Theory, 6.5 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Probability Theory (103 of 834 imports, 6.5×), Analysis (554 of 834 imports, 2.4×), Topology (84 of 834 imports, 1.3×). *Proof depends on* lists 8 of the 114 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [djalilchafai/ginibre-poincare at a1b2ba84](https://github.com/djalilchafai/ginibre-poincare/tree/a1b2ba84e7dad8ba11b5c49a18b986a762a00a41)
