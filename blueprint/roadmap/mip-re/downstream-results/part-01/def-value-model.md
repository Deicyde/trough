---
declaration: definition
origin: cited
lean: MIPRE.ValueModel, MIPRE.ValueModel.tensor, MIPRE.ValueModel.commuting, MIPRE.ValueModel.LowerRE, MIPRE.ValueModel.UpperRE, MIPRE.ValueModel.HaltingReductionRE, MIPRE.ValueModel.HaltingReductionCoRE, MIPRE.Verifier.val, MIPRE.MIPClass
statement: formalized
---

# Value models

A *value model* $\omega$ assigns to every finite game $\mathfrak{G}$ a real number $\omega(\mathfrak{G})$ such that $\mathrm{val}^*(\mathfrak{G}) \leq \omega(\mathfrak{G}) \leq 1$, and such that $\omega$ is invariant under relabeling of the four alphabets, monotone in the decision predicate, zero on a game that rejects everything, unchanged by padding the answer alphabets with always-rejected answers, and unchanged by the doubling of the question set. The two models are $\mathrm{val}^*$ (Definition [Quantum value](../../foundations/part-01/def-q-value.md)) and ${\omega^{\mathrm{co}}}$ (Definition [Commuting-operator value](../../parallel-repetition/def-co-value-bipartite.md)), and every statement below in a model $\omega$ is one theorem in Lean, instantiated twice. The value of $\mathsf{V}_n$ in the model is $\omega(\mathsf{V}_n)$, at an answer bound. The model is *r.e. from below* if the set of triples $(d, p, q)$ with $p/q < \omega(\mathfrak{G}_d)$ is recursively enumerable, in the threshold encoding of Lemma [The value is approximable from below](../../background-results/part-05/lem-value-lower-approx.md), and *r.e. from above* if the set with $\omega(\mathfrak{G}_d) < p/q$ is: $\mathrm{val}^*$ is r.e. from below (Lemma [The value is approximable from below](../../background-results/part-05/lem-value-lower-approx.md)) and ${\omega^{\mathrm{co}}}$ from above (Lemma [Upper semidecision of the commuting-operator value](lem-valco-upper-re.md)), and neither has the other direction, by the two theorems themselves. A *halting reduction of $\mathrm{RE}$ shape* to $\omega$ is a computable map from machines to game descriptions with $\omega = 1$ on the machines that halt on the empty input and $\omega \leq \frac12$ on the others; the *$\mathrm{coRE}$ shape* is the reverse. The class $\mathrm{MIP}(\omega)$ is the set of languages $L$ for which some computable map $g$ from strings to game descriptions has $\omega(\mathfrak{G}_{g(z)}) = 1$ for $z \in L$ and $\omega(\mathfrak{G}_{g(z)}) \leq \frac12$ for $z \notin L$; $\mathrm{MIP}^*$ of Definition [The computable class](../../foundations/part-03/def-mipstar-computable.md) is $\mathrm{MIP}(\mathrm{val}^*)$.

## Depends on

- [Quantum value](../../foundations/part-01/def-q-value.md)
- [Commuting-operator value](../../parallel-repetition/def-co-value-bipartite.md)
- [Game description](../../foundations/part-02/def-game-description.md)
- [Normal form verifier in the ambient model](../../foundations/part-03/def-normal-verifier.md)
- [Basic properties of the correlation sets](lem-correlation-sets-basic.md)

## Lean

Formalized as [`MIPRE.ValueModel`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel), [`MIPRE.ValueModel.tensor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.tensor), [`MIPRE.ValueModel.commuting`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.commuting), [`MIPRE.ValueModel.LowerRE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.LowerRE), [`MIPRE.ValueModel.UpperRE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.UpperRE), [`MIPRE.ValueModel.HaltingReductionRE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.HaltingReductionRE), [`MIPRE.ValueModel.HaltingReductionCoRE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.HaltingReductionCoRE), [`MIPRE.Verifier.val`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.val), [`MIPRE.MIPClass`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.MIPClass).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 746](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L746)
