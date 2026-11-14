---
declaration: definition
origin: cited
lean: MIPRE.BipartiteModel.Embedding, MIPRE.BipartiteModel.Embedding.id, MIPRE.BipartiteModel.Embedding.comp, MIPRE.BipartiteModel.Embedding.swap, MIPRE.BipartiteModel.Iso.toEmbedding, MIPRE.BipartiteModel.LocalIsometry.toWithState
statement: formalized
---

# Embeddings of bipartite models

An *embedding* of bipartite models is a local isometry (Definition [Local isometries of bipartite models](../part-03/def-local-isometry.md)) whose isometry carries the state to the state and whose two homomorphisms are unital: the model form of adjoining registers in fixed vectors. Embeddings have identities, compose and exchange with the players, and every isomorphism is one. A local isometry from $M$ to $M'$ is also one from $M$ to $M'^{\varphi}$, for every vector $\varphi$ of the space of $M'$.

## Depends on

- [Local isometries of bipartite models](../part-03/def-local-isometry.md)
- [Isomorphisms of bipartite models](def-model-iso.md)
- [Local isometries carry the Born rule](../part-03/lem-local-isometry.md)

## Lean

Formalized as [`MIPRE.BipartiteModel.Embedding`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.Embedding), [`MIPRE.BipartiteModel.Embedding.id`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.Embedding.id), [`MIPRE.BipartiteModel.Embedding.comp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.Embedding.comp), [`MIPRE.BipartiteModel.Embedding.swap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.Embedding.swap), [`MIPRE.BipartiteModel.Iso.toEmbedding`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.Iso.toEmbedding), [`MIPRE.BipartiteModel.LocalIsometry.toWithState`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.toWithState).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2368](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2368)
