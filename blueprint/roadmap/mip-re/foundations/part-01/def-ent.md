---
declaration: definition
origin: cited
lean: MIPRE.entRequirement
statement: formalized
---

# Entanglement requirement

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] For a game $\mathfrak{G}$ and $\nu \in [0,1]$, $\mathrm{Ent}(\mathfrak{G}, \nu)$ is the least $d$ such that there exists a synchronous strategy (Definition [Synchronous strategy](def-sync-strategy.md)) with dimension at most $d$ achieving value at least $\nu$ in $\mathfrak{G}$, and $\infty$ if no synchronous strategy achieves $\nu$.

## Depends on

- [Synchronous value](def-sync-value.md)

## Lean

Formalized as [`MIPRE.entRequirement`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.entRequirement).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 249](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L249)
