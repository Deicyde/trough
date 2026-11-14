---
declaration: definition
origin: cited
lean: MIPRE.CommutingUpperRE
statement: formalized
---

# Upper semidecision of the commuting-operator value

The proposition that the set of triples $(d, p, q)$ of a game description $d$ and $p, q \in \mathbb{N}$ with ${\omega^{\mathrm{co}}}(\mathfrak{G}_d) < p/q$ is recursively enumerable, where $p/0 = 0$: the threshold encoding of Lemma [The value is approximable from below](../../background-results/part-05/lem-value-lower-approx.md). Lemma [Upper semidecision of the commuting-operator value](lem-valco-upper-re.md) proves it; Lemma [Conditional separation](lem-tsirelson-conditional.md) takes it as a hypothesis.

## Depends on

- [Game description](../../foundations/part-02/def-game-description.md)
- [Commuting-operator value](../../parallel-repetition/def-co-value-bipartite.md)
- [Value models](def-value-model.md)

## Lean

Formalized as [`MIPRE.CommutingUpperRE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingUpperRE).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 401](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L401)
