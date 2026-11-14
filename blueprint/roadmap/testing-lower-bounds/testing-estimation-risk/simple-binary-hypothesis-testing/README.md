# Simple binary hypothesis testing

In this section, for a measure $\xi$ on $\{0,1\}$, we write $\xi_0$ for $\xi(\{0\})$ and $\xi_1$ for $\xi(\{1\})$ . We sometimes write $(a,b)$ for the measure $\xi$ on $\{0,1\}$ with $\xi_0 = a$ and $\xi_1 = b$.

- [bayesInv_binary](lem-bayesinv-binary.md)
- [bayesRisk_binary](lem-bayesrisk-binary.md)

## Bayes risk of a prior

- [bayesBinaryRisk](def-bayesbinaryrisk.md)

Thanks to the following lemma, we can prove properties of the Bayes binary risk for non-zero finite measures by considering only probability measures.

- [bayesBinaryRisk_mul](lem-bayesbinaryrisk-mul.md)

Alternatively, we can reduce the study of the Bayes binary risk for any prior to the study of the prior $(1, 1)$, for which that risk is related to the total variation distance (defined later).

- [bayesBinaryRisk_one_one](lem-bayesbinaryrisk-one-one.md)
- [Data-processing inequality](thm-data-proc-bayesbinaryrisk.md)
- [bayesBinaryRisk_self](lem-bayesbinaryrisk-self.md)
- [bayesBinaryRisk_le](lem-bayesbinaryrisk-le.md)
- [bayesBinaryRisk_symm](lem-bayesbinaryrisk-symm.md)
- [genBayesEstimator_bayesBinaryRisk](lem-genbayesestimator-bayesbinaryrisk.md)
- [bayesBinaryRisk_eq_event](lem-bayesbinaryrisk-eq-event.md)
- [bayesBinaryRisk_eq](thm-bayesbinaryrisk-eq.md)
- [bayesBinaryRisk_eq_abs](cor-bayesbinaryrisk-eq-abs.md)
