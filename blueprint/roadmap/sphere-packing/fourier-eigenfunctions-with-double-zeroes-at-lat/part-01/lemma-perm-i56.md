---
declaration: lemma
origin: cited
lean: MagicFunction.a.Fourier.perm_I₅
statement: formalized
---

# perm-I56

[(16)](README.md) holds: $\mathcal{F}(I_5) = I_6$.

## Depends on

- [a-definition](def-a-definition.md)
- [phi0-transform](lemma-phi0-transform.md)
- [a-schwartz](prop-a-schwartz.md)

## Proof

As in Lemma [perm-I12](lemma-perm-i12.md), exchange the integrals and apply Lemma [Gaussian-Fourier](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/fourier-analysis.tex#L15), then substitute $w = -1/z$. Here no contour deformation is needed: the substitution maps the segment from $0$ to $i$ onto the ray from $i\infty$ to $i$, reversing orientation, and

$$
-2\,\phi_0\left(\frac{-1}{z}\right) z^2\, z^{-4}\, e^{\pi i \|\xi\|^2(\frac{-1}{z})}\,\mathrm{d} z \;\longmapsto\; 2\,\phi_0(w)\, e^{\pi i \|\xi\|^2 w}\,\mathrm{d} w,
$$

which is the integrand of $I_6$.

## Lean

Stated as [`MagicFunction.a.Fourier.perm_I₅`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.a.Fourier.perm_I₅); the blueprint marks no proof of it as formalized.

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/construct-a-b.tex, line 325](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L325)
