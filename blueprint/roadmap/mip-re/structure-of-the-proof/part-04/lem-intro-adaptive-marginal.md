---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.advancePrefix_fibSum_sqNorm, MIPRE.Introspection.prefixStageMarginalError_reassembled
statement: formalized
proof: formalized
---

# Exact reassembly of the next-prefix marginal error

The stage marginal error is exactly the squared distance between the advanced coarse residual marginal and the next honest prefix measurement. There is no answer-count loss, and no projectivity or normalized-state hypothesis is needed for this equality.

## Depends on

- [Advancing the actual prefix label](lem-intro-adaptive-advance.md)

## Proof

The extended label is injective on attainable old prefixes, and every other prefix-supported operator vanishes. Thus coarse assembly preserves the squared-error sum exactly. Identify its ideal term with the next-prefix projector assembly.

## Lean

Formalized as [`MIPRE.Introspection.advancePrefix_fibSum_sqNorm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.advancePrefix_fibSum_sqNorm), [`MIPRE.Introspection.prefixStageMarginalError_reassembled`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.prefixStageMarginalError_reassembled).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2776](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2776)
