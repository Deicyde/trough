---
declaration: theorem
origin: cited
lean: SchwartzMap.PoissonSummation_Lattices
statement: formalized
---

# Poisson summation formula

Let $\Lambda$ be a lattice in $\mathbb{R}^d$, and let $f:\mathbb{R}^d\to\mathbb{R}$ be a Schwartz function. Then, for all $v \in \mathbb{R}^d$,

$$
\sum_{\ell\in\Lambda}f(\ell + v) = \frac{1}{\operatorname{Vol}\!\left(\mathbb{R}^d/\Lambda\right)} \sum_{m\in\Lambda^*}\widehat{f}(m) e^{-2\pi i \left\langle v, m \right\rangle}.
$$

## Depends on

- [Fourier-Transform](def-fourier-transform.md)
- [Schwartz-Space](def-schwartz-space.md)
- [dual-lattice](../sphere-packings/def-dual-lattice.md)

## Proof

One possible proof would be by induction on $d$. However, there are numerous nuances involved, particularly in manipulating nested infinite sums. Ideas would be appreciated.

## Lean

Stated as [`SchwartzMap.PoissonSummation_Lattices`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SchwartzMap.PoissonSummation_Lattices); the blueprint marks no proof of it as formalized.

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/fourier-analysis.tex, line 86](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/fourier-analysis.tex#L86)
