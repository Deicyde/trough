---
declaration: definition
origin: cited
lean: MIPRE.Weyl.eprScale, MIPRE.Weyl.epr, MIPRE.Weyl.epr_same, MIPRE.Weyl.epr_ne, MIPRE.Weyl.eprScale_sq, MIPRE.Weyl.epr_unit, MIPRE.Weyl.stateVec_entry, MIPRE.Weyl.stateVec_epr, MIPRE.Weyl.wX_transpose, MIPRE.Weyl.wZ_transpose, MIPRE.Weyl.stateVec_epr_wX, MIPRE.Weyl.stateVec_epr_wZ, MIPRE.Weyl.stateVec_epr_proj, MIPRE.sgn_sum, MIPRE.Weyl.isPVM_syn, MIPRE.Weyl.stateVec_epr_syn, MIPRE.Weyl.synOf, MIPRE.Weyl.syn_eq_synOf, MIPRE.Weyl.sum_synOf, MIPRE.Weyl.isPVM_synOf, MIPRE.Weyl.stateVec_epr_synOf
statement: formalized
---

# The maximally entangled state of the Weyl system

On two copies of $(\mathbb{C}^q)^{\otimes n}$,

$$
|\textsc{EPR}_q\rangle^{\otimes n} \;=\; \frac{1}{\sqrt{q^n}} \sum_{a \in \mathbb{F}_q^n} |a\rangle \otimes |a\rangle\;,
$$

a unit vector. For any operator $M$ on one copy,

$$
(M \otimes {I}) |\textsc{EPR}_q\rangle^{\otimes n} \;=\; ({I} \otimes M^{\mathsf T}) |\textsc{EPR}_q\rangle^{\otimes n}\;,\qquad\text{(12)}
$$

and the Weyl operators and their spectral projectors are *symmetric*, so for them the transpose is invisible: the two parties' operators act identically on the state.

Both facts about the syndrome projectors $\tau^W_{[\,\cdot\, v = a]}$ — that they are a projective measurement, and that they transport across the state — hold for the coarse-graining of the eigenbasis measurement along a level set of an *arbitrary* label, the syndrome being the case of the label $e \mapsto \langle e, v\rangle$; and coarse-graining such a family again gives the family of the composite label.

## Depends on

- [Generalized Pauli observables in characteristic two](def-generalized-pauli.md)
- [State-dependent POVM distance](def-state-distance.md)

## Lean

Formalized as [`MIPRE.Weyl.eprScale`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.eprScale), [`MIPRE.Weyl.epr`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.epr), [`MIPRE.Weyl.epr_same`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.epr_same), [`MIPRE.Weyl.epr_ne`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.epr_ne), [`MIPRE.Weyl.eprScale_sq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.eprScale_sq), [`MIPRE.Weyl.epr_unit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.epr_unit), [`MIPRE.Weyl.stateVec_entry`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.stateVec_entry), [`MIPRE.Weyl.stateVec_epr`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.stateVec_epr), [`MIPRE.Weyl.wX_transpose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wX_transpose), [`MIPRE.Weyl.wZ_transpose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.wZ_transpose), [`MIPRE.Weyl.stateVec_epr_wX`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.stateVec_epr_wX), [`MIPRE.Weyl.stateVec_epr_wZ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.stateVec_epr_wZ), [`MIPRE.Weyl.stateVec_epr_proj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.stateVec_epr_proj), [`MIPRE.sgn_sum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sgn_sum), [`MIPRE.Weyl.isPVM_syn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.isPVM_syn), [`MIPRE.Weyl.stateVec_epr_syn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.stateVec_epr_syn), [`MIPRE.Weyl.synOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.synOf), [`MIPRE.Weyl.syn_eq_synOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.syn_eq_synOf), [`MIPRE.Weyl.sum_synOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.sum_synOf), [`MIPRE.Weyl.isPVM_synOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.isPVM_synOf), [`MIPRE.Weyl.stateVec_epr_synOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Weyl.stateVec_epr_synOf).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 1112](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L1112)
