---
declaration: lemma
origin: cited
lean: MIPRE.BipartiteModel.norm_reg_ψ, MIPRE.BipartiteModel.reg_mirror, MIPRE.BipartiteModel.reg_mirror_smulKron, MIPRE.BipartiteModel.regRelabel_W_ψ, MIPRE.BipartiteModel.regSplit_W_ψ, MIPRE.BipartiteModel.regExtend_W_ψ, MIPRE.BipartiteModel.regSwap_W_ψ, MIPRE.Introspection.registerEPR_equiv, MIPRE.Introspection.registerEPR_prod
statement: formalized
proof: formalized
---

# The register model

The state of the register model has the norm of the state of $N$. A matrix $P$ on the first player's register acts on the state as its transpose $P^{\mathsf T}$ on the second player's. Relabelling, splitting, extending and exchanging carry the state of one register model to the state of the other.

## Depends on

- [The register model](def-register-model.md)
- [Moving registers along local isometries](lem-ancilla-isometries.md)
- [The ancilla extension](../part-02/lem-ancilla-extension.md)
- [The expanded state, and an inert ancilla](../../foundations/part-02/def-expanded-state.md)

## Proof depends on

- [Local isometries carry the Born rule](lem-local-isometry.md)

## Proof

The mirror identity is $(P \otimes {I})|\mathrm{EPR}_I\rangle = ({I} \otimes P^{\mathsf T}) |\mathrm{EPR}_I\rangle$ in the ancilla factor. The others are the lemma on moving registers, with $|\mathrm{EPR}_{J \times R}\rangle = |\mathrm{EPR}_J\rangle \otimes |\mathrm{EPR}_R\rangle$ and the invariance of $|\mathrm{EPR}\rangle$ under relabelling.

## Lean

Formalized as [`MIPRE.BipartiteModel.norm_reg_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.norm_reg_ψ), [`MIPRE.BipartiteModel.reg_mirror`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.reg_mirror), [`MIPRE.BipartiteModel.reg_mirror_smulKron`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.reg_mirror_smulKron), [`MIPRE.BipartiteModel.regRelabel_W_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.regRelabel_W_ψ), [`MIPRE.BipartiteModel.regSplit_W_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.regSplit_W_ψ), [`MIPRE.BipartiteModel.regExtend_W_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.regExtend_W_ψ), [`MIPRE.BipartiteModel.regSwap_W_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.regSwap_W_ψ), [`MIPRE.Introspection.registerEPR_equiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.registerEPR_equiv), [`MIPRE.Introspection.registerEPR_prod`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.registerEPR_prod).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1890](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1890)
