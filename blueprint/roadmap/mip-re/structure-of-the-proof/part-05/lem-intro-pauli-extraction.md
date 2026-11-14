---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.RestrictedSoundness.restriction, MIPRE.Introspection.RestrictedSoundness.edgeCount, MIPRE.Introspection.RestrictedSoundness.edgeCount_one_le, MIPRE.Introspection.RestrictedSoundness.exists_extraction
statement: formalized
proof: formalized
---

# Pauli extraction for the introspection game

Let $N$ be the number of ordered edges of the typed graph, so that $N \geq 1$, let $\delta_{qld}$ be the error of Theorem [Pauli basis test / quantum low individual degree test](../../background-results/part-01/thm-qld.md), and let $\omega$ be a value model. Let $\mathscr{S}$ be a projective strategy of the binary parsed introspection game in a bipartite model in which the Pauli basis test is sound with $\omega$ (Definitions [Projective strategy in a bipartite model](../../downstream-results/part-02/def-model-proj-strategy.md) and [The Pauli basis test is sound in a model](../../downstream-results/part-03/def-qld-sound-in.md)), failing with probability at most $\varepsilon$, whose two $(\textsc{Pauli}, W)$ measurements have nonzero effects only at full-register Pauli answers. Then the restriction of $\mathscr{S}$ to the Pauli basis game (Lemma [Restriction to the actual Pauli game](lem-intro-pauli-restriction.md)), its malformed answers completed at a scalar answer, has an *extraction in binary coordinates* at the error $T = \delta_{qld}(N\varepsilon, m, d, q)$: an ancilla model, with state $\psi_{\textsc{aux}}$, whose POVM strategies $\omega$ dominates, and a local isometry of the strategy's model into the register model of the ancilla model on $\mathbb{F}_2^{M \times t}$ (Definition [The register model](../../downstream-results/part-03/def-register-model.md)), which carries the strategy's state within $T$ of $|\textsc{EPR}_2\rangle^{\otimes Mt} \otimes \psi_{\textsc{aux}}$ and carries the first player's $X$ effects and the second player's $Z$ effects at the valid full-register answers within $T$ of the honest qubit readouts, in summed squared state norm. The valid answer at the qubit label $x$ is the Pauli answer at $\phi^{-1}(x)$, for the relabelling $\phi$ of Corollary [Theorem Pauli basis test / quantum low individual degree test on qubits](../../background-results/part-02/cor-qld-binary.md), and it projects back to $x$. In the tensor-product model of a strategy's state the test is sound with $\mathrm{val}^*$ (Lemma [The Pauli basis test is sound in the tensor-product model](../../downstream-results/part-04/lem-qld-sound-in-tensor.md)), the ancilla model is, up to isomorphism, the tensor-product model of an auxiliary unit vector, and the local isometry is one between tensor-product models: the familiar form of the extraction, for tensor-product strategies.

## Depends on

- [Restriction to the actual Pauli game](lem-intro-pauli-restriction.md)
- [The Pauli basis test is sound in a model](../../downstream-results/part-03/def-qld-sound-in.md)
- [The register model](../../downstream-results/part-03/def-register-model.md)
- [Projective strategy in a bipartite model](../../downstream-results/part-02/def-model-proj-strategy.md)
- [Theorem Pauli basis test / quantum low individual degree test on qubits](../../background-results/part-02/cor-qld-binary.md)

## Proof depends on

- [Operations on projective strategies](../../downstream-results/part-03/lem-model-proj-strategy.md)

## Proof

Restrict the strategy to the actual Pauli basis game (Lemma [Restriction to the actual Pauli game](lem-intro-pauli-restriction.md)): same model and state, failure at most $N\varepsilon$, and at a valid answer the same operators. The completion of the malformed answers carries no mass, the strategy having no malformed Pauli outcome, so the restriction's Pauli measurements are supported on the full-register answers too. Corollary [Theorem Pauli basis test / quantum low individual degree test on the valid answers](../../background-results/part-02/cor-qld-valid.md), at the restriction, gives an extraction in field coordinates at the error $\delta_{qld}(N\varepsilon, m, d, q)$, with an ancilla model that $\omega$ dominates, and Corollary [Theorem Pauli basis test / quantum low individual degree test on qubits](../../background-results/part-02/cor-qld-binary.md) relabels its register as qubits along the self-dual basis, at the same error. The valid answer at $x$ projects to $\phi(\phi^{-1}(x)) = x$. In Lean the extraction in binary coordinates is a structure (Corollary [Theorem Pauli basis test / quantum low individual degree test on qubits](../../background-results/part-02/cor-qld-binary.md)), and `exists_extraction` composes these steps.

## Lean

Formalized as [`MIPRE.Introspection.RestrictedSoundness.restriction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.RestrictedSoundness.restriction), [`MIPRE.Introspection.RestrictedSoundness.edgeCount`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.RestrictedSoundness.edgeCount), [`MIPRE.Introspection.RestrictedSoundness.edgeCount_one_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.RestrictedSoundness.edgeCount_one_le), [`MIPRE.Introspection.RestrictedSoundness.exists_extraction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.RestrictedSoundness.exists_extraction).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3539](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3539)
