---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.TypedEstimates.introspect_prefix_register_rigidity_alice, MIPRE.Introspection.stageAnswerRefinement_coarse_marginal, MIPRE.Introspection.stageAnswerRefinement_marginal_le_reported, MIPRE.Introspection.TypedEstimates.introspect_adaptive_marginal, MIPRE.Introspection.TypedEstimates.introspect_refined_stage_bounds, MIPRE.Introspection.TypedEstimates.exists_game_adaptive_prefix_dilation, MIPRE.Introspection.adaptiveStepLoss_le_root, MIPRE.Introspection.adaptiveFailureBudget_mono
statement: formalized
proof: formalized
---

# One stage budget from the actual game tests

Write $e=|E|\varepsilon$, let $\eta_Z$ be the primitive Bob-Z error and $\delta_H$ the fixed Alice hiding error, and let $r$ be the remaining depth. For the current projective prefix product form with its valid-answer support, all three refined stage errors are at most

$$
B_r(e,\eta_Z,\delta_H)
=64\eta_Z+(512r^2+224)e+64\delta_H.
$$

If this budget is at most one, the actual tests construct the common-ancilla residual projectors. The replacement value loss is at most $8B_r^{1/8}$. An explicit monotone numerical failure recurrence records this loss.

## Depends on

- [Actual Sample and Read tests control conditional commutators](lem-intro-adaptive-read-error.md)
- [Exact reassembly of the next-prefix marginal error](lem-intro-adaptive-marginal.md)
- [Refining and updating the actual Introspect answer](lem-intro-answer-refinement.md)

## Proof

The Introspect consistency loop transfers Bob's prefix rigidity to Alice with bound $8\eta_Z+28e$. Refining the dummy answer adds its old-prefix block to the valid reported marginal. Orthogonality charges the sum of these squared norms to the single dummy outcome, giving marginal error at most $16\eta_Z+56e$. Combine this with the actual Z and dual-X commutator estimates and apply mixing and dilation. Three square roots give the stated universal coefficient and exponent. The numerical recurrence does not itself construct a sequence of strategies.

## Lean

Formalized as [`MIPRE.Introspection.TypedEstimates.introspect_prefix_register_rigidity_alice`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.introspect_prefix_register_rigidity_alice), [`MIPRE.Introspection.stageAnswerRefinement_coarse_marginal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.stageAnswerRefinement_coarse_marginal), [`MIPRE.Introspection.stageAnswerRefinement_marginal_le_reported`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.stageAnswerRefinement_marginal_le_reported), [`MIPRE.Introspection.TypedEstimates.introspect_adaptive_marginal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.introspect_adaptive_marginal), [`MIPRE.Introspection.TypedEstimates.introspect_refined_stage_bounds`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.introspect_refined_stage_bounds), [`MIPRE.Introspection.TypedEstimates.exists_game_adaptive_prefix_dilation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.exists_game_adaptive_prefix_dilation), [`MIPRE.Introspection.adaptiveStepLoss_le_root`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.adaptiveStepLoss_le_root), [`MIPRE.Introspection.adaptiveFailureBudget_mono`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.adaptiveFailureBudget_mono).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2852](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2852)
