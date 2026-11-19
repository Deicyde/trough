---
declaration: lemma
origin: cited
lean: MIPRE.AnswerReduction.exists_paramsBound_classical
statement: formalized
proof: formalized
---

# PCP complexity

${{\mathsf{M}}^{\mathsf{ar}}}$ runs in time $\mathrm{poly}(\log T, \log n, Q, \sigma)$, with circuit-size and randomness bounds of the same form. These are the bounds the composition of Remark [Answer-reduction correspondence and optional rank bounds](../README.md) consumes; in particular the randomness bound is what makes the answer-reduced sampler conditionally linear.

## Depends on

- [The PCP's proof format and query structure](lem-pcp-format.md)
- [The typed answer-reduced sampler](lem-ar-typed-sampler.md)

## Proof

The verifier is a polynomial-time program, and its encoded input on a formatted view is polynomial in $\log n+\log T+Q+\sigma$ (`pcpInput_size_polynomial`), whence its running time (`verifyPcp_time_le`). The circuit has $m'$ coordinates, polynomial in the same quantity (`outerDim_polynomial`), and the randomness, a point of $\mathbb F_q^{m'}$, is $km'$ bits, polynomial by the parameter bound (`exists_paramsBound_classical`).

## Lean

Formalized as [`MIPRE.AnswerReduction.exists_paramsBound_classical`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.exists_paramsBound_classical).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 5226](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5226)
