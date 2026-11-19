---
declaration: definition
origin: cited
lean: ProbabilityTheory.bayesBinaryRisk
statement: formalized
---

# bayesBinaryRisk

The Bayes binary risk between measures $\mu$ and $\nu$ with respect to prior $\xi \in \mathcal M(\{0,1\})$, denoted by $\mathcal B_\xi(\mu, \nu)$, is the Bayes risk $\mathcal R^P_\xi$ for $\Theta = \mathcal Y = \mathcal Z = \{0,1\}$, $\ell(y,z) = \mathbb{I}\{y \ne z\}$, $P$ the kernel sending 0 to $\mu$ and 1 to $\nu$ and prior $\xi$. That is,

$$
\begin{aligned}
\mathcal B_\xi(\mu, \nu) = \inf_{\hat{y} : \mathcal X \rightsquigarrow \{0,1\}}\left(\xi_0 (\hat{y} \circ \mu)(\{1\}) + \xi_1 (\hat{y} \circ \nu)(\{0\})\right)
\: ,
\end{aligned}
$$

in which the infimum is over Markov kernels.

If the prior is a probability measure with weights $(\pi, 1 - \pi)$, we write $B_\pi(\mu, \nu) = \mathcal B_{(\pi, 1 - \pi)}(\mu, \nu)$ .

## Depends on

- [Bayes risk](../risk/def-bayesrisk.md)

## Lean

Formalized as [`ProbabilityTheory.bayesBinaryRisk`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.bayesBinaryRisk).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 566](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L566)
