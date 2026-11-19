---
declaration: lemma
origin: cited
lean: MIPRE.Halting.haltProg, MIPRE.Halting.prepProg, MIPRE.Halting.prepProg_runs, MIPRE.Halting.haltProg_runs, MIPRE.Halting.haltProg_runs_inv, MIPRE.Halting.haltProg_accepts_iff, MIPRE.Halting.comprStr, MIPRE.Cost.Prog.readProg, MIPRE.Cost.Prog.readProg_runs, MIPRE.Cost.Prog.wrapBuildProg, MIPRE.Cost.Prog.freezeBuildProg, MIPRE.Halting.prep, MIPRE.Halting.body, MIPRE.Halting.F, MIPRE.Halting.dec, MIPRE.Halting.Vhalt, MIPRE.Halting.body_runs_iff, MIPRE.Halting.dec_runs_iff
statement: formalized
proof: formalized
---

# The self-referential decider is well defined

There is a Turing machine $F$ and a decider $\mathcal{D}^{\mathsf{halt}} = F$ carrying its own description, with a timeout bound $B_{\mathcal{D}^{\mathsf{halt}}}(n)$, such that $\mathcal{D}^{\mathsf{halt}}$ is total within its timeout and $\mathsf{V}^{\mathsf{halt}} = (\mathtt{ComputeSampler}(\lambda), \mathcal{D}^{\mathsf{halt}})$ is a normal form verifier. The self-reference is by direct construction rather than by the recursion theorem, the input-length check precedes the $n$-step simulation of $\mathcal{M}$, and the halting-freeze convention makes the decider total.

## Depends on

- [Normal form verifier in the ambient model](../../foundations/part-03/def-normal-verifier.md)
- [The compressed sampler does not depend on the verifier](lem-compress-sampler-indep.md)
- [Gap-preserving compression from ambient stage contracts](thm-compression.md)
- [Succinct description](../../foundations/part-02/def-succinct.md)
- [Efficient Kleene recursion theorem](../../computability/lem-kleene.md)

## Proof

By construction: the decider is the program `MIPRE.Halting.haltProg`, closed (`haltProg_wellScoped`), and the verifier the compressor's output denotes is a normal form verifier because every string denotes one (`Vof_comprStr`, `Verifier.ofSamplerDecider`). Totality on succinct descriptions is `haltProg_runs` with `haltProg_runs_inv`; the time bound that replaces the timeout counter is Lemma [The parameter of the halting verifier](lem-lambda.md).

## Lean

Formalized as [`MIPRE.Halting.haltProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.haltProg), [`MIPRE.Halting.prepProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.prepProg), [`MIPRE.Halting.prepProg_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.prepProg_runs), [`MIPRE.Halting.haltProg_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.haltProg_runs), [`MIPRE.Halting.haltProg_runs_inv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.haltProg_runs_inv), [`MIPRE.Halting.haltProg_accepts_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.haltProg_accepts_iff), [`MIPRE.Halting.comprStr`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.comprStr), [`MIPRE.Cost.Prog.readProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Prog.readProg), [`MIPRE.Cost.Prog.readProg_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Prog.readProg_runs), [`MIPRE.Cost.Prog.wrapBuildProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Prog.wrapBuildProg), [`MIPRE.Cost.Prog.freezeBuildProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Prog.freezeBuildProg), [`MIPRE.Halting.prep`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.prep), [`MIPRE.Halting.body`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.body), [`MIPRE.Halting.F`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.F), [`MIPRE.Halting.dec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.dec), [`MIPRE.Halting.Vhalt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.Vhalt), [`MIPRE.Halting.body_runs_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.body_runs_iff), [`MIPRE.Halting.dec_runs_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.dec_runs_iff).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 7083](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L7083)
