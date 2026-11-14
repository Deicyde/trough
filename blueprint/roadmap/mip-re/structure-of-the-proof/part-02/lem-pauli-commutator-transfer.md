---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.sum_norm_linearFourier_sq, MIPRE.Introspection.linear_measurement_parseval, MIPRE.Introspection.linear_measurement_commutator_parseval, MIPRE.Introspection.linear_measurement_commutator_parseval_avg
statement: formalized
proof: formalized
---

# Commutator Parseval identity

For the fibre projections $P_y^W$ of $L$ and every operator $M$,

$$
\sum_y\|([M,P_y^W]\otimes{I})\psi\|^2
=\mathbb E_{v\in(\ker L)^\perp}
\|([M,\tau^W(v)]\otimes{I})\psi\|^2.
$$

The identity remains true after averaging questions and summing measurement outcomes. It introduces no dimension or alphabet factor.

## Depends on

- [Pauli operators against a linear-map measurement](lem-pauli-linear-fourier.md)
- [State-dependent POVM distance](../../foundations/part-02/def-state-distance.md)
- [Ancilla extension of a bipartite model](../../downstream-results/part-02/def-ancilla-extension.md)

## Proof

Distinct nonempty fibres give orthogonal characters on $(\ker L)^\perp$. Apply Parseval to the complex-linear action that takes a register operator to its amplified commutator applied to the state. Empty fibre projectors vanish. Summing outcomes and averaging questions preserves the identity. The checked field specialization is characteristic two.

## Lean

Formalized as [`MIPRE.Introspection.sum_norm_linearFourier_sq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.sum_norm_linearFourier_sq), [`MIPRE.Introspection.linear_measurement_parseval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.linear_measurement_parseval), [`MIPRE.Introspection.linear_measurement_commutator_parseval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.linear_measurement_commutator_parseval), [`MIPRE.Introspection.linear_measurement_commutator_parseval_avg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.linear_measurement_commutator_parseval_avg).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1378](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1378)
