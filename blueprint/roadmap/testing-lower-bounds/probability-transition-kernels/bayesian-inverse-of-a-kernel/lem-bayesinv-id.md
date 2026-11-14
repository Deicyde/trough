---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.posterior_id
---

# bayesInv_id

Let $\mu \in \mathcal M (\mathcal X)$ and let $\textup{id} : \mathcal X \rightsquigarrow \mathcal X$ be the identity kernel. Then $\textup{id}_\mu^\dagger = \textup{id}$.

## Depends on

- [bayesInv](def-bayesinv.md)

## Proof depends on

- [a.e.-uniqueness of the Bayesian inverse](lem-eq-bayesinv-of-compprod-eq.md)

## Proof

It suffices to show that $\mu \otimes \textup{id} = ((\textup{id} \circ \mu) \otimes \textup{id})_\leftrightarrow$ , which is clear.

## Lean

Formalized as [`ProbabilityTheory.posterior_id`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.posterior_id).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kernels.tex, line 372](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kernels.tex#L372)
