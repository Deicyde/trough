---
declaration: lemma
origin: cited
lean: MIPRE.CL.CLFun.embed, MIPRE.CL.CLFun.ExactlyOn.embed, MIPRE.CL.CLFun.eval_embed, MIPRE.CL.CLFun.eval_truncate_embed, MIPRE.CL.CLFun.factorOfPrefix_embed, MIPRE.CL.CLFun.mapOfPrefix_embed, MIPRE.CL.CLFun.zeroOn_exactlyOn, MIPRE.CL.CLFun.eval_truncate_zeroOn, MIPRE.CL.CLFun.mapOfPrefix_zeroOn, MIPRE.CL.CLFun.factorOfPrefix_zeroOn, MIPRE.CL.Detyping.marginal_graph, MIPRE.CL.Detyping.marginal_content, MIPRE.CL.Detyping.factor_first, MIPRE.CL.Detyping.factor_second, MIPRE.CL.Detyping.factor_content, MIPRE.CL.Detyping.linear_first, MIPRE.CL.Detyping.linear_second, MIPRE.CL.Detyping.linear_content
statement: formalized
proof: formalized
---

# Register embeddings and detyped query routing

Embedding a CL presentation along a coordinate injection preserves its marginal, factor and linear-map queries. In the detyped presentation the first two levels route to the graph sampler. Later levels route to the selected typed presentation using the content prefix. On an unselected branch all marginal and linear outputs are zero; the first content factor is the whole content register and the later factors are empty.

## Depends on

- [Detyped conditionally linear functions](lem-detype-cl.md)
- [Closure of CL functions](lem-cl-closure.md)

## Proof

Extend each register-linear map by zero along the coordinate injection and restrict each continuation's prefix to the original register. Induction on the presentation proves all four query identities. After the two graph levels, the accumulated graph prefix is the original graph part of the query prefix, and its content part is unchanged. These identities give the specified dispatch rules, including the zero fallback. They are the semantic correctness targets for the ambient sampler implementation.

## Lean

Formalized as [`MIPRE.CL.CLFun.embed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.embed), [`MIPRE.CL.CLFun.ExactlyOn.embed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.ExactlyOn.embed), [`MIPRE.CL.CLFun.eval_embed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.eval_embed), [`MIPRE.CL.CLFun.eval_truncate_embed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.eval_truncate_embed), [`MIPRE.CL.CLFun.factorOfPrefix_embed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.factorOfPrefix_embed), [`MIPRE.CL.CLFun.mapOfPrefix_embed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.mapOfPrefix_embed), [`MIPRE.CL.CLFun.zeroOn_exactlyOn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.zeroOn_exactlyOn), [`MIPRE.CL.CLFun.eval_truncate_zeroOn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.eval_truncate_zeroOn), [`MIPRE.CL.CLFun.mapOfPrefix_zeroOn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.mapOfPrefix_zeroOn), [`MIPRE.CL.CLFun.factorOfPrefix_zeroOn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.factorOfPrefix_zeroOn), [`MIPRE.CL.Detyping.marginal_graph`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.marginal_graph), [`MIPRE.CL.Detyping.marginal_content`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.marginal_content), [`MIPRE.CL.Detyping.factor_first`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.factor_first), [`MIPRE.CL.Detyping.factor_second`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.factor_second), [`MIPRE.CL.Detyping.factor_content`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.factor_content), [`MIPRE.CL.Detyping.linear_first`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.linear_first), [`MIPRE.CL.Detyping.linear_second`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.linear_second), [`MIPRE.CL.Detyping.linear_content`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.linear_content).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 478](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L478)
