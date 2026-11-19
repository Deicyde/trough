---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.adaptiveReplacementJointOp_next_factor, MIPRE.Introspection.nextPrefixResidual_isPVM, MIPRE.Introspection.adaptiveReplacementJointOp_next_reassembly, MIPRE.Introspection.nextPrefixDecodedPOVM_isPVM, MIPRE.Introspection.registeredReplacement_next_mats, MIPRE.Introspection.exists_adaptive_next_strategy
statement: formalized
proof: formalized
---

# Constructing the next-prefix residual invariant

The old-prefix and current-Z replacement operators equal the next honest prefix tensored with constructed residual projectors on its actual remaining coordinates and the common enlarged auxiliary space. After any answer decoder, these residuals are PVMs and reassemble to the selected measurement of the returned strategy. Under the old measurement's refinement identity and the three stage-error bounds, its value loss is at most $2\sqrt{2\sqrt{56\sqrt{\delta}}}$.

## Depends on

- [A concrete strategy after one adaptive replacement](lem-intro-adaptive-strategy.md)

## Proof depends on

- [Advancing the actual prefix label](lem-intro-adaptive-advance.md)

## Proof

Recover the unique old prefix and current label on attainable branches, transport the residual register by the proved coordinate-set equality, and use zero ambient projectors on all other branches. Coarse-graining the residuals commutes with prefix reassembly. Apply the existing quantitative replacement theorem to this concrete construction.

## Lean

Formalized as [`MIPRE.Introspection.adaptiveReplacementJointOp_next_factor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.adaptiveReplacementJointOp_next_factor), [`MIPRE.Introspection.nextPrefixResidual_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.nextPrefixResidual_isPVM), [`MIPRE.Introspection.adaptiveReplacementJointOp_next_reassembly`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.adaptiveReplacementJointOp_next_reassembly), [`MIPRE.Introspection.nextPrefixDecodedPOVM_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.nextPrefixDecodedPOVM_isPVM), [`MIPRE.Introspection.registeredReplacement_next_mats`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.registeredReplacement_next_mats), [`MIPRE.Introspection.exists_adaptive_next_strategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_adaptive_next_strategy).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2824](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2824)
