---
declaration: lemma
origin: cited
lean: MIPRE.Halting.SamplerFamily, MIPRE.Halting.SamplerFamily.sampProg, MIPRE.Halting.SamplerFamily.sampProg_runs, MIPRE.Halting.SamplerFamily.classSampler, MIPRE.Halting.SamplerFamily.classSampler_runs, MIPRE.Halting.SamplerFamily.Samples, MIPRE.Halting.SamplerFamily.samples_of_runs, MIPRE.Halting.SamplerFamily.questions_eq, MIPRE.Halting.SamplerFamily.qEmb, MIPRE.Halting.SamplerFamily.seedCount_eq, MIPRE.Halting.SamplerFamily.game_μ_qEmb, MIPRE.Halting.SamplerFamily.game_support
statement: formalized
proof: formalized
---

# The class verifiers' sampler

Let $\lambda \mapsto \mathcal{S}^\lambda$ be samplers of a level $\ell$ whose programs are computed from $\lambda$ in polynomial time and which run within, and have dimensions at most, a polynomial in $n + \lambda$ at index $n$. Let $R : z \mapsto \mathcal{M}_z$ be computable in polynomial time, $\lambda(z) = \Lambda_0 + 4\left\vert {\mathcal{M}_z} \right\vert$, and $n_0$ an index. There is a program which, on $(z, r)$ with $r$ at least as long as the dimension $s$ of $\mathcal{S}^{\lambda(z)}$ at $n_0$, halts within a polynomial in $\left\vert {z} \right\vert + \left\vert {r} \right\vert$ with the two marginals of $\mathcal{S}^{\lambda(z)}$ at $n_0$ at the first $s$ bits of $r$. For a polynomial-time verifier with this sampler and a polynomial above these bounds, the distribution of its game on $z$ is, on the questions of $\mathcal{S}^{\lambda(z)}$ embedded as bit strings, the distribution of $\mathcal{S}^{\lambda(z)}$ at $n_0$, and it has no weight elsewhere.

## Depends on

- [Sampler](../../foundations/part-03/def-sampler.md)
- [The class $\mathrm{MIP}^*_{1,1/2}(2,1)$](../../foundations/part-03/def-mipstar.md)
- [The parameter of the halting verifier](lem-lambda.md)

## Proof

The program computes $\mathcal{M}_z$, $\lambda(z)$ and the program of $\mathcal{S}^{\lambda(z)}$, asks it its dimension $s$ through the universal machine, converts $s$ to unary, takes the first $s$ bits of the seed and asks the two marginals there; each stage runs within a polynomial in the total input length. At level $0$ the marginal queries are not specified, but the questions are empty, the CL function of level $0$ being exactly on the empty set only, and there the program outputs the empty pair. Of the $2^B$ seeds, those producing a question pair are the extensions of the points of $\mathbb{F}_2^s$ producing it, each in $2^{B - s}$ ways, so the uniform seed pushes forward to the distribution of $\mathcal{S}^{\lambda(z)}$.

## Lean

Formalized as [`MIPRE.Halting.SamplerFamily`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.SamplerFamily), [`MIPRE.Halting.SamplerFamily.sampProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.SamplerFamily.sampProg), [`MIPRE.Halting.SamplerFamily.sampProg_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.SamplerFamily.sampProg_runs), [`MIPRE.Halting.SamplerFamily.classSampler`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.SamplerFamily.classSampler), [`MIPRE.Halting.SamplerFamily.classSampler_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.SamplerFamily.classSampler_runs), [`MIPRE.Halting.SamplerFamily.Samples`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.SamplerFamily.Samples), [`MIPRE.Halting.SamplerFamily.samples_of_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.SamplerFamily.samples_of_runs), [`MIPRE.Halting.SamplerFamily.questions_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.SamplerFamily.questions_eq), [`MIPRE.Halting.SamplerFamily.qEmb`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.SamplerFamily.qEmb), [`MIPRE.Halting.SamplerFamily.seedCount_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.SamplerFamily.seedCount_eq), [`MIPRE.Halting.SamplerFamily.game_μ_qEmb`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.SamplerFamily.game_μ_qEmb), [`MIPRE.Halting.SamplerFamily.game_support`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.SamplerFamily.game_support).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 7342](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L7342)
