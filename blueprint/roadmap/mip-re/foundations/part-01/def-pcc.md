---
declaration: definition
origin: cited
lean: MIPRE.SyncStrategy.IsPCC
statement: formalized
---

# PCC strategy

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] A synchronous strategy $\mathscr{S} = (d, M)$ for a synchronous game $\mathfrak{G} = ({\mathcal{X}}, {\mathcal{A}}, \mu, D)$ is *PCC* (*projective, consistent, and commuting*, following (JNVWY20, Section 5.2)) if the measurements associated with any pair of questions asked with positive probability commute: for all $(x, y)$ in the support of $\mu$,

$$
M^x_a M^y_b = M^y_b M^x_a \qquad \text{for all } a, b \in {\mathcal{A}}\;.
$$

## Depends on

- [Synchronous strategy](def-sync-strategy.md)

## Lean

Formalized as [`MIPRE.SyncStrategy.IsPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SyncStrategy.IsPCC).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 110](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L110)
