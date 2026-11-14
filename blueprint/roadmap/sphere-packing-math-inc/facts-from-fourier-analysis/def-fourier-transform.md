---
declaration: definition
origin: cited
lean: Real.fourierIntegral
statement: formalized
---

# Fourier-Transform

The Fourier transform of an $L^1$-function $f:\mathbb{R}^d\to\mathbb{C}$ is defined as

$$
\mathcal{F}(f)(y) = \widehat{f}(y) := \int_{\mathbb{R}^d} f(x)e^{-2\pi i \langle x, y \rangle} \,\mathrm{d}x, \quad y \in \mathbb{R}^d
$$

where $\langle x, y \rangle = \frac12\|x\|^2 + \frac12\|y\|^2 - \frac12\|x - y\|^2$ is the standard scalar product in $\mathbb{R}^d$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Real.fourierIntegral`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/Real.fourierIntegral).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/fourier-analysis.tex, line 3](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/fourier-analysis.tex#L3)
