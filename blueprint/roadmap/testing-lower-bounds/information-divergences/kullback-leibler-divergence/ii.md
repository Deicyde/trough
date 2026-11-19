---
declaration: lemma
origin: cited
lean: ProbabilityTheory.integrable_llr_compProd_iff
statement: formalized
---

# :ii

Let $\mu, \nu$ be two finite measures on $\mathcal X$ and $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ be two Markov kernels such that $\mu \otimes \kappa \ll \nu \otimes \eta$. Then $p \mapsto \log \frac{d \mu \otimes \kappa}{d \nu \otimes \eta}(p)$ is $\mu \otimes \kappa$-integrable if and only if the following hold:

1. $x \mapsto \log \frac{d \mu}{d \nu}(x)$ is $\mu$-integrable
2. $x \mapsto \int_y \log \frac{d \kappa(x)}{d \eta(x)}(y) \partial \kappa(x)$ is $\mu$-integrable
3. for $\mu$-almost all $x$, $y \mapsto \log \frac{d \kappa(x)}{d \eta(x)}(y)$ is $\kappa(x)$-integrable

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Kullback-Leibler divergence](def-kl.md)
- [integrable_fDiv_compProd_iff](../f-divergences/part-01/lem-integrable-fdiv-compprod-iff.md)

## Proof

Note that from the hypothesis it easily follows that $\mu \ll \nu$ and $\mu$-a.e. $\kappa(x) \ll \eta(x)$.

Applying Lemma [integrable_fDiv_compProd_iff](../f-divergences/part-01/lem-integrable-fdiv-compprod-iff.md) we know that $\log \frac{d \mu \otimes \kappa}{d \nu \otimes \eta}$ is $\nu \otimes \eta$-integrable iff the following hold:

- i. for $\nu$-almost all $x$, $y \mapsto \frac{d \mu}{d \nu}(x) \frac{d \kappa(x)}{d \eta(x)}(y) \log \left(\frac{d \mu}{d \nu}(x) \frac{d \kappa(x)}{d \eta(x)}(y) \right)$ is $\eta(x)$-integrable
- ii. $x \mapsto \int_y \frac{d \mu}{d \nu}(x) \frac{d \kappa(x)}{d \eta(x)}(y) \log \left(\frac{d \mu}{d \nu}(x) \frac{d \kappa(x)}{d \eta(x)}(y) \right) \partial \eta (x)$ is $\nu$-integrable

**(i.$\Leftarrow$)** 3. implies that $\nu$-a.e. $y \mapsto \frac{d \mu}{d \nu}(x) \log \frac{d \kappa(x)}{d \eta(x)}(y)$ is $\kappa(x)$-integrable, hence $y \mapsto \frac{d \mu}{d \nu}(x) \frac{d \kappa(x)}{d \eta(x)}(y) \log \frac{d \kappa(x)}{d \eta(x)}(y)$ is $\eta(x)$-integrable $\nu$-a.e. Moreover $y \mapsto \frac{d \kappa(x)}{d \eta(x)}(y)$ is $\eta(x)$-integrable, then, since $\frac{d \mu}{d \nu}(x) \log \frac{d \mu}{d \nu}(x)$ is constant in $y$, $y \mapsto \frac{d \mu}{d \nu}(x) \frac{d \kappa(x)}{d \eta(x)}(y) \log \frac{d \mu}{d \nu}(x)$ is $\eta(x)$-integrable. This allows us to conclude that $y \mapsto \frac{d \mu}{d \nu}(x) \frac{d \kappa(x)}{d \eta(x)}(y) \log \frac{d \kappa(x)}{d \eta(x)}(y) + \frac{d \mu}{d \nu}(x) \frac{d \kappa(x)}{d \eta(x)}(y) \log \frac{d \mu}{d \nu}(x) = \frac{d \mu}{d \nu}(x) \frac{d \kappa(x)}{d \eta(x)}(y) \log \left(\frac{d \mu}{d \nu}(x) \frac{d \kappa(x)}{d \eta(x)}(y) \right)$ is $\eta(x)$-integrable $\nu$-a.e.

