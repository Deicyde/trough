---
declaration: theorem
origin: cited
lean: Shor.shorGateCountBound_of_setup, Shor.exists_shorGateCountBound, Shor.Policy.shorGateCountBound, Shor.Shor_correct, Shor.submission_correct, Shor.policy_submission_correct, Shor.exactSignedWidth_le_iff, Shor.nextSignedWidthBy_exact_le_scan
statement: formalized
proof: formalized
---

# ForShor

[VerifiedQC/ForShor](https://github.com/VerifiedQC/ForShor) at commit [d26da5ad](https://github.com/VerifiedQC/ForShor/tree/d26da5ad6b52b5abce01a4b930379be420c940e7), 2026-11-11.

> A formal verification of **Shor's algorithm** in Lean 4 — including its **resource estimation**.

*Quoted from [README.md](https://github.com/VerifiedQC/ForShor/blob/d26da5ad6b52b5abce01a4b930379be420c940e7/README.md), Apache-2.0.*

## Depends on

Its headline statements name no Mathlib concept or declaration mapped elsewhere on this site.

## Proof depends on

- [Cramer’s Rule](../../../../hundred-theorems/part-04/cramers-rule.md)
- [$\Z/n\Z$ and its invertible elements](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/z-n-z-and-its-invertible-elements.md)
- [Unitary group](../../../../undergraduate/group-theory/classical-automorphism-groups/unitary-group.md)
- [Congruence in $\Z$](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in-z.md)
- [Power functions](../../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/power-functions.md)
- [Euler's totient function ($\varphi$)](../../../general-algebra/divisibility-in-integral-domains/eulers-totient-function-varphi.md)
- [Complex exponential](../../../../undergraduate/single-variable-complex-analysis/complex-valued-series/complex-exponential.md)
- [Order of an element](../../../../undergraduate/group-theory/basic-definitions/order-of-an-element.md)

## Main results

Its Lean names are 8 of the 11 theorems its README names in code:

- [`Shor.shorGateCountBound_of_setup`](https://github.com/VerifiedQC/ForShor/blob/d26da5ad6b52b5abce01a4b930379be420c940e7/ForShor/ShorVerification/Implementation/Shor/Main.lean#L59) (theorem)
- [`Shor.exists_shorGateCountBound`](https://github.com/VerifiedQC/ForShor/blob/d26da5ad6b52b5abce01a4b930379be420c940e7/ForShor/ShorVerification/Implementation/Shor/Main.lean#L92) (theorem)
- [`Shor.Policy.shorGateCountBound`](https://github.com/VerifiedQC/ForShor/blob/d26da5ad6b52b5abce01a4b930379be420c940e7/ForShor/ShorVerification/Implementation/Shor/Main.lean#L100) (theorem)
- [`Shor.Shor_correct`](https://github.com/VerifiedQC/ForShor/blob/d26da5ad6b52b5abce01a4b930379be420c940e7/ForShor/ShorVerification/Implementation/Shor/Proofs/NaiveShor/Correctness.lean#L44) (theorem)
- [`Shor.submission_correct`](https://github.com/VerifiedQC/ForShor/blob/d26da5ad6b52b5abce01a4b930379be420c940e7/ForShor/ShorVerification/Submission/Correct.lean#L82) (theorem)
- [`Shor.policy_submission_correct`](https://github.com/VerifiedQC/ForShor/blob/d26da5ad6b52b5abce01a4b930379be420c940e7/ForShor/ShorVerification/Submission/Correct.lean#L61) (theorem)
- [`Shor.exactSignedWidth_le_iff`](https://github.com/VerifiedQC/ForShor/blob/d26da5ad6b52b5abce01a4b930379be420c940e7/ForShor/ShorVerification/Implementation/PhaseProduct/Proofs/Compiler/ExactWidthBound.lean#L260) (theorem)
- [`Shor.nextSignedWidthBy_exact_le_scan`](https://github.com/VerifiedQC/ForShor/blob/d26da5ad6b52b5abce01a4b930379be420c940e7/ForShor/ShorVerification/Implementation/PhaseProduct/Proofs/Compiler/ExactWidthBound.lean#L311) (theorem)

No file its headlines import, directly or not (149 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.36.0-rc1, Mathlib at [4dc43842](https://github.com/leanprover-community/mathlib4/tree/4dc43842a11f257ffba2a611c943a133a65cb4b2).
- 615 .lean files; its Lean libraries `ForShor`, `EmitTests`, `Submission`, `PolicySubmission`, `PTPPolicySubmission`, `PolicyTests` and 5 more hold 354, declaring 6,149 names, with `sorry` in 1 file and 1 axiom, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/VerifiedQC/ForShor/blob/d26da5ad6b52b5abce01a4b930379be420c940e7/LICENSE)).

## Builds on

- Mathlib, at [4dc43842](https://github.com/leanprover-community/mathlib4/tree/4dc43842a11f257ffba2a611c943a133a65cb4b2).

## Placement

Of its imports of Mathlib modules in an overview area, 95 of 206 are in Analysis, 1.7 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (95 of 206 imports, 1.7×), General algebra (85 of 206 imports, 1.2×). *Proof depends on* lists 8 of the 40 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [VerifiedQC/ForShor at d26da5ad](https://github.com/VerifiedQC/ForShor/tree/d26da5ad6b52b5abce01a4b930379be420c940e7)
