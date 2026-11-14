---
declaration: lemma
origin: cited
lean: MIPRE.syncValue_le_quantumValue
statement: formalized
proof: formalized
---

# Synchronous value lower-bounds the quantum value

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] For every synchronous game $\mathfrak{G}$, ${\mathrm{val}^{s}}(\mathfrak{G}) \leq \mathrm{val}^*(\mathfrak{G})$.

## Depends on

- [Synchronous value](def-sync-value.md)
- [Quantum value](def-q-value.md)

## Proof

Given a synchronous strategy $\{M^x_a\}$ on $\mathbb{C}^d$, take the tensor-product strategy with $\mathcal{H}_\textsc{A} = \mathcal{H}_\textsc{B} = \mathbb{C}^d$, $A^x_a = M^x_a$, $B^y_b = (M^y_b)^{\mathsf{T}}$, and $|\psi\rangle = d^{-1/2}\sum_i |i\rangle|i\rangle$ (in Lean, `MIPRE.SyncStrategy.toTensorProductStrategy`). On that state $\langle\psi| M \otimes N |\psi\rangle = \operatorname{tr}(M N^{\mathsf{T}})/d$ (`MIPRE.dotProduct_kronecker_maxEntangled`), so with $N = (M^y_b)^{\mathsf{T}}$ the Born-rule probability is $\tau(M^x_a M^y_b)$ and the values agree (`MIPRE.SyncStrategy.value_toTensorProductStrategy`). Taking the supremum uses that the quantum value is a supremum over a possibly empty type with bounded range: `MIPRE.TensorProductStrategy.value_le_one` and `MIPRE.quantumValue_nonneg`, both proved from the Born rule.

## Lean

Formalized as [`MIPRE.syncValue_le_quantumValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.syncValue_le_quantumValue).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 263](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L263)
