---
declaration: theorem
origin: cited
lean: LongTails.OracleTemplate.GeneralizedAccelerated.SelfNormalized.result
statement: formalized
proof: formalized
---

# Gradient-only acceleration for generalized-smooth convex optimization

> A damped accelerated method minimizes convex functions on real Hilbert spaces whose differentiable gradients satisfy the Hessian-growth bound norm(D gradient f x) <= L0 + L1 \* norm(gradient f x). The development proves an explicit gradient-query budget for any positive accuracy, initial distance bound and initial objective-gap bound, with an attained minimum. It retains the oracle execution model, ordinary gradient descent, energy dissipation, charging arguments and two complementary convergence bounds. No objective value or line-search oracle is assumed.

*Quoted from the card [LeanPool/projects/longtails-generalized-convex.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/longtails-generalized-convex.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LongTails.OracleTemplate.GeneralizedAccelerated.SelfNormalized.result`](https://leanpool.github.io/lean-pool/LeanPool/LongTails/Theorems/GeneralizedSelfNormalizedConvex.html#LongTails.OracleTemplate.GeneralizedAccelerated.SelfNormalized.result) (theorem; a main declaration), declared in [LeanPool/LongTails/Theorems/GeneralizedSelfNormalizedConvex.lean, line 32](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LongTails/Theorems/GeneralizedSelfNormalizedConvex.lean#L32): “For positive L0, R, Delta and epsilon and nonnegative L1, a single damped accelerated algorithm returns a point of objective gap at most epsilon for every admissible convex objective with an attained minimum within distance R and initial objective gap at most Delta. Its exact gradient-query budget is zero when Delta <= epsilon; otherwise it is twice the natural ceiling of 4096 times (1 + sqrt(L0\*R^2/epsilon) + min(ceil((L1\*R)^(2/3))\*D, D + (L1\*R\*D)^(2/3))), where D = log(4 + 4\*Delta/epsilon).”
- [`LongTails.OracleTemplate.GeneralizedAccelerated.run_accuracy_self_normalized`](https://leanpool.github.io/lean-pool/LeanPool/LongTails/Proofs/GeneralizedSelfNormalizedConvergence.html#LongTails.OracleTemplate.GeneralizedAccelerated.run_accuracy_self_normalized) (lemma), declared in [LeanPool/LongTails/Proofs/GeneralizedSelfNormalizedConvergence.lean, line 78](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LongTails/Proofs/GeneralizedSelfNormalizedConvergence.lean#L78): “Under the same convexity, gradient, Hessian-growth and initialization hypotheses, N accelerated steps reach objective gap epsilon whenever N >= 4096\*(1 + sqrt(L0\*R^2/epsilon) + D + (L1\*R\*D)^(2/3)).”
- [`LongTails.OracleTemplate.GeneralizedAccelerated.execute_gradient_oracle`](https://leanpool.github.io/lean-pool/LeanPool/LongTails/Proofs/DampedGeneralizedExecution.html#LongTails.OracleTemplate.GeneralizedAccelerated.execute_gradient_oracle) (lemma), declared in [LeanPool/LongTails/Proofs/DampedGeneralizedExecution.lean, line 59](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LongTails/Proofs/DampedGeneralizedExecution.lean#L59): “Execution with any admissible exact-gradient oracle and a budget of 2\*N gradient queries equals the N-step accelerated iterate, for every seed.”
- [`LongTails.OracleTemplate.Gradient.gd_accuracy`](https://leanpool.github.io/lean-pool/LeanPool/LongTails/Proofs/GdConvex.html#LongTails.OracleTemplate.Gradient.gd_accuracy) (lemma), declared in [LeanPool/LongTails/Proofs/GdConvex.lean, line 135](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LongTails/Proofs/GdConvex.lean#L135): “For L > 0, R >= 0 and epsilon > 0, a convex function with an exact L-Lipschitz gradient and initial distance at most R from a comparison point, ordinary gradient descent reaches objective gap epsilon after max(1, ceil(L\*R^2/(2\*epsilon))) queries.”

## Project

- Authors: Alexander Tyurin, QuocViet Pham, Valentin Khrulkov, Ivan Oseledets.
- Project repository: [k3nfalt/longtails](https://github.com/k3nfalt/longtails), at commit [269cbc76](https://github.com/k3nfalt/longtails/tree/269cbc764dd36851fd0b64f2f950f329ee127de4).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 90C25, 90C30, 68Q25.
- In Lean Pool: [LeanPool/LongTails](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LongTails), from the card [LeanPool/projects/longtails-generalized-convex.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/longtails-generalized-convex.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/longtails-generalized-convex.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/longtails-generalized-convex.yaml)
- [Lean Pool at 701389c0: LeanPool/LongTails](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LongTails)
