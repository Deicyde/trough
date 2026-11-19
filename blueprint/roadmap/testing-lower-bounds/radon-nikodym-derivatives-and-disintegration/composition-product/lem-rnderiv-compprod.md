---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.rnDeriv_measure_compProd
---

# rnDeriv_compProd

Let $\mu, \nu$ be two finite measures on $\mathcal X$ and let $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ be two finite kernels, with either $\mathcal X$ countable or $\mathcal{Y}$ countably generated. Then for $(\nu \otimes \eta)$-almost all $(x, y)$,

$$
\begin{aligned}
\frac{d (\mu \otimes \kappa)}{d (\nu \otimes \eta)}(x,y) = \frac{d\mu}{d\nu}(x)\frac{d \kappa}{d \eta}(x,y)
\: .
\end{aligned}
$$

This implies that the equality is true for $\nu$-almost all $x$, for $\eta(x)$-almost all $y$.

## Depends on

- [kernel_rnDeriv](../kernel-radon-nikodym-derivative/def-kernel-rnderiv.md)

## Proof depends on

- [Chain rule for Radon-Nikodym derivatives](thm-rnderiv-chain-compprod.md)
- [rnDeriv_compProd_right](cor-rnderiv-compprod-right.md)
- [ae_rnDeriv_ne_zero](lem-ae-rnderiv-ne-zero.md)
- [rnDeriv_compProd_left](cor-rnderiv-compprod-left.md)

## Proof

First, by Theorem [Chain rule for Radon-Nikodym derivatives](thm-rnderiv-chain-compprod.md), for $(\nu \otimes \eta)$-almost all $(x,y)$,

$$
\begin{aligned}
\frac{d(\mu \otimes \kappa)}{d(\nu \otimes \eta)}(x, y)
= \frac{d \mu}{d \nu}(x) \frac{d(\mu \otimes \kappa)}{d(\mu \otimes \eta)}(x, y)
\: .
\end{aligned}
$$

It remains to show that $\frac{d \mu}{d \nu}(x) \frac{d(\mu \otimes \kappa)}{d(\mu \otimes \eta)}(x, y)$ is $(\nu \otimes \eta)$-almost everywhere equal to $\frac{d\mu}{d\nu}(x)\frac{d \kappa}{d \eta}(x,y)$. By Lemma [rnDeriv_compProd_right](cor-rnderiv-compprod-right.md), $(\mu \otimes \eta)$-almost surely,

$$
\begin{aligned}
\frac{d \kappa}{d \eta} = \frac{d (\mu \otimes \kappa)}{d (\mu \otimes \eta)}
\: .
\end{aligned}
$$

We then use Lemma [ae_rnDeriv_ne_zero](lem-ae-rnderiv-ne-zero.md) to turn that into a $(\nu \otimes \eta)$-almost sure equality:

$$
\begin{aligned}
\frac{d(\mu \otimes \eta)}{d(\nu \otimes \eta)}\frac{d \kappa}{d \eta} = \frac{d(\mu \otimes \eta)}{d(\nu \otimes \eta)}\frac{d (\mu \otimes \kappa)}{d (\mu \otimes \eta)}
\: .
\end{aligned}
$$

Finally, by Lemma [rnDeriv_compProd_left](cor-rnderiv-compprod-left.md), $\frac{d(\mu \otimes \eta)}{d(\nu \otimes \eta)} = \frac{d\mu}{d\nu}$ almost surely.

## Lean

Formalized as [`ProbabilityTheory.rnDeriv_measure_compProd`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.rnDeriv_measure_compProd).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/rn_deriv.tex, line 298](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/rn_deriv.tex#L298)
