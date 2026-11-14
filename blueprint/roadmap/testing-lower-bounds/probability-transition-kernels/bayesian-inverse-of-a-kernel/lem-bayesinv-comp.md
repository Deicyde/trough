---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.posterior_comp
---

# bayesInv_comp

Let $\mu \in \mathcal M(\mathcal X)$, $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ and $\eta : \mathcal Y \rightsquigarrow \mathcal Z$. Then $(\eta \circ \kappa \circ \mu)$-a.e.,

$$
\begin{aligned}
(\eta \circ \kappa)_\mu^\dagger = \kappa_{\mu}^\dagger \circ \eta_{\kappa \circ \mu}^\dagger
\: .
\end{aligned}
$$

## Depends on

- [bayesInv](def-bayesinv.md)
- [Composition](../composition-and-product/def-kernel-comp.md)

## Proof depends on

- [a.e.-uniqueness of the Bayesian inverse](lem-eq-bayesinv-of-compprod-eq.md)

## Proof

It suffices to show that $\mu \otimes (\eta \circ \kappa) = ((\eta \circ \kappa \circ \mu) \otimes (\kappa_{\mu}^\dagger \circ \eta_{\kappa \circ \mu}^\dagger))_\leftrightarrow$.

TODO: transcribe the code.

## Lean

Formalized as [`ProbabilityTheory.posterior_comp`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.posterior_comp).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kernels.tex, line 386](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kernels.tex#L386)
