---
declaration: theorem
origin: cited
lean: g, g_zero, fourier_g_zero, MagicFunction.g.CohnElkies.g_cohnElkies₁, MagicFunction.g.CohnElkies.g_cohnElkies₂
statement: formalized
proof: formalized
---

# g

There exists a radial Schwartz function $g:\mathbb{R}^8\to\mathbb{R}$ which satisfies:

$$
\begin{aligned}
g(x)&\leq 0\mbox{ for } \|x\|\geq \sqrt{2}\qquad\text{(5)}\\
\widehat{g}(x)&\geq0\mbox{ for all } x\in\mathbb{R}^8\qquad\text{(6)}\\
g(0)&=\widehat{g}(0)=1.\qquad\text{(7)}\end{aligned}
$$

## Depends on

- [g1](../proof-of-theorem-g/thm-g1.md)

## Proof

Theorem [Cohn–Elkies (ElkiesCohn)](thm-cohn-elkies-general.md) applied to the optimal function $f(x)=g(x/\sqrt{2})$ immediately implies [Corollary MainTheorem-d8](../sphere-packings/maintheorem-d8.md).

## Lean

Formalized as [`g`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/g), [`g_zero`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/g_zero), [`fourier_g_zero`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/fourier_g_zero), [`MagicFunction.g.CohnElkies.g_cohnElkies₁`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.g.CohnElkies.g_cohnElkies₁), [`MagicFunction.g.CohnElkies.g_cohnElkies₂`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.g.CohnElkies.g_cohnElkies₂).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/cohn-elkies.tex, line 44](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/cohn-elkies.tex#L44)
