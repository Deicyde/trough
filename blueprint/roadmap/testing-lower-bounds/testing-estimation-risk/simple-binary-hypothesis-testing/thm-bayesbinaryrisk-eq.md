---
declaration: theorem
origin: cited
lean: ProbabilityTheory.bayesBinaryRisk_eq_lintegral_min, ProbabilityTheory.toReal_bayesBinaryRisk_eq_integral_min
statement: formalized
proof: formalized
---

# bayesBinaryRisk_eq

The Bayes risk of simple binary hypothesis testing for prior $\xi \in \mathcal M(\{0,1\})$ is

$$
\begin{aligned}
\mathcal B_\xi(\mu, \nu) = (P \circ \xi)\left[x \mapsto \min \left\{\xi_0\frac{d \mu}{d(P \circ \xi)}(x), \xi_1\frac{d \nu}{d(P \circ \xi)}(x)\right\}\right]
\: .
\end{aligned}
$$

## Depends on

- [bayesBinaryRisk](def-bayesbinaryrisk.md)

## Proof depends on

- [bayesianRisk_genBayesEstimator](../risk/lem-bayesianrisk-genbayesestimator.md)
- [isBayesEstimator_genBayesEstimator](../risk/thm-isbayesestimator-genbayesestimator.md)
- [bayesInv_binary](lem-bayesinv-binary.md)

## Proof

By Theorem [isBayesEstimator_genBayesEstimator](../risk/thm-isbayesestimator-genbayesestimator.md), the generalized Bayes estimator is a Bayes estimator, hence it suffices to compute its Bayesian risk. By Lemma [bayesianRisk_genBayesEstimator](../risk/lem-bayesianrisk-genbayesestimator.md),

$$
\begin{aligned}
R_\xi(\hat{y}_B)
&= (P \circ \xi)\left[x \mapsto \inf_{z \in \mathcal Z} P_\xi^\dagger(x) \left[\theta \mapsto \ell'(y(\theta), z)\right]\right]
\\
&= (P \circ \xi)\left[x \mapsto \min \left\{P_\xi^\dagger(x)(\{0\}), P_\xi^\dagger(x)(\{1\})\right\}\right]
\\
&= (P \circ \xi)\left[x \mapsto \min \left\{\xi_0\frac{d \mu}{d(P \circ \xi)}(x), \xi_1\frac{d \nu}{d(P \circ \xi)}(x)\right\}\right]
\: .
\end{aligned}
$$

The last line is obtained by replacing $P_\xi^\dagger$ by its value (Lemma [bayesInv_binary](lem-bayesinv-binary.md)).

## Lean

Formalized as [`ProbabilityTheory.bayesBinaryRisk_eq_lintegral_min`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.bayesBinaryRisk_eq_lintegral_min), [`ProbabilityTheory.toReal_bayesBinaryRisk_eq_integral_min`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.toReal_bayesBinaryRisk_eq_integral_min).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 749](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L749)
