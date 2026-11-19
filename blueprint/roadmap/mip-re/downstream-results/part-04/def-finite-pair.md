---
declaration: definition
origin: cited
lean: MIPRE.VecTrace, MIPRE.BipartiteModel.opsA, MIPRE.BipartiteModel.opsB, MIPRE.BipartiteModel.IsFinitePair
statement: formalized
---

# Finite pairs

A *vector trace* on a set $s$ of bounded operators on a Hilbert space $\mathcal{H}$ is a finite family of vectors $g_1, \dots, g_n \in \mathcal{H}$ with $\sum_k \|g_k\|^2 = 1$ such that $\tau(x) = \sum_k \langle g_k, x g_k \rangle$ is tracial on $s$, $\tau(xy) = \tau(yx)$ for $x, y \in s$, and the family separates $s$: an $x \in s$ with $x g_k = 0$ for every $k$ is zero. On a $*$-closed $s$ the separation is the faithfulness of $\tau$, since $\tau(x^* x) = \sum_k \|x g_k\|^2$. A bipartite model (Definition [Bipartite model](../part-02/def-bipartite-model.md)) is a *finite pair* if both players' representations are injective, the operators of each player are exactly the operators commuting with all of the other player's, and each player's operators carry a vector trace. The state is an arbitrary unit vector.

Two features of the class matter for the port of the soundness proof to it. The trace is a finite sum of vector states, so the class is narrower than that of all pairs with faithful normal tracial states; the standard form of a tracial algebra needs one vector, and ancilla extensions, the doubling $\mathcal{H} \oplus \mathcal{H}$ and amplification by a tracial algebra in standard form (Lemma [Amplification by an algebra with dyadic matrix units](../part-05/lem-amplification-dyadic.md)) stay in the class, while corners do not. And the class contains type $\mathrm{I}$ pairs with diffuse centre, such as $L^\infty[0,1]$ acting on $L^2[0,1]$, whose projections are all abelian. Orthonormalization is proved only in algebras without abelian projections (Theorem [Orthonormalization in algebras without abelian projections](../../background-results/part-01/thm-orthonormalization-no-abelian.md)), so the class the port works in is narrowed to the dyadic pairs (Definition [Dyadic pairs](../part-05/def-dyadic-pair.md)), which exclude them, and Lemma [${\omega^{\mathrm{co}}}$ is approached in dyadic pairs](../part-05/lem-co-value-finite-pair.md) amplifies to reach it.

## Depends on

- [Bipartite model](../part-02/def-bipartite-model.md)

## Lean

Formalized as [`MIPRE.VecTrace`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.VecTrace), [`MIPRE.BipartiteModel.opsA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.opsA), [`MIPRE.BipartiteModel.opsB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.opsB), [`MIPRE.BipartiteModel.IsFinitePair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.IsFinitePair).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2795](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2795)
