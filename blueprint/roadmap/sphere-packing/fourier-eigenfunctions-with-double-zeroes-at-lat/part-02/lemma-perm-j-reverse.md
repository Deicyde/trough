---
declaration: lemma
origin: cited
lean: MagicFunction.b.Fourier.perm_₃_J₄, MagicFunction.b.Fourier.perm_J₆
statement: formalized
proof: formalized
---

# perm-J-reverse

$\mathcal{F}(J_3 + J_4) = -(J_1 + J_2)$ and $\mathcal{F}(J_6) = -J_5$.

## Depends on

- [perm-J12](../part-01/lemma-perm-j12.md)
- [perm-J56](lemma-perm-j56.md)
- [radial-fourier-inversion](../../facts-from-fourier-analysis/lemma-radial-fourier-inversion.md)

## Proof

Apply $\mathcal{F}$ to [(38)](../part-01/README.md) and [(39)](../part-01/README.md) and use $\mathcal{F}^2 = \mathrm{id}$ on radial Schwartz functions (Lemma [radial-fourier-inversion](../../facts-from-fourier-analysis/lemma-radial-fourier-inversion.md)).

## Lean

Formalized as [`MagicFunction.b.Fourier.perm_₃_J₄`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.b.Fourier.perm_₃_J₄), [`MagicFunction.b.Fourier.perm_J₆`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.b.Fourier.perm_J₆).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/construct-a-b.tex, line 698](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L698)
