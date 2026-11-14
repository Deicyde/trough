---
declaration: lemma
origin: cited
lean: ProbabilityTheory.IsSquareIntegrable.integral_iSup_norm_rpow_rpow_inv_le_limitProcess
statement: formalized
proof: formalized
---

# IsSquareIntegrable.integral_iSup_norm_rpow_rpow_inv_le_limitProcess

If $M$ is a square integrable random variable, then

$$
\left(\int (\sup_t \|X_t(\omega)\|)^2\right)^{1/2} \mathrm d\omega \le 2 \|X_\infty\|_2.
$$

## Depends on

- [Square integrable martingales](def-issquareintegrable.md)
- [limitProcess](../../../filtrations-processes-and-martingales/martingale-convergence/def-limitprocess.md)

## Proof depends on

- [doob_lp_norm_top](../../../filtrations-processes-and-martingales/doobs-lp-inequality/cor-doob-lp-norm-top.md)
- [IsSquareIntegrable.sup_eLpNorm_eq_eLpNorm_limitProcess](lem-issquareintegrable-sup-elpnorm-eq-elpnorm-li.md)

## Proof

Combine Corollary [doob_lp_norm_top](../../../filtrations-processes-and-martingales/doobs-lp-inequality/cor-doob-lp-norm-top.md), the fact that suprema commute with power, and Lemma [IsSquareIntegrable.sup_eLpNorm_eq_eLpNorm_limitProcess](lem-issquareintegrable-sup-elpnorm-eq-elpnorm-li.md).

## Lean

Formalized as [`ProbabilityTheory.IsSquareIntegrable.integral_iSup_norm_rpow_rpow_inv_le_limitProcess`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsSquareIntegrable.integral_iSup_norm_rpow_rpow_inv_le_limitProcess).

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 407](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L407)
