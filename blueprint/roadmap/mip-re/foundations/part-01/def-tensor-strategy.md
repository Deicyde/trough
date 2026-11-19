---
declaration: definition
origin: cited
lean: MIPRE.TensorProductStrategy
statement: formalized
---

# Tensor-product strategy

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] A *tensor-product strategy* for $\mathfrak{G}$ consists of finite-dimensional Hilbert spaces $\mathcal{H}_\text{A}$, $\mathcal{H}_\text{B}$, a unit vector $|\psi\rangle \in \mathcal{H}_\text{A} \otimes \mathcal{H}_\text{B}$, and projective measurements (PVMs) $\{A^x_a\}$ on $\mathcal{H}_\text{A}$ and $\{B^y_b\}$ on $\mathcal{H}_\text{B}$, one for each $x$ (resp. $y$): each $A^x_a$ is an orthogonal projection and $\sum_a A^x_a = {I}$.

Outcome probabilities are computed using the Born rule: the players answer $(a,b)$ to questions $(x,y)$ with probability $\langle\psi| A^x_a \otimes B^y_b |\psi\rangle$. Restricting to projective measurements follows (1); by Naimark dilation, allowing general POVMs would define the same quantum value.

## Depends on

- [Nonlocal game](def-game.md)

## Lean

Formalized as [`MIPRE.TensorProductStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TensorProductStrategy).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 48](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L48)
