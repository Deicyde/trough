---
declaration: lemma
origin: cited
lean: MIPRE.AnswerReduction.sum_edges_le, MIPRE.AnswerReduction.sum_copyFail_le, MIPRE.AnswerReduction.sum_copyFail6_le, MIPRE.AnswerReduction.sum_dis_edge_le
statement: formalized
proof: formalized
---

# Global PCP consistency tests

Conditioning the typed success estimate on each checked type pair gives the global PCP subtests with $O(\theta)$ failure, averaged over uniform $\xi$ and the prescribed PCP seed. Retain the joint proof-tuple format, individual proof-line formats, and all identical-question equality subtests. No low-degree theorem is applied to line–point success alone.

## Depends on

- [Full-seed indexing for answer reduction](def-ar-seed-index.md)
- [The typed answer-reduced game](def-ar-typed-game.md)

## Proof depends on

- [Value transfers of the typed oracularized game](../part-06/lem-oracular-typed-transfers.md)
- [Post-processing and detyping, in a model](../../downstream-results/part-02/lem-transports-model.md)
- [Operations on projective strategies](../../downstream-results/part-03/lem-model-proj-strategy.md)

## Proof

The typed game samples a uniform ordered pair of the $54$ types and a uniform seed, so the failure conditioned on one type pair is at most $54^2\theta=2916\theta$ (`sum_edges_le`). Restricted to one copy's type pairs at a fixed oracle half, the strategy is a strategy for that copy's seeded low-degree game, whose failure is at most the conditioned typed failure, averaged over the seed (`sum_copyFail_le`, `sum_copyFail6_le`); an equality subtest between two players' answers gives their disagreement (`sum_dis_edge_le`).

## Lean

Formalized as [`MIPRE.AnswerReduction.sum_edges_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.sum_edges_le), [`MIPRE.AnswerReduction.sum_copyFail_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.sum_copyFail_le), [`MIPRE.AnswerReduction.sum_copyFail6_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.sum_copyFail6_le), [`MIPRE.AnswerReduction.sum_dis_edge_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.sum_dis_edge_le).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 5755](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5755)
