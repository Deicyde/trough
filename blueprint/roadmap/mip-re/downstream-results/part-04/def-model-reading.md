---
declaration: definition
origin: cited
lean: MIPRE.reindexStarAlgHomR, MIPRE.moveEquiv, MIPRE.basisVec, MIPRE.BipartiteModel.recut
statement: formalized
---

# Readings of an extension

Let $M$ be a bipartite model, $e$ a vector on registers $\alpha \times \beta$ and $\sigma : \alpha \times \beta \to \alpha' \times \beta'$ a bijection. The *reading* of the extension of $M$ in $e$ along $\sigma$ has the Hilbert space, the state and the represented algebra of that extension, with the first player's algebra $M_{\alpha'}({\mathscr{A}}_A)$ and the second player's $M_{\beta'}({\mathscr{A}}_B)$ acting through $\sigma$, reindexing square matrices along a bijection being a unital $*$-homomorphism. The registers are regrouped, a register handed across the cut is read by the other player, and nothing happens to the state. The regrouping that hands the first player's outer register $\gamma$ to the second player is $((c, a), b) \mapsto (a, (c, b))$, and the product basis vector of a pair of registers at $(a_0, b_0)$ is written $|a_0 b_0\rangle$.

## Depends on

- [Ancilla extension of a bipartite model](../part-02/def-ancilla-extension.md)

## Lean

Formalized as [`MIPRE.reindexStarAlgHomR`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.reindexStarAlgHomR), [`MIPRE.moveEquiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.moveEquiv), [`MIPRE.basisVec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.basisVec), [`MIPRE.BipartiteModel.recut`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.recut).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2305](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2305)
