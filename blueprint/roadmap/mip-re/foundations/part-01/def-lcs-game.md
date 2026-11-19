---
declaration: definition
origin: cited
lean: MIPRE.LCS.Layout.Question, MIPRE.LCS.Layout.Answer, MIPRE.LCS.Layout.questionDist, MIPRE.LCS.Game.accepts, MIPRE.LCS.Game.toNonlocalGame
statement: formalized
---

# LCS game

The *nonlocal game* of an LCS instance. Both players receive questions from the same alphabet — an equation or a variable — and answer in the same alphabet — an assignment to all the variables, or a single bit. The referee samples an equation $i$ uniformly at random, a uniformly random variable $j \in V_i$, and a uniform *orientation*: one player is asked $i$ and the other $j$. The player asked the equation answers an assignment $a$ (only its restriction to $V_i$ is read), the player asked the variable answers a bit $c$, and they win if $\sum_{k \in V_i} a_k = b_i$ and $a_j = c$. An answer whose shape does not match its question loses, as does an off-support pair $j \notin V_i$.

## Depends on

- [LCS instance](def-lcs-instance.md)
- [Nonlocal game](def-game.md)

## Lean

Formalized as [`MIPRE.LCS.Layout.Question`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.Layout.Question), [`MIPRE.LCS.Layout.Answer`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.Layout.Answer), [`MIPRE.LCS.Layout.questionDist`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.Layout.questionDist), [`MIPRE.LCS.Game.accepts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.Game.accepts), [`MIPRE.LCS.Game.toNonlocalGame`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LCS.Game.toNonlocalGame).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 333](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L333)
