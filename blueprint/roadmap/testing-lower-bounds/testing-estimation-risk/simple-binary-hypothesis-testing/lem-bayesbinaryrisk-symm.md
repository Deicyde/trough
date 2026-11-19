---
declaration: lemma
origin: cited
lean: ProbabilityTheory.bayesBinaryRisk_symm
statement: formalized
proof: formalized
---

# bayesBinaryRisk_symm

For $\mu, \nu \in \mathcal M(\mathcal X)$ and $\xi \in \mathcal M(\{0,1\})$, $\mathcal B_\xi(\mu, \nu) = \mathcal B_{\xi_{\leftrightarrow}}(\nu, \mu)$ where $\xi_{\leftrightarrow} \in \mathcal M(\{0,1\})$ is such that $\xi_{\leftrightarrow}(\{0\}) = \xi_1$ and $\xi_{\leftrightarrow}(\{1\}) = \xi_0$. For $\pi \in [0,1]$, $B_\pi(\mu, \nu) = B_{1 - \pi}(\nu, \mu)$ .

## Depends on

- [bayesBinaryRisk](def-bayesbinaryrisk.md)

## Lean

Formalized as [`ProbabilityTheory.bayesBinaryRisk_symm`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.bayesBinaryRisk_symm).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 683](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L683)
