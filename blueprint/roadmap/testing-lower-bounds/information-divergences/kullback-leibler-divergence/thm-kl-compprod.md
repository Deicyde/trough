---
declaration: theorem
origin: cited
lean: ProbabilityTheory.klDiv_compProd_eq_add_condKL
statement: formalized
proof: formalized
---

# Chain rule, kernel version

Let $\mu, \nu$ be two finite measures on $\mathcal X$ and $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ two Markov kernels, with either $\mathcal X$ countable or $\mathcal{Y}$ countably generated. Then $\operatorname{KL}(\mu \otimes \kappa, \nu \otimes \eta) = \operatorname{KL}(\mu, \nu) + \operatorname{KL}(\kappa, \eta \mid \mu)$.

## Depends on

- [Kullback-Leibler divergence](def-kl.md)
- [Conditional Kullback-Leibler divergence](def-condkl.md)

## Proof depends on

- [rnDeriv_compProd](../../radon-nikodym-derivatives-and-disintegration/composition-product/lem-rnderiv-compprod.md)
- [rnDeriv_value](../../radon-nikodym-derivatives-and-disintegration/kernel-radon-nikodym-derivative/cor-rnderiv-value.md)
- [:ii](ii.md)

## Proof

Handle the case where $\mu \otimes \kappa$ is not absolutely continuous with respect to $\nu \otimes \eta$ first, then the case where $p \mapsto \log \frac{d \mu \otimes \kappa}{d \nu \otimes \eta}(p)$ is not $\mu \otimes \kappa$-integrable using Lemma [:ii](ii.md).

For the case where $\mu \otimes \kappa \ll \nu \otimes \eta$ and $p \mapsto \log \frac{d \mu \otimes \kappa}{d \nu \otimes \eta}(p)$ is $\mu \otimes \kappa$-integrable use Lemma [rnDeriv_compProd](../../radon-nikodym-derivatives-and-disintegration/composition-product/lem-rnderiv-compprod.md) and Corollary [rnDeriv_value](../../radon-nikodym-derivatives-and-disintegration/kernel-radon-nikodym-derivative/cor-rnderiv-value.md) in a computation:

$$
\begin{aligned}
\operatorname{KL}(\mu \otimes \kappa, \nu \otimes \eta)
&= \int_p \log \frac{d(\mu \otimes \kappa)}{d(\nu \otimes \eta)}(p) \partial (\mu \otimes \kappa)
\\
&= \int_x \int_y\log \left(\frac{d\mu}{d \nu}(x)\frac{d\kappa}{d \eta}(x,y)\right) \partial \kappa(x) \partial\mu
\\
&= \int_x \int_y\log \left(\frac{d\mu}{d \nu}(x)\right) + \log \left(\frac{d\kappa}{d \eta}(x,y)\right) \partial \kappa(x) \partial\mu
\\
&= \int_x \log \left(\frac{d\mu}{d \nu}(x)\right)\partial\mu + \int_x \int_y\log \left(\frac{d\kappa}{d \eta}(x,y)\right) \partial \kappa(x) \partial\mu
\\
&= \int_x \log \left(\frac{d\mu}{d \nu}(x)\right)\partial\mu + \int_x \int_y\log \left(\frac{d\kappa(x)}{d \eta(x)}(y)\right) \partial \kappa(x) \partial\mu
\\
&= \operatorname{KL}(\mu, \nu) + \operatorname{KL}(\kappa, \eta \mid \mu)
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.klDiv_compProd_eq_add_condKL`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.klDiv_compProd_eq_add_condKL).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kl_divergence.tex, line 262](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kl_divergence.tex#L262)
