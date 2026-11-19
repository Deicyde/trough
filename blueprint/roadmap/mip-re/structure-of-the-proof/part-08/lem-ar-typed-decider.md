---
declaration: lemma
origin: cited
lean: MIPRE.AnswerReduction.ldB_aline, MIPRE.AnswerReduction.ldB_dline, MIPRE.AnswerReduction.sideB_eq, MIPRE.AnswerReduction.verdictB_eq, MIPRE.AnswerReduction.verdictP_apply, MIPRE.AnswerReduction.parseBP_apply, MIPRE.AnswerReduction.typedDecider, MIPRE.AnswerReduction.core_runs, MIPRE.AnswerReduction.accepts_iff, MIPRE.AnswerReduction.total, MIPRE.AnswerReduction.size_margQuery_le, MIPRE.AnswerReduction.typedDecider_time
statement: formalized
proof: formalized
---

# The typed answer-reduced decider

For a PCP decider and parameters $(\lambda,\mu,\sigma)$, and an $(\ell+1)$-level input verifier $(S,D)$, there is a typed decider on the types of Definition [The typed answer-reduced game](def-ar-typed-game.md), computed from the programs of $S$ and $D$ and $(\lambda,\mu,\sigma)$, which halts on every input and, on the bits of any two questions of that game and any two answers, accepts exactly when that game's predicate does, with the game check run at $\mathrm{pcpparams}(n,T,Q,\sigma)$, $Q=(\lambda n+1)^\mu$, $T=2^{(Q+5)(\mu+1)}$. Under the hypotheses of Lemma [The typed answer-reduced sampler](lem-ar-typed-sampler.md), and $|D|\le W$, it runs within $(C(W+1)^M(|d|+1)^E)^{\mu+1}$ on every input $(n,d)$ whose two questions have oracle halves of length at most $W$ — as the questions the detyping compiler hands it have.

## Depends on

- [The typed answer-reduced game](def-ar-typed-game.md)
- [The typed answer-reduced sampler](lem-ar-typed-sampler.md)

## Proof depends on

- [An executable balanced seed selector and line stages](../part-06/lem-intro-executable-seeded-lines.md)

## Proof

The decider runs the sampler's parameter routine, computes $Q$ and $T$, asks the input sampler for both players' full marginals at the oracle halves of the two questions through the universal machine, and runs the PCP verifier on each question's game-check view. It then parses each answer into $k$-bit blocks and decides on blocks. Of the low-degree test's decision only a point question against a line question of the same copy is ever checked, and there it is the line-versus-point check of the introspection programs on the line the question describes: the seed's high bits select the axis or mask the diagonal direction, and the line's base point is the sampler's third-stage representative. The five steps are organised by what the type pair asks for: at most one comparison of two answer blocks, one low-degree subtest and one game check, chosen by a finite table of the types. Every stage halts on every input, since the parses are total, the input sampler halts on every input and the PCP verifier runs on the encoding of a genuine input; so no clock is needed, and acceptance is the predicate by determinism. Its time is dominated as the sampler's is: each marginal query is the oracle half of a question with a constant-size header, and everything else is polynomial-time work on the context.

## Lean

Formalized as [`MIPRE.AnswerReduction.ldB_aline`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.ldB_aline), [`MIPRE.AnswerReduction.ldB_dline`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.ldB_dline), [`MIPRE.AnswerReduction.sideB_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.sideB_eq), [`MIPRE.AnswerReduction.verdictB_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.verdictB_eq), [`MIPRE.AnswerReduction.verdictP_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.verdictP_apply), [`MIPRE.AnswerReduction.parseBP_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.parseBP_apply), [`MIPRE.AnswerReduction.typedDecider`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.typedDecider), [`MIPRE.AnswerReduction.core_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.core_runs), [`MIPRE.AnswerReduction.accepts_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.accepts_iff), [`MIPRE.AnswerReduction.total`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.total), [`MIPRE.AnswerReduction.size_margQuery_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.size_margQuery_le), [`MIPRE.AnswerReduction.typedDecider_time`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.typedDecider_time).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 5569](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5569)
