---
declaration: theorem
origin: cited
lean: Proofs.LinFold.poc_train_step_tail_certified, Proofs.LinFoldB.lin_train_step_tiedB, Proofs.LinFoldB.lin_weight_meanlossB, Proofs.LinFold.linear_net_lossGrad, Proofs.LinFold.linear_net_lossGrad_CE, Proofs.mlpHasVJPAt_correct, Proofs.mlpHasVJPAt, Proofs.MlpFold.mlp_train_step_tied
statement: formalized
proof: formalized
---

# Lean 4 → MLIR → GPU

[brettkoonce/lean4-mlir](https://github.com/brettkoonce/lean4-mlir) at commit [26820779](https://github.com/brettkoonce/lean4-mlir/tree/26820779f0d87e88bfae89a81c3063aa58d050f1), 2026-11-17.

> **The book: [Verified Deep Learning with Lean 4](https://lean.brettkoonce.com/blueprint/)** — the interactive proof blueprint *is* the book: every theorem clickable, from the `pdiv` primitives to the whole-network backward passes.

*Quoted from [README.md](https://github.com/brettkoonce/lean4-mlir/blob/26820779f0d87e88bfae89a81c3063aa58d050f1/README.md), BSD-3-Clause, Copyright (c) 2026, Brett Koonce.*

## Depends on

- [Natural number](../../../general-algebra/numbers/natural-number.md)

## Proof depends on

- [Binomial law](../../../probability-theory/random-variables-and-their-laws/binomial-law.md)
- [Reflection](../../hilbert-spaces/reflection.md)
- [Differentiable functions](../../../../undergraduate/multivariable-calculus/differential-calculus/differentiable-functions.md)
- [Leibniz formula (Analysis)](../../differentiability/leibniz-formula.md)
- [Bochner integral](../../measures-and-integral-calculus/part-01/bochner-integral.md)
- [Gaussian law](../../../probability-theory/random-variables-and-their-laws/gaussian-law.md)
- [Differentiable function between normed vector spaces](../../differentiability/differentiable-function-between-normed-vector-sp.md)
- [Hyperbolic trigonometric functions](../../special-functions/hyperbolic-trigonometric-functions.md)

## Main results

Its Lean names are 8 of the 150 Lean names of the blueprint nodes that no other node uses, marked \leanok:

- [`Proofs.LinFold.poc_train_step_tail_certified`](https://github.com/brettkoonce/lean4-mlir/blob/26820779f0d87e88bfae89a81c3063aa58d050f1/LeanMlir/Proofs/Nets/Small/LinearFold.lean#L98) (theorem)
- [`Proofs.LinFoldB.lin_train_step_tiedB`](https://github.com/brettkoonce/lean4-mlir/blob/26820779f0d87e88bfae89a81c3063aa58d050f1/LeanMlir/Proofs/Nets/Small/LinearFoldB.lean#L174) (theorem)
- [`Proofs.LinFoldB.lin_weight_meanlossB`](https://github.com/brettkoonce/lean4-mlir/blob/26820779f0d87e88bfae89a81c3063aa58d050f1/LeanMlir/Proofs/Nets/Small/LinearFoldB.lean#L191) (theorem)
- [`Proofs.LinFold.linear_net_lossGrad`](https://github.com/brettkoonce/lean4-mlir/blob/26820779f0d87e88bfae89a81c3063aa58d050f1/LeanMlir/Proofs/Nets/Small/LinearParamGrad.lean#L39) (theorem)
- [`Proofs.LinFold.linear_net_lossGrad_CE`](https://github.com/brettkoonce/lean4-mlir/blob/26820779f0d87e88bfae89a81c3063aa58d050f1/LeanMlir/Proofs/Nets/Small/LinearParamGrad.lean#L46) (theorem)
- [`Proofs.mlpHasVJPAt_correct`](https://github.com/brettkoonce/lean4-mlir/blob/26820779f0d87e88bfae89a81c3063aa58d050f1/LeanMlir/Proofs/Foundation/MLP.lean#L398) (theorem)
- [`Proofs.mlpHasVJPAt`](https://github.com/brettkoonce/lean4-mlir/blob/26820779f0d87e88bfae89a81c3063aa58d050f1/LeanMlir/Proofs/Foundation/MLP.lean#L336) (def)
- [`Proofs.MlpFold.mlp_train_step_tied`](https://github.com/brettkoonce/lean4-mlir/blob/26820779f0d87e88bfae89a81c3063aa58d050f1/LeanMlir/Proofs/Nets/Small/MlpFold.lean#L177) (theorem)

No file its headlines import, directly or not (42 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.36.0, Mathlib at [fc4f59e5](https://github.com/leanprover-community/mathlib4/tree/fc4f59e577feb1a4956671bc04ac18aaaf8cd842).
- 656 .lean files; its Lean libraries `LeanMlir`, `Proofs`, `Certs`, `CertsHeavy`, `ProofsMinimal`, `Reference` and 3 more hold 446, declaring 15,399 names, with `sorry` in 3 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: BSD-3-Clause ([LICENSE](https://github.com/brettkoonce/lean4-mlir/blob/26820779f0d87e88bfae89a81c3063aa58d050f1/LICENSE)).

## Builds on

- Mathlib, at [fc4f59e5](https://github.com/leanprover-community/mathlib4/tree/fc4f59e577feb1a4956671bc04ac18aaaf8cd842).

## Placement

Of its imports of Mathlib modules in an overview area, 214 of 256 are in Analysis, 3.1 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (214 of 256 imports, 3.1×). *Proof depends on* lists 8 of the 38 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [brettkoonce/lean4-mlir at 26820779](https://github.com/brettkoonce/lean4-mlir/tree/26820779f0d87e88bfae89a81c3063aa58d050f1)
