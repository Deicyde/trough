---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Distribution.DistributionFderivWanted.exists_fderiv_distribution, MathlibExt.Analysis.Distribution.WeakThirdDerivativeZeroQuadraticWanted.ae_eq_quadratic_of_integral_mul_iteratedDeriv_three_eq_zero
statement: formalized
---

# Distributional derivatives

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/distributions/distributional-derivatives/index.html).

## The full derivative of a distribution

Let $E$ be a real normed space, $\Omega \subseteq E$
an open set and $F$ a real topological vector space, and let $\mathcal{D}'(\Omega, F)$ be the
space of $F$-valued distributions on $\Omega$ (continuous linear maps from the real-valued test
functions on $\Omega$ to $F$), with the topology of uniform convergence on compact sets of test
functions. For $v \in E$ and $T \in \mathcal{D}'(\Omega, F)$, let $\partial_v T$ be the
directional derivative $\varphi \mapsto -T(\partial_v \varphi)$. Then there is a continuous
linear map $D$ from $\mathcal{D}'(\Omega, F)$ to the space of continuous linear maps
$E \to \mathcal{D}'(\Omega, F)$ (with the topology of uniform convergence on bounded sets) such
that $D(T)(v) = \partial_v T$ for every $T \in \mathcal{D}'(\Omega, F)$ and every $v \in E$.

## Sources

- L. Schwartz, *Théorie des distributions*, Ch. II.

Stated but not proved: `MathlibExt.Analysis.Distribution.DistributionFderivWanted.exists_fderiv_distribution` is written with `theorem_wanted` in [WantedExt/Analysis/Distribution/DistributionFderivWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Distribution/DistributionFderivWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/distributions/distributional-derivatives/index.html#exists-fderiv-distribution).

## A function with vanishing weak third derivative on $(0,1)$ is a.e. a polynomial of degree at most $2$ on $(0,1)$

**A function with vanishing weak third derivative on $(0,1)$ is a.e. a polynomial of
degree at most $2$ on $[0,1]$.** Let $f:\mathbb{R}\to\mathbb{R}$ be integrable on $[0,1]$, and
suppose that $\int_{0}^{1} f(x)\,g'''(x)\,dx=0$ for every smooth function
$g:\mathbb{R}\to\mathbb{R}$ whose support is contained in some closed interval
$[s,t] \subseteq (0,1)$. Then there are real numbers $a$, $b$, $c$ such that $f(x)=a+bx+cx^2$
for almost every $x\in[0,1]$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Distributions, generalized functions, distribution spaces), problem `ma_proofbench_l2_66`.

Stated but not proved: `MathlibExt.Analysis.Distribution.WeakThirdDerivativeZeroQuadraticWanted.ae_eq_quadratic_of_integral_mul_iteratedDeriv_three_eq_zero` is written with `theorem_wanted` in [WantedExt/Analysis/Distribution/WeakThirdDerivativeZeroQuadraticWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Distribution/WeakThirdDerivativeZeroQuadraticWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/distributions/distributional-derivatives/index.html#ae-eq-quadratic-of-integral-mul-iterated).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Distributional derivatives](https://deicyde.github.io/atlas-lean/roadmap/Analysis/distributions/distributional-derivatives/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/distributions/distributional-derivatives)
