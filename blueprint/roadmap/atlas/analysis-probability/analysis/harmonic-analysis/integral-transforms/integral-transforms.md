---
declaration: section
origin: cited
lean: MetaMathlibExt.Ramanujan_master_theorem
statement: formalized
---

# Integral transforms and moment problems: its own results

1 result, 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/index.html).

Laplace, Mellin and Radon transforms (Ramanujan's master theorem, Fourier slice theorem) and Hausdorff moment problems.

## Ramanujan's master theorem

Let $a$ and $b$ be real numbers with $0 < a < b$, and let
$s$ be a complex number with $a < \operatorname{Re} s < b$. Let $\varphi$ be a function from
$\mathbb{C}$ to $\mathbb{C}$ that is analytic on the half-plane $\operatorname{Re} z > -b$, and
suppose there are real constants $C > 0$ and $P < \pi$ such that
$|\varphi(u + iv)| \le C e^{P|v|}$ for all real $u$ and $v$ with $u > -b$. Let $F$ be a function
from $\mathbb{R}$ to $\mathbb{C}$ such that for every real $x > 0$ the series
$\sum_{k=0}^{\infty} \varphi(k)\,(-x)^k / k!$ converges unconditionally to $F(x)$, and suppose
that $x \mapsto x^{s-1} F(x)$ is Lebesgue integrable on $(0, \infty)$, where
$x^{s-1} = e^{(s-1)\log x}$. Then

$$\int_0^\infty x^{s-1} F(x)\,dx = \Gamma(s)\,\varphi(-s).$$

This is a specialization of the theorem: the growth bound on $\varphi$ is uniform in
$\operatorname{Re} z$, and integrability of $x^{s-1} F(x)$ is assumed rather than derived.

## Sources

- https://en.wikipedia.org/wiki/Ramanujan%27s_master_theorem (Raw: `int_0^infty x^{s-1} sum_k phi(k)(-x)^k/k! dx = Gamma(s) phi(-s)`.)

Stated but not proved: `MetaMathlibExt.Ramanujan_master_theorem` is written with `theorem_wanted` in [WantedExt/Analysis/SpecialFunctions/RamanujanMasterTheoremWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SpecialFunctions/RamanujanMasterTheoremWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/index.html#ramanujan-master-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integral transforms and moment problems](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/harmonic-analysis/integral-transforms)
