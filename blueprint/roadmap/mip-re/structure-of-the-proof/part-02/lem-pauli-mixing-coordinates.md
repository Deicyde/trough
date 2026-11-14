---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.snorm_right_projector_le, MIPRE.Introspection.retained_fibre_dist, MIPRE.Introspection.controlledPOVM, MIPRE.Introspection.retained_block_le_completion, MIPRE.Introspection.block_retention_precompletion, MIPRE.Introspection.block_retention_dist_avg, MIPRE.Introspection.mirror_expand, MIPRE.Introspection.reg_wX_mirror, MIPRE.Introspection.reg_readout_mirror, MIPRE.Introspection.pauli_twirl_dist_le, MIPRE.Introspection.fine_commutator_parseval, MIPRE.Introspection.kernel_commutator_parseval, MIPRE.Introspection.pauli_twirl_readout_dist_le, MIPRE.Introspection.exists_pauli_mixing, MIPRE.Introspection.exists_pauli_mixing_avg, MIPRE.Introspection.exists_pauli_mixing_varying, MIPRE.Introspection.mixing_error_sqrt_bound, MIPRE.Introspection.exists_pauli_mixing_sqrt
statement: formalized
proof: formalized
---

# Retained-fibre mixing in coordinate presentations

Over a finite characteristic-two field, write the retained register as $\mathbb{F}^{n_x}$ and the state in each question's coordinates as $\mathrm{EPR}_{\mathbb{F}^{n_x}}\otimes\xi_x$, with $\xi_x$ normalized. Let $e_0,e_Z,e_X$ be the marginal, fine-$Z$ commutator and coarse-$X$ commutator errors of a joint PVM. There are actual normalized POVMs on the complementary Alice space at every retained fibre, whose averaged squared distance from the joint PVM is at most $2\delta+4\sqrt\delta$, where $\delta=\mathbb E_x(2e_0+8e_Z+8e_X)$. If the three averaged errors are at most $0\leq\varepsilon\leq1$, the bound is $56\sqrt\varepsilon$. Register dimensions and auxiliary spaces may vary with $x$. The Lean states it in the register model on $\mathbb{F}^{n_x}$ (Definition [The register model](../../downstream-results/part-03/def-register-model.md)) of a normalized auxiliary model $\Xi_x$, of which $\mathrm{EPR}_{\mathbb{F}^{n_x}}\otimes\xi_x$ is the case of the tensor-product model of $\xi_x$, with the POVMs in the first player's algebra of $\Xi_x$.

## Depends on

- [Linear-map blocks of the twirl](lem-pauli-linear-mixing.md)
- [Commutator Parseval identity](lem-pauli-commutator-transfer.md)
- [Combining two approximate commutations](lem-pauli-two-sided-commutation.md)
- [Completing a nearby submeasurement](lem-close-submeasurement.md)

## Proof depends on

- [Pasting, the two-measurement case](../../foundations/part-02/lem-pasting-updated.md)
- [Projectivity of sampling and hiding readouts](lem-intro-linear-readout-projectivity.md)

## Proof

Twirl into ancillary POVM blocks, keep the matching fibre using the exact EPR mirror, and complete its submeasurement by summing over the discarded output. Average the pointwise estimates using concavity of the square root. This includes empty fibres. The ambient coordinate transport is proved in Lemma [Pauli mixing with a retained classical fibre](lem-pauli-mixing.md).

## Lean

Formalized as [`MIPRE.Introspection.snorm_right_projector_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.snorm_right_projector_le), [`MIPRE.Introspection.retained_fibre_dist`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.retained_fibre_dist), [`MIPRE.Introspection.controlledPOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.controlledPOVM), [`MIPRE.Introspection.retained_block_le_completion`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.retained_block_le_completion), [`MIPRE.Introspection.block_retention_precompletion`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.block_retention_precompletion), [`MIPRE.Introspection.block_retention_dist_avg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.block_retention_dist_avg), [`MIPRE.Introspection.mirror_expand`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.mirror_expand), [`MIPRE.Introspection.reg_wX_mirror`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.reg_wX_mirror), [`MIPRE.Introspection.reg_readout_mirror`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.reg_readout_mirror), [`MIPRE.Introspection.pauli_twirl_dist_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.pauli_twirl_dist_le), [`MIPRE.Introspection.fine_commutator_parseval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.fine_commutator_parseval), [`MIPRE.Introspection.kernel_commutator_parseval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.kernel_commutator_parseval), [`MIPRE.Introspection.pauli_twirl_readout_dist_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.pauli_twirl_readout_dist_le), [`MIPRE.Introspection.exists_pauli_mixing`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_pauli_mixing), [`MIPRE.Introspection.exists_pauli_mixing_avg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_pauli_mixing_avg), [`MIPRE.Introspection.exists_pauli_mixing_varying`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_pauli_mixing_varying), [`MIPRE.Introspection.mixing_error_sqrt_bound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.mixing_error_sqrt_bound), [`MIPRE.Introspection.exists_pauli_mixing_sqrt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_pauli_mixing_sqrt).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1495](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1495)
