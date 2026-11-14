---
declaration: lemma
origin: cited
lean: SpherePacking.Dim24.f_zero, SpherePacking.Dim24.fourier_f_zero, SpherePacking.Dim24.f_real, SpherePacking.Dim24.f_real_fourier, SpherePacking.Dim24.fRadial_sqrtTwo, SpherePacking.Dim24.fRadial_hasDerivAt_sqrtTwo, SpherePacking.Dim24.fRadial_two, SpherePacking.Dim24.fRadial_hasDerivAt_two, SpherePacking.Dim24.fhatRadial_sqrtTwo, SpherePacking.Dim24.fhatRadial_hasDerivAt_sqrtTwo, SpherePacking.Dim24.fhatRadial_two
statement: formalized
proof: formalized
---

# f-basic-d24

The function $f$ is a radial Schwartz function $\mathbb{R}^{24}\to\mathbb{R}$ with $f(0)=\widehat f(0)=1$. Moreover, $f$ and $\widehat f$ have roots at all radii $\sqrt{2k}$ for integers $k\ge 2$; these roots are double except for the root of $f$ at $2$.

## Depends on

- [f-d24](def-f-d24.md)
- [plusone-d24](../part-01/lem-plusone-d24.md)
- [minusone-d24](../part-01/lem-minusone-d24.md)
- [a-zeros-values-d24](../part-01/lem-a-zeros-values-d24.md)
- [b-zeros-values-d24](lem-b-zeros-values-d24.md)

## Lean

Formalized as [`SpherePacking.Dim24.f_zero`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.Dim24.f_zero), [`SpherePacking.Dim24.fourier_f_zero`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.Dim24.fourier_f_zero), [`SpherePacking.Dim24.f_real`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.Dim24.f_real), [`SpherePacking.Dim24.f_real_fourier`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.Dim24.f_real_fourier), [`SpherePacking.Dim24.fRadial_sqrtTwo`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.Dim24.fRadial_sqrtTwo), [`SpherePacking.Dim24.fRadial_hasDerivAt_sqrtTwo`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.Dim24.fRadial_hasDerivAt_sqrtTwo), [`SpherePacking.Dim24.fRadial_two`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.Dim24.fRadial_two), [`SpherePacking.Dim24.fRadial_hasDerivAt_two`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.Dim24.fRadial_hasDerivAt_two), [`SpherePacking.Dim24.fhatRadial_sqrtTwo`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.Dim24.fhatRadial_sqrtTwo), [`SpherePacking.Dim24.fhatRadial_hasDerivAt_sqrtTwo`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.Dim24.fhatRadial_hasDerivAt_sqrtTwo), [`SpherePacking.Dim24.fhatRadial_two`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.Dim24.fhatRadial_two).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/dim24-proof.tex, line 10](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/dim24-proof.tex#L10)
