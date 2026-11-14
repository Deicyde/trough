---
declaration: lemma
origin: cited
lean: MIPRE.AnswerReduction.cutVal, MIPRE.AnswerReduction.arCut, MIPRE.AnswerReduction.arVerifier, MIPRE.AnswerReduction.arSamplerProg, MIPRE.AnswerReduction.arSamplerProg_eq, MIPRE.AnswerReduction.arCompute, MIPRE.AnswerReduction.arCompute_eq, MIPRE.AnswerReduction.arVerifier_within, MIPRE.CL.Detyping.sampler_time, MIPRE.CL.Detyping.DeciderProgram.route_call_typed, MIPRE.CL.Detyping.DeciderProgram.prog_time, MIPRE.Pipeline.PDom, MIPRE.Pipeline.PRuns
statement: formalized
proof: formalized
---

# Answer-reduction construction

With the parameter and timeout hypotheses of Theorem [Answer reduction](../part-09/thm-answer-reduction.md), construct the typed oracle verifier and the PCP verifier. Downsize the PCP sampler using its explicit field routine before taking the direct sum with the binary oracle sampler. This yields a common binary ambient space and $\max\{\ell,3\}$ typed levels, hence $\max\{\ell+2,5\}$ levels after detyping. The compiled timeout and actual runtimes have the claimed polynomial bounds. Format checks include all proof coefficients and answer components. In the ambient model, for a PCP decider whose parameters are polynomial in $(\log n,\log T,Q,\sigma)$: the output's programs are polynomial-time functions of the input programs and $(\lambda,\mu,\sigma)$, and for a polynomial $P$ and degree $d$ depending only on the PCP, an input within the budget of Definition [Ambient answer-reduction contract](../part-09/def-answer-reduction-contract.md) with $|S|,|D|\le\sigma$ gives an output within $P((\lambda n+1)^\mu+\sigma+\lambda+n)^{\mu+1}$ at input-size degree $d(\mu+1)$ that rejects answers longer than its cut $32(k+1)(m'+7)^2$.

## Depends on

- [The bespoke PCP for deciders](../part-07/thm-pcp-decider.md)
- [The typed answer-reduced sampler](lem-ar-typed-sampler.md)
- [The typed answer-reduced decider](lem-ar-typed-decider.md)
- [Effective inversion, Frobenius iteration and trace](../../background-results/part-05/lem-effective-field-inverse-trace.md)

## Proof

The output is the typed verifier of Lemmas [The typed answer-reduced sampler](lem-ar-typed-sampler.md) and [The typed answer-reduced decider](lem-ar-typed-decider.md) through the detyping compiler, at a cutoff routine that runs the parameter routine and writes both cuts $32(k+1)(m'+7)^2$. Its programs place the input programs in fixed contexts, which is polynomial time. Take $W=(\lambda n+1)^\mu+\sigma+\lambda+n$: it is above $Q$, $\lambda$, $\sigma$, $n$, both input programs' sizes and the input sampler's dimension, so the typed sampler's and decider's bounds apply. The detyped sampler's coefficient is the router's cost polynomial at the index, with the typed sampler's coefficient raised to the router's degree; the detyped decider runs the typed sampler on the dimension query, the cutoff routine, and at most one call to the typed decider on a typed input with questions of the typed sampler's dimension, whose oracle halves are the input sampler's questions, and answers within the cut. The dimension and the cut are polynomial in $W$ and the PCP's parameters. Every bound has the shape $(c(W+1)^m)^{\mu+1}(|d|+1)^{e(\mu+1)}$, and the sum of the constants and the largest exponents give $P$ and $d$.

## Lean

Formalized as [`MIPRE.AnswerReduction.cutVal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.cutVal), [`MIPRE.AnswerReduction.arCut`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.arCut), [`MIPRE.AnswerReduction.arVerifier`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.arVerifier), [`MIPRE.AnswerReduction.arSamplerProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.arSamplerProg), [`MIPRE.AnswerReduction.arSamplerProg_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.arSamplerProg_eq), [`MIPRE.AnswerReduction.arCompute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.arCompute), [`MIPRE.AnswerReduction.arCompute_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.arCompute_eq), [`MIPRE.AnswerReduction.arVerifier_within`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.arVerifier_within), [`MIPRE.CL.Detyping.sampler_time`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.sampler_time), [`MIPRE.CL.Detyping.DeciderProgram.route_call_typed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.DeciderProgram.route_call_typed), [`MIPRE.CL.Detyping.DeciderProgram.prog_time`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.DeciderProgram.prog_time), [`MIPRE.Pipeline.PDom`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Pipeline.PDom), [`MIPRE.Pipeline.PRuns`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Pipeline.PRuns).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 5609](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5609)
