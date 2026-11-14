---
declaration: lemma
origin: cited
lean: ProbabilityTheory.bayesBinaryRisk_eq_iInf_measurableSet
statement: formalized
proof: formalized
---

# bayesBinaryRisk_eq_event

$$
\begin{aligned}
\mathcal B_\xi(\mu, \nu) = \inf_{E \text{ event}} \left( \xi_0 \mu(E) + \xi_1 \nu(E^c) \right) \: .
\end{aligned}
$$

## Depends on

- [Bayes risk](../risk/def-bayesrisk.md)

## Proof depends on

- [genBayesEstimator_bayesBinaryRisk](lem-genbayesestimator-bayesbinaryrisk.md)

## Proof

By definition,

$$
\begin{aligned}
\mathcal B_\xi(\mu, \nu)
= \inf_{\hat{y} : \mathcal X \rightsquigarrow \{0,1\}}\left(\xi_0 (\hat{y} \circ \mu)(\{1\}) + \xi_1 (\hat{y} \circ \nu)(\{0\})\right)
\: .
\end{aligned}
$$

If we restrict the infimum to deterministic kernels corresponding to functions of the form $x \mapsto \mathbb{I}\{x \in E\}$, we get that $\mathcal B_\xi(\mu, \nu)$ is bounded from above by the expression for which we want to show equality.

Since the Bayes estimator has that shape (Lemma [genBayesEstimator_bayesBinaryRisk](lem-genbayesestimator-bayesbinaryrisk.md)), $\mathcal B_\xi(\mu, \nu)$ is also greater than the infimum and we have equality.

## Lean

Formalized as [`ProbabilityTheory.bayesBinaryRisk_eq_iInf_measurableSet`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.bayesBinaryRisk_eq_iInf_measurableSet).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 725](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L725)
