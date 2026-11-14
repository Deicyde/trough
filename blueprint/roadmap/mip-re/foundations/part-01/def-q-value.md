---
declaration: definition
origin: cited
lean: MIPRE.TensorProductStrategy.value, MIPRE.quantumValue
statement: formalized
---

# Quantum value

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] The value of a tensor-product strategy $\mathscr{S} = (\mathcal{H}_\textsc{A},\mathcal{H}_\textsc{B},\psi,A,B)$ in $\mathfrak{G}$ is

$$
\mathrm{val}^*(\mathfrak{G}, \mathscr{S}) = \sum_{x, y, a, b} \mu(x,y)\, D(x,y,a,b)\,
\langle\psi| A^x_a \otimes B^y_b |\psi\rangle\;,
$$

and the *quantum value* $\mathrm{val}^*(\mathfrak{G})$ is the supremum of $\mathrm{val}^*(\mathfrak{G}, \mathscr{S})$ over all tensor-product strategies.

## Depends on

- [Tensor-product strategy](def-tensor-strategy.md)

## Lean

Formalized as [`MIPRE.TensorProductStrategy.value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TensorProductStrategy.value), [`MIPRE.quantumValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.quantumValue).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 165](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L165)
