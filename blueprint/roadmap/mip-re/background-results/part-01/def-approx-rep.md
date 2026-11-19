---
declaration: definition
origin: cited
lean: MIPRE.IsApproxRepresentation
statement: formalized
---

# Approximate representation

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] Let $G$ be a finite group and $\varepsilon \in \mathbb{R}$. An *$\varepsilon$-approximate representation* of $G$ is a function $f : G \to U(d)$ such that

$$
\mathop{\mathbb{E}}_{x, y \sim G} \, \mathrm{Re}\, \langle f(x) f(y), f(xy) \rangle_{hs}
\geq 1 - \varepsilon\;,
$$

where $\langle \cdot, \cdot \rangle_{hs}$ is the normalized Hilbert–Schmidt inner product of Definition [Normalized Hilbert–Schmidt norm](../../foundations/part-02/def-hs-norm.md). Since each value of $f$ is unitary, $\left\| {f(x) f(y) - f(xy)} \right\|_{hs}^2 = 2 - 2\, \mathrm{Re}\, \langle f(x) f(y), f(xy) \rangle_{hs}$, so the condition is equivalent to the defect form $\mathop{\mathbb{E}}_{x, y \sim G} \left\| {f(x) f(y) - f(xy)} \right\|_{hs}^2 \leq 2 \varepsilon$.

## Depends on

- [Normalized Hilbert–Schmidt norm](../../foundations/part-02/def-hs-norm.md)

## Lean

Formalized as [`MIPRE.IsApproxRepresentation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsApproxRepresentation).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 63](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L63)
