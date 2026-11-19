---
declaration: lemma
origin: cited
lean: MIPRE.CL.Detyping.restrictAnswers_state, MIPRE.CL.Detyping.restrictAnswers_failAt_le, MIPRE.CL.Detyping.restrictAnswers_failure_le, MIPRE.CL.Detyping.restrictAnswers_value_ge
statement: formalized
proof: formalized
---

# Detyping with answer coarse-graining

Allow different typed and detyped answer alphabets, with question-dependent coarse-graining maps. If acceptance on every valid edge implies acceptance after those maps, restriction and coarse-graining preserve the state and give failure at most $16^{|T|}$ times the detyped failure. Thus a decider may reject additional overlong answers. The program-level cutoff must still establish the stated acceptance implication.

## Depends on

- [Finite-game detyping soundness](../part-02/lem-detype-game-soundness.md)

## Proof

Adapt the strategy's questions and coarse-grain its answer measurements. The acceptance implication bounds conditional failure on each edge. Sum those bounds and apply the already proved detyping conditional-distribution identity.

## Lean

Formalized as [`MIPRE.CL.Detyping.restrictAnswers_state`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.restrictAnswers_state), [`MIPRE.CL.Detyping.restrictAnswers_failAt_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.restrictAnswers_failAt_le), [`MIPRE.CL.Detyping.restrictAnswers_failure_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.restrictAnswers_failure_le), [`MIPRE.CL.Detyping.restrictAnswers_value_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.restrictAnswers_value_ge).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 611](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L611)
