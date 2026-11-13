---
declaration: theorem
origin: cited
lean: V7.main
statement: formalized
proof: formalized
---

# Parameter-Free Gradient Minimization in l_p Geometry

> Exact value-gradient query-complexity results for convex differentiable objectives on finite-dimensional real l_p spaces with attained minima and a positive global primal-to-dual Lipschitz-gradient bound. For finite real p > 1, the development proves strict-local scale-identification impossibility at LR/epsilon = 4 and a deterministic method family with three post-secant-initialization query-rate regimes. For p > 2 it also proves deterministic known-parameter upper and lower query exponents p/(p+2), with explicit horizon and dimension restrictions on the lower bound.

*Quoted from the card [LeanPool/projects/parameter_free_gradient_p.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/parameter_free_gradient_p.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`V7.scaleIdentificationImpossibility`](https://leanpool.github.io/lean-pool/LeanPool/ParameterFreeGradient/V7/Proofs/Stage7StrictRandomizedExpected/Closure.html#V7.scaleIdentificationImpossibility) (theorem), declared in [LeanPool/ParameterFreeGradient/V7/Proofs/Stage7StrictRandomizedExpected/Closure.lean, line 21](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ParameterFreeGradient/V7/Proofs/Stage7StrictRandomizedExpected/Closure.lean#L21): “For finite real p > 1 and positive epsilon, measurable strict-local exact value-gradient methods satisfy scale-identification lower bounds on convex smooth one-dimensional objectives with unique minimizers, even at LR/epsilon = 4. The result includes deterministic and randomized finite-horizon statements and infinite worst-case expected queried-or-returned hitting time.”
- [`V7.knownParameterAboveTwoOptimality`](https://leanpool.github.io/lean-pool/LeanPool/ParameterFreeGradient/V7/Proofs/Stage5AboveTwoLowerS5F/Optimality.html#V7.knownParameterAboveTwoOptimality) (theorem), declared in [LeanPool/ParameterFreeGradient/V7/Proofs/Stage5AboveTwoLowerS5F/Optimality.lean, line 19](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ParameterFreeGradient/V7/Proofs/Stage5AboveTwoLowerS5F/Optimality.lean#L19): “For finite real p > 2 and convex differentiable objectives with attained minima and a positive global primal-to-dual Lipschitz-gradient bound, deterministic known-parameter exact value-gradient methods have upper query exponent p/(p+2). The matching lower exponent concerns the first T queries, requires d >= 2 and 1 <= T <= d, and retains the explicit min(p, log d) dependence.”
- [`V7.main`](https://leanpool.github.io/lean-pool/LeanPool/ParameterFreeGradient/V7/Proofs/Stage8Main/Main.html#V7.main) (theorem; a main declaration), declared in [LeanPool/ParameterFreeGradient/V7/Proofs/Stage8Main/Main.lean, line 186](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ParameterFreeGradient/V7/Proofs/Stage8Main/Main.lean#L186): “For convex differentiable objectives with attained minima and positive global L-Lipschitz gradients from l_p to its dual, one deterministic family works for every finite real p > 1 and positive epsilon after supplied nondegenerate secant initialization with 0 < M0 <= L. It returns a queried point with dual gradient norm at most epsilon. Writing R for distance to the minimizer set, the post-initialization oracle-call bound has polynomial dependence on max(1, LR/epsilon) with exponent 1/2 for 1 < p < 2 and p = 2, and p/(p+2) for p > 2, plus additive log(e + L/M0) calibration cost. Constants depend only on p, with a universal constant at p = 2; discovering the secant pair is outside the count.”

## Project

- Authors: Yuning Yang.
- Project repository: [yuningyang19/parameter_free_gradient_p](https://github.com/yuningyang19/parameter_free_gradient_p), at commit [f71215fa](https://github.com/yuningyang19/parameter_free_gradient_p/tree/f71215fa936fe01aff8a765c62b399e131df963b).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 90C25.
- In Lean Pool: [LeanPool/ParameterFreeGradient](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ParameterFreeGradient), from the card [LeanPool/projects/parameter_free_gradient_p.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/parameter_free_gradient_p.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/parameter_free_gradient_p.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/parameter_free_gradient_p.yaml)
- [Lean Pool at 701389c0: LeanPool/ParameterFreeGradient](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ParameterFreeGradient)
