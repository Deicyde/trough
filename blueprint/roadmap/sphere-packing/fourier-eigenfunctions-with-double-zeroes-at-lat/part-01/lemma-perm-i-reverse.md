---
declaration: lemma
origin: cited
lean: MagicFunction.a.Fourier.perm_₃_I₄, MagicFunction.a.Fourier.perm_I₆
statement: formalized
proof: formalized
---

# perm-I-reverse

$\mathcal{F}(I_3 + I_4) = I_1 + I_2$ and $\mathcal{F}(I_6) = I_5$.

## Depends on

- [perm-I12](lemma-perm-i12.md)
- [perm-I56](lemma-perm-i56.md)
- [radial-fourier-inversion](../../facts-from-fourier-analysis/lemma-radial-fourier-inversion.md)

## Proof

The functions $I_1 + I_2$ and $I_5$ (as functions on $\mathbb{R}^8$) are radial Schwartz functions, so $\mathcal{F}^2$ fixes them (Lemma [radial-fourier-inversion](../../facts-from-fourier-analysis/lemma-radial-fourier-inversion.md)). Applying $\mathcal{F}$ to [(15)](README.md) and [(16)](README.md) gives the claim.

## Lean

Formalized as [`MagicFunction.a.Fourier.perm_₃_I₄`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.a.Fourier.perm_₃_I₄), [`MagicFunction.a.Fourier.perm_I₆`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.a.Fourier.perm_I₆).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/construct-a-b.tex, line 336](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L336)
