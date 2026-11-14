---
declaration: definition
origin: cited
lean: HaltingGameValue.GameData, HaltingGameValue.GameData.toGame, HaltingGameValue.GameData.game
statement: formalized
---

# Game description

A *game description* is a tuple $g = (n_{\mathcal{X}}, n_{\mathcal{A}}, w, \mathrm{acc})$ of two integers, a finite list $w$ of weighted question pairs, and a finite list $\mathrm{acc}$ of accepted answer tuples. It determines a synchronous game $\mathfrak{G}_g$ on question alphabet $\{0, \ldots, n_{\mathcal{X}}\}$ and answer alphabet $\{0, \ldots, n_{\mathcal{A}}\}$: the question distribution is $w$ normalized (a fixed point mass if $w$ has total weight zero), and the predicate accepts exactly the tuples listed in $\mathrm{acc}$, except that unequal answers to equal questions always lose. Game descriptions are first-order data and carry a canonical Gödel numbering (`GameData` in the Lean file).

## Depends on

- [Synchronous game](../part-01/def-sync-game.md)

## Lean

Formalized as [`HaltingGameValue.GameData`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/HaltingGameValue.GameData), [`HaltingGameValue.GameData.toGame`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/HaltingGameValue.GameData.toGame), [`HaltingGameValue.GameData.game`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/HaltingGameValue.GameData.game).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 1370](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L1370)
