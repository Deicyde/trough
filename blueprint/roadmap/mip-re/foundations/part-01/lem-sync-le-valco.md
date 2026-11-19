---
declaration: lemma
origin: cited
lean: MIPRE.syncValue_le_commValue
statement: formalized
proof: formalized
---

# Synchronous value lower-bounds the commuting value

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] For every synchronous game $\mathfrak{G}$, ${\mathrm{val}^{s}}(\mathfrak{G}) \leq {\mathrm{val}^{\mathrm{co}}}(\mathfrak{G})$.

## Depends on

- [Synchronous value](def-sync-value.md)
- [Commuting value](def-commuting-value.md)

## Proof

A synchronous strategy $(d, M)$ is a commuting strategy with ${\mathscr{A}} = \mathbb{C}^{d \times d}$ and $\tau = \operatorname{tr}/d$, with the same value (in Lean, `MIPRE.SyncStrategy.toCommutingStrategy`; the value is preserved by definitional equality).

## Lean

Formalized as [`MIPRE.syncValue_le_commValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.syncValue_le_commValue).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 292](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L292)
