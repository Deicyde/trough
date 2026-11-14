---
declaration: theorem
origin: cited
lean: MIPRE.QLD.rdPauliVec_legalize_pauli, MIPRE.QLD.legalStrat, MIPRE.QLD.legalStrat_PA, MIPRE.QLD.legalStrat_PB, MIPRE.QLD.one_sub_value_legalStrat_le, MIPRE.QLD.legalSupport_legalStrat_A, MIPRE.QLD.legalSupport_legalStrat_B, MIPRE.QLD.legalStrat_pauli_A, MIPRE.QLD.legalStrat_pauli_B, MIPRE.QLD.sum_stateSqNorm_alice_le_four, MIPRE.QLD.sum_stateSqNorm_bob_le_four, MIPRE.QLD.norm_inert_reg_sub_le_four, MIPRE.QLD.inert_reg_ΦA_one, MIPRE.QLD.inert_reg_ΦB_one, MIPRE.QLD.Extraction.trivial, MIPRE.QLD.norm_evec_unitPoint, MIPRE.QLD.dominatesPOVM_of_expand, MIPRE.QLD.MirrorSimul.swapPhi_ΦA_one, MIPRE.QLD.MirrorSimul.swapPhi_ΦB_one, MIPRE.QLD.exists_extraction_of_regime, MIPRE.QLD.soundIn_of_lidt
statement: formalized
proof: formalized
---

# Pauli basis test / quantum low individual degree test

There exists a function

$$
\delta_{qld}(\varepsilon, m, d, q) = a (md)^a \bigl( \varepsilon^b + q^{-b} + 2^{-bmd} \bigr)
$$

for universal constants $a \geq 1$ and $0 < b < 1$ such that the following holds. Let $\mathcal{M}$ be a bipartite model (Definition [Bipartite model](../../downstream-results/part-02/def-bipartite-model.md)) whose two players' algebras are ordered, proper and compatible with the scalars, and let $\omega$ be a value model (Definition [Value models](../../downstream-results/part-01/def-value-model.md)). Suppose (L) that the seeded CL test is sound (Definition [The low-individual-degree test is sound in a model](../../downstream-results/part-03/def-lidt-sound-in.md)) in every ancilla extension of $\mathcal{M}$ by a unit vector (Definition [Ancilla extension of a bipartite model](../../downstream-results/part-02/def-ancilla-extension.md)), and (V) that $\omega$ dominates the POVM strategies (Definition [Domination of the POVM strategies, and approximation by projective strategies](../../downstream-results/part-03/def-povm-domination.md)) of every such extension with its state replaced by any unit vector. Then for all admissible parameter tuples $\mathsf{qldparams} = (q, m, d)$ and every projective strategy in $\mathcal{M}$ (Definition [Projective strategy in a bipartite model](../../downstream-results/part-02/def-model-proj-strategy.md)) for the game $\mathfrak{G}^{\textsc{Pauli}}_{\mathsf{qldparams}}$ that succeeds with probability at least $1 - \varepsilon$, there are an ancilla model $\mathcal{N}$, a bipartite model in a unit state $|\textsc{aux}\rangle$ whose POVM strategies $\omega$ dominates, and a local isometry (Definition [Local isometries of bipartite models](../../downstream-results/part-03/def-local-isometry.md)) from $\mathcal{M}$ to the register model of $\mathcal{N}$ on the register $\mathbb{F}_q^M$, $M = 2^m$, each player holding a copy of $(\mathbb{C}^q)^{\otimes M}$ (Definition [The register model](../../downstream-results/part-03/def-register-model.md)), such that

1. the image of the strategy's state is within $\delta_{qld}$ of $|\textsc{EPR}_q\rangle^{\otimes M} \otimes |\textsc{aux}\rangle$, the state of the register model; and
2. for each $W \in \{X, Z\}$ and each player, the image of that player's own measurement for the question $(\textsc{Pauli}, W)$, read as cube data, is within $\delta_{qld}$ of the Pauli basis measurement $\tau^W_h$, $h \in \mathbb{F}_q^M$, on that player's half of the register, in summed squared state-dependent distance on that state.

