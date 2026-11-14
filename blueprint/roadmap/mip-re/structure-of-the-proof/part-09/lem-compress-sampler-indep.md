---
declaration: lemma
origin: cited
lean: MIPRE.Pipeline.sampler, MIPRE.Pipeline.samplerProg_eq, MIPRE.Pipeline.output_sampler
statement: formalized
proof: formalized
---

# The compressed sampler does not depend on the verifier

For all inputs $(\mathsf{V}, \lambda)$ — $\lambda$-bounded or not, well-formed or not — the sampler $\mathcal{S}^{\textsc{Compr}}$ of ${\mathsf{Compress}}(\mathsf{V}, \lambda)$ depends only on $\lambda$, and there is a Turing machine $\mathtt{ComputeSampler}$ that outputs its description from $\lambda$ in time $\mathrm{polylog}(\lambda)$.

## Depends on

- [Normal form verifier in the ambient model](../../foundations/part-03/def-normal-verifier.md)
- [Conditionally linear function](../part-01/def-cl-function.md)
- [Parallel repetition of normal form verifiers](thm-parallel-repetition.md)
- [Ambient introspection contract](../part-06/def-introspection-contract.md)
- [Ambient answer-reduction contract](def-answer-reduction-contract.md)

## Proof depends on

- [A universal repetition exponent](lem-compress-tau.md)

## Proof

Chain the verifier-independence of the sampler through the three stages: introspection's sampler depends only on $(\lambda, \ell)$, answer reduction's only on its input sampler and the parameters, and repetition's only on its input sampler and $(\lambda, \ell, \tau)$. $\mathtt{ComputeSampler}$ is then realized by running ${\mathsf{Compress}}$ on the trivial verifier. It is this lemma that makes the recursion of Section [The halting reduction](../README.md) possible at all: a fixed point has to quote its own sampler, so the sampler must not depend on what is being compressed. In Lean the lemma is built into the statement of Theorem [Gap-preserving compression from ambient stage contracts](thm-compression.md): the fields `sampler` and `samplerProg` of `MIPRE.GapCompression` are the map $\lambda \mapsto \mathcal{S}^{\textsc{Compr}}_\lambda$ and its polynomial-time description, and `output_sampler` says that every output carries it. The chaining is `MIPRE.Pipeline.sampler`, the composite of the three sampler maps, with `samplerProg_eq` its polynomial-time description and `output_sampler` the claim for every input.

## Lean

Formalized as [`MIPRE.Pipeline.sampler`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Pipeline.sampler), [`MIPRE.Pipeline.samplerProg_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Pipeline.samplerProg_eq), [`MIPRE.Pipeline.output_sampler`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Pipeline.output_sampler).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 6445](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L6445)
