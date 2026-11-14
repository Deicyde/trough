---
declaration: definition
origin: cited
lean: MIPRE.CommutingStrategy
statement: formalized
---

# Commuting strategy

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] A *commuting strategy* for a synchronous game $\mathfrak{G} = ({\mathcal{X}}, {\mathcal{A}}, \mu, D)$ is a unital $C^*$-algebra ${\mathscr{A}}$ with a tracial state $\tau$ (a positive linear functional with $\tau(1) = 1$ and $\tau(ab) = \tau(ba)$ for all $a, b \in {\mathscr{A}}$), together with a family of projective measurements $\{M^x_a\}_{a \in {\mathcal{A}}}$ in ${\mathscr{A}}$, one for each $x \in {\mathcal{X}}$: each $M^x_a$ is a self-adjoint idempotent and $\sum_a M^x_a = 1$.

Outcome probabilities are computed with $\tau$: the players answer $(a,b)$ to questions $(x,y)$ with probability $\tau(M^x_a M^y_b)$, a nonnegative real number since $\tau(M^x_a M^y_b) = \tau(M^x_a M^y_b M^x_a)$.

## Depends on

- [Synchronous game](def-sync-game.md)

## Lean

Formalized as [`MIPRE.CommutingStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingStrategy).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 84](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L84)
