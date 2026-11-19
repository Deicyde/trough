---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.rnDeriv_posterior
---

# rnDeriv_bayesInv

Let $\mu \in \mathcal M(\mathcal X)$ and $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ such that $\kappa_\mu^\dagger$ exists and such that $\kappa(x) \ll \kappa \circ \mu$ almost surely. Then for $\mu$-almost all $x$ and $(\kappa \circ \mu)$-almost all $y$,

$$
\begin{aligned}
\frac{d \kappa_\mu^\dagger(y)}{d \mu}(x) = \frac{d \kappa(x)}{d(\kappa \circ \mu)}(y)
\: .
\end{aligned}
$$

## Depends on

- [bayesInv](def-bayesinv.md)

## Proof

$\mu$-almost all $x$ and $(\kappa \circ \mu)$-almost all $y$ is the same as $(\mu \times (\kappa \circ \mu))$-almost all $(x, y)$. It suffices to show that for all measurable sets of $\mathcal X \times \mathcal Y$, the integrals with respect to that product measure of the two sides of the equality on the set are equal. Furthermore, it is sufficient to show it for sets of the form $s \times t$ since those are a $\pi$-system.

Since $\kappa(x) \ll \kappa \circ \mu$ almost surely, we have $\mu \otimes \kappa \ll \mu \times (\kappa \circ \mu)$, hence $(\kappa \circ \mu) \otimes \kappa_\mu^\dagger \ll (\kappa \circ \mu) \times \mu$. We get that $\kappa_\mu^\dagger(y) \ll \mu$ almost surely.

$$
\begin{aligned}
\int_{x \in s, y \in t} \frac{d \kappa_\mu^\dagger(y)}{d \mu}(x) \partial (\mu \times (\kappa \circ \mu))
&= \int_{y \in t} \int_{x \in s} \frac{d \kappa_\mu^\dagger(y)}{d \mu}(x) \partial \mu \partial (\kappa \circ \mu)
\\
&= \int_{y \in t} \kappa_\mu^\dagger(y)(s) \partial (\kappa \circ \mu)
\\
&= ((\kappa \circ \mu) \otimes \kappa_\mu^\dagger) (t \times s)
\: .
\end{aligned}
$$

$$
\begin{aligned}
\int_{x \in s, y \in t} \frac{d \kappa(x)}{d(\kappa \circ \mu)}(y) \partial (\mu \times (\kappa \circ \mu))
&= \int_{x \in s} \int_{y \in t} \frac{d \kappa(x)}{d(\kappa \circ \mu)}(y) \partial (\kappa \circ \mu) \partial \mu
\\
&= \int_{x \in s} \kappa(x)(t) \partial \mu
\\
&= (\mu \otimes \kappa) (s \times t)
\: .
\end{aligned}
$$

By the defining property of the Bayesian inverse, those two quantities are equal.

## Lean

Formalized as [`ProbabilityTheory.rnDeriv_posterior`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.rnDeriv_posterior).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kernels.tex, line 406](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kernels.tex#L406)
