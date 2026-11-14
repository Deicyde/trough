---
declaration: lemma
origin: cited
lean: MIPRE.Halting.comprStr_accepts, MIPRE.Halting.CompressorSpec.toObligations, MIPRE.Halting.accepts_iff, MIPRE.Halting.accepts_iff_W, MIPRE.Halting.A_of_branch1, MIPRE.Halting.B_of_branch2, MIPRE.Halting.rejectsLong_of_not_branch1, MIPRE.Halting.A_step, MIPRE.Halting.B_step
statement: formalized
proof: formalized
---

# Values of the halting verifier

For every $n$:

1. if $\mathcal{M}$ halts within $n$ steps then $\mathrm{val}^*(\mathsf{V}^{\mathsf{halt}}_n) = 1$, witnessed by a value-$1$ PCC strategy;
2. if $\mathcal{M}$ does not halt within $n$ steps then $\mathsf{V}^{\mathsf{halt}}_n$ and $\mathsf{V}^{\textsc{Compr}}_n$ are the same game up to an identification of the answer alphabets; in particular $\mathrm{val}^*(\mathsf{V}^{\mathsf{halt}}_n) = \mathrm{val}^*(\mathsf{V}^{\textsc{Compr}}_n)$, and $\mathsf{V}^{\mathsf{halt}}_n$ has a value-$1$ PCC strategy if and only if $\mathsf{V}^{\textsc{Compr}}_n$ does.

## Depends on

- [The self-referential decider is well defined](lem-halt-construction.md)
- [The compressed sampler does not depend on the verifier](lem-compress-sampler-indep.md)
- [PCC strategy](../../foundations/part-01/def-pcc.md)
- [Quantum value](../../foundations/part-01/def-q-value.md)
- [Soundness of compression in a value model](../../downstream-results/part-01/def-compression-co-sound.md)

## Proof

Item 1 is the fixed-answer strategy: when $\mathcal{M}$ halts within $n$ steps, $\mathcal{D}^{\mathsf{halt}}$ accepts every answer pair on every question pair in the support, so any strategy has value $1$ and the constant-$0$ strategy is PCC. For item 2, $\mathcal{D}^{\mathsf{halt}}$ at index $n$ performs the same question-length check as $\mathcal{D}^{\textsc{Compr}}$ and then runs $\mathcal{D}^{\textsc{Compr}}(n, x, y, a, b)$ verbatim, with $\mathtt{TIMEOUT}$ rejecting in both, so the two deciders accept on exactly the same inputs; and the two verifiers share the sampler $\mathcal{S}^{\mathsf{halt}} = \mathtt{ComputeSampler}(\lambda)$ (Lemma [The compressed sampler does not depend on the verifier](lem-compress-sampler-indep.md)), so a strategy for either is a strategy for the other with the same winning probability. The timeout counter of $\mathcal{D}^{\mathsf{halt}}$ does not interfere: its bound is chosen in Lemma [The parameter of the halting verifier](lem-lambda.md) so that the computations above finish first.

## Lean

Formalized as [`MIPRE.Halting.comprStr_accepts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.comprStr_accepts), [`MIPRE.Halting.CompressorSpec.toObligations`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.CompressorSpec.toObligations), [`MIPRE.Halting.accepts_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.accepts_iff), [`MIPRE.Halting.accepts_iff_W`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.accepts_iff_W), [`MIPRE.Halting.A_of_branch1`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.A_of_branch1), [`MIPRE.Halting.B_of_branch2`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.B_of_branch2), [`MIPRE.Halting.rejectsLong_of_not_branch1`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.rejectsLong_of_not_branch1), [`MIPRE.Halting.A_step`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.A_step), [`MIPRE.Halting.B_step`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.B_step).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 7266](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L7266)
