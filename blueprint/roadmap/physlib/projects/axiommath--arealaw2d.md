---
declaration: theorem
origin: cited
lean: AreaLaw.areaLaw, AreaLaw.areaLawCorollary, AreaLaw.conditionalContinuity, AreaLaw.marginalTails, AreaLaw.bufferDiscount, AreaLaw.initialBoxEstimate, AreaLaw.positiveReplacement, AreaLaw.Scanner.prop_9_6
statement: formalized
proof: formalized
---

# A two-dimensional area law from a global spectral gap, in Lean 4

[AxiomMath/AreaLaw2D](https://github.com/AxiomMath/AreaLaw2D) at commit [7768136b](https://github.com/AxiomMath/AreaLaw2D/tree/7768136b2e90d736e5de25a6d857b2ea4fdea7b2), 2026-11-09.

> A Lean 4 formalization of *A two-dimensional area law from a global spectral gap* (`paper/paper.pdf`, LaTeX in `paper/sections/`).

*Quoted from [README.md](https://github.com/AxiomMath/AreaLaw2D/blob/7768136b2e90d736e5de25a6d857b2ea4fdea7b2/README.md), Apache-2.0.*

## Depends on

Its headline statements name no Mathlib concept or declaration mapped elsewhere on this site.

## Proof depends on

- [Unitary group](../../mathlib/undergraduate/group-theory/classical-automorphism-groups/unitary-group.md)
- [Inversion formula](../../mathlib/overview/analysis/fourier-analysis/inversion-formula.md)
- [Newton's identities](../../mathlib/undergraduate/ring-theory/polynomial-rings/newtons-identities.md)
- [Grönwall lemma](../../mathlib/undergraduate/multivariable-calculus/differential-equations/gronwall-lemma.md)
- [Matrix exponential](../../mathlib/undergraduate/linear-algebra/exponential/matrix-exponential.md)
- [Free algebra of a commutative ring](../../mathlib/overview/general-algebra/algebras-over-a-ring/free-algebra-of-a-commutative-ring.md)
- [Hyperbolic trigonometric functions](../../mathlib/overview/analysis/special-functions/hyperbolic-trigonometric-functions.md)
- [Self-adjoint operator](../../mathlib/overview/analysis/hilbert-spaces/self-adjoint-operator.md)

## Main results

Its Lean names are 8 of the 16 theorems its README names in code:

- [`AreaLaw.areaLaw`](https://github.com/AxiomMath/AreaLaw2D/blob/7768136b2e90d736e5de25a6d857b2ea4fdea7b2/AreaLaw/Transfer.lean#L361) (theorem)
- [`AreaLaw.areaLawCorollary`](https://github.com/AxiomMath/AreaLaw2D/blob/7768136b2e90d736e5de25a6d857b2ea4fdea7b2/AreaLaw/Transfer.lean#L367) (theorem)
- [`AreaLaw.conditionalContinuity`](https://github.com/AxiomMath/AreaLaw2D/blob/7768136b2e90d736e5de25a6d857b2ea4fdea7b2/AreaLaw/Transfer.lean#L181) (theorem)
- [`AreaLaw.marginalTails`](https://github.com/AxiomMath/AreaLaw2D/blob/7768136b2e90d736e5de25a6d857b2ea4fdea7b2/AreaLaw/Transfer.lean#L228) (theorem)
- [`AreaLaw.bufferDiscount`](https://github.com/AxiomMath/AreaLaw2D/blob/7768136b2e90d736e5de25a6d857b2ea4fdea7b2/AreaLaw/Transfer.lean#L262) (theorem)
- [`AreaLaw.initialBoxEstimate`](https://github.com/AxiomMath/AreaLaw2D/blob/7768136b2e90d736e5de25a6d857b2ea4fdea7b2/AreaLaw/Transfer.lean#L277) (theorem)
- [`AreaLaw.positiveReplacement`](https://github.com/AxiomMath/AreaLaw2D/blob/7768136b2e90d736e5de25a6d857b2ea4fdea7b2/AreaLaw/Transfer.lean#L136) (theorem)
- [`AreaLaw.Scanner.prop_9_6`](https://github.com/AxiomMath/AreaLaw2D/blob/7768136b2e90d736e5de25a6d857b2ea4fdea7b2/AreaLaw/S09_Scanner.lean#L42) (theorem)

No file its headlines import, directly or not (304 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.33.0, Mathlib at [db584cd6](https://github.com/leanprover-community/mathlib4/tree/db584cd6d46c92f209a44c0f1c829460d327499d).
- 334 .lean files; its Lean libraries `OpenAI`, `Challenge`, `Solution`, `AreaLaw`, `AreaLawForMathlib` hold 314, declaring 5,304 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/AxiomMath/AreaLaw2D/blob/7768136b2e90d736e5de25a6d857b2ea4fdea7b2/LICENSE)).

## Builds on

- Mathlib, at [db584cd6](https://github.com/leanprover-community/mathlib4/tree/db584cd6d46c92f209a44c0f1c829460d327499d).
- `lintall`.
- [Physlib](../README.md) at `a50684a1`.

## Placement

Its Lake manifest requires `Physlib`.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Linear algebra (44 of 337 imports, 2.2×), Analysis (189 of 337 imports, 2.1×), General algebra (49 of 337 imports, 0.4×). *Proof depends on* names 8 of the 81 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [AxiomMath/AreaLaw2D at 7768136b](https://github.com/AxiomMath/AreaLaw2D/tree/7768136b2e90d736e5de25a6d857b2ea4fdea7b2)
