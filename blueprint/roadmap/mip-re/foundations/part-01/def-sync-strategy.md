---
declaration: definition
origin: cited
lean: MIPRE.SyncStrategy
statement: formalized
---

# Synchronous strategy

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] A *synchronous strategy* for a synchronous game $\mathfrak{G} = ({\mathcal{X}}, {\mathcal{A}}, \mu, D)$ is a dimension $d \geq 1$ together with a family of projective measurements (PVMs) $\{M^x_a\}_{a \in {\mathcal{A}}}$ on $\mathbb{C}^d$, one for each $x \in {\mathcal{X}}$: each $M^x_a$ is an orthogonal projection and $\sum_a M^x_a = {I}$.

Outcome probabilities are computed with the tracial state $\tau(M) = \operatorname{tr}(M)/d$: the players answer $(a,b)$ to questions $(x,y)$ with probability $\tau(M^x_a M^y_b)$.

## Depends on

- [Synchronous game](def-sync-game.md)

## Lean

Formalized as [`MIPRE.SyncStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SyncStrategy).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 67](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L67)
