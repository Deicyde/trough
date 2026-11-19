---
declaration: definition
origin: cited
lean: FourierTransform.fourier
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

Formalized as [`FourierTransform.fourier`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/FourierTransform.fourier).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/fourier-analysis.tex, line 3](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/fourier-analysis.tex#L3)
