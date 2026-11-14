---
declaration: definition
origin: cited
lean: MIPRE.BipartiteModel.IsDyadicPair, MIPRE.CommutingFinitePairApprox
statement: formalized
---

# Dyadic pairs

A *dyadic pair* is a finite pair (Definition [Finite pairs](../part-04/def-finite-pair.md)) whose two players' algebras both have unital dyadic matrix units (Definition [Unital dyadic matrix units](def-dyadic-units.md)); by Theorem [Dyadic matrix units exclude abelian projections](thm-no-abelian-dyadic.md), neither player's operators then contain a nonzero abelian projection. ${\omega^{\mathrm{co}}}$ is *approached in dyadic pairs* if for every game $\mathfrak{G}$ and every $0 \leq t < {\omega^{\mathrm{co}}}(\mathfrak{G})$ there is a projective strategy for $\mathfrak{G}$ of value greater than $t$ in a dyadic pair.

## Depends on

- [Finite pairs](../part-04/def-finite-pair.md)
- [Unital dyadic matrix units](def-dyadic-units.md)
- [Projective strategy in a bipartite model](../part-02/def-model-proj-strategy.md)

## Lean

Formalized as [`MIPRE.BipartiteModel.IsDyadicPair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.IsDyadicPair), [`MIPRE.CommutingFinitePairApprox`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingFinitePairApprox).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2964](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2964)
