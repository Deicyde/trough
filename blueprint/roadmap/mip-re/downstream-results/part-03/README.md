---
navigation: transparent
---

# Operations on projective… to The Pauli basis test is sound…

- [Operations on projective strategies](lem-model-proj-strategy.md)
- [Projective strategies in the two models](lem-model-proj-strategy-values.md)
- [The low-individual-degree test is sound in a model](def-lidt-sound-in.md)
- [The low-individual-degree test is sound in the tensor-product model](lem-lidt-sound-in-tensor.md)
- [Answer reduction is sound in ${\omega^{\mathrm{co}}}$, given the low-individual-degree test](thm-ar-sound-co.md)

### Introspection in the model, given the Pauli basis test

Phase 4 of `planning/mipco-track.md` reads introspection in ${\omega^{\mathrm{co}}}$. Its soundness analysis (Lemmas [Restriction to the actual Pauli game](../../structure-of-the-proof/part-05/lem-intro-pauli-restriction.md) to [Supplying ambient introspection](../../structure-of-the-proof/part-06/lem-introspection-supply.md)) works with a strategy: it restricts it to the Pauli block, extracts from the Pauli basis test local isometries into an EPR register tensored with an auxiliary state, transports the strategy there, replaces its two Introspect measurements stage by stage by projective ones dilated on fresh ancillas, and reads a strategy for the original game off the result. It is written once, for a projective strategy in a bipartite model, and the one fact about the Pauli basis test it uses, the conclusion of Theorem [Pauli basis test / quantum low individual degree test](../../background-results/part-01/thm-qld.md), becomes a hypothesis on the model: the test is sound in it (Definition [The Pauli basis test is sound in a model](def-qld-sound-in.md)). Phase 5 discharges that hypothesis (Section The Pauli basis test in the model, given the low-individual-degree test): Theorem [Pauli basis test / quantum low individual degree test](../../background-results/part-01/thm-qld.md) is proved in every model with ordered, proper player algebras in which the seeded low-individual-degree test is sound in every extension by a unit vector and whose extensions the value model dominates. So the hypothesis holds in the tensor-product model, which gives back the soundness clause of Theorem [Introspection](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3993), and in the commuting-operator model as soon as the seeded test is sound there (Lemma [The Pauli basis test is sound in the commuting-operator model, given the seeded test](../part-04/lem-qld-sound-co.md)); Corollary [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from the co-soundness of the Pauli basis test and of the low-individual-degree test](../part-02/cor-mipco-from-stages.md) assumes it in place of introspection's clause, and Corollary [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from the co-soundness of the low-individual-degree test](../part-04/cor-mipco-from-lidt.md) no longer does. Four things change with the setting, each a definition below. The local isometries are one local isometry of models, whose homomorphisms are not unital, so a transported measurement is completed by the complement of the image. The EPR register tensored with an auxiliary state is the register model of an auxiliary model. The Naimark dilations of the adaptive stages are Halmos dilations of a Kraus family in the first player's algebra, whose ancilla has a size chosen along the way, so each stage returns a new model; every strategy of it reduces to one of the original model, which is how a value model dominating the auxiliary model dominates the model of the extracted strategy. And the extracted strategy is a POVM strategy there, which the value model has to dominate.

- [The order of a matrix algebra over an ordered $*$-ring](def-block-order.md)
- [Local isometries of bipartite models](def-local-isometry.md)
- [Local isometries carry the Born rule](lem-local-isometry.md)
- [Moving registers along local isometries](lem-ancilla-isometries.md)
- [The register model](def-register-model.md)
- [The register model](lem-register-model.md)
- [The ancilla extension of a tensor-product model](lem-tensor-expand.md)
- [The one-sided ancilla extension](def-one-sided-extension.md)
- [The one-sided ancilla extension](lem-one-sided-extension.md)
- [Projective dilation against a fixed state, in a star-ordered ring](lem-kraus-dilation.md)
- [Domination of the POVM strategies, and approximation by projective strategies](def-povm-domination.md)
- [Domination and approximation in the two models](lem-povm-domination.md)
- [Reduction of POVM strategies](def-povm-reduction.md)
- [Reductions](lem-povm-reduction.md)
- [The Pauli basis test is sound in a model](def-qld-sound-in.md)
