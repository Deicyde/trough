---
declaration: lemma
origin: cited
lean: MIPRE.stateSqNorm_eq_bornProb_one, MIPRE.normSq_stateVecB_eq_one_bornProb, MIPRE.QLD.SimulPair.stateSqNorm_aOp, MIPRE.QLD.SimulPair.normSq_stateVecB_aOp, MIPRE.QLD.SimulPair.xSqNorm_aOp, MIPRE.aOp_mul_one_sub_eq, MIPRE.snorm_aOp_mul_one_sub_le, MIPRE.snorm_sq_aOp_mul_one_sub_le, MIPRE.QLD.sum_bornProb_diag_eq, MIPRE.QLD.sum_content_pt, MIPRE.QLD.sum_uniform_xSqNorm_hatMats_le, MIPRE.QLD.SimulPair.hatMats_conjTranspose, MIPRE.QLD.SimulPair.sum_bornProb_evalMarg_ge, MIPRE.QLD.SimulPair.sum_xSqNorm_evalMarg_le, MIPRE.QLD.SimulPair.sum_xSqNorm_hat_le, MIPRE.QLD.SimulPair.sum_snorm_sq_evalMarg_one_sub_le
statement: formalized
proof: formalized
---

# The marginals track the point measurements

Let $(S_A, S_B)$ be a simultaneous pair measurement of error $\delta_S$ (Lemma [The simultaneous global measurement](lem-qld-simultaneous.md)) for a strategy of failure $\varepsilon$, in a model with state $\Phi$ into which the register model embeds. For $W \in \{X, Z\}$ and on average over a uniform $u \in \mathbb{F}_q^m$, with $\widehat S^W_a$ the evaluated $W$ marginal,

$$
1 - \mathbb E_u \sum_a \bigl\langle \widehat{S}^W_a \otimes
\widehat{M}^{(\mathtt{Point}, W), u}_{a} \bigr\rangle_\Phi \leq \delta_S ,
$$

the opposite party's measurement being the one on the right, and

$$
\mathbb E_u \sum_a \bigl\| \bigl( \widehat{S}^W_a
( {I} - \widehat{M}^{(\mathtt{Point}, W), u}_{a} ) \otimes {I} \bigr) \Phi \bigr\|^2
\leq 4 \delta_S + 344\,\varepsilon ,
$$

in which *both* factors sit on the same party, the point measurements being carried to that model by the embedding. All symmetric equivalents hold. The Lean proves it for a `SimulPair` of a projective strategy in any bipartite model; the statement above is its tensor-product instance.

## Depends on

- [The simultaneous global measurement](lem-qld-simultaneous.md)
- [State-dependent POVM distance](../../foundations/part-02/def-state-distance.md)
- [Inconsistency](../../foundations/part-02/def-inconsistency.md)

## Proof

The first display is the consistency of Lemma [The simultaneous global measurement](lem-qld-simultaneous.md) read as an agreement: for two POVMs with the same outcomes on a unit state, the inconsistency is one minus the probability that they agree.

For the second, write $T = \widehat S^W_a$ and $A = \widehat M^{(\mathtt{Point}, W), u}_a$ on Alice's register and $B$ for the same point measurement on Bob's; all three are projections, $T$ because the marginal of a projective measurement is projective, $A$ and $B$ because the expanded point measurements are. Since operators on opposite parties commute and $B^2 = B$,

$$
(T \otimes {I})({I} - A \otimes {I})
= ({I} - {I} \otimes B)\,(T \otimes {I} - {I} \otimes B) - (T \otimes {I})(A \otimes {I} - {I} \otimes B) ,
$$

an identity whose two right-hand factors in front, ${I} - {I} \otimes B$ and $T \otimes {I}$, are contractions. So the same-party deviation is at most the sum of two cross-party ones: the first is the deviation of the marginal from the opposite party's point measurement, which the first display bounds by $2\delta_S$ after summing, and the second is the self-consistency of the expanded point measurements, $172\varepsilon$ by Lemma [Expanded point measurements](../part-02/lem-qld-expanded-points.md). Squaring costs a factor two on each. The self-consistency is stated at the verifier's content and used at a uniform point; the content's $W$ block is uniform, and it transfers to the model of the pair measurement because operators carried along the embedding keep their expanded-state expectations.

## Lean

Formalized as [`MIPRE.stateSqNorm_eq_bornProb_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.stateSqNorm_eq_bornProb_one), [`MIPRE.normSq_stateVecB_eq_one_bornProb`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.normSq_stateVecB_eq_one_bornProb), [`MIPRE.QLD.SimulPair.stateSqNorm_aOp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.SimulPair.stateSqNorm_aOp), [`MIPRE.QLD.SimulPair.normSq_stateVecB_aOp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.SimulPair.normSq_stateVecB_aOp), [`MIPRE.QLD.SimulPair.xSqNorm_aOp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.SimulPair.xSqNorm_aOp), [`MIPRE.aOp_mul_one_sub_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.aOp_mul_one_sub_eq), [`MIPRE.snorm_aOp_mul_one_sub_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.snorm_aOp_mul_one_sub_le), [`MIPRE.snorm_sq_aOp_mul_one_sub_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.snorm_sq_aOp_mul_one_sub_le), [`MIPRE.QLD.sum_bornProb_diag_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.sum_bornProb_diag_eq), [`MIPRE.QLD.sum_content_pt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.sum_content_pt), [`MIPRE.QLD.sum_uniform_xSqNorm_hatMats_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.sum_uniform_xSqNorm_hatMats_le), [`MIPRE.QLD.SimulPair.hatMats_conjTranspose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.SimulPair.hatMats_conjTranspose), [`MIPRE.QLD.SimulPair.sum_bornProb_evalMarg_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.SimulPair.sum_bornProb_evalMarg_ge), [`MIPRE.QLD.SimulPair.sum_xSqNorm_evalMarg_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.SimulPair.sum_xSqNorm_evalMarg_le), [`MIPRE.QLD.SimulPair.sum_xSqNorm_hat_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.SimulPair.sum_xSqNorm_hat_le), [`MIPRE.QLD.SimulPair.sum_snorm_sq_evalMarg_one_sub_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.SimulPair.sum_snorm_sq_evalMarg_one_sub_le).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 4533](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L4533)