**(ii.$\Leftarrow$)** 1. implies that $x \mapsto \frac{d \mu}{d \nu}(x) \log \frac{d \mu}{d \nu}(x)$ is $\nu$-integrable. 2. implies that $x \mapsto \frac{d \mu}{d \nu}(x) \int_y \frac{d \kappa(x)}{d \eta(x)}(y) \log \frac{d \kappa(x)}{d \eta(x)}(y) \partial \eta(x)$ is $\nu$-integrable. Therefore

$$
x \mapsto \frac{d \mu}{d \nu}(x) \log \frac{d \mu}{d \nu}(x) + \frac{d \mu}{d \nu}(x) \int_y \frac{d \kappa(x)}{d \eta(x)}(y) \log \frac{d \kappa(x)}{d \eta(x)}(y) \partial \eta(x) = \int_y \frac{d \mu}{d \nu}(x) \frac{d \kappa(x)}{d \eta(x)}(y) \log \left(\frac{d \mu}{d \nu}(x) \frac{d \kappa(x)}{d \eta(x)}(y) \right) \partial \eta (x)
$$

is $\nu$-integrable.

**($\Rightarrow$1.)** This follows from the hypothesis applying a more general Lemma for f divergences, see ProbabilityTheory.integrable\_f\_rnDeriv\_of\_integrable\_compProd' in the lean code.

**($\Rightarrow$3.)** i. implies that $\mu$-a.e. $y \mapsto \frac{d \kappa(x)}{d \eta(x)}(y) \log \left(\frac{d \mu}{d \nu}(x) \frac{d \kappa(x)}{d \eta(x)}(y) \right)$ is $\eta(x)$-integrable, hence $y \mapsto \log \left(\frac{d \mu}{d \nu}(x) \frac{d \kappa(x)}{d \eta(x)}(y) \right) = \log \frac{d \mu}{d \nu}(x) + \log \frac{d \kappa(x)}{d \eta(x)}(y)$ is $\kappa(x)$-integrable. Then, since $\log \frac{d \mu}{d \nu}(x)$ is constant in $y$ and $\kappa(x)$ is a finite measure, $y \mapsto \log \frac{d \kappa(x)}{d \eta(x)}(y)$ is $\kappa(x)$-integrable.

**($\Rightarrow$2.)** ii. implies that $x \mapsto \int_y \frac{d \kappa(x)}{d \eta(x)}(y) \log \left(\frac{d \mu}{d \nu}(x) \frac{d \kappa(x)}{d \eta(x)}(y) \right) \partial \eta (x) = \int_y \log \left(\frac{d \mu}{d \nu}(x) \frac{d \kappa(x)}{d \eta(x)}(y) \right) \partial \kappa (x)$ is $\mu$-integrable. Thanks to 3. we can split the integral:

$$
\int_y \log \left(\frac{d \mu}{d \nu}(x) \frac{d \kappa(x)}{d \eta(x)}(y) \right) \partial \kappa (x)
= \int_y \log \frac{d \mu}{d \nu}(x) \partial \kappa (x) + \int_y \log \frac{d \kappa(x)}{d \eta(x)}(y) \partial \kappa (x) = \log \frac{d \mu}{d \nu}(x) + \int_y \log \frac{d \kappa(x)}{d \eta(x)}(y) \partial \kappa (x)
$$

Then using 1. we can conclude that $x \mapsto \int_y \log \frac{d \kappa(x)}{d \eta(x)}(y) \partial \kappa (x)$ is $\mu$-integrable.

## Lean

Stated as [`ProbabilityTheory.integrable_llr_compProd_iff`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.integrable_llr_compProd_iff); the blueprint marks no proof of it as formalized.

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kl_divergence.tex, line 175](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kl_divergence.tex#L175)
