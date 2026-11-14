---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.registerPOVM, MIPRE.Introspection.registerOp_isPVM, MIPRE.Introspection.stateSqNorm_registerOp, MIPRE.Introspection.registerEPR_norm, MIPRE.Introspection.registerState_split, MIPRE.Introspection.stateSqNorm_registerExtend, MIPRE.Introspection.exists_register_mixing_sqrt, MIPRE.Introspection.coordinateSplit, MIPRE.Introspection.coordinateLinear_restrict, MIPRE.Introspection.coordinateInsert_linear, MIPRE.Introspection.exists_ambient_pauli_mixing
statement: formalized
proof: formalized
---

# Pauli mixing with a retained classical fibre

Let $U_x\subseteq V_x\subseteq V$ be coordinate registers, $L_x:U_x\to U_x$ linear, and the state be $\mathrm{EPR}_V\otimes\mathrm{aux}$. Let $M^x_{y,a}$ be a PVM on Alice's $V_x$ register and auxiliary space. Assume its $y$ marginal is $O(\varepsilon)$-close to $P_y^Z(L_x)$ in the averaged squared state norm, and that its commutators with the fine $Z$ projectors on $U_x$ and coarse $X$ fibre projectors for a map with kernel $(\ker L_x)^\perp$ have total outcome-summed squared norm $O(\varepsilon)$. For $0\leq\varepsilon\leq1$ there are POVMs $N_a^{x,y}$ on the complementary register outside $U_x$ in $V_x$ and Alice auxiliary space with

$$
\mathbb E_x\sum_{y,a}
\|((M^x_{y,a}-P_y^Z\otimes N_a^{x,y})\otimes{I})\psi\|^2
\leq C\sqrt\varepsilon
$$

for a universal $C$ (once the hypothesis constants are fixed). The sums in the commutator hypotheses include both projector and measurement outcomes. Empty fibres allow any $N$; their left-hand mass is controlled by consistency, not identically zero.

## Depends on

- [Linear-map blocks of the twirl](lem-pauli-linear-mixing.md)
- [Commutator Parseval identity](lem-pauli-commutator-transfer.md)
- [Approximate commutation controls unitary mixing](lem-pauli-unitary-mixing.md)
- [Combining two approximate commutations](lem-pauli-two-sided-commutation.md)
- [Completing a nearby submeasurement](lem-close-submeasurement.md)
- [Retained-fibre mixing in coordinate presentations](lem-pauli-mixing-coordinates.md)

## Proof depends on

- [Conditioning on part of a question](lem-conditional-measurement.md)
- [Local isometries carry the Born rule](../../downstream-results/part-03/lem-local-isometry.md)

## Proof

Split the actual finite coordinate registers by explicit basis equivalences. The ambient EPR state factors exactly, and adjoining or removing the untouched complement preserves every squared state norm. Pull back the local operators, apply Lemma [Retained-fibre mixing in coordinate presentations](lem-pauli-mixing-coordinates.md), and transport its actual POVMs back to the residual register. With each hypothesis bounded by $\varepsilon$, the conclusion has the explicit constant $56$.

The source's route: twirl to blocks $B^z_{y,a}$, retain the matching blocks $B^y_{y,a}$ using projectivity and EPR consistency, then complete with $N_a^{x,y}=\sum_z B^y_{z,a}$. Lemma [Completing a nearby submeasurement](lem-close-submeasurement.md) accounts for the square-root loss. Transfers across EPR use matrix transpose, in particular $X(v)^T=X(-v)$; no odd-characteristic identity $X(v)^T=X(v)$ is presumed.

## Lean

Formalized as [`MIPRE.Introspection.registerPOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.registerPOVM), [`MIPRE.Introspection.registerOp_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.registerOp_isPVM), [`MIPRE.Introspection.stateSqNorm_registerOp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.stateSqNorm_registerOp), [`MIPRE.Introspection.registerEPR_norm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.registerEPR_norm), [`MIPRE.Introspection.registerState_split`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.registerState_split), [`MIPRE.Introspection.stateSqNorm_registerExtend`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.stateSqNorm_registerExtend), [`MIPRE.Introspection.exists_register_mixing_sqrt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_register_mixing_sqrt), [`MIPRE.Introspection.coordinateSplit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.coordinateSplit), [`MIPRE.Introspection.coordinateLinear_restrict`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.coordinateLinear_restrict), [`MIPRE.Introspection.coordinateInsert_linear`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.coordinateInsert_linear), [`MIPRE.Introspection.exists_ambient_pauli_mixing`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_ambient_pauli_mixing).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1542](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1542)
