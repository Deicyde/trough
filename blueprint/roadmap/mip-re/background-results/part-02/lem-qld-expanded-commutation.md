---
declaration: lemma
origin: cited
lean: MIPRE.QLD.Anc, MIPRE.QLD.weylOf, MIPRE.QLD.ancVec, MIPRE.QLD.gam_eq_trDot, MIPRE.QLD.weylOf_isUnitary, MIPRE.QLD.weylOf_prod_isUnitary, MIPRE.QLD.hatObs, MIPRE.QLD.norm_evec_epr, MIPRE.QLD.hatVec_unit, MIPRE.QLD.hatObs_comm_eq, MIPRE.QLD.norm_hatVec_hatObs_comm, MIPRE.QLD.hatObs_commutation
statement: formalized
proof: formalized
---

# Expanded point observables commute

Let $|\hat\psi\rangle = |\psi\rangle \otimes |\textsc{EPR}_q\rangle^{\otimes M}$ with the ancilla halves split between the two parties, and let $\widehat{W}^{r}(u) = W^{r}(u) \otimes \tau^W(r \cdot {\mathrm{ind}}_m(u))$. If the first player's measurements are projective then, on average over the verifier's content and with *no sign*,

$$
\sum_\omega \frac{1}{\left\vert {{\mathcal{C}}} \right\vert}
\left\| {\bigl[ \widehat{X}^{r_X}(u_X),\, \widehat{Z}^{r_Z}(u_Z) \bigr]
\otimes {I} |\hat\psi\rangle} \right\|^2 \;\leq\; 57676416\, \varepsilon\;.
$$

The Lean proves it for a strategy in any bipartite model, $|\hat\psi\rangle$ being the state of its register model on $\mathbb{F}_q^M$ (Definition [The register model](../../downstream-results/part-03/def-register-model.md)); the statement above is its tensor-product instance.

## Depends on

- [Signed commutation of the point observables](lem-qld-obs-commutation.md)
- [Generalized Pauli observables in characteristic two](../../foundations/part-02/def-generalized-pauli.md)
- [The maximally entangled state of the Weyl system](../../foundations/part-02/def-weyl-epr.md)
- [The expanded state, and an inert ancilla](../../foundations/part-02/def-expanded-state.md)

## Proof depends on

- [The ancilla extension](../../downstream-results/part-02/lem-ancilla-extension.md)

## Proof

One identity and two bookkeeping facts. The identity is

$$
\bigl[ \widehat{X}^{r_X}(u_X),\, \widehat{Z}^{r_Z}(u_Z) \bigr]
\;=\; \Bigl( X^{r_X}(u_X) Z^{r_Z}(u_Z) - (-1)^{\gamma(\omega)} Z^{r_Z}(u_Z) X^{r_X}(u_X) \Bigr)
\otimes \Bigl( \tau^X(r_X \cdot {\mathrm{ind}}_m(u_X))\, \tau^Z(r_Z \cdot {\mathrm{ind}}_m(u_Z)) \Bigr)\;,
$$

because the two ancilla operators commute up to *exactly* the sign $(-1)^{\gamma(\omega)}$ — the twisted commutation relation of Definition [Generalized Pauli observables in characteristic two](../../foundations/part-02/def-generalized-pauli.md), whose sign is the form $\operatorname{tr}\bigl( (r_X {\mathrm{ind}}_m(u_X)) \cdot (r_Z {\mathrm{ind}}_m(u_Z)) \bigr)$, and that form *is* $\gamma(\omega)$ (`gam_eq_trDot`). Then the surviving ancilla operator is unitary, hence invisible to the state-norm, and what is left has an inert ancilla, hence the same norm on $|\hat\psi\rangle$ as on $|\psi\rangle$ (Definition [The expanded state, and an inert ancilla](../../foundations/part-02/def-expanded-state.md), items 3 and 4). So the bound is exactly Lemma [Signed commutation of the point observables](lem-qld-obs-commutation.md)'s, with the sign removed.

## Lean

Formalized as [`MIPRE.QLD.Anc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Anc), [`MIPRE.QLD.weylOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.weylOf), [`MIPRE.QLD.ancVec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.ancVec), [`MIPRE.QLD.gam_eq_trDot`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.gam_eq_trDot), [`MIPRE.QLD.weylOf_isUnitary`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.weylOf_isUnitary), [`MIPRE.QLD.weylOf_prod_isUnitary`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.weylOf_prod_isUnitary), [`MIPRE.QLD.hatObs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.hatObs), [`MIPRE.QLD.norm_evec_epr`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.norm_evec_epr), [`MIPRE.QLD.hatVec_unit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.hatVec_unit), [`MIPRE.QLD.hatObs_comm_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.hatObs_comm_eq), [`MIPRE.QLD.norm_hatVec_hatObs_comm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.norm_hatVec_hatObs_comm), [`MIPRE.QLD.hatObs_commutation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.hatObs_commutation).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 2578](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L2578)
