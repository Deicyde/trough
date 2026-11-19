---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.conditional_coarse_consistency, MIPRE.Introspection.CLChecks.prefixRegister_outputPrefix_succ, MIPRE.Introspection.CLChecks.dualReadout_outputPrefix, MIPRE.Introspection.TypedEstimates.hiding_next_accepts_conditional, MIPRE.Introspection.TypedEstimates.hiding_next_conditional_estimate
statement: formalized
proof: formalized
---

# Conditional estimate for the actual adjacent hiding test

The next visited register and dual readout depend only on the claimed output prefix. In the actual parsed adjacent-Hide game, the earlier player's coarse answer is therefore conditioned on precisely the later player's retained prefix. If the later measurement is projective, the conditional squared-distance estimate is at most $2|E|\varepsilon$. The conditioning marginal is retained as an operator; it is not replaced by an unconditional distance or an assumed ideal hiding measurement.

## Depends on

- [The parsed introspection decision predicate](../part-02/lem-intro-parsed-predicate.md)
- [Introspection type graph and typed CL family](../part-02/lem-intro-type-presentation.md)
- [Conditioning on part of a question](../part-02/lem-conditional-measurement.md)
- [Concrete typed sampling and terminal hiding estimates](../part-03/lem-intro-typed-estimates.md)

## Proof

Prove prefix invariance by recursion on the CL presentation. The four accepted-answer comparisons imply the conditional equality of coarse labels. Use the later joint PVM and its marginal to convert conditional consistency to squared distance, and the actual edge probability $1/|E|$ to bound failure.

## Lean

Formalized as [`MIPRE.Introspection.conditional_coarse_consistency`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.conditional_coarse_consistency), [`MIPRE.Introspection.CLChecks.prefixRegister_outputPrefix_succ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CLChecks.prefixRegister_outputPrefix_succ), [`MIPRE.Introspection.CLChecks.dualReadout_outputPrefix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CLChecks.dualReadout_outputPrefix), [`MIPRE.Introspection.TypedEstimates.hiding_next_accepts_conditional`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hiding_next_accepts_conditional), [`MIPRE.Introspection.TypedEstimates.hiding_next_conditional_estimate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hiding_next_conditional_estimate).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2554](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2554)
