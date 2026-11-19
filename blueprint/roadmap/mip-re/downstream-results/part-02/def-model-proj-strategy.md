---
declaration: definition
origin: cited
lean: MIPRE.BipartiteModel.ProjStrat, MIPRE.BipartiteModel.ProjStrat.value, MIPRE.BipartiteModel.ProjStrat.failAt, MIPRE.BipartiteModel.ProjStrat.adapt, MIPRE.BipartiteModel.ProjStrat.relabel, MIPRE.BipartiteModel.ProjStrat.restrict, MIPRE.BipartiteModel.inconsistency, MIPRE.ValueModel.Dominates, MIPRE.POVMIn.toPOVM, MIPRE.POVMIn.isPVMIn_map
statement: formalized
---

# Projective strategy in a bipartite model

A *projective strategy* for a game $\mathfrak{G}$ in a bipartite model $(\mathcal{H}, \psi, {\mathscr{A}}, {\mathscr{A}}_A, {\mathscr{A}}_B)$ with a unit state (Definition [Bipartite model](def-bipartite-model.md)) is a projective measurement $\{A^x_a\}_a$ in ${\mathscr{A}}_A$ for each question $x$ of the first player and a projective measurement $\{B^y_b\}_b$ in ${\mathscr{A}}_B$ for each question $y$ of the second. Its value is the model's value of the two families, and its conditional failure at $(x, y)$ is the probability of rejection given the question pair. It is played on another game through a map of the questions and a question-dependent coarse-graining of the answers, relabelled along equivalences, or restricted to other questions; a coarse-graining of a projective measurement is projective, so these are projective strategies. The *inconsistency* of a family $\{P^x\}$ in ${\mathscr{A}}_A$ and a family $\{Q^x\}$ in ${\mathscr{A}}_B$ with a common outcome set, on an index weighted by $\mu$, is $\sum_x \mu(x) \sum_{a \neq b} \mathrm{Re}\langle \psi, \pi(\pi_A(P^x_a)\pi_B(Q^x_b))\psi\rangle$, Definition [Inconsistency](../../foundations/part-02/def-inconsistency.md) in the model. A value model $\omega$ *dominates* the model if every projective strategy in it has value at most $\omega$ of its game.

## Depends on

- [Bipartite model](def-bipartite-model.md)
- [Value models](../part-01/def-value-model.md)

## Lean

Formalized as [`MIPRE.BipartiteModel.ProjStrat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.ProjStrat), [`MIPRE.BipartiteModel.ProjStrat.value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.ProjStrat.value), [`MIPRE.BipartiteModel.ProjStrat.failAt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.ProjStrat.failAt), [`MIPRE.BipartiteModel.ProjStrat.adapt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.ProjStrat.adapt), [`MIPRE.BipartiteModel.ProjStrat.relabel`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.ProjStrat.relabel), [`MIPRE.BipartiteModel.ProjStrat.restrict`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.ProjStrat.restrict), [`MIPRE.BipartiteModel.inconsistency`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.inconsistency), [`MIPRE.ValueModel.Dominates`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.Dominates), [`MIPRE.POVMIn.toPOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.POVMIn.toPOVM), [`MIPRE.POVMIn.isPVMIn_map`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.POVMIn.isPVMIn_map).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1601](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1601)
