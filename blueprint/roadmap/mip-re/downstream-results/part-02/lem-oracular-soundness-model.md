---
declaration: lemma
origin: cited
lean: MIPRE.SeededGame.povmValue_sound_ge, MIPRE.StateModel.sum_snorm_sq_ge_of_close, MIPRE.StateModel.sum_snorm_sq_eq_one_of_isPVMIn, MIPRE.BipartiteModel.sum_snorm_sq_chain, MIPRE.SeededGame.oracleView, MIPRE.SeededGame.isPVMIn_oracleJoint, MIPRE.SeededGame.sum_snorm_sq_joint_le, MIPRE.SeededGame.condWin_oracle_le, MIPRE.SeededGame.condWin_sound_ge, MIPRE.SeededGame.sum_condFail_four_le
statement: formalized
proof: formalized
---

# Soundness of oracularization, in a bipartite model

Let $S$ be a seeded game with nonempty seed space and nonempty answer alphabet, let $0 \leq \varepsilon \leq 1$, and let $\{N^q_u\}$ and $\{N'^q_u\}$, one for each question $q$ of the oracularization of $S$, be projective measurements in the first and the second player's algebra of a bipartite model with a unit state, of model value at least $1 - \varepsilon$ in the oracularization of $S$. Then the families in which the first player measures $\{N^{(\textsc{A},\, x)}_a\}$ and the second $\{N'^{(\textsc{B},\, y)}_b\}$, each relabelled so that the oracle-shaped answers are grouped into one fixed answer, have model value at least $1 - 24\sqrt{\varepsilon}$ in the game of $S$.

## Depends on

- [The oracularized game](../../structure-of-the-proof/part-06/def-oracular-game.md)
- [Bipartite model](def-bipartite-model.md)

## Proof

Fix a seed $z$ and write $O$ for the first player's measurement at $(\textsc{O}, z)$, $O^\textsc{A}_u$ and $O^\textsc{B}_v$ for its sums over the answers whose Alice, respectively Bob, component is $u$, respectively $v$, $C$ for the first player's measurement at $(\textsc{A}, L^\textsc{A}(z))$, and $P$, $Q$ for the second player's at $(\textsc{A}, L^\textsc{A}(z))$ and $(\textsc{B}, L^\textsc{B}(z))$. In the model's algebra, $\pi_A(C_u)\pi_B(Q_v) - \pi_A(O^\textsc{A}_u O^\textsc{B}_v) = X_1 + X_2 + X_3$, where

$$
X_1 = \pi_B(Q_v)(\pi_A(C_u) - \pi_B(P_u)), \quad
X_2 = \pi_B(Q_v)(\pi_B(P_u) - \pi_A(O^\textsc{A}_u)), \quad
X_3 = \pi_A(O^\textsc{A}_u)(\pi_B(Q_v) - \pi_A(O^\textsc{B}_v)),
$$

because the two players' operators commute. The front factors are projective measurements, so summed over their outcome they cost nothing, and each of the three deviations is the cross-party inconsistency of one role pair — $(\textsc{A}, \textsc{A})$, $(\textsc{O}, \textsc{A})$, $(\textsc{O}, \textsc{B})$ — at which acceptance forces the two answers compared to agree, so by the estimate of Definition [Cross-party state-dependent distance](../../foundations/part-02/def-cross-distance.md) each is at most twice that pair's conditional failure. So $\delta_z = \sum_{u,v} \|\pi(\pi_A(C_u)\pi_B(Q_v) - \pi_A(O^\textsc{A}_u O^\textsc{B}_v))\psi\|^2$ is at most $6$ times the sum of the three conditional failures. Both $\{\pi_A(C_u)\pi_B(Q_v)\}$ and $\{\pi_A(O^\textsc{A}_u O^\textsc{B}_v)\}$ are projective measurements indexed by pairs, the second because distinct outcomes of $O$ are orthogonal, and on the pairs of isolated answers the input predicate accepts at $(L^\textsc{A}(z), L^\textsc{B}(z))$ the second carries at least the oracle's acceptance probability at $(\textsc{O}, \textsc{O})$. The vector form of Lemma [Close measurements have close values](../../foundations/part-02/lem-close-measurements-close-values.md) then puts the conditional value of the extracted families at the seed at least one minus the conditional failure at $(\textsc{O}, \textsc{O})$ minus $2\sqrt{\delta_z}$. The four role pairs used are distinct and each carries a ninth of the question weight, so their conditional failures average to at most $9\varepsilon$ in total, and with Cauchy–Schwarz taking the average inside the square root the value is at least $1 - 9\varepsilon - 2\sqrt{54\varepsilon} \geq 1 - 24\sqrt\varepsilon$. Nothing here uses a dimension: projectivity is a hypothesis, and in the commuting-operator model it is supplied by Lemma [Strategies in a model, read in ${\omega^{\mathrm{co}}}$](lem-model-strategy-co.md). The matrix analysis of Lemma [Soundness of oracularization, for bipartite strategies](../../structure-of-the-proof/part-06/lem-oracular-soundness-tensor.md) is this one in the tensor-product model.

## Lean

Formalized as [`MIPRE.SeededGame.povmValue_sound_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.povmValue_sound_ge), [`MIPRE.StateModel.sum_snorm_sq_ge_of_close`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.StateModel.sum_snorm_sq_ge_of_close), [`MIPRE.StateModel.sum_snorm_sq_eq_one_of_isPVMIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.StateModel.sum_snorm_sq_eq_one_of_isPVMIn), [`MIPRE.BipartiteModel.sum_snorm_sq_chain`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.sum_snorm_sq_chain), [`MIPRE.SeededGame.oracleView`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.oracleView), [`MIPRE.SeededGame.isPVMIn_oracleJoint`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.isPVMIn_oracleJoint), [`MIPRE.SeededGame.sum_snorm_sq_joint_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.sum_snorm_sq_joint_le), [`MIPRE.SeededGame.condWin_oracle_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.condWin_oracle_le), [`MIPRE.SeededGame.condWin_sound_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.condWin_sound_ge), [`MIPRE.SeededGame.sum_condFail_four_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.sum_condFail_four_le).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1427](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1427)
