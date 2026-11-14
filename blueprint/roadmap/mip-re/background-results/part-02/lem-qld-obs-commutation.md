---
declaration: lemma
origin: cited
lean: MIPRE.QLD.signed_commutation
statement: formalized
proof: formalized
---

# Signed commutation of the point observables

Under the hypotheses of Lemma [Win implications](lem-qld-win.md), with the first player's measurements projective, on average over uniformly random $\omega = (u_X, u_Z, r_X, r_Z)$,

$$
X^{r_X}(u_X)\, Z^{r_Z}(u_Z) \otimes {I}_\textsc{B}
\;\approx_{57676416\,\varepsilon}\;
(-1)^{\gamma(\omega)}\; Z^{r_Z}(u_Z)\, X^{r_X}(u_X) \otimes {I}_\textsc{B}\;.\qquad\text{(1)}
$$

The Lean proves it for a strategy in any bipartite model (Definition [Bipartite model](../../downstream-results/part-02/def-bipartite-model.md)), the first player's measurements projective; the statement above is its tensor-product instance.

## Depends on

- [Win implications](lem-qld-win.md)
- [Anticommuting question tuples](fact-omega-anticomm-prob.md)
- [Signed commutation, the anticommuting case](lem-qld-obs-commutation-acomm.md)

## Proof depends on

- [Signed commutation, the commuting case](lem-qld-obs-commutation-comm.md)

## Proof

Two cases, and the sign is the branch. The content distribution is uniform and the two cases partition it, so the statement is the sum of the two restricted ones: Lemma [Signed commutation, the commuting case](lem-qld-obs-commutation-comm.md) at $9519168\,\varepsilon$ and Lemma [Signed commutation, the anticommuting case](lem-qld-obs-commutation-acomm.md) at $48157248\,\varepsilon$.

## Lean

Formalized as [`MIPRE.QLD.signed_commutation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.signed_commutation).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 2326](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L2326)
