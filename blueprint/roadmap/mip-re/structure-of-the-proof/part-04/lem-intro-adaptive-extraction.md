---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.stageRemaining_step, MIPRE.Introspection.prefixStageMarginalError_eq, MIPRE.Introspection.prefixStageCommutatorError_eq, MIPRE.Introspection.exists_adaptive_prefix_mixing, MIPRE.Introspection.transportedConditionalDilation_compress, MIPRE.Introspection.exists_adaptive_prefix_dilation, MIPRE.Introspection.adaptiveReplacement_distance
statement: formalized
proof: formalized
---

# Adaptive extraction and common-ancilla projectivization

Suppose the current residual measurements are projective and their three full-carrier marginal and commutator errors are at most $\varepsilon$, with $0\leq\varepsilon\leq1$. Using the actual prefix law and selected registers, mixing constructs residual POVMs with squared error at most $56\sqrt{\varepsilon}$. A single fixed ancillary alphabet suffices to produce residual PVMs and one ambient replacement measurement with squared error at most $2\sqrt{56\sqrt{\varepsilon}}$. Its residual support is exactly the next unvisited register.

## Depends on

- [Pauli mixing with a retained classical fibre](../part-02/lem-pauli-mixing.md)
- [Conditional projectivization on a common ancilla](lem-intro-conditional-dilation.md)
- [Concrete adaptive Z and dual-X factorization](lem-intro-adaptive-factorization.md)
- [Projective reassembly across adaptive prefixes](lem-intro-adaptive-reassembly.md)

## Proof

Apply the exact conditioning identities to ambient Pauli mixing. Dilate the constructed residual POVMs with one common fixed ancilla, apply the quantitative compression estimate, average square roots by concavity, and use the exact prefix reassembly and register reassociation.

## Lean

Formalized as [`MIPRE.Introspection.stageRemaining_step`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.stageRemaining_step), [`MIPRE.Introspection.prefixStageMarginalError_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.prefixStageMarginalError_eq), [`MIPRE.Introspection.prefixStageCommutatorError_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.prefixStageCommutatorError_eq), [`MIPRE.Introspection.exists_adaptive_prefix_mixing`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_adaptive_prefix_mixing), [`MIPRE.Introspection.transportedConditionalDilation_compress`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.transportedConditionalDilation_compress), [`MIPRE.Introspection.exists_adaptive_prefix_dilation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_adaptive_prefix_dilation), [`MIPRE.Introspection.adaptiveReplacement_distance`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.adaptiveReplacement_distance).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2699](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2699)
