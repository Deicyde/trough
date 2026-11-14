---
declaration: definition
origin: cited
lean: MIPRE.hsInner, MIPRE.hsNormSq
statement: formalized
---

# Normalized Hilbert–Schmidt norm

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] For matrices $A, B \in \mathbb{C}^{d \times d}$, let $\langle A, B \rangle_{hs} = \tau(A^\dagger B)$ and $\left\| {A} \right\|_{hs}^2 = \tau(A^\dagger A)$, where $\tau = \operatorname{tr}/d$ is the dimension-normalized trace.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MIPRE.hsInner`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.hsInner), [`MIPRE.hsNormSq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.hsNormSq).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 482](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L482)
