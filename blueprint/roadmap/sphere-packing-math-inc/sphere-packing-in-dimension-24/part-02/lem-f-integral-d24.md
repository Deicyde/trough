---
declaration: lemma
origin: cited
lean: SpherePacking.Dim24.LaplaceTmp.f_eq_laplace_A, SpherePacking.Dim24.LaplaceTmp.fourier_f_eq_laplace_B
statement: formalized
proof: formalized
---

# f-integral-d24

For $r>2$,

$$
f(r)=\sin\!\left(\frac{\pi r^2}{2}\right)^{\!2}\int_{0}^{\infty}A(t)e^{-\pi r^2 t}\,dt
\qquad\text{and}\qquad
\widehat f(r)=\sin\!\left(\frac{\pi r^2}{2}\right)^{\!2}\int_{0}^{\infty}B(t)e^{-\pi r^2 t}\,dt.
$$

## Depends on

- [f-d24](def-f-d24.md)
- [A-d24](def-a-d24.md)
- [B-d24](def-b-d24.md)

## Lean

Formalized as [`SpherePacking.Dim24.LaplaceTmp.f_eq_laplace_A`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.Dim24.LaplaceTmp.f_eq_laplace_A), [`SpherePacking.Dim24.LaplaceTmp.fourier_f_eq_laplace_B`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.Dim24.LaplaceTmp.fourier_f_eq_laplace_B).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/dim24-proof.tex, line 31](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/dim24-proof.tex#L31)
