---
declaration: lemma
origin: cited
lean: MIPRE.QLD.pts_obs_consistency
statement: formalized
proof: formalized
---

# Consistency of the point observables

For $W \in \{X, Z\}$ and $r \in \mathbb{F}_q$ write $W^r(u) = M^{(\mathtt{Point}, W), u}_{[\operatorname{tr}(\cdot\, r) = 0]} - M^{(\mathtt{Point}, W), u}_{[\operatorname{tr}(\cdot\, r) = 1]}$ for the $\pm 1$-observable of the probe. Under the hypotheses of Lemma [Win implications](lem-qld-win.md), on average over the verifier's content,

$$
W^r(u) \otimes {I}_\textsc{B} \;\approx_{344\varepsilon}\; {I}_\textsc{A} \otimes W^r(u)\;.
$$

As Lemma [Win implications](lem-qld-win.md), the Lean proves it for a strategy in any bipartite model, with no projectivity.

## Depends on

- [Win implications](lem-qld-win.md)

## Proof

Item 1 of Lemma [Win implications](lem-qld-win.md) holds for any *common* reading of the two answers, the rule at equal types accepting only when the answers are equal and equal answers having equal readings — so the data-processing step the paper cites separately is already in the item. Take the reading to be the probe $a \mapsto \operatorname{tr}(a\,r)$ and apply `xStateDist_obsOf_le`, the cross-party form of Lemma [From POVM elements to generalized observables](lem-qld-povm-to-obs.md), with the two signs $\pm 1$: the factor is the number of outcomes of the probe, which is two, giving $2 \cdot 172\varepsilon$.

## Lean

Formalized as [`MIPRE.QLD.pts_obs_consistency`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.pts_obs_consistency).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 2295](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L2295)
