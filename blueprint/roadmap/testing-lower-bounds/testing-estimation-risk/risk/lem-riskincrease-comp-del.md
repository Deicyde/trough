---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.riskIncrease_comp_le
---

# Data-processing inequality

For any measurable space $\mathcal X$, let $d_{\mathcal X} : \mathcal X \rightsquigarrow *$ be the Markov kernel to the point space. For all Markov kernels $\kappa : \mathcal X \rightsquigarrow \mathcal X'$,

$$
\begin{aligned}
I_\pi^P(d_{\mathcal X}) \ge I_\pi^{\kappa \circ P}(d_{\mathcal X'}) \: .
\end{aligned}
$$

## Depends on

- [riskIncrease](def-riskincrease.md)

## Proof

By Lemma [riskIncrease_comp](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L479), then Lemma [riskIncrease_nonneg](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L466),

$$
\begin{aligned}
I_\pi^P(d_{\mathcal X'} \circ \kappa)
= I^P_\pi(\kappa) + I^{\kappa \circ P}_\pi(d_{\mathcal X'})
\ge I_\pi^{\kappa \circ P}(d_{\mathcal X'})
\: .
\end{aligned}
$$

Finally, $d_{\mathcal X'} \circ \kappa = d_{\mathcal X}$ since $\kappa$ is a Markov kernel.

## Lean

Formalized as [`ProbabilityTheory.riskIncrease_comp_le`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.riskIncrease_comp_le).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 501](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L501)
