---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Distribution.GaussianSchwartzWanted.gaussian_mem_schwartz, MathlibExt.Analysis.Distribution.SchwartzCommutantMulDerivWanted.exists_eq_smul_of_comp_mul_eq_of_comp_deriv_eq
statement: formalized
---

# Schwartz space

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/distributions/schwartz-space/index.html).

## The Gaussian is a Schwartz function

Let $E$ be a finite-dimensional real inner product
space. Then there is a real-valued Schwartz function $g$ on $E$ such that
$g(x) = e^{-\|x\|^2}$ for every $x \in E$.

## Sources

- <https://en.wikipedia.org/wiki/Schwartz_space>.

Stated but not proved: `MathlibExt.Analysis.Distribution.GaussianSchwartzWanted.gaussian_mem_schwartz` is written with `theorem_wanted` in [WantedExt/Analysis/Distribution/GaussianSchwartzWanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Distribution/GaussianSchwartzWanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/distributions/schwartz-space/index.html#gaussian-mem-schwartz).

## Linear maps on Schwartz space commuting with $x$ and $d/dx$ are scalars

Let
$\mathcal{S}(\mathbb{R})$ be the space of complex-valued Schwartz functions on $\mathbb{R}$, and
let $M:\mathcal{S}(\mathbb{R})\to\mathcal{S}(\mathbb{R})$ be a $\mathbb{C}$-linear map with
$(Mf)(x)=x f(x)$ for all $f\in\mathcal{S}(\mathbb{R})$ and $x\in\mathbb{R}$. If
$T:\mathcal{S}(\mathbb{R})\to\mathcal{S}(\mathbb{R})$ is a $\mathbb{C}$-linear map (not assumed
continuous) with $TM=MT$ and $T\frac{d}{dx}=\frac{d}{dx}T$, then there exists $c\in\mathbb{C}$
such that $Tf=cf$ for all $f\in\mathcal{S}(\mathbb{R})$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Operator theory; General theory of linear operators), problem `ma_proofbench_l2_54`.

Stated but not proved: `MathlibExt.Analysis.Distribution.SchwartzCommutantMulDerivWanted.exists_eq_smul_of_comp_mul_eq_of_comp_deriv_eq` is written with `theorem_wanted` in [WantedExt/Analysis/Distribution/SchwartzCommutantMulDerivWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Distribution/SchwartzCommutantMulDerivWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/distributions/schwartz-space/index.html#exists-eq-smul-of-comp-mul-eq-of-comp-de).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Schwartz space](https://deicyde.github.io/atlas-lean/roadmap/Analysis/distributions/schwartz-space/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/distributions/schwartz-space)
