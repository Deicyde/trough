---
declaration: definition
origin: cited
lean: MIPRE.BipartiteModel.expand, MIPRE.smulKron, MIPRE.liftLeft, MIPRE.liftRight, MIPRE.mapMatrixStarAlgHom
statement: formalized
---

# Ancilla extension of a bipartite model

Let $(\mathcal{H}, \psi, {\mathscr{A}}, {\mathscr{A}}_A, {\mathscr{A}}_B)$ be a bipartite model, $\alpha$ and $\beta$ finite sets and $e \in \mathbb{C}^{\alpha \times \beta}$. The *ancilla extension* of the model by $e$ has the Hilbert space $\mathcal{H} \otimes \mathbb{C}^{\alpha \times \beta}$, the $\ell^2$-sum of $\alpha \times \beta$ copies of $\mathcal{H}$; the state $\psi \otimes e$; the algebra $M_{\alpha \times \beta}({\mathscr{A}})$, acting entrywise; the first player's algebra $M_\alpha({\mathscr{A}}_A)$, acting as $X \otimes {I}_\beta$; and the second player's algebra $M_\beta({\mathscr{A}}_B)$, acting as ${I}_\alpha \otimes Y$. For $X \in {\mathscr{A}}_A$ and $P \in M_\alpha(\mathbb{C})$, $X \otimes P \in M_\alpha({\mathscr{A}}_A)$ is the matrix with entries $P_{ab} X$, and likewise for the second player.

## Depends on

- [Bipartite model](def-bipartite-model.md)
- [Commutation-preserving dilation](lem-co-dilation.md)

## Lean

Formalized as [`MIPRE.BipartiteModel.expand`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.expand), [`MIPRE.smulKron`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.smulKron), [`MIPRE.liftLeft`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.liftLeft), [`MIPRE.liftRight`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.liftRight), [`MIPRE.mapMatrixStarAlgHom`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.mapMatrixStarAlgHom).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1252](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1252)
