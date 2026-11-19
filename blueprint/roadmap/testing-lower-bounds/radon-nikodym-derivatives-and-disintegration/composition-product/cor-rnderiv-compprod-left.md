---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.rnDeriv_measure_compProd_left
---

# rnDeriv_compProd_left

Let $\mu, \nu \in \mathcal M(\mathcal X)$ and let $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ be a finite kernel. Then for $(\nu \otimes \kappa)$-almost all $(x, y)$, $\frac{d (\mu \otimes \kappa)}{d (\nu \otimes \kappa)}(x,y) = \frac{d\mu}{d\nu}(x)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [rnDeriv_eq_ac_left](lem-rnderiv-eq-ac-left.md)

## Proof

We can suppose $\mu \ll \nu$ without loss of generality (by Lemma [rnDeriv_eq_ac_left](lem-rnderiv-eq-ac-left.md)). That implies $\mu \otimes \kappa \ll \nu \otimes \kappa$. It suffices to show that the integrals of the two functions agree on all sets in the $\pi$-system of products of measurable sets. Let $s, t$ be two measurable sets of $\mathcal X$ and $\mathcal Y$ respectively.

$$
\begin{aligned}
\int_{p \in s \times t} \frac{d (\mu \otimes \kappa)}{d (\nu \otimes \kappa)}(p) \partial(\nu \otimes \kappa)
&= (\mu \otimes \kappa) (s \times t)
\: .
\end{aligned}
$$

$$
\begin{aligned}
\int_{p \in s \times t} \frac{d \mu}{d \nu}(p_1) \partial(\nu \otimes \kappa)
&= \int_{x \in s} \int_{y \in t} \frac{d \mu}{d \nu}(x) \partial \kappa(x) \partial \nu
\\
&= \int_{x \in s} \frac{d \mu}{d \nu}(x) \kappa(x)(t) \partial \nu
\\
&= \int_{x \in s} \kappa(x)(t) \partial \mu
\\
&= (\mu \otimes \kappa) (s \times t)
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.rnDeriv_measure_compProd_left`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.rnDeriv_measure_compProd_left).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/rn_deriv.tex, line 173](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/rn_deriv.tex#L173)
