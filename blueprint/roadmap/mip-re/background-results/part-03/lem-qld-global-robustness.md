---
declaration: lemma
origin: cited
lean: MIPRE.QLD.deltaProd, MIPRE.QLD.deltaSep, MIPRE.QLD.deltaS, MIPRE.QLD.GlobalPair.one_sub_two_eta_ge, MIPRE.QLD.GlobalPair.sum_not_isGood_mass_A_le', MIPRE.QLD.GlobalPair.sum_not_isGood_mass_B_le', MIPRE.QLD.liftPt, MIPRE.QLD.liftPt_mats, MIPRE.QLD.GlobalPair.inconsistency_evalMarg_A_le, MIPRE.QLD.GlobalPair.inconsistency_evalMarg_B_le
statement: formalized
proof: formalized
---

# Global robustness in both register versions

Collect the three errors of stage 4b–4c as explicit functions of the error $\delta$ of Lemma [A global padded polynomial PVM](lem-qld-global-pvm.md) and the failure $\varepsilon$ of the strategy: $\Delta = 2\delta + 2 \cdot 57676416\,\varepsilon$ is the ordered-products bound, $\delta_G = 8\Delta$ the weight of the outcomes that are not of the separated form, and $\delta_S = 2\sqrt{\Delta} + 2/q + \delta_G$ the marginal error. The bound $\delta_G = 8\Delta$ holds under $48md \leq q$, where the factor $1 - 2\eta$ of Lemma [Separating the two point variables](lem-qld-global-separate.md) is at least $1/2$. Both register versions are obtained by running the same estimates in the model with the players exchanged; no symmetry of the strategy is assumed. The marginal consistencies hold in the model of the global measurements, against the expanded point measurements carried there by the embedding of the register model, which is the form Lemma [The simultaneous global measurement](lem-qld-simultaneous.md) states them in, so no register is moved. The Lean proves it for a `GlobalPair` in any model into which the register model embeds; the statement above is its tensor-product instance.

## Depends on

- [Sandwich estimates and the two marginals](lem-qld-global-sandwich.md)
- [Separating the two point variables](lem-qld-global-separate.md)
- [Admissible padded setup](lem-qld-global-setup.md)

## Proof

For the arithmetic: $2 + 2d + 8md \leq 12md$ for $m, d \geq 1$, so $48md \leq q$ gives $\eta = (2 + 2d + 8md)/q \leq 1/4$ and $1 - 2\eta \geq 1/2$; since the weight is nonnegative, Lemma [Separating the two point variables](lem-qld-global-separate.md) then reads $\delta_G \leq 8\Delta$. The expanded point measurements enter carried along the embedding (`liftPt`), whose Born probabilities are their expanded-state ones. Bob's versions are Alice's applied in the model with the players exchanged, which the inconsistency and the Born rule exchange.

## Lean

Formalized as [`MIPRE.QLD.deltaProd`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.deltaProd), [`MIPRE.QLD.deltaSep`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.deltaSep), [`MIPRE.QLD.deltaS`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.deltaS), [`MIPRE.QLD.GlobalPair.one_sub_two_eta_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.GlobalPair.one_sub_two_eta_ge), [`MIPRE.QLD.GlobalPair.sum_not_isGood_mass_A_le'`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.GlobalPair.sum_not_isGood_mass_A_le'), [`MIPRE.QLD.GlobalPair.sum_not_isGood_mass_B_le'`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.GlobalPair.sum_not_isGood_mass_B_le'), [`MIPRE.QLD.liftPt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.liftPt), [`MIPRE.QLD.liftPt_mats`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.liftPt_mats), [`MIPRE.QLD.GlobalPair.inconsistency_evalMarg_A_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.GlobalPair.inconsistency_evalMarg_A_le), [`MIPRE.QLD.GlobalPair.inconsistency_evalMarg_B_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.GlobalPair.inconsistency_evalMarg_B_le).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 4494](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L4494)
