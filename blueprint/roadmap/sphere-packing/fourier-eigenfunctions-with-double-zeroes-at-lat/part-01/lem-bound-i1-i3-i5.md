---
declaration: lemma
origin: cited
lean: MagicFunction.a.IntegralEstimates.I₁.I₁'_bounding, MagicFunction.a.IntegralEstimates.I₃.I₃'_bounding, MagicFunction.a.IntegralEstimates.I₅.I₅'_bounding
statement: formalized
proof: formalized
---

# bound-I1-I3-I5

There exists $C > 0$ such that for all $r \geq 0$,

$$
|I_1(r)|, |I_3(r)|, |I_5(r)| \leq C \int_1^{\infty} e^{-2\pi s} \, e^{-\pi r / s} \, \mathrm{d} s.
$$

## Depends on

- [a-definition](def-a-definition.md)

## Proof

We only prove the bound for $I_1(r)$, as the other two are similar. By the change of variable $z = -1 + i t$ for $t \in [0,1]$, we have

$$
I_1(r) = -i \int_0^1 \phi_0\left(\frac{-1}{i t}\right) t^2 e^{-\pi i r} \cdot e^{-\pi r t} \, \mathrm{d} t.
$$

With the change of variable $s = 1 / t$, we get

$$
I_1(r) = -i \int_1^{\infty} \phi_0(i s) \cdot s^{-4} \cdot e^{-\pi i r} \cdot e^{-\pi r / s} \, \mathrm{d} s
$$

and, by the triangle inequality and monotonicity of the integral,

$$
|I_1(r)| \leq \int_1^{\infty} |\phi_0(i s)| \cdot s^{-4} \cdot |e^{-\pi i r}| \cdot e^{-\pi r / s} \, \mathrm{d} s \le \int_1^{\infty} |\phi_0(is)| \cdot e^{-\pi r / s} \, \mathrm{d} s.
$$

Now, Corollary [phi0-bound](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L138) shows

$$
|I_1(r)| \leq C_0 \int_1^{\infty} e^{-2\pi s} \, e^{-\pi r / s} \, \mathrm{d} s.
$$

## Lean

Formalized as [`MagicFunction.a.IntegralEstimates.I₁.I₁'_bounding`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.a.IntegralEstimates.I₁.I₁'_bounding), [`MagicFunction.a.IntegralEstimates.I₃.I₃'_bounding`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.a.IntegralEstimates.I₃.I₃'_bounding), [`MagicFunction.a.IntegralEstimates.I₅.I₅'_bounding`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.a.IntegralEstimates.I₅.I₅'_bounding).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/construct-a-b.tex, line 190](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L190)
