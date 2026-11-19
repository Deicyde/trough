---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.TypedEstimates.prefix_chain_step_estimate_bob, MIPRE.Introspection.TypedEstimates.hiding_introspect_prefix_estimate_bob, MIPRE.Introspection.TypedEstimates.hidingNormalizer_eq_reportedPrefix, MIPRE.Introspection.TypedEstimates.hidingNormalizer_estimate
statement: formalized
proof: formalized
---

# The actual later normalizer from the prefix chain

The same prefix-chain estimate holds on Bob's side without assuming that the Pauli predicate is symmetric. The actual conditional marginal in the adjacent hiding test is exactly the later answer's reported-prefix measurement, including the malformed label. If the corresponding Introspect prefix has squared error $\delta$ from its ideal, then the later Hide normalizer has error at most $16|E|(\ell-j+1)^2\varepsilon+2\delta$.

## Depends on

- [Actual hiding-prefix propagation to Introspect](lem-intro-actual-prefix-chain.md)
- [Guarded maps on arbitrary hiding answers](lem-intro-guarded-hiding-maps.md)

## Proof

Use each forward path edge and the loop at its earlier endpoint to obtain Bob's estimate via the common Alice measurement. Sum the joint coarse outcomes to identify the actual prefix marginal exactly, then combine the chain and Introspect-prefix distances by the squared triangle inequality.

## Lean

Formalized as [`MIPRE.Introspection.TypedEstimates.prefix_chain_step_estimate_bob`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.prefix_chain_step_estimate_bob), [`MIPRE.Introspection.TypedEstimates.hiding_introspect_prefix_estimate_bob`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hiding_introspect_prefix_estimate_bob), [`MIPRE.Introspection.TypedEstimates.hidingNormalizer_eq_reportedPrefix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hidingNormalizer_eq_reportedPrefix), [`MIPRE.Introspection.TypedEstimates.hidingNormalizer_estimate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hidingNormalizer_estimate).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2244](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2244)
