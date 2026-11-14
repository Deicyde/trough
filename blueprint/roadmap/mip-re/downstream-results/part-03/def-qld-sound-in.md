---
declaration: definition
origin: cited
lean: MIPRE.QLD.AncillaModel, MIPRE.QLD.AncillaModel.of, MIPRE.QLD.Extraction, MIPRE.QLD.Extraction.mono, MIPRE.QLD.SoundIn, MIPRE.QLD.SoundCo, MIPRE.QLD.ApproxSoundIn
statement: formalized
---

# The Pauli basis test is sound in a model

An *ancilla model* is a bipartite model on a Hilbert space, with a unit state and with ordered, proper player algebras (Definition [The order of a matrix algebra over an ordered $*$-ring](def-block-order.md)); every such model is one. An *extraction* at error $\delta$, for a projective strategy of the Pauli basis game $\mathfrak{G}^{\textsc{Pauli}}_{(q,m,d)}$ in a bipartite model $M$, is an ancilla model $N$ and a local isometry of $M$ into the register model of $N$ on $\mathbb{F}_q^{\{0,1\}^m}$ that carries the state of $M$ within $\delta$ of the state $|\textsc{EPR}_q\rangle^{\otimes 2^m} \otimes \psi_N$ of the register model, and carries each player's $(\textsc{Pauli}, W)$ measurement, read as cube data, within $\delta$ of the honest Pauli projectors on that player's register, in summed squared state norm, for both bases $W$. An extraction at one error is one at every larger error. The Pauli basis test is *sound in $M$, with the value model $\omega$*, if for every field $\mathbb{F}_q$ of characteristic two, every $m \geq 1$ dividing $q$ and every $d \geq 1$, every projective strategy in $M$ failing the test with probability at most $\varepsilon$ has an extraction at the error $\delta_{qld}(\varepsilon, m, d, q)$ of Theorem [Pauli basis test / quantum low individual degree test](../../background-results/part-01/thm-qld.md) whose ancilla model $\omega$ dominates (Definition [Domination of the POVM strategies, and approximation by projective strategies](def-povm-domination.md)). That error is, in Lean, the function `qldErr` the proof of the theorem produces, at most the closed form of the theorem when $\varepsilon \leq 1$ (Lemma [The error of the Pauli basis test](../../background-results/part-03/lem-qld-error.md)). Soundness in $M$ is the conclusion of Theorem [Pauli basis test / quantum low individual degree test](../../background-results/part-01/thm-qld.md) for the projective strategies in $M$, and that theorem proves it in every model with ordered, proper player algebras in which the seeded low-individual-degree test is sound in every extension by a unit vector and whose extensions, in every unit state, $\omega$ dominates. The test is *sound in the commuting-operator model* if it is sound, with ${\omega^{\mathrm{co}}}$, in the model of every commuting-operator strategy. A value model is *approached in models where the test is sound* if, for every game $\mathfrak{G}$ and every $0 \leq t < \omega(\mathfrak{G})$, some projective strategy for $\mathfrak{G}$ in a model on a Hilbert space in which the test is sound with $\omega$ has value greater than $t$.

## Depends on

- [Pauli basis test](../../background-results/part-01/def-qld-game.md)
- [The register model](def-register-model.md)
- [Local isometries of bipartite models](def-local-isometry.md)
- [Domination of the POVM strategies, and approximation by projective strategies](def-povm-domination.md)
- [Projective strategy in a bipartite model](../part-02/def-model-proj-strategy.md)
- [The order of a matrix algebra over an ordered $*$-ring](def-block-order.md)
- [The error of the Pauli basis test](../../background-results/part-03/lem-qld-error.md)

## Lean

Formalized as [`MIPRE.QLD.AncillaModel`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.AncillaModel), [`MIPRE.QLD.AncillaModel.of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.AncillaModel.of), [`MIPRE.QLD.Extraction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Extraction), [`MIPRE.QLD.Extraction.mono`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Extraction.mono), [`MIPRE.QLD.SoundIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.SoundIn), [`MIPRE.QLD.SoundCo`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.SoundCo), [`MIPRE.QLD.ApproxSoundIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.ApproxSoundIn).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2061](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2061)
