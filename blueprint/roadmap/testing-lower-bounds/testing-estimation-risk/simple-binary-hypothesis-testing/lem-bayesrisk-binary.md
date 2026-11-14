---
declaration: lemma
origin: cited
lean: ProbabilityTheory.bayesRisk_boolKernel_eq_lintegral_iInf
statement: formalized
proof: formalized
---

# bayesRisk_binary

For $\Theta = \{0,1\}$, the Bayes risk of a prior $\xi \in \mathcal M(\{0,1\})$ is

$$
\begin{aligned}
\mathcal R^P_\xi = (P \circ \xi)\left[x \mapsto \inf_{z \in \mathcal Z} \left( \xi_0\frac{d P(0)}{d(P \circ \xi)}(x)\ell'(y(0), z) + \xi_1\frac{d P(1)}{d(P \circ \xi)}(x)\ell'(y(1), z) \right) \right]
\: .
\end{aligned}
$$

## Depends on

- [Bayes risk](../risk/def-bayesrisk.md)

## Proof depends on

- [bayesInv_binary](lem-bayesinv-binary.md)
- [isBayesEstimator_genBayesEstimator](../risk/thm-isbayesestimator-genbayesestimator.md)

## Proof

Use Theorem [isBayesEstimator_genBayesEstimator](../risk/thm-isbayesestimator-genbayesestimator.md), with the value of $P_\xi^\dagger$ given by Lemma [bayesInv_binary](lem-bayesinv-binary.md).

## Lean

Formalized as [`ProbabilityTheory.bayesRisk_boolKernel_eq_lintegral_iInf`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.bayesRisk_boolKernel_eq_lintegral_iInf).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 545](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L545)
