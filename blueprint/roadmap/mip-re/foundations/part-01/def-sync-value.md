---
declaration: definition
origin: cited
lean: MIPRE.SyncStrategy.value, MIPRE.syncValue
statement: formalized
---

# Synchronous value

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] The value of a synchronous strategy $\mathscr{S} = (d, M)$ in $\mathfrak{G}$ is

$$
{\mathrm{val}^{s}}(\mathfrak{G}, \mathscr{S}) = \sum_{x, y, a, b} \mu(x,y)\, D(x,y,a,b)\,
\tau\bigl(M^x_a M^y_b\bigr)\;,
$$

and the *synchronous value* of $\mathfrak{G}$ is ${\mathrm{val}^{s}}(\mathfrak{G}) = \sup_\mathscr{S} {\mathrm{val}^{s}}(\mathfrak{G}, \mathscr{S})$.

## Depends on

- [Synchronous strategy](def-sync-strategy.md)

## Lean

Formalized as [`MIPRE.SyncStrategy.value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SyncStrategy.value), [`MIPRE.syncValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.syncValue).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 182](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L182)
