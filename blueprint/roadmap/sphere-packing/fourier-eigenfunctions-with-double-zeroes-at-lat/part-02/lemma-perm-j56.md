---
declaration: lemma
origin: cited
lean: MagicFunction.b.Fourier.perm_J₅
statement: formalized
---

# perm-J56

[(39)](../part-01/README.md) holds: $\mathcal{F}(J_5) = -J_6$.

## Depends on

- [b-definition](../part-01/def-b-definition.md)
- [psi-slash-relations](../part-01/lemma-psi-slash-relations.md)
- [b-schwartz](../part-01/prop-b-schwartz.md)

## Proof

As in Lemma [perm-I56](../part-01/lemma-perm-i56.md), using the definition [(20)](../part-01/def-psii-psit-psis.md) in the form $\psi_I(-1/w)\, w^2 = \psi_S(w)$. The substitution $w = -1/z$ maps the contour of $J_5$ onto that of $J_6$ with reversed orientation, whence the sign.

## Lean

Stated as [`MagicFunction.b.Fourier.perm_J₅`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.b.Fourier.perm_J₅); the blueprint marks no proof of it as formalized.

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/construct-a-b.tex, line 691](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L691)
