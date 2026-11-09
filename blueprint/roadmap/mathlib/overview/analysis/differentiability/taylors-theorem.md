# Taylor's theorem

This file defines the Taylor polynomial of a real function `f : ℝ → E`,
where `E` is a normed vector space over `ℝ` and proves Taylor's theorem,
which states that if `f` is sufficiently smooth, then
`f` can be approximated by the Taylor polynomial up to an explicit error term.

Mathlib covers this with the module `Mathlib.Analysis.Calculus.Taylor` rather than a single declaration.

Its 23 documented declarations include `taylorCoeffWithin`, `taylorWithin`, `taylorWithinEval`, `taylor_within_zero_eval`, `taylorWithinEval_self`, `continuousOn_taylorWithinEval`, `monomial_has_deriv_aux`, `hasDerivWithinAt_taylorWithinEval`, `taylorWithinEval_hasDerivAt_Ioo`, `hasDerivWithinAt_taylorWithinEval_at_Icc`, `hasDerivAt_taylorWithinEval_succ`, `taylor_isLittleO`, and 11 more.

## Depends on

Dependencies are tracked for single declarations only.

## Sources

- [Mathlib documentation: Mathlib.Analysis.Calculus.Taylor](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Taylor.html)
- [Source: Mathlib/Analysis/Calculus/Taylor.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Calculus/Taylor.lean)
- [Mathlib overview: Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L312)
