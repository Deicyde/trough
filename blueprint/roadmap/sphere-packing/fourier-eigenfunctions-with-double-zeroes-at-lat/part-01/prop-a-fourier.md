---
declaration: proposition
origin: cited
lean: MagicFunction.a.Fourier.eig_a
statement: formalized
proof: formalized
---

# a-fourier

$a(x)$ satisfies [(1)](../README.md).

## Depends on

- [a-definition](def-a-definition.md)
- [a-schwartz](prop-a-schwartz.md)
- [perm-I12](lemma-perm-i12.md)
- [perm-I56](lemma-perm-i56.md)
- [perm-I-reverse](lemma-perm-i-reverse.md)

## Proof

By linearity of $\mathcal{F}$ on the Schwartz space,

$$
\mathcal{F}(a) = \mathcal{F}(I_1 + I_2) + \mathcal{F}(I_3 + I_4) + \mathcal{F}(I_5) + \mathcal{F}(I_6)
= (I_3 + I_4) + (I_1 + I_2) + I_6 + I_5 = a
$$

by Lemmas [perm-I12](lemma-perm-i12.md), [perm-I56](lemma-perm-i56.md) and [perm-I-reverse](lemma-perm-i-reverse.md).

## Lean

Formalized as [`MagicFunction.a.Fourier.eig_a`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.a.Fourier.eig_a).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/construct-a-b.tex, line 343](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L343)
