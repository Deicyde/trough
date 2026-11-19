---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.testAcceptance_stability_map_left, MIPRE.Introspection.replaceExtended_other, MIPRE.Introspection.replaceExtended_value, MIPRE.Introspection.registeredReplacementStrategy_value_loss, MIPRE.Introspection.exists_conditional_replacement_strategy, MIPRE.Introspection.exists_adaptive_replacement_strategy
statement: formalized
proof: formalized
---

# A concrete strategy after one adaptive replacement

If the selected measurement has the stated current prefix form and the three stage errors are bounded as above, an actual finite-dimensional tensor-product strategy is constructed. The new state retains the original EPR factor, all other measurements are extended by identity, and the selected measurement retains the prefix and newly extracted Z factor. The absolute game-value loss is at most $2\sqrt{2\sqrt{56\sqrt{\varepsilon}}}$. Arbitrary answer relabelling is allowed. These are single-stage hypotheses, not a completed induction from game success.

## Depends on

- [Adaptive extraction and common-ancilla projectivization](lem-intro-adaptive-extraction.md)

## Proof depends on

- [Quantitative measurement and state replacement](lem-intro-value-stability.md)

## Proof

Construct the residual Naimark projectors and the ambient joint PVM, replace the selected question, and reassociate the shared EPR-plus-auxiliary state exactly. Pull the acceptance predicate back through answer relabelling before applying value stability; no same-party coarse-distance contraction is used.

## Lean

Formalized as [`MIPRE.Introspection.testAcceptance_stability_map_left`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.testAcceptance_stability_map_left), [`MIPRE.Introspection.replaceExtended_other`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.replaceExtended_other), [`MIPRE.Introspection.replaceExtended_value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.replaceExtended_value), [`MIPRE.Introspection.registeredReplacementStrategy_value_loss`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.registeredReplacementStrategy_value_loss), [`MIPRE.Introspection.exists_conditional_replacement_strategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_conditional_replacement_strategy), [`MIPRE.Introspection.exists_adaptive_replacement_strategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_adaptive_replacement_strategy).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2717](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2717)
