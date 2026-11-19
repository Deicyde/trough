---
declaration: definition
origin: cited
lean: MIPRE.MIPCo
statement: formalized
---

# The class $\mathrm{MIP}^{\mathrm{co}}$

A language $L \subseteq \{0,1\}^*$ is in $\mathrm{MIP}^{\mathrm{co}}$ if there is a computable map $g$ from bit strings to game descriptions (Definition [Game description](../../foundations/part-02/def-game-description.md)) such that for every string $z$,

$$
z \in L\ \Longrightarrow\ {\omega^{\mathrm{co}}}(\mathfrak{G}_{g(z)}) = 1,
\qquad
z \notin L\ \Longrightarrow\ {\omega^{\mathrm{co}}}(\mathfrak{G}_{g(z)}) \leq \tfrac12,
$$

in the bipartite commuting-operator value of Definition [Commuting-operator value](../../parallel-repetition/def-co-value-bipartite.md): the class $\mathrm{MIP}({\omega^{\mathrm{co}}})$ of Definition [Value models](def-value-model.md). As Definition [The computable class](../../foundations/part-03/def-mipstar-computable.md), this is the computable class, with no polynomial-time bound on $g$; the polynomial-time class of Lin's paper is contained in it, as Lemma [The class is contained in the computable one](../../foundations/part-03/lem-mipstar-poly-sub.md) shows for $\mathrm{MIP}^*$, and is not formalized.

## Depends on

- [Commuting-operator value](../../parallel-repetition/def-co-value-bipartite.md)
- [Game description](../../foundations/part-02/def-game-description.md)
- [Value models](def-value-model.md)

## Lean

Formalized as [`MIPRE.MIPCo`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.MIPCo).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 785](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L785)
