---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.posterior_posterior
---

# bayesInv_self

For $\mathcal X$ and $\mathcal Y$ two standard Borel spaces, $\mu \in \mathcal M(\mathcal X)$ s-finite and $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ a Markov kernel, $(\kappa_\mu^\dagger)_{\kappa \circ \mu}^\dagger = \kappa$ ($\mu$-a.e.).

## Depends on

- [bayesInv](def-bayesinv.md)

## Proof depends on

- [bayesInv_comp_self](lem-bayesinv-comp-self.md)
- [a.e.-uniqueness of the Bayesian inverse](lem-eq-bayesinv-of-compprod-eq.md)

## Proof

By uniqueness of the disintegration, it suffices to show that $(\kappa \circ \mu) \otimes \kappa_\mu^\dagger = ((\kappa_\mu^\dagger \circ \kappa \circ \mu) \otimes \kappa)_\leftrightarrow$ . By Lemma [bayesInv_comp_self](lem-bayesinv-comp-self.md), $\kappa_\mu^\dagger \circ \kappa \circ \mu = \mu$ and we need to prove $(\kappa \circ \mu) \otimes \kappa_\mu^\dagger = (\mu \otimes \kappa)_\leftrightarrow$ . This is true by definition of $\kappa_\mu^\dagger$ .

## Lean

Formalized as [`ProbabilityTheory.posterior_posterior`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.posterior_posterior).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kernels.tex, line 356](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kernels.tex#L356)
