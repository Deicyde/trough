---
declaration: lemma
origin: cited
lean: MIPRE.BipartiteModel.IsFinitePair.expand, MIPRE.BipartiteModel.IsFinitePair.swap
statement: formalized
proof: formalized
---

# Finite pairs are closed under ancilla extensions

An ancilla extension of a finite pair (Definition [Ancilla extension of a bipartite model](../part-02/def-ancilla-extension.md)) with nonempty registers is a finite pair, and so is a finite pair with the players exchanged.

## Depends on

- [Finite pairs](def-finite-pair.md)
- [Ancilla extension of a bipartite model](../part-02/def-ancilla-extension.md)
- [The commutant of a matrix amplification](lem-ampl-commutant.md)

## Proof

Let the registers be $\alpha$ and $\beta$. The first player's operators of the extension are the $X \otimes {I}_\beta$ for matrices $X$ over the first player's operators, and the second player's the ${I}_\alpha \otimes Y$. An operator commuting with every ${I}_\alpha \otimes Y$ commutes with the matrix units of the second register and with the amplifications of the second player's operators, so it is an $X \otimes {I}_\beta$ whose entries commute with the second player's operators (Lemma [The commutant of a matrix amplification](lem-ampl-commutant.md)), and these entries are the first player's operators; symmetrically for the second player. If $g_1, \dots, g_n$ is a vector trace of the first player's operators, the vectors $\left\vert {\alpha} \right\vert^{-1/2}\, g_k \otimes e_i \otimes e_{b_0}$, for $k \leq n$, $i \in \alpha$ and a fixed $b_0 \in \beta$, give $X \otimes {I}_\beta$ the normalized trace $\left\vert {\alpha} \right\vert^{-1} \sum_i \tau(X_{ii})$. It is tracial because $\tau$ is, and the family separates because $X \otimes {I}_\beta$ kills the vector of $(k, i)$ only if $X_{ji} g_k = 0$ for every $j$. Exchanging the players exchanges the conditions.

## Lean

Formalized as [`MIPRE.BipartiteModel.IsFinitePair.expand`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.IsFinitePair.expand), [`MIPRE.BipartiteModel.IsFinitePair.swap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.IsFinitePair.swap).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2823](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2823)
