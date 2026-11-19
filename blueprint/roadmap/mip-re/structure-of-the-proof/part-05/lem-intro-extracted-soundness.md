---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.RestrictedSoundness.quantumValue_ge_of_extraction, MIPRE.Introspection.RestrictedSoundness.profileCoefficient, MIPRE.Introspection.RestrictedSoundness.profileCoefficient_one_le
statement: formalized
proof: formalized
---

# Introspection soundness from the extracted Pauli strategy

Suppose the original game's CL functions are exact on the whole Pauli register. Let a projective strategy of the binary parsed introspection game, in a bipartite model, fail with probability at most $\varepsilon$, and let its restriction to the Pauli basis game have an extraction in binary coordinates at an error $\delta \geq 0$ (Lemma [Pauli extraction for the introspection game](lem-intro-pauli-extraction.md)). Then every value model $\omega$ dominating the POVM strategies of the extraction's ancilla model (Definition [Domination of the POVM strategies, and approximation by projective strategies](../../downstream-results/part-03/def-povm-domination.md)) gives the original game value at least $1 - C\,\mathrm{root}_{6\ell+2}(\max(\varepsilon, \delta))$, with $C$ the coefficient of Lemma [Finite soundness from the valid-answer extraction interface](lem-intro-valid-isometric-soundness.md) at the $N$ ordered edges of the typed graph. In the tensor-product model, with $\omega = \mathrm{val}^*$, this bounds the quantum value of the original game. For $a \geq 1$ and $0 < b \leq 1$, the coefficient $A = \max\{1, C' a^r, ar\}$, where $r = 2^{-(6\ell+2)}$ and $C' = C\max(1, N^b)^r$, is at least $1$ and depends only on $\ell$, $a$ and $b$. It is the coefficient with which Lemma [Absorbing fixed introspection error losses](../part-03/lem-intro-error-absorption.md) turns this loss into the two-term profile $E(A, br, x, \varepsilon)$ of that lemma when $\delta \leq E(a, b, x, N\varepsilon)$ and $x \geq 1$, which is how Lemma [Full question transport and actual QLD extraction](../part-06/lem-intro-numbered-transport.md) absorbs the error of Theorem [Pauli basis test / quantum low individual degree test](../../background-results/part-01/thm-qld.md).

## Depends on

- [Pauli extraction for the introspection game](lem-intro-pauli-extraction.md)
- [Finite soundness from the valid-answer extraction interface](lem-intro-valid-isometric-soundness.md)
- [Domination of the POVM strategies, and approximation by projective strategies](../../downstream-results/part-03/def-povm-domination.md)

## Proof depends on

- [Restriction to the actual Pauli game](lem-intro-pauli-restriction.md)

## Proof

Lemma [Finite soundness from the valid-answer extraction interface](lem-intro-valid-isometric-soundness.md), applied to the strategy with the local isometry and the ancilla model of the extraction, at the common error $\max(\varepsilon, \delta)$. The Pauli question's sampler is constant, the valid answer at a register label projects back to that label, and at a valid answer the restriction's operators are the strategy's (Lemma [Restriction to the actual Pauli game](lem-intro-pauli-restriction.md)), so the extraction's estimates are the hypotheses of that lemma. The coefficient is a maximum of terms at least one.

## Lean

Formalized as [`MIPRE.Introspection.RestrictedSoundness.quantumValue_ge_of_extraction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.RestrictedSoundness.quantumValue_ge_of_extraction), [`MIPRE.Introspection.RestrictedSoundness.profileCoefficient`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.RestrictedSoundness.profileCoefficient), [`MIPRE.Introspection.RestrictedSoundness.profileCoefficient_one_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.RestrictedSoundness.profileCoefficient_one_le).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3598](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3598)
