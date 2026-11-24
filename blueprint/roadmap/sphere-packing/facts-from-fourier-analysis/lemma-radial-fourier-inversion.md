---
declaration: lemma
origin: cited
lean: MagicFunction.a.Fourier.radial_inversion
statement: formalized
proof: formalized
---

# radial-fourier-inversion

If $f : \mathbb{R}^d \to \mathbb{C}$ is an even Schwartz function — in particular, if $f$ is radial — then $\mathcal{F}(\mathcal{F}(f)) = f$.

## Depends on

- [fourier-involution](lemma-fourier-involution.md)

## Proof

Immediate from Lemma [fourier-involution](lemma-fourier-involution.md), since $f(-x) = f(x)$.

## Lean

Formalized as [`MagicFunction.a.Fourier.radial_inversion`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.a.Fourier.radial_inversion).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/fourier-analysis.tex, line 63](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/fourier-analysis.tex#L63)
