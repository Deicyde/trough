---
declaration: lemma
origin: cited
lean: ProbabilityTheory.fDiv_compProd_right
statement: formalized
proof: formalized
---

# fDiv_compProd_right

Let $\mu$ be a finite measure on $\mathcal X$ and let $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ be two finite kernels. Then $D_f(\mu \otimes \kappa, \mu \otimes \eta) = D_f(\kappa, \eta \mid \mu)$.

## Depends on

- [f-divergence](../part-01/def-fdiv.md)
- [Conditional f-divergence](../part-01/def-condfdiv.md)

## Proof depends on

- [rnDeriv_compProd_right](../../../radon-nikodym-derivatives-and-disintegration/composition-product/cor-rnderiv-compprod-right.md)
- [rnDeriv_value](../../../radon-nikodym-derivatives-and-disintegration/kernel-radon-nikodym-derivative/cor-rnderiv-value.md)

## Proof

The singular part of $\mu \otimes \kappa$ with respect to $\mu \otimes \eta$ is $\mu \otimes \kappa_{\perp \eta}$, hence $(\mu \otimes \kappa)_{\perp (\mu \otimes \eta)}(\mathcal X \times \mathcal Y) = \mu\left[x \mapsto \kappa(x)_{\perp \eta(x)}(\mathcal Y)\right]$. For the integral part, by Lemma [rnDeriv_compProd_right](../../../radon-nikodym-derivatives-and-disintegration/composition-product/cor-rnderiv-compprod-right.md) and Corollary [rnDeriv_value](../../../radon-nikodym-derivatives-and-disintegration/kernel-radon-nikodym-derivative/cor-rnderiv-value.md),

$$
\begin{aligned}
\int_{p} f\left(\frac{d (\mu \otimes \kappa)}{d (\mu \otimes \eta)}(p)\right) \partial(\mu \otimes \eta)
&= \int_{p} f\left(\frac{d \kappa}{d \eta}(p)\right) \partial(\mu \otimes \eta)
\\
&= \int_x \int_y f\left(\frac{d \kappa}{d \eta}(x, y)\right) \partial \eta(x) \partial \mu
\\
&= \int_x \int_y f\left(\frac{d \kappa(x)}{d \eta(x)}(y)\right) \partial \eta(x) \partial \mu
\: .
\end{aligned}
$$

Adding $f'(\infty)$ times the singular parts gives $D_f(\mu \otimes \kappa, \mu \otimes \eta) = \mu\left[D_f(\kappa(x), \eta(x))\right] = D_f(\kappa, \eta \mid \mu)$.

## Lean

Formalized as [`ProbabilityTheory.fDiv_compProd_right`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_compProd_right).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 496](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L496)
