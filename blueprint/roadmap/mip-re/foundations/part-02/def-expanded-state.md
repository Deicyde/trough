---
declaration: definition
origin: cited
lean: MIPRE.expVec, MIPRE.expEquiv, MIPRE.sum_prod_mul, MIPRE.norm_evec_expVec, MIPRE.expVec_dotProduct, MIPRE.expVec_unit, MIPRE.mulVec_kron_expVec, MIPRE.norm_stateVec_kron_unitary, MIPRE.norm_stateVec_expVec_kron_one, MIPRE.expVec_dotProduct_of_pair, MIPRE.mulVec_kron_kron_expVec, MIPRE.bornProb_expVec_kron, MIPRE.POVM.kron, MIPRE.POVM.kron_mats, MIPRE.bornProb_sum_sum, MIPRE.sum_bornProb_le_map, MIPRE.IsPVM.toPOVM, MIPRE.IsPVM.toPOVM_mats, MIPRE.POVM.ext', MIPRE.POVM.map_mats, MIPRE.POVM.map_map, MIPRE.POVM.kron_map, MIPRE.IsPVM.coarse, MIPRE.isPVM_kron, MIPRE.isPVM_povm_map, MIPRE.isPVM_povm_kron
statement: formalized
---

# The expanded state, and an inert ancilla

Let $|\psi\rangle$ be a state on $\mathbb{C}^{d_\textsc{A}} \otimes \mathbb{C}^{d_\textsc{B}}$ and $|e\rangle$ one on $\mathbb{C}^{a} \otimes \mathbb{C}^{a'}$. The *expanded state* is $|\psi\rangle \otimes |e\rangle$, **re-bipartitioned** so that the first party holds $\mathbb{C}^{d_\textsc{A}} \otimes \mathbb{C}^{a}$ and the second $\mathbb{C}^{d_\textsc{B}} \otimes \mathbb{C}^{a'}$: one half of the ancilla goes to each. Then

1. an operator of product form acts factor by factor, $\bigl((M \otimes N) \otimes {I}\bigr)(|\psi\rangle \otimes |e\rangle) = \bigl((M \otimes {I})|\psi\rangle\bigr) \otimes \bigl((N \otimes {I})|e\rangle\bigr)$;
2. the norm of a product state is the product of the norms, so the expanded state is a unit vector when both factors are;
3. consequently an operator with an *inert* ancilla has the same state-norm on the expanded state as on the original one: $\left\| {(M \otimes {I}_a) \otimes {I} \,|\hat\psi\rangle} \right\| = \left\| {(M \otimes {I}_\textsc{B})|\psi\rangle} \right\|$ when $|e\rangle$ is a unit vector;
4. and a *unitary* on the ancilla is invisible: $\left\| {(M \otimes U) \otimes {I} |\hat\psi\rangle} \right\| = \left\| {(M \otimes {I}_a) \otimes {I} |\hat\psi\rangle} \right\|$.

## Depends on

- [State-dependent POVM distance](def-state-distance.md)

## Lean

Formalized as [`MIPRE.expVec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.expVec), [`MIPRE.expEquiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.expEquiv), [`MIPRE.sum_prod_mul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_prod_mul), [`MIPRE.norm_evec_expVec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.norm_evec_expVec), [`MIPRE.expVec_dotProduct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.expVec_dotProduct), [`MIPRE.expVec_unit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.expVec_unit), [`MIPRE.mulVec_kron_expVec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.mulVec_kron_expVec), [`MIPRE.norm_stateVec_kron_unitary`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.norm_stateVec_kron_unitary), [`MIPRE.norm_stateVec_expVec_kron_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.norm_stateVec_expVec_kron_one), [`MIPRE.expVec_dotProduct_of_pair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.expVec_dotProduct_of_pair), [`MIPRE.mulVec_kron_kron_expVec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.mulVec_kron_kron_expVec), [`MIPRE.bornProb_expVec_kron`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.bornProb_expVec_kron), [`MIPRE.POVM.kron`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.POVM.kron), [`MIPRE.POVM.kron_mats`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.POVM.kron_mats), [`MIPRE.bornProb_sum_sum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.bornProb_sum_sum), [`MIPRE.sum_bornProb_le_map`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_bornProb_le_map), [`MIPRE.IsPVM.toPOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsPVM.toPOVM), [`MIPRE.IsPVM.toPOVM_mats`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsPVM.toPOVM_mats), [`MIPRE.POVM.ext'`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.POVM.ext'), [`MIPRE.POVM.map_mats`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.POVM.map_mats), [`MIPRE.POVM.map_map`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.POVM.map_map), [`MIPRE.POVM.kron_map`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.POVM.kron_map), [`MIPRE.IsPVM.coarse`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsPVM.coarse), [`MIPRE.isPVM_kron`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.isPVM_kron), [`MIPRE.isPVM_povm_map`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.isPVM_povm_map), [`MIPRE.isPVM_povm_kron`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.isPVM_povm_kron).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 661](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L661)
