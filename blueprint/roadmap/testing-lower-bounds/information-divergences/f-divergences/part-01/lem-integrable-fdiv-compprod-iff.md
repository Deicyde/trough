---
declaration: lemma
origin: cited
lean: ProbabilityTheory.integrable_f_rnDeriv_compProd_iff
statement: formalized
---

# integrable_fDiv_compProd_iff

Let $\mu$ be a finite measure on $\mathcal X$ and $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ be two finite kernels from $\mathcal X$ to $\mathcal Y$. Then $p \mapsto f \left(\frac{d(\mu \otimes \kappa)}{d(\mu \otimes \eta)}(p)\right)$ is $(\mu \otimes \eta)$-integrable iff

- $x \mapsto D_f(\kappa(x), \eta(x))$ is $\mu$-integrable and
- for $\mu$-almost all $x$, $y \mapsto f \left( \frac{d\kappa(x)}{d\eta(x)}(y) \right)$ is $\eta(x)$-integrable.

## Depends on

- [f-divergence](def-fdiv.md)

## Proof

Since $x \mapsto f \left(\frac{d(\mu \otimes \kappa)}{d(\mu \otimes \eta)} x \right)$ is measurable, the integrability condition w.r.t. $\mu \otimes \eta$ is equivalent to

- $x \mapsto \int_y \left\Vert f \left( \frac{d\kappa(x)}{d\eta(x)}(y) \right) \right\Vert \partial \eta(x)$ is $\mu$-integrable and
- for $\mu$-almost all $x$, $y \mapsto f \left( \frac{d\kappa(x)}{d\eta(x)}(y) \right)$ is $\eta(x)$-integrable.

It suffices to use convexity to show that integrability of $x \mapsto \int_y f \left( \frac{d\kappa(x)}{d\eta(x)}(y) \right) \partial \eta(x)$ implies integrability of $x \mapsto \int_y \left\Vert f \left( \frac{d\kappa(x)}{d\eta(x)}(y) \right) \right\Vert \partial \eta(x)$.

TODO

## Lean

Stated as [`ProbabilityTheory.integrable_f_rnDeriv_compProd_iff`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.integrable_f_rnDeriv_compProd_iff); the blueprint marks no proof of it as formalized.

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 437](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L437)
