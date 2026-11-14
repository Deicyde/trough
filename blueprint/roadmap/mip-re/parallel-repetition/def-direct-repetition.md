---
declaration: definition
origin: cited
lean: MIPRE.Game.repeat, MIPRE.SynchronousGame.repeat
statement: formalized
---

# Direct repetition

Let $\mathfrak{G} = ({\mathcal{X}}, {\mathcal{Y}}, {\mathcal{A}}, {\mathcal{B}}, \mu, D)$ be a game and $n \geq 0$ an integer. The *$n$-fold direct repetition* of $\mathfrak{G}$ is the game $\mathfrak{G}^{n}$ with question alphabets ${\mathcal{X}}^n$, ${\mathcal{Y}}^n$ and answer alphabets ${\mathcal{A}}^n$, ${\mathcal{B}}^n$, question distribution $\mu^{n}(\bar{x}, \bar{y}) = \prod_{i=1}^{n} \mu(x_i, y_i)$, and decision predicate $D^{n}(\bar{x}, \bar{y}, \bar{a}, \bar{b}) = \bigwedge_{i=1}^{n} D(x_i, y_i, a_i, b_i)$. The direct repetition of a synchronous game is synchronous, with the same data.

## Depends on

- [Nonlocal game](../foundations/part-01/def-game.md)
- [Synchronous game](../foundations/part-01/def-sync-game.md)

## Lean

Formalized as [`MIPRE.Game.repeat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Game.repeat), [`MIPRE.SynchronousGame.repeat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SynchronousGame.repeat).

## Sources

- [MIP* = RE blueprint: content/05_parallel_repetition.tex, line 41](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/05_parallel_repetition.tex#L41)
