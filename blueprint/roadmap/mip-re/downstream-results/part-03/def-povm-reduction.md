---
declaration: definition
origin: cited
lean: MIPRE.BipartiteModel.POVMReduces, MIPRE.ModelOver, MIPRE.ModelOver.of, MIPRE.ModelOver.expandA, MIPRE.Game.swap, MIPRE.POVMIn.compress
statement: formalized
---

# Reduction of POVM strategies

A bipartite model $M'$ *reduces* to $M$ if every POVM strategy in $M'$, for every game, has value at most that of some POVM strategy in $M$. A *model over* an algebra ${\mathscr{A}}_B$ is a bipartite model whose second player's algebra is ${\mathscr{A}}_B$, packed with its first player's algebra and its represented algebra, the former ordered and proper; its one-sided extension is again one. The game with the players exchanged asks the second player the first question.

## Depends on

- [The one-sided ancilla extension](def-one-sided-extension.md)
- [The order of a matrix algebra over an ordered $*$-ring](def-block-order.md)
- [Nonlocal game](../../foundations/part-01/def-game.md)

## Lean

Formalized as [`MIPRE.BipartiteModel.POVMReduces`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.POVMReduces), [`MIPRE.ModelOver`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ModelOver), [`MIPRE.ModelOver.of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ModelOver.of), [`MIPRE.ModelOver.expandA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ModelOver.expandA), [`MIPRE.Game.swap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Game.swap), [`MIPRE.POVMIn.compress`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.POVMIn.compress).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2025](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2025)
