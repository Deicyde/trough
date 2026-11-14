---
declaration: definition
origin: cited
lean: MIPRE.CommutingOperatorStrategy
statement: formalized
---

# Commuting-operator strategy

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] A *commuting-operator strategy* for $\mathfrak{G}$ consists of a Hilbert space $\mathcal{H}$ (a complete inner product space over $\mathbb{C}$, of any dimension), a unit vector $|\psi\rangle \in \mathcal{H}$, and POVMs $\{E^x_a\}_{a \in {\mathcal{A}}}$ and $\{F^y_b\}_{b \in {\mathcal{B}}}$ on $\mathcal{H}$, one for each $x$ (resp. $y$) — each $E^x_a$ and $F^y_b$ is a positive bounded operator, $\sum_a E^x_a = {I}$ and $\sum_b F^y_b = {I}$ — such that $E^x_a F^y_b = F^y_b E^x_a$ for all $x, y, a, b$. The players answer $(a, b)$ to questions $(x, y)$ with probability $\langle\psi| E^x_a F^y_b |\psi\rangle$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MIPRE.CommutingOperatorStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy).

## Sources

- [MIP* = RE blueprint: content/05_parallel_repetition.tex, line 60](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/05_parallel_repetition.tex#L60)
