---
declaration: lemma
origin: cited
lean: MIPRE.AnswerReduction.sum_dis_MA1_MB6_le, MIPRE.AnswerReduction.sum_dis_MA6_MB1_le
statement: formalized
proof: formalized
---

# Input-codeword consistency tests

The two input-codeword tests, conditioned on their respective typed questions, have $O(\theta)$ failure on the required seeded point/line laws. The distributions are conditioned before averaging over $\xi$, and include answer formats and equality tests. These supply both input evaluation relations consumed by the individual-polynomial extraction.

## Depends on

- [Global PCP consistency tests](lem-ar-global-tests.md)

## Proof

The two input-codeword tests are type pairs of the typed game: an isolated player's point of copy $i$ against the oracle's $\mathrm{Point}_6$, in both orders of the players. Each fails at most the conditioned typed failure, which bounds the disagreement of the two evaluations averaged over the seed.

## Lean

Formalized as [`MIPRE.AnswerReduction.sum_dis_MA1_MB6_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.sum_dis_MA1_MB6_le), [`MIPRE.AnswerReduction.sum_dis_MA6_MB1_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.sum_dis_MA6_MB1_le).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 5781](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5781)