That is, the Pauli basis test is sound in $\mathcal{M}$ with $\omega$ (Definition [The Pauli basis test is sound in a model](../../downstream-results/part-03/def-qld-sound-in.md)). The pipeline uses two instances. In the tensor-product model of a state $|\psi\rangle$ on $\mathbb{C}^{d_\textsc{A}} \otimes \mathbb{C}^{d_\textsc{B}}$, with $\mathrm{val}^*$, both hypotheses hold, and the conclusion is the matrix statement: local isometries $\phi_\textsc{A}, \phi_\textsc{B}$ into $\mathcal{H}' \otimes (\mathbb{C}^q)^{\otimes M}$ and a state $|\textsc{aux}\rangle$ with $\left\| {\phi_\textsc{A} \otimes \phi_\textsc{B} |\psi\rangle - |\textsc{aux}\rangle \otimes |\textsc{EPR}_q\rangle^{\otimes M}} \right\| \leq \delta_{qld}$, and for $W \in \{X, Z\}$ the measurements for the questions $(\textsc{Pauli}, W)$ $\delta_{qld}$-close to the Pauli basis measurements $\tau^W_u$, $u \in \mathbb{F}_q^M$, acting on $|\textsc{EPR}_q\rangle^{\otimes M}$ (Lemma [The Pauli basis test is sound in the tensor-product model](../../downstream-results/part-04/lem-qld-sound-in-tensor.md)). In the model of every commuting-operator strategy, with ${\omega^{\mathrm{co}}}$, the second hypothesis always holds and the first follows from the soundness of the seeded CL test in the commuting-operator model (Lemma [The Pauli basis test is sound in the commuting-operator model, given the seeded test](../../downstream-results/part-04/lem-qld-sound-co.md)).

## Depends on

- [Pauli basis test](def-qld-game.md)
- [Quantum value](../../foundations/part-01/def-q-value.md)
- [Direct Magic Square anticommutation — what the pipeline actually needs](lem-ms-direct-anticomm.md)
- [The register model](../../downstream-results/part-03/def-register-model.md)
- [Local isometries of bipartite models](../../downstream-results/part-03/def-local-isometry.md)
- [Ancilla extension of a bipartite model](../../downstream-results/part-02/def-ancilla-extension.md)
- [Projective strategy in a bipartite model](../../downstream-results/part-02/def-model-proj-strategy.md)
- [The low-individual-degree test is sound in a model](../../downstream-results/part-03/def-lidt-sound-in.md)
- [Domination of the POVM strategies, and approximation by projective strategies](../../downstream-results/part-03/def-povm-domination.md)
- [Value models](../../downstream-results/part-01/def-value-model.md)
- [The Pauli basis test is sound in a model](../../downstream-results/part-03/def-qld-sound-in.md)
- [The error of the Pauli basis test](../part-03/lem-qld-error.md)

## Proof depends on

- [The swap isometry](../part-03/lem-qld-swap.md)
- [Self-consistency of the exact Pauli observables](../part-03/lem-qld-pauli-selfcons.md)
- [Axis degree for expanded line measurements](../part-02/lem-qld-axis-degree.md)
- [Pauli mixing with a retained classical fibre](../../structure-of-the-proof/part-02/lem-pauli-mixing.md)
- [The models of stages 4 and 5](../part-03/def-qld-physical-model.md)
- [Reductions](../../downstream-results/part-03/lem-povm-reduction.md)

## Proof

Two cases. Inside the regime — $48md \leq q$, and $2\sqrt{X} + 2X < 1$ at the constant $X$ of Lemma [Self-consistency of the exact Pauli observables](../part-03/lem-qld-pauli-selfcons.md), which is what item 1 of Lemma [The swap isometry](../part-03/lem-qld-swap.md) needs — three steps, and no dilation.

