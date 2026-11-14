---
declaration: corollary
origin: cited
lean: MIPRE.Introspection.RestrictedSoundness.binaryX, MIPRE.Introspection.RestrictedSoundness.binaryZ, MIPRE.Introspection.RestrictedSoundness.FieldExtraction.toBinary, MIPRE.Introspection.RestrictedSoundness.Extraction, MIPRE.Introspection.RestrictedSoundness.validAnswer, MIPRE.Introspection.RestrictedSoundness.project_validAnswer
statement: formalized
proof: formalized
---

# Theorem Pauli basis test / quantum low individual degree test on qubits

Let $q = 2^k$, let $\{e_1, \ldots, e_k\}$ be a self-dual basis of $\mathbb{F}_q$ over $\mathbb{F}_2$, and let $\phi : \mathbb{F}_q^M \to \mathbb{F}_2^{M \times k}$ be the relabelling of Lemma [Qudits are qubits, in characteristic two](../../foundations/part-02/lem-pauli-binary.md). Then Corollary [Theorem Pauli basis test / quantum low individual degree test on the valid answers](cor-qld-valid.md) holds with the same $\delta_{qld}$ and with the register $(\mathbb{C}^q)^{\otimes M}$ read as $M k$ qubits: the local isometry maps into the register model on $\mathbb{F}_2^{M \times k}$, item 1 compares with $|\textsc{EPR}_2\rangle^{\otimes Mk} \otimes |\textsc{aux}\rangle$, and in item 2 the honest measurement at the outcome $\phi(u)$, for the genuine answer $u$, is the qubit Pauli $X$ measurement $\sigma^X_{\phi(u)}$ for the first player and the computational-basis measurement $\sigma^Z_{\phi(u)}$ for the second. Indexed by the qubit label $x \in \mathbb{F}_2^{M \times k}$, the element of the strategy's measurement compared with the honest one at $x$ is its element at the *valid answer* $\phi^{-1}(x)$, the Pauli answer that the binary introspection game reads as $x$; this conclusion in binary coordinates is the form Lemma [Pauli extraction for the introspection game](../../structure-of-the-proof/part-05/lem-intro-pauli-extraction.md) consumes. The Lean proves it for a projective strategy in any bipartite model, the relabelling acting on the register of the ancilla model's register model after the local isometry; the statement above is its tensor-product instance.

## Depends on

- [Theorem Pauli basis test / quantum low individual degree test on the valid answers](cor-qld-valid.md)
- [Qudits are qubits, in characteristic two](../../foundations/part-02/lem-pauli-binary.md)

## Proof depends on

- [The register model](../../downstream-results/part-03/lem-register-model.md)

## Proof

The relabelling is a bijection of basis index sets, so the transport relabels the register of the register model, a local isometry carrying the state of one register model exactly to the state of the other (Lemma [The register model](../../downstream-results/part-03/lem-register-model.md)); composed after the extraction's local isometry it changes no quantity. The state error is unchanged, and the two error sums are reindexed along $\phi$: the $Z$ readouts are computational-basis projectors on both sides, and the $X$ readouts correspond by Lemma [Qudits are qubits, in characteristic two](../../foundations/part-02/lem-pauli-binary.md), which is where self-duality is used.

## Lean

Formalized as [`MIPRE.Introspection.RestrictedSoundness.binaryX`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.RestrictedSoundness.binaryX), [`MIPRE.Introspection.RestrictedSoundness.binaryZ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.RestrictedSoundness.binaryZ), [`MIPRE.Introspection.RestrictedSoundness.FieldExtraction.toBinary`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.RestrictedSoundness.FieldExtraction.toBinary), [`MIPRE.Introspection.RestrictedSoundness.Extraction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.RestrictedSoundness.Extraction), [`MIPRE.Introspection.RestrictedSoundness.validAnswer`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.RestrictedSoundness.validAnswer), [`MIPRE.Introspection.RestrictedSoundness.project_validAnswer`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.RestrictedSoundness.project_validAnswer).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 1892](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L1892)
