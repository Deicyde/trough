---
declaration: lemma
origin: cited
lean: MagicFunction.a.IntegralEstimates.I₂.I₂'_bounding, MagicFunction.a.IntegralEstimates.I₄.I₄'_bounding, MagicFunction.a.IntegralEstimates.I₆.I₆'_bounding
statement: formalized
---

# bound-I2-I4-I6

There exist $C_1, C_2 > 0$ such that for all $r \geq 0$,

$$
|I_2(r)|, |I_4(r)| \leq C_1 e^{-\pi r}
$$

and

$$
|I_6(r)| \leq C_2 \frac{e^{-\pi(r + 2)}}{r + 2}
$$

## Depends on

- [a-definition](def-a-definition.md)

## Proof

For $I_2(r)$, parametrize $z$ as $z = t + i$ for $t \in [-1,0]$, and we have

$$
I_2(r) = \int_{-1}^0 \phi_0\left(\frac{-1}{t + 1 + i}\right) (t + 1 + i)^2 e^{\pi i r t} e^{-\pi r} \, \mathrm{d} t.
$$

Since the function $z \mapsto \phi_0\left(\frac{-1}{z+1}\right) (z+1)^2$ is holomorphic and bounded on the contour, there exists $C > 0$ such that $|\phi_0\left(\frac{-1}{z+1}\right) (z + 1)^2| \leq C$, and the absolute value of the integral can be bounded by

$$
|I_2(r)| \le \int_{-1}^{0} C e^{-\pi r} \, \mathrm{d} t = C e^{-\pi r}.
$$

The bound for $I_4(r)$ is similar. For $I_6(r)$, parametrize $z$ as $z = i t$ for $t \in [1, \infty)$, and we have

$$
I_6(r) = 2 i \int_1^{\infty} \phi_0(i t) e^{-\pi r t} \, \mathrm{d} t
$$

and the absolute value can be bounded as (using Corollary [phi0-bound](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L138))

$$
|I_6(r)| \leq 2 \int_1^{\infty} |\phi_0(i t)| e^{-\pi r t} \, \mathrm{d} t \leq 2C_0 \int_1^{\infty} e^{-2\pi t} e^{-\pi r t} \, \mathrm{d} t = \frac{2C_0}{\pi} \frac{e^{-\pi (r + 2)}}{r + 2}.
$$

## Lean

Stated as [`MagicFunction.a.IntegralEstimates.I₂.I₂'_bounding`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.a.IntegralEstimates.I₂.I₂'_bounding), [`MagicFunction.a.IntegralEstimates.I₄.I₄'_bounding`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.a.IntegralEstimates.I₄.I₄'_bounding), [`MagicFunction.a.IntegralEstimates.I₆.I₆'_bounding`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.a.IntegralEstimates.I₆.I₆'_bounding); the blueprint marks no proof of it as formalized.

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/construct-a-b.tex, line 217](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L217)
