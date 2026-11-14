---
declaration: theorem
origin: cited
lean: MIPRE.Tailored.re_subset_tmipStar_of, MIPRE.Tailored.tmipStar_eq_re_of, MIPRE.Tailored.TailoredGapCompression.samplerFamily, MIPRE.Tailored.seqUniv_runs, MIPRE.Tailored.seqUniv_runs_rev, MIPRE.Tailored.Halting.classTV, MIPRE.Tailored.Halting.classTV_efficient, MIPRE.Tailored.Halting.lenIs_iff, MIPRE.Tailored.Halting.lpIs_iff, MIPRE.Tailored.Halting.tgame_extends, MIPRE.Tailored.Halting.classTV_values
statement: formalized
proof: formalized
---

# $\mathrm{TMIP}^* = \mathrm{RE}$ for the polynomial-time class; II:787, II:1505

Given a tailored gap compression, $\mathrm{TMIP}^* = \mathrm{RE}$ for the class of Definition [The class $\mathrm{TMIP}^*$; II:787, II:1505](def-tmipstar-poly.md).

## Depends on

- [The class $\mathrm{TMIP}^*$; II:787, II:1505](def-tmipstar-poly.md)
- [Recursively enumerable](../../foundations/part-02/def-re.md)
- [The class is contained in the computable one](lem-tmipstar-poly-sub.md)
- [Extending a tailored game along its questions](lem-tailored-extend.md)
- [The class verifiers' sampler](../../structure-of-the-proof/part-09/lem-class-sampler.md)
- [Halting from tailored compression; II:1887–2066](thm-tailored-halting.md)
- [Turing](../../background-results/part-03/thm-halting-undecidable.md)

## Proof

$\mathrm{TMIP}^* \subseteq \mathrm{RE}$ is Lemma [The class is contained in the computable one](lem-tmipstar-poly-sub.md). Conversely, an r.e. language many-one reduces to halting on the empty input by a polynomial-time map $z \mapsto \mathcal{M}_z$, as in Theorem [$\mathrm{MIP}^* = \mathrm{RE}$](../../the-main-theorem/thm-mipstar-eq-re.md). The class verifier on $z$ plays the game of the tailored halting verifier $\mathsf{V}^{\mathcal{M}_z, \lambda(z)}$ at the fixed level $C$, with $\lambda(z) = \Lambda_0 + 4\left\vert {\mathcal{M}_z} \right\vert$. Its sampler is that of Lemma [The class verifiers' sampler](../../structure-of-the-proof/part-09/lem-class-sampler.md) for the compressed samplers. Its calculator and its processor compute, in polynomial time, the programs of the compressed calculator at $\lambda(z)$ and of the processor of $\mathsf{V}^{\mathcal{M}_z, \lambda(z)}$, and run them on $C$ and the rest of the input through the universal machine, which halts exactly when the simulated program does, with its output. They run within polynomials in the total input length: the compressed calculator within $\mathrm{poly}(C, \lambda)$ times a power of the size of its input, and the processor within $Q(C + \left\vert {\mathcal{M}} \right\vert + \lambda)$ times one. So the class verifier's game on $z$ extends that of $\mathsf{V}^{\mathcal{M}_z, \lambda(z)}$ at $C$ along the embedding of its questions as bit strings, and Lemma [Extending a tailored game along its questions](lem-tailored-extend.md) transfers both clauses of Theorem [Halting from tailored compression; II:1887–2066](thm-tailored-halting.md) at the level $C$.

## Lean

Formalized as [`MIPRE.Tailored.re_subset_tmipStar_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.re_subset_tmipStar_of), [`MIPRE.Tailored.tmipStar_eq_re_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.tmipStar_eq_re_of), [`MIPRE.Tailored.TailoredGapCompression.samplerFamily`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGapCompression.samplerFamily), [`MIPRE.Tailored.seqUniv_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.seqUniv_runs), [`MIPRE.Tailored.seqUniv_runs_rev`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.seqUniv_runs_rev), [`MIPRE.Tailored.Halting.classTV`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.classTV), [`MIPRE.Tailored.Halting.classTV_efficient`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.classTV_efficient), [`MIPRE.Tailored.Halting.lenIs_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.lenIs_iff), [`MIPRE.Tailored.Halting.lpIs_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.lpIs_iff), [`MIPRE.Tailored.Halting.tgame_extends`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.tgame_extends), [`MIPRE.Tailored.Halting.classTV_values`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.classTV_values).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1026](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1026)
