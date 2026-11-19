---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.conditionalIdeal_eq_coarse_of_reject, MIPRE.Introspection.Honest.hidingPrefixOp_isPVM, MIPRE.Introspection.Honest.hidingPrefixOp_commute_hideOp, MIPRE.Introspection.Honest.hideOp_prefix_fixed, MIPRE.Introspection.Honest.hidingPrefixOp_mul_next, MIPRE.Introspection.Honest.hideCoarseOp_isPVM, MIPRE.Introspection.Honest.hideCoarseOp_conditionalIdeal_eq_next, MIPRE.Introspection.Honest.hideCoarseOp_conditionalIdeal_step
statement: formalized
proof: formalized
---

# The concrete ideal hiding step

The computational readout of the next truncated CL prefix is a complete PVM with zero malformed outcome and commutes with the preceding honest Hide family. Its product with the guarded coarse preceding family is exactly the next honest hiding measurement under the actual test's retained map. Discarding the redundant key bookkeeping gives exactly the next fine hiding coarse family. Only CL support and the adjacent-level index condition are assumed; the operator identities are proved from the constructed measurements.

## Depends on

- [Dimension-independent conditional normalizer replacement](lem-intro-conditional-normalizer.md)
- [Honest hiding marginals and edge compatibility](lem-intro-honest-hiding.md)
- [Guarded maps on arbitrary hiding answers](lem-intro-guarded-hiding-maps.md)

## Proof

The next prefix is a marginal of the next honest Hide PVM, whose effects commute with the preceding Hide effects. Matrix support forces every nonzero effect's claimed prefix to be fixed by prefix extraction. Expand the ideal conditional product in the next PVM. Rejected products vanish; summing the complete earlier family leaves exactly the indicated next outcome. Finally compose the retained outcome maps.

## Lean

Formalized as [`MIPRE.Introspection.conditionalIdeal_eq_coarse_of_reject`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.conditionalIdeal_eq_coarse_of_reject), [`MIPRE.Introspection.Honest.hidingPrefixOp_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hidingPrefixOp_isPVM), [`MIPRE.Introspection.Honest.hidingPrefixOp_commute_hideOp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hidingPrefixOp_commute_hideOp), [`MIPRE.Introspection.Honest.hideOp_prefix_fixed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hideOp_prefix_fixed), [`MIPRE.Introspection.Honest.hidingPrefixOp_mul_next`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hidingPrefixOp_mul_next), [`MIPRE.Introspection.Honest.hideCoarseOp_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hideCoarseOp_isPVM), [`MIPRE.Introspection.Honest.hideCoarseOp_conditionalIdeal_eq_next`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hideCoarseOp_conditionalIdeal_eq_next), [`MIPRE.Introspection.Honest.hideCoarseOp_conditionalIdeal_step`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hideCoarseOp_conditionalIdeal_step).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2304](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2304)
