---
declaration: lemma
origin: cited
lean: MIPRE.CL.CLFun.SupportedOn.proj_eval_cons, MIPRE.CL.CLFun.SupportedOn.outputPrefix_eval, MIPRE.CL.CLFun.ExactlyOn.outputPrefix_self, MIPRE.CL.CLFun.ExactlyOn.outputPrefix_univ, MIPRE.Introspection.agreement_subtest_average, MIPRE.Introspection.sampling_pauli_estimate, MIPRE.Introspection.sampling_prefix_estimate, MIPRE.Introspection.mapped_operator_zero_of_not_range, MIPRE.Introspection.off_range_weight_le, MIPRE.Introspection.same_side_via_common_other, MIPRE.Introspection.hiding_same_side_estimate, MIPRE.Introspection.operator_chain_telescope, MIPRE.Introspection.stateSqNorm_hiding_chain, MIPRE.Introspection.hiding_chain_average, MIPRE.Introspection.hiding_chain_uniform
statement: formalized
proof: formalized
---

# Sampling and hiding subtest estimates

Construct a CL output-prefix map on every claimed full output; on honest outputs it agrees with the truncated CL evaluation. For any finite game, a subtest of weight $c>0$ whose accepted answers force equality of processed outcomes gives averaged squared cross-party distance at most $2\varepsilon/c$, where the game's failure is at most $\varepsilon$. The probability hypothesis is a pushforward bound, so the sampled question map need not be injective. Replacing one side by ideal Pauli readouts of squared error $\eta$ costs at most $2\eta+4\varepsilon/c$. All output values, including impossible claims, are controlled. Two such tests with a common opposite-party measurement give a same-side bound $4\varepsilon/c_1+4\varepsilon/c_2$. A chain of $k$ squared edge errors bounded by $\delta$ costs at most $k^2\delta$, without an outcome-cardinality factor.

## Depends on

- [Conditionally linear function](../part-01/def-cl-function.md)
- [Structure of a CL function](../part-01/lem-cl-structure.md)
- [Bipartite model](../../downstream-results/part-02/def-bipartite-model.md)
- [Nonlocal game](../../foundations/part-01/def-game.md)

## Proof

Coarse-grain the accepted-answer relations before converting consistency to distance. The opposite-party triangle inequality then gives the same-side estimate. Telescope the operator chain and use Cauchy–Schwarz. These are checked subtest lemmas; their acceptance implications and probability bounds must still be instantiated for the actual introspective decision procedure.

## Lean

Formalized as [`MIPRE.CL.CLFun.SupportedOn.proj_eval_cons`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.SupportedOn.proj_eval_cons), [`MIPRE.CL.CLFun.SupportedOn.outputPrefix_eval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.SupportedOn.outputPrefix_eval), [`MIPRE.CL.CLFun.ExactlyOn.outputPrefix_self`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.ExactlyOn.outputPrefix_self), [`MIPRE.CL.CLFun.ExactlyOn.outputPrefix_univ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.ExactlyOn.outputPrefix_univ), [`MIPRE.Introspection.agreement_subtest_average`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.agreement_subtest_average), [`MIPRE.Introspection.sampling_pauli_estimate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.sampling_pauli_estimate), [`MIPRE.Introspection.sampling_prefix_estimate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.sampling_prefix_estimate), [`MIPRE.Introspection.mapped_operator_zero_of_not_range`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.mapped_operator_zero_of_not_range), [`MIPRE.Introspection.off_range_weight_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.off_range_weight_le), [`MIPRE.Introspection.same_side_via_common_other`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.same_side_via_common_other), [`MIPRE.Introspection.hiding_same_side_estimate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.hiding_same_side_estimate), [`MIPRE.Introspection.operator_chain_telescope`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.operator_chain_telescope), [`MIPRE.Introspection.stateSqNorm_hiding_chain`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.stateSqNorm_hiding_chain), [`MIPRE.Introspection.hiding_chain_average`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.hiding_chain_average), [`MIPRE.Introspection.hiding_chain_uniform`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.hiding_chain_uniform).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1661](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1661)
