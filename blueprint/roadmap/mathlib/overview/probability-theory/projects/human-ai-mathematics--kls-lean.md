---
declaration: theorem
origin: cited
lean: FunctionalInequalities.Energy.SmoothGradient.Intrinsic.closedQuadratic, FunctionalInequalities.Poincare.SmoothGradient.Intrinsic.constant, FunctionalInequalities.Poincare.SmoothGradient.Intrinsic.Holds, FunctionalInequalities.Poincare.SmoothGradient.Intrinsic.holds_iff_constant_le, FunctionalInequalities.Energy.NormalContraction.smoothed, FunctionalInequalities.Energy.NormalContraction.contDiff_smoothed, FunctionalInequalities.Energy.NormalContraction.lipschitzWith_smoothed, FunctionalInequalities.Energy.NormalContraction.norm_smoothed_sub_le
statement: formalized
proof: formalized
---

# kls-lean

[human-ai-mathematics/kls-lean](https://github.com/human-ai-mathematics/kls-lean) at commit [e609af5f](https://github.com/human-ai-mathematics/kls-lean/tree/e609af5fa9c0087c66761c02a083cd9e8e8e2504), 2026-11-16.

> Lean 4 formalization of the dimension-free Kannan–Lovász–Simonovits (KLS) bound, following the proof of Bizeul, Klartag, and Lehec.

*Quoted from [README.md](https://github.com/human-ai-mathematics/kls-lean/blob/e609af5fa9c0087c66761c02a083cd9e8e8e2504/README.md), Apache-2.0.*

## Depends on

- [$C^k$ function](../../analysis/differentiability/c-k-function.md)
- [Lipschitz continuity](../../topology/metric-spaces/lipschitz-continuity.md)

## Proof depends on

- [Besicovitch covering theorem](../../../thousand-plus/analysis/26-real-functions/part-01/besicovitch-covering-theorem.md)
- [Continuity (continuity and differentiability of convex functions)](../../../undergraduate/single-variable-real-analysis/convexity/continuity-and-differentiability-of-convex-funct/continuity.md)
- [Partial derivatives commute](../../../undergraduate/multivariable-calculus/differential-calculus/partial-derivatives-commute.md)
- [Gradient vector](../../../undergraduate/multivariable-calculus/differential-calculus/gradient-vector.md)
- [Approximation by convolution](../../analysis/measures-and-integral-calculus/part-02/approximation-by-convolution.md)
- [Symmetric bilinear form](../../linear-algebra/bilinear-and-quadratic-forms/symmetric-bilinear-form.md)
- [Extension by continuity](../../topology/general-topology/part-01/extension-by-continuity.md)
- [Conditional expectation](../definitions-in-probability-theory/conditional-expectation.md)

## Main results

Its Lean names are 8 of the 207 Lean names of the blueprint nodes that no other node uses, marked \leanok:

- [`FunctionalInequalities.Energy.SmoothGradient.Intrinsic.closedQuadratic`](https://github.com/human-ai-mathematics/kls-lean/blob/e609af5fa9c0087c66761c02a083cd9e8e8e2504/formalization/FunctionalInequalities/Energy/SmoothGradient/Intrinsic/Closed.lean#L37) (theorem)
- [`FunctionalInequalities.Poincare.SmoothGradient.Intrinsic.constant`](https://github.com/human-ai-mathematics/kls-lean/blob/e609af5fa9c0087c66761c02a083cd9e8e8e2504/formalization/FunctionalInequalities/Poincare/SmoothGradient/Intrinsic.lean#L35) (def)
- [`FunctionalInequalities.Poincare.SmoothGradient.Intrinsic.Holds`](https://github.com/human-ai-mathematics/kls-lean/blob/e609af5fa9c0087c66761c02a083cd9e8e8e2504/formalization/FunctionalInequalities/Poincare/SmoothGradient/Intrinsic.lean#L41) (def)
- [`FunctionalInequalities.Poincare.SmoothGradient.Intrinsic.holds_iff_constant_le`](https://github.com/human-ai-mathematics/kls-lean/blob/e609af5fa9c0087c66761c02a083cd9e8e8e2504/formalization/FunctionalInequalities/Poincare/SmoothGradient/Intrinsic.lean#L48) (theorem)
- [`FunctionalInequalities.Energy.NormalContraction.smoothed`](https://github.com/human-ai-mathematics/kls-lean/blob/e609af5fa9c0087c66761c02a083cd9e8e8e2504/formalization/FunctionalInequalities/Energy/SmoothGradient/Dirichlet.lean#L51) (def)
- [`FunctionalInequalities.Energy.NormalContraction.contDiff_smoothed`](https://github.com/human-ai-mathematics/kls-lean/blob/e609af5fa9c0087c66761c02a083cd9e8e8e2504/formalization/FunctionalInequalities/Energy/SmoothGradient/Dirichlet.lean#L55) (theorem)
- [`FunctionalInequalities.Energy.NormalContraction.lipschitzWith_smoothed`](https://github.com/human-ai-mathematics/kls-lean/blob/e609af5fa9c0087c66761c02a083cd9e8e8e2504/formalization/FunctionalInequalities/Energy/SmoothGradient/Dirichlet.lean#L59) (theorem)
- [`FunctionalInequalities.Energy.NormalContraction.norm_smoothed_sub_le`](https://github.com/human-ai-mathematics/kls-lean/blob/e609af5fa9c0087c66761c02a083cd9e8e8e2504/formalization/FunctionalInequalities/Energy/SmoothGradient/Dirichlet.lean#L64) (theorem)

No file its headlines import, directly or not (30 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 1,591 .lean files; its Lean libraries `FunctionalInequalities`, `Solutions`, `Examples`, `LevyStochCalc`, `BrownianMotion`, `MathFin` and 1 more hold 1,080, declaring 9,164 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/human-ai-mathematics/kls-lean/blob/e609af5fa9c0087c66761c02a083cd9e8e8e2504/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).

## Placement

Of its imports of Mathlib modules in an overview area, 160 of 1509 are in Probability Theory, 5.6 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Probability Theory (160 of 1509 imports, 5.6×), Analysis (1015 of 1509 imports, 2.5×), Topology (165 of 1509 imports, 1.5×). *Proof depends on* names 8 of the 151 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [human-ai-mathematics/kls-lean at e609af5f](https://github.com/human-ai-mathematics/kls-lean/tree/e609af5fa9c0087c66761c02a083cd9e8e8e2504)
