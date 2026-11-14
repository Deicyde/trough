---
declaration: lemma
origin: cited
lean: MIPRE.QLD.synPOVM, MIPRE.QLD.synPOVM_mats, MIPRE.QLD.weylOf_transpose, MIPRE.QLD.sum_bornProb_epr_synPOVM, MIPRE.QLD.ptValPOVM, MIPRE.QLD.hatPOVM, MIPRE.QLD.sum_xSqNorm_hatPOVM_le, MIPRE.QLD.hatPOVM_consistency
statement: formalized
proof: formalized
---

# Expanded point measurements are self-consistent

With $|\hat\psi\rangle$ as in Lemma [Expanded point observables commute](lem-qld-expanded-commutation.md), let

$$
\widehat{M}^{(\mathtt{Point},W),u}_a
\;=\; \sum_{a' + a'' = a} M^{(\mathtt{Point},W),u}_{a'} \otimes \tau^{W}_{[\,\cdot\, {\mathrm{ind}}_m(u) = a'']}
$$

be the convolution of the strategy's point measurement with the ancilla's syndrome measurement. Then, on average over the verifier's content,

$$
\widehat{M}^{(\mathtt{Point},W),u}_a \otimes {I} \;\simeq_{172\varepsilon}\;
{I} \otimes \widehat{M}^{(\mathtt{Point},W),u}_a\;.
$$

The Lean proves it for a strategy in any bipartite model, with no projectivity, on its register model (Definition [The register model](../../downstream-results/part-03/def-register-model.md)); the statement above is its tensor-product instance.

## Depends on

- [Win implications](lem-qld-win.md)
- [Generalized Pauli observables in characteristic two](../../foundations/part-02/def-generalized-pauli.md)
- [The maximally entangled state of the Weyl system](../../foundations/part-02/def-weyl-epr.md)
- [The expanded state, and an inert ancilla](../../foundations/part-02/def-expanded-state.md)
- [The order of a matrix algebra over an ordered $*$-ring](../../downstream-results/part-03/def-block-order.md)

## Proof depends on

- [Cross-party state-dependent distance](../../foundations/part-02/def-cross-distance.md)
- [The ancilla extension](../../downstream-results/part-02/lem-ancilla-extension.md)

## Proof

Three inputs and no loss. The agreement probability of a product measurement on the expanded state factorizes (Definition [The expanded state, and an inert ancilla](../../foundations/part-02/def-expanded-state.md)); the ancilla factor is *exactly one*, because the syndrome projectors are perfectly self-consistent across the two halves of $|\textsc{EPR}_q\rangle^{\otimes M}$ — that is Definition [The maximally entangled state of the Weyl system](../../foundations/part-02/def-weyl-epr.md)'s stabilizer relation, summed over the level set, and it is $1$ rather than $1 - O(\varepsilon)$; and the convolution is a coarse-graining, so it can only *increase* agreement. What is left is the disagreement of the strategy's own point measurements, which item 1 of Lemma [Win implications](lem-qld-win.md) bounds by the conditional failure of the $(\mathtt{Point}, W)$ subtest. One conversion from agreement to distance ([(1)](../../foundations/part-02/def-cross-distance.md)) gives $2 \cdot 86 \varepsilon$.

## Lean

Formalized as [`MIPRE.QLD.synPOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.synPOVM), [`MIPRE.QLD.synPOVM_mats`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.synPOVM_mats), [`MIPRE.QLD.weylOf_transpose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.weylOf_transpose), [`MIPRE.QLD.sum_bornProb_epr_synPOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.sum_bornProb_epr_synPOVM), [`MIPRE.QLD.ptValPOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.ptValPOVM), [`MIPRE.QLD.hatPOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.hatPOVM), [`MIPRE.QLD.sum_xSqNorm_hatPOVM_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.sum_xSqNorm_hatPOVM_le), [`MIPRE.QLD.hatPOVM_consistency`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.hatPOVM_consistency).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 2535](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L2535)
