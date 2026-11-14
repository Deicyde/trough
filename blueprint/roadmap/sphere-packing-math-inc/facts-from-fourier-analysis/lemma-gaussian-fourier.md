---
declaration: lemma
origin: cited
lean: fourier_gaussian_innerProductSpace
statement: formalized
proof: formalized
---

# Gaussian-Fourier

$$
\mathcal{F}(e^{\pi i \|x\|^2 z})(y) = z^{-4}\,e^{\pi i \|y\|^2 \,(\frac{-1}{z}) }.
$$

## Depends on

- [Fourier-Transform](def-fourier-transform.md)

## Proof

This is implemented in Lean via the Gaussian Fourier transform lemma `fourier_gaussian_innerProductSpace`.

## Lean

Formalized as [`fourier_gaussian_innerProductSpace`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/fourier_gaussian_innerProductSpace).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/fourier-analysis.tex, line 15](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/fourier-analysis.tex#L15)
