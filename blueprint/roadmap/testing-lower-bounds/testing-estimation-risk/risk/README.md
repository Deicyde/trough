# Risk

Let $\hat{\mu}_\theta$ be the law of $\hat{y}(\theta)$. That is, $\hat{\mu} : \mathcal \Theta \rightsquigarrow \mathcal X$ is the kernel $\hat{y} \circ P$.

*Example (SBHT):* $r^P_\theta(\hat{y}) = \hat{\mu}_\theta(\hat{y}(\theta) \ne y(\theta))$.

- [Bayesian risk](def-bayesianrisk.md)

If we write $\ell'$ and $y$ for their deterministic kernels, the Bayesian risk of $\hat{y}$ is the mean of the measure $\ell' \circ (y \parallel \hat{y}) \circ (\pi \otimes P)$ .

- [Bayes risk](def-bayesrisk.md)

*Example (SBHT):* $\mathcal R^*_B = \sup_{\gamma \in [0,1]}\inf_{\hat{y}}\left(\gamma \hat{\mu}_0(\hat{y} \ne 0) + (1 - \gamma) \hat{\mu}_1(\hat{y} \ne 1)\right)$.

- [Bayes estimator](def-bayesestimator.md)
- [Minimax risk](def-minimaxrisk.md)

*Example (SBHT):* $\mathcal R^* = \inf_{\hat{y}} \max\{\hat{\mu}_0(\hat{y} \ne 0), \hat{\mu}_1(\hat{y} \ne 1)\}$.

- [bayesRisk_le_minimaxRisk](lem-bayesrisk-le-minimaxrisk.md)

TODO: “often”, $\mathcal R^*_B = \mathcal R^*$.

## Properties of the Bayes risk of a prior

- [bayesRisk_le_const](lem-bayesrisk-le-const.md)
- [bayesRisk_const](lem-bayesrisk-const.md)

Data-processing inequality and consequences

- [Data-processing inequality](thm-data-proc-bayesrisk.md)
- [bayesRisk_compProd_le_fst](lem-bayesrisk-compprod-le-fst.md)

Generalized Bayes estimator

- [bayesianRisk_bayesInv](lem-bayesianrisk-bayesinv.md)
- [bayesianRisk_ge_inf_bayesInv](lem-bayesianrisk-ge-inf-bayesinv.md)
- [Generalized Bayes estimator](def-genbayesestimator.md)
- [bayesianRisk_genBayesEstimator](lem-bayesianrisk-genbayesestimator.md)
- [isBayesEstimator_genBayesEstimator](thm-isbayesestimator-genbayesestimator.md)

## Bayes risk increase

TODO: remove this section? It's not used for anything now.

The following is a new definition, which is a natural generalization of the DeGroot statistical information.

- [riskIncrease](def-riskincrease.md)

In particular, if we take $\kappa : \mathcal X \rightsquigarrow *$ equal to the Markov kernel to the point space (denoted by $d_{\mathcal X}$, for “discard” kernel), we get $I^P_{\pi}(d_{\mathcal X}) = \mathcal R^{d_{\mathcal X} \circ P}_\pi - \mathcal R^P_\pi$, where $d_{\mathcal X} \circ P = d_\Theta$ if $P$ is a Markov kernel. We recover a difference between the risk of the best constant kernel and the Bayes estimator, as in the DeGroot statistical information.

The risk increase quantifies how much risk we accrue by forgetting information due to the composition with $\kappa$.

- [Data-processing inequality](lem-riskincrease-comp-del.md)