1. **Legalize** (Lemma [Axis degree for expanded line measurements](../part-02/lem-qld-axis-degree.md)): send every answer of the wrong format to its question's default. The legalized strategy is projective, fails with probability at most $\varepsilon$, and is legally supported, which stage 4 needs; and its coarse $(\textsc{Pauli}, W)$ measurements are the strategy's, a malformed Pauli answer and the default both reading as the cube datum $0$.
2. **Both cuts on one state**: stage 4 (Lemma [The simultaneous global measurement](../part-03/lem-qld-simultaneous.md)) at the legalized strategy and at the legalized strategy with the players exchanged, at one padding size. This is where hypothesis (L) is used: the padded models of $\mathcal{M}$ and of $\mathcal{M}$ with the players exchanged are ancilla extensions of $\mathcal{M}$ up to associativity, and the two runs' pair measurements are the two cuts of one physical model (Definition [The models of stages 4 and 5](../part-03/def-qld-physical-model.md)).
3. **The swap isometry** of Lemma [The swap isometry](../part-03/lem-qld-swap.md) is a local isometry of $\mathcal{M}$ into the register model of the extension of $\mathcal{M}$ by the padded registers in an auxiliary unit state; that extension, in that state, is the ancilla model, and hypothesis (V) is that $\omega$ dominates it. Item 2 is item 2 of the lemma as it stands, the measurements it carries being the strategy's own, and item 1 is the square root of the lemma's bound on the squared distance.

Both items are also at most the trivial bound $4$, which caps the error. Outside the regime the error is $4$, and the model itself, with the EPR register adjoined inertly, is an extraction at that bound: the state is carried exactly to the state of the register model, and two projective measurements on a unit vector are within $4$ of each other in summed squared state-dependent distance. Its ancilla model is $\mathcal{M}$ itself, which $\omega$ dominates by (V) at the extension by one-point registers. In both cases the error is the function of Lemma [The error of the Pauli basis test](../part-03/lem-qld-error.md), which has the closed form.

## Lean

Formalized as [`MIPRE.QLD.rdPauliVec_legalize_pauli`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.rdPauliVec_legalize_pauli), [`MIPRE.QLD.legalStrat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.legalStrat), [`MIPRE.QLD.legalStrat_PA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.legalStrat_PA), [`MIPRE.QLD.legalStrat_PB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.legalStrat_PB), [`MIPRE.QLD.one_sub_value_legalStrat_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.one_sub_value_legalStrat_le), [`MIPRE.QLD.legalSupport_legalStrat_A`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.legalSupport_legalStrat_A), [`MIPRE.QLD.legalSupport_legalStrat_B`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.legalSupport_legalStrat_B), [`MIPRE.QLD.legalStrat_pauli_A`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.legalStrat_pauli_A), [`MIPRE.QLD.legalStrat_pauli_B`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.legalStrat_pauli_B), [`MIPRE.QLD.sum_stateSqNorm_alice_le_four`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.sum_stateSqNorm_alice_le_four), [`MIPRE.QLD.sum_stateSqNorm_bob_le_four`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.sum_stateSqNorm_bob_le_four), [`MIPRE.QLD.norm_inert_reg_sub_le_four`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.norm_inert_reg_sub_le_four), [`MIPRE.QLD.inert_reg_ΦA_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.inert_reg_ΦA_one), [`MIPRE.QLD.inert_reg_ΦB_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.inert_reg_ΦB_one), [`MIPRE.QLD.Extraction.trivial`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Extraction.trivial), [`MIPRE.QLD.norm_evec_unitPoint`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.norm_evec_unitPoint), [`MIPRE.QLD.dominatesPOVM_of_expand`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.dominatesPOVM_of_expand), [`MIPRE.QLD.MirrorSimul.swapPhi_ΦA_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.MirrorSimul.swapPhi_ΦA_one), [`MIPRE.QLD.MirrorSimul.swapPhi_ΦB_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.MirrorSimul.swapPhi_ΦB_one), [`MIPRE.QLD.exists_extraction_of_regime`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.exists_extraction_of_regime), [`MIPRE.QLD.soundIn_of_lidt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.soundIn_of_lidt).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 1631](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L1631)
