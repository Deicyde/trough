---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.rnDeriv_compProd
---

# Chain rule for Radon-Nikodym derivatives

Let $\mu, \nu$ be two finite measures on $\mathcal X$ and let $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ be two finite kernels with $\mu \otimes \kappa \ll \mu \otimes \eta$. Then for $(\nu \otimes \eta)$-almost all $(x,y)$,

$$
\begin{aligned}
\frac{d(\mu \otimes \kappa)}{d(\nu \otimes \eta)}(x, y)
= \frac{d \mu}{d \nu}(x) \frac{d(\mu \otimes \kappa)}{d(\mu \otimes \eta)}(x, y)
\: .
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [rnDeriv_chain](lem-rnderiv-chain.md)
- [rnDeriv_compProd_left](cor-rnderiv-compprod-left.md)

## Proof

By the first point of Lemma [rnDeriv_chain](lem-rnderiv-chain.md), $(\nu \otimes \eta)$-almost surely,

$$
\begin{aligned}
\frac{d(\mu \otimes \kappa)}{d(\nu \otimes \eta)}
= \frac{d(\mu \otimes \kappa)}{d(\mu \otimes \eta)} \frac{d (\mu \otimes \eta)}{d (\nu \otimes \eta)}
\end{aligned}
$$

Then, by Lemma [rnDeriv_compProd_left](cor-rnderiv-compprod-left.md), $\frac{d (\mu \otimes \eta)}{d (\nu \otimes \eta)}$ is almost everywhere equal to $\frac{d\mu}{d\nu}$.

## Lean

Formalized as [`ProbabilityTheory.rnDeriv_compProd`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.rnDeriv_compProd).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/rn_deriv.tex, line 223](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/rn_deriv.tex#L223)
