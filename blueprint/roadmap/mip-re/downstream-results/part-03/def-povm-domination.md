---
declaration: definition
origin: cited
lean: MIPRE.ValueModel.DominatesPOVM, MIPRE.ValueModel.ProjApprox
statement: formalized
---

# Domination of the POVM strategies, and approximation by projective strategies

A value model $\omega$ *dominates the POVM strategies* of a bipartite model if every pair of families of POVMs in the players' algebras has value at most $\omega$ of the game. It is *approached by projective strategies* if, for every game $\mathfrak{G}$ and every $0 \leq t < \omega(\mathfrak{G})$, some projective strategy for $\mathfrak{G}$ in a model on a Hilbert space that $\omega$ dominates has value greater than $t$.

## Depends on

- [Projective strategy in a bipartite model](../part-02/def-model-proj-strategy.md)
- [Value models](../part-01/def-value-model.md)

## Lean

Formalized as [`MIPRE.ValueModel.DominatesPOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.DominatesPOVM), [`MIPRE.ValueModel.ProjApprox`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.ProjApprox).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1991](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1991)
