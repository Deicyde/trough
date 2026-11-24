---
declaration: proposition
origin: cited
lean: MagicFunction.b.Fourier.eig_b
statement: formalized
proof: formalized
---

# b-fourier

$b(x)$ satisfies [(2)](../README.md).

## Depends on

- [b-definition](../part-01/def-b-definition.md)
- [b-schwartz](../part-01/prop-b-schwartz.md)
- [perm-J12](../part-01/lemma-perm-j12.md)
- [perm-J56](lemma-perm-j56.md)
- [perm-J-reverse](lemma-perm-j-reverse.md)

## Proof

By linearity, Lemmas [perm-J12](../part-01/lemma-perm-j12.md), [perm-J56](lemma-perm-j56.md) and [perm-J-reverse](lemma-perm-j-reverse.md) give

$$
\mathcal{F}(b) = -(J_3 + J_4) - (J_1 + J_2) - J_6 - J_5 = -b.
$$

## Lean

Formalized as [`MagicFunction.b.Fourier.eig_b`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.b.Fourier.eig_b).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/construct-a-b.tex, line 705](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L705)
