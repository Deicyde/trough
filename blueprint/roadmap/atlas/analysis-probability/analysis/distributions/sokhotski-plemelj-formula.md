---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Distribution.PlemeljLimitTemperedDistributionWanted.uPlusEps, MathlibExt.Analysis.Distribution.PlemeljLimitTemperedDistributionWanted.uMinusEps, MathlibExt.Analysis.Distribution.PlemeljLimitTemperedDistributionWanted.exists_temperedDistribution_tendsto_inv_add_mul_I
statement: formalized
---

# Sokhotski–Plemelj formula

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/distributions/sokhotski-plemelj-formula/index.html).

## The pairing with $(x + i\varepsilon)^{-1}$

For a real number $\varepsilon$ and a Schwartz
function $\phi : \mathbb{R} \to \mathbb{C}$, $u_{+,\varepsilon}(\phi)$ is the complex number
$\int_{\mathbb{R}} (x + i\varepsilon)^{-1}\phi(x)\, dx$.

The integral is the Lebesgue integral, taken to be $0$ when the integrand is not integrable;
this can happen only for $\varepsilon = 0$.

Formalized by `MathlibExt.Analysis.Distribution.PlemeljLimitTemperedDistributionWanted.uPlusEps`, a definition declared in [WantedExt/Analysis/Distribution/PlemeljLimitTemperedDistributionWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Distribution/PlemeljLimitTemperedDistributionWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/distributions/sokhotski-plemelj-formula/index.html#u-plus-eps).

## The pairing with $(x - i\varepsilon)^{-1}$

For a real number $\varepsilon$ and a Schwartz
function $\phi : \mathbb{R} \to \mathbb{C}$, $u_{-,\varepsilon}(\phi)$ is the complex number
$\int_{\mathbb{R}} (x - i\varepsilon)^{-1}\phi(x)\, dx$.

The integral is the Lebesgue integral, taken to be $0$ when the integrand is not integrable;
this can happen only for $\varepsilon = 0$.

Formalized by `MathlibExt.Analysis.Distribution.PlemeljLimitTemperedDistributionWanted.uMinusEps`, a definition declared in [WantedExt/Analysis/Distribution/PlemeljLimitTemperedDistributionWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Distribution/PlemeljLimitTemperedDistributionWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/distributions/sokhotski-plemelj-formula/index.html#u-minus-eps).

## The tempered distributions $(x \pm i\varepsilon)^{-1}$ converge as $\varepsilon \to 0^+$

Write $S(\mathbb{R})$ for the space of complex-valued Schwartz functions on $\mathbb{R}$, and for
$\varepsilon > 0$ and $\phi \in S(\mathbb{R})$ let
$u_{\pm,\varepsilon}(\phi) = \int_{\mathbb{R}} (x \pm i\varepsilon)^{-1}\phi(x)\, dx$. Then for
every $\varepsilon > 0$ both $u_{+,\varepsilon}$ and $u_{-,\varepsilon}$ are tempered
distributions, that is, continuous $\mathbb{C}$-linear functionals on $S(\mathbb{R})$, and there
are tempered distributions $u_+$ and $u_-$ such that $u_{+,\varepsilon}(\phi) \to u_+(\phi)$ and
$u_{-,\varepsilon}(\phi) \to u_-(\phi)$ as $\varepsilon \to 0^+$ for every $\phi \in S(\mathbb{R})$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Distributions, generalized functions, distribution spaces), problem `ma_proofbench_l2_15`.

Stated but not proved: `MathlibExt.Analysis.Distribution.PlemeljLimitTemperedDistributionWanted.exists_temperedDistribution_tendsto_inv_add_mul_I` is written with `theorem_wanted` in [WantedExt/Analysis/Distribution/PlemeljLimitTemperedDistributionWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Distribution/PlemeljLimitTemperedDistributionWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/distributions/sokhotski-plemelj-formula/index.html#exists-tempered-distribution-tendsto-inv).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sokhotski–Plemelj formula](https://deicyde.github.io/atlas-lean/roadmap/Analysis/distributions/sokhotski-plemelj-formula/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/distributions/sokhotski-plemelj-formula)
