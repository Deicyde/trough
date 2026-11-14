---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.TypedEstimates.check_hiding_next_prefix, MIPRE.Introspection.TypedEstimates.check_hiding_read_prefix, MIPRE.Introspection.TypedEstimates.prefixChainType_adj, MIPRE.Introspection.TypedEstimates.prefixChainType_check, MIPRE.Introspection.TypedEstimates.prefix_chain_step_estimate, MIPRE.Introspection.TypedEstimates.hiding_introspect_prefix_estimate
statement: formalized
proof: formalized
---

# Actual hiding-prefix propagation to Introspect

For any hiding index $j$ and $m\leq j$, the actual Hide-$j$ and Introspect measurements of the reported $m$-prefix on Alice's side have squared distance at most $8|E|(\ell-j+1)^2\varepsilon$. Every wrong answer constructor contributes to a separate dummy outcome. No honest-image or support assumption is imposed on the strategy's answers.

## Depends on

- [Guarded maps on arbitrary hiding answers](lem-intro-guarded-hiding-maps.md)
- [The parsed introspection decision predicate](../part-02/lem-intro-parsed-predicate.md)

## Proof

Construct the actual path from Hide-$j$ through the remaining Hide vertices and Read to Introspect. Each accepted edge preserves the reported prefix. Combine its cross-party estimate with the consistency loop at the next vertex to get same-party error $8|E|\varepsilon$. Telescope the chain with the squared Cauchy–Schwarz inequality.

## Lean

Formalized as [`MIPRE.Introspection.TypedEstimates.check_hiding_next_prefix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.check_hiding_next_prefix), [`MIPRE.Introspection.TypedEstimates.check_hiding_read_prefix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.check_hiding_read_prefix), [`MIPRE.Introspection.TypedEstimates.prefixChainType_adj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.prefixChainType_adj), [`MIPRE.Introspection.TypedEstimates.prefixChainType_check`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.prefixChainType_check), [`MIPRE.Introspection.TypedEstimates.prefix_chain_step_estimate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.prefix_chain_step_estimate), [`MIPRE.Introspection.TypedEstimates.hiding_introspect_prefix_estimate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hiding_introspect_prefix_estimate).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2219](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2219)
