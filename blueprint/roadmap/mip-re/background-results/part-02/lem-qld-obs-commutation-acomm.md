---
declaration: lemma
origin: cited
lean: MIPRE.QLD.ptObs, MIPRE.QLD.varObs, MIPRE.QLD.ptObs_mul_self_le_one, MIPRE.QLD.varObs_mul_self_le_one, MIPRE.QLD.acommWeight, MIPRE.QLD.acommWeight_nonneg, MIPRE.QLD.sum_acommWeight_mul, MIPRE.QLD.xStateDist_ptObs_varObs_X, MIPRE.QLD.xStateDist_ptObs_varObs_Z, MIPRE.QLD.question_var, MIPRE.QLD.mats_msPOVM_var, MIPRE.QLD.bobs_msPOVM, MIPRE.QLD.anti_eq_varObs, MIPRE.QLD.sq_norm_ptObs_anticomm_le, MIPRE.QLD.acomm_signed_commutation
statement: formalized
proof: formalized
---

# Signed commutation, the anticommuting case

Under the hypotheses of Lemma [Win implications](lem-qld-win.md), with the first player's measurements projective, summed over the *anticommuting* tuples with the uniform weight $\left\vert {{\mathcal{C}}} \right\vert^{-1}$ on the verifier's content,

$$
\sum_{\omega \,:\, \gamma(\omega) = 1} \frac{1}{\left\vert {{\mathcal{C}}} \right\vert}
\left\| {\bigl( X^{r_X}(u_X)\, Z^{r_Z}(u_Z) + Z^{r_Z}(u_Z)\, X^{r_X}(u_X) \bigr) \otimes {I}_\textsc{B}
|\psi\rangle} \right\|^2
\;\leq\; 16049664\, \varepsilon + 8256\, \varepsilon \;=\; 48157248\, \varepsilon\;,
$$

which is Lemma [Signed commutation of the point observables](lem-qld-obs-commutation.md) at $(-1)^{\gamma(\omega)} = -1$.

## Depends on

- [Win implications](lem-qld-win.md)
- [Anticommuting question tuples](fact-omega-anticomm-prob.md)

## Proof

Item 7 of Lemma [Win implications](lem-qld-win.md) says that on an anticommuting tuple each point probe agrees with one of the two distinguished $\mathtt{Variable}$ bits on the other side. At the level of observables that is $X^{r_X}(u_X) \otimes {I} \simeq_{344\varepsilon} {I} \otimes V_1$ and $Z^{r_Z}(u_Z) \otimes {I} \simeq_{344\varepsilon} {I} \otimes V_5$ — item 7 at the two-outcome probe, then `xStateDist_obsOf_le`, whose cost is the number of outcomes of the probe, two. Item 6 says $V_1$ and $V_5$ anticommute on the state at $16049664\,\varepsilon$. Feed the three into [(3)](../../foundations/part-02/README.md) and square with $(a+b+c)^2 \leq 3(a^2+b^2+c^2)$: the constant is $12 \cdot 344 + 12 \cdot 344 + 3 \cdot 16049664$.

Two bookkeeping points. The weight is uniform on all contents but supported on the anticommuting ones, which is how every item of Lemma [Win implications](lem-qld-win.md) is stated, so it is a sub-probability and not a distribution; `sum_acommWeight_mul` is the one lemma that converts between the two forms. And item 6 is stated for the anticommutator of the *conditional Magic Square strategy*'s observables, which are the same operators as the $\mathtt{Variable}$ observables here: the conditional strategy at a $\mathtt{Variable}$ question is the Pauli test's measurement at the corresponding question with its answer relabelled to the bit it reports, and relabelling along the injection $\mathtt{Sum.inr}$ leaves a coarse-grained POVM element alone (`bobs_msPOVM`).

## Lean

Formalized as [`MIPRE.QLD.ptObs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.ptObs), [`MIPRE.QLD.varObs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.varObs), [`MIPRE.QLD.ptObs_mul_self_le_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.ptObs_mul_self_le_one), [`MIPRE.QLD.varObs_mul_self_le_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.varObs_mul_self_le_one), [`MIPRE.QLD.acommWeight`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.acommWeight), [`MIPRE.QLD.acommWeight_nonneg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.acommWeight_nonneg), [`MIPRE.QLD.sum_acommWeight_mul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.sum_acommWeight_mul), [`MIPRE.QLD.xStateDist_ptObs_varObs_X`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.xStateDist_ptObs_varObs_X), [`MIPRE.QLD.xStateDist_ptObs_varObs_Z`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.xStateDist_ptObs_varObs_Z), [`MIPRE.QLD.question_var`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.question_var), [`MIPRE.QLD.mats_msPOVM_var`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.mats_msPOVM_var), [`MIPRE.QLD.bobs_msPOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.bobs_msPOVM), [`MIPRE.QLD.anti_eq_varObs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.anti_eq_varObs), [`MIPRE.QLD.sq_norm_ptObs_anticomm_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.sq_norm_ptObs_anticomm_le), [`MIPRE.QLD.acomm_signed_commutation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.acomm_signed_commutation).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 2429](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L2429)
