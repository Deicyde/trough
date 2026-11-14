---
declaration: theorem
origin: cited
lean: SchwartzMap.poissonSummation_lattice
statement: formalized
proof: formalized
---

# Poisson summation formula

Let $\Lambda$ be a lattice in $\mathbb{R}^d$, and let $f:\mathbb{R}^d\to\mathbb{R}$ be a Schwartz function. Then, for all $v \in \mathbb{R}^d$,

$$
\sum_{\ell\in\Lambda}f(\ell + v) = \frac{1}{\operatorname{Vol}\!\left(\mathbb{R}^d/\Lambda\right)} \sum_{m\in\Lambda^*}\widehat{f}(m)\, e^{2\pi i \left\langle v, m \right\rangle}.
$$

## Depends on

- [Fourier-Transform](def-fourier-transform.md)
- [Schwartz-Space](def-schwartz-space.md)
- [dual-lattice](../sphere-packings/def-dual-lattice.md)

## Lean

Formalized as [`SchwartzMap.poissonSummation_lattice`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SchwartzMap.poissonSummation_lattice).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/fourier-analysis.tex, line 48](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/fourier-analysis.tex#L48)
