---
declaration: lemma
origin: cited
lean: MIPRE.BipartiteModel.norm_expandA_ψ, MIPRE.BipartiteModel.qform_expandA, MIPRE.BipartiteModel.bornProb_expandA, MIPRE.BipartiteModel.stateSqNorm_expandA, MIPRE.BipartiteModel.inertA_W_ψ, MIPRE.BipartiteModel.LocalIsometry.expand_W_ψ, MIPRE.BipartiteModel.LocalIsometry.expandA_W_ψ, MIPRE.BipartiteModel.exchange_W_ψ
statement: formalized
proof: formalized
---

# The one-sided ancilla extension

On the one-sided extension, a quadratic form, a Born probability or a squared state norm is that of the $(t_0, t_0)$ entry, or of the $t_0$-th column, in $M$; the state keeps its norm; the inert embedding, the extensions of a local isometry and the exchange of layers carry the state to the state.

## Depends on

- [The one-sided ancilla extension](def-one-sided-extension.md)

## Proof

The state has one nonzero component, in the copy $t_0$, so every operator acts on it through its column $t_0$.

## Lean

Formalized as [`MIPRE.BipartiteModel.norm_expandA_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.norm_expandA_ψ), [`MIPRE.BipartiteModel.qform_expandA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.qform_expandA), [`MIPRE.BipartiteModel.bornProb_expandA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.bornProb_expandA), [`MIPRE.BipartiteModel.stateSqNorm_expandA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.stateSqNorm_expandA), [`MIPRE.BipartiteModel.inertA_W_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.inertA_W_ψ), [`MIPRE.BipartiteModel.LocalIsometry.expand_W_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.expand_W_ψ), [`MIPRE.BipartiteModel.LocalIsometry.expandA_W_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.expandA_W_ψ), [`MIPRE.BipartiteModel.exchange_W_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.exchange_W_ψ).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1951](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1951)
