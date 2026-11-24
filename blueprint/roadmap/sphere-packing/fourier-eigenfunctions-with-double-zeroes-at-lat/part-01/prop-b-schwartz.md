---
declaration: proposition
origin: cited
lean: MagicFunction.FourierEigenfunctions.b
statement: formalized
---

# b-schwartz

$b(x)$ is a Schwartz function.

## Depends on

Its statement uses no other node that has an article here.

## Proof

As for Proposition [a-schwartz](prop-a-schwartz.md): $b_\mathrm{rad}$ is smooth on $(-1, \infty)$ with all derivatives decaying rapidly on $[0, \infty)$, so Corollary [schwartz-of-nonneg-decay](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/fourier-analysis.tex#L187) with $\theta = -1$ shows that $b = b_\mathrm{rad}(\|\cdot\|^2)$ is Schwartz.

## Lean

Stated as [`MagicFunction.FourierEigenfunctions.b`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.FourierEigenfunctions.b); the blueprint marks no proof of it as formalized.

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/construct-a-b.tex, line 668](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L668)
