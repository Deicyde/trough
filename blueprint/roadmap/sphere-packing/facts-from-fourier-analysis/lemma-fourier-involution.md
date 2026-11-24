---
declaration: lemma
origin: cited
lean: MagicFunction.a.Fourier.fourier_involution
statement: formalized
proof: formalized
---

# fourier-involution

For every Schwartz function $f : \mathbb{R}^d \to \mathbb{C}$ and every $x \in \mathbb{R}^d$,

$$
\mathcal{F}(\mathcal{F}(f))(x) = f(-x).
$$

## Depends on

- [Schwartz-Space](def-schwartz-space.md)
- [Fourier-transform-is-automorphism](lemma-fourier-transform-is-automorphism.md)

## Proof

Schwartz functions are integrable with integrable Fourier transforms, so the Fourier inversion theorem (together with the identity $\mathcal{F}^{-1}(f)(x) = \mathcal{F}(f)(-x)$) applies.

## Lean

Formalized as [`MagicFunction.a.Fourier.fourier_involution`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.a.Fourier.fourier_involution).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/fourier-analysis.tex, line 53](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/fourier-analysis.tex#L53)
