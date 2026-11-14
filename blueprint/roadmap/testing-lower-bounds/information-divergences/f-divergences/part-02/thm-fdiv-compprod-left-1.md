---
declaration: lemma
origin: cited
lean: ProbabilityTheory.fDiv_compProd_left
statement: formalized
proof: formalized
---

# Composition-product with a kernel

Let $\mu, \nu$ be two measures on $\mathcal X$ and let $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ be a Markov kernel. Then $D_f(\mu \otimes \kappa, \nu \otimes \kappa) = D_f(\mu, \nu)$.

## Depends on

- [f-divergence](../part-01/def-fdiv.md)

## Proof depends on

- [rnDeriv_compProd_left](../../../radon-nikodym-derivatives-and-disintegration/composition-product/cor-rnderiv-compprod-left.md)

## Proof

By Lemma [rnDeriv_compProd_left](../../../radon-nikodym-derivatives-and-disintegration/composition-product/cor-rnderiv-compprod-left.md) and the fact that $(\mu \otimes \kappa)_{\perp \nu \otimes \kappa} = \mu_{\perp \nu} \otimes \kappa$ (Lemma TODO),

$$
\begin{aligned}
D_f(\mu \otimes \kappa, \nu \otimes \kappa)
&= \int_{p} f \left(\frac{d (\mu \otimes \kappa)}{d (\nu \otimes \kappa)}(p)\right) \partial(\nu \otimes \kappa)
+ f'(\infty) (\mu \otimes \kappa)_{\perp \nu \otimes \kappa}(\mathcal X)
\\
&= \int_{p} f \left(\frac{d \mu}{d \nu}(p_X)\right) \partial(\nu \otimes \kappa)
+ f'(\infty) (\mu_{\perp \nu} \otimes \kappa)(\mathcal X)
\\
&= \int_x \int_y f \left(\frac{d \mu}{d \nu}(x)\right) \partial \kappa(x) \partial \nu
+ f'(\infty) \mu_{\perp \nu}(\mathcal X)
\\
&= \int_x f \left(\frac{d \mu}{d \nu}(x)\right) \partial \nu
+ f'(\infty) \mu_{\perp \nu}(\mathcal X)
\\
&= D_f(\mu, \nu)
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.fDiv_compProd_left`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_compProd_left).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 834](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L834)
