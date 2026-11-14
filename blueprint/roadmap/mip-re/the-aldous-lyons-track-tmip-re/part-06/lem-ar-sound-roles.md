---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.eval_seed, MIPRE.Tailored.AnsRed.Typed.arDt_role, MIPRE.Tailored.AnsRed.Typed.one_sub_value_roleStrat_le, MIPRE.Tailored.AnsRed.Typed.one_sub_value_eq_sum, MIPRE.Tailored.AnsRed.Typed.sum_edges_le, MIPRE.Tailored.AnsRed.Typed.sum_edge_le, MIPRE.Tailored.AnsRed.Typed.sum_one_sub_value_roleStrat_le
statement: formalized
proof: formalized
---

# The per-role failures

The failure $\theta$ is the average of $T$'s failure over the $81$ pairs of types and the seeds, so its failures at any set of pairs of types sum, over the seeds, to at most $81 |Z| |W| \theta$. At two typed questions of one role and one oracularized question, the typed data's low-degree check is the test's predicate on the role's codewords, and the per-role strategies' failures at $y_r(z)$ sum over $z \in Z$ to at most $9 |Z| \theta$.

## Depends on

- [The per-role low-degree strategies](def-ar-sound-roles.md)
- [Reading the answer-reduced constraints](lem-ar-tailored-reading.md)

## Proof depends on

- [Post-processing and detyping, in a model](../../downstream-results/part-02/lem-transports-model.md)
- [Operations on projective strategies](../../downstream-results/part-03/lem-model-proj-strategy.md)

## Proof

The detyped failure is the average over the pairs of types and the seeds of the failure at the questions an answer-reduced sampler gives them. A role's nine pairs of types are a ninth of the $81$, and the registers of a uniform vector carry a uniform sample of the test, with multiplicity one.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.eval_seed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.eval_seed), [`MIPRE.Tailored.AnsRed.Typed.arDt_role`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.arDt_role), [`MIPRE.Tailored.AnsRed.Typed.one_sub_value_roleStrat_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.one_sub_value_roleStrat_le), [`MIPRE.Tailored.AnsRed.Typed.one_sub_value_eq_sum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.one_sub_value_eq_sum), [`MIPRE.Tailored.AnsRed.Typed.sum_edges_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_edges_le), [`MIPRE.Tailored.AnsRed.Typed.sum_edge_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_edge_le), [`MIPRE.Tailored.AnsRed.Typed.sum_one_sub_value_roleStrat_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.sum_one_sub_value_roleStrat_le).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3149](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3149)
