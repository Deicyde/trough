---
declaration: lemma
origin: cited
lean: MagicFunction.b.Fourier.perm_J₁_J₂
statement: formalized
---

# perm-J12

[(38)](README.md) holds: $\mathcal{F}(J_1 + J_2) = -(J_3 + J_4)$.

## Depends on

- [b-definition](def-b-definition.md)
- [psi-slash-relations](lemma-psi-slash-relations.md)
- [b-schwartz](prop-b-schwartz.md)

## Proof

As in Lemma [perm-I12](lemma-perm-i12.md), we exchange the Fourier integral with the contour integral (absolute convergence follows from the bounds above), apply Lemma [Gaussian-Fourier](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/fourier-analysis.tex#L15), and substitute $w = -1/z$. Here the relevant transformation law is [(26)](lemma-psi-slash-relations.md): $\psi_T(-1/w)\, w^2 = -\psi_T(w)$, so the integrand becomes $-\psi_T(w)\, e^{\pi i \|\xi\|^2 w}$, and the same contour deformation as in Lemma [perm-I12](lemma-perm-i12.md) identifies the result with $-(J_3 + J_4)$.

## Lean

Stated as [`MagicFunction.b.Fourier.perm_J₁_J₂`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.b.Fourier.perm_J₁_J₂); the blueprint marks no proof of it as formalized.

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/construct-a-b.tex, line 684](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L684)
