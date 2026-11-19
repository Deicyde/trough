---
declaration: definition
origin: cited
lean: ProbabilityTheory.statInfo
statement: formalized
---

# statInfo

The statistical information between measures $\mu$ and $\nu$ with respect to prior $\xi \in \mathcal M(\{0,1\})$ is $\mathcal I_\xi(\mu, \nu) = \min\{\xi_0 \mu(\mathcal X), \xi_1 \nu(\mathcal X)\} - \mathcal B_\xi(\mu, \nu)$. This is the risk increase $I_\xi^P(d_{\mathcal X})$ in the binary hypothesis testing problem for $d_{\mathcal X} : \mathcal X \rightsquigarrow *$ the Markov kernel to the point space.

## Depends on

- [bayesBinaryRisk](../../../testing-estimation-risk/simple-binary-hypothesis-testing/def-bayesbinaryrisk.md)
- [riskIncrease](../../../testing-estimation-risk/risk/def-riskincrease.md)

## Lean

Formalized as [`ProbabilityTheory.statInfo`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.statInfo).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/stat_div.tex, line 8](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/stat_div.tex#L8)
