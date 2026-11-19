---
declaration: lemma
origin: cited
lean: MIPRE.SeededGame.commutingOperatorValue_ge_of_oracular
statement: formalized
proof: formalized
---

# Soundness of oracularization, in ${\omega^{\mathrm{co}}}$

Let $S$ be a seeded game with nonempty seed space and nonempty answer alphabet. For every $\varepsilon > 0$, if ${\omega^{\mathrm{co}}}$ of the oracularization of $S$ exceeds $1 - \varepsilon$, then ${\omega^{\mathrm{co}}}$ of the game of $S$ is at least $1 - 24\sqrt{\varepsilon}$.

## Depends on

- [Soundness of oracularization, in a bipartite model](lem-oracular-soundness-model.md)
- [Strategies in a model, read in ${\omega^{\mathrm{co}}}$](lem-model-strategy-co.md)
- [The oracularized game](../../structure-of-the-proof/part-06/def-oracular-game.md)
- [Commuting-operator value](../../parallel-repetition/def-co-value-bipartite.md)

## Proof

For $\varepsilon \leq 1$, Lemma [Strategies in a model, read in ${\omega^{\mathrm{co}}}$](lem-model-strategy-co.md) gives a commuting-operator strategy whose measurements are projective in its model and whose model value exceeds $1 - \varepsilon$. Lemma [Soundness of oracularization, in a bipartite model](lem-oracular-soundness-model.md) in that model gives families of value at least $1 - 24\sqrt\varepsilon$ in the game of $S$, and those families are a commuting-operator strategy (Lemma [Strategies in a model, read in ${\omega^{\mathrm{co}}}$](lem-model-strategy-co.md)). For $\varepsilon > 1$ the bound is negative.

## Lean

Formalized as [`MIPRE.SeededGame.commutingOperatorValue_ge_of_oracular`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.commutingOperatorValue_ge_of_oracular).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1480](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1480)
