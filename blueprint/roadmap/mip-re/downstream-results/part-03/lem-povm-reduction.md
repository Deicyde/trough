---
declaration: lemma
origin: cited
lean: MIPRE.BipartiteModel.POVMReduces.refl, MIPRE.BipartiteModel.POVMReduces.trans, MIPRE.BipartiteModel.POVMReduces.swap, MIPRE.BipartiteModel.LocalIsometry.povmReduces, MIPRE.BipartiteModel.povmReduces_expandA, MIPRE.BipartiteModel.povmReduces_expandB, MIPRE.BipartiteModel.povmValue_swap_game, MIPRE.ValueModel.DominatesPOVM.of_povmReduces, MIPRE.ModelOver.povmReduces_expandA, MIPRE.ModelOver.norm_expandA_ψ, MIPRE.POVMIn.compress_op
statement: formalized
proof: formalized
---

# Reductions

Reduction is reflexive and transitive and survives exchanging the players. A model reduces to any model it receives a unital local isometry from that carries the state to the state, and a one-sided extension, on either side, reduces to the model. A value model dominating the POVM strategies of $M$ dominates those of every model reducing to $M$.

## Depends on

- [Reduction of POVM strategies](def-povm-reduction.md)
- [Local isometries carry the Born rule](lem-local-isometry.md)
- [The one-sided ancilla extension](lem-one-sided-extension.md)
- [Domination of the POVM strategies, and approximation by projective strategies](def-povm-domination.md)

## Proof

On the one-sided extension, the Born probability of a pair of POVMs is that of the $(t_0, t_0)$ entries (Lemma [The one-sided ancilla extension](lem-one-sided-extension.md)), and the diagonal blocks of a POVM in $M_T({\mathscr{A}}_A)$ form a POVM in ${\mathscr{A}}_A$. The rest is a composition.

## Lean

Formalized as [`MIPRE.BipartiteModel.POVMReduces.refl`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.POVMReduces.refl), [`MIPRE.BipartiteModel.POVMReduces.trans`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.POVMReduces.trans), [`MIPRE.BipartiteModel.POVMReduces.swap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.POVMReduces.swap), [`MIPRE.BipartiteModel.LocalIsometry.povmReduces`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.povmReduces), [`MIPRE.BipartiteModel.povmReduces_expandA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.povmReduces_expandA), [`MIPRE.BipartiteModel.povmReduces_expandB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.povmReduces_expandB), [`MIPRE.BipartiteModel.povmValue_swap_game`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.povmValue_swap_game), [`MIPRE.ValueModel.DominatesPOVM.of_povmReduces`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.DominatesPOVM.of_povmReduces), [`MIPRE.ModelOver.povmReduces_expandA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ModelOver.povmReduces_expandA), [`MIPRE.ModelOver.norm_expandA_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ModelOver.norm_expandA_ψ), [`MIPRE.POVMIn.compress_op`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.POVMIn.compress_op).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2038](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2038)
