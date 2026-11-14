---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.prefixResidual_isPVM, MIPRE.Introspection.prefixResidual_reassembled_isPVM, MIPRE.Introspection.prefixResidual_reassembled_distance, MIPRE.Introspection.prefixResidual_reassembled_commutator_sum, MIPRE.Introspection.adaptiveZ_reassembled_commutator_sum, MIPRE.Introspection.prefixResidualOp_extend
statement: formalized
proof: formalized
---

# Projective reassembly across adaptive prefixes

Residual projective measurements assemble into one ambient PVM even though their coordinate spaces depend on the prefix. Prefix branches are orthogonal, so reassembly preserves squared errors exactly and global commutators reduce to the corresponding weighted local commutators. A common ancillary extension commutes with this concrete embedding.

## Depends on

- [Actual adaptive prefix law and residual registers](lem-intro-adaptive-prefix.md)
- [The one-sided ancilla extension](../../downstream-results/part-03/def-one-sided-extension.md)

## Proof depends on

- [Concrete adaptive Z and dual-X factorization](lem-intro-adaptive-factorization.md)

## Proof

Each branch is supported by its actual honest prefix projector. Distinct projectors multiply to zero; summing the branch normalizers gives identity. The same orthogonality eliminates all cross terms in squared distances and commutators.

## Lean

Formalized as [`MIPRE.Introspection.prefixResidual_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.prefixResidual_isPVM), [`MIPRE.Introspection.prefixResidual_reassembled_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.prefixResidual_reassembled_isPVM), [`MIPRE.Introspection.prefixResidual_reassembled_distance`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.prefixResidual_reassembled_distance), [`MIPRE.Introspection.prefixResidual_reassembled_commutator_sum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.prefixResidual_reassembled_commutator_sum), [`MIPRE.Introspection.adaptiveZ_reassembled_commutator_sum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.adaptiveZ_reassembled_commutator_sum), [`MIPRE.Introspection.prefixResidualOp_extend`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.prefixResidualOp_extend).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2681](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2681)
