---
declaration: definition
origin: cited
lean: MIPRE.SynchronousGame, MIPRE.SynchronousGame.toGame
statement: formalized
---

# Synchronous game

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] A game is *synchronous* if ${\mathcal{X}} = {\mathcal{Y}}$, ${\mathcal{A}} = {\mathcal{B}}$, and unequal answers to equal questions are rejected: $D(x,x,a,b) = 0$ whenever $a \neq b$. We write a synchronous game as $\mathfrak{G} = ({\mathcal{X}}, {\mathcal{A}}, \mu, D)$.

## Depends on

- [Nonlocal game](def-game.md)

## Lean

Formalized as [`MIPRE.SynchronousGame`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SynchronousGame), [`MIPRE.SynchronousGame.toGame`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SynchronousGame.toGame).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 34](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L34)
