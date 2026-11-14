---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.weyl_projectors_isPVM, MIPRE.Introspection.linear_measurement_isPVM, MIPRE.Introspection.joint_measurement_isPVM, MIPRE.Introspection.sampling_hiding_isPVM
statement: formalized
proof: formalized
---

# Projectivity of sampling and hiding readouts

Over a finite characteristic-two field, reading a linear map of either Weyl eigenbasis outcome is a projective measurement. If $\ker(R)^\perp\subseteq\ker(L)$, the joint readout with projectors $\sigma^Z_{[L(\cdot)=a]}\sigma^X_{[R(\cdot)=b]}$ is also projective.

## Depends on

- [Pauli operators against a linear-map measurement](lem-pauli-linear-fourier.md)
- [A commutation criterion for $X$ and $Z$ measurements](lem-pauli-commute-criterion.md)

## Proof depends on

- [The expanded state, and an inert ancilla](../../foundations/part-02/def-expanded-state.md)

## Proof

The Weyl spectral projectors are self-adjoint idempotents summing to identity, and coarse-graining preserves these properties. By Lemma [A commutation criterion for $X$ and $Z$ measurements](lem-pauli-commute-criterion.md), the two coarse-grained families commute. Their products are therefore self-adjoint idempotents; summing over both readouts gives the identity.

## Lean

Formalized as [`MIPRE.Introspection.weyl_projectors_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.weyl_projectors_isPVM), [`MIPRE.Introspection.linear_measurement_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.linear_measurement_isPVM), [`MIPRE.Introspection.joint_measurement_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.joint_measurement_isPVM), [`MIPRE.Introspection.sampling_hiding_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.sampling_hiding_isPVM).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1266](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1266)
